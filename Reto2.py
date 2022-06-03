def cliente(informacion: dict) -> dict:

    # Uso Variables
    cli_id = informacion['id_cliente']  # id_cliente
    cli_nom = informacion['nombre']  # nombre del cliente
    cli_edad = informacion['edad']  # edad del cliente
    cli_primer_ingreso = informacion['primer_ingreso']  # peso del cliente

    if cli_edad > 18:
        atraccion = 'X-Treme'
        apto = True
        if cli_primer_ingreso == True:
            total_boleta = 20000-(20000*0.05)
        else:
            total_boleta = 20000

    elif cli_edad >= 15 and cli_edad <= 18:
        atraccion = 'Carros chocones'
        apto = True
        if cli_primer_ingreso == True:
            total_boleta = 5000-(5000*0.07)
        else:
            total_boleta = 5000

    elif cli_edad >= 7 and cli_edad < 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if cli_primer_ingreso == True:
            total_boleta = 10000-(10000*0.05)
        else:
            total_boleta = 10000

    else:

        atraccion = 'N/A'
        apto = False
        total_boleta = 'N/A'

    diccionario_respuesta = {
        'nombre': cli_nom,
        'edad': cli_edad,
        'atraccion': atraccion,
        'apto': apto,
        'primer_ingreso': cli_primer_ingreso,
        'total_boleta': total_boleta

    }

    return diccionario_respuesta
