from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from blogs.models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def listing(page, page_index):
    per_page = 5
    paginator = Paginator(page, per_page) # Show 25 contacts per page
    try:
        page_index = int(page_index)
    except TypeError:
        page_index = 1
    try:
        blogs = paginator.page(page_index)
    except PageNotAnInteger:
        blogs = paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages) # If page is out of range (e.g. 9999), deliver last page of results.
    return blogs

def page(request, page_index=1):
    blogs = listing(Blog.objects.all().order_by('-pub_date'), page_index)
    return render(request, 'blogs/index.html', {'blogs':blogs})

def tagShow(request, tag_name, page_index=1):
    blog_list = Blog.objects.filter(tag=tag_name).order_by('-pub_date')
    blogs = listing(blog_list, page_index)
    return render(request, 'blogs/tagShow.html', {'blogs':blogs, 'page_index':page_index, 'tag':tag_name,})

def detail(request, id):
    p = get_object_or_404(Blog, pk=id)
    p.visit_count+=1
    p.save()
    return render(request, 'blogs/detail.html', {'blog':p,})

def test(request):
    return render(request,'blogs/test.html',{})
