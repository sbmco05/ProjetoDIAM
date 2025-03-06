from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="forum"

urlpatterns = [

    path("base", views.base, name='base'),

    path("login", views.dologin, name='dologin'),

    path("registo/", views.registo, name='registo'),

    path('', views.index, name='index'),

    path('perfil', views.ver_perfil, name='perfil'),

    path('fazlogout', views.fazlogout, name='fazlogout'),

    path('login/', views.dologin, name='login'),
]
