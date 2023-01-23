from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def article_list_view(request):
    article_list = Article.published.all()
    # return HttpResponse("article list")
    return render(request, "articles/list.html", {"article_list": article_list})

def article_detail_view(request, slug):
    article = Article.published.get(slug=slug)
    return render(request, "articles/detail.html", {"article": article})
