# --------------------------
# Classe Personne :
# --------------------------
class Personne:
    def __init__(self, nom, poid):
        self.__nom = nom
        self.__poid = poid




# --------------------------
# Classe Endroit
# --------------------------
class Endroit:
    def __init__(self, abs, ord):
        self.__abs = abs
        self.__ord = ord




# --------------------------
# Classe TaxiScooter
# --------------------------
class TaxiScooter:
    def __init__(self):
        self.__p1 = None
        self.__p2 = None
        self.__endroit = Endroit(0, 0)
        self.__poids = 0.0
        self.__poid_max = 180.0

    def entrer(self, personne):
        if self.__p1 is not None and self.__p2 is not None:
            print("❌ Le taxi est plein.")
            return
        if self.__p1 is None:
            self.__p1 = personne
        else:
            self.__p2 = personne
        self.__poids += personne.get_poid()

    def sortir(self, personne):
        if self.__p1 == personne:
            self.__p1 = None
            self.__poids -= personne.get_poid()
        elif self.__p2 == personne:
            self.__p2 = None
            self.__poids -= personne.get_poid()
        else:
            print("⚠️ La personne n'est pas dans le taxi.")

    def est_en_surpoids(self):
        return self.__poids > self.__poid_max

    def deplacer(self, depart, arrivee):
        if self.est_en_surpoids():
            return False
        self.__endroit.set_abs(arrivee.get_abs())
        self.__endroit.set_ord(arrivee.get_ord())
        return True

    def __str__(self):
        return f"Le taxi est à l’endroit ({self.__endroit.get_abs()}, {self.__endroit.get_ord()}), de poids total : {self.__poids} kg."

    # Getters pour accéder au poids et à l’endroit sans property
    def get_poids(self):
        return self.__poids

    def get_endroit(self):
        return self.__endroit


# --------------------------
# Fonction de test avec assert et affichage
# --------------------------
def test_taxi_scooter():
    print("\n🔧 Initialisation")
    p1 = Personne("Alain", 120)
    p2 = Personne("Jean", 100)
    p3 = Personne("Slim", 60)

    depart = Endroit(0, 0)
    arrivee = Endroit(10, 10)
    taxi = TaxiScooter()

    print("\n🚕 Entrée de p1 (120 kg)")
    taxi.entrer(p1)
    assert taxi.get_poids() == 120
    print("✅ p1 embarqué, poids total = 120 kg")

    print("\n🚕 Entrée de p2 (100 kg)")
    taxi.entrer(p2)
    assert taxi.get_poids() == 220
    print("✅ p2 embarqué, poids total = 220 kg")
    assert taxi.est_en_surpoids()
    print("✅ Surpoids détecté")

    print("\n🚫 Tentative de déplacement en surpoids")
    assert not taxi.deplacer(depart, arrive)
    print("✅ Déplacement bloqué en surpoids")

    print("\n🧍 Sortie de p2")
    taxi.sortir(p2)
    assert taxi.get_poids() == 160
    assert not taxi.est_en_surpoids()
    print("✅ p2 est sorti, poids total = 120 kg, plus de surpoids")

    print("\n🚕 Déplacement autorisé vers (10,10)")
    assert taxi.deplacer(depart, arrivee)
    e = taxi.get_endroit()
    assert e.get_abs() == 10 and e.get_ord() == 8
    print("✅ Déplacement effectué avec succès")

    print("\n🧍 Entrée de p3 (60 kg)")
    taxi.entrer(p3)
    assert taxi.get_poids() == 180
    print("✅ p3 embarqué, poids total = 180 kg")

    print("\n🧍 Sortie de p1 et p3")
    taxi.sortir(p1)
    taxi.sortir(p3)
    assert taxi.get_poids() == 0
    print("✅ p1 et p3 sont sortis, taxi vide")

    print("\n🔎 Vérification finale du poids")
    assert taxi.get_poids() == 0
    print("✅ Poids vérifié : 0 kg")

    print("\n📍 État final du taxi :")
    print(taxi)

    print("\n🎉 Tous les tests ont réussi avec succès.")


# Exécution du test
test_taxi_scooter()
