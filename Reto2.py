def cuadrados_ordenados(matriz, S):
    SS = S*11
    # Ordenar la matriz de entrada usando ordenación por inserción
    for i in range(1, len(matriz)):
        clave = matriz[i]
        j = i-1
        while j >=0 and clave < matriz[j]:
            matriz[j+1] = matriz[j]
            j -= 1
        matriz[j+1] = clave
    # Calcular el cuadrado y filtrar
    cuadrados_filtrados = [x**2 for x in matriz if 0 <= x**2 <= SS]
    for i in range(1, len(cuadrados_filtrados)):
        clave = cuadrados_filtrados[i]
        j = i-1
        while j >=0 and clave < cuadrados_filtrados[j]:
            cuadrados_filtrados[j+1] = cuadrados_filtrados[j]
            j -= 1
        cuadrados_filtrados[j+1] = clave
    return cuadrados_filtrados

def imprimir(lista, S):
    lista_final = cuadrados_ordenados(lista, S)
    print(f"matriz : {lista} -> {lista_final}")
S = 7
numeros = input("Ingrese números separados por espacio: ").split()[:100]
lista = list(map(int, numeros))
imprimir(lista, S)