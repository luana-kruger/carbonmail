# É onde fica o código para a Interface Gráfica
# Tudo que existir de visual vai ficar aqui 
# É principalmente aqui que usaremos o PySimpleGUI (que cria a interface gráfica)

from carbonmail.email_sender.view import get_window
import PySimpleGUI as sg
from carbonmail.utils import inner_element_space

lista = ['Administradores', 'Alunos']

def get_layout():

    frame_list = [
        inner_element_space(600),
        [
            sg.Text('Selecione a lista: '),
            sg.Combo(lista, default_value=lista[1], key='-List-')
        ],

        [
            sg.Text('Criar uma lista: '),
            sg.In(key='-ListName-'),
            sg.Button('Criar', key='-Create-', size=(10,1))
        ],

        [
            sg.Button('Deletar a Lista', key='-Delete-', size=(15,1), pad=((5, 5), (7, 7))),
            sg.Button('Mostrar Contatos', key='-Show-', size=(15,1), pad=((5, 5), (7, 7)))
        ],
        inner_element_space(600),
    ]

    frame_import = [
        inner_element_space(600),
        [
            sg.Text('Selecionar o arquivo (CSV):', tooltip='Cabeçalhos: name e email'),
            sg.In(key='-CSV-'),
            sg.FileBrowse('Selecionar', file_types=(("CSV", "*.csv"),), tooltip='Cabeçalhos: name e email')
        ],

        [
            sg.Button('Importar Contatos', key='-Import-', size=(15, 1), pad=((5, 5), (7, 7)))
        ],
        inner_element_space(600),
    ]

    frame_add = [
        inner_element_space(600),
        [
            sg.Text('Innsira o Nome:'),
            sg.In(key='-Name-'),
        ],

        [
            sg.Text('Innsira o E-mail:'),
            sg.In(key='-Email-')
        ],

        [
            sg.Button('Adicionar Contanto', key='-Add-', size=(15, 1), pad=((5, 5), (7, 7)))
        ]
    ]

    layout = [
        [
            sg.Frame('Configurações da Lista', frame_list, element_justification='c')
        ],

        [
            sg.Frame('Importar Contatos', frame_import, element_justification='c')
        ],

        [
            sg.Frame('Adicionar Contato', frame_add, element_justification='c')
        ],

        [
            sg.Button("Voltar", key='-Back-', size=(15, 1), pad=((5, 5), (7, 7)))
        ]
    ]

    return layout

def get_window():
    # pysimplegui themes
    sg.theme("DarkPurple")
    return sg.Window('Editor de Lista', get_layout(), element_justification='c')