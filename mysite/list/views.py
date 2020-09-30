from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import Http404
from .models import MangaEntry

def index(request):
    latest_manga_list = MangaEntry.objects.order_by('-name')
    ids = []
    for entry in latest_manga_list:
        link = entry.link
        manga_id = link.rsplit('/')[-2]
        ids.append(manga_id)
    manga_list = zip(latest_manga_list,ids)
    context = {
        'latest_manga_list': manga_list,
        
    }
    return render(request, 'list/index.html', context)

def detail(request, question_id):
    manga = get_object_or_404(MangaEntry, pk=question_id)
    return render(request,'list/detail.html', {'manga':manga})

  