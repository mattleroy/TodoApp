from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem

def todoView(request):
    items = TodoItem.objects.all()
    return render(request, 'todo/todo.html', {'items': items})

def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content = c)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    deleted_item = TodoItem.objects.get(id=todo_id)
    deleted_item.delete()
    return HttpResponseRedirect('/todo/')