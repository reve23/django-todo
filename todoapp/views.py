from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request,'todo.html',{'all_todo_items':all_todo_items})

def addTodo(request):
    #create a new Todo item
    #save 
    #redirect the user
    new_item = TodoItem(content =request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request,todo_id):
    try:
        item_to_delete = TodoItem.objects.get(id=todo_id)
        item_to_delete.delete()
    except:
        print("item doesn't exist")
    return HttpResponseRedirect('/todo/')
