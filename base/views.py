from django.shortcuts import render
from .models import CategoryModel, BlogModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

# Create your views here.


def landing(request):
    categories = CategoryModel.objects.all()
    blogs = BlogModel.objects.all()

    context = {'categories': categories, 'blogs': blogs}
    return render(request, 'base/landing.html', context)


def blog(request, pk):
    blog = BlogModel.objects.get(id=pk)
    return render(request, 'base/blog.html', {'blog': blog})


class BlogCreate(CreateView):
    model = BlogModel
    fields = ['category', 'name', 'description']
    success_url = reverse_lazy('base:landing')
    template_name = 'base/addBlog.html'


class BlogUpdate(UpdateView):
    model = BlogModel
    fields = ['category', 'name', 'description']
    success_url = reverse_lazy('base:landing')
    template_name = 'base/addBlog.html'


class CategoryCreate(CreateView):
    model = CategoryModel
    fields = ['name']
    success_url = reverse_lazy('base:landing')
    template_name = 'base/addCategory.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreate, self).form_valid(form)
