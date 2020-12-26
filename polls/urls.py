from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('<uuid:question_id>/', views.DetailView.as_view(), name='detail'),
    path('<uuid:question_id>/results/', views.ResultsView.as_view(), name='results'),
    path('<uuid:question_id>/vote/', views.vote, name='vote'),
]
