/*$( "#btnClick" ).click(function() {
  alert( "Handler for .click() called." );
});*/ //test for jquery run hoy kina
let csr = $("input[name=csrfmiddlewaretoken").val();
let total = $("#total").attr("value");

$('#pagination-demo').twbsPagination({
    totalPages: total,
    visiblePages: total,
    next: 'Next',
    prev: 'Prev',
    onPageClick: function (event, page) {
        window.value = page;
        //fetch content and render here
        $('#page-content').text('Page ' + page) + ' content here';
        //$("#"+page).removeAttribute("hidden");
        HideQuestions();
        ShowQuestion(page);
    }
});

function HideQuestions(){
    for(let i = 1; i <= total; i++)
    {
        $("#"+i).hide();
        //console.log(i);
    }
}

function ShowQuestion(x){
    $("#"+x).show();
}


$("input").click(function() {
    
    optionChecked = $(this).val();
    questionId = $(this).attr('name');
    //let quesNo = $(this).parent().parent().parent().attr('id');
    console.log(window.value);
    console.log(optionChecked)
    console.log(questionId)
    const myData = {optionChecked:optionChecked,questionId:questionId };

    $.ajax({
        cache : false,
        url: "saveAnswer",
        method: "POST",
        headers: {'X-CSRFToken': csr},
        data: myData,
        success: function(data){
            console.log("well");
        },
    });

 });