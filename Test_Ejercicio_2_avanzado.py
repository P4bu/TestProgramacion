# Se debe importar la libreria numlet (https://pypi.org/project/numlet/)
# copiar en consola pycharm -> pip install git+https://github.com/roylanmartinez/Numlet.git 

from nlt import numlet as nl

def ingresar():
    while True:
        number =  input("Ingrese un numero: ")
        if number.isdigit() or (number[0] == '-' and number[1:].isdigit()):
            number_int = int(number)
            break
        else:
            print("Haz ingresado algo distinto a un Numero!")
    #print(number_int)
    return number_int

def traducir(number_int):
    resultado = nl.Numero(number_int).a_letras
    print(number_int," : ", " => ",resultado)

traducir(ingresar())