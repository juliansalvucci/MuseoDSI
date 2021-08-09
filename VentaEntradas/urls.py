from django.urls import path
from . import views

app_name='VentaEntradas'

urlpatterns = [
    path('registrarNuevaEntrada/', views.registrarNuevaEntrada),
    path('buscarEmpleadoLogueado/', views.buscarEmpleadoLogueado),
    path('getFechaHoraActual/', views.getFechaHoraActual),
    path('buscarTarifasSedeEmpleado/', views.buscarTarifasSedeEmpleado),
    path('tomarTarifasSeleccionadas/', views.tomarTarifasSeleccionadas),
    path('buscarExposicionVigente/', views.buscarExposicionVigente),
    path('tomarCantidadDeEntradasAEmitir/', views.tomarCantidadDeEntradasAEmitir),
    path('validarLimiteDeVisitantes/', views.validarLimiteDeVisitantes),
    path('buscarReservaParaAsistir/', views.buscarReservaParaAsistir),
    path('calcularTotalDeVenta/', views.calcularTotalDeVenta),
    path('tomarConfirmacionDeVenta/', views.tomarConfirmacionDeVenta),
    path('buscarUltimoNumeroDeEntrada/', views.buscarUltimoNumeroDeEntrada),
    path('generarEntradas/', views.generarEntradas),
    path('imprimirEntrada/', views.imprimirEntrada),
    path('actualizarVisitantesEnPantalla/', views.actualizarVisitantesEnPantalla),
    path('finCu/', views.finCu),
]