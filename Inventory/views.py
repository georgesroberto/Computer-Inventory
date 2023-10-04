from django.shortcuts import render, redirect, get_object_or_404
from .models import Computer
from .forms import ComputerForm, SearchForm
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

#READ FORM
@login_required
def list(request):#READ FORM 
    title = "List of Computers"
    form = SearchForm()
    queryset = Computer.objects.all()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            pc_name = form.cleaned_data.get('pc_name')
            username = form.cleaned_data.get('username')

            if pc_name:
                queryset = queryset.filter(pc_name__icontains=pc_name)
            if username:
                queryset = queryset.filter(username__icontains=username)

    context = {
        "title": title,
        "form": form,
        "queryset": queryset,
    }

    return render(request, 'list.html', context)

#UPDATE FORM
@login_required
def update(request, pk):#UPDATE FORM
    item = get_object_or_404(Computer, id=pk)
    form = ComputerForm(instance=item)
    
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
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
        return redirect('list')
    
    
    return render(request, 'delete.html/')