"""
Entradas:
Cantidad de naranjas ---> int ---> X
precio por docena--->float--->Y
valor venta--->float--->K
Salidas:
numero de docenas--->float--->docena
costo--->float--->precio
ganancia--->float--->ganancia
porcentaje ganancia--->float--->porcentaje
"""
X = int ( input ( "Numero de naranjas: " ))
Y = float ( input ( "Valor por docena: " ))
K = float ( entrada ( "Valor de las ventas: " ))
docenas = ( X / 12 )
precio = ( Y * docenas )
ganancia = ( K - precio )
porcentaje = (( ganancia * 100 ) / precio )
print ( "El porcentaje de ganancia es: " + str ( porcentaje ), "%" )