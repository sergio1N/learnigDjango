from django.http import HttpResponse ,HttpResponseNotFound

def home(request):
    return HttpResponse('solo somoa nada por que no somos nada <br> quiero cuca')

def Con_estilos(request,vareta='coño madre'): 
    return HttpResponseNotFound(f"<h1>Welcome to {vareta}</h1>")

def qryview(request):
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))

# Prueba de platos:
def menuItems(request,dish):
    items={
        'pasta':" no tenemos pasta pero si arroz al a francesa",
        'arroz':"El arroz esta salado pero demaciado salado",
        'propina':'dejenos propina a su sanchas'
    }
    
    description=items.get(dish,'no hay papi')
    
    return HttpResponse("<h2>{}: </h2>  <br> {}".format(dish,description) )