import re


# Validate fields
def validate_local(local):
    regex = r"[A-Z]{2,}-[A-Z]{0,}[0-9]{2,}"
    return re.match(regex, local)


def validate_qualificacao_profissional(qualificacao_profissional):
    quali = [
        "Engenheiro Eletricista",
        "Técnico Eletrotécnico",
        "Eletricista",
        "Aluno de curso profissionalizante",
    ]
    return qualificacao_profissional in quali


def validate_riscos_detectados(riscos_detectados):
    risk = [
        "Queda",
        "Explosão",
        "Ergonômico",
        "Animais Peçonhentos",
        "Arco Voltaico",
        "Atropelamento",
        "Ruído",
        "Choque",
    ]
    riscos_list = riscos_detectados.split(", ")
    for r in riscos_list:
        if r not in risk:
            return False
    return True


def validate_equipamentos(equipamentos):
    eqp = [
        "Capacete",
        "Manga Isolante",
        "Botina Dielétrica",
        "Luva de Cobertura",
        "Óculos de Proteção",
        "Protetor Auricular",
        "Luva de Borracha Isolante",
        "Cinto de Segurança",
    ]
    eqp_list = equipamentos.split(", ")
    for e in eqp_list:
        if e not in eqp:
            return False
    return True


def validate_sinalizacao(sinalizacao):
    silz = [
        "Cone",
        "Giroflex",
        "Fita para Isolamento da área",
        "Sinaleira Sonora",
        "Cavaletes",
        "Nenhum",
    ]
    silz_list = sinalizacao.split(", ")
    for s in silz_list:
        if s not in silz:
            return False
    return True


def validate_tempambiente(tempambiente):
    tempambiente_choices = [
        "AA1 - Frigorífico (-60 ° a 5 °C)",
        "AA2 - Muito frio (-40 ° a 5 °C)",
        "AA3 - Frio (-25 ° a 5 °C)",
        "AA4 - Temperado (-5 ° a 40 °C)",
        "AA5 - Quente (5 ° a 40 °C)",
        "AA6 - Muito quente (5 ° a 60 °C)",
        "AA7 - Extrema (-25 ° a 55 °C)",
        "AA8 - (-50 ° a 40 °C)",
    ]
    return tempambiente in tempambiente_choices


def validate_condambiente(condambiente):
    condambiente_choices = [
        "AB1 - Ambientes internos e externos com temperaturas extremamente baixas",
        "AB2 - Ambientes internos e externos com temperaturas baixas",
        "AB3 - Ambientes internos e externos com temperaturas baixas",
        "AB4 - Locais abrigados sem controle da temperatura e da umidade. Uso de calefação possível",
        "AB5 - Locais abrigados com temperatura ambiente controlada",
        "AB6 - Ambientes internos e externos com temperaturas extremamente altas, protegidos contra baixas temperaturas ambientes. Ocorrência de radiação solar e de calor.",
        "AB7 - Ambientes internos e abrigados sem controle da temperatura e da umidade. Podem ter aberturas para o exterior e são sujeitos a radiação solar.",
        "AB8 - Ambientes externos e sem proteção contra intempéries, sujeitos a altas e baixas temperaturas",
    ]
    return condambiente in condambiente_choices


def validate_altitude(altitude):
    altitude_choices = ["AC1 Baixa ( ≤ 2000 m )", "AC2 Alta ( > 2000 m )"]
    return altitude in altitude_choices


def validate_presagua(presagua):
    presagua_choices = [
        "AD1 Desprezível",
        "AD2 Gotejamento",
        "AD3 Precipitação",
        "AD4 Aspersão",
        "AD5 Jatos",
        "AD6 Ondas",
        "AD7 Imersão",
        "AD8 Submersão",
    ]
    return presagua in presagua_choices


def validate_pressolidos(pressolidos):
    pressolidos_choices = [
        "AE1 Desprezível",
        "AE2 Pequenos objetos",
        "AE3 Objetos muito pequenos",
        "AE4 Poeira leve",
        "AE5 Poeira moderada",
        "AE6 Poeira intensa",
    ]
    return pressolidos in pressolidos_choices


def validate_pressubst(pressubst):
    pressubst_choices = [
        "AF1 Desprezível",
        "AF2 Atmosférica",
        "AF3 Intermitente ou acidental",
        "AF4 Permanente",
    ]
    return pressubst in pressubst_choices


def validate_solmecanicas(solmecanicas):
    solmecanicas_choices = [
        "AG1 Impactos fracos",
        "AG2 Impactos médios",
        "AG3 Impactos severos",
        "AH1 Vibrações fracas",
        "AH2 Vibrações médias",
        "AH3 Vibrações severas",
    ]
    return solmecanicas in solmecanicas_choices


def validate_presmofo(presmofo):
    presmofo_choices = ["AK1 Desprezível", "AK2 Prejudicial"]
    return presmofo in presmofo_choices


