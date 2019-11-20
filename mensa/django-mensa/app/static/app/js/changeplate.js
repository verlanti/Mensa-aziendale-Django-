function checkprice() {
      var price =  document.getElementById("id_price").value;

      if(price<0 ){
          alert("Errore: Il prezzo non puo' essere negativo");
          return false;
      }

      alert("Piatto cambiato correttamente");
      return true;
  }
