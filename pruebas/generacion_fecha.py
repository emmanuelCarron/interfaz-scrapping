def tipo_mes(mes):
    tolower_mes = mes.lower()

    return tolower_mes

def set_dias_mes(meses):
    if meses == "02":
        dias = 28
    elif meses == "04" or mes == "06" or mes == "09" or mes == "11":
        dias = 30
    else:
        dias = 31

    return dias

def fecha_comp(dias_mes, meses, anio):
    for dia in range (1, dias_mes + 1, 1):
        str_dia = str (dia)
        if len (str_dia) == 1:
            str_dia = "0" + str (dia)
            fecha = str_dia + "/" + str(meses) + "/" + str(anio)
            print (fecha)
        else:
            fecha = str_dia + "/" + str(meses) + "/" + str(anio)
            print (fecha)


if __name__ == "__main__":
    anio = input("Año: ")
    mes = input("ingrese mes: ")
    meses = tipo_mes(mes)
    dias_mes = set_dias_mes(meses)
    fecha_completa = fecha_comp(dias_mes, meses, anio)
