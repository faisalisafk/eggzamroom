/*$( "#btnClick" ).click(function() {
  alert( "Handler for .click() called." );
});*/ //test for jquery run hoy kina

let total = $("#total").attr("value");

$('#pagination-demo').twbsPagination({
    totalPages: total,
    visiblePages: 6,
    next: 'Next',
    prev: 'Prev',
    onPageClick: function (event, page) {
        //fetch content and render here
        $('#page-content').text('Page ' + page) + ' content here';
    }
});