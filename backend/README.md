# 🥗 APK-Regime - Assistant IA Nutritionnel (Backend)

Hada howa l-moteur central dyal l-application **Beauté Naturelle**, m-gadd b **Django REST Framework** w m-optimizé bach i-dir wa7ed l-suivi d-qiq l-perte de poids b-stikhdam l-Intelligence Artificielle.

## 🧠 Intelligence d-l-Assistant IA
L-backend kiy-tabbaq l-marahil l-3ilmiya d-l-cadrage nutritionnel bach i-3ti n-asa'i7 m-kh-essesa:

### 1. Calculateur Métabolique (Mifflin-St Jeor)
L-Assistant kiy-7seb l-**BMR** (Basal Metabolic Rate) dyal l-user automatique bach i-3ref ch-hal dyal l-energy kiy-7req l-jismi f l-7ala d-l-ra7a.
* **Formule**: $10 \times \text{poids (kg)} + 6.25 \times \text{taille (cm)} - 5 \times \text{âge (ans)} + s$


### 2. Base de Données Nutritionnelle (50k+ Aliments)
Integration d-wa7ed l-dataset kbir fih l-macronutriments:
* **Protéines**: Bach n-7afdo 3la l-3adala.
* **Lipides**: L-douhoun l-moufida.
* **Glucides**: Masdar l-taqa.


### 3. Coaching en Temps Réel (WebSockets)
Utilisation d-**Daphne** w **Django Channels** bach l-IA t-welli t-jaweb l-user real-time dakhil l-app Flutter.


---

## 🛠️ Configuration Technique

### ⚙️ Stack Technique
* **Framework**: Django 5.2.8 / Django REST Framework
* **Real-time**: Daphne / Channels (ASGI)
* **Database**: PostgreSQL (nutri_fit)
* **Storage**: AWS S3 / MinIO (nutrifit-media)
* **Security**: JWT Authentication / python-dotenv

### 🚀 Lancement Rapide
1. **Activ-i l-venv**: 
   ```bash
   ".\venv\Scripts\activate"