from django.urls import path
from usuario.views import registro, login, logout, home
#from usuario import views as usuario_views

urlpatterns = [
    path('registro', registro),
    path('login', login),
    path('logout', logout),
    path('', home),

]