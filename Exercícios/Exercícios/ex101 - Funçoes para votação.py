def voto(ano=0):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return print(f'Com {idade} anos: VOTO NEGADO')
    if 16 <= idade < 18 or idade > 70:
        return print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATORIO')


nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
