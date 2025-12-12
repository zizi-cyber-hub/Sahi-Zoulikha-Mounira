# NomDuChefDeProjet, Sahi Zoulikha Mounira, Master 1 Microbiologie Fondamentale , 10/12/2025)
# Nom du Membre 1 : Nedjar Douaa
# Nom du Membre 2 : Zeggai Meriem
# Nom du Membre 3 : Hachim El Chaima
# Nom du Membre 4 : Benabdallah soumia

import pandas as pd

# Données : Séquence ADN, Longueur, Pourcentage de CG
# J'ajoute les nouvelles séquence de l'image (ATGAAGGCTT et TTAACCGGAT)
data = { 
        "Séquence": ['ATGCGTACGTA', 'GCTAGCTAGGC', 'ATGCGCGTAAGT', 'TACGATCGTA', 'ATGAAAGGCTT', 'CGTACGTAC', 'TTAACCGGAT'], 
        "Longueur": [12, 12, 12, 10, 11, 10, 10],
        "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

# 1) Créer et afficher le tableau ci-dessous en utilisant la bibliothèque pandas.
df = pd.DataFrame(data)
print("**************** Création et affichage du DataFrame ****************"),"\n""\n")

# Affichage du tableau initial"
print("Tableau des séquences ADN :", "\n")
print(df,"\n""\n" )

# Opération sur le tableaux:
print("**************** Opération demandées ****************")

# 2) Sélectionner et afficher uniquement la colonne "Longueur ".
print("\n# 2) colonne 'Longueur' :")
longueurs= df["Longueur "]
print(longueurs,"\n")

# 3) Filtrer les séquences dont la longueur est supérieure à 10
print("\n# 3) Filtrage : Séquences de Longueur > 10")
filtered_df_long = df[df["Longueur"] > 10]
print(filtered_df_long)

# 4) Calculer le pourcentage moyen de GC avec 3 chiffres après la virgule.
print("\n# 4) Calcul de la moyenne de GC")
# Calculer la moyenne du pourcentage  de GC
average_gc = df["Pourcentage GC"].mean()
# Afficher avec le formatage à 3 décimales
print(f"Pourcentage moyen de GC : {averge_gc:.3}%")

# 5) Ajouter une colonne "catégorie GC"
print("\n# 5) Ajout de la colonne 'catégorie GC'")
# Fonction lambda pour catégoriser le pourcentage de GC
df["Catégorie GC"] = df["Pourcentage GC"].apply(
    lambda x: "Riche" if x > 55
    else ("Moyen" if 45 <= x <= 55
    else "Faible")
)
print(df)

# 6) Ajouter une colonne donnant le nombre de 'G' dans chaque séquence.
print ("\n# 6 ) Ajout de la colonne ' Nombre de G' ") 
# utiliser la méthode .str.count() sur la colonne "séquence"
df["Nombre de G" ]=df["séquence"].str.count ("G")
print(df)

# 7) Calculer  l’écart-type du %GC et de la longueur des séquences.
print("\n# 7) Calcul de l'Écart-type (Standard Deviation-std)")
std_gc = df["pourcentage GC"].std()
std_Longueur = df["longueur"].std()
print(f"Écart-type du Pourcentage GC : {std_gc:.2f}")
print(f"Écart-type de la longueur : {std_longueur:.2f}")

# 8) Sauvegarder le tableau final dans un fichier CSV.
print("\n# 8) Sauvegarde du DataFrame dans un fichier CSV")
# Sauvegarder le Dataframe dans un fichier CSV (sans l’index)
file_name = "analyse_séquences_adn_final.csv"
df.to_csv(file_name, index=False)
print("Le tableau final a ètè Sauvegardè dans '{file_name}' avec succès.")








