#Ejercicioquiz2EDM
def modelar_descomposicion(d):
    descomposicion = []
    mensaje = "Proceso inconcluso"
    for i in range(d):
        porcentaje = float(input("Por favor ingrese un porcentaje de descomposicion: "))
        if i > 0:
            while porcentaje < descomposicion[i - 1]:
                porcentaje = float(input("Por favor ingrese un porcentaje de descomposicion: "))
        descomposicion.append(porcentaje)
        if porcentaje >= 100:
            mensaje = "Proceso completado antes de tiempo"
            break
    descomposicion_mayor_cincuenta = 0
    for desc in descomposicion:
        if desc > 50.0:
            descomposicion_mayor_cincuenta += 1
    return descomposicion, descomposicion_mayor_cincuenta, mensaje


def main():
    d = int(input("Por favor ingrese un número: "))
    res = modelar_descomposicion(d)
    for r in res:
        print(r)

main()