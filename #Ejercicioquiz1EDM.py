#Ejercicio 1    
def cal_lotes(n):
    lotes = []
    for i in range(n):
        temperatura = float(input("Por favor ingrese una temperatura: "))
        concentracion = float(input("Por favor ingrese una concentración: "))
        lotes.append((temperatura, concentracion))
    temperatura_mayor_cien = 0
    temperatura_promedio = 0
    concentracion_promedio = 0
    for lote in lotes:
        if lote[0] > 100:
            temperatura_mayor_cien += 1
        temperatura_promedio += lote[0]
        concentracion_promedio += lote[1]
    temperatura_promedio /= n
    concentracion_promedio /= n
    if temperatura_promedio > concentracion_promedio:
        proceso = "inestable"
    else:
        proceso = "estable"
    return lotes, temperatura_mayor_cien, concentracion_promedio, proceso


def main():
    n = int(input("Por favor ingrese un número: "))
    res = cal_lotes(n)
    for r in res:
        print(r)

main()     
        