📚 PROJET ALGO – Gestionnaire de Notes d'Étudiants

Projet académique développé dans le cadre du cours Principes Algorithmiques et Programmation


📖 Présentation du Projet
Ce programme Python permet de gérer simplement les notes d'étudiants directement depuis votre terminal. 
Conçu selon la méthodologie Waterfall (analyse → conception → développement → tests → déploiement), il offre une solution complète pour :
✅ Enregistrer les matricules et notes de plusieurs étudiants
✅ Calculer automatiquement les moyennes individuelles
✅ Déterminer qui est admis ou ajourné
✅ Générer des statistiques de classe
✅ Créer un rapport récapitulatif au format texte

🎯 Fonctionnalités Détaillées
1️⃣ Saisie Interactive des Données Étudiants
Le programme vous guide pas à pas pour enregistrer vos étudiants :
🔹 Entrez le nom de l'étudiant
🔹 Saisissez ses notes une par une (entre 0 et 20)
🔹 Tapez 'q' pour passer à l'étudiant suivant
🔹 Recommencez jusqu'à avoir saisi tous vos étudiants

Validation automatique :

✓ Seules les notes entre 0 et 20 sont acceptées
✓ Messages d'erreur clairs en cas de saisie invalide
✓ Possibilité d'arrêter à tout moment


2️⃣ Bulletins Individuels
Pour chaque étudiant, le programme affiche un bulletin complet :
════════════════════════════════
📋 BULLETIN DE ALICE
════════════════════════════════
📝 Notes : 16.0, 14.5, 19.0
📊 Moyenne : 16.50/20
✅ Statut : ADMIS
════════════════════════════════
Le statut est automatiquement déterminé :

✅ ADMIS si moyenne ≥ 10/20
❌ AJOURNÉ si moyenne < 10/20


3️⃣ Statistiques de Classe
Le programme calcule automatiquement :
StatistiqueDescription📈 Moyenne de classeMoyenne de toutes les notes de tous les étudiants🏆 Meilleure noteNote maximale obtenue📉 Pire noteNote minimale obtenue👥 Nombre d'étudiantsTotal d'étudiants évalués
Exemple d'affichage :
═══════════════════════════════════
📊 STATISTIQUES DE LA CLASSE
═══════════════════════════════════
📈 Moyenne générale : 13.45/20
🏆 Meilleure note : 19.00/20
📉 Note la plus basse : 8.50/20
👥 Nombre d'étudiants : 25
═══════════════════════════════════

4️⃣ Génération de Rapport
Le programme crée automatiquement un fichier rapport_notes.txt contenant :

Section 1 : Bulletins détaillés

Matricule de chaque étudiant
Un bulletin complet pour chaque étudiant
Toutes les notes individuelles
Moyennes et statuts


Section 2 : Statistiques globales

Vue d'ensemble de la classe
Indicateurs de performance



📁 Le fichier est créé dans le même dossier que le programme

🚀 Installation et Lancement dans VS Code
Prérequis

Python 3.x installé sur votre ordinateur (Télécharger Python)
Visual Studio Code installé (Télécharger VS Code)
Extension Python pour VS Code (installée depuis le marketplace VS Code)
Aucune bibliothèque externe nécessaire ! 🎉


Étapes d'installation et configuration
1️⃣ Préparer le projet

Créez un nouveau dossier pour votre projet (ex: gestion_notes)
Téléchargez ou copiez le fichier main.py dans ce dossier


2️⃣ Ouvrir le projet dans VS Code
Méthode 1 : Depuis VS Code

Ouvrez VS Code
Fichier → Ouvrir le dossier...
Sélectionnez votre dossier gestion_notes

Méthode 2 : Depuis l'explorateur de fichiers

Windows : Clic droit sur le dossier → Ouvrir avec Code
Mac : Clic droit sur le dossier → Ouvrir avec → Visual Studio Code
Linux : Clic droit sur le dossier → Ouvrir dans Code


3️⃣ Vérifier l'installation de Python
Dans VS Code, ouvrez le terminal intégré :

Raccourci : Ctrl + ù (Windows/Linux) ou Cmd + J (Mac)
Menu : Terminal → Nouveau terminal

Tapez la commande suivante pour vérifier Python :
bashpython --version
ou sur Mac/Linux :
bashpython3 --version
```

**Résultat attendu :**
```
Python 3.11.5

4️⃣ Lancer le programme

**Avec le bouton "Run"**

1. Ouvrez le fichier `main.py`
2. Cliquez sur le bouton **▶️ Run** en haut à droite
3. Ou utilisez le raccourci : `Ctrl + F5` (Windows/Linux) ou `Cmd + F5` (Mac)


## 💡 Guide d'Utilisation Pas à Pas

### Scénario d'utilisation typique

**Étape 1 : Démarrage**
```
=== Système de gestion des notes d'étudiants ===

Matricule de l'étudiant (ou 'q' pour terminer) : ETU001
Nom de l'étudiant : Alice
```

**Étape 2 : Saisie des notes**
```
Saisie des notes pour Alice (ETU001) :
Entrez une note (ou 'q' pour terminer) : 16
Note ajoutée : 16.0

Entrez une note (ou 'q' pour terminer) : 14.5
Note ajoutée : 14.5

Entrez une note (ou 'q' pour terminer) : 19
Note ajoutée : 19.0

Entrez une note (ou 'q' pour terminer) : q
Notes enregistrées pour Alice : [16.0, 14.5, 19.0]
```

**Étape 3 : Ajout d'autres étudiants**
```
Matricule de l'étudiant (ou 'q' pour terminer) : ETU002
Nom de l'étudiant : Bob
Saisie des notes pour Bob (ETU002) :
...
```

**Étape 4 : Fin de saisie**
```
Matricule de l'étudiant (ou 'q' pour terminer) : q

📊 Traitement des résultats...
```

**Étape 5 : Affichage des résultats**
- Les bulletins s'affichent dans le terminal
- Les statistiques sont calculées
- Le fichier `rapport_notes.txt` est créé

---

## 📄 Comment Obtenir le Rapport .txt

### 🔍 Localisation du fichier

Une fois le programme terminé, le fichier **`rapport_notes.txt`** est automatiquement créé dans le **même dossier** que votre fichier `main.py`.

---

### 📂 Accéder au fichier dans VS Code

**Méthode 1 : Explorateur de fichiers VS Code**

1. Dans le panneau de gauche de VS Code, vous verrez apparaître `rapport_notes.txt`
2. Cliquez dessus pour l'ouvrir dans l'éditeur
```
📁 VOTRE_DOSSIER
  ├── 📄 main.py
  └── 📄 rapport_notes.txt  ⬅️ Nouveau fichier créé
