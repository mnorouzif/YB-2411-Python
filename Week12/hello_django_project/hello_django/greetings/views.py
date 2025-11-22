from django.http import HttpResponse

def welcome(request, name):
    return HttpResponse(f"<h1>Welcome {name} to Django!</h1>")
