# Arquivo principal (inicial) a ser executado.
# Quando iniciamos o projeto (carbonmail) ele é o primeiro ao Python executar.
# Nós usamos para ser o ponto de entrada da aplicação.

from carbonmail.email_sender.manager import iniatialize as init_sender

init_sender()

