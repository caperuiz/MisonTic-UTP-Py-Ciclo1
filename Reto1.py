#Solución del reto
def CDT(usuario: str, capital: int, tiempo: int):
    Porcentaje_interes = 0.03
    Porcentaje_aperder = 0.02

    #Primero se Comprueba que los meses son mayores a dos
    # Caso de ganacia.
    if(tiempo > 2):
        Valor_inte = (capital*Porcentaje_interes*tiempo)/12
        Valor_total=capital+Valor_inte
             
     #Caso contrario no existe ganacia    
    else :
        Valor_aperder = capital*Porcentaje_aperder
        Valor_total=capital-Valor_aperder
    return 'Para el usuario '+str(usuario)+' La cantidad de dinero a recibir, según el monto inicial '+str(capital)+' para un tiempo de '+str(tiempo)+ ' meses es: '+str(Valor_total)