from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import element
import generacion_fecha


def download(some_url):
    some_page = urlopen(some_url)
    return BeautifulSoup(some_page.read(), features="html.parser")

def func(x):
    if str(x).startswith('./quiniela-cordoba-'):
        return True

def obtencion_extracto_mensual (fechas, tipo):
    extractos_del_mes = {}
    for fecha in fechas:
        my_soup = download(f"http://quinielatop.com.ar/resultado-quiniela-{fecha}.html")
        divs = my_soup.find_all('a', {"href": func})
    
        print("Descargando.... ")
        if len(divs) == 0:
            print (f"No se encontró información para la fecha {fecha}.")
            continue

        sorteos_dia = {}
        for i in divs:
            url = i.get("href")
            tipo_sorteo = url.split("-")[2]
            sorteos_dia[tipo_sorteo] = url

        if fecha in sorteos_dia[tipo]:
            extractos_del_mes[fecha] = sorteos_dia[tipo]

    return extractos_del_mes


def construir_url_sorteo(url_sorteo):
    return "http://quinielatop.com.ar" + url_sorteo[1:]

def obterner_extracto(sorteo):
    tablas = sorteo.find("table", {"class":"resultados"})
    filas = [tr for tr in tablas.children if isinstance(tr, element.Tag)]
    filas = filas[2:-1]
    del filas[5]
    results = []
    for tr in filas:
        for td in tr.children:
            results.append(td)

    extracto = {}
    for i in range(0,len(results),2):
        extracto[results[i].string] = results[i+1].string
    return extracto


def presentar_extracto(extracto):
    for i in range(1, 11):
        print(f"Numero en Posicion {i} -- valor: {extracto[str(i)]}")


def seleccion_tipo_sorteo():
    tipo_de_sorteo = {"1": "primera",
                      "2": "matutina",
                      "3": "vespertina",
                      "4": "nocturna"}
    seleccion = input ("""Elegir el tipo de sorteo a consultar: 
           1 - Primera
           2 - Matutina
           3 - Vespertina
           4 - Nocturna
           0 - Salir

           -> """)

    return tipo_de_sorteo[seleccion]


if __name__ == "__main__":

    fechas_generadas = generacion_fecha.fechas()
    tipo_sorteo = seleccion_tipo_sorteo()
    sorteo_elejido = obtencion_extracto_mensual(fechas_generadas, tipo_sorteo)
    extracto_del_mes = {}
    for key in sorteo_elejido:
        url = construir_url_sorteo(sorteo_elejido[key])
        sorteo = download(url)
        extracto_del_mes[key] = obterner_extracto(sorteo)
        print("\n ----------------")
        print(key)
        presentar_extracto(extracto_del_mes[key])