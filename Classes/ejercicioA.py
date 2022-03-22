class Palindromo:
    def esPalindromo(entrada):
        if entrada == entrada[::-1]:
            return True
        else:
            return False