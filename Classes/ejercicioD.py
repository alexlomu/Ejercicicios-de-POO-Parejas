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
            

