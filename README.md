<<<<<<< HEAD
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

Voici le modèle logique final de la base de données :

```mermaid
classDiagram
    class ROLE {
        int id PK
        string name
        string description
    }

    class USER {
        int id PK
        string last_name
        string first_name
        string email (unique)
        string password
        datetime registration_date
        int role_id FK -> ROLE.id
    }

    class PATIENT {
        int id PK, FK -> USER.id
        date birth_date
    }

    class DOCTOR {
        int id PK, FK -> USER.id
        string speciality
        string hospital
    }

    class APPOINTMENT {
        int id PK
        int patient_id FK -> USER.id
        int medecin_id FK -> USER.id
        datetime appointment_datetime
        enum status {PENDING, CONFIRMED, CANCELLED}
    }

    %% Relations
    ROLE "1" --> "0..*" USER : "assigns"
    USER "1" --> "0..1" PATIENT : "is"
    USER "1" --> "0..1" DOCTOR : "is"
    USER "1" --> "0..*" APPOINTMENT : "books (as patient)"
    USER "1" --> "0..*" APPOINTMENT : "handles (as doctor)"


=======
# InFyWise2
a new version of my app
>>>>>>> 23c623577e9c710aa30345fe6ff60e2d572096d9
