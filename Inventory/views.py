from django.shortcuts import render, redirect, get_object_or_404
from .models import Computer
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    title = "Homepage"
    context = {"title" : title}

    return render(request, 'home.html/', context)

#CREATE FORM
@login_required
def add(request):
    title = "Add Computers"
    form = ComputerForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Form saved successfully")
        return redirect('list')

    context = { 
        "title" : title,
        "form" : form
    }

    return render(request, 'add.html/', context)

def add_os(request):
    if request.method == 'POST':
        form = AddOsForm(request.POST)

        if form.is_valid():
            os_choices = form.cleaned_data['os_system']
            os_choices_string = ''.join(os_choices)

            # Create an Os_Choice instance with the combined string
            os_choice_instance = Os_Choice(os_system=os_choices_string)
            os_choice_instance.save()

            messages.success(request, "OS saved successfully")
            return redirect('list')
    else:
        form = AddOsForm()

    context = {
        "title": "Add Operating System",
        "form": form
    }

    return render(request, 'os.html', context)
#READ FORM
@login_required
def list(request):
    title = "List of Computers"
    form = SearchForm()
    items = Computer.objects.all()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            items = Computer.objects.filter(
                pc_name__icontains=form['pc_name'].value(),
                username__icontains=form['username'].value())

    context = {
        'title': title,
        'form' : form,
        'items' : items
    }

    return render(request, 'list.html', context)

#UPDATE FORM
@login_required
def update(request, pk):#UPDATE FORM
    item = get_object_or_404(Computer, id=pk)
    form = UpdateForm(instance=item)
    
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            form.instance.os.set(form.cleaned_data['os'])
            return redirect('list')
        
    context = {
        'form':form
    }

    return render(request, 'add.html/', context)

#DELETE FORM
@login_required
def delete(request, pk):#DELTE FORM
    item = get_object_or_404(Computer, id=pk)

    if request.method == 'POST':
        item.delete()
        messages.success(request, "Item deleted successfully")
        return redirect('list')
    
    return render(request, 'delete.html/')