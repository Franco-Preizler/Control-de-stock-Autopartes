def Agregar_Stock():
    codigo=[]
    autoparte=[]
    marca=[]
    modelo=[]
    stock=[]

    print('''¿Que categoria de autoparte desea ingresar? 
        (1.Suspension
        2.Filtros/mantenimiento
        3.Motor
        4.Carroceria)''')
    
    opcion=int(input('Ingrese la categoria a ingresar: '))
    validarNum(opcion)
    if opcion==1:
        stockSuspe()
        producto = stockSuspe()
    elif opcion==2:
        stockMantenimiento()
        producto = stockMantenimiento()
    elif opcion==3:
        stockMotor()
        producto = stockMotor()
    else:
        stockCarroceria()
        producto=stockCarroceria()
