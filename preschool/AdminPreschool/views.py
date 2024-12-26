
from django.shortcuts import render, redirect
# from .forms import EleveForm, EnseignantForm
from .models import Eleve, Enseignant, Matiere, Utilisateur, Niveau, Classe
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

from django.http import JsonResponse
from .models import Eleve, Classe
import secrets

from django.db import IntegrityError

import secrets
from django.shortcuts import render, redirect
from .models import Utilisateur, Eleve, Classe

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Enseignant, Matiere, Classe
from .models import EnseignantMatiere, EnseignantClasse


def liste_des_enseignants(request):
    # Récupérer tous les enseignants
    enseignants = Enseignant.objects.all()
    return render(request, 'preschool/html-template/liste_des_enseignants.html', {'enseignants': enseignants})

from django.db import IntegrityError
from django.core.exceptions import ValidationError

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Enseignant, Matiere, Classe



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Eleve, Matiere, Note, Enseignant, Classe

# def tableau_de_bord_enseignant(request):
#     # Récupérer l'enseignant connecté
#     enseignant = request.user.enseignant  # Assurez-vous que l'utilisateur est un enseignant

#     # Récupérer les classes de l'enseignant
#     classes = enseignant.classes.all()

#     # Récupérer les élèves de ces classes
#     eleves = Eleve.objects.filter(classe__in=classes)

#     # Récupérer les matières enseignées par l'enseignant
#     matieres = enseignant.matiere.all()

#     # Si la requête est POST, c'est une demande de saisie de note
#     if request.method == 'POST':
#         eleve_id = request.POST.get('eleve')
#         matiere_id = request.POST.get('matiere')
#         note_value = request.POST.get('note')
#         commentaire = request.POST.get('commentaire')

#         # Vérifier que les données sont valides
#         if not eleve_id or not matiere_id or not note_value:
#             messages.error(request, "Veuillez remplir tous les champs obligatoires.")
#             return redirect('tableau_de_bord_enseignant')

#         # Récupérer les objets correspondants
#         eleve = get_object_or_404(Eleve, id=eleve_id)
#         matiere = get_object_or_404(Matiere, id=matiere_id)

#         # Créer la note
#         note = Note.objects.create(
#             eleve=eleve,
#             matiere=matiere,
#             enseignant=enseignant,  # L'enseignant connecté
#             classe=eleve.classe,  # La classe de l'élève
#             note=note_value,
#             commentaire=commentaire,
#         )
#         messages.success(request, "La note a été ajoutée avec succès.")
#         return redirect('tableau_de_bord_enseignant')

#     # Passer les données au template
#     context = {
#         'enseignant': enseignant,
#         'classes': classes,
#         'eleves': eleves,
#         'matieres': matieres,
#         'notes': Note.objects.filter(enseignant=enseignant),  # Notes saisies par l'enseignant
#     }
#     return render(request, 'preschool/html-template/tableau_de_bord_enseignant.html', context)

from django.shortcuts import render
from .models import Enseignant, Note

from django.shortcuts import render
from .models import Enseignant, Classe, Eleve, Matiere, Note



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Eleve, Matiere, Note, Enseignant


from django.http import JsonResponse
from .models import Eleve, Note
from django.http import JsonResponse
from .models import Eleve, Note, Matiere

from django.http import JsonResponse
from .models import Eleve, Note, Matiere
from django.shortcuts import render
from django.utils import timezone
from .models import Eleve


from django.shortcuts import render
from django.utils import timezone
from .models import Cour, Eleve

@login_required
def mes_cours(request):
    # Récupérer l'élève connecté
    try:
        eleve = Eleve.objects.get(utilisateur=request.user)
    except Eleve.DoesNotExist:
        return render(request, 'erreur.html', {'message': 'Vous n\'êtes pas un élève.'})

    # Récupérer la classe de l'élève
    classe = eleve.classe

    # Récupérer tous les cours de la classe
    cours = Cour.objects.filter(classe=classe).order_by('date_debut')

    # Passer les cours au template
    return render(request, 'preschool/html-template/mes_cours.html', {'cours': cours})

@login_required
def tableau_de_bord_eleve(request):
    # Récupéreraion de l'élève qui connecté
    try:
        eleve = Eleve.objects.get(utilisateur=request.user)
    except Eleve.DoesNotExist:
        return render(request, 'erreur.html', {'message': 'Vous n\'êtes pas un élève.'})

    classe = eleve.classe # Récupérer la classe de l'élève
    cours = Cour.objects.filter(classe=classe) # Récupérer tous les cours de la classe

    # Récupérer les cours d'aujourd'hui
    aujourdhui = timezone.now().date()
    cours_aujourdhui = cours.filter(date_debut__date=aujourdhui)

    # Récupérer les cours récents (7 derniers jours)
    cours_recents = cours.filter(date_debut__gte=timezone.now() - timezone.timedelta(days=7))

    # Nombre total de cours
    total_cours = cours.count()

    # Passer les données au template
    context = {
        'cours_aujourdhui': cours_aujourdhui,
        'cours_recents': cours_recents,
        'total_cours': total_cours,
    }
    return render(request, 'preschool/html-template/student-dashboard.html', context)


