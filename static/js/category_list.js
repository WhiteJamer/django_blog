$(document).ready(function(){

	/* Обработчики запросов [CREATE, UPDATE, DELETE] 
		 для "category"
	*/

	// Модальное окно для подтверждения запросов
	var modal = $('#confirm-modal');
	
	// [AJAX update categories-section] Обновить секцию категорий при нажатии на кнопку
	$('#category-list').on('click', '.refresh', function(e){
		e.preventDefault();
		// Обновляем блок с категориями
		getCategories();
	});
	
	
	// [CREATE] Добавление категории
	$('#category-add-btn').on('click', function(e){
		e.preventDefault();
		let url = $(this).attr('href');
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
				alert('Шаблон модального окна не получен!');
			}
		});
	});	

	// [CREATE confirm] Подтверждение на добавление категории
	$(modal).on('submit', '#category-add-form', function(e){
		e.preventDefault();
		let form = $(this);
		$.ajax({
			type: 'POST',
			url: form.attr('action'),
			data: form.serialize(),
			success: function (data) {
				// Заполняем модальное окно нужным HTML
				modal.modal('hide');
				getCategories();
			},
			error: function(error) {
				console.log('Error: ' + error);
				alert('Шаблон модального окна не получен!');
			}
		});
	});

	// [DELETE] Удаление категории 
	$('#category-list').on('click', '.delete-btn', function(e){
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
				alert('Шаблон модального окна не получен!');
			}
		});
	});

	// [DELETE confirm] Подтверждение удаления
	$(modal).on('submit', '#category-delete-form', function(e){
		e.preventDefault();
		let form = $(this);
		$.ajax({
			type: form.attr('method'),
			url: form.attr('action'),
			data: form.serialize(),
			success: function (data) {
				modal.modal('hide');
				getCategories();
				console.log(form.serialize());
			},
			error: function(error) {
				console.log('Error: ' + error);
				alert('Произошла ошибка, категория не удалена!');
			}
		});
	  
		
	});
	

	// [UPDATE] Обновление категории
	$('#category-list').on('click', '.update-btn', function(e){
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
	$(modal).on('submit', '#category-update-form', function(e){
		e.preventDefault();
		let form = $(this);
		$.ajax({
			type: form.attr('method'),
			url: form.attr('action'),
			data: form.serialize(),
			success: function (data) {
				getCategories();
				modal.modal('hide');
			},
			error: function(error) {
				alert('Категория не обновлена!');
			}
		});
	});


	// [Get all categories function] Обновить секцию с категориями
	function getCategories(){
		$.ajax({
			type: 'GET',
			url: '/categories/',
			success: function (data) {
				$('#category-list').html(data);
			},
			error: function(error) {
				console.log('Error: ' + error);
				alert('Список категорий не получен!');
			}
		});
	}
});