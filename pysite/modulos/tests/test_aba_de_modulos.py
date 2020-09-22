from model_mommy import mommy
import pytest
from django.urls import reverse
from pysite.django_assertions import assert_contains
from pysite.modulos.models import Modulo

@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)

@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home'))
    return resp

def test_titulos_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)
