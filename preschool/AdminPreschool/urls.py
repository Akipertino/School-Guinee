from django.urls import path
from .views import *
 
urlpatterns = [
	path('', accueil, name="accueil"),
	    # Connexion et déconnexion
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('deconnexion/', deconnexion, name='deconnexion'),

	# Saisie de notes
    path('saisie_notes/', saisie_notes, name='saisie_notes'),
	# Filtrer les notes (pour AJAX)
    path('filtrer_notes/', filtrer_notes, name='filtrer_notes'),
    # Tableaux de bord
	path('mes-cours/', mes_cours, name='mes_cours'),
	path('eleve/tableau-de-bord/', tableau_de_bord_eleve, name='tableau_de_bord_eleve'),

    # path('eleve/tableau-de-bord/', student_dashboard, name='student_dashboard'),
    path('enseignant/tableau-de-bord/', tableau_de_bord_enseignant, name='tableau_de_bord_enseignant'),
    path('admin/tableau-de-bord/', admin_dashboard, name='admin_dashboard'),
    path('comptable/tableau-de-bord/', accountant_dashboard, name='accountant_dashboard'),
	path('enseignant/ajout/', ajouter_un_enseignant, name='ajouter_un_enseignant'),
	path('enseignant/liste/', liste_des_enseignants, name='liste_des_enseignants'),
	path('eleve/ajout/', ajouter_un_eleve, name='ajouter_un_eleve'),
	path('accueil/apropos/', a_propos, name='a_propos'),
	path('accueil/nous-contacter/', nous_contacter, name='nous_contacter'),
	
	path('get_eleves_par_niveau_et_sexe/', get_eleves_par_niveau_et_sexe, name='get_eleves_par_niveau_et_sexe'),
	path('get_student_data/', get_student_data, name='get_student_data'),
	path('<str:page_name>/', static_page, name='static_page'),
	# path('ajouter_eleve', ajouter_eleve, name='ajouter_eleve'),
	# path('ajouter_enseignant', ajouter_enseignant, name='ajouter_enseignant'),
	# path('liste_enseignants', liste_enseignants, name='liste_enseignants'),
	path('ajouter_matiere', ajouter_matiere, name="ajouter_matiere"),
	path('liste_eleves', liste_eleves, name="liste_eleves"),
	path('details_eleve', details_eleve, name="details_eleve"),
	# path('connexion', connexion, name="connexion"),
	# path('modification_eleve/<int:eleve_id>/', modification_eleve, name='modification_eleve'),
	# path('inscription_eleve', inscription_eleve, name="inscription_eleve"),
	path('student_dashboard', student_dashboard, name="student_dashboard"),
	path('teacher_dashboard', teacher_dashboard, name="teacher_dashboard"),
	path('admin_dashboard', admin_dashboard, name="admin_dashboard"),
	# path('accountant_dashboard', admin_dashboard, name="accountant_dashboard"),
	# path('deconnexion', deconnexion, name="deconnexion")
	# path('modifier_eleve', modifier_eleve, name="modifier_eleve"),
] 