"""
Entradas:
Capital-->flotante-->límite
tiempo-->int-->Tiempo
tasa-->float-->Tasa
Salidas:
Interés-->flotante-->Interés
Promedio-->float-->prom
"""
Cap = float ( input ( "Insertar capital: " ))
Tiempo = int ( input ( "Insertar el tiempo de inversión: " ))
Tasa = float ( input ( "Insertar la tasa de interés: " ))
Interés = (( Cap * Tasa * Tiem ) / 100 )
Prom = ( Interés / Tiempo )
print ( "El valor total de ineteres es: " +  str ( Interes ), " El porcentaje de interes por año es: " +  str ( Prom ), "%" )