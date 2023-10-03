from django.shortcuts import render, redirect
from .forms import ComputerForm

# Create your views here.

def home(request):
    title = "Homepage"
    context = {"title" : title}

    return render(request, 'home.html/', context)

def list(request):
    title = "View Computers"
    form = ComputerForm
    context = { 
        "title" : title,
        "form" : form
    }

    #if form.is_valid():
    #    form.save()
    #    return redirect('/')
    
    #context = { "title" : title, "form" : form }


    return render(request, 'list.html/', context)

def add(request):
    return render(request, 'add.html/')

def update(request):
    return render(request, 'update.html/')

def delete(request):
    return render(request, 'delete.html/')