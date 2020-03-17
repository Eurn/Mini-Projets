/*$(document).ready(function()
{
	$("#ajout-bouton").click(function(){
		var joueur = 
		{
			nom : $("#ajout-nom").val(),
			score : $("#ajout-score").val()
		}
		ajouter_joueur(joueur); 	
	});
	function ajouter_joueur(joueur){
		var ligne = $('<tr><td class="nom">'+joueur.nom+'</td><td class="score">'+joueur.score+'</td></tr>')
		$("#joueurs").append(ligne)
	}

});
CE CODE COMPORTE UN FAILLE XSS!!!!  ex: <script>alert('il y a une faille XSS ici')</script>
*/



$(document).ready(function()
{

	
	$('#ajout-bouton').click(function()
		{
			var joueur=
			{ 
				nom:   $('#ajout-nom'  ).val(),
				score: $('#ajout-score').val()
			};
			ajouter_joueur(joueur);
			$('#ajout-nom'	).val('');
			$('#ajout-score').val('');
			$('#total').text(calculer_total());
			$("#mediane").text(calculer_mediane())
		});

});

function ajouter_joueur(joueur)
{
	var ligne=$('<tr><td class="nom"></td><td class="score"></td></tr>');
	ligne.find(".nom"  ).text(joueur.nom  );
	ligne.find(".score").text(joueur.score);
	$('#joueurs').append(ligne);
}
function calculer_total()
{
	var total=0;
	// Pour chaque ligne du tableau .each() appelle la fonction.
	$('#joueurs tr').each(function()
		{
			// $(this) est la ligne (tr) ... 
			// on veut le texte dans la case avec le score
			var score=parseInt($(this).find('.score').text());
			// La variable "total" est définie dans la fonction calculer_total... 
			// mais on peut y accéder ici (fermeture)
			total+=score;
		});
	return total;
}
function calculer_mediane()
{
	var scores=[];
	$('#joueurs tr').each(function()
		{
			var s=parseInt($(this).find('.score').text());
			scores.push(s);
		});
	scores.sort(function(a,b){return a-b;});
	return scores[Math.floor(scores.length/2)];

}