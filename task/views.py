from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .form import AddTask_Form
from .models import *
import os 
from django.contrib import messages
from django.db.models import Case, When, IntegerField
# Create your views here.
def task_list(request):
    if request.method == 'GET':
        search_kay = request.GET.get('search_bar')
        filter = request.GET.get('filter')
        ordering = request.GET.get('ordering')
        priority = request.GET.get('priority')
        
        if search_kay:
            if Task.objects.filter(title__icontains = search_kay).exists():
                task = Task.objects.filter(title__icontains = search_kay)
            else:
                messages.warning(request,'Task not found!')
                task = Task.objects.all()

        elif ordering == 'created_date':
            task = Task.objects.all().order_by('-created_date')

        elif ordering == 'due_date':
            task = Task.objects.all().order_by('due_date')

        elif filter == 'complete':
            task = Task.objects.filter(is_complete=True)
            
        elif filter == 'incomplete':
            task = Task.objects.filter(is_complete=False)  

        elif priority == 'all':
            task = Task.objects.all()

        elif priority == 'high':
            task = Task.objects.filter(priority='High')

        elif priority == 'medium':
            task = Task.objects.filter(priority="Medium")

        elif priority == 'low':
            task = Task.objects.filter(priority='Low')

        else:
            task = Task.objects.all()
    return render(request,'task/task.html',{'task':task, 'filter':filter})

def add_task(request):
    form=AddTask_Form()
    if request.method == 'POST':
        form  = AddTask_Form(request.POST)
        if form.is_valid():
            task = form .save()
            task.save() 
            return redirect('task_list')
        else:
            return HttpResponse(form.errors)
        
    return render(request,'task/add_task.html',{'form':form})

def task_view(request,id):
    task_view = Task.objects.get(id=id)    
    image = Task_Image.objects.filter(task=task_view)

    if request.method == 'POST':
        image = request.FILES.get('image')
        print(image)

        task_image = Task_Image.objects.create(image=image,task=task_view)
        task_image.save()
        return redirect(request.META['HTTP_REFERER'])
    
    return render(request,'task/task_view.html',{'task_view':task_view, 'image':image})

def edit_task(request,id):
    task = Task.objects.get(id=id)

    form=AddTask_Form(instance=task)
    if request.method == 'POST':
        form = AddTask_Form(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_view',id=id)
    return render(request,'task/edit_task.html',{'form':form})

def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')

def delete_task_image(request,id):
    task_image = Task_Image.objects.get(id=id)
    os.remove(task_image.image.path)
    task_image.delete()
    return redirect(request.META['HTTP_REFERER'])


def task_submition(request,id):
    task = Task.objects.get(id=id)
    task.is_complete = True
    task.save()        
    return redirect(request.META['HTTP_REFERER'])

def notification(request):
    pass