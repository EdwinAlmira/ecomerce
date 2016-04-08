/*Se oculta el elemento de objetos en el carrito*/
 var elem = document.getElementById('barranueva');
    elem.style.visibility = 'hidden';

 function getBuy(){
	 window.location.assign("/compra");
}

/*Aparece objetos en el carrito y boton comprar*/
$('.btn-hola-carrito').click(function() {
    $(this).toggleClass("btn-hola-carrito-active");
    var elem = document.getElementById('barranueva');
    elem.style.visibility = 'visible';
    document.getElementById("boton1").innerHTML = "Objetos en el carrito - 1";
});

/*Cambia la cantidad de objetos en el carrito*/
$('.btn-hola-carrito2').click(function() {
    $(this).toggleClass("btn-hola-carrito2-active");
    document.getElementById("boton1").innerHTML = "Objetos en el carrito - 2";
});