
from django import forms
# from .models import Eleve, Enseignant

# class EleveForm(forms.ModelForm):
#     class Meta:
#         model = Eleve
#         fields = '__all__'
#         widgets = {
#             'date_naissance': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'type': 'date',  # Assure l'utilisation d'un champ date HTML5
#             }),
#         }


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'

# class EnseignantForm(forms.ModelForm):
#     class Meta:
#         model = Enseignant
#         fields = '__all__'