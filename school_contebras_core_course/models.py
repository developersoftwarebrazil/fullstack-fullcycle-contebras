from django.db import models

# Create your models here.

##Model de Gerenviamento de aluno
class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome do aluno")
    studentEmail = models.EmailField(max_length=100, verbose_name='Email do aluno')
    course = models.ManyToManyField('Course', verbose_name='Curso', related_name='student')
    classroom = models.ManyToManyField('Classroom', verbose_name='Turma', related_name='student')

    class Meta:
        verbose_name = "Aluno"  # Singular
        verbose_name_plural = "Alunos"  # Plural

    def __str__(self):
        return self.name


##Model de Gerencimaneto de Curso
class Course(models.Model):
    titleCourse = models.CharField(max_length=255, verbose_name="Título do curso")
    description = models.TextField(verbose_name="Descrição do curso")

    class Meta:
        verbose_name = "Curso"  # Singular
        verbose_name_plural = "Cursos"  # Plural

    def __str__(self):
        return self.titleCourse

  
#Model de Gerenciemnto de Turma   
class Classroom(models.Model):
    name = models.CharField(max_length=100, default="Nome padrão", verbose_name='Curso')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classrooms')
    students = models.ManyToManyField(Student, through='RegistrationClassroom', related_name='classrooms')

    class Meta:
        verbose_name = "Turma"  # Singular
        verbose_name_plural = "Turmas"  # Plural

    def __str__(self):
        return f'Turma {self.name} - {self.course.titleCourse}'

class RegistrationClassroom(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="nome do aluno")
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, verbose_name='matriculado na turma')
    registration_date = models.DateField(auto_now_add=True, verbose_name="Matriculado em")

    class Meta:
        verbose_name = "Matrícula"  # Singular
        verbose_name_plural = "Matrículas"  # Plural

    def __str__(self):
        return f"{self.student.name} matriculado na turma {self.classroom.name}"

# def register_models():
#     from .models import Student, Course, Classroom, RegistrationClassroom
#     admin.site.register(Student)
#     admin.site.register(Course)
#     admin.site.register(Classroom)
#     admin.site.register(RegistrationClassroom)

# register_models()