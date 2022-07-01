def cliente(informacion:dict)->dict:
    id=informacion['id_cliente']
    nombre=informacion['nombre']
    edad=informacion['edad']
    primerImgreso = informacion['primer_ingreso']

    if edad>18:
        atraccion='X-Treme'
        apto=True
        if primerImgreso ==True:
            totalBoleta=20000-(20000*0.05)
        else:
            totalBoleta=20000
    
    elif edad>=15 and edad <=18:
        atraccion='Carros chocones'
        apto=True
        if primerImgreso == True:
            totalBoleta=5000-(5000*0.07)
        else:
            totalBoleta = 5000

    elif edad>=7 and edad <15:
        atraccion='Sillas voladoras'
        apto=True
        if primerImgreso == True:
            totalBoleta=10000-(10000*0.05)
        else:
            totalBoleta = 10000
    
    else:
        atraccion='N/A'
        apto=False
        totalBoleta='N/A'
    
    respuesta = {'nombre': nombre, 'edad':edad, 'atraccion':atraccion, 'apto': apto, 'primer_ingreso': primerImgreso, 'total_boleta': totalBoleta}
    
    return respuesta
