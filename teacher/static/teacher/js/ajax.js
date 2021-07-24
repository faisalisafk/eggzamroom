$("#btnSave").click(function(){
    console.log('clicked')
    let ft = $('#form-title').val();
    let fd = $('#form-description').val();
    let csr = $("input[name=csrfmiddlewaretoken").val();
    console.log(ft)
    console.log(fd)
    myData = {title:ft, description:fd };
 

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
        let myId = $(this).data("id");
        let myQuestion = $(this).val();
        let mark = $(markList[i]).val();
        
        console.log(mark)
        quesData = {myId:myId, myQuestion:myQuestion,mark:mark };
        
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

    
  
    

})