def filtrer_notes(request):
    # Récupérer les paramètres de la requête
    classe_id = request.GET.get('classe')

    # Récupérer les élèves de la classe sélectionnée
    eleves = Eleve.objects.filter(classe_id=classe_id)

    # Récupérer les matières enseignées dans cette classe
    matieres = Matiere.objects.filter(classe=classe_id)

    # Récupérer les notes pour chaque élève et chaque matière
    resultats = []
    for eleve in eleves:
        notes_eleve = []
        for matiere in matieres:
            notes = Note.objects.filter(eleve=eleve, matiere=matiere)
            note_semestre_1 = notes.filter(semestre=1).first()
            note_semestre_2 = notes.filter(semestre=2).first()
            note_semestre_3 = notes.filter(semestre=3).first()

            # Calculer la moyenne générale
            moyenne_generale = (
                (note_semestre_1.note if note_semestre_1 else 0) +
                (note_semestre_2.note if note_semestre_2 else 0) +
                (note_semestre_3.note if note_semestre_3 else 0)
            ) / 3 if notes.exists() else None

            # Déterminer la mention
            mention = "Excellent" if moyenne_generale >= 16 else "Très bien" if moyenne_generale >= 14 else "Bien" if moyenne_generale >= 12 else "Passable" if moyenne_generale >= 10 else "Insuffisant"

            notes_eleve.append({
                'matiere': matiere.nom,
                'note_semestre_1': note_semestre_1.note if note_semestre_1 else None,
                'note_semestre_2': note_semestre_2.note if note_semestre_2 else None,
                'note_semestre_3': note_semestre_3.note if note_semestre_3 else None,
                'moyenne_generale': round(moyenne_generale, 2) if moyenne_generale else None,
                'mention': mention if moyenne_generale else None,
            })

        resultats.append({
            'prenom': eleve.prenom,
            'nom': eleve.nom,
            'notes': notes_eleve,
        })

    return JsonResponse({'eleves': resultats})
def saisie_notes(request):
    # Récupérer l'enseignant connecté
    enseignant = request.user.enseignant

    if request.method == 'POST':
        # Récupérer les données du formulaire
        eleve_id = request.POST.get('eleve')
        matiere_id = request.POST.get('matiere')
        note_value = request.POST.get('note')

        # Vérifier que les champs obligatoires sont remplis
        if not eleve_id or not matiere_id or not note_value:
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")
            return redirect('saisie_notes')

        # Récupérer les objets correspondants
        eleve = Eleve.objects.get(id=eleve_id)
        matiere = Matiere.objects.get(id=matiere_id)

        # Créer la note
        Note.objects.create(
            eleve=eleve,
            matiere=matiere,
            enseignant=enseignant,  # L'enseignant connecté
            note=note_value,
        )

        messages.success(request, "La note a été ajoutée avec succès.")
        return redirect('saisie_notes')

    # Récupérer les élèves et les matières disponibles
    eleves = Eleve.objects.filter(classe__in=enseignant.classes.all())
    matieres = enseignant.matiere.all()

    context = {
        'eleves': eleves,
        'matieres': matieres,
    }
    return render(request, 'preschool/html-template/saisie_notes.html', context)


def tableau_de_bord_enseignant(request):
    # Récupérer l'enseignant connecté
    enseignant = request.user.enseignant  # Assurez-vous que l'utilisateur est un enseignant

    # Récupérer les classes de l'enseignant
    classes = enseignant.classes.all()

    # Récupérer les élèves dans les classes de l'enseignant
    eleves = Eleve.objects.filter(classe__in=classes)

    # Récupérer les matières enseignées par l'enseignant
    matieres = enseignant.matiere.all()

    # Récupérer les notes saisies par l'enseignant
    notes_saisies = Note.objects.filter(enseignant=enseignant).count()

    context = {
        'enseignant': enseignant,
        'classes': classes,
        'eleves': eleves,
        'matieres': matieres,
        'notes_saisies': notes_saisies,
    }
    return render(request, 'preschool/html-template/tableau_de_bord_enseignant.html', context)

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Connecter l'utilisateur
            login(request, user)

            # Rediriger vers le tableau de bord approprié en fonction du rôle
            if user.role == 'eleve':
                return redirect('tableau_de_bord_eleve')
            elif user.role == 'enseignant':
                return redirect('tableau_de_bord_enseignant')
            elif user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'comptable':
                return redirect('accountant_dashboard')
            else:
                messages.error(request, "Rôle utilisateur non reconnu.")
                return redirect('connexion')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect('connexion')

    return render(request, 'preschool/html-template/login.html')

