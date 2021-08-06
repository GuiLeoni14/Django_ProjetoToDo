from django.shortcuts import render, get_object_or_404,  redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
@login_required()
def hellouworld(request):
    return HttpResponse('Hello Word!')

@login_required()
def tasks_list(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')
    tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()

    if search:

        tasks = Task.objects.filter(title__icontains=search, user=request.user)#filtar as tarefas de cada usuario

    elif filter:

        tasks = Task.objects.filter(done=filter, user=request.user)

    else:

        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)#filtar as tarefas de cada usuario
        paginator = Paginator(tasks_list, 4)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html',
                  {'tasks': tasks, 'tasksdoneRecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing})


@login_required()
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


@login_required()
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing' #seta o campo 'fazendo' na hora de criar a task
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


@login_required()
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task':task})


@login_required()
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa Deletada com sucesso.')
    return redirect('/')


@login_required()
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if task.done == 'doing':
        task.done = 'done'

    else:
        task.done = 'doing'

    task.save()

    return redirect('/')

@login_required()
def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})

