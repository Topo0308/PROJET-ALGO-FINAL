# 💙 Gestionnaire de notes d’étudiants (Python)

Ce projet est un programme **Python en ligne de commande (terminal)** qui permet de gérer simplement une liste d’étudiants, leurs matricules et leurs notes, puis d’afficher des statistiques de classe et de sauvegarder les données dans un fichier texte.

---

## ✅ Fonctionnalités

- **Ajouter un étudiant**
  - Saisie sécurisée du **matricule** (alphanumérique uniquement)
  - Saisie sécurisée du **nom** (lettres + espaces uniquement)
  - Saisie sécurisée d’une **note sur 20** (entre 0 et 20)
  - Matricule **unique** (si le matricule existe déjà, le programme redemande)

- **Afficher tous les étudiants**
  - Affichage sous forme de **tableau aligné** (Matricule / Nom / Note)

- **Modifier un étudiant**
  - Possibilité de modifier le **nom**, la **note**, ou les **deux**

- **Supprimer un étudiant**
  - Suppression après confirmation

- **Afficher les statistiques de la classe**
  - Nombre d’étudiants
  - Moyenne générale
  - Meilleure note + étudiant correspondant
  - Pire note + étudiant correspondant

- **Sauvegarder et quitter**
  - Génère un fichier texte `notes.txt` contenant la liste des étudiants au format tableau

---

## 🧾 Pré-requis

- Python **3.x**
- Aucun module externe requis (uniquement Python standard)

---

## ▶️ Installation & Exécution

1. Copier le code dans un fichier, par exemple :
   - `gestion_notes.py`

2. Lancer le programme :

```bash
python gestion_notes.py
🧭 Utilisation (Menu)
Au lancement, le programme affiche un menu :

1 : Ajouter un étudiant

2 : Afficher tous les étudiants

3 : Modifier un étudiant

4 : Supprimer un étudiant

5 : Afficher les statistiques de la classe

6 : Sauvegarder et quitter

Exemple :

text
Copier le code
===== MENU GESTION DES NOTES =====
1 - Ajouter un étudiant
2 - Afficher tous les étudiants
3 - Modifier un étudiant
4 - Supprimer un étudiant
5 - Afficher les statistiques de la classe
6 - Sauvegarder et quitter
==================================
🔐 Validations intégrées
Matricule
Doit être alphanumérique uniquement (AB123, 2025A, etc.)

Le matricule est converti automatiquement en MAJUSCULES

Les doublons sont refusés

Nom
Lettres uniquement (espaces autorisés)

Le nom est automatiquement formaté en Title Case (ex: jean pierre → Jean Pierre)

Note
Doit être un nombre entre 0 et 20

Peut être saisie avec virgule ou point (12,5 ou 12.5)

Arrondie automatiquement à 2 décimales

📊 Statistiques de classe
Quand vous choisissez l’option 5, le programme affiche :

Nombre total d’étudiants

Moyenne de classe

Meilleure note (avec matricule et nom)

Pire note (avec matricule et nom)

💾 Fichier de sauvegarde
Quand vous choisissez l’option 6, le programme crée un fichier :

notes.txt

Contenu :

Tableau aligné : Matricule | Nom | Note

🗂️ Structure des données
Les étudiants sont stockés dans un dictionnaire Python :

python
Copier le code
etudiants = {
  "AB123": {"nom": "Alice Dupont", "note": 15.5},
  "CD456": {"nom": "Bob Martin", "note": 9.75}
}
🚀 Améliorations possibles
Ajouter plusieurs notes par étudiant et calculer la moyenne individuelle

Générer un rapport complet (bulletins + stats) dans un fichier dédié

Trier automatiquement l’affichage par matricule ou par note

Exporter en CSV ou Excel