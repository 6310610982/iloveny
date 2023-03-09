# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        video = request.FILES['video']
        Video.objects.create(title=title, description=description, video=video)
        messages.success(request, 'Video uploaded successfully!')
        return redirect('home')
    return render(request, 'trafficmonitor/upload.html')

def home_page(request):
    return render(request, 'trafficmonitor/home.html')
