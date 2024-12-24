from django.shortcuts import render,redirect
from . models import Tasks
from .forms import InputForm
def task_list(request):
    tasks=Tasks.objects.all().order_by('last_date')
    return render(request,'app/task_list.html',{'tasks':tasks})

def add_task(request):
    if request.method == "POST":
        form=InputForm(request.POST)
        if form.is_valid():
            form=form.save()
        return redirect('/')
    else:
        form=InputForm()
    return render(request,'app/add_task.html',{'form':form})
       
   