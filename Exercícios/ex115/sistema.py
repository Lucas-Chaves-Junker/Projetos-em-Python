from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['\033[34mVer pessoas cadastradas\033[m',
                     '\033[34mCadastrar novas pessoas\033[m',
                     '\033[34mSair do sistemas\033[m '])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo!
        leitura(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo')
        break
    else:
        cabecalho('\033[31mERRO: Digite uma opção valida\033[m')
    sleep(1)
