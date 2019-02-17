$(document).ready(function(){
	$('#msg').focus();
	$.ajax({
		url: '/test',
		data: 'testdata',
		success: function(data){
			$('h1').text(data);
		},
		error: function(a, b, c){
			$('h1').apend('p').text(a + '<br>' + b + '<br>' + c);
		}
	});
	
	$('#send').click(function(event){
		event.preventDefault();
		var msg = $('#msg').val();
		if(msg != ''){
			$('#area').append($('<div></div>').attr('id', 'hum').text(msg));
			$('#msg').val('');
			var m = {mg: msg};
			$.ajax({
				url: '/post',
				type: 'POST',
				contentType: 'application/json;charset=UTF-8',
				data: JSON.stringify(m),
				success: function(btm){
					$('#area').append($('<div></div>').attr('id', 'bot').text(btm.msg));
				}
			});
		}
	});
	
});
