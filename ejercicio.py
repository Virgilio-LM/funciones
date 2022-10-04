import re


def calcularIVA(precio):
    precio = precio*16/100
    return precio

def calculoDesc(precio,descuento):
    total = precio - precio*(descuento/100)
    print("El total a pagar con un descuento del ",descuento,"% es: $",total)
    return total

def calculoIMC(peso,estatura):
    imc =  peso/(estatura**2)

    if imc <= 18.5:
        print("Bajo peso")
    else:
        if imc >= 18.5  and imc <= 24.9:
            print("Peso adecuado")
        else:
            if imc >= 25 and imc <= 29.9:
                print("SobrePeso")
            else:
                if imc >= 30 and imc <=34.9:
                    print("Obesidad grado 1")
                else:
                    if imc >= 35 and imc <=39.9:
                        print("Obesidad grado 2")
                    else:
                        print("Obesidad grado 3")


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
        iva = calcularIVA(precio)
        print("El IVA del precio $",precio,"es $",iva)

    if op == 2:
        precio = int(input("Ingrese el precio del producto: "))
        descuento = int(input("Ingrese el % del descuento (0-100): "))
        calculoDesc(precio,descuento)

    if op == 3:
        peso = float(input("Ingrese el peso: "))
        estatura = float(input("Ingrese el estatura: "))
        calculoIMC(peso,estatura)