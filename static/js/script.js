$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.datepicker').datepicker({
      format: "dd mm yyyy,",
      yearRange: 100,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
    });
    $('select').formSelect();
  });