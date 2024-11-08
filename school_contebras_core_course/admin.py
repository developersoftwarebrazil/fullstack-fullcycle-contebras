from django.contrib import admin
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

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(RegistrationClassroom, RegistrationAdmin)