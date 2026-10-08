Algoritmo  interes 
	definir  vlintereses,dinero, porcentajeinteres, Periodo, pago como real
	escribir "cantidad de dinero invertido"
	leer dinero 
	escribir "porcentaje de intereses"
	leer intereses 
	escribir "periodo en dias"
	leer periodo
	escribir "intereses son" 

	impuestos= valorIntereses*0.07 
	pagar=dinero+valorintereses-impuestos
	vintereses= (dinero*intereses/100)* periodo/360
	escribir "los intereses son", valorintereses 
	escribir "los impuestos son", impuestos
	escribir " el valor a pagar" , pago
	
	
	

FinAlgoritmo
