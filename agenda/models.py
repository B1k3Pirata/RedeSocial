from django.db import models
import pandas as pd
import csv

app_name = 'agenda'

class AgendamentoInicio(models.Model):
    pass

"""class Nivel_Disc_Prof(models.Model):
    pnivel = models.CharField(max_length=20)
    pdiscf = models.CharField(max_length=20)
    pdiscm = models.CharField(max_length=20)
    pprof = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Nivel_Disc_Prof'
    def __str__(self) -> str:
        return f'{self.pnivel}'"""

class Nivel(models.Model):
    opcaof = models.CharField(max_length=11)
    #opcaom = models.CharField(max_length=11)
    class Meta:
        verbose_name = 'Nivel'

    def __str__(self) -> str:
        return f"{self.opcao}"

class Disciplinas(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    disc = models.CharField(max_length=20,verbose_name='Disciplinas')

    class Meta:
        verbose_name = 'Disciplinas'

    def __str__(self) -> str:
        return f"{self.disc}"

class Professor(models.Model):
    disciplina = models.CharField(max_length=20)
    nivel = models.CharField(max_length=20)
    turno = models.CharField(max_length=20)
    docente = models.CharField(max_length=20)

    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    disc = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    """profF = models.CharField(max_length=20,choices=profF,verbose_name='professores Fundamental(as)')
    profM = models.CharField(max_length=20,choices=profM,verbose_name='professores Médio(as)')
"""
    class Meta:
        verbose_name = 'Professor'

    def __str__(self) -> str:
        return f"{self.prof}"
