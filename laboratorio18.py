#Crear Variables
s = input("Ingrese una frase: ")
i = int(input("Ingresa un numero entero: "))
f = float(input("Ingresa un numero con decimales: "))
b = bool(input("Ingresa True or False: "))
print("String = ",s)
print("Int =",i)
print("Float =",f)
print("Boolean =",b)
#Operaciones matematicas
x = int(input("Ingresa un numero: "))
y = int(input("Ingresa otro numero: "))
print("Valor de X = ", x)
print("Valor de Y = ", y)
print("Operaciones")
print("Suma = ", x + y)
print("Resta = ", x - y)
print("Multiplicacion = ", x * y)
print("Division = ", x / y)
print("Division Entera = ", x // y)
print("Potencia = ", x ** y)
print("Modulo = ", x % y)
#Frases
frase1 = input("Ingrese la Frase 1: ")
frase2 = input("Ingresa la frase 2: ")
frase = frase1 + " " + frase2
print("La frase completa es: ",frase)
#Listas
numeros = [1, 2, 3, 4, 5]
mixta = [3.14,"Python", True,5,6.3,False,"frase",8,"nueve",True]

print("Lista de numeros =", numeros)
print("Lista Mixta = ",mixta)
print("Segundo elemento de la lista: ", mixta[1])
mixta[2] = "false"
print("Lista actualizada: ",mixta)

#Diccionario
persona = {
    "nombre":"Luisillo",
    "edad":23,
    "ciudad":"Santa Marta",
    "profesion":"estudiante"
}
print("Diccionario actualizado = ", persona)

#Agregar Clave-Valor
persona["hobby"] = "programar"
print("Actualizar clave-valor =",persona)

#Actualizar Clave-Valor
persona["edad"] = 34
print("Diccionario corregido =", persona)
