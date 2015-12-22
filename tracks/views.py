from requests.models import json_dumps

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import Track
# Create your views here.

def track_view(request, title):
    #title = Track.objects.get(title=title)
    track = get_object_or_404(Track, title=title)
    bio = track.artist.biography

    data = {
        'title': track.title,
        'order': track.order,
        'album': track.album.title,
        'artist': {
            'name': track.artist.first_name,
            'bio': bio,
        }
    }

    json_data = json_dumps(data)
    return HttpResponse(json_data, content_type='application/json')
    #return HttpResponse(title)
    #return render(request, 'track.html', {'track': track, 'bio': bio})