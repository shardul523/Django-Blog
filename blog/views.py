from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
from .models import Post

# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'blog/post/list.html'
    paginate_by = 3


# def post_list(request):
#     posts_list = Post.objects.all()
#     paginator = Paginator(posts_list, 3)
#     page_number = request.GET.get('page', 1)

#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         posts = paginator.page(1)

#     return render(
#         request, 
#         'blog/post/list.html', 
#         {'posts': posts}
#     )


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