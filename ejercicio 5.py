"""
Entradas
Parcial1-->flotante-->P1
Parcial2-->flotante-->P2
Parcial3-->flotante-->P3
examenfinal-->flotante-->Ef
Trabajofinal-->flotante-->Tf
salidas
Promedioparciales-->float-->Promp
Notadefinitiva-->flotante-->Notafinal
"""
P1 = float ( entrada ( "Nota del parcial 1: " ))
P2 = float ( entrada ( "Nota del parcial 2: " ))
P3 = float ( entrada ( "Nota del parcial 3: " ))
Ef = float ( entrada ( "Nota examen final: " ))
Tf = float ( entrada ( "Nota del trabajo final: " ))
Indicador = (( P1 + P2 + P3 ) / 3 )
Notafinal = (( Promp * 0.55 ) + ( Ef * 0.33 ) + ( Tf * 0.15 ))
print ( "Nota definitiva: " + str ( Notafinal ))