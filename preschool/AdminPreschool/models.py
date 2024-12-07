from django.db import models

# Create your models here.

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



