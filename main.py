import pandas as pd
import matplotlib.pyplot as plt
import csv

# 1. Génération du fichier ventes.csv
with open("ventes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Transaction ID", "Date", "Customer ID", "Gender",
        "Product Category", "Quantity", "Price per Unit", "Remise (%)"
    ])
    writer.writerow([1, "2023-01-01", "CUST1", "Male", "Clothing", 2, 50, 10])
    writer.writerow([2, "2023-01-02", "CUST2", "Female", "Beauty", 1, 30, 5])
    writer.writerow([3, "2023-01-03", "CUST3", "Male", "Electronics", 3, 100, 15])
    writer.writerow([4, "2023-01-04", "CUST4", "Female", "Clothing", 4, 25, 0])
    writer.writerow([5, "2023-01-05", "CUST5", "Male", "Beauty", 2, 40, 20])
    writer.writerow([6, "2023-01-06", "CUST6", "Female", "Electronics", 1, 200, 10])
    writer.writerow([7, "2023-01-07", "CUST7", "Male", "Clothing", 3, 60, 5])
    writer.writerow([8, "2023-01-08", "CUST8", "Female", "Beauty", 5, 20, 0])

print("Fichier ventes.csv généré automatiquement.")

# 2. Lecture des données
df = pd.read_csv("ventes.csv")
print("\nAperçu des données :")
print(df.head())

# 3. Calculs
df["CA_Brut"] = df["Price per Unit"] * df["Quantity"]
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise (%)"] / 100)
df["TVA"] = df["CA_Net"] * 0.2

# 4. Résultats
ca_total = df["CA_Net"].sum()
print("\nChiffre d'affaires total :", round(ca_total, 2))

best = df.loc[df["CA_Net"].idxmax()]
print("\nProduit le plus rentable :")
print(best[["Transaction ID", "Product Category", "CA_Net"]])

# 5. Analyse
ca_categorie = df.groupby("Product Category")["CA_Net"].sum()
print("\nChiffre d'affaires par catégorie :")
print(ca_categorie)

ca_genre = df.groupby("Gender")["CA_Net"].sum()
df["Date"] = pd.to_datetime(df["Date"])
ca_temps = df.groupby("Date")["CA_Net"].sum()

# 6. Export
df.to_csv("resultats_final.csv", index=False)
print("\nFichier resultats_final.csv créé.")

# 7. Graphiques
# Graphique 1 : CA par catégorie
plt.figure()
ca_categorie.plot(kind="bar")
plt.title("Chiffre d'affaires par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("CA Net")
plt.xticks(rotation=30)
plt.savefig("graphique_categorie.png")
plt.close()

# Graphique 2 : CA par genre
plt.figure()
ca_genre.plot(kind="pie", autopct="%1.1f%%")
plt.title("Répartition du CA par genre")
plt.ylabel("")
plt.savefig("graphique_genre.png")
plt.close()

# Graphique 3 : Évolution dans le temps
plt.figure()
ca_temps.plot(marker="o")
plt.title("Évolution du chiffre d'affaires")
plt.xlabel("Date")
plt.ylabel("CA Net")
plt.savefig("graphique_temps.png")
plt.close()

print("Graphiques générés avec succès !")
