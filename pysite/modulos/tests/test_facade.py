from pysite.modulos import facade
import pytest
from pysite.modulos.models import Modulo
from pysite.django_assertions import assert_contains
from model_mommy import mommy

@pytest.fixture
def modulos(db):
    return [mommy.make(Modulo, titulo=s) for s in 'Antes Depois'.split()]

def test_lista_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.titulo)) == facade.listar_modulos_ordenados()
