nom_produit = "Ordinateur portable"
prix_unitaire = 500
quantite_en_stock = 50

print("Informations du produit :")
print("Nom Du Produit:", nom_produit)
print("Prix unitaire :", prix_unitaire)
print("Quantité en stock :", quantite_en_stock)

quantite_achetee = int(input("Combien d'Ordinateur Portable voulez-vous ? :"))

quantite_en_stock -= quantite_achetee
prix_unitaire *= 1.10

print("\nAprès l'achat et l'inflation de 10% :")
print("Nom :", nom_produit)
print("Nouveau prix unitaire :", prix_unitaire)
print("Nouvelle quantité en stock :", quantite_en_stock)