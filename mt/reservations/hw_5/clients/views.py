from django.http import HttpResponse

def index(request):
    return HttpResponse("Страница клиентов работает!")
