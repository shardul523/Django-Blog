from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

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