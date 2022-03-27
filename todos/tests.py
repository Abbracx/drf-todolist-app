from django.http import response
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from todos.models import Todo

class TestListCreateTodos(APITestCase):

    def authenticate(self):
        self.client.post(reverse('register'), {'username':'username', 'email':'email@gmail.com', 'password':'password'})
        resp = self.client.post(reverse('login'), {'email':'email@gmail.com', 'password':'password'})
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {resp.data['token']}")


    # Anytime we inherit from apitestcase we get access to a client
    def test_should_fail_create_todo_with_no_auth_user(self):
        sample_todo = {'title':'Hello world', 'desc':'Test', }
        resp = self.client.post(reverse('todos'), sample_todo)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)


    def test_should_create_todo_with_auth_user(self):
        previous_todo_count = Todo.objects.all().count()
        self.authenticate()
        sample_todo = {'title':'Hello world', 'desc':'Test', }
        resp = self.client.post(reverse('todos'), sample_todo)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.all().count(), previous_todo_count + 1)
        self.assertEqual(resp.data['title'], sample_todo.get('title'))
        self.assertEqual(resp.data['desc'], sample_todo.get('desc'))

    def test_retrieves_all_todos(self):
        self.authenticate()
        resp = self.client.get(reverse('todos'))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsInstance(resp.data['results'], list)

        sample_todo = {'title':'Hello world', 'desc':'Test', }
        self.client.post(reverse('todos'), sample_todo)

        res = self.client.get(reverse('todos'))
        self.assertIsInstance(res.data['count'], int)
        self.assertEqual(res.data['count'], 1)


