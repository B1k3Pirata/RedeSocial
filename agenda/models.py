from django.db import models

app_name = 'agenda'

class AgendamentoInicio(models.Model):
    pass

class Nivel(models.Model):
    opt = [
        ('Fd', 'Fundamental'),('Md','Médio')
    ]
    opcao = models.CharField(max_length=11, choices=opt, verbose_name='Selecione nível')
    class Meta:
        verbose_name = 'Disciplinas'

    def __str__(self) -> str:
        return f"{self.opcao}"

class Disciplinas(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
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

    class Meta:
        verbose_name = 'Disciplinas'

    def __str__(self) -> str:
        return f"{self.dF}{self.dM}"

class Professor(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    profF = []
    profM = []
    profF = models.CharField(max_length=20,choices=profF,verbose_name='professores Fundamental(as)')
    profM = models.CharField(max_length=20,choices=profM,verbose_name='professores Médio(as)')

    class Meta:
        verbose_name = 'Professor'

    def __str__(self) -> str:
        return f"{self.profF}{self.profM}"
