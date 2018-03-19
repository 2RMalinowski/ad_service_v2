from django.urls import path
from ui_app import views

app_name = 'ui_app'

urlpatterns = [
    path('', views.answer_list, name='answer_list'),
    path('<int:year>/<int:month>/<int:day>/', views.answer_detail, name='answer_detail'),
]
