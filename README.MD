# Django-blog
Это мой домашний проект, целью которого было - Продемострировать мои навыки и показать что я способен справляться с полным циклом разработки.

### Features
- Проект написан на [Django Framework](https://www.djangoproject.com/ "Django Framework") v2.2.7
- Для создания динамики на сайте использован Jquery & Ajax
- В качестве HTML-редактора для создания постов используется [TinyMCE](https://www.tiny.cloud/get-tiny "TinyMCE"), а точнее [django-tinymce](https://github.com/aljosa/django-tinymce "django-tinymce")
- В проект внедрена Ajax-пагинация контента с помощью [django-el-pagination](https://github.com/shtalinberg/django-el-pagination/tree/master "django-el-pagination-package") 
- Для упрощения стилизации форм используется [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms "django-crispy-forms")

### QuickStart
Вам нужен Python 3.6 и выше.
	
    git clone https://github.com/WhiteJamer/django_blog.git
В репозитории:


    pip install -r requirements.txt
Выберите базу данных и запустите:


    python manage.py makemigrations
    python manage.py migrate
Запустите дев-сервер:


    python manage.py runserver
