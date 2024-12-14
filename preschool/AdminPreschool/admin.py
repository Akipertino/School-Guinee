from django.contrib import admin

# Register your models here.
from .models import Eleve, Enseignant, Matiere, Departement, NiveauClasse, Utilisateur, InscriptionEleve



admin.site.register(Eleve)
admin.site.register(Enseignant)
admin.site.register(Matiere)
admin.site.register(Departement)
admin.site.register(NiveauClasse)
admin.site.register(InscriptionEleve)
admin.site.register(Utilisateur)