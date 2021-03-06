from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Resources
from .forms import ResourceForm
import os

def home(request):
    resource = Resources.objects.all()
    context = {'resource': resource}
    return render(request, 'journal/home.html', context)

def form(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/journal')
        else:
            pass
    else:
        form = ResourceForm()
    return render(request, 'journal/form.html', {'form': form})

def edit(request, id):
    resource = get_object_or_404(Resources, pk=id)
    if request.method == 'POST' and 'edit' in request.POST:
        form = ResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            image_before=Resources.objects.get(pk=id).image
            form.save()
            image_after=Resources.objects.get(pk=id).image
            if image_before and image_before != image_after:
                os.remove("/home/amoghvnaik/learnjournal/media/"+str(image_before))
            else:
                pass
            return HttpResponseRedirect('/journal')
        else:
            pass
    elif request.method == 'POST' and 'delete' in request.POST:
        image=Resources.objects.get(pk=id).image
        if image:
            os.remove("/home/amoghvnaik/learnjournal/media/"+str(image))
        else:
            pass
        Resources.objects.get(pk=id).delete()
        return HttpResponseRedirect('/journal')
    else: 
        form = ResourceForm(instance=resource)
    return render(request, 'journal/edit.html', {'form': form})

