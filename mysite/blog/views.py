from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from mysite.blog.models import Post
from mysite.blog.forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')
    context = {
        'posts': posts
    }
    
    return render(request=request, template_name='blog/post_list.html', context=context)

def post_show(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post)
    context = {
        'post': post
    }

    return render(request=request, template_name='blog/post_show.html', context=context)

def post_save(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect(to='blog:post_show', pk=post.pk) 
    else:
        form = PostForm()
    return render(request=request, template_name='blog/post_create.html', context={'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect(to='blog:post_show', pk=post.pk) 
    else:
        form = PostForm(instance=post)
    return render(request=request, template_name='blog/post_edit.html', context={'form': form})