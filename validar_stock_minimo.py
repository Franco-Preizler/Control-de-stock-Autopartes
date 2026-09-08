def validar_stock_minimo(matrices):
    bajo_stock = []
    
    for matriz in matrices:
        bajo_stock.extend(filter(lambda producto: producto[5] < producto[7], matriz))
                
    print("\nLos productos con stock debajo del minimo son:")
    if bajo_stock:
        for item in bajo_stock:
            print(
                "Categoria:", item[0],
                "| Codigo:", item[1],
                "| Autoparte:", item[2],
                "| Stock actual:", item[5],
                "| Stock minimo:", item[7]
            )
    else:
        print("No hay productos por debajo del stock minimo.")
        
    return bajo_stock