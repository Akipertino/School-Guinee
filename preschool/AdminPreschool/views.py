
from django.shortcuts import render, redirect
# from .forms import EleveForm, EnseignantForm
from .models import Eleve, Enseignant, Matiere, Departement, Utilisateur
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponse




def connexion(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			if(user.role == 'eleve'):
				return redirect('student_dashboard')
			elif(user.role == 'admin'):
				return redirect('admin_dashboard')
			elif(user.role == 'enseignant'):
				return redirect('teacher-dashboard')
			else:
				return redirect('accountant_dashboard')
		else:
			messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrecte')
	return render(request, 'preschool/html-template/login.html')

def deconnexion(request):
	logout(request)
	return redirect('connexion')

def inscription_eleve(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        matricule = request.POST['matricule']

        # Vérification des mots de passe
        if password != password_confirm:
            return render(request, 'preschool/html-template/inscription_eleve.html', {
                'erreur': "Les mots de passe ne correspondent pas.",
                'username': username,
                'email': email,
                'matricule': matricule,
            })

        # Vérification du matricule
        try:
            eleve = Eleve.objects.get(matricule=matricule)
        except Eleve.DoesNotExist:
            return render(request, 'preschool/html-template/inscription_eleve.html', {
                'erreur': "Le matricule est invalide ou n'existe pas.",
                'username': username,
                'email': email,
                'matricule': matricule,
            })

        # Création de l'utilisateur élève
        utilisateur = Utilisateur.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='eleve',
            identifiant_unique=matricule
        )
        utilisateur.save()

        # Connecter l'utilisateur après inscription
        login(request, utilisateur)
        return redirect('liste_eleves')  # Rediriger vers le tableau de bord de l'élève

    return render(request, 'preschool/html-template/inscription_eleve.html')

def accueil(request):
	return render(request, 'preschool/html-template/landing_page.html')

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

def ajouter_departement(request):
	if request.method == "POST":
		id_departement = request.POST.get('id_departement')
		nom = request.POST.get('nom')
		responsable = request.POST.get('responsable')
		debut = request.POST.get('debut')
		nombre_etudiant = request.POST.get('nombre_etudiant')

		departement = Departement(id_departement=id_departement, nom="nom", responsable=responsable, date_debut=debut, nombre_etudiant=nombre_etudiant)
		departement.save()
		return redirect('ajouter_departement')

	return render(request, 'preschool/html-template/add-department.html')

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


#Gestion des élèves

def ajouter_eleve(request):
	if request.method == 'POST':
		prenom = request.POST.get('prenom')
		nom = request.POST.get('nom')
		matricule = request.POST.get('matricule')
		genre = request.POST.get('genre')
		date_naissance = request.POST.get('date_naissance')
		classe = request.POST.get('classe')
		religion = request.POST.get('religion')
		photo = request.FILES.get('photo')

		nom_pere = request.POST.get('nom_pere')
		profession_pere = request.POST.get('profession_pere')
		telephone_pere = request.POST.get('profession_pere')
		email_pere = request.POST.get('profession_pere')

		nom_mere = request.POST.get('nom_mere')
		profession_mere = request.POST.get('profession_mere')
		telephone_mere = request.POST.get('profession_mere')
		email_mere = request.POST.get('profession_mere')

		eleve = Eleve(prenom=prenom,
			nom=nom,
			matricule=matricule,
			genre=genre,
			date_naissance=date_naissance,
			classe=classe, 
			religion=religion,
			photo=photo, 
			nom_pere=nom_pere, 
			profession_pere=profession_pere, 
			telephone_pere=telephone_pere, 
			email_pere=email_pere, 
			nom_mere=nom_mere, 
			profession_mere=profession_mere, 
			telephone_mere=telephone_mere, 
			email_mere=email_mere)

		eleve.save()
		return redirect('ajouter_eleve')
	return render(request, 'preschool/html-template/add-student.html')

def modification_eleve(request, eleve_id):
    # Récupérer l'élève à modifier ou retourner une 404 si l'élève n'existe pas
    eleve = get_object_or_404(Eleve, id=eleve_id)

    if request.method == "POST":
        # Récupérer les données soumises
        eleve.prenom = request.POST.get("prenom")
        eleve.nom = request.POST.get("nom")
        eleve.matricule = request.POST.get("matricule")
        eleve.genre = request.POST.get("genre")
        eleve.date_naissance = request.POST.get("date_naissance")
        eleve.classe = request.POST.get("classe")
        eleve.religion = request.POST.get("religion")

        # Gérer le téléchargement de la photo (si fournie)
        if request.FILES.get("photo"):
            eleve.photo = request.FILES.get("photo")

        # Informations des parents
        eleve.nom_pere = request.POST.get("nom_pere")
        eleve.profession_pere = request.POST.get("profession_pere")
        eleve.telephone_pere = request.POST.get("telephone_pere")
        eleve.email_pere = request.POST.get("email_pere")
        eleve.nom_mere = request.POST.get("nom_mere")
        eleve.profession_mere = request.POST.get("profession_mere")
        eleve.telephone_mere = request.POST.get("telephone_mere")
        eleve.email_mere = request.POST.get("email_mere")

        # Sauvegarder les modifications
        eleve.save()

        # Afficher un message de succès
        messages.success(request, "Les informations de l'élève ont été modifiées avec succès.")
        return redirect("liste_eleves")  # Rediriger vers la liste des élèves

    # Afficher le formulaire avec les données existantes
    return render(request, "preschool/html-template/modification.html", {"eleve": eleve})

def modifier_eleve(request):
	return render(request, 'preschool/html-template/modification.html')

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
	return render(request, 'preschool/html-template/salary.html')

@login_required(redirect_field_name="redirection")
def admin_dashboard(request):
	return render(request, 'preschool/html-template/index.html')