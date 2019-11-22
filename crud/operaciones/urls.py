from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$',index, name= "index"),

    url(r'^crear_student',crearStudiante, name= "crear_student"),
    url(r'^crear_professor',crearProfessor, name= "crear_professor"),
    url(r'^listar_students',listarStudiante, name= "listar_students"),
    url(r'^listar_professor',listarProfesor, name= "listar_professor"),
    url(r'^editar_student/(?P<id>\d+)/$',editarStudiante, name= "editar_student"),
    url(r'^editar_professor/(?P<id>\d+)/$',editarProfessor, name= "editar_professor"),
    url(r'^eliminar_student/(?P<id>\d+)/$',eliminarStudent, name= "eliminar_student"),
    url(r'^eliminar_professor/(?P<id>\d+)/$',eliminarProfessor, name= "eliminar_professor"),
    url(r'^crear_score',crearScore, name= "crear_score"),
    url(r'^listar_score',listarScore, name= "listar_score"),
    url(r'^editar_score/(?P<id>\d+)/$',editarScore, name= "editar_score"),
    url(r'^eliminar_score/(?P<id>\d+)/$',eliminarScore, name= "eliminar_score"),



]
