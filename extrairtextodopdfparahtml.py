# extrairtextodopdfparahtml.py
# pip install tika
from tika import parser
novo=""
achei=0
anterior=0
raw = parser.from_file('101FATOS.pdf')
texto = raw
print(texto)
for n in str(texto):
    if n =="}":
        achei = 1
    if anterior == 1 or achei == 0:
        anterior=0
        continue
    else:
        if n == "\\":
            novo = novo +"<br>"
            anterior=1
        else:
            novo = novo + n

resultado='texto.html'
file = open(resultado, 'w')
file.write('<html><header>Extraido</header><body>')

with open(resultado, 'a') as arquivo:
    print(novo, file=arquivo)

file = open(resultado, 'a')
file.write('</body></html>')
print("Fim")
