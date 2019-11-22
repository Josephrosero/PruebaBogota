from rest_framework import serializers
from .models import Student
from .models import Professor
from .models import Score

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name')
