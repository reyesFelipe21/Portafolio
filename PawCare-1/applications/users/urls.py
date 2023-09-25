
from django.urls import path


from django.contrib.auth import views as auth_views
from .views import *

from .forms import UserPasswordResetForm
from .views import View
from . import views
app_name ="users_app"


urlpatterns = [
    path('registro/', UserRegisterView.as_view(),name='user_register'),
    path('login/', LoginUser.as_view(),name='user_login'),
    path('logout/', LogoutView.as_view(),name='user_logout'),
    path('servicios/', ListCuidadores.as_view(),name='cuidadores'),
    path('users/<username>', PerfilDetailView.as_view(),name='profile'),
    path('calendario/',CalendarioView.as_view(), name= 'calendario'),
    path('horas/',Addhoras.as_view(), name= 'horas'),
    path('list_mascota/', ListMascotas.as_view(), name='mascota'),
    path('list_mascota/<id>', ListMascotas2.as_view(), name='mascota'),
    path('crear_mascota/',AddMascota.as_view(), name='crear_mascota'),
    path('mascota_modificar/<int:pk>', ModificarMascota.as_view(),name='mascota_modificar'),
    path('mascota_eliminar/<int:pk>', MascotaDeleteView.as_view(),name='mascota_eliminar'),
    path('update/<int:pk>', PerfilUpdateView.as_view(),name='update'),

    path('list_horas/', ListCronogramaDisponibles.as_view(), name='horaseliminar'),
    path('cronograma_eliminar/<int:pk>', CronogramaDeleteView.as_view(),name='cronograma_eliminar'),

    path('servicios/', ListCuidadores.as_view(),name='cuidadores'),

  

    path('servicios/<int:id>', ListCuidadores3.as_view(),name='cuidadores3'),
    
    path('servicios/<id>', ReservaRegisterView.as_view(),name='cuidadores3'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', form_class=UserPasswordResetForm,html_email_template_name ='users/password_reset_email.html'), name='password_reset'),
    path('api/mascota/por-usuario/', ListMascotaUser.as_view(),name='mascota-mascota-by-user'),

    path('vista_reserva/',ClienteResevarView.as_view(), name= 'vista_reserva'),

    path('list_user_admin/', ListUser.as_view(), name='usuarios_admin'),
    path('list_user_admin/<id>', ListUser2.as_view(), name='usuarios_admin_s'),
    path('user_modificar/<int:pk>', ModificarUser_admin.as_view(),name='user_modificar'),


    path('list_servicio_admin/', ListServicios.as_view(), name='servicios_admin'),
    path('list_servicio_admin/<id>', ListServicios2_admin.as_view(), name='servicios_admin_s'),
    path('crear_servicios/',AddServicios_admin.as_view(), name='crear_servicio'),
    path('servicio_modificar/<int:pk>', ModificarServicio_admin.as_view(),name='servicio_modificar'),
    path('servicio_eliminar/<int:pk>', ServicioDeleteView.as_view(),name='servicio_eliminar'),

    path('list_especie_admin/', ListEspecies.as_view(), name='especie_admin'),
    path('list_especie_admin/<id>', ListEspecies2_admin.as_view(), name='especie_admin_s'),
    path('crear_especie/',AddEspecies_admin.as_view(), name='crear_especie'),
    path('especie_modificar/<int:pk>', ModificarEspecie_admin.as_view(),name='especie_modificar'),
    path('especie_eliminar/<int:pk>', EspecieDeleteView.as_view(),name='especie_eliminar'),

    path('reservar_cuidador/<int:cronograma_id>', views.reservar_cuidador, name='reservar_cuidador'),
    
    path('list_horas_user/', HorasporUserList.as_view(), name='horas_user'),

    path('list_horas_realizadas_user/', HorasRealizadasporUserList.as_view(), name='horas_user_realizadas'), #esta

    path('cancelar_cuidador/<int:idReserva>', views.cancelar_cuidador, name='cancelar_cuidador'),
    path('finalizar_reserva/<int:idReserva>', views.finalizar_reserva, name='finalizar_reserva'),
    #path('rating_modal/', views.rating_modal , name='rating_modal'),
    path('rating_modal/', Calificacion.as_view() , name='rating_modal'),
    path('finalizar_reserva/<int:idReserva>/', views.finalizar_reserva, name='finalizar_reserva'),

    path('guardar_calificacion/', views.guardar_calificacion, name='guardar_calificacion'),
    #path('calcular_promedio_calificacion/', views.calcular_promedio_calificacion, name='calcular_promedio_calificacion'),
]

