from django.http import HttpResponse

def handler404(request,exception):
    return HttpResponse("papi esa vaina no se encontro")