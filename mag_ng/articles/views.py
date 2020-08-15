from django.shortcuts import render, redirect


def add_article(request):
    context = {}
    return render(request, 'articles/add_article.html', context)


