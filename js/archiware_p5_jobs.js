

var formatNewLines = function ( col, row ) {
  // Get cell data and cell position, and make it into variables `cell` and `value`
  alert("here");
  var cell = $('td:eq('+col+')', row);
  var value = cell.text();
  // Process contents of variable `value`
  var newValue = value.replace(/\n/g, "<br>").replace(/\r/g, "<br>");
  // Output new variable `value` to cell
  cell.html(newValue)
}


