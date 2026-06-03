from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def test_validacion(request):
    texto = request.GET.get('texto', '')
    if not texto:
        return HttpResponse("Falta parámetro de texto", status=400)
    if "ñ" not in texto:
        return HttpResponse("El texto requiere la letra ñ", status=400)
    return HttpResponse("Validación correcta")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_prometheus.urls')),
    path('test/', test_validacion),
]
