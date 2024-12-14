from django.urls import path
from .views import *
 
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
	path('connexion', connexion, name="connexion"),
	path('modification_eleve/<int:eleve_id>/', modification_eleve, name='modification_eleve'),
	path('inscription_eleve', inscription_eleve, name="inscription_eleve"),
	path('student_dashboard', student_dashboard, name="student_dashboard"),
	path('teacher_dashboard', teacher_dashboard, name="teacher_dashboard"),
	path('admin_dashboard', admin_dashboard, name="admin_dashboard"),
	path('accountant_dashboard', admin_dashboard, name="accountant_dashboard"),
	path('deconnexion', deconnexion, name="deconnexion")
	# path('modifier_eleve', modifier_eleve, name="modifier_eleve"),
] 