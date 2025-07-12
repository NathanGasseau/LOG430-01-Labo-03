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
git clone https://github.com/NathanGasseau/LOG430-01-Labo-02.git
cd LOG430-01-Labo-02
docker-compose up --build
```

Accéder à l’application :  
[http://localhost:8000](http://localhost:8000)  
Ou : [http://IP-DE-LA-VM:8000](http://IP-DE-LA-VM:8000) si lancé depuis une VM distante.

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
git clone https://github.com/NathanGasseau/LOG430-01-Labo-02.git
cd LOG430-01-Labo-02
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
LOG430-01-Labo-02/
│
├── sgc/             # Répertoire du projet Django
│   ├── settings.py          # Configuration du projet
│   ├── urls.py              # Routes principales
│   └── ...
│
├── caisse/                  # Application Django principale
│   ├── models.py            # Modèles de données (Produit, Vente, etc.)
│   ├── views.py             # Logique des vues / API
│   ├── services/            # Logique métier (StockService, etc.)
│   ├── templates/           # Fichiers HTML (si UI)
│   └── ...
│
├── db/
│   └── init_postgres.sql    # Script de création des tables PostgreSQL
│
├── docker-compose.yml       # Configuration Docker multi-services
├── Dockerfile               # Image Docker Django
├── manage.py                # Entrée principale Django
├── requirements.txt         # Dépendances python3
└── README.md                # Ce fichier
```

---

### 💡 Remarques  
- Le projet suit une architecture **monolithique modulaire**.  
- Des composants comme `CaisseService` ou `MaisonMereService` orchestrent les opérations métiers.  
- L’interface employé est en ligne de commande, mais l’extension vers une UI web est envisageable.