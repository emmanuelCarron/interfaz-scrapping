from urllib.request import urlopen

from bs4 import BeautifulSoup
from bs4 import element


def download(some_url):
    some_page = urlopen(some_url)
    return BeautifulSoup(some_page.read(), features="html.parser")

def func(x):
    if str(x).startswith('./quiniela-cordoba-'):
        return True


def seleccion_sorteo():
    fecha = input("Fecha sorteo dd-mm-aaaa: ")  # Ver validacion de fecha - no a futuro
    my_soup = download(f"http://quinielatop.com.ar/resultado-quiniela-{fecha}.html")
    divs = my_soup.find_all('a', {"href": func})
    
    if len(divs) == 0:
        raise ValueError("No se encontró información para la fecha ingresada.")
    
    sorteos_dia = {}
    for i in divs:
        url = i.get("href")
        tipo_sorteo = url.split("-")[2]
        sorteos_dia[tipo_sorteo] = url
    tipo_de_sorteo = {"1": "primera",
                    "2": "matutina",
                    "3": "vespertina",
                    "4": "nocturna"}
    seleccion = input("""Elegir el tipo de sorteo a consultar: 
    1 - Primera
    2 - Matutina
    3 - Vespertina
    4 - Nocturna
    0 - Salir
    
    -> """)
    return sorteos_dia[tipo_de_sorteo[seleccion]]

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


if __name__ == "__main__":

    sorteo_elejido = seleccion_sorteo()
    url_sorteo = construir_url_sorteo(sorteo_elejido)
    sorteo = download(url_sorteo)
    extracto = obterner_extracto(sorteo)
    for i in range(1, 11):
        print(f"Numero en Posicion {i} -- valor: {extracto[str(i)]}")






