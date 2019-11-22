

from django.contrib import admin

from .models import Student
from .models import Professor
from .models import Score

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Score)

# Register your models here.
