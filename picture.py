from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """ 
    return Picture(self.img[::-1])

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    auxi=[]
    for i in range (len(self.img)-1,-1,-1):
      auxi.append(self.img[i])
    return Picture(auxi)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    auxi=[]
    for i in range(len(self.img)):
      auxi2=[]
      for j in range(len(self.img[i])):
        auxi2.append(0)
      auxi.append(auxi2)

    for i in range(len(self.img)):
      for j in range (len(self.img[i])):
        auxi[i][j]=self._invColor(self.img[i][j])

    return Picture(auxi)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    auxi=[]
    for i in range(len(self.img)):
      auxi.append(self.img[i]+p.img[i])

    return Picture(auxi)

  def up(self, p):
    auxi=[]
    for i in range(len(p.img)):
      auxi.append(p.img[i])
    for i in range(len(self.img)):
      auxi.append(self.img[i])
    return Picture(auxi)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    auxi=[]
    for i in range(len(self.img)):
      auxi.append(self.img[i])
    for i in range(len(p.img)):
      auxi.append(p.img[i])
    
    return Picture(auxi)   
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    auxi=self
    for i in range(n-1):
      auxi=self.join(auxi)
    return Picture(auxi.img)

  def verticalRepeat(self, n):
    copia=[]
    rpta=[]
    for i in range (len(self.img)):
      copia.append(self.img[i])
    for j in range (n):
      rpta+=copia
    return Picture(rpta)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
  
