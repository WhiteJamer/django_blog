$(document).ready(function(){
	$('#comment-list').on('click','.comment-delete-btn', function(){
		var comment = this.closest('.card');
		var commentId = $(this).attr("commentid");
		var commentBody = $(this).attr("commentbody");
		console.log(commentId);
		console.log(commentBody);

		var modal = $('#comment-delete-modal');
		var csrf = $('input[name=csrfmiddlewaretoken]').val();
		$('#modal-comment-title').html(commentBody);	
		modal.modal('show');
		$('#confirm-delete-comment').on('click', function(e){
			e.preventDefault();
			$.ajax({
				type: 'POST',
				url: `/comments/${commentId}/delete`,
				data: {'csrfmiddlewaretoken':csrf},
				success: function (data) {
					console.log(data);
					modal.modal('hide');
					comment.remove();
				},
				error: function(error) {
					console.log('Error: ' + error);
				}
			});
		});


		
	});
});