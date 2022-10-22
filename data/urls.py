from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('list/', views.DataListView.as_view(), name='list'),
]