from django.shortcuts import render
from KB.posts.models import Posts
from KB.articles.models import Articles


def home(request):
    context = {}
    return render(request, 'index.html', context)


def searchresults(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Posts.objects.filter(Keywords__contains=searched)
        context = {'results': results}
        return render(request, 'searchresults.html', context)
    else:
        context = {}
        return render(request, 'index.html', context)


def info(request, name):
    articles = Articles.objects.filter(title=name)
    context = {'articles': articles}
    return render(request, 'info.html', context)
