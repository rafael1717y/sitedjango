from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<htl><body>Olá SIMONINHA</body></hml>', content_type='text/html')
