from interpreter import draw
from chessPictures import *
dominoArriba=square.join(square.negative())
dominoAbajo=square.negative().join(square)
cuadrado=dominoAbajo.up(dominoArriba)
rpta=cuadrado
for i in range (3):
	rpta=rpta.join(cuadrado)

for i in range (2):
	rpta=rpta.up(rpta)

draw(rpta)