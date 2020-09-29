from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import Http404
from .models import MangaEntry

def index(request):
    latest_manga_list = MangaEntry.objects.order_by('-name')
    context = {
        'latest_manga_list': latest_manga_list,
    }
    return render(request, 'list/index.html', context)

def detail(request, question_id):
    manga = get_object_or_404(MangaEntry, pk=question_id)
    #output = "manga with id {0} is {1}. can be found under {2}.\n Current chapter is: {3}".format(question_id, MangaEntry.objects.get(id=question_id),MangaEntry.objects.get(id=question_id).link, MangaEntry.objects.get(id=question_id).current_chapter)
    return render(request,'list/detail.html', {'manga':manga})

def link(request, question_id):
    output = "{0}: the url is {1}".format(MangaEntry.objects.get(id=question_id), MangaEntry.objects.get(id=question_id).link)
    return HttpResponse(output)

def current_c(request, question_id):
    output = "{0}: your current chapter is {1}".format(MangaEntry.objects.get(id=question_id), MangaEntry.objects.get(id=question_id).current_chapter)
    return HttpResponse(output)
