nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {} '.format(nome.upper()))
print('Seu nome em minúsculas: {} '.format(nome.lower()))

print('Seu nome tem ao todo {} letras '.format(len(nome)- nome.count(' ')))

# separa e conta apenas o primeiro nome
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras '. format(separa[0],len(separa[0])))
