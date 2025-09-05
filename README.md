InfyWise – API d’infertilité féminine
InfyWise est une plateforme REST pensée pour accompagner les patientes et les médecins dans le suivi de l’infertilité féminine.
Le backend est développé en Python avec Flask et SQLAlchemy, le frontend en Angular pour une interface réactive et intuitive.

🎯 Objectif
Offrir un écosystème complet où :
• 	Les patientes peuvent créer un compte, partager leurs témoignages, gérer leurs rendez-vous.
• 	Les médecins référencent des pathologies (avec causes & effets), prennent et valident les rendez-vous.
• 	Les médecins experts (rôle ADMIN) modèrent et catégorisent les témoignages et pathologies selon leur spécialité.

1. Exigences et User Stories

1.1 Acteurs et rôles
• 	Un utilisateur non authentifié
• 	Un patient
• 	Un médecin
• 	Un ADMIN (médecin doté du rôle ADMIN)
Chaque utilisateur peut cumuler plusieurs rôles (PATIENT, MEDECIN, ADMIN). Un patient peut aussi être médecin, et inversement.

1.2 User Stories détaillées

• 	En tant qu’utilisateur non authentifié,

je veux m’inscrire (nom, prénom, date de naissance, email, mot de passe),
afin de créer un compte InfyWise.

• 	En tant qu’utilisateur,

je veux me connecter (login) et me déconnecter (logout),
afin d’accéder à mes données en toute sécurité.

• 	En tant qu’utilisateur authentifié,
je veux consulter et mettre à jour mon profil,
afin de garder mes informations personnelles à jour.

• 	En tant qu’utilisateur,
je veux obtenir un ou plusieurs rôles (PATIENT, MEDECIN),
afin de bénéficier des fonctionnalités appropriées.

• 	En tant que médecin,
je veux pouvoir demander ou recevoir le rôle ADMIN,
uniquement si j’ai au moins une spécialité,
afin de modérer et catégoriser les contenus soumis par les patientes.

• 	En tant que patient,
je veux soumettre un témoignage libre sur mon parcours,
afin de partager mon expérience.

• 	En tant qu’ADMIN,
je veux lister tous les témoignages et pathologies en attente,
afin de valider ou rejeter leur publication et de les assigner à des catégories.

• 	En tant que médecin,
je veux créer une pathologie (nom, description, spécialité),
afin de référencer une nouvelle problématique d’infertilité.

• 	En tant que médecin,
je veux ajouter des causes et des effets à une pathologie,
afin de documenter ses facteurs et ses conséquences.

 	En tant que patient,
je veux prendre, modifier ou annuler mes rendez-vous,
afin de gérer mon suivi médical.

• 	En tant que médecin,
je veux consulter les rendez-vous demandés et les confirmer ou refuser,
afin d’organiser mon planning.
2. 
Modèle Conceptuel de Données (MCD)

Entités principales et associations :
• 	Utilisateur (1,n) ←→ (n,1) Roles via UserRoles
• 	Utilisateur (1,n) ←→ (n,1) Specialite via UserSpecialites
• 	Pathologie (n,1) ←→ Specialite
• 	Pathologie (1,n) ←→ Cause
• 	Pathologie (1,n) ←→ Effet
• 	Pathologie (n,m) ←→ Categorie via PathologieCategories
• 	Temoignage (n,m) ←→ Categorie via TemoignageCategories
• 	Utilisateur (1,n) ←→ Temoignage
• 	Utilisateur (1,n) ←→ RendezVous (comme patient)
• 	Utilisateur (1,n) ←→ RendezVous (comme medecin)
3. 
4. Modèle Logique de Données (MLD)
## 📌 Modèle Logique de Données (MLD)

## 📌 Modèle Logique de Données (MLD)

Voici le modèle logique final de la base de données :

```mermaid
erDiagram
    USERS {
        int id PK
        varchar first_name
        varchar last_name
        date birth_date
        varchar email
        varchar password_hash
        datetime created_at
        datetime updated_at
    }
    ROLES {
        int id PK
        enum name
    }
    USER_ROLES {
        int user_id PK, FK
        int role_id PK, FK
    }
    SPECIALITES {
        int id PK
        varchar name
    }
    USER_SPECIALITES {
        int user_id PK, FK
        int specialite_id PK, FK
    }
    CATEGORIES {
        int id PK
        varchar name
    }
    PATHOLOGIES {
        int id PK
        varchar name
        text description
        enum status
        int specialite_id FK
        datetime created_at
        datetime updated_at
    }
    PATHOLOGIE_CAUSES {
        int id PK
        int pathologie_id FK
        text description
    }
    PATHOLOGIE_EFFETS {
        int id PK
        int pathologie_id FK
        text description
    }
    PATHOLOGIE_CATEGORIES {
        int pathologie_id PK, FK
        int category_id PK, FK
    }
    TEMOIGNAGES {
        int id PK
        int user_id FK
        text content
        datetime submitted_at
        enum status
    }
    TEMOIGNAGE_CATEGORIES {
        int temoignage_id PK, FK
        int category_id PK, FK
    }
    RENDEZ_VOUS {
        int id PK
        int patient_id FK
        int medecin_id FK
        datetime appointment_datetime
        enum status
        text commentaire
    }

    USERS ||--o{ USER_ROLES           : has
    ROLES ||--o{ USER_ROLES           : assigned_to
    USERS ||--o{ USER_SPECIALITES     : specializes_in
    SPECIALITES ||--o{ USER_SPECIALITES : assigned_to
    SPECIALITES ||--o{ PATHOLOGIES      : contains
    PATHOLOGIES ||--o{ PATHOLOGIE_CAUSES   : has_causes
    PATHOLOGIES ||--o{ PATHOLOGIE_EFFETS   : has_effects
    PATHOLOGIES ||--o{ PATHOLOGIE_CATEGORIES: categorized_in
    CATEGORIES ||--o{ PATHOLOGIE_CATEGORIES : applies_to
    USERS ||--o{ TEMOIGNAGES          : writes
    TEMOIGNAGES ||--o{ TEMOIGNAGE_CATEGORIES: categorized_in
    CATEGORIES ||--o{ TEMOIGNAGE_CATEGORIES: applies_to
    USERS ||--o{ RENDEZ_VOUS          : requests_as_patient
    USERS ||--o{ RENDEZ_VOUS          : manages_as_medecin
