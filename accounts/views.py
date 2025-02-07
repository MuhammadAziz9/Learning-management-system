from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form':form
    }
    return render(request,'registration/register.html',context=context)
