$(document).ready(function(){
	var basic = $('#resizer').croppie({
			enableExif: true,
	    viewport: {
	        width: 200,
	        height: 200
	    },
	    boundary: {
	        width: 300,
	        height: 300
	    }
	});
	$('#resizer').hide();
	$('input[type=file]').on('change', function(){
		$('#resizer').show();
		if(this.files[0]){
			var filename = this.files[0].name;
			var reader = new FileReader();
			var formdata = new FormData();
			reader.onload = function(event){
				basic.croppie('bind', {
					url: event.target.result,
					points: [77,469,280,739],
				}).then(function(){
					console.log('Bind complete');
				});

			}
			reader.readAsDataURL(this.files[0]);
			$('form#image-upload').submit(function(e){
				e.preventDefault();
				basic.croppie('result', 'base64').then(function(base64){
					var uploadImageForm = $('#image-upload');
					$.ajax({
						type: uploadImageForm.attr('method'),
						url: uploadImageForm.attr('action'),
						data: {'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
									'avatar':base64,
									'filename': filename},
						success: function (data) {
							console.log(data);
							$('#profile-avatar').css('backgroundImage',`url(${data.avatar_path})`);
							$('.comment-avatar').css('backgroundImage',`url(${data.avatar_path})`);
							$('#av-ed-modal').modal('hide');

						},
						error: function(error) {
							console.log('Error: ' + error);
						}
					});
				});
			});
		}
	});
	
});