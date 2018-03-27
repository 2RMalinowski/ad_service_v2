from django.urls import path
from sub_app import views

app_name = 'sub_app'

urlpatterns = [
    # path('', views.answer_list, name='answer_list'),
    path('', views.AnswerListView.as_view(), name='answer_list'),
    path('<int:year>/<int:month>/<int:day>/\<answer>', views.answer_detail, name='answer_detail'),
]