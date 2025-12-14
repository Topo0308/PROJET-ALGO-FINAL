def saisir_matricule():
    """Saisie sécurisée d'un matricule (alphanumérique uniquement)."""
    while True:
        matricule = input("  Matricule : ").strip()

        if matricule.isalnum():
            return matricule.upper()  # normalisation : tout en majuscules
        else:
            print("  Matricule invalide ! Utilisez uniquement des lettres et/ou chiffres (for example : AB123).")


def saisir_nom():
    """Saisie sécurisée d'un nom (lettres uniquement, espaces autorisés)."""
    while True:
        nom = input("  Nom       : ").strip()

        if nom.replace(" ", "").isalpha():
            return nom.title()  # normalisation : première lettre en majuscule
        else:
            print("  Nom invalide ! Utilisez uniquement des lettres.")


def saisir_note():
    """Saisie sécurisée d'une note sur 20 (float entre 0 et 20)."""
    while True:
        try:
            note_str = input("  Note sur 20 : ").replace(",", ".")
            note = float(note_str)
            if 0 <= note <= 20:
                return round(note, 2)  # normalisation à 2 décimales
            print("  La note doit être comprise entre 0 et 20.")
        except ValueError:
            print("  Entrez un nombre valide pour la note.")


def afficher_etudiants(etudiants: dict):
    """Affiche tous les étudiants sous forme de tableau aligné."""
    if not etudiants:
        print("\nAucun étudiant enregistré.")
        return

    print("\nListe des étudiants :")
    print(f"{'Matricule':<15}{'Nom':<25}{'Note':>6}")
    print("-" * 46)
    for matricule, infos in etudiants.items():
        nom = infos["nom"]
        note = infos["note"]
        print(f"{matricule:<15}{nom:<25}{note:>6.2f}")
    print("-" * 46)


def sauvegarder_dans_fichier(etudiants: dict, nom_fichier="notes.txt"):
    """Sauvegarde les étudiants dans un fichier texte aligné."""
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"{'Matricule':<15}{'Nom':<25}{'Note':>6}\n")
        f.write("-" * 46 + "\n")
        for matricule, infos in etudiants.items():
            nom = infos["nom"]
            note = infos["note"]
            f.write(f"{matricule:<15}{nom:<25}{note:>6.2f}\n")

    print(f"\nDonnées sauvegardées dans le fichier : {nom_fichier}")
# ---------- Fonctions liées au menu ---------- #
def ajouter_etudiant(etudiants: dict):
    """Ajoute un étudiant si le matricule n'existe pas déjà."""
    print("\n=== Ajout d'un nouvel étudiant ===")
    matricule = saisir_matricule()

    if matricule in etudiants:
        print(" Ce matricule existe déjà ! Impossible d'ajouter un doublon.")
        return

    nom = saisir_nom()
    note = saisir_note()

    etudiants[matricule] = {"nom": nom, "note": note}
    print("  Étudiant ajouté avec succès.")


def modifier_etudiant(etudiants: dict):
    """Modifie le nom et/ou la note d'un étudiant existant."""
    print("\n=== Modification d'un étudiant ===")
    matricule = input("  Matricule de l'étudiant à modifier : ").strip().upper()

    if matricule not in etudiants:
        print("  Matricule introuvable.")
        return

    etu = etudiants[matricule]
    print(f"  Étudiant actuel : {etu['nom']} - Note : {etu['note']:.2f}")

    # Choix de ce qu'on modifie
    choix = input("  Modifier (n)om, (o)te, (b)oth ? [n/o/b] : ").lower().strip()

    if choix in ("n", "b"):
        nouveau_nom = saisir_nom()
        etu["nom"] = nouveau_nom

    if choix in ("o", "b"):
        nouvelle_note = saisir_note()
        etu["note"] = nouvelle_note

    print(" Étudiant modifié avec succès.")


def supprimer_etudiant(etudiants: dict):
    """Supprime un étudiant à partir de son matricule."""
    print("\n=== Suppression d'un étudiant ===")
    matricule = input("  Matricule de l'étudiant à supprimer : ").strip().upper()

    if matricule not in etudiants:
        print("  Matricule introuvable.")
        return

    etu = etudiants[matricule]
    confirm = input(f" Confirmer la suppression de {etu['nom']} (o/n) ? ").lower().strip()
    if confirm == "o":
        del etudiants[matricule]
        print(" Étudiant supprimé. ")
    else:
        print(" Suppression annulée. ")


def afficher_menu():
    """Affiche le menu principal."""
    print("\n===== MENU GESTION DES NOTES =====")
    print("1 - Ajouter un étudiant")
    print("2 - Afficher tous les étudiants")
    print("3 - Modifier un étudiant")
    print("4 - Supprimer un étudiant")
    print("5 - Sauvegarder et quitter")
    print("==================================")


def main():
    etudiants = {}  # {matricule: {"nom": str, "note": float}}

    print("=== Système de gestion des notes d'étudiants ===")

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_etudiant(etudiants)
        elif choix == "2":
            afficher_etudiants(etudiants)
        elif choix == "3":
            modifier_etudiant(etudiants)
        elif choix == "4":
            supprimer_etudiant(etudiants)
        elif choix == "5":
            sauvegarder_dans_fichier(etudiants)
            print("Au revoir !")
            break
        else:
            print("  Choix invalide, veuillez recommencer.")


if __name__ == "__main__":
    main()
############################################################
#  Gestionnaire de notes d'étudiants
#  - Menu (ajouter, afficher, modifier, supprimer, quitter)
#  - Matricules uniques (pas de doublons)
#  - Nom et matricule normalisés
#  - Notes normalisées (0 à 20, arrondies à 2 décimales)
#  - Sauvegarde dans notes.txt (tableau aligné)
############################################################