from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import Http404
from .models import MangaEntry

def index(request):
    if request.method == 'POST':
        string = str(request.body).strip("'").rsplit('&')[1]
        name, chapter = string.split('=')[0], string.split('=')[1]
        name = name.replace("+"," ")
        print(name)
        if chapter != '':
            man = MangaEntry.objects.get(name=name)
            man.current_chapter = chapter
            man.save()
            return HttpResponseRedirect('/')
        
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

def add_manga(request):
    print(request)
    if request.method == 'POST':
        if str(request.body).find('&') != -1:
            print(request.body)
            string = str(request.body).strip("'").rsplit('&')
            name = string[1].split('=')[1]
            name = name.replace("+", " ")
            ch = string[2].split('=')[1]
            link = string[3].split('=')[1].replace("%3A",":")
            link = link.replace("%2F","/")
            
            new_entry = MangaEntry.objects.create(name=name,current_chapter=ch,link=link)
            new_entry.save()
            return HttpResponseRedirect('/')
    return render(request,'list/add_manga.html')

def delete_manga(request):
    latest_manga_list = MangaEntry.objects.order_by('-name')
    context = {
        'latest_manga_list': latest_manga_list,
    }
    if request.method == 'POST':
        if str(request.body).find('&') != -1:
            string = str(request.body).strip("'").rsplit('&')
            name = string[1].split('=')[1]
            entry = MangaEntry.objects.get(name=name)
            entry.delete()
            return HttpResponseRedirect('/')
    return render(request,'list/delete_manga.html', context)