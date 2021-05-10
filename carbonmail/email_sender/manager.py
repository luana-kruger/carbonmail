# Onde estarão todas as funções deste pacote.
# Ele é quem vai coodernar este pacote (gerenciador)

def iniatialize():
    from carbonmail.email_sender import Email_Sender

    ems = Email_Sender()
    ems.enable_window()