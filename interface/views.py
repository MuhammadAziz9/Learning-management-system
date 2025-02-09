from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import News
# Create your views here.

@login_required
def main(request):
    news = News.objects.all()
    context = {
        'news':news,
        'user':request.user
    }
    return render(request,'main.html',context=context)


