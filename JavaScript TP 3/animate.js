$(document).ready(function()
{
	var options=
	{
		top :500,
		left :500,
		opacity :0,
		width : 400,
		padding : 80,
		"border-radius" : 100
	};
	var options2=
	{
		top :0,
		left :0,
		opacity :1,
		width : 200,
		padding : 20,
		"border-radius" : 0
	};

	$("h1").mousedown(function(){
		$("h1").animate(options,1000, function(){
			$("h1").animate(options2,1000);
		});
	})
});