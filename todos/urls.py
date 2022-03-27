from django.urls import path
from todos.views import CreateTodoAPIView, ListTodoAPIView

urlpatterns = [
    path('create/', CreateTodoAPIView.as_view(), name='create-todo'),
    path('list/', ListTodoAPIView.as_view(), name='list-todo'),
]


