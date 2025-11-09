

def busca_sequencial(lista, valor):
    comparacoes = 0
    for i, v in enumerate(lista):
        comparacoes += 1
        if v == valor:
            return i, comparacoes
    return -1, comparacoes

def busca_binaria(lista, valor):
    comparacoes = 0
    low, high = 0, len(lista) - 1
    while low <= high:
        comparacoes += 1
        mid = (low + high) // 2
        if lista[mid] == valor:
            return mid, comparacoes
        elif lista[mid] < valor:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparacoes