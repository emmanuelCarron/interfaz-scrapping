from urllib.request import urlopen

from bs4 import BeautifulSoup


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


if __name__ == "__main__":

    my_soup = download("http://quinielatop.com.ar/resultado-quiniela-22-11-2021.html")
    divs = my_soup.find_all('a', {"href": func})
    print(divs)
    
    #print(divs)
    # sopa = bajar("https://www.google.com.ar/")
    # # print(sopa.get_text())
    # # print(sopa.prettify())
    # # print(sopa.find_all('a')) #lista de todos los <a>
    # enlaces = sopa.find_all('a')
    # #for enlace in enlaces:
    # #   print(enlace.get_text())

    # for enlace in enlaces:
    #     print(enlace.attrs["href"])



    # soup = download("https://es.wikipedia.org/wiki/C%C3%B3rdoba_(Argentina)")
    # tablaClima = soup.find_all('table')[6]
    #
    # tablaPyClima = read_table(tablaClima)
    # for i in tablaPyClima[3]:
    #     print(i[:4])
