# Ejercicicios-de-POO-Parejas
Mi dirección de GitHub para este repositorio es: [GitHub](https://github.com/alexlomu/Ejercicicios-de-POO-Parejas)
https://github.com/alexlomu/Ejercicicios-de-POO-Parejas
Para esta entrega hemos tenido que realizar diversos ejercicios que vienen resueltos a continuación.

# Ejercicio a) Palíndromo - método de clase
Para este ejercicio primero hemos tenido que crear una clase llamada Palindromo en la que definiriamos una función que al introducirla con un texto nos devolvería un boleano o otro dependiendo si el texto es o no un palíndromo.
El UML desarrollado para el ejercicio es:
![uml a](https://user-images.githubusercontent.com/91721507/159481810-55e9d7c3-286d-4d30-8920-9a1ed34d6197.PNG)


El código corresponiente es el siguiente:
```
class Palindromo:
  def esPalindromo(entrada):
        if entrada == entrada[::-1]:
            return True
        else:
            return False
```

# Ejercicio b) Palíndromo - método de instancia
Ahora, partiendo de el código que tenemos del apartado a hemos de añadir un atributo que se inicializará en el constructor, además crearemos una nueva función que pruebe si el atributo de la instancia es un palíndromo. 
El UML desarrollado para el ejercicio es:
![uml b](https://user-images.githubusercontent.com/91721507/159481864-41c4b417-41c6-445e-b746-268d48b2a0dd.PNG)


El código propuesto es el siguiente:
```
class Palindromo:
    global entrada
    entrada = input("Qué atributo quieres añadir? ")
    global lista
    lista = []
    def esPalindromo(entrada):
        if entrada == entrada[::-1]:
            return True
        else:
            return False
    
    
    def test(entrada):
        lista.append(entrada)
        if entrada == entrada[::-1]:
            print(True)
            
        else:
            print(False) 
        if len(lista) > 1:
            eliminar = lista.pop()
            eliminar = eliminar.upper()
            print(eliminar)
```

# Ejercicio c) Puzzle
En este ejercicio nos piden únicamente qué mensajes muestran el código que nos dan, los cuáles son los siguiente:
```
<class '__main__.A'>
False
0
1
2
3
```
# Ejercicio d) Logger
Para el último ejercicio nos piden que creemos una función a la que tras introducir un texto y un número (x) para que cree un archivo de texto en el que escribirá el texto x veces entre otras cosas. 
El UML desarrollado para el ejercicio es:
![uml d](https://user-images.githubusercontent.com/91721507/159482606-8b48a7dc-e2d7-44e2-9c54-34060e226a10.PNG)


El código propuesto es el siguiente:
```
class Logger:
    class Test:
        def llamada():
            texto = input("Introduce el texto que quieres escribir en el archivo: ")
            num = int(input("Introduce el numero de veces que quieres que se escriba el texto en el archivo: "))
            file = open("log.txt", "w")
            file.write("--Start log--")
            for i in range(1, num + 1):
                file.write(f" \n {str(i)} {texto}")
            file.write(f"  \n --End log: {str(num)} log(s)")
            file.close()
```
