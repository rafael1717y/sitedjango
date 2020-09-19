from django.shortcuts import get_object_or_404, render

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
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
