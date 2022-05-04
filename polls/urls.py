from django.urls import path
from polls import views

app_name='polls'

urlpatterns = [

    path('', views.index, name='index'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/<int:question_id>/results/', views.results, name='results'),
]
