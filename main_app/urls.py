from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('lists/create/', views.ListCreate.as_view(), name="list_create"),
    path('lists/', views.ListIndex.as_view(), name="list_index"),
    path('lists/<int:pk>', views.ListDetail.as_view(), name="list_detail"),
    path('lists/<int:list_id>/todos/create',
         views.todo_create, name="create_todo")
]
