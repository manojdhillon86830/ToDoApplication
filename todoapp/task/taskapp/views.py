from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
# Create your views here.
def home_view(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    tasks = Task.objects.all()
    context = {'form':form,'tasks':tasks}
    res=render(request, 'star/home.html',context)
    return res

def delete_view(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')
