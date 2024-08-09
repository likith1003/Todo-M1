from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    alltodos = Todo.objects.all()
    d = {'alltodos': alltodos}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        todo = Todo(title=title, desc=desc)
        todo.save()
    return render(request, 'home.html', d)


def srt(request):
    alltodos = Todo.objects.all()
    d = {'alltodos': alltodos}
    if request.method == 'POST':
        s = request.POST.get('sort')
        if s == 'sno':
            sorted_objects = sorted(alltodos, key=lambda a:a.sno)
        elif s == 'title':
            sorted_objects = sorted(alltodos, key=lambda a:a.title)
        elif s == 'desc':
            sorted_objects = sorted(alltodos, key=lambda a:a.desc)
        d = {'alltodos': sorted_objects}
        return render(request, 'home.html', d)


    return render(request, 'home.html', d)


def update(request):
    if request.method == 'GET':
        pk = request.GET.get('pk')
        todo_object = Todo.objects.get(sno=pk)
        if todo_object:
            d = {'obj': todo_object}
            return render(request, 'update.html', d)
        return HttpResponse('object not found')
    elif request.method == 'POST':
        pk = request.POST.get('pk')
        todo_object = Todo.objects.filter(sno=pk)
        if todo_object:
            title = request.POST.get('title')
            desc = request.POST.get('desc')
            todo_object.update(title=title, desc=desc)
            alltodos = Todo.objects.all()
            d = {'alltodos': alltodos}
            return render(request, 'home.html', d)
        return HttpResponse('invalid object')
    return render(request, 'update.html')

def delete(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        todo_object = Todo.objects.filter(sno=pk)
        if todo_object:
            todo_object.delete()
            alltodos = Todo.objects.all()
            d = {'alltodos': alltodos}
            return render(request, 'home.html', d)
    return render(request, 'home.html')