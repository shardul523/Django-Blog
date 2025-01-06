from django.http import Http404
from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(
        request, 
        'blog/post/list.html', 
        {'posts': posts}
    )


def post_detail(request, year, month, day, post):
    try:
        post = Post.published.get(
            slug=post,
            publish__year=year,
            publish__month=month,
            publish__day=day
        )
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    return render(
        request,
        'blog/post/detail.html',
        {'post' : post}
    )