op = 0


def menu():
  print()
  print("Hola >:)")
  print()
  print("------------Menu------------")
  print("1- convertor Centigrados a Fahrenheit")
  print("2- numeros Positivo o negativo?")
  print("3- numeros Par o impar?")
  print("4- Numeros a letras")
  print("5- Sumatoria de 5 numero")
  print("6- Salir")
  print("----------------------------")


def grados():
  c = float(input("pon los centigrados >:(  :"))
  f = ((c * 1.8) + 32)

  print("El Fahrenheit es >:(  :", f)
  return f


def moM():
  o = int(input("escoge un numero:"))
  if o > 0:
    print("El numero es positivo :)")
  else:
    print("El numero es negativo :(")

def par_o_impar():
  numero=int(input("introduce un numero entero: "))
  if numero % 2 == 0:
    print("el numero es impar.")
  else:
    print("el numero es par.")

def numero_a_letras():
  unidades = ['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']
  numeros= int(input("introduce un numero entre 0 y 9: "))
  if 0<= numeros<= 9:
    print("el numero en ltra es:", unidades[numeros])
  else:
    print("numero fuera del rango ")

def sumatrio(numero=None):
  cantidad = int(input("cuantos numeros deseas ingresar?"))
  numeros = []
  for i in range (cantidad):
    numeros= float(input(f'ingresa el numero {i+1}:'))
    numeros.append(numeros)
    print("los numeros ingresados son:", numeros)
    print("la sumatroria de los numeros es:",sum(numeros))




while op != 6:
  menu()
  op = int(input("escoge una opcion:"))
  if op == 1:
    grados()
  elif op == 2:
    moM()
  elif op == 3:
    par_o_impar()
  elif op == 4:
    numero_a_letras()
  elif op == 5:
    sumatrio()
  elif op == 6:
    print("saliendo del programa...")
    break
  else:
    print("opcion invalida")


