$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.datepicker').datepicker({
      format: "dd mmm yyyy,",
      yearRange: 2,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
    });
    $('select').formSelect();
  });