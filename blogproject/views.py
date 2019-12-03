from django.shortcuts import redirect, reverse

def index(request):
    response = redirect(reverse('postmanager:post_list'))
    return response