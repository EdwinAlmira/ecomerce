
/*Animación de dropdown*/
$('.dropdown').on('show.bs.dropdown', function(e){
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
  });

  $('.dropdown').on('hide.bs.dropdown', function(e){
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
  });


/*referencia para proceder a pagar por paypal*/
function comprar(){
		 window.location.assign('https://www.paypal.com/sv/webapps/mpp/home');
}

/*cancela pedido y redirreciona al catalogo de productos*/
function cancelar(){
		 window.location.assign('products.php');
}