$(document).ready(function(){
    $.getJSON("euro.json", function(data){
        let lista = []
        for (let i=0; i<49; i++){
            lista.push(data[i].name)
        }
        $( function() {
            $( "#tags" ).autocomplete({
              source: lista
            });
          } );  
    }).fail(function(){
        console.log("An error has occurred.");
    });
});

$( function() {
    $( "#sortable" ).sortable({
      revert: true
    });
    $( "ul, li" ).disableSelection();
  } );

  $( function() {
    $( "#datepicker" ).datepicker({
      showWeek: true,
      firstDay: 1
    });
  } );

  $( function() {
    $( "#slider-range-min" ).slider({
      range: "min",
      value: 0,
      min: 0,
      max: 140,
      slide: function( event, ui ) {
        $( "#amount" ).val(ui.value + " years" );
      }
    });
    $( "#amount" ).val($( "#slider-range-min" ).slider( "value" ) );
  } );

