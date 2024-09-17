# Programacion
# Escriba una funcion/metodo que determine la cantidad de 0s a la derecha de n! (factorial)

# funcion para ingresar un numero
def ingresar():
    while True: 
        number =  input("Ingrese un numero: ")
        if(number.isdigit() or (number[0] == '-' and number[1:].isdigit())):
            number_int = int(number)
            break
        else: 
            print("Haz ingresado algo distinto a un Numero!")
    #print(number_int)
    return number_int  

# funcion calcular factorial
def factorial(number_int):
    if number_int == 0:
        return 1
    result = number_int * factorial(number_int-1)
    return result


# funcion para contar los ceros del numero
def contar_ceros(result):
    num_arr = []
    cantidad_ceros = 0
    print("Resultado de la factorial es: ", result)
    num_arr = str(result)[::-1]
    # print(num_arr)
    for i in range(len(num_arr)):
        if num_arr[i] == "0":
            cantidad_ceros += 1
        else:
            break     
    return print(cantidad_ceros, "Ceros a la derecha del numero")     
   
# llamado a las funciones
contar_ceros(factorial(ingresar()))
