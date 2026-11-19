dineroInvertido=float(input("Ingresa el dinero invertido: "))
Dias=float(input( "Ingresa los días: "))
porcentaje=float(input("Ingrese el porcentaje de intereses: "))
intereses = (dineroInvertido*porcentaje/100*Dias/360)
impuestos= intereses*0.07
pagar = dineroInvertido + intereses - impuestos
print("El valor de los intereses: ", intereses)
print("El valor de los impuestos es: ", impuestos)
print("El dinero neto a pagar es: ", pagar)
