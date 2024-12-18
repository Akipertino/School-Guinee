# Generated by Django 5.1.2 on 2024-12-07 16:23

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_departement', models.CharField(max_length=50, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('responsable', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('nombre_etudiant', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('matricule', models.CharField(max_length=50, unique=True)),
                ('genre', models.CharField(max_length=20)),
                ('date_naissance', models.DateField()),
                ('classe', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo_eleves/')),
                ('nom_pere', models.CharField(max_length=100)),
                ('profession_pere', models.CharField(max_length=100)),
                ('telephone_pere', models.CharField(max_length=15)),
                ('email_pere', models.EmailField(blank=True, max_length=254, null=True)),
                ('nom_mere', models.CharField(max_length=100)),
                ('profession_mere', models.CharField(max_length=100)),
                ('telephone_mere', models.CharField(max_length=15)),
                ('email_mere', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InscriptionEleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=100, unique=True, verbose_name='Matricule')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Élève',
                'verbose_name_plural': 'Élèves',
            },
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_matiere', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NiveauClasse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_enseignant', models.CharField(max_length=50, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('sexe', models.CharField(max_length=30)),
                ('date_naissance', models.DateField()),
                ('telephone', models.CharField(max_length=15)),
                ('date_entree', models.DateField()),
                ('qualification', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('nom_utilisateur', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mot_de_passe', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPreschool.matiere')),
            ],
        ),
        migrations.AddField(
            model_name='matiere',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPreschool.niveauclasse'),
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Administrateur'), ('enseignant', 'Enseignant'), ('eleve', 'Élève'), ('comptable', 'Comptable')], max_length=20)),
                ('identifiant_unique', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
