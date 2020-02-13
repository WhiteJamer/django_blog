# Django-blog
Это мой домашний проект, целью которого было - Продемострировать мои навыки и показать что я способен справляться с полным циклом разработки.
### Features
- Проект написан на [Django Framework](https://www.djangoproject.com/ "Django Framework") v2.2.7
- Для создания динамики на сайте использован Jquery & Ajax
- В качестве HTML-редактора для создания постов используется [TinyMCE](https://www.tiny.cloud/get-tiny "TinyMCE"), а точнее [django-tinymce](https://github.com/aljosa/django-tinymce "django-tinymce")
- В проект внедрена Ajax-пагинация контента с помощью [django-el-pagination](https://github.com/shtalinberg/django-el-pagination/tree/master "django-el-pagination-package") 
- Для упрощения стилизации форм используется [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms "django-crispy-forms")
- 


### QuickStart
Скачайте проект и установите [Docker](https://docs.docker.com/install/) и [docker-compose](https://docs.docker.com/compose/install/)
	
    git clone https://github.com/WhiteJamer/django_blog.git

Находясь в папке с проектом введите:

		docker-compose up --build

Теперь локальный сервер запущен и вы видите логи базы данных и вашего приложения.

Чтобы вводить комманды внутри вашего приложения откройте bash-консоль внутри с помощью комманды:

		docker-compose exec web bash 

Или можно просто вводить их не проникая в контейнер, например так:
		
		docker-compose exec python manage.py makemigrations



    
    
![Users list photo](https://i.imgur.com/6Z9dDDs.png)
![Update page photo](https://i.imgur.com/FkKq5b6.png)
![Categories list photo](https://i.imgur.com/L4Ndc3L.png)
![Posts list photo](https://i.imgur.com/dLePR97.png)

