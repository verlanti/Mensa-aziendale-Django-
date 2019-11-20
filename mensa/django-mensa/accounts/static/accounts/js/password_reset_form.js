
function checkemail() {
      var email =  document.getElementById("id_email").value;
      var email_user =  document.getElementById("email_user").value;
  
      if(email != email_user){
          alert("Errore: Email non valida");
          return false;
      }


      return true;
  }
