from django.contrib import admin


# Register your models here.

from .models import Eleve, Enseignant, Matiere, Niveau, Utilisateur, InscriptionEleve, Classe, Cour



admin.site.register(Eleve)

class AdminClasse(admin.ModelAdmin):
    list_display = ['nom', 'niveau']

admin.site.register(Classe, AdminClasse)
class AdminEnseignant(admin.ModelAdmin):
    list_display = ['nom', 'email', 'telephone','adresse']

admin.site.register(Enseignant, AdminEnseignant)

class CourAdmin(admin.ModelAdmin):
    # Champs à afficher dans la liste des cours
    list_display = ('nom', 'enseignant', 'matiere', 'afficher_classes', 'date_debut', 'date_fin')

    # Filtres disponibles dans la barre latérale
    list_filter = ('enseignant', 'matiere', 'date_debut')

    # Champs de recherche
    search_fields = ('nom', 'enseignant__nom', 'matiere__nom', 'description')

    # Champs regroupés dans le formulaire d'édition
    fieldsets = (
        ('Informations générales', {
            'fields': ('nom', 'enseignant', 'matiere', 'classe', 'date_debut', 'date_fin', 'description')
        }),
    )

    # Fonction pour afficher les classes dans la liste des cours
    def afficher_classes(self, obj):
        return ", ".join([classe.nom for classe in obj.classe.all()])  # Itérer sur les classes
    afficher_classes.short_description = 'Classes'

# Enregistrement du modèle Cour avec la personnalisation
admin.site.register(Cour, CourAdmin)

# @admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('id_matiere', 'nom', 'get_niveaux')  # Affiche les classes associées

    def get_niveaux(self, obj):
        return ", ".join([niveau.nom for niveau in obj.niveau.all()])
    get_niveaux.short_description = 'Niveau associées'

admin.site.register(Matiere, MatiereAdmin)

admin.site.register(Niveau)

admin.site.register(InscriptionEleve)

admin.site.register(Utilisateur)