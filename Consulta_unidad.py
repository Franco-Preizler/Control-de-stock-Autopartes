def mostrar_info(cod, mat):
    for fila in mat:
        if fila[1] == cod:
            return True, fila
    return False, []
