## Calculadora de interés compuesto

def calc_comp_index(capital_inicial, mensualidad, rentabilidad_esperada, años):
    meses = 12
    retorno_total = capital_inicial
    i = 0
    z = 0

    # Año 1
    while i < años:
        while z < meses:
            retorno_total += mensualidad
            retorno_total += retorno_total * (rentabilidad_esperada / meses)
            z += 1
        i += 1
        z = 0
    return retorno_total

# Example of use
capital_inicial = 5000
aport_mensual = 100
rentabilidad = 0.06
años = 10

retorno_total1 = calc_comp_index(capital_inicial, aport_mensual, rentabilidad, años)
print(f"Con capital inicial de {capital_inicial}€ y aportando {aport_mensual}€ al mes durante {años} año/s obtienes {retorno_total1:.2f}€")
