/*$( "#btnClick" ).click(function() {
  alert( "Handler for .click() called." );
});*/ //test for jquery run hoy kina

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
    
    console.log("Choice key - ",$(this).val());
    console.log($(this).attr('name'));
    //let quesNo = $(this).parent().parent().parent().attr('id');
    console.log(window.value);


 });