# É onde fica o código para a Interface Gráfica
# Tudo que existir de visual vai ficar aqui 
# É principalmente aqui que usaremos o PySimpleGUI (que cria a interface gráfica)

import PySimpleGUI as sg
from carbonmail.utils import inner_element_space

# Window =>  Janela
# Layout =>  O que vai mostrar na janela 
#        ==> Listas de listas: Cada sublista é uma "linha" da janela e cada elemento é um componente visual

lista = ['Administradores', 'Alunos']
def get_layout():

    frame_campaign = [
        inner_element_space(500),
        [
            sg.Text('Selecione o código'),
            sg.In(key='-Code-', size=(30, 1)),
            sg.FileBrowse("Selecionar", file_types=(("Códigos Python", "*.py"), ))
        ],

        [
            sg.Text('Selecione a lista de destinatários'), 
            sg.Combo(lista, default_value=lista[1], key='-Lists-')
        ],

        inner_element_space(500),
    ]

    frame_email = [
        inner_element_space(500),

        [
            sg.Text('Insira o Título', font=("Helvetica 15")),
        ],

        [
            sg.In(key='-Title-', size=(62, 10))

        ],

        [
            sg.Text('Insira o Conteúdo', font=("Helvetica 15")),
        ],

        [
            sg.MLine(key='-Content-', size=(62, 10))
        ],

        inner_element_space(500),
    ]


    layout = [
        inner_element_space(500),
        [
            sg.Frame('Configurações da Campanha', frame_campaign, element_justification='c')
        ],

        [
            sg.Frame('Configurações do E-mail', frame_email, element_justification='c')
        ],

        [
            sg.Button('Enviar E-mail', key='-Send-', size=(15, 1), pad=(10, (10, 0))),
            sg.Button('Gerenciar Listas', key='-ListEditor-', size=(15, 1), pad=(10, (10, 0))),
        ],
        inner_element_space(500),
    ]

    return layout

def get_window():
    sg.theme("DarkPurple")
    return sg.Window('Enviador de Email', get_layout(), element_justification='c')