var modal = document.getElementById("myModal");
function Modal() {
  var personaje = event.target.id;
  fetch('http://superstock.herokuapp.com/api/superhumanos')
  .then((respuesta) => {return respuesta.json();}).then((respuesta) => {
    for (const index of respuesta) {
      if (index.personaje_nombre === personaje) {
        document.getElementById("myModal").innerHTML =+ 
          "<div id='myModal' class='modal'>"+
            "<div class='modal-content'>"+
              "<span class='close' onclick='Close()'>&times;</span>"+
              "<div>"+
                  "<h1>"+index.personaje_nombre+"</h1>"+
                  "<h2>"+index.personaje_descripcion+"</h2>"+
                  "<h3>"+index.franquicia+"</h3>"+
                  "<img src='"+"https://static0.cbrimages.com/wordpress/wp-content/uploads/2019/11/dc-10-rarest-batman-comics-what-theyre-worth.jpg"+"' alt=''>"+
                  //"<img src='"+index.personaje_imagen+"' alt=>"+
              "</div>"+
            "</div>"+
          "</div>";
        //alert(personaje);
        modal.style.display = "block";
      }
    }   
  });
};

function Close() {
  modal.style.display = "none";
};

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};