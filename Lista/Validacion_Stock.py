def validarStock(a):
    print(a)
    prod=input("Elija un producto para agregar stock")
    while prod not in a:
        print("El producto elegido es incorrecto")
        prod=input("Elija un producto para agregar stock:  ")
    return prod


suspe=["amortiguador","espiral","buje","rotula","bieleta"]
mante=["ruleman","tensor","filtro de combustible","filtro de aire","filtro de aceite"]
mot=["carter","piston","biela","valvula","cigueñal"]
carro=["paragolpe","optica","capot","manija","espejo"]

if opcion ==1:
    producto=validarStock(suspe)
elif opcion == 2:
    producto=validarStock(mante)
elif opcion == 3:
    producto=validarStock(mot)
elif opcion == 4: 
    producto=validarStock(carro)






