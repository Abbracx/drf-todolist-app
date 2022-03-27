from django.urls import path
# from todos.views import CreateTodoAPIView, ListTodoAPIView
from todos.views import ListCreateTodoAPIView, DetailTodoAPIView

urlpatterns = [
    path('list-create/', ListCreateTodoAPIView.as_view(), name='todos'),
    path('retrieve/<int:id>/', DetailTodoAPIView.as_view(), name='detail'),
 ]


# path('create/', CreateTodoAPIView.as_view(), name='create-todo'),
#     path('list/', ListTodoAPIView.as_view(), name='list-todo'),