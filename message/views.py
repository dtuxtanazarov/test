from io import text_encoding

from django.template.defaultfilters import title
from django.urls import reverse, reverse_lazy

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .models import Post, Category, Region

# Create your views here.
def home(request):
    first_news=Post.objects.first()
    three_news=Post.objects.all()[1:4]
    return render(request, 'home.html',{
        'first_news':first_news,
        'three_news':three_news
    })
def all_news(request):
    all_news=Post.objects.all()
    return render(request, 'all-news.html',{
        'all_news':all_news
    })
def detail(request, id):
    news = Post.objects.get(id=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = Post.objects.filter(category=category).exclude(id=id)
    context = {'news':news,
               'category':category,
               'rel_news':rel_news}
    return render(request, 'detail.html', context)
def all_category(request):
    cats=Category.objects.all()
    return render(request,'category.html',{
        'cats':cats
    })
def category(request,id):
    category=Category.objects.get(id=id)
    news=Post.objects.filter(category=category)
    return render(request,'category-news.html',{
        'all_news':news,
        'category':category
    })

def all_region(request):
    regs=Region.objects.all()
    return render(request,'region.html',{
        'regs':regs
    })

def region(request,id):
    region=Region.objects.get(id=id)
    news=Post.objects.filter(region=region)
    return render(request,'region-news.html',{
        'all_news':news,
        'region':region
    })
class Create_post(CreateView):
    model = Post
    template_name = 'create-post.html'
    fields = ['category','region','title','body','image','author']

class Edit_view(UpdateView):
    model = Post
    template_name = 'edit-post.html'
    fields = ['category','region','title','body']

class Delete_post(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')


