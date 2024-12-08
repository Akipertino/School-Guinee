from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

<<<<<<< HEAD
=======
# Create your models here.

from django.contrib.auth.models import AbstractUser,User

>>>>>>> 2890c5a866a1afe2e91940b793a462eee24fe025
class Utilisateur(AbstractUser):
    # Ajoutez ici des champs supplémentaires si nécessaire
    pass
# Modèle pour les cours

# Modèle pour les enseignants
class Enseignant(models.Model):
    id_enseignant = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=30)
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE)  # Utilisation de chaîne de caractères pour éviter l'importation circulaire
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=15)
    date_entree = models.DateField()
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    nom_utilisateur = models.CharField(max_length=100)
    email = models.EmailField()
    mot_de_passe = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

<<<<<<< HEAD
=======


class InscriptionEnseignant(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    matricule = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.username} ({self.matricule})"

    class Meta:
        verbose_name = "enseignant"
        verbose_name_plural = "enseignant"


class InscriptionEleve(models.Model):
    matricule = models.CharField(max_length=100, unique=True, verbose_name="Matricule")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    
>>>>>>> 2890c5a866a1afe2e91940b793a462eee24fe025
    def __str__(self):
        return self.nom

class Cour(models.Model):
    identifiant = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=100, help_text="Nom du cours")
    description = models.TextField(blank=True, help_text="Description du cours")
    
    # Utilisation de settings.AUTH_USER_MODEL pour pointer vers le modèle utilisateur personnalisé
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    def clean(self):
        if not self.nom:
            raise ValidationError("Le nom du cours est requis.")
        if not self.identifiant:
            raise ValidationError("L'identifiant du cours est requis.")


# Modèle pour les horaires des cours
class Horaire(models.Model):
    cours = models.ForeignKey(Cour, on_delete=models.CASCADE, related_name='horaires')
    jour = models.CharField(
        max_length=9,
        choices=[
            ('lundi', 'Lundi'), ('mardi', 'Mardi'), ('mercredi', 'Mercredi'),
            ('jeudi', 'Jeudi'), ('vendredi', 'Vendredi'), ('samedi', 'Samedi'), ('dimanche', 'Dimanche')
        ]
    )
    heure_debut = models.TimeField(help_text="Heure de début du cours")
    heure_fin = models.TimeField(help_text="Heure de fin du cours")

    def __str__(self):
        return f"{self.cours.nom} - {self.jour} ({self.heure_debut} - {self.heure_fin})"

    def clean(self):
        if self.heure_debut >= self.heure_fin:
            raise ValidationError("L'heure de fin doit être après l'heure de début.")


# Modèle pour les élèves
class Eleve(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=50, unique=True)
    genre = models.CharField(max_length=20)
    date_naissance = models.DateField()
    classe = models.CharField(max_length=100)
    religion = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photo_eleves/', blank=True, null=True)

    nom_pere = models.CharField(max_length=100)
    profession_pere = models.CharField(max_length=100)
    telephone_pere = models.CharField(max_length=15)
    email_pere = models.EmailField(blank=True, null=True)

    nom_mere = models.CharField(max_length=100)
    profession_mere = models.CharField(max_length=100)
    telephone_mere = models.CharField(max_length=15)
    email_mere = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"


# Modèle pour les niveaux de classe
class NiveauClasse(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


# Modèle pour les matières
class Matiere(models.Model):
    id_matiere = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    classe = models.ForeignKey(NiveauClasse, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

<<<<<<< HEAD

=======
class Enseignant(models.Model):
    id_enseignant = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=30) #(max_length=10, choices=[('Homme', 'Homme'), ('Femme', 'Femme'), ('Autres', 'Autres')])
    matiere = models.ForeignKey(Matiere, on_delete = models.CASCADE)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=15)
    date_entree = models.DateField()
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"
>>>>>>> 2890c5a866a1afe2e91940b793a462eee24fe025



# Modèle pour les départements
class Departement(models.Model):
    id_departement = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)
    date_debut = models.DateField()
    nombre_etudiant = models.PositiveIntegerField()

    def __str__(self):
        return self.nom


# Modèle pour les rôles d'utilisateur
class Role(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom
