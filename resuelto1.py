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

lista=[]
valor=int(input("Ingrese orden de la matriz escalar: "))
for i in range (valor):
  for j in range(valor):
    auxi=[]
    auxi.append(int(input("Ingrese valor: ")))
  lista.append(auxi)

if(esEscalar(lista)):
  print("La matriz es escalar")
else:
  print("La matriz no es escalar")


