$(document).ready(function(){
	getComments();
	/* Обработчики запросов [CREATE, UPDATE, DELETE] 
		 для "comment"
	*/

	// Модальное окно для подтверждения запросов
	var modal = $('#confirm-modal');
	
	// [AJAX update comments-section] Обновить секцию категорий при нажатии на кнопку
	$('#comment-list').on('click', '.refresh', function(e){
		e.preventDefault();
		// Обновляем блок с категориями
		getComments();
	});
	
	
	// [CREATE] Добавление категории
	$('#add_comment_form').on('submit', function(e){
		e.preventDefault();
		let form = $(this);
		$.ajax({
			type: form.attr('method'),
			url: form.attr('action'),
			data: form.serialize(),
			success: function (modalData) {
				form[0].reset();
				getComments();
			},
			error: function(error) {
				console.log('Error: ' + error);
				alert('Modal template not loaded!');
			}
		});
	});	

	// [CREATE confirm] Подтверждение на добавление категории
	$(modal).on('submit', '#comment-add-form', function(e){
		e.preventDefault();
		let form = $(this);
		$.ajax({
			type: 'POST',
			url: form.attr('action'),
			data: form.serialize(),
			success: function (data) {
				// Заполняем модальное окно нужным HTML
				modal.modal('hide');
				getComments();
			},
			error: function(error) {
				console.log('Error: ' + error);
				alert('Modal template not loaded!');
			}
		});
	});

	// [DELETE] Удаление категории 
	$('#comment-list').on('click', '.delete-btn', function(e){
		e.preventDefault();
		let url = $(this).attr('data-url')
		// Подгружаем в модальное окно DeleteConfirm-шаблон
		$.ajax({
			type: 'GET',
			url: `${url}`,
			success: function (modalData) {
				// Заполняем модальное окно нужным HTML
				modal.html(modalData);
				modal.modal('show');
			},
			error: function(error) {
				console.log('Error: ' + error);
				alert('Modal template not loaded!');
			}
		});
	});

	// [DELETE confirm] Подтверждение удаления
	$(modal).on('submit', '#comment-delete-form', function(e){
		e.preventDefault();
		let form = $(this);
		$.ajax({
			type: form.attr('method'),
			url: form.attr('action'),
			data: form.serialize(),
			success: function (data) {
				modal.modal('hide');
				getComments();
				console.log(form.serialize());
			},
			error: function(error) {
				console.log('Error: ' + error);
				alert('Произошла ошибка, категория не удалена!');
			}
		});
	  
		
	});
	

	// [UPDATE] Обновление категории
	$('#comment-list').on('click', '.update-btn', function(e){
		e.preventDefault();
		let url = $(this).attr('data-url');
		// Подгружаем в модальное окно UpdateConfirm-шаблон
		$.ajax({
			type: 'GET',
			url: `${url}`,
			success: function (modalData) {
				modal.html(modalData);
				modal.modal('show');
			},
			error: function(error) {
				alert('Шаблон модального окна не получен')
			}
		});
	});
	
	// [UPDATE confirm] Подтверждение обновления
	$(modal).on('submit', '#comment-update-form', function(e){
		e.preventDefault();
		let form = $(this);
		$.ajax({
			type: form.attr('method'),
			url: form.attr('action'),
			data: form.serialize(),
			success: function (data) {
				getComments();
				modal.modal('hide');
			},
			error: function(error) {
				alert('Категория не обновлена!');
			}
		});
	});


	// [Get all comments function] Обновить секцию с категориями
	function getComments(){
		let postslug = $('input[name=postslug]').val();
		$.ajax({
			type: 'GET',
			url: `/comments/${postslug}/`,
			success: function (data) {
				$('#comment-list').html(data);
			},
			error: function(error) {
				console.log('Error: ' + error);
				alert('Список категорий не получен!');
			}
		});
	}
});