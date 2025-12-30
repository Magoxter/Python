# Programa para pular o botão Youtube automaticamente
import pyautogui
import time
import cv2
# Instalar biblioteca cmd -> pip install pyautogui

# Caminho da Imagem
imagem = "files/pular.png"

# Loop Verificação
while True:
	try:
		posicao = pyautogui.locateOnScreen(imagem,confidence=0.8)

		if posicao:
			time.sleep(2)

	time.sleep(1)	
