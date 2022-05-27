from interpreter import draw
from chessPictures import *
domino=square.join(square.negative())
rpta=domino
for i in range (3):
	rpta=rpta.join(domino)
draw(rpta)