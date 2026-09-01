def validar_stock_minimo(lista):
    bajo_stock=[]
    for i in range(len(lista)):
        if lista[i][5]<lista[i][7]:
            bajo_stock.append(lista[i][1])
    print('los productos con stock debajo del minimo son:')
    print(bajo_stock)
    return bajo_stock



