def convertisseur_binaire() : 
    nombre_entier = int(input("Entrez le nombre à convertir : "))
    binaire = []
    while nombre_entier != 0 :
        binaire.append(nombre_entier % 2)
        nombre_entier = nombre_entier // 2
    binaire.reverse()
print(''.join(str(x) for x in binaire))
