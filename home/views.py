from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'success' : False, 'name':'Abhishek'}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        task = Task(tasktitle = title, taskdesc = desc)
        task.save()
        context['success'] = True;
        # context = {'success':True, 'name' : 'Abhishek'}


    return render(request, 'index.html', context = context)

def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'tasks.html', context = context)
