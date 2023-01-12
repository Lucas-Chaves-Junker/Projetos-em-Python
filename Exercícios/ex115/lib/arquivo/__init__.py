from ex115.lib.interface import *


# manipulando arquivos
def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        arquivo = open('cadastro.txt', 'wt+')
        arquivo.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def leitura(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            arquivo.close()
