"""
Entradas:
Ladoa-->flotador-->a
ladob-->flotante-->b
ladoc-->flotante-->c
salidas:
semiperimetro-->flotador-->S
área-->flotante-->A
"""
a = float ( input ( "Insertar valor de lado a: " ))
b = float ( input ( "Insertar valor de lado b: " ))
c = float ( input ( "Insertar valor de lado c: " ))
S = (( un + segundo + c ) / 2 )
A = (( S * ( S - a ) * ( S - b ) * ( S - c )) ** 0.5 )
print ( "El area del triangulo es: " + str ( A ))
