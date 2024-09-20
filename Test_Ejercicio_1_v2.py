def contar_ceros(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    print("La cantidad de 0 a la derecha de n! es => ", count)

def ingresar():
    while True: 
        number =  input("Ingrese un numero para calcular la Factorial: ")
        if(number.isdigit() or (number[0] == '-' and number[1:].isdigit())):
            number_int = int(number)
            break
        else: 
            print("Haz ingresado algo distinto a un Numero!")
    #print(number_int)
    return number_int  

contar_ceros(ingresar())