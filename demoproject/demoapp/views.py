from django.http import HttpResponse ,HttpResponseNotFound
from .forms import MiFormulario,logForm
from django.shortcuts import render


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

def mostrar_formulario(request):
    if request.method == 'POST':  # Cuando se envía el formulario
        form = MiFormulario(request.POST)
        if form.is_valid():
            # Procesar datos (ej: guardar en BD)
            nombre = form.cleaned_data['nombre']
            return HttpResponse(f"¡Gracias {nombre}!")  # Respuesta después de enviar
    else:
        form = MiFormulario()  # Formulario vacío para GET
    
    return render(request, 'formulario.html', {'form': form})
 
 #esto es un prueba
def  from_view(request):
    form = logForm()
    if request.method == 'POST':
        form = logForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'formulario2.html', context)
    