$(document).ready(function() {
   $('.carousel').carousel({
		interval:4000
	});
	$(".typed h3").typed({
		strings: ["Mejores herramientas","Servicios personalizados","Seguridad empresarial"],
		typeSpeed: 100,
		backDelay: 1500, 
		loop:true
	});
});