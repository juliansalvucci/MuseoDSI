from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.utils.translation import ugettext_lazy as _  # conversión de idiomas
# trae los usuarios logueados en el sistema.
from django.contrib.auth.models import User

class TipoDeEntrada(models.Model):
    nombre = models.TextField(
        _('nombre'),
        help_text=_('Nombre de tipo de entrada'),
        max_length=200,
    )

class TipoDevisita(models.Model):
    nombre = models.TextField(
        _('nombre'),
        help_text=_('Nombre de tipo de visita'),
        max_length=200,
    )

class Empleado(models.Model):
    apellido = models.TextField(
        _('apellido'),
        help_text=_('Apellido de empleado'),
        max_length=200,
    )
    nombre = models.TextField(
        _('nombre'),
        help_text=_('Nombre de empleado'),
        max_length=200,
    )
    codigoValidacion = models.IntegerField(
        _('CodigoValidacion'),
        help_text=_('Código de validación'),
    )
    cuit = models.IntegerField(
        _('cuit'),
        help_text=_('CUIT'),
    )
    dni = models.IntegerField(
        _('dni'),
        help_text=_('DNI'),
    )
    calle = models.TextField(
        _('calle'),
        help_text=_('Calle'),
        max_length=200,
    )
    numero = models.IntegerField(
        _('numero'),
        help_text=_('Número'),
    )
    fechaIngreso = models.DateField(
        _('fechaIngreso'),
        help_text=_('Fecha de ingreso'),
    )
    fechaNacimiento = models.DateField(
        _('fechaNacimiento'),
        help_text=_('Fecha de nacimiento'),
    )
    mail = models.EmailField(
        _('mail'),
        help_text=_('Mail'),
    )
    telefono = models.IntegerField(
        _('telefono'),
        help_text=_('Telefono'),
    )
    
