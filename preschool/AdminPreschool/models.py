from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

import datetime
from django.db import models
from django.core.exceptions import ValidationError

import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.contrib.auth.models import User
import secrets
import logging

logger = logging.getLogger(__name__)

class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('enseignant', 'Enseignant'),
        ('eleve', 'Élève'),
        ('comptable', 'Comptable'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    matricule = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.username

class Niveau(models.Model):
    nom = models.CharField(max_length=50, unique=True)  # Exemple : "Terminale", "CM2", etc.
    description = models.TextField(blank=True, null=True)  # Description optionnelle

    def __str__(self):
        return self.nom       

class Classe(models.Model):
    nom = models.CharField(max_length=30)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    capacite = models.IntegerField()

    def __str__(self):
        return f'{self.niveau} {self.nom}'

class Matiere(models.Model):
    id_matiere = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=50)
    coefficient = models.PositiveIntegerField(default=1)  # Coefficient par défaut à 1
    niveau = models.ManyToManyField(Niveau, related_name='matiere')

    def __str__(self):
        return self.nom

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    genre = models.CharField(max_length=10, choices=[('Homme', 'Homme'), ('Femme', 'Femme'), ('Autres', 'Autres')])
    matiere = models.ManyToManyField(Matiere, through='EnseignantMatiere', related_name='enseignant')
    classes = models.ManyToManyField(Classe, through='EnseignantClasse', related_name="enseignant")
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=15)
    date_entree = models.DateField()
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    matricule = models.CharField(max_length=50, unique=True, blank=True, null=True)
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name="enseignant", null=True, blank=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        # Générer un matricule si ce n'est pas déjà fait
        if not self.matricule:
            self.matricule = self.generer_matricule()

        # Vérifier si un utilisateur associé existe déjà
        if not self.utilisateur:
            # Créer un utilisateur avec le rôle "enseignant"
            mot_de_passe = secrets.token_urlsafe(8)  # Générer un mot de passe aléatoire
            utilisateur = Utilisateur.objects.create_user(
                username=self.matricule,  # Utilisez le matricule comme nom d'utilisateur
                password=mot_de_passe,
                email=self.email,
                role="enseignant",
                matricule=self.matricule
            )
            self.utilisateur = utilisateur  # Associer l'utilisateur à l'enseignant

            # Envoyer un email avec les identifiants de connexion
            self.envoyer_email_identifiants(self.matricule, mot_de_passe)

        super().save(*args, **kwargs)

    def generer_matricule(self):
        # Récupérer l'année en cours (les deux derniers chiffres)
        annee = datetime.datetime.now().strftime('%y')

        # Récupérer le dernier matricule pour les enseignants
        dernier_enseignant = Enseignant.objects.order_by('-matricule').first()

        if dernier_enseignant and dernier_enseignant.matricule:
            # Extraire le numéro séquentiel du dernier matricule
            dernier_matricule = dernier_enseignant.matricule
            try:
                numero_sequentiel = int(dernier_matricule[-3:]) + 1
            except (ValueError, IndexError):
                numero_sequentiel = 1
        else:
            numero_sequentiel = 1

        # Formater le numéro séquentiel sur 3 chiffres
        numero_sequentiel_formatte = f"{numero_sequentiel:03d}"

        # Générer le matricule complet
        matricule = f"ENS{annee}{numero_sequentiel_formatte}"  # Exemple : ENS23001
        return matricule

    def envoyer_email_identifiants(self, username, mot_de_passe):
        sujet = "Vos identifiants de connexion"
        message = f"""
        Bonjour {self.nom},

        Votre compte enseignant a été créé avec succès.

        Nom d'utilisateur : {username}
        Mot de passe : {mot_de_passe}

        Vous pouvez vous connecter à votre compte en utilisant ces informations.

        Cordialement,
        L'équipe de l'école, School-Guinée
        """
        expediteur = "fkipertino@gmail.com"  # Adresse email de l'expéditeur
        destinataire = self.email  # Adresse email de l'enseignant

        send_mail(
            subject=sujet,
            message=message,
            from_email=expediteur,
            recipient_list=[destinataire],
            fail_silently=False,
        )

