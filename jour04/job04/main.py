def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    
    if len(fruits) > 2:
        fruits.insert(2, "Mangue")
    else:
        print("L'index 2 n'existe pas dans la liste.")

    return fruits

resultat = ajouter_mangue()
print(resultat)