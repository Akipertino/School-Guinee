from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('enseignant', 'Enseignant'),
        ('eleve', 'Élève'),
        ('comptable', 'Comptable'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    identifiant_unique = models.CharField(max_length=50, unique=True, blank=True, null=True)

    
    
    # Vérification de l'identifiant pour les élèves uniquement
    def save(self, *args, **kwargs):
        if self.role == 'eleve' and not self.identifiant_unique:
            raise ValueError("Un élève doit avoir un identifiant unique.")
        super().save(*args, **kwargs)



class InscriptionEleve(models.Model):
    matricule = models.CharField(max_length=100, unique=True, verbose_name="Matricule")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    
    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"

    class Meta:
        verbose_name = "Élève"
        verbose_name_plural = "Élèves"



# class InscriptionEleve(models.Model):
#     utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, related_name="inscription", verbose_name="Utilisateur associé")
#     eleve = models.OneToOneField(Eleve, on_delete=models.CASCADE, related_name="inscription", verbose_name="Élève")
#     date_inscription = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")
#     est_actif = models.BooleanField(default=True, verbose_name="Inscription active")

#     def __str__(self):
#         return f"{self.utilisateur.username} - {self.eleve.matricule}"

#     class Meta:
#         verbose_name = "Inscription d'élève"
#         verbose_name_plural = "Inscriptions d'élèves"



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

# Niveau de classe
class NiveauClasse(models.Model):
    nom = models.CharField(max_length=50, unique=True)  # Exemple : "Terminale", "CM2", etc.
    description = models.TextField(blank=True, null=True)  # Description optionnelle

    def __str__(self):
        return self.nom
        
class Matiere(models.Model):
    id_matiere = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    classe = models.ForeignKey(NiveauClasse, on_delete = models.CASCADE)

    def __str__(self):
        return self.nom

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
    nom_utilisateur = models.CharField(max_length=100)
    email = models.EmailField()
    mot_de_passe = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Departement(models.Model):
    id_departement = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)
    date_debut = models.DateField()
    nombre_etudiant = models.IntegerField()

    def __str__(self):
        return self.nom

# Type d'utilisateur
class Role(models.Model):
    nom = models.CharField(max_length=50, unique=True)  # Exemple : "Élève", "Enseignant", "Administrateur"

    def __str__(self):
        return self.nom



