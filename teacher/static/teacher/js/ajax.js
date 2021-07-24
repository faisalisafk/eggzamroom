$("#btnSave").click(function(){
    
    let ft = $('#form-title').val();
    let fd = $('#form-description').val();
    let csr = $("input[name=csrfmiddlewaretoken").val();
    const myData = {title:ft, description:fd };
    
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

    //getting questions
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

    
    //editing options
    $('.edit-choice').each(function(i, obj) {
        let optionId = $(this).data("id");
        let myOption = $(this).val();     
 
        const myOptionData = {optionId:optionId,myOption:myOption};

        $.ajax({
            cache : false,
            url: "editOption",
            method: "POST",
            headers: {'X-CSRFToken': csr},
            data: myOptionData,
            success: function(data){
                console.log("edited options")
            },
        });         

    });
    

})