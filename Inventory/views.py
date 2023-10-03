from django.shortcuts import render, redirect
from .models import Computer
from .forms import ComputerForm, SearchForm

# Create your views here.

def home(request):
    title = "Homepage"
    context = {"title" : title}

    return render(request, 'home.html/', context)

def list(request):
    title = "List of Computers"
    form = ComputerForm
    queryset = Computer.objects.all()

    search = SearchForm

    context = { 
        "title" : title,
        "form" : form,
        "queryset" : queryset,
        "search" : search
    }

    

    return render(request, 'list.html/', context)

def add(request):
    title = "Add Computers"
    form = SearchForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list')

    context = { 
        "title" : title,
        "form" : form
    }



    return render(request, 'add.html/', context)

def update(request):

    return render(request, 'update.html/')

def delete(request):
    return render(request, 'delete.html/')