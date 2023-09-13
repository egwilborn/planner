from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('lists/create/', views.ListCreate.as_view(), name="list_create"),
    path('lists/', views.ListIndex.as_view(), name="list_index"),
]
