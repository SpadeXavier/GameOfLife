$(document).ready(function(){

    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();



    $(".collapsible-header").click(function() {
    	$('form').fadeToggle();
    	$('.grid-size-option').fadeToggle();
    })


});
