let csr = $("input[name=csrfmiddlewaretoken").val();

//save form title
$("#form-title").change(function(){

    let ft = $('#form-title').val();
    let fd = $('#form-description').val();
    
    const myData = {title:ft};
    $.ajax({
        cache : false,
        url: "saveFormTitle",
        method: "POST",
        headers: {'X-CSRFToken': csr},
        data: myData,
        success: function(data){
            console.log("Title saved");
        },
    });   
});

//save form description
$("#form-description").change(function(){

    let fd = $('#form-description').val();
    
    const myData = {description:fd };
    $.ajax({
        cache : false,
        url: "saveFormDes",
        method: "POST",
        headers: {'X-CSRFToken': csr},
        data: myData,
        success: function(data){
            console.log("Description saved");
        },
    });   
});


//save question title
$(".starting").on('change','.input-question',function(i,obj){  
        let quesId = $(this).data("id");
        let myQuestion = $(this).val();

        const quesData = {quesId:quesId, myQuestion:myQuestion };
        
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

//save question mark
$(".starting").on('change','.required-checkbox',function(i,obj){  

    let quesId = $(this).data("id");
    let mark = $(this).val();

    const quesData = {quesId:quesId, mark:mark };
    
    $.ajax({
        cache : false,
        url: "saveMark",
        method: "POST",
        headers: {'X-CSRFToken': csr},
        data: quesData,
        success: function(data){
            console.log("saved marks")
        },
    });    

});

//save choice name and answer
$(".starting").on('change','.choice',function(){   
    
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

//remove choices
$(".starting").on('click','.remove-option',function(){

    let mcq_choice_id = $(this).data('id');
    
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

//add new choice
$(".starting").on('click', '.add-option', function(){


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

//add new questions
$(".starting").on('click', '#add-question', function(){

  
    $.ajax({
            cache : false,
            url: "addQuestion",
            method: "POST",
            headers: {'X-CSRFToken': csr},
            data: '',
            dataType:"json",
            success: function(data){
                console.log(data.newques);
                
                //$("#"+data.newques).load(" #"+data.newques);
                $(".starting").load(document.URL + " .starting");
            },
        }); 
    
    
})

//deleting questions
$("#question_div").on('click', '.btn-danger', function(){

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