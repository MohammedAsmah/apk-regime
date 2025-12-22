# 🥗 Beauté Naturelle - Backend Assistant IA Nutritionnel

![Django](https://img.shields.io/badge/Django-5.2.8-092E20?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

## 📋 Présentation du Projet
Ce dépôt contient le moteur central (Backend) de l'application **Beauté Naturelle**, un écosystème intelligent dédié à l'accompagnement personnalisé pour la perte de poids. Développé avec **Django REST Framework**, ce système intègre des algorithmes de calcul métabolique et une architecture temps réel pour un coaching interactif.

---

## 🧠 Intelligence Artificielle & Nutrition

Le backend repose sur des protocoles scientifiques rigoureux pour garantir des résultats optimaux :

### 1. Métabolisme Prédictif (Équation de Mifflin-St Jeor)
Le système calcule dynamiquement le **BMR** (Basal Metabolic Rate) pour définir les besoins caloriques journaliers en fonction du profil utilisateur.
$$BMR = 10 \times \text{poids (kg)} + 6.25 \times \text{taille (cm)} - 5 \times \text{âge (ans)} + s$$

### 2. Analyse des Macronutriments
Intégration d'une base de données exhaustive permettant de décomposer chaque aliment en :
* **Protéines** : Maintien de la masse musculaire.
* **Lipides** : Équilibre hormonal et vitamines liposolubles.
* **Glucides** : Gestion de l'index glycémique et de l'énergie.



### 3. Coaching Interactif via WebSockets
Utilisation de **Daphne** et **Django Channels** pour assurer une communication bidirectionnelle asynchrone, permettant à l'assistant IA de fournir un feedback instantané sur les repas saisis.



---

## 🛠️ Stack Technique

* **Langage** : Python 3.14+
* **Framework Web** : Django 5.2.8 / DRF
* **Serveur ASGI** : Daphne (Gestion des WebSockets)
* **Base de Données** : PostgreSQL
* **Stockage Cloud** : AWS S3 / MinIO (Gestion des photos de repas et rapports)
* **Sécurité** : SimpleJWT (Rotation de tokens) & Python-Dotenv

---

## 🚀 Installation et Démarrage

### 1. Prérequis
- Python 3.10 ou supérieur
- PostgreSQL installé et configuré

### 2. Configuration de l'environnement
```bash
# Activer l'environnement virtuel
".\venv\Scripts\activate"

# Installer les dépendances
pip install -r requirements.txt