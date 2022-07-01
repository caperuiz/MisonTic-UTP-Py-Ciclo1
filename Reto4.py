def ordenes(rutinaContable):
    #Importar la funcion "reduce" desde la libreria "functools"
    from functools import reduce

    #Declarar constante "ordenMinima"
    ordenMinima = 600000
    #Primer lambda que suma el total de cada tupla de cada lista
    ordenTotal = list(
        map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), rutinaContable))
    print(ordenTotal)
    #Segundo lambda suma los totales de todas las tuplas de toda la lista
    ordenTotal = list(
        map(lambda x: [x[0]] + [reduce(lambda a, b: round(a + b, 2), x[1:])], ordenTotal))
    #Tercer lambda que suma el incremento si la compra no llega al minimo
    ordenTotal = list(
        map(lambda x: x if x[1] >= ordenMinima else (x[0], x[1] + 25000), ordenTotal))

    print('------------------------ Inicio Registro diario ---------------------------------')
    #Ciclo para imprimir el total de cada compra
    for x in range(len(ordenTotal)):
        print(
            f'La factura {ordenTotal[x][0]} tiene un total en pesos de {ordenTotal[x][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')


#Registro diario
rutinaContable = [[1201, ("5464", 4, 25842.99), ("7854", 18, 23254.99), ("8521", 9, 48951.95)],
                  [1202, ("8756", 3, 115362.58), ("1112", 18, 2354.99)],
                  [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20),
                   ("1254", 1, 13645.20), ("9965", 5, 1645.20)],
                  [1204, ("9635", 7, 11.99), ("7733", 11, 18.99),
                   ("88112", 5, 390.95)]
                  ]
ordenes(rutinaContable)
