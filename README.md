InfyWise – API d’infertilité féminine
InfyWise est une plateforme REST pensée pour accompagner les patientes et les médecins dans le suivi de l’infertilité féminine.
Le backend est développé en Python avec Flask et SQLAlchemy, le frontend en Angular pour une interface réactive et intuitive.

🎯 Objectif
Offrir un écosystème complet où :
• 	Les patientes peuvent créer un compte, partager leurs témoignages, gérer leurs rendez-vous.
• 	Les médecins référencent des pathologies (avec causes & effets), prennent et valident les rendez-vous.
• 	Les médecins experts (rôle ADMIN) modèrent et catégorisent les témoignages et pathologies selon leur spécialité.

1. Exigences et User Stories

User Stories InfyWise (Mise à jour des rôles)
1. Acteurs et rôles
   • 	Utilisateur non authentifié
   • 	Patient
   • 	Médecin
   • 	ADMIN (médecin doté du rôle ADMIN)
   Chaque utilisateur peut porter un seul rôle parmi PATIENT ou MEDECIN.
   Le rôle ADMIN ne peut être attribué qu’à un utilisateur déjà médecin.

2. Inscription et authentification
   • 	En tant qu’utilisateur non authentifié,
   je veux m’inscrire en précisant nom, prénom, date de naissance, email et mot de passe,
   afin de créer un compte InfyWise avec un rôle initial PATIENT ou MEDECIN.
   • 	En tant qu’utilisateur
   En tant qu’utilisateur non authentifié,
   je veux m’inscrire en choisissant nom, prénom, date de naissance, email, mot de passe et rôle unique ( ou ),
   afin d’accéder à InfyWise.
   • 	En tant qu’utilisateur,
   je veux me connecter (login) et me déconnecter (logout),
   afin de sécuriser l’accès à mon compte.
   • 	En tant qu’utilisateur authentifié,
   je veux consulter et mettre à jour mon profil,
   afin de maintenir mes informations personnelles à jour.
2. Gestion des rôles
   • 	En tant qu’utilisateur lors de l’inscription,
   je dois sélectionner un rôle unique :  ou .
   Un même compte ne peut pas cumuler patient et médecin.
   • 	En tant que médecin,
   je peux demander le rôle ,
   uniquement si je suis déjà médecin et que j’ai au moins une spécialité validée.
   • 	En tant qu’ADMIN,
   je veux valider ou rejeter les pathologies et témoignages soumis,
   afin de garantir la qualité et la cohérence du contenu.
3. Spécialités
   • 	En tant que médecin,
   je veux lister les spécialités validées,
   afin de choisir celles qui correspondent à mes compétences.
   • 	En tant que médecin,
   je veux proposer une nouvelle spécialité (statut ),
   afin d’enrichir le référentiel d’InfyWise.
   • 	En tant qu’ADMIN,
   je veux valider ou rejeter une spécialité proposée,
   afin de maintenir la fiabilité du référentiel.
4. Pathologies, causes & effets
   • 	En tant que médecin,
   je veux créer une pathologie (nom, description, spécialité),
   afin de documenter une nouvelle problématique d’infertilité.
   • 	En tant que médecin,
   je veux ajouter des causes et des effets à une pathologie,
   afin d’en préciser les facteurs et les conséquences.
   • 	En tant que patient,
   je veux lister les pathologies validées avec leurs causes et effets,
   afin de m’informer sur les différentes prises en charge.
   • 	En tant qu’ADMIN,
   je veux modérer uniquement les pathologies en attente liées à mes spécialités,
   afin de garantir leur fiabilité avant publication.
5. Témoignages
   • 	En tant que patient,
   je veux soumettre un témoignage libre sur mon parcours,
   afin de partager mon expérience.
   • 	En tant qu’utilisateur,
   je veux consulter les témoignages validés,
   afin de bénéficier de retours d’expérience fiables.
   • 	En tant qu’ADMIN,
   je veux modérer uniquement les témoignages en attente liés à mes spécialités,
   afin de garantir la pertinence des contenus.
6. Rendez-vous
   • 	En tant que patient,
   je veux prendre, modifier ou annuler mes propres rendez-vous,
   afin de gérer mon suivi médical de manière autonome.
   • 	En tant que médecin,
   je veux consulter et confirmer ou refuser les demandes de rendez-vous,
   afin d’organiser mon planning.
   • 	En tant que patient,
   je veux recevoir une notification lorsque mon rendez-vous est confirmé,
   afin de planifier ma venue.

Diagramme Entité-Relation
- En tant qu’utilisateur non authentifié,
  je veux m’inscrire en choisissant nom, prénom, date de naissance, email, mot de passe et rôle unique (PATIENT ou MEDECIN),
  afin d’accéder à InfyWise.
- En tant qu’utilisateur,
  je veux me connecter (login) et me déconnecter (logout),
  afin de sécuriser l’accès à mon compte.
