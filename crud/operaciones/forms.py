from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields=[
            'id',
            'name'
        ]



class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor

        fields=[
            'id',
            'name'
        ]

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score

        fields=[
            'id',
            'name',
            'professor',
            'student',
        ]
