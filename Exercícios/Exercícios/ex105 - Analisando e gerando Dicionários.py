def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)

    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['media'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(0.5, 10, 6.5, sit=False)
print(resp)
