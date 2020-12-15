import pytest

from libpythonpro_rm.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['renzo@python.pro.br', 'food@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'luciano@python.pro.br',
        'Curso Python Pro',
        'Turma Gido Von Rossun aberta'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'renzo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'luciano@python.pro.br',
            'Curso Python Pro',
            'Turma Gido Von Rossun aberta'
        )
        assert remetente in resultado
