chaine = "abcdefghijklmnopqrstuvwxyz" * 10
longueur_chaine = len(chaine)

for i in range(1, longueur_chaine + 1):
    portion = chaine[:i].center(longueur_chaine, ' ')
    print(portion)