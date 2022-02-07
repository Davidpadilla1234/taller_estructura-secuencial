"""""
Entradas:
precio de contado--->float--->P
valor de la cuota mensual--->float--->T
Salidas:
precio cuotas--->float--->precioc
recargar--->flotar--->recargar
porcentaje de recargo--->float--->porcentaje
"""
P = float ( entrada ( "Precio de contado:" ))
T = float ( entrada ( "Valor de la cuota mensual: " ))
precioc = ( T * 12 )
recargo = ( precioc - P )
porcentaje = (( recarga * 100 / P ))
print ( "El porcentaje de recarga es: " + str ( porcentaje ), "%" )