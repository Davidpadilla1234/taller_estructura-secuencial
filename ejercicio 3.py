"""
Entradas
Venta-->flotador-->Venta
salidas
Descuento-->flotante-->D
Valor total-->flotante-->total
"""
Venta = float ( input ( "Digite la venta: " ))
D = ( Venta * 0.15 )
total = ( Venta - D )
print ( "valor de descuento: " + str ( D ), " valor a pagar: " + str ( total ))