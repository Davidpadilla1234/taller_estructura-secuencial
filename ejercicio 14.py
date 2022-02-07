"""
Entradas:
lectura actual--->float--->lect2
lectura anterior--->float--->lect1
valor kw--->float--->valorkw
Salidas:
consumo--->float--->consumo
total factura-->flotante--->total
"""
lect2 = float ( entrada ( "Digite lectura real:" ))
lect1 = float ( entrada ( "Digite lectura anterior:" ))
valorkw = float ( input ( "Valor del kilowatio: " ))
consumo = ( lect2 - lect1 )
total = ( consumo * valorkw )
print ( "El valor a pagar es: " + str ( total ))