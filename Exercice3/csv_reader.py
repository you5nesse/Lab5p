
import os
import csv


# Exception principale
class CsvException(Exception):
    pass


# Exception fichier introuvable
class FichierIntrouvableException(CsvException):
    pass


# Exception ligne invalide
class LigneInvalideException(CsvException):
    pass


# Exception prix négatif ou nul
class PrixNegatifException(CsvException):
    pass


def charger_csv(chemin):

    # Vérifier l'existence du fichier
    if not os.path.isfile(chemin):
        raise FichierIntrouvableException(
            f"Le fichier '{chemin}' est introuvable."
        )

    articles = []

    try:
        with open(chemin, mode="r", encoding="utf-8-sig", newline="") as fichier:

            lecteur = csv.reader(fichier, delimiter=';')

            # Lire l'en-tête
            try:
                entete = next(lecteur)
            except StopIteration:
                raise LigneInvalideException("Le fichier est vide.")

            # Nettoyer l'en-tête
            entete = [col.strip().lower() for col in entete]

            if entete != ["id", "nom", "prix"]:
                raise LigneInvalideException(
                    f"En-tête CSV invalide : {entete}"
                )

            # Parcourir les lignes
            for numero, ligne in enumerate(lecteur, start=2):

                # Ignorer les lignes vides
                if not ligne or all(col.strip() == "" for col in ligne):
                    continue

                # Vérifier le nombre de colonnes
                if len(ligne) != 3:
                    raise LigneInvalideException(
                        f"Ligne {numero} : 3 colonnes sont attendues."
                    )

                identifiant, nom, prix = ligne

                # Vérifier ID et nom
                if not identifiant.strip() or not nom.strip():
                    raise LigneInvalideException(
                        f"Ligne {numero} : ID ou nom manquant."
                    )

                # Vérifier le prix
                try:
                    prix = float(prix.strip())
                except ValueError:
                    raise LigneInvalideException(
                        f"Ligne {numero} : prix non numérique."
                    )

                if prix <= 0:
                    raise PrixNegatifException(
                        f"Ligne {numero} : le prix doit être supérieur à zéro."
                    )

                # Ajouter l'article
                articles.append({
                    "id": identifiant.strip(),
                    "nom": nom.strip(),
                    "prix": prix
                })

    except UnicodeDecodeError:
        raise LigneInvalideException(
            "Le fichier doit être encodé en UTF-8."
        )

    return articles
