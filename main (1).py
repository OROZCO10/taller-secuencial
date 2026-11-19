salarioBase = float(input("Ingrese el salario base del empleado: "))
aporteSalud = salarioBase *0.04
aportePension = salarioBase* 0.04
	
descuento = aporteSalud + aportePension
salarioNeto = salarioBase - descuento
	
print(("El aporte a salud es de " + str(aporteSalud)))
print("El aporte a pensión es de " + str(aportePension))
print("El descuento es de " + str(descuento))
print("El salario neto a pagar es " + str(salarioNeto))