$(document).ready(function(){
  $('#id_new_password1').keyup(updateCount);
  $('#id_new_password1').keydown(updateCount);

  $('#id_new_password2').keyup(updateCount2);
  $('#id_new_password2').keydown(updateCount2);


  function updateCount() {
        var cs = $(this).val().length;
        $('#characters').text(cs);
    }

    function updateCount2() {
          var cs = $(this).val().length;
          $('#characters2').text(cs);
      }



});


function checkpassword() {
    var valid = true;
    var pass1 =  document.getElementById("id_new_password1").value;
    var len_pass1 = $('#id_new_password1').val().length;
    var pass2 = document.getElementById("id_new_password2").value;

    if(pass1 != pass2 ){
      //  document.getElementById("helptext").innerHTML = "Le due password non coincidono";
      alert("Errore: Le due password non coincidono")
        valid = false;
    }
    if(len_pass1 < 8 ){

      //document.getElementById("helptext").innerHTML = "La tua password deve contenere almeno 8 caratteri.";
      alert("Errore: La tua password deve contenere almeno 8 caratteri.")
      valid=false;
    }
    if (valid == false){
      return false;
    }
  //  document.getElementById("helptext").innerHTML = "";
    return true;
}
