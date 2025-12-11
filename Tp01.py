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
print ("\n# 3) Filtrage : Séquences de longueur>10")
filtered_df_long = df[df["longueur"]>10]
print(filtered_df_long)






