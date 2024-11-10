from xml.dom import ValidationErr
from django.contrib import admin
from django.forms import ModelForm, ValidationError
from django.http import HttpRequest
from school_contebras_core_course.models import Student, Course,Classroom, RegistrationClassroom



# Register your models here.

admin.site.site_header = 'Painel Administrativo da Escola Contebras'

class CourseAdmin(admin.ModelAdmin):
  list_display = ('titleCourse','description')
  list_filter = ('titleCourse', 'description')
  search_fields = ('titleCourse', 'description')
  
class StudentAdmin(admin.ModelAdmin):
  list_display = ('name', 'studentEmail')
  list_filter = ('name', 'studentEmail')
  search_fields = ('name', 'studentEmail')


class ClassroomAdmin(admin.ModelAdmin):
  list_display = ('name','course')
  list_filter = ('name', 'course')
  search_fields = ('name', 'course')

class RegistrationAdmin(admin.ModelAdmin):
  list_display = ('student','classroom', 'registration_date')
  list_filter = ('student', 'classroom', 'registration_date')
  search_fields = ('student', 'classroom')
  date_hierarchy= ('registration_date')

  def save_model(self, request: HttpRequest, obj, form, change):
    if not obj.student or not obj.course:
      raise ValidationError("A matrícula só pode ser feita se houver um aluno e um curso.")
    super().save_model(request, obj, form, change)

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(RegistrationClassroom, RegistrationAdmin)