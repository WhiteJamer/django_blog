from .models import Category
from .forms import  CategoryForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required


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


class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    paginate_by = 10


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'


class CategoryUpdate(View):

    @method_decorator(login_required)
    def get(self, request, slug):
        category = get_object_or_404(slug_iexact=slug)
        form = CategoryForm(instance=category)
        context = {'form': form}
        return render(request, 'categorymanager/category_update_form', context)

    @method_decorator(login_required)
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
class CategoryDelete(View):
    @method_decorator(login_required)
    def post(self, request, slug):
        category = get_object_or_404(slug_iexact=slug)
        category.delete()
        return redirect(reverse_lazy('categorymanager:category_list'))


