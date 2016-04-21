$(document).ready(function(){


  $(".submenu > a").click(function(e) {
    e.preventDefault();
    var $li = $(this).parent("li");
    var $ul = $(this).next("ul");

    if($li.hasClass("open")) {
      $ul.slideUp(350);
      $li.removeClass("open");
    } else {
      $(".nav > li > ul").slideUp(350);
      $(".nav > li").removeClass("open");
      $ul.slideDown(350);
      $li.addClass("open");
    }
  });
  $(".modificar").css("display","none");
  
});

function prueba(pk, nombre){
    
    $(".modificar").css("display","block");
    $(".modificar").find("input").val(nombre);
    $('form').attr('action', "/dashboard/categoria/editar/"+pk+"/"); //this fails silently
  } 
function loadimg(img){

  $(".loadimg").attr("src","/media/"+img+"").load();

}
  
