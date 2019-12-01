from .models import Category
from .forms import CategoryForm
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from el_pagination.views import AjaxListView
from django.http import JsonResponse, HttpResponse
import time


class CategoryCreate(View):

    @method_decorator(login_required)
    def get(self, request):
        form = CategoryForm
        context = {'form': form}
        return render(request, 'categorymanager/includes/category_add_modal.html', context)

    @method_decorator(login_required)
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            data = {'data': 'Category has been created'}
            return JsonResponse(data)
        else:
            data = {'data': 'Form is not valid!'}
            return JsonResponse(data)


class CategoryDetail(View):
    def get(self, request, slug):
        category = Category.objects.get(slug__iexact=slug)
        return render(request, 'categorymanager/category_item.html', context={'category': category})


class CategoryList(View):

    def get(self, request):
        categories = Category.objects.all()

        if request.is_ajax():
            return render(request, 'categorymanager/includes/category_list_page.html',
                          context={'categories': categories})

        else:
            return render(request, 'categorymanager/category_list.html',
                          context={'categories': categories})


class CategoryUpdate(View):

    @method_decorator(login_required)
    def get(self, request, slug):
        category = Category.objects.get(slug__iexact=slug)
        form = CategoryForm(instance=category)
        context = {'category':category,'form': form}
        return render(request, 'categorymanager/includes/category_update_modal.html', context)

    @method_decorator(login_required)
    def post(self, request, slug):
        if request.user.is_staff:
            category = Category.objects.get(slug__iexact=slug)
            form = CategoryForm(request.POST, instance=category)
            form.save()
            data = {'info': 'Category has been updated'}
            return JsonResponse(data)
        else:
            data = {'info': 'You is not staff'}
            return JsonResponse(data)


class CategoryDelete(View):

    @method_decorator(login_required)
    def get(self, request, slug):
        if request.user.is_staff:
            category = Category.objects.get(slug__iexact=slug)
            return render(request, 'categorymanager/includes/category_delete_modal.html', {'category': category})
        else:
            data = {'info': 'You is not staff'}
            return JsonResponse(data)

    @method_decorator(login_required)
    def post(self, request, slug):
        category = Category.objects.get(slug__iexact=slug)
        if request.user.is_staff:
            category.delete()
            data = {'info': 'Category has been deleted'}
            return JsonResponse(data)
        else:
            data = {'info': 'You is not staff'}
            return JsonResponse(data)
