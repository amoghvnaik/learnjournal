from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Resource
from .forms import ResourceForm

def home(request):
    resource = Resource.objects.all()
    context = {'resource': resource}
    return render(request, 'journal/home.html', context)

def form(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/journal')
        else:
            pass
    else:
        form = ResourceForm()
    return render(request, 'journal/form.html', {'form': form})

def edit(request, id):
    resource = get_object_or_404(Resource, pk=id)
    if request.method == 'POST' and 'edit' in request.POST:
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/journal')
        else:
            pass
    elif request.method == 'POST' and 'delete' in request.POST:
        Resource.objects.filter(pk=id).delete()
        return HttpResponseRedirect('/journal')
    else: 
        form = ResourceForm(instance=resource)
    return render(request, 'journal/edit.html', {'form': form})

