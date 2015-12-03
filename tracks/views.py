from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Track
# Create your views here.

def track_view(request, title):
    #title = Track.objects.get(title=title)
    track = get_object_or_404(Track, title=title)
    #return HttpResponse(title)
    return render(request, 'track.html', {'track': track})