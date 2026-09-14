from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task

"""

@login_required
def task_list(request):
    all_item = Task.objects.filter(user = request.user)
    context = {'task': all_item}
    return render(request, 'todo/task_list.html', context)

#buat aplikasi. 

def task_list(request):
    
    all_item = Task.objects.all()
    
    context = {
        'task' : all_item
    }

    return render(request, 'todo/task_list.html', context) 
"""

#buat login & aplikasi
@login_required
def task_list(request):
    filter_status = request.GET.get('filter', 'all')

    if filter_status == 'done':
        all_item = Task.objects.filter(user=request.user, status=True)
    elif filter_status == 'pending':
        all_item = Task.objects.filter(user=request.user, status=False)
    else:
        all_item = Task.objects.filter(user=request.user)

    context = {
        'task': all_item,
        'filter_status': filter_status,
    }
    return render(request, 'todo/task_list.html', context)

#buat menambah task
@login_required
def add_task(request):
    
    if request.method == 'POST':
        task_name = request.POST['task_name']
        Task.objects.create(task_name = task_name, user = request.user)
    return redirect('task_list')

#buat tanda centang
@login_required
def toggle_status(request, task_id):
    
    task = Task.objects.get(id = task_id, user = request.user)
    task.status = not task.status
    task.save()
    return redirect('task_list')

#buat update
@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id = task_id, user = request.user)
    if request.method == 'POST':
        task.task_name = request.POST['task_name']
        task.save()
        return redirect('task_list')
    return render(request, 'todo/edit_task.html', {'task' : task})

#buat hapus task
@login_required
def delete_task(request, task_id):
    
    task = Task.objects.get(id = task_id, user = request.user)
    task.delete()
    return redirect('task_list')

#buat user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = UserCreationForm()
    
    for field in form.fields.values():
        field.widget.attrs['class'] = 'form-control'
    
    return render(request, 'todo/register.html', {'form' : form})








