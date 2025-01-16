from django.http import HttpResponse

def Home(request):
    return HttpResponse("Welcome to the Home page!")
