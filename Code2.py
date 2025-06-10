import numpy as np

# Données : nombre d'incidents détectés chaque mois
incidents = np.array([12, 9, 14, 7, 8, 11, 13, 6, 15, 10, 9, 12])

# 1. Afficher tous les incidents détectés par mois
print("📊 Incidents mensuels :", incidents)

# 2. Statistiques
total_annuel = incidents.sum()
moyenne = incidents.mean()
maximum = incidents.max()
minimum = incidents.min()

print("\n📈 Statistiques annuelles :")
print("Nombre total d'incidents :", total_annuel)
print("Nombre moyen d'incidents par mois :", moyenne)
print("Maximum d'incidents détectés dans un mois :", maximum)
print("Minimum d'incidents détectés dans un mois :", minimum)

# 3. Évaluation de la tendance
if moyenne > 10:
    print("\n⚠️ Attention : Tendance élevée d’incidents.")
else:
    print("\n✅ Niveau d’incidents sous contrôle.")

# 4. Les valeurs des incidents supérieurs à 12
incidents_critique = incidents[incidents > 12]
print("\n🚨 Les valeurs des incidents supérieurs à 12 :", incidents_critique)

# 5. Réduction de 20 % des incidents grâce à l'amélioration de la sécurité
incidents_reduits = incidents * 0.8
print("\n🔧 Incidents après réduction de 20 % :", incidents_reduits)

# 6. Trier les incidents réduits par ordre croissant
incidents_trie = np.sort(incidents_reduits)
print("\n📉 Incidents réduits triés :", incidents_trie)
