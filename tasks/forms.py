from django.forms import ModelForm
from .models import Task

class createTask(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'limit_date']
