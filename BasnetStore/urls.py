from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import WelcomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', WelcomeView.as_view(), name='welcome'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
