from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('posts/<post_id>', views.show, name="show-post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
