from django.shortcuts import render, redirect, get_list_or_404
from ..models import Blogs
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    blogs_data = Blogs.objects.all()
    data = {
        'blogs':blogs_data
    }
    return render(request,'main/home.html', context=data) 


def single_blog(request, blog_id):
    blog = get_list_or_404(Blogs,pk=blog_id)
    return render(request,'main/single_blog.html', {"blog":blog})

def edit_blog(request):
    return render(request,'main/edit_blog.html')

def delete_blog(request, blog_id):
    blog = get_list_or_404(Blogs,pk=blog_id)
    blog.delete()
    return redirect("home")


@login_required 
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        data = Blogs(title=title, subtitle=subtitle, description=description, image=image)
        data.save()
        return redirect('home')
    
    return render(request,'main/create_blog.html')