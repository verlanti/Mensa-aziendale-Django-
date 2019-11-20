function countTotal() {
  var array = [];
  var checkboxes = document.querySelectorAll('input[type=checkbox]:checked');
  var total = 0;
  for (var i = 0; i < checkboxes.length; i++) {
    total = total + parseFloat(document.getElementById(checkboxes[i].value+'label').textContent);
  }

  $('#total').text(total);
}
