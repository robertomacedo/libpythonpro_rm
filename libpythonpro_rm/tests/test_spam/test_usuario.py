from libpythonpro_rm.spam.modelos import Usuario
from spam.db import Conexao


def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome ='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuario(conexao=None):
    conexao = Conexao()
    sessao = conexao.gerar_sessao()email='renzo@python.pro.br'
    usuarios = [Usuario(nome ='Renzo',email='renzo@python.pro.br'),
                Usuario(nome='Luciano',email='luciano@python.pro.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()