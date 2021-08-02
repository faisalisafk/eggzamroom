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

$(".choices").on('click','.remove-option',function(){

    let mcq_choice_id = $(this).data('id');
    let csr = $("input[name=csrfmiddlewaretoken").val();
    let temp = $(this);
    const context = {mcq_choice_id:mcq_choice_id}

    console.log(mcq_choice_id);

    $.ajax({
            cache : false,
            url: "deleteOption",
            method: "POST",
            headers: {'X-CSRFToken': csr},
            data: context,
            success: function(data){
                console.log("removed mcq choice");
                $(temp).parent().remove();
            },
        });
    
})


$(".starting").on('click', '.add-option', function(){


    let csr = $("input[name=csrfmiddlewaretoken").val();
    let mcq_question_id = $(this).data('question');

    //console.log(mcq_question_id);
    const context = {mcq_question_id:mcq_question_id};
    let par = $("#"+mcq_question_id+"");
    $.ajax({
            cache : false,
            url: "addOption",
            method: "POST",
            headers: {'X-CSRFToken': csr},
            data: context,
            success: function(data){

               $("#"+mcq_question_id).load(" #"+mcq_question_id);
                
                console.log("added option");
            },
        });
    //$(this).parent().remove();
})

$(".starting").on('click', '#add-question', function(){

    let csr = $("input[name=csrfmiddlewaretoken").val();


    $.ajax({
            cache : false,
            url: "addQuestion",
            method: "POST",
            headers: {'X-CSRFToken': csr},
            data: '',
            dataType:"json",
            success: function(data){
                console.log(data.newques);
                $(".someRandomDiv").load(" .someRandomDiv");
                //$("#"+data.newques).load(" #"+data.newques);
                //$("#question_div").load(document.URL + " #question_div");
            },
        }); 
    
    
})

//deleting questions
$("#question_div").on('click', '.btn-danger', function(){

    let csr = $("input[name=csrfmiddlewaretoken").val();
    let del_qid = $(this).data('id');
    const myDelData = {del_qid:del_qid};
    let temp = $(this);

    $.ajax({
        cache : false,
        url: "delQuestion",
        method: "POST",
        headers: {'X-CSRFToken': csr},
        data: myDelData,
        success: function(data){
            console.log("Deleted Question "+del_qid); 
            $(temp).fadeOut(200, function() {
                $(temp).parent().parent().parent().remove(); 
            }); 
                     
        },
    });
   // $(this).parent().parent().parent().remove();    
})