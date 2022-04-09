from django.http import HttpResponse


def index(request):
    return HttpResponse("eugene")

def john(request):
    return HttpResponse("<center>hello</center>")