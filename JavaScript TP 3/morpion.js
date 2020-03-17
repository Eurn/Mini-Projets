$(document).ready(function()
{
	var joueur = "X"
	$("#morpion td").mousedown(function(){
		if ($(this).text() == ""){
			if (joueur == "X") {
				$(this).text(joueur);
				joueur = "O";
			}else{
				$(this).text(joueur);
				joueur = "X";
			}
		}else{
			return;
		}
		
	});
});