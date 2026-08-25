def crear_matriz(codigo,autoparte,marca,modelo,precio,stock,stockMin):
    matriz = []
    for i in range(len(codigo)):
        fila = [codigo[i], autoparte[i], marca[i], modelo[i], precio[i], stock[i], stockMin[i]]
        matriz.append(fila) 
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
            