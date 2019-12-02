# Django-blog
This is my pet-project, the purpose of which was - Demonstrate my skills and show that I am able to cope with the full development cycle.

### Features
- The project is written on the [Django Framework](https://www.djangoproject.com/ "Django Framework") v2.2.7.
- To create the dynamics of the site used a JQUERY & AJAX.
- The [TinyMCE](https://www.tiny.cloud/get-tiny "TinyMCE"), or rather the [django-tinymce](https://github.com/aljosa/django-tinymce "django-tinymce"), is used as an HTML editor for creating posts.
- Ajax-pagination of content using a [django-el-pagination](https://github.com/shtalinberg/django-el-pagination/tree/master "django-el-pagination-package") was introduced into the project.
- A [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms "django-crispy-forms") is used to simplify the styling of forms.

### QuickStart
You need a Python 3.6 and higher.
`git clone https://github.com/WhiteJamer/django_blog.git`
Install dependencies:
`pip install -r requirements.txt`
Set your db and run:
`python manage.py makemigrations`
`python manage.py migrate`
Run the dev server:
`python manage.py runserver`