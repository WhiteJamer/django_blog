from .models import Category
from .forms import  CategoryForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from el_pagination.views import AjaxListView
from django.http import JsonResponse


class CategoryCreate(View):

    @method_decorator(login_required)
    def get(self, request):
        form = CategoryForm
        context = {'form': form}
        return render(request, 'categorymanager/category_add_form.html', context)

    @method_decorator(login_required)
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = Category.objects.create(
                name=form.cleaned_data['name']
            )
            new_category.save()
            return redirect(new_category)
        return redirect(reverse_lazy('categorymanager:category_create'))


class CategoryList(AjaxListView):
    model = Category
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'


class CategoryUpdate(View):

    @method_decorator(login_required)
    def post(self, request, slug):
        category = Category.objects.get(slug__iexact=slug)
        if request.user.is_staff:
            category.name = request.POST.get('categoryName')
            category.save()
            data = {'info':'Category has been updated'}
            return JsonResponse(data)
        else:
            data = {'info': 'You is not staff'}
            return JsonResponse(data)


class CategoryDelete(View):

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


