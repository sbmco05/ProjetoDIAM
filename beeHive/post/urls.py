from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="post"

urlpatterns = [

    path("<int:topic_id>/new_post", views.new_post, name='new_post'),

    path("<int:topic_id>/<int:post_id>", views.post_page, name='post_page'),

    path("<int:topic_id>/<int:post_id>/comment/", views.new_comment, name='new_comment'),

    path("<int:topic_id>/<int:post_id>/edit", views.alterar_post, name='alterar_post'),

    path("<int:topic_id>/<int:post_id>/upload", views.post_upload, name='upload_post'),

    path('<int:topic_id>/<int:post_id>/delete', views.delete_post, name="delete_post"),

    path('<int:topic_id>/<int:post_id>/like', views.like_post, name="like_post"),

    path('<int:topic_id>/<int:post_id>/dislike', views.dislike_post, name="dislike_post"),

]
