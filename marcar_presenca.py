import pyautogui
import subprocess
import time
import random
comando = "notify-send 'Chamada detectada' 'Executando script de marcação de presença...' --urgency=low "

# Executa o comando
subprocess.run(comando, shell=True, check=True)

comando = "xdotool search --name 'Mozilla Firefox' windowactivate"
subprocess.run(comando, shell=True, check=True)

pyautogui.hotkey('alt', '1')

screenWidth, screenHeight = pyautogui.size()
botao_responder = './BotaoResponder.png'

#botao_posicao = pyautogui.locateOnScreen(botao_responder)


# if botao_posicao is not None:
#     print("Botão encontrado na tela.")
#     botao_centro = pyautogui.center(botao_posicao)
#     pyautogui.click(botao_centro)
# else:
#     print("Botão não encontrado na tela.")


pyautogui.moveTo(screenWidth- 150, screenHeight - 90 , duration=0.5, tween=pyautogui.easeInOutQuad)
pyautogui.click()

def GetRandomMessage():
    strings = ["eu", "sim", "presente", "aqui"]
    return random.choice(strings)
time.sleep(15)

messageToSend = GetRandomMessage()
pyautogui.write(messageToSend, interval=0.03)

pyautogui.press('enter')
