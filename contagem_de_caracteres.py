contador = 0
string = input("Digita uma palavra: ")

for letra in string:
    if letra == "e":
        contador += 1
    
print(f"O total de letras é: {contador}")


    