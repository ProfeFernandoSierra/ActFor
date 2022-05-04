

""" x = range(1, 11, 1)    
for n in x :
    print(n) """


""" x = range(1, 10, 2)
for a in x :
    print(a) """
    
""" frase = "hola mundo"
for caracter in frase:
    print(caracter) """
    
""" num_mayor = 0
num_menor = 0
num_cero = 0    
num = int(input("ingrese la cantidad de numeros que desea investigar"))    
for n in range(num) :
    num = int(input("ingrese un numero\n"))
    if num > 0:
        print(f"el numero {num} es mayor a 0")
        num_mayor = num_mayor + 1
    elif num < 0:
        print(f"el numero {num} es menor a 0")
        num_menor = num_menor + 1
    else:
        print(f"el numero {num} es igual a 0")
        num_cero = num_cero + 1
print(f"la cantidad de numeros mayores a 0 es: {num_mayor}")  
print(f"la cantidad de numeros menores a 0 es: {num_menor}") 
print(f"la cantidad de numeros iguales a 0 es: {num_cero}") """

""" cont_vocal = 0
cont_cons = 0
letra1 = int(input("ingrese la cantidad de letras que desea investigar\n"))    
for caracter in range(letra1) :
    letra = input("ingrese una letra\n")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print(f"la letra {letra} es una vocal")
        cont_vocal = cont_vocal + 1
    else:
        print(f"la letra {letra} es una consonante")
        cont_cons = cont_cons + 1
print("la cantidad de vocales que has ingresado es ", cont_vocal)
print(f"la cantidad de consonantes que has ingresado es {cont_cons}") """

#formula para sacar numeros primos
num = int(input("ingresar un numero"))
if num %num == 0 and num/num == 1:
    print("numero primo")
else:
    print("numero no es primo")