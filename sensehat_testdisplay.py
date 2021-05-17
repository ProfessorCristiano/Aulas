# sensehat_testdisplay.py
# Na aplicação use sense_hat no emulador use sense_emu https://sense-emu.readthedocs.io/en/v1.0/install.html
# from sense_hat import SenseHat
from sense_emu import SenseHat
import time

# instanciamos o objeto hat como membro da classe Sensehat
hat = SenseHat()

#Variáveis preparadas para facilitar a utilização
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

#limpamos o display
hat.clear()

# preenchemos uma lista de 64 posições com os valores de red
pixels = [red for i in range(64)]
# descomente o print abaixo para visualizar no terminal
#print(pixels)

# aplicamos a lista completa no display e atualizamos
hat.set_pixels(pixels)

#espera para dar tempo de ver na tela
time.sleep(2.5)

hat.clear()

# preenchemos até a posição 32 da lista com valor blue e o restante com green
pixels = [blue if i < 32 else green for i in range(64)]

#atualizamos os valores no display
hat.set_pixels(pixels)
time.sleep(2.5)

# agora manipulamos os itens da lista individualmente
# primeiro apagamos a posição 27 da lista
del pixels[27]
# depois inserimos na posição 27 o valor white
pixels.insert(27, white)

#atualizamos os valores no display
hat.set_pixels(pixels)
time.sleep(2.5)

# primeiro apagamos a posição 36 da lista
del pixels[36]
# depois inserimos na posição 36 o valor white
pixels.insert(36, white)
#atualizamos os valores no display
hat.set_pixels(pixels)
time.sleep(2.5)

# descomente a linha abaixo print final no terminal para o programados entender o que aconteceu
#print(pixels)



# Aqui vamos fazer as inserções de modo individualmente
# perceba que o método é set_pixel,
# antes era set_pixels
# a diferença é que o primeiro (set_pixels) atualiza a lista inteira
# e se basei em posições de 0 à 63

# Já o segundo (set_pixel) pracisa de duas informações de posição
# um valor para coluna
# outro para linha
# só depois os valores das cores em RGB

#setamos o pixel da coluna 0 e linha 0 com os valores RGB 255, 255, 255
hat.set_pixel(0, 0, 255, 255, 255)
time.sleep(2.5)
hat.set_pixel(7, 0, 255, 255, 255)
time.sleep(2.5)
# Os valores em RGB também funcionam para os valores predefinidos nas linhas 8 à 11
hat.set_pixel(0, 7, white)
time.sleep(2.5)
hat.set_pixel(7, 7, white)
time.sleep(2.5)
# Os mesmos que setamos de branco com a lista
# agora pintaremos de vermelho de forma individual
hat.set_pixel(3, 3, red)
time.sleep(2.5)
hat.set_pixel(4, 4, red)
time.sleep(2.5)
