from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
import uuid
from datetime import date, time, datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

#candidato a banca Permanente
class BancaPermanente(models.Model):
    nome = models.CharField(max_length=255, verbose_name='nome completo')
    snome = models.CharField(max_length=255, verbose_name='sobrenome completo')
    dataCad = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)
    controle = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'BancaPermanente'

    def __str__(self) -> str:
        return f"{self.nome}"

#candidato/aluno
class AtendimentoPersonalizado(models.Model):
    nome = models.CharField(max_length=255, verbose_name='nome completo')
    snome = models.CharField(max_length=255, verbose_name='sobrenome completo')
    dataCad = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)
    controle = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'AtendimentoPersonalizado'

    def __str__(self) -> str:
        return f"{self.nome}"

#cadastro de aluno/usuario
class UsrCad(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'UsrCad'

    def __str__(self) -> str:
        return self.nome

#dados educacionais
class EduCad(models.Model):
    usuario = models.ForeignKey(UsrCad, on_delete=models.CASCADE)
    nvl = [('EF','fundamental'),('EM','Médio')]
    nivel = models.CharField(choices=nvl, max_length=255, verbose_name='nível pretendido')
    
    class Meta:
        verbose_name = 'EduCad'

    def __str__(self) -> str:
        return f'{self.nivel}{self.ano}'

#dados do aluno
class AlunoDados(models.Model):
    usuario = models.ForeignKey(UsrCad, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, verbose_name='nome completo')
    snome = models.CharField(max_length=255, verbose_name='sobrenome completo')
    dataMat = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'AlunoDados'

    def __str__(self) -> str:
        return f"{self.nome}{self.snome}{self.dataMat}"

class Parentesco(models.Model):
    usuario = models.ForeignKey(UsrCad, null=True, blank=True, on_delete=models.CASCADE)
    filia1 = models.CharField(max_length=30, verbose_name='filiação_1')
    filia2 = models.CharField(max_length=30, verbose_name='filiação_2')

    class Meta:
        verbose_name = 'DocPessoal'

    def __str__(self) -> str:
        return f'{self.rg}{self.cpf}{self.filia1}{self.filia2}'

class Pessoal(models.Model):
    usuario = models.ForeignKey(UsrCad, null=True, blank=True, on_delete=models.CASCADE)
    #fonte de dados
    Sexo = [
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das Opções")
    ]
    Raca = [
        ("I","Indigena"),
        ("N","Negro(a)"),
        ("P","Pardo(a)"),
        ("A","Amarelos(as)"),
        ("B","Branco(as)")
    ]
    QPNL = [
        ("S","Sim"),
        ("N","Não")
    ]
    NAC = [
        ("Bra","Brasileiro(a)"),
        ("Est","Estrangeiro(a)")
    ]
    UF = [
        ("PA","PA"), ("AM","AM"),("AC","AC"),("AP","AP"),("RR","RR"),("MA","MA"),("TO","TO"),
        ("AL","AL"),("PE","PE"),("GO","GO"),("ES","ES"),("BA","BA"),("MT","MT"),("MS","MS"),("MG","MG"),
        ("PR","PR"),("PI","PI"),("RJ","RJ"),("RN","RN"),("RS","RS"),("RO","RO"),("SC","SC"),("SP","SP"),
        ("SE","SE"),
    ]
    Dnasc = models.DateField(null=False, blank=False, verbose_name="data de nascimento")
    sexo = models.CharField(max_length=10, choices=Sexo)
    raca = models.CharField(max_length=10, choices=Raca,verbose_name="raça")
    qprenm = models.CharField(max_length=10, choices=QPNL,verbose_name="deseja usar pré-nome social?")
    prenm = models.CharField(max_length=255,verbose_name="digite o seu pré-nome social, caso possua.")

    nacio = models.CharField(max_length=10, choices=NAC,verbose_name="nacionalidade")
    qnacio = models.CharField(max_length=255,verbose_name="nacionalidade")
    ufnasc = models.CharField(max_length=10, choices=UF,verbose_name="UF de nascimento")
    locnasc = models.CharField(max_length=255, verbose_name="local de nascimento")

    class Meta:
        verbose_name = 'Pessoal'

    def __str__(self) -> str:
        return  f'{self.Dnasc}{self.sexo}{self.raca}{self.qprenm}{self.prenm}{self.nacio}{self.qnacio}{self.ufnasc}{self.locnascS}'

class Documento(models.Model):
    usuario = models.ForeignKey(UsrCad, null=True, blank=True, on_delete=models.CASCADE)
    #Documentos
    QCer = [
        ("S","Sim"),
        ("N","Não"),
    ]
    TPCerL = [
        ("Nasc","Nascimento"),
        ("Casa", "Casamento"),
        ("Divo","Divórcio"),
    ]
    Qrg = [
        ("S","Sim"),
        ("N","Não"),
    ]
    QZon = [
        ("S","Sim"),
        ("N","Não"),
    ]
    UF = [
        ("PA","PA"), ("AM","AM"),("AC","AC"),("AP","AP"),("RR","RR"),("MA","MA"),("TO","TO"),
        ("AL","AL"),("PE","PE"),("GO","GO"),("ES","ES"),("BA","BA"),("MT","MT"),("MS","MS"),("MG","MG"),
        ("PR","PR"),("PI","PI"),("RJ","RJ"),("RN","RN"),("RS","RS"),("RO","RO"),("SC","SC"),("SP","SP"),
        ("SE","SE"),
    ]
#certidão
    qpcer = models.CharField(max_length=10, choices=QCer,verbose_name="Possui Certidão?")
    tpcerl = models.CharField(max_length=10, choices=TPCerL,verbose_name="Tipo de certidão")
    nocer = models.CharField(max_length=255,verbose_name="número da certidão")
    licer = models.CharField(max_length=105,verbose_name="livro da certidão")
    flcer = models.CharField(max_length=105,verbose_name="folha da certidão")
    emtcr = models.CharField(max_length=105,verbose_name="data de emissão da certidão")
    cartc = models.CharField(max_length=105,verbose_name="cartório de registro")
    ufcrt = models.CharField(max_length=10, choices=UF,verbose_name="UF do cartório")
    cidcrt = models.CharField(max_length=105,verbose_name="cidade do cartório")
    #imgCert = models.ImageField(upload_to='imagens/{}{}{}'.format(self.nome,self.id,self.ano))
    #image = models.ImageField(upload_to='media')

    qrg = models.CharField(max_length=10, choices=Qrg,verbose_name="possui R.G?")
    norg = models.CharField(max_length=105,verbose_name="número do R.G")
    orgrg = models.CharField(max_length=105,verbose_name="Órgão emissor")
    ufrg = models.CharField(max_length=10, choices=UF,verbose_name="UF do Órgão Emissor")
    dtrg = models.CharField(max_length=105,verbose_name="data de emissão do R.G")
    cpf = models.CharField(max_length=105,verbose_name="C.P.F.")
    pasp = models.CharField(max_length=105,verbose_name="passaporte")

    class Meta:
        verbose_name = 'Documento'

    def __str__(self) -> str:
        return f'{self.qpcer}{self.tpcerl}{self.nocer}{self.nocer}{self.licer}{self.flcer}{self.emtcr}{self.cartc}{self.ufcrt}{self.cidcrt}{self.qrg}{self.norg}{self.orgrg}{self.ufrg}{self.dtrg}{self.cpf}{self.pasp}'

class End(models.Model):
    usuario = models.ForeignKey(UsrCad, null=True, blank=True, on_delete=models.CASCADE)
    UF = [
        ("PA"), ("AM"),("AC"),("AP"),("RR"),("MA"),("TO"),
        ("AL"),("PE"),("GO"),("ES"),("BA"),("MT"),("MS"),("MG"),
        ("PR"),("PI"),("RJ"),("RN"),("RS"),("RO"),("SC"),("SP"),
        ("SE"),("RO")
    ]
    QZon = [
        ("U","Urbana"),
        ("R","Rural"),
    ]
    end = models.CharField(max_length=1055,verbose_name="endereço residêncial")
    num = models.CharField(max_length=7,verbose_name="número")
    muni = models.CharField(max_length=1055,verbose_name="município")
    cep = models.CharField(max_length=105,verbose_name="C.E.P")
    comp = models.CharField(max_length=1055,verbose_name="complemento")
    brr = models.CharField(max_length=1055,verbose_name="bairro")
    uncon = models.CharField(max_length=105,verbose_name="Unidade Consumidora(CELPA)")
    qzon = models.CharField(max_length=10, choices=QZon,verbose_name="zona")

    class Meta:
        verbose_name = 'Endereço'

    def __str__(self) -> str:
        return f'{self.end}{self.num}{self.muni}{self.cep}{self.comp}{self.brr}{self.uncon}{self.qzon}{self.ct1}{self.ct2}{self.email}'

class Sau(models.Model):
    usuario = models.ForeignKey(UsrCad, null=True, blank=True, on_delete=models.CASCADE)
    #dados Complementares
    AEP = [
        ("S","Sim"),
        ("N","Não")
    ]
    SAEP = [
        ("S","Sim"),
        ("N","Não")
    ]
    NAEP = [
        ("S","Sim"),
        ("N","Não")
    ]
    aep = models.CharField(max_length=10, choices=AEP,verbose_name="necessita de atendimento especializado(Apoio Pedagógico?)")
    #saep = models.CharField(max_length=10, choices=SAEP,)
    #naep = models.CharField(max_length=10, choices=NAEP,)
    CEGO = [
        ("S","Sim"),
        ("N","Não")
    ]
    BV = [
        ("S","Sim"),
        ("N","Não")
    ]
    SC = [
        ("S","Sim"),
        ("N","Não")
    ]
    cego = models.CharField(max_length=10, choices=CEGO)
    bv = models.CharField(max_length=10, choices=BV,verbose_name="baixa visão")
    sc = models.CharField(max_length=10, choices=SC, verbose_name="surdo-cegueira")
    SD = [
        ("S","Sim"),
        ("N","Não")
    ]
    DA = [
        ("S","Sim"),
        ("N","Não")
    ]
    DI = [
        ("S","Sim"),
        ("N","Não")
    ]
    sd = models.CharField(max_length=10, choices=SD,verbose_name="surdez")
    da = models.CharField(max_length=10, choices=DA,verbose_name="deficiência auditiva")
    di = models.CharField(max_length=10, choices=DI,verbose_name="deficiência intelectual")
    DM = [
        ("S","Sim"),
        ("N","Não")
    ]
    DF = [
        ("S","Sim"),
        ("N","Não")
    ]
    AI = [
        ("S","Sim"),
        ("N","Não")
    ]
    dm = models.CharField(max_length=10, choices=DM,verbose_name="deficiências multiplas")
    df = models.CharField(max_length=10, choices=DF,verbose_name="deficiêcnia física")
    ai = models.CharField(max_length=10, choices=AI,verbose_name="autismo infantil")
    SRT = [
        ("S","Sim"),
        ("N","Não")
    ]
    SASP = [
        ("S","Sim"),
        ("N","Não")
    ]
    TDI = [
        ("S","Sim"),
        ("N","Não")
    ]
    AHS = [
        ("S","Sim"),
        ("N","Não")
    ]
    srt = models.CharField(max_length=10, choices=SRT,verbose_name="síndrome de Rett")
    sasp = models.CharField(max_length=10, choices=SASP,verbose_name="síndrome de Asperger")
    tdi = models.CharField(max_length=10, choices=TDI,verbose_name="transtorno desintegrativo da infância")
    ahs = models.CharField(max_length=10, choices=AHS,verbose_name="altas habilidades/superdotação")

    class Meta:
        verbose_name = 'Saúde'

    def __str__(self):
        return  f'{self.aep}{self.cego}{self.bv}{self.sc}{self.sd}{self.da}{self.di}{self.dm}{self.df}{self.ai}{self.srt}{self.sasp}{self.tdi}{self.ahs}{slf.srt}{self.sasp}{self.tdi}'

class Social(models.Model):
    usuario = models.ForeignKey(UsrCad, null=True, blank=True, on_delete=models.CASCADE)
    #Programas sociais
    BCP = [
        ("S","Sim"),
        ("N","Não")
    ]
    PBF = [
        ("S","Sim"),
        ("N","Não")
    ]
    PBT = [
        ("S","Sim"),
        ("N","Não")
    ]
    PETI = [
        ("S","Sim"),
        ("N","Não")
    ]
    bcp = models.CharField(max_length=10, choices=BCP,verbose_name="é atendido(a) pelo BCP(Benefício de Prestação Continuada)?")
    pbf = models.CharField(max_length=10, choices=PBF,verbose_name="é atendido(a) pelo PBF(Programa Bolsa Familia)?")
    pbt = models.CharField(max_length=10, choices=PBT,verbose_name="é atendido pelo PBT(Programa Bolsa Trabalho)?")
    peti = models.CharField(max_length=10, choices=PETI,verbose_name="é atendido(a) pelo PETI(Programa de Erradicação do Trabalho Infantil)")

    class Meta:
        verbose_name = 'Social'

    def __str__(self) -> str:
        return f'{self.bcp}{self.pbf}{self.pbt}{self.peti}'

class Transp(models.Model):
    usuario = models.ForeignKey(UsrCad, null=True, blank=True, on_delete=models.CASCADE)
    #Programas Transporte
    PPRTE = [
        ("S","Sim"),
        ("N","Não")
    ]
    PBFa = [
        ("S","Sim"),
        ("N","Não")
    ]
    QServ = [
        ("S","Sim"),
        ("N","Não")
    ]
    URB = [
        ("RU","Rural/Urbano"),
        ("UR","Urbano/Rural"),
        ("RR","Rural/Rural"),
        ("UU","Urbana/Urbana")
    ]
    ROD = [
        ("Não Uso","Não Uso"),
        ("VK","Vans/Kombi"),
        ("Mo","Urbano/Rural"),
        ("BK","Bicicleta"),
        ("On","Ônibus"),
        ("An","Animal"),
        ("Ot","Outro")
    ]
    Aqua = [
        ("Não Uso","Não Uso"),
        ("C5","Cap. de até 5 anos"),
        ("C105","Cap. de 5 a 105 anos"),
        ("C105","Cap. de até 105 a105 anos"),
        ("C105+","Cap. acima de 105 anos")
    ]
    Trm = [
        ("Não Uso","Não Uso"),
        ("Trem","Trem/Metrô")
    ]
    pprte = models.CharField(max_length=10, choices=PPRTE,verbose_name="Poder Público Responsável Pelo Transporte Escolar")
    pbfa = models.CharField(max_length=10, choices=PBFa,verbose_name="é atendido(a) pelo PBF(Programa Bolsa Familia)")
    qserv = models.CharField(max_length=10, choices=QServ,verbose_name="você utiliza esse serviço?")
    urb = models.CharField(max_length=10, choices=URB,verbose_name="urbano/rural")
    rod = models.CharField(max_length=10, choices=ROD,verbose_name="rodoviário")
    aqua = models.CharField(max_length=10, choices=Aqua,verbose_name="aquaviário/embarcação")
    trm = models.CharField(max_length=10, choices=Trm,verbose_name="trem/metrô")

    class Meta:
        verbose_name = 'Transporte'

    def __str__(self):
        return  f'{self.pprte},{self.pbfa},{self.qserv},{self.urb},{self.rod},{self.aqua},{self.trm}'

class Proc(models.Model):
    usuario = models.ForeignKey(UsrCad, null=True, blank=True, on_delete=models.CASCADE)
    #Procedência do aluno
    P1a = [
        ("S","Sim"),
        ("N","Não")
    ]
    P2a = [
        ("S","Sim"),
        ("N","Não")
    ]
    P3a = [
        ("S","Sim"),
        ("N","Não")
    ]
    P4a = [
        ("S","Sim"),
        ("N","Não")
    ]
    RAT = [
        ("H","Hospital"),
        ("D","Domicílio"),
        ("N","Não Recebe")
    ]
    nesc = models.CharField(max_length=1055,verbose_name="nome da escola")
    pore1a = models.CharField(max_length=10, choices=P1a,default="", editable=True, verbose_name="procedente de outra rede de ensino, após a 1ª avaliação, com parãmetros diferenciados da SEDUC?")
    pore2a = models.CharField(max_length=10, choices=P2a,default="", editable=True, verbose_name="recebido(a) na 2ª avaliação")
    pore3a = models.CharField(max_length=10, choices=P3a, default="", editable=True, verbose_name="recebido(a) na 3ª avaliação")
    pore4a = models.CharField(max_length=10, choices=P4a,default="", editable=True, verbose_name="recebido(a) na 4ª avaliação")
    comec = models.CharField(max_length=100,verbose_name="código MEC")
    anx = models.CharField(max_length=1055,verbose_name="anexo")
    idtnv = models.CharField(max_length=100,verbose_name="nível")
    fase = models.CharField(max_length=100,verbose_name="fase")
    turno = models.CharField(max_length=100,verbose_name="turno")
    modal = models.CharField(max_length=100,verbose_name="modalidade")
    seq = models.CharField(max_length=100,verbose_name="sequencial (0 a 99)")
    rat = models.CharField(max_length=10, choices=RAT,verbose_name="recebe escolarização em outro espaço(diferente da escola)?")

    class Meta:
        verbose_name = 'Procedência'

    def __str__(self) -> str:
        return f'{self.nesc},{self.pore1a},{self.pore2a},{self.pore3a}, {self.pore4a},{self.comec},{self.anx},{self.idtnv},{self.fase},{self.turno},{self.turno},{self.modal},{self.seq},{self.rat}'

class Imagens(models.Model):
    usuario = models.ForeignKey(UsrCad, null=True, blank=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', blank=True)
    dochist = models.ImageField(upload_to='historico', blank=True)
    docRG = models.ImageField(upload_to='rg', blank=True)
    docRG2 = models.ImageField(upload_to='rg', blank=True)
    docCPF = models.ImageField(upload_to='cpf',blank=True)
    docRes = models.ImageField(upload_to='comprovaResid', blank=True)
    docCert = models.ImageField(upload_to='certificaFund', blank=True)

    class Meta:
        verbose_name = 'Imagens'

    def __str__(self) -> str:
        return f'{avatar}{dochist}{docRG}{docRG2}{docCPF}{docRes}{docCertp}'

class Contato(models.Model):
    usuario = models.ForeignKey(UsrCad, null=True, blank=True, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=10, blank=True)
    celular = models.CharField(max_length=11)

    class Meta:
        verbose_name = 'Contato'

    def __str__(self) -> str:
        return f"{self.telefone}{self.celular}"
