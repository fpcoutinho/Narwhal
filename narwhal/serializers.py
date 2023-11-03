from rest_framework import serializers
import re
from .models import Relatorio, Circuito, Imagem

class CircuitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = ['modelo', 'fase', 'disjuntor', 'descricao', 'condutor', 'corrente']

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'

class RelatorioSerializer(serializers.ModelSerializer):
    imagens = ImagemSerializer(many=True, read_only=True)
    imagens_do_relatorio = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )
    circuitos = CircuitoSerializer(many=True, read_only=True)
    circuitos_do_relatorio = serializers.ListField(
        child=CircuitoSerializer(),
        write_only=True,
        required=False
    )
    class Meta:
        model = Relatorio
        fields = '__all__'
    
    def create(self, validated_data):
        imagens_data = []
        circuitos_data = []
        if 'imagens_do_relatorio' in validated_data:
            imagens_data = validated_data.pop('imagens_do_relatorio')
        if 'circuitos_do_relatorio' in validated_data:
            circuitos_data = validated_data.pop('circuitos_do_relatorio')
            print("Circuitos data: ")

        relatorio = Relatorio.objects.create(**validated_data)

        for imagem_data in imagens_data:
            Imagem.objects.create(rel_pai=relatorio, img=imagem_data)
        for circuito_data in circuitos_data:
            Circuito.objects.create(rel_pai=relatorio, **circuito_data)

        return relatorio
    
    # Validate fields
    def validate_local(self, local):
        regex = r"[A-Z]{2,}-[A-Z]{0,}[0-9]{2,}"
        if not re.match(regex, local):
            raise serializers.ValidationError("Local inválido. O nome do local deve seguir o padrão: BLOCO-Nº, por exemplo: CCHLA-301.")
        return local
    
    def validate_qualificacao_profissional(self, qualificacao_profissional):
        quali = ['Engenheiro Eletricista', 'Técnico Eletrotécnico', 'Eletricista', 'Aluno de curso profissionalizante']
        if qualificacao_profissional not in quali:
            raise serializers.ValidationError("Qualificação profissional inválida. As opções são: Engenheiro Eletricista, Técnico Eletrotécnico, Eletricista e Aluno de curso profissionalizante.")
        return qualificacao
    
    def validate_riscos_detectados(self, riscos_detectados):
        risk = ['Queda', 'Explosão', 'Ergonômico', 'Animais Peçonhentos', 'Arco Voltaico', 'Atropelamento', 'Ruído', 'Choque']
        if riscos_detectados not in risk:
            raise serializers.ValidationError("Risco detectado inválido. As opções são: Queda, Explosão, Ergonômico, Animais Peçonhentos, Arco Voltaico, Atropelamento, Ruído e Choque.")
        return riscos_detectados
    
    def validate_equipamentos(self, equipamentos):
        eqp = ['Capacete', 'Manga Isolante', 'Botina Dielétrica', 'Luva de Cobertura', 'Óculos de Proteção', 'Protetor Auricular', 'Luva de Borracha Isolante', 'Cinto de Segurança']
        if equipamentos not in eqp:
            raise serializers.ValidationError("Equipamento inválido. As opções são: " + ', '.join(eqp) + ".")
        return equipamentos

    def validate_sinalizacao(self, sinalizacao):
        silz = ['Cone', 'Giroflex', 'Fita para Isolamento da área', 'Sinaleira Sonora', 'Cavaletes', 'Nenhum']
        if sinalizacao not in silz:
            raise serializers.ValidationError("Sinalização inválida. As opções são: " + ', '.join(silz) + ".")
        return sinalizacao
    
    def validate_tempambiente(self, tempambiente):
        tempambiente_choices = [
            'AA1 - Frigorífico (-60 ° a 5 °C)',
            'AA2 - Muito frio (-40 ° a 5 °C)',
            'AA3 - Frio (-25 ° a 5 °C)',
            'AA4 - Temperado (-5 ° a 40 °C)',
            'AA5 - Quente (5 ° a 40 °C)',
            'AA6 - Muito quente (5 ° a 60 °C)',
            'AA7 - Extrema (-25 ° a 55 °C)',
            'AA8 - (-50 ° a 40 °C)'
        ]
        
        if tempambiente not in tempambiente_choices:
            raise serializers.ValidationError("Temperatura ambiente inválida. As opções são: " + ', '.join(tempambiente_choices) + ".")
        
        return tempambiente

    def validate_condambiente(self, condambiente):
        condambiente_choices = [
            'AB1 - Ambientes internos e externos com temperaturas extremamente baixas',
            'AB2 - Ambientes internos e externos com temperaturas baixas',
            'AB3 - Ambientes internos e externos com temperaturas baixas',
            'AB4 - Locais abrigados sem controle da temperatura e da umidade. Uso de calefação possível',
            'AB5 - Locais abrigados com temperatura ambiente controlada',
            'AB6 - Ambientes internos e externos com temperaturas extremamente altas, protegidos contra baixas temperaturas ambientes. Ocorrência de radiação solar e de calor.',
            'AB7 - Ambientes internos e abrigados sem controle da temperatura e da umidade. Podem ter aberturas para o exterior e são sujeitos a radiação solar.',
            'AB8 - Ambientes externos e sem proteção contra intempéries, sujeitos a altas e baixas temperaturas'
        ]
        
        if condambiente not in condambiente_choices:
            raise serializers.ValidationError("Condição do ambiente inválida. As opções são: " + ', '.join(condambiente_choices) + ".")
        
        return condambiente
        
    def validate_altitude(self, altitude):
        altitude_choices = ['AC1 Baixa ( ≤ 2000 m )', 'AC2 Alta ( > 2000 m )']
        if altitude not in altitude_choices:
            raise serializers.ValidationError("Altitude inválida. As opções são: " + ', '.join(altitude_choices) + ".")
        return altitude

    def validate_presagua(self, presagua):
        presagua_choices = ['AD1 Desprezível', 'AD2 Gotejamento', 'AD3 Precipitação', 'AD4 Aspersão', 'AD5 Jatos', 'AD6 Ondas', 'AD7 Imersão', 'AD8 Submersão']
        if presagua not in presagua_choices:
            raise serializers.ValidationError("Presença de água inválida. As opções são: " + ', '.join(presagua_choices) + ".")
        return presagua

    def validate_pressolidos(self, pressolidos):
        pressolidos_choices = ['AE1 Desprezível', 'AE2 Pequenos objetos', 'AE3 Objetos muito pequenos', 'AE4 Poeira leve', 'AE5 Poeira moderada', 'AE6 Poeira intensa']
        if pressolidos not in pressolidos_choices:
            raise serializers.ValidationError("Presença de corpos sólidos inválida. As opções são: " + ', '.join(pressolidos_choices) + ".")
        return pressolidos

    def validate_pressubst(self, pressubst):
        pressubst_choices = ['AF1 Desprezível', 'AF2 Atmosférica', 'AF3 Intermitente ou acidental', 'AF4 Permanente']
        if pressubst not in pressubst_choices:
            raise serializers.ValidationError("Presença de substâncias corrosivas ou poluentes inválida. As opções são: " + ', '.join(pressubst_choices) + ".")
        return pressubst

    def validate_solmecanicas(self, solmecanicas):
        solmecanicas_choices = ['AG1 Impactos fracos', 'AG2 Impactos médios', 'AG3 Impactos severos', 'AH1 Vibrações fracas', 'AH2 Vibrações médias', 'AH3 Vibrações severas']
        if solmecanicas not in solmecanicas_choices:
            raise serializers.ValidationError("Solicitações mecânicas inválidas. As opções são: " + ', '.join(solmecanicas_choices) + ".")
        return solmecanicas

    def validate_presmofo(self, presmofo):
        presmofo_choices = ['AK1 Desprezível', 'AK2 Prejudicial']
        if presmofo not in presmofo_choices:
            raise serializers.ValidationError("Presença de flora e mofo inválida. As opções são: " + ', '.join(presmofo_choices) + ".")
        return presmofo

    def validate_presfauna(self, presfauna):
        presfauna_choices = ['AL1 Desprezível', 'AL2 Prejudicial']
        if presfauna not in presfauna_choices:
            raise serializers.ValidationError("Presença de fauna inválida. As opções são: " + ', '.join(presfauna_choices) + ".")
        return presfauna

    def validate_infleletro(self, infleletro):
        infleletro_choices = [
            'AM1-1 Harmônicas e inter-harmonicas nível controlado',
            'AM1-2 Harmônicas e inter-harmonicas nível normal',
            'AM1-3 Harmônicas e inter-harmonicas nível alto',
            'AM2-1 Tensões de sinalização nível controlado',
            'AM2-2 Tensões de sinalização nível normal',
            'AM2-3 Tensões de sinalização nível alto',
            'AM3-1 Variação de amplitude da tensão nível controlado',
            'AM3-2 Variação de amplitude da tensão nível controlado',
            'AM4 Desequilíbrio de tensão',
            'AM5 Variações de frequência',
            'AM6 Tensões induzidas de baixa frequência',
            'AM7 Componentes contínuas em redes C.A.',
            'AM8-1 Campos magnéticos radiados nível médio (linhas de energia, transformadores, equipamentos de frequência industrial e suas harmônicas)',
            'AM8-2 Campos magnéticos radiados nível alto (grande proximidade dos itens mencionados em AM8-1)',
            'AM9-1 Campo elétrico nível desprezível',
            'AM9-2 Campo elétrico nível médio',
            'AM9-3 Campo elétrico nível alto',
            'AM9-4 Campo elétrico nível muito alto',
            'AM21 perturbações de modo comum geradas por campos eletromagnéticos modulados em AM ou FM',
            'AM22-1 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível desprezível',
            'AM22-2 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível médio',
            'AM22-3 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível alto',
            'AM22-4 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível muito alto',
            'AM23-1 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível controlado',
            'AM23-2 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível médio',
            'AM23-3 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível alto',
            'AM24-1 Transitórios oscilantes conduzidos nível médio',
            'AM24-2 Transitórios oscilantes conduzidos nível alto',
            'AM25-1 Fenômenos radiados de alta frequência nível desprezível',
            'AM25-2 Fenômenos radiados de alta frequência nível médio',
            'AM25-3 Fenômenos radiados de alta frequência nível alto',
            'AM31-1 Descargas eletrostáticas nível baixo',
            'AM31-2 Descargas eletrostáticas nível médio',
            'AM31-3 Descargas eletrostáticas nível alto',
            'AM31-4 Descargas eletrostáticas nível muito alto',
            'AM41-1 Radiações ionizantes perigosas'
        ]
        if infleletro not in infleletro_choices:
            raise serializers.ValidationError("Influências eletromagnéticas, eletrostáticas ou ionizantes inválidas. As opções são: " + ', '.join(infleletro_choices) + ".")
        return infleletro

    def validate_radsolar(self, radsolar):
        radsolar_choices = ['AN1 Desprezível', 'AN2 Média', 'AN3 Alta']
        if radsolar not in radsolar_choices:
            raise serializers.ValidationError("Radiação solar inválida. As opções são: " + ', '.join(radsolar_choices) + ".")
        return radsolar

    def validate_descatm(self, descatm):
        descatm_choices = ['AQ1 Desprezíveis', 'AQ2 Indiretas', 'AQ3 Diretas']
        if descatm not in descatm_choices:
            raise serializers.ValidationError("Descargas atmosféricas inválidas. As opções são: " + ', '.join(descatm_choices) + ".")
        return descatm

    def validate_movdoar(self, movdoar):
        movdoar_choices = ['AR1 Desprezível', 'AR2 Média', 'AR3 Forte']
        if movdoar not in movdoar_choices:
            raise serializers.ValidationError("Movimentação do ar inválida. As opções são: " + ', '.join(movdoar_choices) + ".")
        return movdoar

    def validate_vento(self, vento):
        vento_choices = ['AS1 Desprezível', 'AS2 Médio', 'AS3 Forte']
        if vento not in vento_choices:
            raise serializers.ValidationError("Vento inválido. As opções são: " + ', '.join(vento_choices) + ".")
        return vento

    def validate_competencia(self, competencia):
        competencia_choices = ['BA1 Comuns', 'BA2 Crianças', 'BA3 Incapacitadas', 'BA4 Advertidas', 'BA5 Qualificadas']
        if competencia not in competencia_choices:
            raise serializers.ValidationError("Competência das pessoas inválida. As opções são: " + ', '.join(competencia_choices) + ".")
        return competencia

    def validate_reseletr(self, reseletr):
        reseletr_choices = ['BB1 Alta', 'BB2 Normal', 'BB3 Baixa', 'BB4 Muito baixa']
        if reseletr not in reseletr_choices:
            raise serializers.ValidationError("Resistência elétrica do corpo humano no ambiente inválida. As opções são: " + ', '.join(reseletr_choices) + ".")
        return reseletr

    def validate_contpessoas(self, contpessoas):
        contpessoas_choices = ['BC1 Nulo', 'BC2 Raro', 'BC3 Frequente', 'BC4 Contínuo']
        if contpessoas not in contpessoas_choices:
            raise serializers.ValidationError("Contato das pessoas com o potencial da terra inválido. As opções são: " + ', '.join(contpessoas_choices) + ".")
        return contpessoas

    def validate_condfuga(self, condfuga):
        condfuga_choices = ['BD1 Normal', 'BD2 Longa', 'BD3 Tumultuada', 'BD4 Longa e tumultuada']
        if condfuga not in condfuga_choices:
            raise serializers.ValidationError("Condições de fuga das pessoas em emergências inválidas. As opções são: " + ', '.join(condfuga_choices) + ".")
        return condfuga

    def validate_natmatpr(self, natmatpr):
        natmatpr_choices = ['BE1 Riscos desprezíveis', 'BE2 Riscos de incêndio', 'BE3 Riscos de explosão', 'BE4 Riscos de contaminação']
        if natmatpr not in natmatpr_choices:
            raise serializers.ValidationError("Natureza dos materiais processados ou armazenados inválida. As opções são: " + ', '.join(natmatpr_choices) + ".")
        return natmatpr

    def validate_natmatcons(self, natmatcons):
        natmatcons_choices = ['CA1 Não combustíveis', 'CA2 Combustíveis']
        if natmatcons not in natmatcons_choices:
            raise serializers.ValidationError("Natureza dos materiais de construção inválida. As opções são: " + ', '.join(natmatcons_choices) + ".")
        return natmatcons

    def validate_classestr(self, classestr):
        classestr_choices = ['CB1 Riscos desprezíveis', 'CB2 Sujeitas a propagação de incêndio', 'CB3 Sujeitas a movimentação', 'CB4 Flexíveis ou instáveis']
        if classestr not in classestr_choices:
            raise serializers.ValidationError("Classificação da estrutura das edificações inválida. As opções são: " + ', '.join(classestr_choices) + ".")
        return classestr

class ListaImagensPorRelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'img']

class ListaCircuitosPorRelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = ['id', 'modelo', 'fase', 'disjuntor', 'descricao', 'condutor', 'corrente']