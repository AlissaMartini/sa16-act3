from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def work(request):
    context = {
        'image1_url': '/path/to/Ai.jpg',
        'image2_url': '/path/to/youtube.jpg',
        'image3_url': '/path/to/fortnite.jpg',
    }
    return render(request, 'pages/work.html',context)

def contact(request):
    return render(request, 'pages/contact.html')
from django.shortcuts import render

