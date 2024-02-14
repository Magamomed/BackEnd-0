from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm


def todos_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todos_list.html', {'todos': todos})

def todo_detail(request, pk):  # Изменяем аргумент на 'pk'
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todos_list')



def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_detail', pk=pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form})