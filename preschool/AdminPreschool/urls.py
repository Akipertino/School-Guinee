from django.urls import path
<<<<<<< HEAD
from .views import accueil, static_page, ajouter_eleve, inscription_eleve, modification_eleve, details_eleve, modifier_eleve, liste_eleves, ajouter_departement, ajouter_matiere, ajouter_enseignant, liste_enseignants,ajouter_cour
=======
from .views import accueil, static_page, ajouter_eleve, inscription_eleve, modification_eleve, details_eleve, modifier_eleve, liste_eleves, ajouter_departement, ajouter_matiere, ajouter_enseignant, liste_enseignants,inscription_enseignant
>>>>>>> 2890c5a866a1afe2e91940b793a462eee24fe025
 
urlpatterns = [
	path('', accueil, name="accueil"),
	path('<str:page_name>/', static_page, name='static_page'),
	path('ajouter_eleve', ajouter_eleve, name='ajouter_eleve'),
	path('ajouter_enseignant', ajouter_enseignant, name='ajouter_enseignant'),
	path('liste_enseignants', liste_enseignants, name='liste_enseignants'),
	path('ajouter_matiere', ajouter_matiere, name="ajouter_matiere"),
	path('ajouter_departement', ajouter_departement, name="ajouter_departement"),
	path('liste_eleves', liste_eleves, name="liste_eleves"),
	path('details_eleve', details_eleve, name="details_eleve"),
	path('modification_eleve/<int:eleve_id>/', modification_eleve, name='modification_eleve'),
	path('inscription_eleve', inscription_eleve, name="inscription_eleve"),
	path('ajouter_cour', ajouter_cour, name="ajouter_cour"),
 
	# path('modifier_eleve', modifier_eleve, name="modifier_eleve"),
<<<<<<< HEAD
  # path('ajouter_matiere/', views.ajouter_matiere, name='ajouter_matiere'),
=======
	path('inscription_enseignant', inscription_enseignant, name="inscription_enseignant"),
>>>>>>> 2890c5a866a1afe2e91940b793a462eee24fe025
]