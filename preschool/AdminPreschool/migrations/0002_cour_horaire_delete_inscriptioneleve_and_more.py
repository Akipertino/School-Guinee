# Generated by Django 5.1.3 on 2024-12-08 13:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPreschool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifiant', models.CharField(max_length=100, unique=True)),
                ('nom', models.CharField(help_text='Nom du cours', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Description du cours')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(choices=[('lundi', 'Lundi'), ('mardi', 'Mardi'), ('mercredi', 'Mercredi'), ('jeudi', 'Jeudi'), ('vendredi', 'Vendredi'), ('samedi', 'Samedi'), ('dimanche', 'Dimanche')], max_length=9)),
                ('heure_debut', models.TimeField(help_text='Heure de début du cours')),
                ('heure_fin', models.TimeField(help_text='Heure de fin du cours')),
            ],
        ),
        migrations.DeleteModel(
            name='InscriptionEleve',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='identifiant_unique',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='role',
        ),
        migrations.AlterField(
            model_name='departement',
            name='nombre_etudiant',
            field=models.PositiveIntegerField(),
        ),
        migrations.AddField(
            model_name='cour',
            name='enseignant',
            field=models.ForeignKey(help_text='Enseignant responsable du cours', limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='cours', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='horaire',
            name='cours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horaires', to='AdminPreschool.cour'),
        ),
    ]
