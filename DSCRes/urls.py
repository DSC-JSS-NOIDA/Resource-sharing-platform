
from django.contrib import admin
from django.urls import path, include
from Resource import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Resource/', include('Resource.urls')),
    path('accounts/login/', views.login_view, name="login_view"),
    path('accounts/register/', views.register_view, name="register_view"),
    path('accounts/logout', views.logout_view, name="logout_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)