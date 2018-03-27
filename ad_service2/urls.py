from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sub_app/', include('sub_app.urls', namespace='sub_app')),

]

