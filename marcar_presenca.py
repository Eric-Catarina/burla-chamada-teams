import pyautogui
import subprocess
import time

comando = "notify-send 'Chamada detectada' 'Executando script de marcação de presença...' --urgency=low "

# Executa o comando
subprocess.run(comando, shell=True, check=True)

comando = "xdotool search --name 'Mozilla Firefox' windowactivate"
subprocess.run(comando, shell=True, check=True)

pyautogui.hotkey('alt', '1')

screenWidth, screenHeight = pyautogui.size()
botao_responder = './BotaoResponder.png'

botao_posicao = pyautogui.locateOnScreen(botao_responder, confidence=0)


if botao_posicao is not None:
    botao_centro = pyautogui.center(botao_posicao)
    pyautogui.click(botao_centro)
else:
    print("Botão não encontrado na tela.")
    pyautogui.moveTo(screenWidth- 150, screenHeight - 90 , duration=0.5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()

time.sleep(10)
pyautogui.write('presente', interval=0.03)
pyautogui.press('enter')