def deconnexion(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('connexion')

def ajouter_un_enseignant(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.POST.get('nom')
        genre = request.POST.get('genre')
        date_naissance = request.POST.get('date_naissance')
        telephone = request.POST.get('telephone')
        date_entree = request.POST.get('date_entree')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        matieres = request.POST.getlist('matieres')  # Liste des matières
        classes = request.POST.getlist('classes')  # Liste des classes

        # Vérifier que les champs obligatoires sont remplis
        if not nom or not date_naissance or not telephone or not date_entree or not email:
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")
            return redirect('ajouter_un_enseignant')

        # Créer l'enseignant
        enseignant = Enseignant.objects.create(
            nom=nom,
            genre=genre,
            date_naissance=date_naissance,
            telephone=telephone,
            date_entree=date_entree,
            qualification=qualification,
            experience=experience,
            email=email,
            adresse=adresse,
            ville=ville,
        )

        # Ajouter les matières via le modèle intermédiaire
        for matiere_id in matieres:
            matiere = Matiere.objects.get(id=matiere_id)
            EnseignantMatiere.objects.create(enseignant=enseignant, matiere=matiere)

        # Ajouter les classes via le modèle intermédiaire
        for classe_id in classes:
            classe = Classe.objects.get(id=classe_id)
            EnseignantClasse.objects.create(enseignant=enseignant, classe=classe)

        messages.success(request, "L'enseignant a été ajouté avec succès.")
        return redirect('liste_des_enseignants')

    # Récupérer toutes les matières et classes disponibles
    matieres = Matiere.objects.all()
    classes = Classe.objects.all()
    return render(request, 'preschool/html-template/ajouter_un_enseignant.html', {'matieres': matieres, 'classes': classes})

def ajouter_un_eleve(request):
    if request.method == 'POST':
        try:
            # Récupérer les données du formulaire
            prenom = request.POST['prenom']
            nom = request.POST['nom']
            classe_id = request.POST['classe']
            genre = request.POST['genre']
            date_naissance = request.POST['date_naissance']
            religion = request.POST['religion']
            photo = request.FILES.get('photo')
            nom_pere = request.POST['nom_pere']
            profession_pere = request.POST['profession_pere']
            telephone_pere = request.POST['telephone_pere']
            email_pere = request.POST['email_pere']
            nom_mere = request.POST['nom_mere']
            profession_mere = request.POST['profession_mere']
            telephone_mere = request.POST['telephone_mere']
            email_mere = request.POST['email_mere']

            # Créer l'élève
            eleve = Eleve.objects.create(
                prenom=prenom,
                nom=nom,
                classe_id=classe_id,
                genre=genre,
                date_naissance=date_naissance,
                religion=religion,
                photo=photo,
                nom_pere=nom_pere,
                profession_pere=profession_pere,
                telephone_pere=telephone_pere,
                email_pere=email_pere,
                nom_mere=nom_mere,
                profession_mere=profession_mere,
                telephone_mere=telephone_mere,
                email_mere=email_mere,
            )

            # Créer un utilisateur associé à l'élève
            username = eleve.matricule  # Utilisez le matricule comme nom d'utilisateur
            password = secrets.token_urlsafe(8)  # Générer un mot de passe aléatoire de 10 caractères
            utilisateur = Utilisateur.objects.create_user(
                username=username,
                password=password,
                email=email_pere or email_mere,
                role="eleve",
                matricule=eleve.matricule  # Assigner le matricule de l'élève à l'utilisateur
            )

            # Associer l'utilisateur à l'élève
            eleve.utilisateur = utilisateur
            eleve.save()

            # Envoi de l'email avec le mot de passe
            eleve.envoyer_email_mot_de_passe(password)
            
        except IntegrityError as e:
            messages.error(request, "Le matricule généré est déjà utilisé. Veuillez réessayer.")
            return redirect('ajouter_un_eleve')

    # Récupérer toutes les classes disponibles
    classes = Classe.objects.all()
    return render(request, 'preschool/html-template/ajouter_un_eleve.html', {'classes': classes})


@login_required(redirect_field_name="redirection")
def admin_dashboard(request):
	total_eleve = Eleve.objects.count()
	total_classe = Eleve.objects.count()

	return render(request, 'preschool/html-template/index.html', {'totalEleve': total_eleve, 'totalClasse': total_classe})

def get_eleves_par_niveau_et_sexe(request):
    # Récupérer tous les niveaux
    niveaux = Niveau.objects.all()

    # Initialiser un dictionnaire pour stocker les données
    data = {
        'labels': [],  # Noms des niveaux
        'garcons': [], # Nombre de garçons par niveau
        'filles': [],  # Nombre de filles par niveau
    }

    # Parcourir chaque niveau et compter les élèves masculins et féminins
    for niveau in niveaux:
        # Compter les garçons
        garcons_count = Eleve.objects.filter(classe__niveau=niveau, genre='Homme').count()
        # Compter les filles
        filles_count = Eleve.objects.filter(classe__niveau=niveau, genre='Femme').count()

        # Ajouter les données au dictionnaire
        data['labels'].append(niveau.nom)
        data['garcons'].append(garcons_count)
        data['filles'].append(filles_count)

    # Retourner les données au format JSON
    return JsonResponse(data)

def get_student_data(request):
    # Récupérer le nombre d'élèves masculins
    total_boys = Eleve.objects.filter(genre='Homme').count()

    # Récupérer le nombre d'élèves féminins
    total_girls = Eleve.objects.filter(genre='Femme').count()

    # Retourner les données au format JSON
    return JsonResponse({
        'boys': total_boys,
        'girls': total_girls,
    })

def totalEleve(request):
	total = Eleve.objects.count()
	return render(request, 'preschool/html-template/index.html', {'totalEleve': total})

def accueil(request):
	return render(request, 'preschool/html-template/landing_page.html')
def a_propos(request):
	return render(request, 'preschool/html-template/a_propos.html')
def nous_contacter(request):
	return render(request, 'preschool/html-template/nous_contacter.html')

def static_page(request, page_name):
	return render(request, f"preschool/html-template/{page_name}.html")

def liste_enseignants(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'preschool/html-template/teachers.html', {'enseignants': enseignants})

def ajouter_matiere(request):
	if request.method == "POST":
		id_matiere = request.POST.get('id_matiere')
		nom = request.POST.get('nom')
		classe = request.POST.get('classe')

		matiere = Matiere(id_matiere=id_matiere, nom=nom, classe=classe)
		matiere.save()

		return redirect('ajouter_matiere')

	return render(request, 'preschool/html-template/add-subject.html')

def ajouter_enseignant(request):
	if request.method == 'POST':
		id_enseignant = request.POST.get('id_enseignant')
		nom = request.POST.get('nom')
		sexe = request.POST.get('sexe')
		date_naissance = request.POST.get('date_naissance')
		telephone = request.POST.get('telephone')
		date_entree = request.POST.get('date_entree')
		qualification = request.POST.get('qualification')
		experience = request.POST.get('experience')
		nom_utilisateur = request.POST.get('nom_utilisateur')
		email = request.POST.get('email')
		mot_de_passe = request.POST.get('mot_de_passe')
		adresse = request.POST.get('adresse')
		ville = request.POST.get('ville')
		pays = request.POST.get('pays')

		enseignant = Enseignant(id_enseignant=id_enseignant, nom=nom, sexe=sexe, date_naissance=date_naissance, telephone=telephone, date_entree=date_entree, qualification=qualification, experience=experience, nom_utilisateur=nom_utilisateur, email=email, mot_de_passe=mot_de_passe, adresse=adresse, ville=ville, pays=pays)
		enseignant.save()

		return redirect('ajouter_enseignant')
	
	return render(request, 'preschool/html-template/add-teacher.html')

def liste_eleves(request):
	eleves = Eleve.objects.all()
	return render(request, 'preschool/html-template/students.html', {'eleves':eleves})

def details_eleve(request, id_eleve):
    # Récupérer l'élève ou renvoyer une erreur 404 s'il n'existe pas
    eleve = get_object_or_404(Eleve, id=id_eleve)
    # Rendre le modèle avec les données de l'élève
    return render(request, 'preschool/html-template/student-details.html', {'eleve': eleve})


# TABLEAUX DE BORD
@login_required(redirect_field_name="redirection")
def student_dashboard(request):
	return render(request, 'preschool/html-template/student-dashboard.html')

@login_required(redirect_field_name="redirection")
def teacher_dashboard(request):
	return render(request, 'preschool/html-template/teacher-dashboard.html')

@login_required(redirect_field_name="redirection")
def accountant_dashboard(request):
	return render(request, 'preschool/html-template/accountant_dashboard.html')

