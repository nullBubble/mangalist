from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import Http404
from .models import MangaEntry
from .forms import chapterForm

def index(request):
    if request.method == 'POST':
        form = chapterForm(request.POST)
        if form.is_valid():
            print(form)
            # get name from the form which is not possible since the forms all look the same, have to change the id
            # of the forms to the actual names of the manga and then we can parse them into the name below to update
            # the correct entry. right now it only updates the first one obviously
            # TODO: if it is an empty field, dont reset it to None
            man = MangaEntry.objects.get(name='pseudoharem')
            man.current_chapter = form.cleaned_data['chapter']
            man.save()
            return HttpResponseRedirect('/')
    else:
        form = chapterForm()
        print(form)
    
    latest_manga_list = MangaEntry.objects.order_by('-name')
    ids = []
    for entry in latest_manga_list:
        link = entry.link
        manga_id = link.rsplit('/')[-2]
        ids.append(manga_id)
    manga_list = zip(latest_manga_list,ids)
    context = {
        'latest_manga_list': manga_list,
        'form': form,
    }
    return render(request, 'list/index.html', context)

def detail(request, question_id):
    manga = get_object_or_404(MangaEntry, pk=question_id)
    return render(request,'list/detail.html', {'manga':manga})
