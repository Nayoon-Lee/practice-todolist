from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.

'''
def index(request):
    return HttpResponse('to_do_app first page')
'''

def index(request):
    todos = Todo.objects.all()
    content = {'todos' : todos}
    return render(request, 'to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    return HttpResponse("create Todo를 할거야! =>" +user_input_str)

'''
def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id", done_todo_id)
    return HttpResponseRedirect(reverse('index'))
'''

def deleteTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))
