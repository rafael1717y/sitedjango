
import pytest
from django.urls import reverse
from pysite.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Site do Rafa - Home</title>')


## REVER ESSE TESTE
def test_home_link(resp):
    assert_contains(resp, f'href={reverse("base:home")}">Site do Rafa</a>')

