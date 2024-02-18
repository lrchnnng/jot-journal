$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.datepicker').datepicker({
      format: "dd mmm yyyy,",
      yearRange: 100,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
    });
    $('select').formSelect();
  });

  const year = document.querySelector('#current-year');
  year.innerHTML = new Date().getFullYear();