from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import randint, choice
import logging
from .models import Author, Post
from .forms import AuthorForm, PostForm

logger = logging.getLogger(__name__)


def index(request):
    html = """
        <h1>Привет,  в этом разделе будут храниться статьи</h1>
        <p>в много авторов и интересные темы:</p>
    """
    logger.info('Index page accessed')
    return HttpResponse(html)


def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            bday = form.cleaned_data['bday']
            new_author = Author(
                name=name,
                lastname=lastname,
                email=email,
                bio=bio,
                bday=bday
            )
            new_author.save()
            return HttpResponse(f'new author {name} {lastname} {bday} added')
    else:
        form = AuthorForm()
        authors = Author.objects.all()
        context = {'authors': authors, 'form': form}
        return render(request, 'blogapp/author.html', context)


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            new_post = Post(
                title=title,
                content=content,
                author=author)
            new_post.save()
            return HttpResponse(f'new post {title} {author} added')
    else:
        form = PostForm()
        last_posts = Post.objects.all().order_by('-id')[:3]
        context = {'posts': last_posts, 'form': form}
        return render(request, 'blogapp/post.html', context)


def a_post(request, author_id):
    name = Author.objects.filter(pk=author_id).first()
    posts = name.post_set.all()
    context = {'name': name, 'posts': posts}
    return render(request, 'blogapp/a_post.html', context)