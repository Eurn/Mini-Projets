$(document).ready(function()
{
	$("#onglets-menu li").mousedown(function(){
		$(".menu-actif").removeClass();
		$(this).addClass("menu-actif");
		var num = $(this).index();
		$(".contenu-actif").removeClass();
		$("#onglets-contenu>div").eq(num).addClass("contenu-actif");
	});
});