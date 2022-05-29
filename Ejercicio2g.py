from interpreter import draw
from chessPictures import *

principal=[rock,knight,bishop,queen,king,bishop,knight,rock]

filaBlanca=rock
peonesBlancos=pawn
peonesNegros=pawn.negative()
filaNegra=rock.negative()

for i in range(1,len(principal)):
	filaBlanca=filaBlanca.join(principal[i])
	filaNegra=filaNegra.join(principal[i].negative())
	peonesNegros=peonesNegros.join(pawn.negative())
	peonesBlancos=peonesBlancos.join(pawn)

#Ejercicio 2d usado 
domino=square.join(square.negative())
lineaStartBlanco=domino.join(domino).join(domino).join(domino)

#Ejercicio 2e usado
domino=domino.negative()
lineaStartNegro=domino.join(domino).join(domino).join(domino)

#Ejercicio 2f usado
dominoArriba=square.join(square.negative())
dominoAbajo=square.negative().join(square)
cuadrado=dominoAbajo.up(dominoArriba)
tablero=cuadrado
for i in range (3):
	tablero=tablero.join(cuadrado)

tablero=tablero.up(tablero)

filaN=lineaStartBlanco.under(filaNegra)
filaB=lineaStartNegro.under(filaBlanca)
peonesN=lineaStartNegro.under(peonesNegros)
peonesB=lineaStartBlanco.under(peonesBlancos)

completo=filaB.up(peonesB).up(tablero).up(peonesN).up(filaN)
draw(completo)
