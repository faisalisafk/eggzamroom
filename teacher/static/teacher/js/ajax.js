$("#btnSave").click(function(){
    
    let ft = $('#form-title').val();
    let fd = $('#form-description').val();
    let csr = $("input[name=csrfmiddlewaretoken").val();
    const myData = {title:ft, description:fd };
    
    //only form title and description
    $.ajax({
        cache : false,
        url: "saveForm",
        method: "POST",
        headers: {'X-CSRFToken': csr},
        data: myData,
        success: function(data){
            console.log("Saved title and description")
        },
    });

    //setting questions title and mark
    let markList = $('.required-checkbox');
    $('.input-question').each(function(i, obj) {
        let quesId = $(this).data("id");
        let myQuestion = $(this).val();
        let mark = $(markList[i]).val();
        
        const quesData = {quesId:quesId, myQuestion:myQuestion,mark:mark };
        
        $.ajax({
            cache : false,
            url: "saveQuestion",
            method: "POST",
            headers: {'X-CSRFToken': csr},
            data: quesData,
            success: function(data){
                console.log("saved question")
            },
        });

    });

    
    //editing options value and checking answers

    $('.choice').each(function(i, obj) {       
    
        let optionId = $(this).find(".edit-choice").data("id");
        let myOption = $(this).find(".edit-choice").val(); 
        let isChecked = $(this).find("input").prop('checked');

        const myOptionData = {optionId:optionId,myOption:myOption,isChecked:isChecked};

        $.ajax({
            cache : false,
            url: "editOption",
            method: "POST",
            headers: {'X-CSRFToken': csr},
            data: myOptionData,
            success: function(data){
                console.log("saved options")
            },
        });
             

    });
    

})

$(".choices").on('click', '.remove-option', function(){

    let mcq_choice_id = $(this).data('id');
    let csr = $("input[name=csrfmiddlewaretoken").val();

    const context = {mcq_choice_id:mcq_choice_id}

    console.log(mcq_choice_id);

    $.ajax({
            cache : false,
            url: "deleteOption",
            method: "POST",
            headers: {'X-CSRFToken': csr},
            data: context,
            success: function(data){
                console.log("saved options")
            },
        });
    $(this).parent().remove();
})


$(".choices").on('click', '.choice-add', function(){



    /*let html_string_for_adding = <input type="radio" data-id="{{choice.id}}" name="{{question.id}}" {% if choice.is_answer %}checked{% endif %} >
                        <label for="{{choice.id}}">
                            <input type="text" value="{{choice.question_choice}}" class="edit-choice" data-id="{{choice.id}}">
                        </label>
                        <span class="remove-option" title="Remove" data-id="{{choice.id}}">&times;</span> */






        $(this).append(
        $('<input>', {
            type: 'text',
            val: 'dummy option'
          })
        );
    let csr = $("input[name=csrfmiddlewaretoken").val();

    //const context = {mcq_choice_id:mcq_choice_id}

    console.log("working");

    /*$.ajax({
            cache : false,
            url: "deleteOption",
            method: "POST",
            headers: {'X-CSRFToken': csr},
            data: context,
            success: function(data){
                console.log("saved options")
            },
        }); */
    //$(this).parent().remove();
})