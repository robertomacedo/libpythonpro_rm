import pytest

from spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    return Conexao()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    return sessao_obj