def validate_presfauna(presfauna):
    presfauna_choices = ["AL1 Desprezível", "AL2 Prejudicial"]
    return presfauna in presfauna_choices


def validate_infleletro(infleletro):
    infleletro_choices = [
        "AM1-1 Harmônicas e inter-harmonicas nível controlado",
        "AM1-2 Harmônicas e inter-harmonicas nível normal",
        "AM1-3 Harmônicas e inter-harmonicas nível alto",
        "AM2-1 Tensões de sinalização nível controlado",
        "AM2-2 Tensões de sinalização nível normal",
        "AM2-3 Tensões de sinalização nível alto",
        "AM3-1 Variação de amplitude da tensão nível controlado",
        "AM3-2 Variação de amplitude da tensão nível controlado",
        "AM4 Desequilíbrio de tensão",
        "AM5 Variações de frequência",
        "AM6 Tensões induzidas de baixa frequência",
        "AM7 Componentes contínuas em redes C.A.",
        "AM8-1 Campos magnéticos radiados nível médio (linhas de energia, transformadores, equipamentos de frequência industrial e suas harmônicas)",
        "AM8-2 Campos magnéticos radiados nível alto (grande proximidade dos itens mencionados em AM8-1)",
        "AM9-1 Campo elétrico nível desprezível",
        "AM9-2 Campo elétrico nível médio",
        "AM9-3 Campo elétrico nível alto",
        "AM9-4 Campo elétrico nível muito alto",
        "AM21 perturbações de modo comum geradas por campos eletromagnéticos modulados em AM ou FM",
        "AM22-1 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível desprezível",
        "AM22-2 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível médio",
        "AM22-3 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível alto",
        "AM22-4 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível muito alto",
        "AM23-1 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível controlado",
        "AM23-2 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível médio",
        "AM23-3 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível alto",
        "AM24-1 Transitórios oscilantes conduzidos nível médio",
        "AM24-2 Transitórios oscilantes conduzidos nível alto",
        "AM25-1 Fenômenos radiados de alta frequência nível desprezível",
        "AM25-2 Fenômenos radiados de alta frequência nível médio",
        "AM25-3 Fenômenos radiados de alta frequência nível alto",
        "AM31-1 Descargas eletrostáticas nível baixo",
        "AM31-2 Descargas eletrostáticas nível médio",
        "AM31-3 Descargas eletrostáticas nível alto",
        "AM31-4 Descargas eletrostáticas nível muito alto",
        "AM41-1 Radiações ionizantes perigosas",
    ]
    return infleletro in infleletro_choices


def validate_radsolar(radsolar):
    radsolar_choices = ["AN1 Desprezível", "AN2 Média", "AN3 Alta"]
    return radsolar in radsolar_choices


def validate_descatm(descatm):
    descatm_choices = ["AQ1 Desprezíveis", "AQ2 Indiretas", "AQ3 Diretas"]
    return descatm in descatm_choices


def validate_movdoar(movdoar):
    movdoar_choices = ["AR1 Desprezível", "AR2 Média", "AR3 Forte"]
    return movdoar in movdoar_choices


def validate_vento(vento):
    vento_choices = ["AS1 Desprezível", "AS2 Médio", "AS3 Forte"]
    return vento in vento_choices


def validate_competencia(competencia):
    competencia_choices = [
        "BA1 Comuns",
        "BA2 Crianças",
        "BA3 Incapacitadas",
        "BA4 Advertidas",
        "BA5 Qualificadas",
    ]
    return competencia in competencia_choices


def validate_reseletr(reseletr):
    reseletr_choices = ["BB1 Alta", "BB2 Normal", "BB3 Baixa", "BB4 Muito baixa"]
    return reseletr in reseletr_choices


def validate_contpessoas(contpessoas):
    contpessoas_choices = ["BC1 Nulo", "BC2 Raro", "BC3 Frequente", "BC4 Contínuo"]
    return contpessoas in contpessoas_choices


def validate_condfuga(condfuga):
    condfuga_choices = [
        "BD1 Normal",
        "BD2 Longa",
        "BD3 Tumultuada",
        "BD4 Longa e tumultuada",
    ]
    return condfuga in condfuga_choices


def validate_natmatpr(natmatpr):
    natmatpr_choices = [
        "BE1 Riscos desprezíveis",
        "BE2 Riscos de incêndio",
        "BE3 Riscos de explosão",
        "BE4 Riscos de contaminação",
    ]
    return natmatpr in natmatpr_choices


def validate_natmatcons(natmatcons):
    natmatcons_choices = ["CA1 Não combustíveis", "CA2 Combustíveis"]
    return natmatcons in natmatcons_choices


def validate_classestr(classestr):
    classestr_choices = [
        "CB1 Riscos desprezíveis",
        "CB2 Sujeitas a propagação de incêndio",
        "CB3 Sujeitas a movimentação",
        "CB4 Flexíveis ou instáveis",
    ]
    return classestr in classestr_choices
