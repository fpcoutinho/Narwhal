from django.db import models
from django.contrib.auth.models import User


class Relatorio(models.Model):
    # Campos principais do relatório.
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField()
    local = models.CharField(max_length=255)
    temperatura = models.IntegerField()
    clima = models.CharField(max_length=255)
    responsaveis = models.TextField(blank=True)

    # Campos da Avaliação e planejamento da execução.
    qualificacao_profissional = models.CharField(max_length=255, default="")
    riscos_detectados = models.CharField(max_length=255, default="[]")
    equipamentos = models.CharField(max_length=255, default="[]")
    requer_sinalizacao = models.CharField(max_length=255, default="[]")
    requer_desligamento_rede = models.CharField(max_length=4, default="")
    integridade = models.CharField(max_length=4, default="")
    dialogo_seguranca = models.CharField(max_length=4, default="")
    curso_nr = models.CharField(max_length=4, default="")
    servico_conferido = models.CharField(max_length=4, default="")
    necessita_delimitar_area = models.CharField(max_length=4, default="")
    necessita_auxilio_concessionaria = models.CharField(max_length=4, default="")
    tensao = models.CharField(max_length=4, default="")
    aterramento = models.CharField(max_length=4, default="")
    altura = models.CharField(max_length=4, default="")
    cinto_seg = models.CharField(max_length=4, default="")
    requi_seg = models.CharField(max_length=4, default="")
    reavaliacao = models.CharField(max_length=4, default="")

    # Campos da Avaliação das influencias externas da instalação elétrica.
    tempambiente = models.CharField(max_length=255, default="")
    condambiente = models.CharField(max_length=255, default="")
    altitude = models.CharField(max_length=255, default="")
    presagua = models.CharField(max_length=255, default="")
    pressolidos = models.CharField(max_length=255, default="")
    pressubst = models.CharField(max_length=255, default="")
    solmecanicas = models.CharField(max_length=255, default="")
    presmofo = models.CharField(max_length=255, default="")
    presfauna = models.CharField(max_length=255, default="")
    infleletro = models.CharField(max_length=255, default="")
    radsolar = models.CharField(max_length=255, default="")
    descatm = models.CharField(max_length=255, default="")
    movdoar = models.CharField(max_length=255, default="")
    vento = models.CharField(max_length=255, default="")
    competencia = models.CharField(max_length=255, default="")
    reseletr = models.CharField(max_length=255, default="")
    contpessoas = models.CharField(max_length=255, default="")
    condfuga = models.CharField(max_length=255, default="")
    natmatpr = models.CharField(max_length=255, default="")
    natmatcons = models.CharField(max_length=255, default="")
    classestr = models.CharField(max_length=255, default="")

    # Campos da Avaliação qualitativa da instalação elétrica.
    documentacao = models.CharField(max_length=255, default="")
    ambientesofreu = models.CharField(max_length=255, default="")
    instalacaoinspecionada = models.CharField(max_length=255, default="")
    linhaseletricasdisp = models.CharField(max_length=255, default="")
    compinstalacao = models.CharField(max_length=255, default="")
    linhaseletricascorr = models.CharField(max_length=255, default="")
    tomadasdeforca = models.CharField(max_length=255, default="")
    qtdesufitomadas = models.CharField(max_length=255, default="")
    instlquadist = models.CharField(max_length=255, default="")
    novoscircuitos = models.CharField(max_length=255, default="")
    advquadist = models.CharField(max_length=255, default="")
    dispprotecaoident = models.CharField(max_length=255, default="")
    protcircuitos = models.CharField(max_length=255, default="")
    barramentoquadist = models.CharField(max_length=255, default="")
    bitola = models.CharField(max_length=255, default="")
    condutident = models.CharField(max_length=255, default="")
    disjundif = models.CharField(max_length=255, default="")
    dispprotecaosurtos = models.CharField(max_length=255, default="")
    servseguranca = models.CharField(max_length=255, default="")
    esqaterramento = models.CharField(max_length=255, default="")
    reservadeenergia = models.CharField(max_length=255, default="")
    fontseguranca = models.CharField(max_length=255, default="")
    paralelismo = models.CharField(max_length=255, default="")

    # Campos da Avaliação quantitativa da instalação elétrica.
    capbarramento = models.PositiveSmallIntegerField(default=0)
    protgeral = models.PositiveSmallIntegerField(default=0)
    protdr = models.PositiveSmallIntegerField(default=0)
    protdps = models.PositiveSmallIntegerField(default=0)
    vab = models.PositiveSmallIntegerField(default=0)
    van = models.PositiveSmallIntegerField(default=0)
    ia = models.PositiveSmallIntegerField(default=0)
    vbc = models.PositiveSmallIntegerField(default=0)
    vbn = models.PositiveSmallIntegerField(default=0)
    ib = models.PositiveSmallIntegerField(default=0)
    vca = models.PositiveSmallIntegerField(default=0)
    vcn = models.PositiveSmallIntegerField(default=0)
    ic = models.PositiveSmallIntegerField(default=0)
    continuidade = models.CharField(max_length=255, default="")
    resistencia = models.CharField(max_length=255, default="")
    selvpelv = models.CharField(max_length=255, default="")
    verificacao = models.CharField(max_length=255, default="")
    ensaiodetensao = models.CharField(max_length=255, default="")
    ensaiodefunc = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.local + " - " + str(self.data) + " - " + str(self.autor)


class Circuito(models.Model):
    rel_pai = models.ForeignKey(Relatorio, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=255, default="")
    fase = models.CharField(max_length=255, default="")
    disjuntor = models.CharField(max_length=255, default="")
    descricao = models.CharField(max_length=255, default="")
    condutor = models.CharField(max_length=255, default="")
    corrente = models.CharField(max_length=255, default="")

    def __str__(self):
        return (
            self.modelo
            + " - "
            + self.fase
            + " - "
            + self.disjuntor
            + " - "
            + self.descricao
            + " - "
            + self.condutor
            + " - "
            + self.corrente
        )


class Imagem(models.Model):
    rel_pai = models.ForeignKey(Relatorio, on_delete=models.CASCADE)
    img = models.FileField(upload_to="media/", blank=True, null=True)
