from urllib.request import urlopen

from bs4 import BeautifulSoup
from bs4 import element


def download(some_url):
    some_page = urlopen(some_url)
    return BeautifulSoup(some_page.read(), features="html.parser")


"""
pueden testearla escribiendo:
sopa = bajar("http://www.pirulo.com")
(Cambien por una dirección que exista y de una página liviana, va a demorar algunos segundos)
print(sopa.gettext())
print(sopa.prettify())
"""


def get_table():
    my_soup = download("https://es.wikipedia.org/wiki/C%C3%B3rdoba_(Argentina)")
    return my_soup.find_all('table')[6]


def read_table(table):
    rows = []
    for row in table.find_all('tr'):
        rows.append(read_line(row))
    return rows


def read_line(line):
    all_data = []
    for data in line.find_all('td'):
        all_data.append(data.get_text())
    return all_data

def func(x):
    if str(x).startswith('./quiniela-cordoba-'):
        return True


def seleccion_sorteo():
    global sorteos_dia
    fecha = input("Fecha sorteo dd-mm-aaaa: ")  # Ver validacion de fecha - no a futuro
    my_soup = download(f"http://quinielatop.com.ar/resultado-quiniela-{fecha}.html")
    divs = my_soup.find_all('a', {"href": func})
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


if __name__ == "__main__":

    sorteo_elejido = seleccion_sorteo()
    nueva_url = "http://quinielatop.com.ar" + sorteo_elejido[1:]
    sorteo = download(nueva_url)
    tablas = sorteo.find("table", {"class":"resultados"})
    filas = [tr for tr in tablas.children if isinstance(tr, element.Tag)]
    filas = filas[2:-1]
    del filas[5]
    results = []
    for tr in filas:
        for td in tr.children:
            results.append(td)

    for i in results:
        print(i.string)





