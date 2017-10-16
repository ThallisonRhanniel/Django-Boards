from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board
#from ..views import board_topics
from ..views import TopicListView


class BoardTopicsTests(TestCase):
    def setUp(self): # adiciona dados no banco para efetuar os testes
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self): # verifica se está retornando error 404 para um valor que não existe
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self): # está testando se a url está chamando a view certa
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)


    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})

        response = self.client.get(board_topics_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
