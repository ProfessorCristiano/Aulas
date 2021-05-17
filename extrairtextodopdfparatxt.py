# extrairtextodopdfparatxt.py
# pip install tika
from tika import parser
resultado='texto.txt'
raw = parser.from_file('101FATOS.pdf')
texto = str(raw['content'])
#print(texto)
with open(resultado, 'a') as arquivo:
    print(texto, file=arquivo)
print("Fim")
