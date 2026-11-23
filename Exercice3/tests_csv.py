
import unittest
import os

from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


class TestCSV(unittest.TestCase):

    def setUp(self):
        with open("test.csv", "w", encoding="utf-8") as f:
            f.write("id;nom;prix\n")
            f.write("1;Clavier;150\n")
            f.write("2;Souris;80\n")
            f.write("3;Ecran;1200\n")

    def tearDown(self):
        if os.path.exists("test.csv"):
            os.remove("test.csv")

    def test_csv_valide(self):
        articles = charger_csv("test.csv")

        self.assertEqual(len(articles), 3)
        self.assertEqual(articles[0]["nom"], "Clavier")
        self.assertEqual(articles[0]["prix"], 150.0)

    def test_fichier_absent(self):
        with self.assertRaises(FichierIntrouvableException):
            charger_csv("inexistant.csv")

    def test_prix_texte(self):
        with open("test.csv", "w", encoding="utf-8") as f:
            f.write("id;nom;prix\n1;Clavier;abc\n")

        with self.assertRaises(LigneInvalideException):
            charger_csv("test.csv")

    def test_prix_negatif(self):
        with open("test.csv", "w", encoding="utf-8") as f:
            f.write("id;nom;prix\n1;Clavier;-50\n")

        with self.assertRaises(PrixNegatifException):
            charger_csv("test.csv")

    def test_colonne_manquante(self):
        with open("test.csv", "w", encoding="utf-8") as f:
            f.write("id;nom;prix\n1;Clavier\n")

        with self.assertRaises(LigneInvalideException):
            charger_csv("test.csv")

    def test_colonne_supplementaire(self):
        with open("test.csv", "w", encoding="utf-8") as f:
            f.write("id;nom;prix\n1;Clavier;150;informatique\n")

        with self.assertRaises(LigneInvalideException):
            charger_csv("test.csv")


if __name__ == "__main__":
    unittest.main()
