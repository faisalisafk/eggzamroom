$("#btnSave").click(function(){
    console.log('clicked')
    let ft = $('#form-title').val();
    let fd = $('#form-description').val();
    let csr = $("input[name=csrfmiddlewaretoken").val();
    console.log(ft)
    console.log(fd)
    myFormData = {title:ft, description:fd,csrfmiddlewaretoken: csr };
 

    $.ajax({
        url: "save",
        method: "POST",
        data : myFormData,
        success: function(data){
            console.log(data)
        },
    });
})