print("----calificaciones------")
cali= float(input("ingresa tus calificacion: "))
if cali >=100 :
    print("calificacion excelente")
elif cali <=99.99 and cali >=90:
    print("calificacion muy buena ")
elif cali <= 89.99 and cali >=80:
     print("calificacion buena")
elif cali <= 79.99 and cali>= 70:
    print("calificacion REGULAR")
elif cali <=69.99 and cali>= 60:
    print("calificacion sugiente ")
else:
    print("calificacion reprobatoria ")
