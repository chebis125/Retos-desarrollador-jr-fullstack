def cantidad_cambio(moneda):
    moneda.sort()
    contador = 1
    for valor in moneda:
        if valor > contador:
            return contador
        contador += valor
    return contador

def imprimir(moneda):
    cambio_final = cantidad_cambio(moneda)
    print(f"monedas : {moneda} -> {cambio_final}")

numeros = input("Ingrese números separados por espacio: ").split()[:100]
moneda = list(map(int, numeros))

imprimir(moneda)