#lista
milista=["banderas","tachos","guates","uniforme","termo","balon"]
print(milista)
for elementos in milista:
    print(elementos)

milista.append("rodillera")
print(milista)

milista.remove("termo")
print(milista)

for i in range(milista):
    print(i)
    break
