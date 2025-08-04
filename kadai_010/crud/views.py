from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy


class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 3

class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    fields = '__all__'


class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'


class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('list')


    class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
   

