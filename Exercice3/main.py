
from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


def main():

    chemin = "articles.csv"

    try:
        articles = charger_csv(chemin)

        print("Importation réussie !")
        print("\nListe des articles :")

        for article in articles:
            print(article)

    except FichierIntrouvableException as e:
        print("Erreur fichier :", e)

    except PrixNegatifException as e:
        print("Erreur prix :", e)

    except LigneInvalideException as e:
        print("Erreur format :", e)


if __name__ == "__main__":
    main()
