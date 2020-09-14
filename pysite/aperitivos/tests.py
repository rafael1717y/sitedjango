from django.test import TestCase
import pytest
from django.urls import reverse
from pysite.django_assertions import assert_contains

@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))

def test_status_code(resp):
    assert resp.status_code==200

def test_titulo_video(resp):
    assert_contains(resp, '<h1>Video Aperitivo: Motivação</h1>'

'''## colocar o video aqui
def test_conteudo_video(resp):
     assert_contains(resp, '<iframe src="https://player.vimeo.com/video/251224475"'>'
'''

