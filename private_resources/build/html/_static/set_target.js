$(document).ready(function() {
    var h1_tags = document.getElementsByTagName('h1');
    console.log(h1_tags[0].textContent);
    if (h1_tags[0].textContent.indexOf('Welcome to Dojo Resources!') > -1){
	console.log("Index Page!");
	$("a[href^='http']").attr('target','_blank');	
    };    
});
