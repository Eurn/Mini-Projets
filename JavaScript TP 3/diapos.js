/*$(document).ready(function()
{
	$("#dia-droite").click(function(){
		var position = parseInt($('#dia-images').css('left'));
		var x = position - 600
		if (position<=-600*3) {return;}
		$('#dia-images').css('left',x);
	})
	$("#dia-gauche").click(function(){
		var position = parseInt($('#dia-images').css('left'));
		var x = position + 600
		if (position >=0) {return;}
		$('#dia-images').css('left',x);
	})
	
});*/



/*$(document).ready(function()
{
	$("#dia-fleches span").click(function(){
		if ($(this).attr('id') == "dia-droite") {
			var position = parseInt($('#dia-images').css('left'));
			var x = position - 600;
			if (position<=-600*3) {return;}
			$('#dia-images').animate({'left': x});
		}else{
			var position = parseInt($('#dia-images').css('left'));
			var x = position + 600;
			if (position >=0) {return;}
			$('#dia-images').animate({'left': x});
		};
		
	})

}); PROBLEME SI ON SPAM
*/


/*$(document).ready(function()
{

	$('#dia-fleches span').mousedown(function()
		{
			var position=parseInt($('#dia-images').css('left'));
			if(position%600!==0){return;}
			var flecheDroite=$(this).attr('id')==='dia-droite';
			position+=(flecheDroite ? -600 : 600);
			if(position<-600*3 || position>0){return;}
			$('#dia-images').animate({left: position});
		});
	
});FONCTIONNEL
*/


$(document).ready(function(){

	var test = setInterval(function(){
		var position=parseInt($('#dia-images').css('left'));
		if(position%600!==0){return;}
		position-=600;
		if(position<-600*3){position = 0;}
		$('#dia-images').animate({left: position});



		
	},2000);

	$('#dia-fleches span').mousedown(function(){
		if(test!==false)
			{
				clearInterval(test);
				test=false;
			}
			var position=parseInt($('#dia-images').css('left'));
			if(position%600!==0){return;}
			var flecheDroite=$(this).attr('id')==='dia-droite';
			position+=(flecheDroite ? -600 : 600);
			if(position<-600*3 || position>0){return;}
			$('#dia-images').animate({left: position});
		});
});