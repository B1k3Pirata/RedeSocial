from django.db import models
import pandas as pd

app_name = 'agenda'

class AgendamentoInicio(models.Model):
    pass

class Nivel(models.Model):
    opt = []
    opcao = models.CharField(max_length=11, choices=opt, verbose_name='Selecione nível')
    class Meta:
        verbose_name = 'Nivel'

    def __str__(self) -> str:
        return f"{self.opcao}"

class Disciplinas(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    discF = []
    discM = []

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
