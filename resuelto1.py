def esEscalar(m):
  d = m[0][0]
  for i in range(len(m)):
    for j in range(len(m)):
      if i != j:
        if m[i][j] != 0:
          print(m[i][j])
          return False
      elif m[i][j] != d:
        print(m[i][j])
        return False
  return True

def esUnitaria(m):
  return m[0][0] == 1 and esEscalar(m)


lista=[]
valor=int(input("Ingrese orden de la matriz escalar: "))
for i in range (valor):
  auxi=[]
  for j in range(valor):
    auxi.append(int(input("Ingrese valor: ")))
  lista.append(auxi)

print("esta es la lista: ")
print(lista)
if(esEscalar(lista)):
  print("La matriz es escalar")
else:
  print("La matriz no es escalar")
if(esUnitaria(lista)):
  print("La matriz es unitaria")
else:
  print("La matriz no es unitaria")


