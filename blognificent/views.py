from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.views import generic

from blognificent.forms import CommentForm
from blognificent.models import Post, Comment


class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'Post'

    def get_queryset(self):
        return Post.objects.order_by('published')


def categories(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        'published'
    )
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'categories.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=User,
                body=form.cleaned_data['body'],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect('blognificent:detail', post.id)
    else:
        form = CommentForm()

    context = {
        'comments': comments,
        'form': form,
        'post': post,
    }
    return render(request, 'details.html', context)
