from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import News,Todo
from .forms import TodoForm
import requests
import wikipedia
from .forms import DashboardForm
# Create your views here.

wikipedia.set_lang("uz")

def wiki(request):
    if request.method == 'POST':
        text = request.POST['text'].strip()
        form = DashboardForm(request.POST)
        
        try:
            # Qidiruv natijalarini olish
            search_results = wikipedia.search(text)
            if search_results:
                best_match = search_results[0]  # Eng mos kelgan maqolani olish
                search = wikipedia.page(best_match)
                
                context = {
                    'form': form,
                    'title': search.title,
                    'link': search.url,
                    'details': search.summary
                }
            else:
                context = {
                    'form': form,
                    'title': "Ma'lumot topilmadi",
                    'link': "",
                    'details': f"'{text}' bo‘yicha hech qanday maqola topilmadi. Iltimos, aniqroq so‘rov kiriting."
                }
        except wikipedia.exceptions.DisambiguationError as e:
            context = {
                'form': form,
                'title': "Bir nechta natijalar topildi",
                'link': "",
                'details': f"'{text}' bo‘yicha aniq maqola yo‘q. Quyidagilardan birini tanlab ko‘ring:\n" + ", ".join(e.options[:5])
            }
        except wikipedia.exceptions.PageError:
            context = {
                'form': form,
                'title': "Xatolik",
                'link': "",
                'details': f"'{text}' bo‘yicha maqola topilmadi. Iltimos, boshqa so‘rov kiriting yoki xatolikni tekshiring."
            }
        
        return render(request, 'wiki.html', context)
    
    else:
        form = DashboardForm()

    return render(request, 'wiki.html', {'form': form})



@login_required
def base(request):
    news = News.objects.all()
    context = {
        'news':news,
        'user':request.user
    }
    return render(request,'base.html',context=context)

def todo_vc(request):
    todos = Todo.objects.all()
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
        
    else:
        form = TodoForm()
    
    context = {
        'form':form,
        'todos':todos
                }
    return render(request,'todo.html',context=context)

def todo_d(request,id):
    todo = get_object_or_404(Todo,id=id)
    todo.delete()
    return redirect('todo')

def todo_e(request,id):
    todo = get_object_or_404(Todo,id=id)
    if id:  
        todo = get_object_or_404(Todo,id=id)
        form = TodoForm(instance=todo) 
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm()
    context = {
        'form':form,
        'todo':todo 
                }
    
    return render(request,'todo_e.html',context=context)


