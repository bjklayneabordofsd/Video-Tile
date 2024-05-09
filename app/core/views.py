from django.shortcuts import render, redirect, get_object_or_404
from core.forms import VideoForm
from core.models import Video

def UploadVideo(request):
    videos = Video.objects.all()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage-videos')
        else:
            context = {'form': form}
            return render(request, 'core/manage-videos.html', context)
    context = {'form': VideoForm(), 'videos': videos}
    return render(request, 'core/manage-videos.html', context)

def DeleteVideo(request, pk):
   video = get_object_or_404(Video, pk=pk)
   video.delete()
   return redirect('manage-videos')


def VideoList(request):
    videos = Video.objects.all()
    return render(request, 'core/home.html', {'videos': videos})