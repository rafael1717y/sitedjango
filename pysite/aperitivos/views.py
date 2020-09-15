from django.shortcuts import render

class Video:

    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id



#substituição dos dicionários pela classe
videos = [
         Video('motivacao', 'Vídeo Aperitivo: Motivação', 458138324),
         Video('instalacao-windows', 'Instalação Windows',251497668),
]

#videos_dct = {dct['slug']: dct for dct in videos}

videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})

def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
