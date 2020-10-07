from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import Http404
from django.urls import reverse
from .models import MangaEntry
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data.pop('csrfmiddlewaretoken')
        name = list(data.keys())[0]
        if data.get(name) != '':
            man = MangaEntry.objects.get(name=name)
            man.current_chapter = data.get(name)
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
    if request.method == 'POST':
        data = request.POST
        if "new_manga" in data.keys() and "chapter" in data.keys() and "url" in data.keys():
            latest_manga_list = MangaEntry.objects.order_by('-name')
            names = []
            for entry in latest_manga_list:
                names.append(entry.name)

            if data.get('new_manga') == "" or data.get('new_manga') in names:
                messages.error(request, "Enter a valid name and one that is not taken")
                return HttpResponseRedirect(reverse('list:add_manga'))
            if "mangadex" not in data.get('url'):
                messages.error(request, "Provide correct link")
                return HttpResponseRedirect(reverse('list:add_manga'))
            if data.get('chapter') == "":
                messages.error(request, "Enter a valid chapter number")
                return HttpResponseRedirect(reverse('list:add_manga'))

            new_entry = MangaEntry.objects.create(name=data.get('new_manga'),current_chapter=data.get('chapter'),link=data.get('url'))
            new_entry.save()
            return HttpResponseRedirect('/')
    return render(request,'list/add_manga.html')    

def delete_manga(request):
    latest_manga_list = MangaEntry.objects.order_by('-name')
    context = {
        'latest_manga_list': latest_manga_list,
    }
    if request.method == 'POST':
        data = request.POST
        if "deleted_manga" in data.keys():
            entry = MangaEntry.objects.get(name=data['deleted_manga'])
            entry.delete()
            return HttpResponseRedirect('/')
    return render(request,'list/delete_manga.html', context)