from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

# Create your views here.

#@login_required
def index(request):
    return render(request, "tasks/index.html")


#@login_required
def createTask(request):
    form = TaskForm()
    context = {"form": form}
    return render(request, 'tasks/form.html', context)
 