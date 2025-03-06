from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "topic"

urlpatterns = [

    path("<int:Topic_id>", views.hpage, name='hpage'),

    path("new_topic", views.new_topic, name='new_topic'),

    path('<int:topic_id>/upload', views.fazer_upload, name="fazer_upload"),

    path('<int:topic_id>/delete', views.delete_topic, name="delete_topic"),

    path('<int:topic_id>/alterar', views.alterar_topic, name="alterar_topic"),


]
