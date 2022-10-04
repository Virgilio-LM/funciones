import re
import funciones as fcns


op=3

while op!=4:
    print("  MENU  ")
    print("*"*10)
    print("1. Calcular IVA")
    print("2. Descuento")
    print("3. Calcular IMC")
    print("4. Salir")
    op = int(input("Ingresar opción: (1-4) "))

    if op == 1:
        precio = int(input("Ingrese el precio del producto: "))
        iva = fcns.calcularIVA(precio)
        print("El IVA del precio $",precio,"es $",iva)

    if op == 2:
        precio = int(input("Ingrese el precio del producto: "))
        descuento = int(input("Ingrese el % del descuento (0-100): "))
        fcns.calculoDesc(precio,descuento)

    if op == 3:
        peso = float(input("Ingrese el peso: "))
        estatura = float(input("Ingrese el estatura: "))
        fcns.calculoIMC(peso,estatura)