$(document).ready(function(){
	$("#sendReq").click(function(){
		$.ajax({
				url : "/answer/sqroot",
				data : {answer : $("#answer").val()},
				method : "POST",
				success : function(response) {
					$("#response").html(response);
				}
			});
	});
});