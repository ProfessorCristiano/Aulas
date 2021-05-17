# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:17:19 2019
@author: cristiano_54549
"""
import os
'''
#falta testar o lambda no windows.... Linux para variar está 100%
if os.name == 'nt':
    import winsound
    beep = lambda freq, temp : winsound.Beep=(freq, temp)
else:
    # não esqueça do sudo apt install sox
    beep = lambda freq, temp : os.system('play -nq -t alsa synth {} sine {}'.format(freq, temp))
'''

beep = lambda freq, temp: os.system('play -nq -t alsa synth {} sine {}'.format(temp, freq))
nota=[440, 440, 440, 349, 523, 440, 349, 523, 440, 0, 659, 659, 659, 698, 523, 831, 349, 523, 440, 0, 880, 440, 440, 880, 831, 784, 740, 698, 740, 0, 466, 622, 587, 554, 523, 494, 523, 0, 349, 415, 349, 440, 523, 440, 523, 659, 880, 440, 440, 880, 831, 784, 740, 698, 740, 0, 466, 622, 587, 554, 523, 494, 523, 0, 349, 415, 349, 523, 440, 349, 523, 440]

inte=[500, 500, 500, 350, 150, 500, 350, 150, 650, 150, 500, 500, 500, 350, 150, 500, 350, 150, 650, 150, 500, 300, 150, 400, 200, 200, 125, 125, 250, 250, 250, 400, 200, 200, 125, 125, 250, 250, 125, 500, 375, 125, 500, 375, 125, 650, 500, 300, 150, 400, 200, 200, 125, 125, 250, 250, 250, 400, 200, 200, 125, 125, 250, 250, 250, 500, 375, 125, 500, 375, 125, 650]

if len(nota) != len(inte):
    print("ERRO")
else:
    print(len(nota))
    total=len(nota)

x = 0
for x in range (total):
    f=nota[x]
    t=inte[x]/1000
    beep(f, t)
    print(f,t)
print("FIM")
