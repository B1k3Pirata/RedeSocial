from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from datetime import datetime, date
import uuid

class AgendamentoNVL(models.Model):
    niv = [('Fundamental','Fundamental'),
    ('Médio','Médio'),
    ]
    nivel = models.CharField(max_length=20,choices=niv)
    AgendamentoAln = models.ForeignKey('AgendamentoAln', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nivel}'
    #-----
class AgendamentoDSC(models.Model):
    discF = [
        ('Selecione','Selecione'),
        ('Artes','Artes'),
        ('Ciências','Ciências'),
        ('Ed.Fisica','Ed.Fisica'),
        ('Geografia','Geografia'),
        ('História','História'),
        ('Inglês','Inglês'),
        ('Matemática','Matemática'),
        ('Português','Português'),
        ]
    discM = [
        ('Selecione','Selecione'),
        ('Artes','Artes'),
        ('Biologia','Biologia'),
        ('Ed.Fisica','Ed.Fisica'),
        ('Espanhol','Espanhol'),
        ('Filosofia','Filosofia'),
        ('Geografia','Geografia'),
        ('História','História'),
        ('Inglês','Inglês'),
        ('Matemática','Matemática'),
        ('Português','Português'),
        ('Quimica','Quimica'),
        ('Sociologia','Sociologia'),
        ]
    dF = models.CharField(max_length=20,choices=discF,verbose_name='Disciplinas do Fundamental')
    dM = models.CharField(max_length=20,choices=discM,verbose_name='Disciplinas do Médio')
    AgendamentoAln = models.ForeignKey('AgendamentoAln', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.dF}{self.dM}'
#-----
class AgendamentoPRF(models.Model):
    prof = [('carlos','carlos'),('helda','helda'),('ilma','ilma'),('barbara','barbara')]
    professor = models.CharField(max_length=20,choices=prof,verbose_name='professores(as)')
    AgendamentoAln = models.ForeignKey('AgendamentoAln', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.professor}'
#-----
class AgendamentoAln(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    matricula = models.IntegerField()

    t = [('manhã','manhã'),('tarde','tarde'),('noite','noite')]
    turno = models.CharField(max_length=20,choices=t)
    email = models.EmailField(max_length=20)
    cell = models.IntegerField(verbose_name='celular')
    protocolo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='insira novamento sua matricula (somente numeros)')
    criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-criado",)
        def __str__(self):
            return self.matricula

    def get_absolute_url(self):
        return reverse("agenda:detalhe", kwargs={"slug": self.slug})

    def __str__(self):
        return f'{self.nome},{self.sobrenome},{self.matricula},{self.turno},{self.email}, {self.cell}, {self.protocolo},{self.slug},{self.criado}'
