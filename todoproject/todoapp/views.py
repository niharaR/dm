from django.shortcuts import render
from .models import Task
from django.shortcuts import redirect
from  django.forms import ModelForm
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy




# Create your views here.
class TaskListView(ListView):
    model=Task
    template_name='home.html'
    context_object_name="task"

class TaskDetailtView(DetailView):
    model=Task
    template_name='details.html'
    context_object_name="task"

class TaskUpdateView(UpdateView):
    model=Task
    template_name='edit.html'
    context_object_name="task"
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy()

def add(request):
    task1 = Task.objects.all()

    if request.method=="POST":
        task=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        obj=Task(name=task,priority=priority,date=date)
        obj.save()
    return render(request,'home.html',{'task':task1})

# def details(request):
    # task=Task.objects.all()
    # return render(request,"details.html",{'task':task})

def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method=="POST":
         task.delete()
         return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task1=Task.objects.get(id=id)
    forms=TodoForm(request.POST or None,instance=task1)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'form':forms,'task':task1})



