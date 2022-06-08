import pandas as pd

# ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'


def listaPeliculas(rutaFileCsv: str) -> str:
    if rutaFileCsv.split('.')[-1] != 'csv':
        try:
            # Leer el archivo csv
            csv = pd.read_csv(rutaFileCsv)
            # print(csv)

            # Se crea un subconjunto con las columnas "Country", "Language" e "Gross Earnings".
            subGrupoPeliculas = csv[['Country', 'Language', 'Gross Earnings']]
            # print(subGrupoPeliculas)

            # Se usa las columnas "Country" y "Language" como índice para la tabla dinámica y "Gross Earnings" como tabla de resumen
            gananciaPaisLenguaje = subGrupoPeliculas.pivot_table(
                index=['Country', 'Language'])
            return gananciaPaisLenguaje.head(10)

            # Se importa la libreria matplotlib.pyplot
            #import matplotlib.pyplot as plt

            # Se muestra la tabla dinámica con un diagrama de barras mostrando solo 50 registros.
            #gananciaPaisLenguaje.head(50).plot(kind='bar', figsize=(20,8))

            # print(gananciaPaisLenguaje) #[100 rows x 1 columns]
            # plt.show()

        except:
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión inválida.')
    return


print(listaPeliculas(rutaFileCsv))
