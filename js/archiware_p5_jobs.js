

var formatNewLines = function ( nRow ) {
  var celldata=$('td:eq(2)', nRow).text();
  $('td:eq(2)', nRow).html(celldata.replace(/\n/g, "<br>").replace(/\r/g, "<br>"));
}