class Exposicion(models.Model):
    fechaFin = models.DateField(
        _('fechafin'),
        help_text='Fecha de fin',
        blank=True
    )
    fechaFinReplanificada = models.DateField(
        _('fechaFinReplanificada'),
        help_text='Fecha de fin replanificada',
        blank=True
    )
    fechaInicio = models.DateField(
        _('fechaInicio'),
        help_text='Fecha de inicio'
    )
    fechaInicioReplanificada = models.DateField(
        _('fechaInicioReplanificada'),
        help_text='Fecha de inicio replanificada'
    )
    horaApertura = models.TimeField(
        _('horaApertura'),
        help_text='Hora de apertura'
    )
    horaCierre = models.TimeField(
        _('horaCierre'),
        help_text='Hora de cierre'
    )
    nombre = models.TextField(
        _('nombre'),
        help_text=_('Nombre de exposición'),
        max_length=200,
    )
    empleado = models.ForeignKey(
        Empleado,
        verbose_name=_('Empleado'),
        help_text=_('Empleado'),
        related_name= 'Empleado',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    def esVigente(self):
        if self.fechaFin or self.fechaFinReplanificada:
            return Exposicion

class Sede(models.Model):
    cantMaxVisitantes = models.IntegerField(
        _('cantMaxiVistantes'),
        help_text='Cantidad máxima de Vistantes'
    )
    cantMaxPorGuia = models.IntegerField(
        _('cantMaxPorGuia'),
        help_text='Cantidad máxima de Vistantes por guía'
    )
    nombre = models.TextField(
        _('nombre'),
        help_text=_('Nombre de la sede'),
        max_length=200,
    )
    exposicion = models.ForeignKey(
        Exposicion,
        verbose_name=_('Exposición'),
        help_text=_('Exposición'),
        related_name= 'Exposición',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    def mostra

class Tarifa(models.Model):
    fechaInicioVigencia = models.DateField(
        _('FechaIncioVigencia'),
        help_text='Fecha de incio de vigencia'
    )
    fechaFinVigencia = models.CharField(
        _('fechaFinVigencia'),
        help_text='Fecha de fin de vigencia',
        null=True
    )
    monto = models.DecimalField(
        _('monto'),
        help_text=_('Monto de la tarifa'),
        max_digits=15, 
        decimal_places=2,
        default = 0
    )
    montoAdicionalGuia = models.DecimalField(
        _('montoAdicionalGuia'),
        help_text=_('Monto adicional con guía'),
        max_digits=15, 
        decimal_places=2,
        default = 0
    )
    tipoDeEntrada = models.ForeignKey(
        TipoDeEntrada,
        verbose_name=_('Tipo de entrada'),
        help_text=_('Tipo de entrada'),
        related_name= 'TipoDeEntrada',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    tipoDeVisita = models.ForeignKey(
        TipoDevisita,
        verbose_name=_('Tipo de visita'),
        help_text=_('Tipo de visita'),
        related_name= 'TipoDeVisita',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    def esVigente(self):
        if self.fechaFinVigencia = null:
            return Tarifa

class Entrada(models.Model):
    fechaVenta = models.DateField(
        _('fechaVenta'),
        help_text='Fecha de venta'
    )
    horaVenta = models.TimeField(
        _('horaVenta'),
        help_text='Hora de venta'
    )
    monto = models.DecimalField(
        _('monto'),
        help_text=_('Monto de la entrada'),
        max_digits=15, 
        decimal_places=2,
        default = 0
    )
    numero = models.IntegerField(
        _('numero'),
        help_text='Numero de entrada'
    )
    empleado = models.ForeignKey(
        Empleado,
        verbose_name=_('Empleado'),
        help_text=_('Empleado'),
        related_name= 'empleado',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    sede = models.ForeignKey(
        Sede,
        verbose_name=_('Sede'),
        help_text=_('Sede'),
        related_name= 'sede',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    tarifa = models.ForeignKey(
        Tarifa,
        verbose_name=_('Tarifa'),
        help_text=_('Tarifa'),
        related_name= 'tarifa',
        on_delete=models.SET_NULL,
        blank = False,
        null = True    
    )

class Obra(models.Model):
    nombre = models.CharField(
        _('nombre'),
        help_text=_('Nombre de la obra'),
        max_length=200,
    )
    peso = models.IntegerField(
        _('peso'),
        help_text=_('Peso en kg')
    )
    valuacion = models.DecimalField(
        _('valuación'),
        help_text=_('Valuación en pesos'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    alto = models.IntegerField(
        _('alto'),
        help_text=_('Alto de la obra')
    )
    ancho = models.IntegerField(
        _('ancho'),
        help_text=_('Ancho de la obra')
    )
    descripcion = models.TextField(
        _('descripción'),
        help_text=_('Descripción de la obra')
    )
    fechaCreacion = models.DateField(
        _('FechaCreacion'),
        help_text=_('Fecha de creación de la obra')
    )
    fechaPrimerIngreso = models.DateField(
        _('FechaPrimerIngreso'),
        help_text=_('Fecha de primer ingreso de la obra')
    )
    duracionExtendida = models.DurationField(
        _('DuracionExtendida'),
        help_text=_('Duración extendida')
    )
    duracionResumida = models.DurationField(
        _('DuracionResumida'),
        help_text=_('Duración resumida')
    )

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return '{}'.format(self.nombre)

    def getDuracionExtendida(self):
        return self.duracionExtendida

class ReservaVisita(models.Model):
    cantidadAlumnos = models.IntegerField(
        _('cantidadAlumnos'),
        help_text=_('Cantidad de alumnos'),
    )
    cantidadAlumnosConfirmada = models.IntegerField(
        _('cantidadAlumnosConfirmada'),
        help_text=_('Cantidad de alumnos confirmada'),
    )
    duracionEstimada = models.IntegerField(
        _('duracionEstimada'),
        help_text=_('Duración estimada'),
    )
    fechaHoraCreacion = models.DateTimeField(
        _('fechaHoraCreacion'),
        help_text=_('Fecha y hora de creación'),
    )
    fechaHoraReserva = models.DateTimeField(
        _('fechaHoraReserva'),
        help_text=_('Fecha y hora de reserva'),
    )
    horaInicioReal = models.TimeField(
        _('horaInicioReal'),
        help_text=_('Hora de inicio real'),
    )
    horaFinReal = models.TimeField(
        _('horaFinReal'),
        help_text=_('Hora de fin real'),
    )
    numeroReserva = models.IntegerField(
        _('numeroRserva'),
        help_text=_('Numero de reserva'),
    )
    sede = models.ForeignKey(
        Sede,
        verbose_name=_('Sede'),
        help_text=_('Sede'),
        related_name= 'Sede',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )

class GestorVentaEntradas(models.Model):
    entrada = models.ForeignKey(
        Entrada,
        verbose_name=_('Entrada'),
        help_text=_('Entrada'),
        related_name= 'Entrada',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )