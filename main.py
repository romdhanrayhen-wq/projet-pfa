import pandas as pd
import matplotlib.pyplot as plt
import os

fichier = r"C:\logiciel\vscode\projet pfa\amazon\amazon-e-commerce.csv"

print("Chargement en cours...")
df = pd.read_csv(fichier, encoding="utf-8")
print(f"OK : {len(df)} lignes chargees")

df["CA_Brut"] = df["price"]
df["CA_Net"]  = df["final_price"]
df["TVA"]     = df["CA_Net"] * 0.20
df["CA_TTC"]  = df["CA_Net"] + df["TVA"]

print("\n" + "="*50)
print("     RAPPORT DES VENTES - AMAZON E-COMMERCE")
print("="*50)
print(f"  Transactions  : {len(df):>12,}")
print(f"  CA Brut       : {df['CA_Brut'].sum():>12.2f} Rs")
print(f"  Remises       : {(df['CA_Brut'] - df['CA_Net']).sum():>12.2f} Rs")
print(f"  CA Net        : {df['CA_Net'].sum():>12.2f} Rs")
print(f"  TVA (20%)     : {df['TVA'].sum():>12.2f} Rs")
print(f"  CA TTC        : {df['CA_TTC'].sum():>12.2f} Rs")
print("="*50)

idx = df["CA_Net"].idxmax()
print(f"\nMeilleur produit : {df.loc[idx, 'product_id']}")
print(f"Categorie        : {df.loc[idx, 'category']}")
print(f"CA Net           : {df.loc[idx, 'CA_Net']:.2f} Rs")

print("\nCA Net par categorie :")
print("-"*40)
ca_cat = df.groupby("category")["CA_Net"].sum().sort_values(ascending=False)
for cat, ca in ca_cat.items():
    print(f"  {str(cat):<20} : {ca:>14.2f} Rs")

os.makedirs("graphiques", exist_ok=True)

plt.figure(figsize=(10, 5))
plt.bar(ca_cat.index.astype(str), ca_cat.values, color="#4C72B0", edgecolor="white")
plt.title("CA Net par categorie", fontsize=14, fontweight="bold")
plt.xlabel("Categorie")
plt.ylabel("CA Net (Rs)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("graphiques/ca_par_categorie.png", dpi=150)
plt.close()
print("Graphique 1 sauvegarde : ca_par_categorie.png")

top_brands = df.groupby("brand")["CA_Net"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
plt.bar(top_brands.index.astype(str), top_brands.values, color="#55A868", edgecolor="white")
plt.title("Top 10 marques par CA Net", fontsize=14, fontweight="bold")
plt.xlabel("Marque")
plt.ylabel("CA Net (Rs)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("graphiques/top10_marques.png", dpi=150)
plt.close()
print("Graphique 2 sauvegarde : top10_marques.png")

ca_pay = df.groupby("payment_method")["CA_Net"].sum().sort_values(ascending=False)
plt.figure(figsize=(7, 7))
plt.pie(ca_pay.values, labels=ca_pay.index.astype(str),
        autopct="%1.1f%%", startangle=140)
plt.title("CA Net par methode de paiement", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("graphiques/ca_par_paiement.png", dpi=150)
plt.close()
print("Graphique 3 sauvegarde : ca_par_paiement.png")

df.to_csv("resultats_final.csv", index=False, encoding="utf-8")
print("\nresultats_final.csv exporte avec succes")
print("\nAnalyse Amazon E-commerce terminee avec succes !")