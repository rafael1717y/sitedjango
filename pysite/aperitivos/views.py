from django.shortcuts import render
from pysite.aperitivos.models import Video

#substituição dos dicionários pela classe
videos = [
         Video(slug='motivacao', titulo='Vídeo Aperitivo: Motivação', vimeo_id='458138324'),
         Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id='251497668'),
]

#videos_dct = {dct['slug']: dct for dct in videos}

videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})

def video(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
