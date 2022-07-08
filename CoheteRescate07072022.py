def CDT(usuario:str,capital:int,tiempo:int):
    porcentajeGanancia=0.03
    porcentajePerdida=0.02

    if(tiempo>2):
        valorIntereses=(capital*porcentajeGanancia*tiempo)/12
        valorTotal=valorIntereses+capital
    else:
        valorPerdida=capital*porcentajePerdida
        valorTotal=capital-valorPerdida

    return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}"

    