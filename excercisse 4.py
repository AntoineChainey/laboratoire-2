nombre1 = input("entrer un nombre: ") # demande a l'utilisateur d'entrer un nombre et définie la var 1
nombre2 = input("entrer le deuxième nombre: ") # refais l'étape 1
opération = input("entré l'opération désirer a=+ s=-: ") # l'utilisateur entrer une opération et définis la var 3
nombre1 = float(nombre1) # convertir nombre en float
nombre2 = float(nombre2)
if(opération == ("+")) : # vérifie si l,opération est addition ou soustraction
    résultat = nombre1 + nombre2
    
elif(opération == ("-")) : 
    résultat = nombre1 - nombre2
    
print(résultat)# momntre le résultat