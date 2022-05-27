from interpreter import draw
from chessPictures import *

fragmento=knight.join(knight.negative())
fragmentoVerti=fragmento.verticalMirror()
draw(fragmentoVerti.up(fragmento))