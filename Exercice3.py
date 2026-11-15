
import datetime
import copy


class ValidationMixin:

    def valider_titre(self):
        if not self.titre or not self.titre.strip():
            raise ValueError("Erreur : le titre est obligatoire !")


class HistoriqueMixin:

    def __init__(self):
        self.historique = []

    def enregistrer_historique(self):
        ancienne_description = copy.copy(self.description)

        self.historique.append({
            "date": datetime.datetime.now(),
            "description": ancienne_description
        })

    def afficher_historique(self):
        print("\n Historique des modifications ")

        for element in self.historique:
            print("Date :", element["date"])
            print("Ancienne description :", element["description"])
            print("\n")


class JournalisationMixin:

    def journaliser(self, message):
        print(f"[LOG] {datetime.datetime.now()} : {message}")


class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):

    def __init__(self, titre, description):

        HistoriqueMixin.__init__(self)

        self.titre = titre
        self.description = description
        self.date_creation = datetime.datetime.now()

        self.valider_titre()

        self.journaliser("Création de la tâche")


    def mettre_a_jour(self, description):

        self.valider_titre()

        self.journaliser("Modification de la tâche")

        self.enregistrer_historique()

        self.description = description



t = Tache("Projet IA", "Première description")

t.mettre_a_jour("Deuxième description")

t.mettre_a_jour("Troisième description")

t.afficher_historique()
