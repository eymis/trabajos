
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print("La suma de todos los números del 1 al 100 es:", total)


numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
