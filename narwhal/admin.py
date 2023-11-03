from django.contrib import admin
from narwhal.models import Relatorio, Circuito, Imagem

class Relatorios(admin.ModelAdmin):
    list_display = (
    'autor',
    'data',
    'local',
    'temperatura',
    'clima',
    'responsaveis',
    'qualiprof',
    'riscos',
    'equipamentos',
    'sinalizacao',
    'desligamento',
    'integridade',
    'dialogo',
    'curso_nr',
    'conferido',
    'delimitar_area',
    'auxconces',
    'tensao',
    'aterramento',
    'altura',
    'cinto_seg',
    'requi_seg',
    'reavaliacao',
    'tempambiente',
    'condambiente',
    'altitude',
    'presagua',
    'pressolidos',
    'pressubst',
    'solmecanicas',
    'presmofo',
    'presfauna',
    'infleletro',
    'radsolar',
    'descatm',
    'movdoar',
    'vento',
    'competencia',
    'reseletr',
    'contpessoas',
    'condfuga',
    'natmatpr',
    'natmatcons',
    'classestr',
    'documentacao',
    'ambientesofreu',
    'instalacaoinspecionada',
    'linhaseletricasdisp',
    'compinstalacao',
    'linhaseletricascorr',
    'tomadasdeforca',
    'qtdesufitomadas',
    'instlquadist',
    'novoscircuitos',
    'advquadist',
    'dispprotecaoident',
    'protcircuitos',
    'barramentoquadist',
    'bitola',
    'condutident',
    'disjundif',
    'dispprotecaosurtos',
    'servseguranca',
    'esqaterramento',
    'reservadeenergia',
    'fontseguranca',
    'paralelismo',
    'capbarramento',
    'protgeral',
    'protdr',
    'protdps',
    'vab',
    'van',
    'ia',
    'vbc',
    'vbn',
    'ib',
    'vca',
    'vcn',
    'ic',
    'continuidade',
    'resistencia',
    'selvpelv',
    'verificacao',
    'ensaiodetensao',
    'ensaiodefunc',
  )
    list_filter = ('local', 'data', 'autor')
    search_fields = ('local', 'data', 'autor')
    list_per_page = 10


admin.site.register(Relatorio, Relatorios)

class Circuitos(admin.ModelAdmin):
    list_display = (
    'rel_pai',
    'modelo',
    'fase',
    'disjuntor',
    'descricao',
    'condutor',
    'corrente',
  )
    list_filter = ('rel_pai', 'modelo')
    search_fields = ('rel_pai', 'modelo', 'disjuntor')
    list_per_page = 10

admin.site.register(Circuito, Circuitos)

class Imagens(admin.ModelAdmin):
    list_display = (
    'rel_pai',
    'img',
  )
    list_filter = ('rel_pai',)
    search_fields = ('rel_pai',)
    list_per_page = 10

admin.site.register(Imagem, Imagens)
