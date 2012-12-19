from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def home(request):
    pass