- En tant qu’utilisateur authentifié,
  je veux consulter et mettre à jour mon profil,
  afin de maintenir mes informations personnelles à jour.
2. Gestion des rôles
- En tant qu’utilisateur lors de l’inscription,
  je dois sélectionner un rôle unique : PATIENT ou MEDECIN.
  Un même compte ne peut pas cumuler patient et médecin.
- En tant que médecin,
  je peux demander le rôle ADMIN,
  uniquement si je suis déjà médecin et que j’ai au moins une spécialité validée.
- En tant qu’ADMIN,
  je veux valider ou rejeter les pathologies et témoignages soumis,
  afin de garantir la qualité et la cohérence du contenu.
3. Spécialités
- En tant que médecin,
  je veux lister les spécialités validées,
  afin de choisir celles qui correspondent à mes compétences.
- En tant que médecin,
  je veux proposer une nouvelle spécialité (statut PENDING),
  afin d’enrichir le référentiel d’InfyWise.
- En tant qu’ADMIN,
  je veux valider ou rejeter une spécialité proposée,
  afin de maintenir la fiabilité du référentiel.
4. Pathologies, causes & effets
- En tant que médecin,
  je veux créer une pathologie (nom, description, spécialité),
  afin de documenter une nouvelle problématique d’infertilité.
- En tant que médecin,
  je veux ajouter des causes et des effets à une pathologie,
  afin d’en préciser les facteurs et les conséquences.
- En tant que patient,
  je veux lister les pathologies validées avec leurs causes et effets,
  afin de m’informer sur les différentes prises en charge.
- En tant qu’ADMIN,
  je veux modérer uniquement les pathologies en attente liées à mes spécialités,
  afin de garantir leur fiabilité avant publication.
5. Témoignages
- En tant que patient,
  je veux soumettre un témoignage libre sur mon parcours,
  afin de partager mon expérience.
- En tant qu’utilisateur,
  je veux consulter les témoignages validés,
  afin de bénéficier de retours d’expérience fiables.
- En tant qu’ADMIN,
  je veux modérer uniquement les témoignages en attente liés à mes spécialités,
  afin de garantir la pertinence des contenus.
6. Rendez-vous
- En tant que patient,
  je veux prendre, modifier ou annuler mes propres rendez-vous,
  afin de gérer mon suivi médical de manière autonome.
- En tant que médecin,
  je veux consulter et confirmer ou refuser les demandes de rendez-vous,
  afin d’organiser mon planning.
- En tant que patient,
  
- je veux recevoir une notification lorsque mon rendez-vous est confirmé,
  

```mermaid
  erDiagram
  USERS {
  int id PK
  string first_name
  string last_name
  date birth_date
  string email
  string password_hash
  enum role "PATIENT, MEDECIN, ADMIN"
  datetime created_at
  datetime updated_at
  }

  SPECIALITES {
  int id PK
  string name
  }

  USER_SPECIALITES {
  int user_id FK
  int specialite_id FK
  }

  CATEGORIES {
  int id PK
  string name
  }

  PATHOLOGIES {
  int id PK
  string name
  text description
  enum status "PENDING, VALIDATED, REJECTED"
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
  int pathologie_id FK
  int category_id FK
  }

  TEMOIGNAGES {
  int id PK
  int user_id FK
  text content
  datetime submitted_at
  enum status "PENDING, VALIDATED, REJECTED"
  }

  TEMOIGNAGE_CATEGORIES {
  int temoignage_id FK
  int category_id FK
  }

  RENDEZ_VOUS {
  int id PK
  int patient_id FK
  int medecin_id FK
  datetime appointment_datetime
  enum status "PENDING, CONFIRMED, CANCELLED"
  text commentaire
  }

  USERS ||--o{ USER_SPECIALITES : specializes_in
  SPECIALITES ||--o{ USER_SPECIALITES : assigned_to

  SPECIALITES ||--o{ PATHOLOGIES : contains
  PATHOLOGIES ||--o{ PATHOLOGIE_CAUSES : has_causes
  PATHOLOGIES ||--o{ PATHOLOGIE_EFFETS : has_effects
  PATHOLOGIES ||--o{ PATHOLOGIE_CATEGORIES : categorized_in
  CATEGORIES ||--o{ PATHOLOGIE_CATEGORIES : applies_to

  USERS ||--o{ TEMOIGNAGES : writes
  TEMOIGNAGES ||--o{ TEMOIGNAGE_CATEGORIES : categorized_in
  CATEGORIES ||--o{ TEMOIGNAGE_CATEGORIES : applies_to

  USERS ||--o{ RENDEZ_VOUS : requests_appointments_as_patient
  USERS ||--o{ RENDEZ_VOUS : manages_appointments_as_medecin
  fin de planifier ma venue.
- 
