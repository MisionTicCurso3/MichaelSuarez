print ( "Digíta tu peso" )
Peso = input ()
print ( "Listo tu peso es" , Peso , "Ahora digíta tu altura" )
Altura = input ()

kg = Peso
m = Altura

Resultado == kg % m
print ( "Tu IMC es de", Resultado )

if ( Resultado <18.5 ):
    print ( "Insuficiencia Ponderal" )
else:
    print ( "Todo bien" )
