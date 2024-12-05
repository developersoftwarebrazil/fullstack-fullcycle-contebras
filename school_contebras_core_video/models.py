import hashlib
import time
import os
from django.utils import timezone
from django.db import models
from django.forms import ValidationError

from school_contebras_core_course.models import Student, RegistrationClassroom

def random_filename(instance, filename):
    # Extrai a extensão do arquivo
    ext = filename.split('.')[-1]
    
    # Usa o timestamp atual e o nome original para gerar o hash simples
    hash_object = hashlib.md5(f"{filename}{time.time()}".encode('utf-8'))
    hashed_filename = f"{hash_object.hexdigest()}.{ext}"

    # Retorna o caminho completo dentro da pasta 'thumbnails/'
    return os.path.join('/media/uploads', hashed_filename)

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    thumbnail = models.ImageField(upload_to=random_filename, verbose_name='Thumbnail')
    slug = models.SlugField(unique=True)
    published_at = models.DateTimeField(verbose_name='Publicado em', null=True, editable=False)
    is_published = models.BooleanField(default=False, verbose_name='Publicado')
    num_likes = models.IntegerField(default=0, verbose_name='Likes', editable=False)
    num_views = models.IntegerField(default=0, verbose_name='Visualizações', editable=False)
    tags = models.ManyToManyField('Tag', verbose_name='Tags', related_name='videos')
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='Autor', related_name='videos', editable=False)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        return super().save(force_insert, force_update, using, update_fields)

    def clean(self):
        if self.is_published:
            if not hasattr(self, 'video_media'):
                raise ValidationError('O vídeo não possui mídia associada.')
            if self.video_media.status != VideoMedia.Status.PROCESS_FINISHED:
                raise ValidationError('O vídeo não foi processado.')


    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        return super().save(force_insert, force_update, using, update_fields)

    def clean(self):
        if self.is_published:
            if not hasattr(self, 'video_media'):
                raise ValidationError('O vídeo não possui mídia associada.')
            if self.video_media.status != VideoMedia.Status.PROCESS_FINISHED:
                raise ValidationError('O vídeo não foi processado.')


    def get_video_status_display(self):
        if not hasattr(self, 'video_media'):
            return 'Pendente'
        return self.video_media.get_status_display()

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'
    
    def __str__(self):
        return self.title



class VideoMedia(models.Model):

    class Status(models.TextChoices):
        UPLOADED_STARTED = 'UPLOADED_STARTED', 'Upload Iniciado'
        PROCESS_STARTED = 'PROCESSING_STARTED', 'Processamento Iniciado'
        PROCESS_FINISHED = 'PROCESSING_FINISHED', 'Processamento Finalizado'
        PROCESS_ERROR = 'PROCESSING_ERROR', 'Erro no Processamento'

    video_path = models.CharField(max_length=255, verbose_name='Vídeo')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.UPLOADED_STARTED, verbose_name='Status')
    video = models.OneToOneField('Video', on_delete=models.PROTECT, verbose_name='Vídeo', related_name='video_media')

    def get_status_display(self):
        return VideoMedia.Status(self.status).label

    # def viridied_access_video(self,student: Student) ->bool:
    #     """
    #         Verifica se o aluno tem acesso ao vídeo, com base na matrícula e pagamento.
    #     """
    #     try:
    #         registration = RegistrationClassroom.objects.get(student=student, course=self.course)
    #         return registration.ok_access()
    #     except RegistrationClassroom.DoesNotExist:
    #         return False

    

    class Media:
        verbose_name = 'Mídia'
        verbose_name_plural = 'Mídias'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nome')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name