#Convertisseur Binaire vers Décimal
def convertisseur_2to10() :
    entree = input("entrez le nombre binaire à convertir : ")
    nb_binaire = [int(bit) for bit in entree][::-1] 
    indice = [i for i, bit in enumerate(nb_binaire) if bit == 1]
    nb_decimal = sum(2**i for i in indice)
    print("Nombre décimal :", nb_decimal)

#Convertisseur Décimal vers Binaire
def convertisseur_10to2() : 
    nb_decimal = int(input("entrez le nombre decimal à convertir : "))
    nb_binaire = []
    while nb_decimal != 0 :
        nb_binaire.append(nb_decimal % 2)
        nb_decimal = nb_decimal // 2
    nb_binaire.reverse()
    print("Nombre binaire :", ''.join(str(n) for n in nb_binaire))

#Convertisseur Décimal vers Héxadécimal
def convertisseur_10to16() :
    nb_decimal = int(input("entrez le nombre decimal à convertir : "))
    symbole_hex = "0123456789ABCDEF"
    nb_hexadecimal = []
    while nb_decimal != 0 : 
        reste = nb_decimal % 16
        symbole = symbole_hex[reste]  
        nb_hexadecimal.append(symbole)  
        nb_decimal = nb_decimal // 16   
    nb_hexadecimal.reverse()
    print("Nombre hexadécimal :", ''.join(nb_hexadecimal))


#Convertisseur Héxadéciaml vers Décimal
def convertisseur_16to10():
    entree = input("Entrez le nombre hexadécimal à convertir : ")
    entree = entree.upper()
    symbole_hex = "0123456789ABCDEF"
    entree_inversee = entree[::-1]
    nb_decimal = sum(symbole_hex.index(lettre) * (16**i) for i, lettre in enumerate(entree_inversee))
    print("Nombre décimal :", nb_decimal)

choix = input("1 : 2-->10 ; 2 : 10-->2 ; 3 : 10-->16 ; 4 : 16--10")
if choix == "1" : 
    convertisseur_2to10()
elif choix == "2" : 
    convertisseur_10to2()
elif choix == "3" :
    convertisseur_10to16()
elif choix == "4" :
    convertisseur_16to10()
else : 
    print("Erreur, relancer le programme et sélectionner 1, 2, 3 ou 4. ")