class EnseignantClasse(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('enseignant', 'classe')

class EnseignantMatiere(models.Model):
    enseignant = models.ForeignKey(Enseignant , on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('enseignant', 'matiere')

class InscriptionEleve(models.Model):
    matricule = models.CharField(max_length=100, unique=True, verbose_name="Matricule")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    
    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"

    class Meta:
        verbose_name = "Élève"
        verbose_name_plural = "Élèves"

class Eleve(models.Model):

    GENRE_CHOICES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Autres', 'Autres'),
    ]

    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=50, unique=True, blank=True, null=True)
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default='Autres')
    date_naissance = models.DateField()
    religion = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photo_eleves/', blank=True, null=True)
    utilisateur = models.OneToOneField('Utilisateur', on_delete=models.CASCADE, related_name="eleve", null=True, blank=True)

    # Informations des parents
    nom_pere = models.CharField(max_length=100, verbose_name="Nom du père")
    profession_pere = models.CharField(max_length=100, verbose_name="Profession du père")
    telephone_pere = models.CharField(max_length=15, verbose_name="Téléphone du père")
    email_pere = models.EmailField(blank=True, null=True, verbose_name="Email du père")

    nom_mere = models.CharField(max_length=100, verbose_name="Nom de la mère")
    profession_mere = models.CharField(max_length=100, verbose_name="Profession de la mère")
    telephone_mere = models.CharField(max_length=15, verbose_name="Téléphone de la mère")
    email_mere = models.EmailField(blank=True, null=True, verbose_name="Email de la mère")

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"

    def save(self, *args, **kwargs):
        # Si le matricule n'est pas défini, générer un nouveau matricule
        if not self.matricule:
            self.matricule = self.generer_matricule()
        
        # Si l'élève est créé et qu'il n'a pas encore d'utilisateur associé
        if not self.utilisateur:
            # Création d'un utilisateur avec un nom d'utilisateur basé sur le matricule
            username = self.matricule  # Par exemple, le matricule devient le nom d'utilisateur
            password = secrets.token_urlsafe(8)  # Générer un mot de passe aléatoire de 10 caractères

            # Création de l'utilisateur
            utilisateur = Utilisateur.objects.create_user(
                username=username,
                password=password,
                email=self.email_pere or self.email_mere,  # Utilise l'email des parents s'il est disponible
                role="eleve",
                matricule=self.matricule  # Assigner le matricule de l'élève à l'utilisateur
            )

            # Associe l'utilisateur à l'élève
            self.utilisateur = utilisateur

            # Envoi de l'email avec le mot de passe
            self.envoyer_email_mot_de_passe(password)

        super().save(*args, **kwargs)

    def generer_matricule(self):
        # Récupérer l'année en cours (les deux derniers chiffres)
        annee = datetime.datetime.now().strftime('%y')
        
        # Récupérer le code de la classe (par exemple, "CM1" -> "CM1")
        code_classe = self.classe.nom
        
        # Récupérer le dernier matricule pour cette classe
        dernier_eleve = Eleve.objects.filter(classe=self.classe).order_by('-matricule').first()
        
        if dernier_eleve:
            # Extraire le numéro séquentiel du dernier matricule
            dernier_matricule = dernier_eleve.matricule
            try:
                # Tenter de convertir les 3 derniers chiffres en entier
                numero_sequentiel = int(dernier_matricule[-3:]) + 1
            except ValueError:
                # Si la conversion échoue, initialiser le numéro séquentiel à 1
                numero_sequentiel = 1
        else:
            # Si c'est le premier élève de la classe, commencer à 1
            numero_sequentiel = 1
        
        # Formater le numéro séquentiel sur 3 chiffres
        numero_sequentiel_formatte = f"{numero_sequentiel:03d}"
        
        # Générer le matricule complet
        matricule = f"{annee}{code_classe}{numero_sequentiel_formatte}"
        return matricule
        
    def clean(self):
        # Vérifier que le matricule est unique
        if self.matricule and Eleve.objects.filter(matricule=self.matricule).exclude(id=self.id).exists():
            raise ValidationError("Ce matricule est déjà utilisé.")

    def calculer_moyenne(self):
        notes = self.notes.all()  # Récupère toutes les notes de l'élève
        if notes.exists():
            total_points = 0
            total_coefficients = 0

            for note in notes:
                total_points += note.note * note.matiere.coefficient  # Note pondérée par le coefficient
                total_coefficients += note.matiere.coefficient  # Somme des coefficients

            if total_coefficients > 0:
                return round(total_points / total_coefficients, 2)  # Moyenne pondérée arrondie à 2 décimales
            else:
                return None
        return None

    def calculer_moyenne_par_matiere(self, matiere):
        notes = self.notes.filter(matiere=matiere)  # Récupère les notes pour la matière spécifiée
        if notes.exists():
            total_points = sum(note.note * note.matiere.coefficient for note in notes)
            total_coefficients = sum(note.matiere.coefficient for note in notes)
            if total_coefficients > 0:
                return round(total_points / total_coefficients, 2)
        return None

    def envoyer_email_mot_de_passe(self, mot_de_passe):
        sujet = "Votre compte élève"
        message = f"""
        Bonjour {self.prenom},

        Votre compte a été créé avec succès.

        Nom d'utilisateur : {self.matricule}
        Mot de passe : {mot_de_passe}

        Vous pouvez vous connecter à votre compte en utilisant ces informations.

        Cordialement,
        L'équipe de l'école, School-Guinée
        """
        expediteur = "fkipertino@gmail.com"  # Adresse email de l'expéditeur
        destinataire = self.email_pere or self.email_mere  # Adresse email de l'élève ou des parents

        send_mail(
            subject=sujet,
            message=message,
            from_email=expediteur,
            recipient_list=[destinataire],
            fail_silently=False,
        )

class Cour(models.Model):
    nom = models.CharField(blank=False, null=False, max_length=300)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='cours')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='cours')
    classe = models.ManyToManyField(Classe, related_name='cours')  # ManyToManyField pour les classes
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        classes = ", ".join([classe.nom for classe in self.classe.all()])  # Itérer sur les classes
        return f"{self.nom} (Enseignant: {self.enseignant.nom}, Classes: {classes}, Début: {self.date_debut.strftime('%d/%m/%Y %H:%M')})"

class Note(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='notes')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='notes')
    enseignant = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, blank=True, related_name='notes')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='notes')
    note = models.DecimalField(max_digits=5, decimal_places=2)
    date_saisie = models.DateField(auto_now_add=True)
    commentaire = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.eleve} - {self.matiere} : {self.note}"