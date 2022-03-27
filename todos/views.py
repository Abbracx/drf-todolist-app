# from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.jwtauthenticate import JWTAuthentication
from todos.serializers import TodoSerializer
from todos.models import Todo


class ListCreateTodoAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class DetailTodoAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_fields = 'id'

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

# class CreateTodoAPIView(CreateAPIView):
#     serializer_class = TodoSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)

# class ListTodoAPIView(ListAPIView):
#     serializer_class = TodoSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     # queryset = Todo.objects.all()
#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)


