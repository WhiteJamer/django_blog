$(document).ready(function(){
	$('#category-list').on('click','.category-delete-btn', function(e){
		e.preventDefault();
		var category = this.closest('.card');
		var categorySlug = $(this).attr("categoryslug");
		var categoryName = $(this).attr("categoryname");
		console.log(categorySlug);
		console.log(categoryName);

		var modal = $('#category-delete-modal');
		var csrf = $('input[name=csrfmiddlewaretoken]').val();
		$('#modal-category-title').html(categoryName);	
		modal.modal('show');
		$('#confirm-delete-category').on('click', function(e){
			e.preventDefault();
			$.ajax({
				type: 'POST',
				url: `/categories/${categorySlug}/delete/`,
				data: {'csrfmiddlewaretoken':csrf},
				success: function (data) {
					console.log(data);
					modal.modal('hide');
					category.remove();
				},
				error: function(error) {
					console.log('Error: ' + error);
				}
			});
		});
	});

	$('#category-list').on('click','.category-update-btn', function(e){
		e.preventDefault();
		var categoryItem = $(this).closest('.card');
		var categorySlug = $(this).attr("categoryslug");
		var categoryName = $(this).attr("categoryname");
		console.log(categorySlug);
		console.log(categoryName);

		var modal = $('#category-update-modal');
		var csrf = $('input[name=csrfmiddlewaretoken]').val();
		$('#modal-category-title').html(categoryName);

		var categoryNameInput = $('input[name=categoryNameInput]');
		categoryNameInput.val(categoryName);

		modal.modal('show');
		$('#confirm-update-category').on('click', function(e){
			e.preventDefault();
			$.ajax({
				type: 'POST',
				url: `/categories/${categorySlug}/edit/`,
				data: {'csrfmiddlewaretoken':csrf, 'categoryName':categoryNameInput.val()},
				success: function (data) {
					console.log(data);
					modal.modal('hide');
					categoryItem.find(".card-title a").html(categoryNameInput.val());
				},
				error: function(error) {
					console.log('Error: ' + error);
				}
			});
		});
	});

});