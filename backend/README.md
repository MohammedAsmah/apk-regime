# 🥗 Beauté Naturelle – Backend Assistant Nutritionnel (Mobile API)

![Django](https://img.shields.io/badge/Django-5.2.8-092E20?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/Django-REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

---

## 📋 Présentation du Projet

**Beauté Naturelle** est le backend officiel d’une application **mobile** dédiée au coaching nutritionnel intelligent et à la perte de poids personnalisée.

Cette API REST, développée avec **Django REST Framework**, fournit :
- La gestion des utilisateurs
- L’authentification sécurisée (JWT)
- Le calcul des besoins nutritionnels
- La communication temps réel avec l’application mobile

---

## 🎯 Objectif du Backend
- Servir de **backend mobile (Flutter / React Native)**
- Fournir des calculs nutritionnels fiables
- Assurer un échange rapide et sécurisé via API REST
- Supporter la montée en charge en production

---

## 🧠 Calcul Nutritionnel

### Métabolisme de Base (Mifflin-St Jeor)
Le backend calcule le **BMR (Basal Metabolic Rate)** afin d’estimer les besoins énergétiques journaliers 



*s dépend du sexe biologique.*

---

## ⚙️ Stack Technique

- **Langage** : Python 3.10+
- **Framework** : Django 5.2.8
- **API** : Django REST Framework
- **Base de données** :
  - SQLite (développement & tests)
  - PostgreSQL (production)
- **Authentification** : JWT (SimpleJWT)
- **Temps réel** : Django Channels + Daphne
- **Stockage** : AWS S3 / MinIO (optionnel)

---

## 🗄️ Environnements & Base de Données

### 🔹 Développement / Tests
- Base de données : **SQLite**
- Configuration simple pour développement mobile rapide

### 🔹 Production
- Base de données : **PostgreSQL**
- Configuration via variables d’environnement

---

## 🚀 Installation & Démarrage

### 1. Prérequis
- Python 3.10+
- pip
- virtualenv
- PostgreSQL (pour production)

---

### 2. Installation

```bash
git clone https://github.com/AGH-Data-Agency-Holding/APK-Regimes-Perte-de-Poids.git
cd APK-Regimes-Perte-de-Poids

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

### 3.  migrations 
python manage.py makemigrations
python manage.py migrate


### 4. demarrage 
python manage.py runserver
