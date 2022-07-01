def CDT(usuario:str, capital:int, tiempo:int):
    return f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {(((capital*0.03*tiempo)/12)+capital) if (tiempo>2) else capital-(capital*0.02) }'


true_val if condition else false_val

print(CDT('AB1012', 1000000, 3))
print(CDT('ER3366', 650000, 2))
