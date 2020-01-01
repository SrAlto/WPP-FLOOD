from selenium import webdriver
import argparse
from selenium.webdriver.common.keys import Keys
import time as t
import os

parser = argparse.ArgumentParser(description='Ferramenta para flood em Whatsapp')
parser.add_argument('-m', help='Para setar a mensagem')
parser.add_argument('-n', help='Para setar o nome do grupo ou contato')
parser.add_argument('-b', help='Para setar o navegador ')
parser.add_argument ('-q', help='Para setar a quantidade de mensages')
parser.add_argument ('-t', help='Para setar a quantidade de segundos')
args = parser.parse_args()

print('''
 __        __  ____    ____      _____   _        ___     ___    ____    
   \      / / |  _ \  |  _ \    |  ___| | |      / _ \   / _ \  |  _ \   
  \ \ /\ / /  | |_) | | |_) |   | |_    | |     | | | | | | | | | | | |  
   \ V  V /   |  __/  |  __/    |  _|   | |___  | |_| | | |_| | | |_| |  
    \_/\_/    |_|     |_|       |_|     |_____|  \___/   \___/  |____/   
                                                                         


''')

navegador = args.b
name = args.n
mensagem = args.m
quantidade = int(args.q)
tempo = float(args.t)



print('Nome do grupo: '+name)
print('Mensagem: '+mensagem)
print('Quantidade: '+ str(quantidade))
print('Navegador: '+navegador.upper())
print('Tempo: '+ str(tempo))

if navegador == 'chrome':
	driver = webdriver.Chrome()
if navegador == 'firefox':
	driver = webdriver.Firefox()

driver.get('http://web.whatsapp.com')

yn = raw_input('Digite Y: ')

if yn == 'Y' or yn == 'y':
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_13mgZ')

    for i in range(quantidade):
        msg_box.send_keys(mensagem)
        t.sleep(float(tempo))
        msg_box.send_keys(Keys.ENTER)
	print('[*] MENSAGEM ENVIADA COM SUCESSO [*]')

    print('='*30)
    print('\nProcesso finalizado: '+str(quantidade)+' mensagens enviadas ao grupo ou contato: '+name+'\n')
    print('='*30)
