def validar_stock_minimo(matrices):
    bajo_stock = []
    
    for matriz in matrices:
        for producto in matriz:
            if producto[5] < producto[7]:
                bajo_stock.append(producto)
                
    print("\nLos productos con stock debajo del mínimo son:")
    if bajo_stock:
        for item in bajo_stock:
            print(
                "Categoría:", item[0],
                "| Código:", item[1],
                "| Autoparte:", item[2],
                "| Stock actual:", item[5],
                "| Stock mínimo:", item[7]
            )
    else:
        print("No hay productos por debajo del stock mínimo.")
        
    return bajo_stock