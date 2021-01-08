from libpythonpro_rm.spam.main import EnviadorDeSapm


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSapm(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantástcios'
    )