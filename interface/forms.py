from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['subject_name','description','due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100,label='Bu yerdan izlashingiz mumkin')
