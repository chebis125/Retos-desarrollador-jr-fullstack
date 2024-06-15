def eliminar_invertir(lista, S):
    lista_modificada = []
    for num in lista:
        # Filtrar dígitos menores que S
        digitos_filtrados = [d for d in str(num) if int(d) < S]
        if digitos_filtrados:
            num_modificado = int(''.join(digitos_filtrados))
            lista_modificada.append(num_modificado)
    # Invertir la lista
    return lista_modificada[::-1]

def imprimir(lista, S):
    lista_final = eliminar_invertir(lista, S)
    print(f"{lista} -> {lista_final}")

# Limitar a 100 números
S = 7
numeros = input("Ingrese números separados por espacio: ").split()[:100]
lista = list(map(int, numeros))
imprimir(lista, S)
