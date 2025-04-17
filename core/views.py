from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Blog
from .forms import BlogForm

def home(request):
    return render(request, 'web/home.html')

def about(request):
    return render(request, 'web/about.html')

def showcase(request):
    return render(request, 'web/showcase.html')

def blog(request):
    search_query = request.GET.get('search', '').strip()
    filter_field = request.GET.get('filter', '').strip()

    blogs = Blog.objects.all()

    if search_query:
        blogs = blogs.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    if filter_field:
        blogs = blogs.filter(category=filter_field)

    categories = Blog.objects.values_list('category', flat=True).distinct().order_by('category')

    paginator = Paginator(blogs.order_by('-created_at'), 3)  # 3 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs': page_obj.object_list,
        'categories': categories,
        'search_query': search_query,
        'filter_field': filter_field,
        'page_obj': page_obj,
    }
    return render(request, 'web/blog.html', context)

@login_required
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'web/blog_edit.html', {'form': form, 'blog': blog})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'web/blog_create.html', {'form': form})

@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.author == request.user:
        blog.delete()
    return redirect('blog')
