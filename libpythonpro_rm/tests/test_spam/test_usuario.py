import pytest

from libpythonpro_rm.spam.modelos import Usuario
from spam.db import Conexao

@pytest.fixture
def conexao():
    return Conexao()

@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    return sessao_obj

def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome ='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()



def test_listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome ='Renzo'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()