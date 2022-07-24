from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Board


class BoardListAPIViewTestCase(APITestCase):
    def test_board_list(self):
        Board.objects.create(title="hello", content="world")
        
        url = reverse('board_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)


class BoardCreateAPIViewTestCase(APITestCase):
    def test_board_create(self):
        url = reverse('board_list')
        response = self.client.post(url, data={'title': 'hello', 'content': 'world'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['title'], 'hello')
        self.assertEqual(Board.objects.count(), 1)

