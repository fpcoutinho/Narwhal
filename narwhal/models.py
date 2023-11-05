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
    qualificacao_profissional = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    riscos_detectados = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    equipamentos = models.CharField(max_length=255, default="", blank=True, null=True)
    requer_sinalizacao = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    requer_desligamento_rede = models.CharField(
        max_length=4, default="", blank=True, null=True
    )
    integridade = models.CharField(max_length=4, default="", blank=True, null=True)
    dialogo_seguranca = models.CharField(
        max_length=4, default="", blank=True, null=True
    )
    curso_nr = models.CharField(max_length=4, default="", blank=True, null=True)
    servico_conferido = models.CharField(
        max_length=4, default="", blank=True, null=True
    )
    necessita_delimitar_area = models.CharField(
        max_length=4, default="", blank=True, null=True
    )
    necessita_auxilio_concessionaria = models.CharField(
        max_length=4, default="", blank=True, null=True
    )
    tensao = models.CharField(max_length=4, default="", blank=True, null=True)
    aterramento = models.CharField(max_length=4, default="", blank=True, null=True)
    altura = models.CharField(max_length=4, default="", blank=True, null=True)
    cinto_seg = models.CharField(max_length=4, default="", blank=True, null=True)
    requi_seg = models.CharField(max_length=4, default="", blank=True, null=True)
    reavaliacao = models.CharField(max_length=4, default="", blank=True, null=True)

    # Campos da Avaliação das influencias externas da instalação elétrica.
    tempambiente = models.CharField(max_length=255, default="", blank=True, null=True)
    condambiente = models.CharField(max_length=255, default="", blank=True, null=True)
    altitude = models.CharField(max_length=255, default="", blank=True, null=True)
    presagua = models.CharField(max_length=255, default="", blank=True, null=True)
    pressolidos = models.CharField(max_length=255, default="", blank=True, null=True)
    pressubst = models.CharField(max_length=255, default="", blank=True, null=True)
    solmecanicas = models.CharField(max_length=255, default="", blank=True, null=True)
    presmofo = models.CharField(max_length=255, default="", blank=True, null=True)
    presfauna = models.CharField(max_length=255, default="", blank=True, null=True)
    infleletro = models.CharField(max_length=255, default="", blank=True, null=True)
    radsolar = models.CharField(max_length=255, default="", blank=True, null=True)
    descatm = models.CharField(max_length=255, default="", blank=True, null=True)
    movdoar = models.CharField(max_length=255, default="", blank=True, null=True)
    vento = models.CharField(max_length=255, default="", blank=True, null=True)
    competencia = models.CharField(max_length=255, default="", blank=True, null=True)
    reseletr = models.CharField(max_length=255, default="", blank=True, null=True)
    contpessoas = models.CharField(max_length=255, default="", blank=True, null=True)
    condfuga = models.CharField(max_length=255, default="", blank=True, null=True)
    natmatpr = models.CharField(max_length=255, default="", blank=True, null=True)
    natmatcons = models.CharField(max_length=255, default="", blank=True, null=True)
    classestr = models.CharField(max_length=255, default="", blank=True, null=True)

    # Campos da Avaliação qualitativa da instalação elétrica.
    documentacao = models.CharField(max_length=255, default="", blank=True, null=True)
    ambientesofreu = models.CharField(max_length=255, default="", blank=True, null=True)
    instalacaoinspecionada = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    linhaseletricasdisp = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    compinstalacao = models.CharField(max_length=255, default="", blank=True, null=True)
    linhaseletricascorr = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    tomadasdeforca = models.CharField(max_length=255, default="", blank=True, null=True)
    qtdesufitomadas = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    instlquadist = models.CharField(max_length=255, default="", blank=True, null=True)
    novoscircuitos = models.CharField(max_length=255, default="", blank=True, null=True)
    advquadist = models.CharField(max_length=255, default="", blank=True, null=True)
    dispprotecaoident = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    protcircuitos = models.CharField(max_length=255, default="", blank=True, null=True)
    barramentoquadist = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    bitola = models.CharField(max_length=255, default="", blank=True, null=True)
    condutident = models.CharField(max_length=255, default="", blank=True, null=True)
    disjundif = models.CharField(max_length=255, default="", blank=True, null=True)
    dispprotecaosurtos = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    servseguranca = models.CharField(max_length=255, default="", blank=True, null=True)
    esqaterramento = models.CharField(max_length=255, default="", blank=True, null=True)
    reservadeenergia = models.CharField(
        max_length=255, default="", blank=True, null=True
    )
    fontseguranca = models.CharField(max_length=255, default="", blank=True, null=True)
    paralelismo = models.CharField(max_length=255, default="", blank=True, null=True)

    # Campos da Avaliação quantitativa da instalação elétrica.
    capbarramento = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    protgeral = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    protdr = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    protdps = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    vab = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    van = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    ia = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    vbc = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    vbn = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    ib = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    vca = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    vcn = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    ic = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    continuidade = models.CharField(max_length=255, default="", blank=True, null=True)
    resistencia = models.CharField(max_length=255, default="", blank=True, null=True)
    selvpelv = models.CharField(max_length=255, default="", blank=True, null=True)
    verificacao = models.CharField(max_length=255, default="", blank=True, null=True)
    ensaiodetensao = models.CharField(max_length=255, default="", blank=True, null=True)
    ensaiodefunc = models.CharField(max_length=255, default="", blank=True, null=True)

    def __str__(self):
        return self.local + " - " + str(self.data) + " - " + str(self.autor)


class Circuito(models.Model):
    rel_pai = models.ForeignKey(Relatorio, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=255, default="", blank=True, null=True)
    fase = models.CharField(max_length=255, default="", blank=True, null=True)
    disjuntor = models.CharField(max_length=255, default="", blank=True, null=True)
    descricao = models.CharField(max_length=255, default="", blank=True, null=True)
    condutor = models.CharField(max_length=255, default="", blank=True, null=True)
    corrente = models.CharField(max_length=255, default="", blank=True, null=True)

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
