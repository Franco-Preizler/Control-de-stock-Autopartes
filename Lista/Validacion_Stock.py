def validarStock(a,b):
    print(a)
    prod=input("Elija un producto para agregar stock")
    while prod not in b:
        print("El producto elegido es incorrecto")
        prod=input("Elija un producto para agregar stock:  ")
    return prod


suspe=["amortiguador","espiral","buje","rotula","bieleta"]
mante=["ruleman","tensor","filtro de combustible","filtro de aire","filtro de aceite"]
mot=["carter","piston","biela","valvula","cigueñal"]
carro=["paragolpe","optica","capot","manija","espejo"]



