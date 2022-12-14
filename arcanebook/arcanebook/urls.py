
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from froala_editor import views

urlpatterns = [
    path('',include('blogs.urls')),
    path('admin/', admin.site.urls),
    path('froala_editor/',include('froala_editor.urls')),
    path('api/',include('blogs.api_urls')),

    
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
