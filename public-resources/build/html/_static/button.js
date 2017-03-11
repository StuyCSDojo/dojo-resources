$(document).ready(function(){
    $.getJSON('/logged_in', {},
	      function(data){
		  var is_logged_in = JSON.parse(data.result);
		  if (is_logged_in){
		      var button_form = document.getElementById('button_form');
		      button_form.innerHTML = '<button class="button"><span>Logout</span><span class="glyphicon glyphicon-log-out"></span></button>'
		  }
	      });
});
















