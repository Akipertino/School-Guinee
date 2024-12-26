from AdminPreschool.models import Niveau

niveaux = ['1ère', '2ème', '3ème', '4ème', '5ème', '6ème', '7ème', '8ème', '9ème', '10ème', '11ème', '12ème', 'Terminale']

for n in niveaux:
    Niveau.objects.get_or_create(nom=n, defaults={'description':'Aucune'})

print('Fin des opérations');





