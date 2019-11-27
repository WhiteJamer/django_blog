$(document).ready(function(){
	$('#post-list').on('click','.post-delete-btn', function(){
		var post = this.closest('.card');
		var postSlug = $(this).attr("postslug");
		var postTitle = $(this).attr("posttitle");
		console.log(postSlug);
		console.log(postTitle);

		var modal = $('#post-delete-modal');
		var csrf = $('input[name=csrfmiddlewaretoken]').val();
		$('#modal-post-title').html(postTitle);	
		modal.modal('show');
		$('#confirm-delete-post').on('click', function(e){
			e.preventDefault();
			$.ajax({
				type: 'POST',
				url: `/posts/${postSlug}/delete`,
				data: {'csrfmiddlewaretoken':csrf},
				success: function (data) {
					console.log(data);
					modal.modal('hide');
					post.remove();
				},
				error: function(error) {
					console.log('Error: ' + error);
				}
			});
		});


		
	});
});