import pyautogui
import time
import requests



#posição da tela 
print(pyautogui.position())
print(pyautogui.size())

#funçoes do mouse
time.sleep(5)
#clicar no app do wthas 
pyautogui.click(x=478, y=1055)
time.sleep(2)
#clicar na barra de pesquisa 
pyautogui.click(x=216, y=144)
time.sleep(2)
#digitar na barra de pesquisa
pyautogui.write('AMOR')
time.sleep(2)
#clicar na conversa
pyautogui.click(x=220, y=241)
#clicar na barra de conversa 
pyautogui.click(x=769, y=989)
time.sleep(2)
#escrever na barra da conversa
time.sleep(2)
pyautogui.write('voce e muito gostosa msm (robo)')
#clicar para enviar a msg 
time.sleep(2)
pyautogui.click(x=1884, y=985)

