
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('accounts.urls'), name='signin'), # forwarded to accounts.urls
    path('admin/', admin.site.urls), # path for admin panel
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) #for media file
