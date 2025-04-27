from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login/', permanent=False)),  # Redirect root to login
    path('', include('auth_app.urls')),  # Include auth URLs (register, login, logout)
    path('crud/', include('crud_app.urls')),  # Include CRUD URLs
]