def remplacer_element_par_somme(L):
    if len(L) >= 5:
        deuxieme_valeur = L[1]
        print("Deuxième valeur de la liste :", deuxieme_valeur)

        L[3] = L[2] + L[4]

        print("Liste après la modification :", L)

        derniere_valeur = L[-1]
        print("Dernière valeur de la liste :", derniere_valeur)
    else:
        print("La liste ne contient pas au moins 5 entiers.")

liste_entiers = [1, 2, 3, 4, 5]

remplacer_element_par_somme(liste_entiers)