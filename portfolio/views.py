from django.shortcuts import render
from .models import Project
from blog.forms import MessageForm


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'portfolio/thankyou.html')            
        else:
             form = MessageForm()

    form = MessageForm()
    return render(request, 'portfolio/contact.html', {'form':form})

# def login(request):
#     return render(request, 'portfolio/login.html')

def about(request):
    return render(request, 'portfolio/about.html')
