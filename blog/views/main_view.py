from django.shortcuts import render, redirect
from ..models import blogs
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'main/home.html')


def single_blog(request):
    return render(request,'main/single_blog.html')

def edit_blog(request):
    return render(request,'main/edit_blog.html')

@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        data = blogs(title=title, subtitle=subtitle, description=description, image=image)
        data.save()
        return redirect('home')
    
    return render(request,'main/create_blog.html')