from django.db import models

# Create your models here.
class Acesso(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Acesso'

    def __str__(self) -> str:
        return self.nome

class Docente(models.Model):
    acesso = models.ForeignKey(Acesso, on_delete=models.CASCADE)
    gp = [('professor','professor'),('secretaria','secretaria'),('coordenacao','coordenacao')]
    grupo = models.CharField(max_length=50, choices=gp)
    nome = models.CharField(max_length=30)
    snome = models.CharField(max_length=30, verbose_name='sobrenome')
    avatar =  models.ImageField(upload_to='avatar',blank=True)
    assinatura = models.CharField(max_length=30)
    nv = [
        ('EF','fundamental'),
        ('EM','Médio')
        ]
    nivel = models.CharField(max_length=30,choices=nv)
    dc = [
        ('artes','artes'),
        ('ciencias','ciências'),
        ('ed.fisica','educação física'),
        ('geografia','geografia'),
        ('historia','história'),
        ('ingles','inglês'),
        ('portugues','lingua portuguesa'),
        ('matematica','matemática'),
        ('artesm','artes médio'),
        ('biologia','biologia'),
        ('ed.fisicam','educação física médio'),
        ('espanhol','espanhol'),
        ('filosofia','filosofia'),
        ('fisica','física'),
        ('geografiam','geografia médio'),
        ('historiam','história médio'),
        ('inglesm','inglês médio '),
        ('portuguesm','lingua portuguesa médio'),
        ('matematicam','matemática médio'),
        ('quimica','química'),
        ('sociologia','sociologia'),
    ]
    disciplina = models.CharField(max_length=30, choices=dc)
    tn = [
        ('manha','Manhã'),
        ('tarde','Tarde'),
        ('noite','Noite')
    ]
    turno = models.CharField(max_length=30,choices=tn)
    class Meta:
        verbose_name = 'Docente'

    def __str__(self) -> str:
        return self.nome
