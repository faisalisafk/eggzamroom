$('#btn-edit').click(function(){
    let questionId = $(this).data("data-id");
    console.log(questionId)
    $("#editSubmit").attr("data-id", questionId);



    $('editSubmit').click(function(){
    let questionId = $(this).data("data-id");
    let csr = $("input[name=csrfmiddlewaretoken]").val();
    let title = $("#title").val();
    let subject = $("#subject").val();


    data = {courseId:questionId, csrfmiddlewaretoken: csr, title: title, subject: subject};

    $.ajax({
    url: "{% url 'editCourse' %}",
    method: "POST",
    data: data,
    dataType: "json",
    success:function(data){
    console.log(data)
    },

    });

    });


});


