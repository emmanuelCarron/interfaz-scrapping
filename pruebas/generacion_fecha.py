def set_dias_mes(meses, anio):
    if meses == 2:
        dias = 28
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            dias = 29

    elif meses in [4, 6, 9, 11]:
        dias = 30
    else:
        dias = 31

    return dias

def fecha_comp(dias_mes, meses, anio):
    fechas = []
    str_meses = str(meses)

    if len(str_meses) == 1:
        str_meses = "0" + str_meses

    for dia in range (1, dias_mes + 1, 1):
        str_dia = str (dia)
        if len (str_dia) == 1:
            str_dia = "0" + str (dia)
            fecha = str_dia + "-" + str_meses + "-" + str(anio)
            fechas.append(fecha)
        else:
            fecha = str_dia + "-" + str_meses + "-" + str(anio)
            fechas.append(fecha)

    return fechas


def entrada_valida(anio, mes):
    return mes in range (1,13)

def fechas():
    bandera = True
    mes = 0
    while mes > 0 and mes < 13 or bandera:
        anio = int (input ("Año: "))
        mes = int (input ("ingrese mes: "))
        if entrada_valida (anio, mes):
            bandera = False
        else:
            print ("Debera ingresar valores del mes correcto (del 1 al 12)")
            continue
        dias_mes = set_dias_mes (mes, anio)
        fecha_completa = fecha_comp (dias_mes, mes, anio)
        return fecha_completa