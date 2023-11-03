import os
from io import BytesIO
from django.http import FileResponse
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from .models import Relatorio, Circuito, Imagem

def relatorio_exporta(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    circuitos = Circuito.objects.filter(rel_pai__pk=rel_id)
    imagens = Imagem.objects.filter(rel_pai__pk=rel_id)
    byte_io = BytesIO()
    base = settings.PROJECT_PATH
    doc = DocxTemplate(os.path.join(base, "narwhal/assets/template.docx"))
    context = { 
        'data':relatorio.data.strftime('%d/%m/%Y'),
        'hora':relatorio.data.strftime('%H:%M'),
        'local':relatorio.local,
        'temperatura':relatorio.temperatura,
        'clima':relatorio.clima,
        'responsaveis':relatorio.responsaveis,
        'qualificacao_profissional':relatorio.qualificacao_profissional, 
        'integridade':relatorio.integridade,
        'dialogo_seguranca':relatorio.dialogo_seguranca,
        'curso_nr':relatorio.curso_nr,
        'servico_conferido':relatorio.servico_conferido,
        'riscos_detectados': ', '.join(ast.literal_eval(relatorio.riscos_detectados)),
        'equipamentos': ', '.join(ast.literal_eval(relatorio.equipamentos)),
        'requer_desligamento_rede':relatorio.requer_desligamento_rede,
        'requer_sinalizacao': ', '.join(ast.literal_eval(relatorio.requer_sinalizacao)),
        'necessita_delimitar_area':relatorio.necessita_delimitar_area,
        'necessita_auxilio_concessionaria':relatorio.necessita_auxilio_concessionaria,
        'tensao':relatorio.tensao,
        'aterramento':relatorio.aterramento,
        'altura':relatorio.altura,
        'cinto_seg':relatorio.cinto_seg,
        'requi_seg':relatorio.requi_seg,
        'reavaliacao':relatorio.reavaliacao,
        'tempambiente' : relatorio.tempambiente,
        'condambiente' : relatorio.condambiente,
        'altitude' : relatorio.altitude,
        'presagua' : relatorio.presagua,
        'pressolidos' : relatorio.pressolidos,
        'pressubst' : relatorio.pressubst,
        'solmecanicas' : relatorio.solmecanicas,
        'presmofo' : relatorio.presmofo,
        'presfauna' : relatorio.presfauna,
        'infleletro' : relatorio.infleletro,
        'radsolar' : relatorio.radsolar,
        'descatm' : relatorio.descatm,
        'movdoar' : relatorio.movdoar,
        'vento' : relatorio.vento,
        'competencia' : relatorio.competencia,
        'reseletr' : relatorio.reseletr,
        'contpessoas' : relatorio.contpessoas,
        'condfuga' : relatorio.condfuga,
        'natmatpr' : relatorio.natmatpr,
        'natmatcons' : relatorio.natmatcons,
        'classestr' : relatorio.classestr,
        'documentacao':relatorio.documentacao.split(': '),
        'ambientesofreu':relatorio.ambientesofreu.split(': '),
        'instalacaoinspecionada':relatorio.instalacaoinspecionada.split(': '),
        'linhaseletricasdisp':relatorio.linhaseletricasdisp.split(': '),
        'compinstalacao':relatorio.compinstalacao.split(': '),
        'linhaseletricascorr':relatorio.linhaseletricascorr.split(': '),
        'tomadasdeforca':relatorio.tomadasdeforca.split(': '),
        'qtdesufitomadas':relatorio.qtdesufitomadas.split(': '),
        'instlquadist':relatorio.instlquadist.split(': '),
        'novoscircuitos':relatorio.novoscircuitos,
        'advquadist':relatorio.advquadist.split(': '),
        'dispprotecaoident':relatorio.dispprotecaoident.split(': '),
        'protcircuitos':relatorio.protcircuitos.split(': '),
        'barramentoquadist':relatorio.barramentoquadist.split(': '),
        'bitola':relatorio.bitola.split(': '),
        'condutident':relatorio.condutident.split(': '),
        'disjundif':relatorio.disjundif.split(': '),
        'dispprotecaosurtos':relatorio.dispprotecaosurtos.split(': '),
        'servseguranca':relatorio.servseguranca.split(': '),
        'esqaterramento':relatorio.esqaterramento,
        'reservadeenergia':relatorio.reservadeenergia.split(': '),
        'fontseguranca':relatorio.fontseguranca.split(': '),
        'paralelismo':relatorio.paralelismo.split(': '),
        'capbarramento':relatorio.capbarramento,
        'protgeral':relatorio.protgeral,
        'protdr':relatorio.protdr,
        'protdps':relatorio.protdps,
        'vab':relatorio.vab,
        'van':relatorio.van,
        'ia':relatorio.ia,
        'vbc':relatorio.vbc,
        'vbn':relatorio.vbn,
        'ib':relatorio.ib,
        'vca':relatorio.vca,
        'vcn':relatorio.vcn,
        'ic':relatorio.ic,
        'continuidade':relatorio.continuidade.split(': '),
        'resistencia':relatorio.resistencia.split(': '),
        'selvpelv':relatorio.selvpelv.split(': '),
        'verificacao':relatorio.verificacao.split(': '),
        'ensaiodetensao':relatorio.ensaiodetensao.split(': '),
        'ensaiodefunc':relatorio.ensaiodefunc.split(': '),
    }

    for i in range(len(circuitos)):
        numero = str(i)
        context.update({('circuito'+numero):circuitos[i].modelo})
        context.update({('fase'+numero):circuitos[i].fase})
        context.update({('disjuntor'+numero):circuitos[i].disjuntor})
        context.update({('descricao'+numero):circuitos[i].descricao})
        context.update({('condutor'+numero):circuitos[i].condutor})
        context.update({('corrente'+numero):circuitos[i].corrente})

    fotos = [InlineImage(doc, base + i.img.url, width = Mm(50)) for i in imagens]
    context.update({'imagens':fotos})

    doc.render(context)
    doc.save(byte_io)
    byte_io.seek(0)
    return FileResponse(byte_io, as_attachment=True, filename=f'generated_{rel_id}.docx')