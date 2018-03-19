from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ui_app/', include('ui_app.urls', namespace='ui_app')),

]

