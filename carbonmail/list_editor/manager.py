# Onde estarão todas as funções deste pacote.
# Ele é quem vai coodernar este pacote (gerenciador)

def iniatialize(email_sender):
    from carbonmail.list_editor import List_Editor

    ems = List_Editor(email_sender)
    ems.enable_window()