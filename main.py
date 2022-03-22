from Classes.ejercicioA import *
from Classes.ejercicioB import *
from Classes.ejercicioD import *

if __name__ == "__main__":
    ejercicio = input("Introduce a que ejercicio quieres acceder(a, b o d)")
    ejercicio = ejercicio.lower()
    if ejercicio == "a":
        entrada = input("Introduce que texto queres comprobar si es un palindromo: ")
        Palindromo.esPalindromo(entrada)
    if ejercicio == "b":
        Palindromo.test(entrada)
    if ejercicio == "d":
        Logger.Test.llamada()
