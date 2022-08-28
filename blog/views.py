from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q


def all_blogs(request, category_id=None):
    category = request.GET.get('category')

    if category == None:
        blogs = Blog.objects.order_by('-date')
    else:
        blogs = Blog.objects.filter(category__name=category)

    P = Paginator(blogs,10)
    page_num = request.GET.get('page',1)
    try:
        page = P.page(page_num)
    except EmptyPage:
        page = P.page(1)
    categories = Category.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs':page,'categories':categories})
    

def detail(request, blog_id):
    category = request.GET.get('category')
    
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            
        else:
            form = CommentForm()

    form = CommentForm()
    categories = Category.objects.all()
    return render(request, 'blog/detail.html', {'blog':blog, 'form':form,'categories':categories})

def search(request):
    category = request.GET.get('category')
    blogs = Blog.objects.order_by('-date')
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            blogs = Blog.objects.order_by('-date').filter(Q(description__icontains=query) | Q(title__icontains=query))
    categories = Category.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs':blogs,'categories':categories})
