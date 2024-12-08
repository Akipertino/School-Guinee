from django.contrib import admin
from .models import Eleve, Enseignant, Matiere, Departement, NiveauClasse, Cour, Horaire, Role

# Configuration de l'administration pour le modèle Eleve
@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'matricule', 'classe', 'genre', 'date_naissance')
    search_fields = ('prenom', 'nom', 'matricule', 'classe')
    list_filter = ('genre', 'classe', 'religion')
    ordering = ('nom', 'prenom')


# Configuration de l'administration pour le modèle Enseignant
@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('id_enseignant', 'nom', 'matiere', 'telephone', 'date_entree', 'qualification')
    search_fields = ('nom', 'id_enseignant', 'telephone')
    list_filter = ('matiere', 'qualification', 'experience')
    ordering = ('nom',)


# Configuration de l'administration pour le modèle Matiere
@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('id_matiere', 'nom', 'classe')
    search_fields = ('id_matiere', 'nom')
    list_filter = ('classe',)
    ordering = ('nom',)


# Configuration de l'administration pour le modèle Departement
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('id_departement', 'nom', 'responsable', 'date_debut', 'nombre_etudiant')
    search_fields = ('id_departement', 'nom', 'responsable')
    list_filter = ('date_debut',)
    ordering = ('nom',)


# Configuration de l'administration pour le modèle NiveauClasse
@admin.register(NiveauClasse)
class NiveauClasseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)
    ordering = ('nom',)


# Configuration de l'administration pour le modèle Cour
@admin.register(Cour)
class CourAdmin(admin.ModelAdmin):
    list_display = ('identifiant', 'nom', 'enseignant', 'date_creation')
    search_fields = ('identifiant', 'nom', 'enseignant__username')
    list_filter = ('enseignant', 'date_creation')
    ordering = ('nom',)


# Configuration de l'administration pour le modèle Horaire
@admin.register(Horaire)
class HoraireAdmin(admin.ModelAdmin):
    list_display = ('cours', 'jour', 'heure_debut', 'heure_fin')
    search_fields = ('cours__nom', 'jour')
    list_filter = ('jour',)
    ordering = ('cours', 'jour', 'heure_debut')


# Configuration de l'administration pour le modèle Role
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)
    ordering = ('nom',)
