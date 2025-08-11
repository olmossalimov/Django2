from django.shortcuts import render
from .models import Post
from django.http import Http404

def asosiy_menyu(request):
    return render(request, 'home.html')


def news(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'news.html', context)



def detail(request, id):
    try:
        post = Post.objects.get(id=id)
        context = {'post':post}
    except:
        raise Http404("Page not found")
    return render(request, 'detail.html', context)


