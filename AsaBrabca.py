# -*- coding: utf-8 -*-
"""
Created on Jun 25 2021
@author: cristiano
"""
import os
'''
# Era para ser um programa cross Windows / Linux, mas não testei ainda no Windows
if os.name == 'nt':
    import winsound
    beep = lambda freq, temp : winsound.Beep=(freq, temp * 1000)
else:
    # não esqueça do sudo apt install sox
    beep = lambda freq, temp : os.system('play -nq -t alsa synth {} sine {}'.format(freq, temp))
'''
beep = lambda freq, temp: os.system('play -nq -t alsa synth {} sine {}'.format(temp, freq))

# Confirmar a nota14 F5 698. tá fora de tom
# t é a velocidade básica.USB
t=120
x1=t
x2=t*2
x3=t*3
x4=t*4
x5=t*5

nota=[392, 440, 494, 587, 587, 494,
  523, 523, 392, 440,
  494, 587, 587, 523,

  494, 0, 392, 392, 440,
  494, 587, 0, 587, 523, 494,
  392, 523, 0, 523, 494, 440,

  440, 494, 0, 494, 440, 392,
  392, 0, 392, 392, 440,
  494, 587, 0, 587, 523, 494,

  392, 523, 0, 523, 494, 440,
  440, 494, 0, 494, 440, 392,
  392, 698, 587, 659, 523, 587, 494,

  523, 440, 494, 392, 440, 392, 330, 392,
  392, 698, 587, 659, 523, 587, 494,
  523, 440, 494, 392, 440, 392, 330, 392,
  392, 0]
inte=[x2,x2,x3,x3,x3,x3,
      x3,x4,x2,x2,
      x3,x3,x3,x3,

      x4,x2,x2,x2,x2,
      x3,x3,x2,x2,x2,x2,
      x3,x3,x2,x2,x2,x2,

      x3,x3,x2,x2,x2,x2,
      x4,x2,x2,x2,x2,
      x3,x3,x2,x2,x2,x2,

      x3,x3,x2,x2,x2,x2,
      x3,x3,x2,x2,x2,x2,
      x3,x2,x2,x2,x2,x2,x2,

      x2,x2,x2,x2,x2,x2,x2,x2,
      x3,x2,x2,x2,x2,x2,x2,
      x2,x2,x2,x2,x2,x2,x2,x2,
      x5,x3]

'''
# Era um teste para ver se a sequencia de notas era igual a sequencia de intervalos, vai que eu tinha pulado um...
if len(nota) != len(inte):
    print("ERRO")
else:
    print(len(nota))
'''
total=len(nota)
x = 0
for x in range (total):
    f=nota[x]
    # A maioria das notações trabalha com milisegundos, o alsa com segundos, por isso a divisão
    t=inte[x]/1000
    beep(f, t)
    print(f, t)
print("FIM")
