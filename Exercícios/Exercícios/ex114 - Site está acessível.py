import urllib.request

try:
    url = urllib.request.urlopen('http://www.pudim.com.br/')

except :
    print('\033[33mNão consegui acessar o site pudim \033[m')
else:
    print('\033[33mConsegui acessar o site pudim \033[m')
