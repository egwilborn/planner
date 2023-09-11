from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('lists/', views.ListCreate.as_view(), name="list_create")
]
