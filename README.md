### ✍️ Auteur  
**Nom** : Nathan Gasseau  
**Cours** : LOG430-01  
**Session** : ÉTÉ 2025  

---

### 🎯 Système de Gestion de Caisse (SGC)  
Cette application Django simule un système de gestion de caisse pour un réseau de petits magasins connectés à une maison mère. Elle offre différentes interfaces selon le rôle (employé, gestionnaire, responsable logistique) et permet de :

- Rechercher des produits par nom, catégorie ou identifiant  
- Enregistrer des ventes et gérer les retours  
- Suivre l'état du stock local et central  
- Initier des demandes d’approvisionnement  
- Générer des rapports consolidés sur les ventes  
- Visualiser les performances des magasins  

L'application utilise PostgreSQL comme base de données centrale, avec un **pool de connexions** partagé entre les services internes. Django ORM assure la persistance et les transactions.

---

### 🔧 Méthodes d’exécution  

#### 📦 Option 1 – Via Docker (recommandé en production ou en CI/CD)

Prérequis : [Docker](https://www.docker.com/) et [docker-compose](https://docs.docker.com/compose/)

```bash
git clone https://github.com/NathanGasseau/LOG430-01-Labo-03.git
cd LOG430-01-Labo-02
docker-compose up --build
```

Accéder à l’application :  
[http://localhost:8000](http://localhost:8000)  
Ou : [http://10.194.32.191:8000](http://10.194.32.191:8000) si lancé depuis une VM distante.

---

#### 💻 Option 2 – Lancement manuel local (environnement virtuel)

Prérequis :
- python3 3.10+  
- pip + virtualenv  
- PostgreSQL (local ou via Docker)  
- Django 4.x  
- (Optionnel) pgAdmin ou autre client PostgreSQL

```bash
# Cloner et installer
git clone https://github.com/NathanGasseau/LOG430-01-Labo-03.git
cd LOG430-01-Labo-03
python3 -m venv venv
source venv/bin/activate  # (Sous Windows: venv\Scripts\activate)
pip install -r requirements.txt

# Configuration et exécution
python3 manage.py migrate
python3 manage.py loaddata initial_data.json  # Optionnel
python3 manage.py runserver
```

Accéder à l’application : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 📁 Structure du projet Django  

```
LOG430-01-Labo-03/
│
├── api/                     # Application exposant les endpoints REST
│   ├── controllers.py       # Contrôleurs RESTful
│   ├── authentication.py    # Gestion de l’authentification
│   ├── urls.py              # Routes de l’API
│   └── ...
│
├── sgc/                     # Répertoire du projet Django principal
│   ├── settings.py          # Configuration Django
│   ├── urls.py              # Routes principales
│   ├── views.py             # Vues principales
│   ├── caisse/              # Application métier – caisse
│   │   ├── services/        # Logique métier (CaisseService, etc.)
│   │   ├── urls.py
│   │   └── ...
│   ├── core/                # Domaine principal : modèles et services
│   │   ├── models.py
│   │   ├── repositories/
│   │   ├── services/
│   │   └── ...
│   ├── maison_mere/         # Application maison mère
│   │   ├── views.py
│   │   └── ...
│   ├── templates/           # Fichiers HTML (interface ou emails)
│   │   ├── accueil.html
│   │   └── menu.html
│   └── ...
│
├── docs/                    # Documentation technique
│   ├── ADR/                 # Architecture Decision Records
│   └── UML/                 # Diagrammes UML
│
├── docker-compose.yml       # Orchestration multi-services
├── Dockerfile               # Image Docker de l’application
├── manage.py                # Entrée Django
├── requirements.txt         # Dépendances Python
├── README.md                # Fichier d’instructions
└── venv/                    # Environnement virtuel Python (local)
```

