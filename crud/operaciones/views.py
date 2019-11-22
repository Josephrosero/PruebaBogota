from django.shortcuts import render,redirect
from django.http import HttpResponse

from rest_framework import generics
from .serializers import StudentsSerializer
from .models import *
from .forms import *

class StudentsList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


def home(request):
    return render(request,"index.html")


def crearStudiante(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form=StudentForm()
    return render(request,'operaciones/crear_student.html', {'form':form})

def listarStudiante(request):
    student = Student.objects.all
    context = {'student':student}
    return render(request,'operaciones/listar_students.html', context)

def editarStudiante(request,id):
    student =Student.objects.get(id= id)
    if request.method == 'GET':
        form = StudentForm(instance = student)
    else:
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'operaciones/crear_student.html', {'form':form})


def eliminarStudent(request, id):
    student = Student.objects.get(id = id)
    if request.method=='POST':
        student.delete()
        return redirect('index')
    return  render(request,'operaciones/eliminar_student.html', {'student':student})



def crearProfessor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form=ProfessorForm()
    return render(request,'operaciones/crear_professor.html', {'form':form})

def listarProfesor(request):
    professor = Professor.objects.all
    context = {'professor':professor}
    return render(request,'operaciones/listar_professor.html', context)


def editarProfessor(request,id):
    professor =Professor.objects.get(id= id)
    if request.method == 'GET':
        form = StudentForm(instance = professor)
    else:
        form = ProfessorForm(request.POST, instance = professor)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'operaciones/crear_professor.html', {'form':form})

def eliminarProfessor(request, id):
    professor = Professor.objects.get(id = id)
    if request.method=='POST':
        professor.delete()
        return redirect('index')
    return  render(request,'operaciones/eliminar_professor.html', {'professor':professor})


def crearScore(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=ScoreForm()
    return render(request,'operaciones/crear_score.html', {'form':form})


def listarScore(request):
    score = Score.objects.all
    context = {'score':score}
    return render(request,'operaciones/listar_score.html', context)

def editarScore(request,id):
    score =Score.objects.get(id= id)
    if request.method == 'GET':
        form = ScoreForm(instance = score)
    else:
        form = ScoreForm(request.POST, instance = score)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'operaciones/crear_score.html', {'form':form})

def eliminarScore(request, id):
    score = Score.objects.get(id = id)
    if request.method=='POST':
        score.delete()
        return redirect('index')
    return  render(request,'operaciones/eliminar_score.html', {'score':score})


def index(request):
    return HttpResponse("Welcome. look the urls configuration for the accion in the db. thanks!")


# Create your views here.
