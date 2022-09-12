import PySimpleGUI as sg

# Criar as janelas e estilos(layout)
def janela_login():
    sg.theme('DarkBlue4')
    layout = [
        [sg.Text('Nome'),sg.Input(key='nome',size=(25,3))],
        [sg.Text('Senha'),sg.Input(key='senha',size=(25,3))],
        [sg.Button('Enter'),sg.Button('Sair')] 
    ]
    return sg.Window('Login', layout=layout,finalize=True)

def janela_cadastro():
    sg.theme('DarkBlue4')
    layout = [
        [sg.Text('      Id'), sg.Input(key='id',size=(30,3))],
        [sg.Text('')],
        [sg.Text('    NOME'), sg.Input(key='nome',size=(30,3))],
        [sg.Text('')],
        [sg.Text('     CPF'), sg.Input(key='cpf',size=(30,3))],
        [sg.Text('')],
        [sg.Text('TELEFONE'), sg.Input(key='telefone',size=(30,3))],
        [sg.Text('')],
        [sg.Button('Adicionar'),sg.Button('Pesquisar'),sg.Button('Alterar'),sg.Button('Excluir')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Tela de cadastro',layout=layout,finalize=True)
# Criar  as janelas iniciais
janela1,janela2 = janela_login(), None
# Criar um loop de leituras de eventos
while True:
    window,event,values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # Quando queremos ir para próxima janela
    if window == janela1 and event == 'Enter':
        janela2 = janela_cadastro()
        janela1.hide()
    # Quando queremos voltar para janela anterior
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
        
# Lógica de o que deve acontecer ao clicar os botões
