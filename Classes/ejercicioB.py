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
    

        

