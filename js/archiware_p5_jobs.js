var formatArchiware_p5NewLines = function ( col, row ) {
  // Get cell data and cell position, and make it into variables `cell` and `value`
  var cell = $('td:eq('+col+')', row),
      value = cell.text();
  // Process contents of variable `value`
  value = value.replace(/\n/g, "<br>").replace(/\r/g, "<br>");
  // Output new variable `value` to cell
  cell.html(value)
}







