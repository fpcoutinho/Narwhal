from rest_framework import serializers
from narwhal.models import Relatorio, Circuito, Imagem
from narwhal.validators import *


class CircuitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = ["modelo", "fase", "disjuntor", "descricao", "condutor", "corrente"]
        ordering = ["-id"]


class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = "__all__"
        ordering = ["-id"]


class RelatorioSerializer(serializers.ModelSerializer):
    imagens = ImagemSerializer(many=True, read_only=True)
    imagens_do_relatorio = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
        required=False,
    )
    circuitos = CircuitoSerializer(many=True, read_only=True)
    circuitos_do_relatorio = serializers.ListField(
        child=CircuitoSerializer(), write_only=True, required=False
    )

    class Meta:
        model = Relatorio
        fields = "__all__"
        ordering = ["-id"]

    def create(self, validated_data):
        imagens_data = []
        circuitos_data = []
        if "imagens_do_relatorio" in validated_data:
            imagens_data = validated_data.pop("imagens_do_relatorio")
        if "circuitos_do_relatorio" in validated_data:
            circuitos_data = validated_data.pop("circuitos_do_relatorio")
            print("Circuitos data: ")

        relatorio = Relatorio.objects.create(**validated_data)

        for imagem_data in imagens_data:
            Imagem.objects.create(rel_pai=relatorio, img=imagem_data)
        for circuito_data in circuitos_data:
            Circuito.objects.create(rel_pai=relatorio, **circuito_data)

        return relatorio

    # Validate fields
    def validate(self, data):
        if not validate_local(data["local"]):
            raise serializers.ValidationError(
                {
                    "local": "Local inválido. O nome do local deve seguir o padrão: BLOCO-Nº, por exemplo: CCHLA-301."
                }
            )
        if data.get("qualificacao_profissional"):
            if not validate_qualificacao_profissional(
                data["qualificacao_profissional"]
            ):
                raise serializers.ValidationError(
                    {
                        "qualificacao_profissional": "Qualificação profissional inválida. As opções são: Engenheiro Eletricista, Técnico Eletrotécnico, Eletricista e Aluno de curso profissionalizante."
                    }
                )
        if data.get("riscos_detectados"):
            if not validate_riscos_detectados(data["riscos_detectados"]):
                raise serializers.ValidationError(
                    {
                        "riscos_detectados": "Risco detectado inválido. As opções são: Queda, Explosão, Ergonômico, Animais Peçonhentos, Arco Voltaico, Atropelamento, Ruído e Choque."
                    }
                )

        if data.get("equipamentos"):
            if not validate_equipamentos(data["equipamentos"]):
                raise serializers.ValidationError(
                    {
                        "equipamentos": "Equipamento inválido. As opções são: Capacete, Manga Isolante, Botina Dielétrica, Luva de Cobertura, Óculos de Proteção, Protetor Auricular, Luva de Borracha Isolante e Cinto de Segurança."
                    }
                )

        if data.get("sinalizacao"):
            if not validate_sinalizacao(data["sinalizacao"]):
                raise serializers.ValidationError(
                    {
                        "sinalizacao": "Sinalização inválida. As opções são: Cone, Giroflex, Fita para Isolamento da área, Sinaleira Sonora, Cavaletes e Nenhum."
                    }
                )

        if data.get("tempambiente"):
            if not validate_tempambiente(data["tempambiente"]):
                raise serializers.ValidationError(
                    {
                        "tempambiente": "Temperatura ambiente inválida. As opções são: AA1 - Frigorífico (-60 ° a 5 °C), AA2 - Muito frio (-40 ° a 5 °C), AA3 - Frio (-25 ° a 5 °C), AA4 - Temperado (-5 ° a 40 °C), AA5 - Quente (5 ° a 40 °C), AA6 - Muito quente (5 ° a 60 °C), AA7 - Extrema (-25 ° a 55 °C) e AA8 - (-50 ° a 40 °C)."
                    }
                )
        if data.get("condambiente"):
            if not validate_condambiente(data["condambiente"]):
                raise serializers.ValidationError(
                    {
                        "condambiente": "Condição do ambiente inválida. As opções são: AB1 - Ambientes internos e externos com temperaturas extremamente baixas, AB2 - Ambientes internos e externos com temperaturas baixas, AB3 - Ambientes internos e externos com temperaturas baixas, AB4 - Locais abrigados sem controle da temperatura e da umidade. Uso de calefação possível, AB5 - Locais abrigados com temperatura ambiente controlada, AB6 - Ambientes internos e externos com temperaturas extremamente altas, protegidos contra baixas temperaturas ambientes. Ocorrência de radiação solar e de calor., AB7 - Ambientes internos e abrigados sem controle da temperatura e da umidade. Podem ter aberturas para o exterior e são sujeitos a radiação solar e AB8 - Ambientes externos e sem proteção contra intempéries, sujeitos a altas e baixas temperaturas."
                    }
                )

        if data.get("altitude"):
            if not validate_altitude(data["altitude"]):
                raise serializers.ValidationError(
                    {
                        "altitude": "Altitude inválida. As opções são: AC1 Baixa ( ≤ 2000 m ) e AC2 Alta ( > 2000 m )."
                    }
                )

        if data.get("presagua"):
            if not validate_presagua(data["presagua"]):
                raise serializers.ValidationError(
                    {
                        "presagua": "Presença de água inválida. As opções são: AD1 Desprezível, AD2 Gotejamento, AD3 Precipitação, AD4 Aspersão, AD5 Jatos, AD6 Ondas, AD7 Imersão e AD8 Submersão."
                    }
                )

        if data.get("pressolidos"):
            if not validate_pressolidos(data["pressolidos"]):
                raise serializers.ValidationError(
                    {
                        "pressolidos": "Presença de corpos sólidos inválida. As opções são: AE1 Desprezível, AE2 Pequenos objetos, AE3 Objetos muito pequenos, AE4 Poeira leve, AE5 Poeira moderada e AE6 Poeira intensa."
                    }
                )

        if data.get("pressubst"):
            if not validate_pressubst(data["pressubst"]):
                raise serializers.ValidationError(
                    {
                        "pressubst": "Presença de substâncias corrosivas ou poluentes inválida. As opções são: AF1 Desprezível, AF2 Atmosférica, AF3 Intermitente ou acidental e AF4 Permanente."
                    }
                )

        if data.get("solmecanicas"):
            if not validate_solmecanicas(data["solmecanicas"]):
                raise serializers.ValidationError(
                    {
                        "solmecanicas": "Solicitações mecânicas inválidas. As opções são: AG1 Impactos fracos, AG2 Impactos médios, AG3 Impactos severos, AH1 Vibrações fracas, AH2 Vibrações médias e AH3 Vibrações severas."
                    }
                )

        if data.get("presmofo"):
            if not validate_presmofo(data["presmofo"]):
                raise serializers.ValidationError(
                    {
                        "presmofo": "Presença de flora e mofo inválida. As opções são: AK1 Desprezível ou AK2 Prejudicial"
                    }
                )

        if data.get("presfauna"):
            if not validate_presfauna(data["presfauna"]):
                raise serializers.ValidationError(
                    {
                        "presfauna": "Presença de fauna inválida. As opções são: AL1 Desprezível ou AL2 Prejudicial"
                    }
                )

        if data.get("infleletro"):
            if not validate_infleletro(data["infleletro"]):
                raise serializers.ValidationError(
                    {
                        "infleletro": "Influências eletromagnéticas, eletrostáticas ou ionizantes inválidas."
                    }
                )

        if data.get("radsolar"):
            if not validate_radsolar(data["radsolar"]):
                raise serializers.ValidationError(
                    {
                        "radsolar": "Radiação solar inválida. As opções são: AN1 Desprezível, AN2 Média, AN3 Alta."
                    }
                )

        if data.get("descatm"):
            if not validate_descatm(data["descatm"]):
                raise serializers.ValidationError(
                    {
                        "descatm": "Descargas atmosféricas inválidas. As opções são: AQ1 Desprezíveis, AQ2 Indiretas, AQ3 Diretas."
                    }
                )

        if data.get("movdoar"):
            if not validate_movdoar(data["movdoar"]):
                raise serializers.ValidationError(
                    {
                        "movdoar": "Movimentação do ar inválida. As opções são: AR1 Desprezível, AR2 Média, AR3 Forte."
                    }
                )

        if data.get("vento"):
            if not validate_vento(data["vento"]):
                raise serializers.ValidationError(
                    {
                        "vento": "Vento inválido. As opções são: AS1 Desprezível, AS2 Médio, AS3 Forte."
                    }
                )

        if data.get("competencia"):
            if not validate_competencia(data["competencia"]):
                raise serializers.ValidationError(
                    {
                        "competencia": "Competência das pessoas inválida. As opções são: BA1 Comuns, BA2 Crianças, BA3 Incapacitadas, BA4 Advertidas, BA5 Qualificadas."
                    }
                )

        if data.get("reseletr"):
            if not validate_reseletr(data["reseletr"]):
                raise serializers.ValidationError(
                    {
                        "reseletr": "Resistência elétrica do corpo humano no ambiente inválida. As opções são: BB1 Alta, BB2 Normal, BB3 Baixa, BB4 Muito baixa."
                    }
                )

        if data.get("contpessoas"):
            if not validate_contpessoas(data["contpessoas"]):
                raise serializers.ValidationError(
                    {
                        "contpessoas": "Contato das pessoas com o potencial da terra inválido. As opções são: BC1 Nulo, BC2 Raro, BC3 Frequente, BC4 Contínuo."
                    }
                )

        if data.get("condfuga"):
            if not validate_condfuga(data["condfuga"]):
                raise serializers.ValidationError(
                    {
                        "condfuga": "Condições de fuga das pessoas em emergências inválidas. As opções são: BD1 Normal, BD2 Longa, BD3 Tumultuada, BD4 Longa e tumultuada."
                    }
                )

        if data.get("natmatpr"):
            if not validate_natmatpr(data["natmatpr"]):
                raise serializers.ValidationError(
                    {
                        "natmatpr": "Natureza dos materiais processados ou armazenados inválida. As opções são: BE1 Riscos desprezíveis, BE2 Riscos de incêndio, BE3 Riscos de explosão, BE4 Riscos de contaminação."
                    }
                )

        if data.get("natmatcons"):
            if not validate_natmatcons(data["natmatcons"]):
                raise serializers.ValidationError(
                    {
                        "natmatcons": "Natureza dos materiais de construção inválida. As opções são: CA1 Não combustíveis, CA2 Combustíveis."
                    }
                )

        if data.get("classestr"):
            if not validate_classestr(data["classestr"]):
                raise serializers.ValidationError(
                    {
                        "classestr": "Classificação da estrutura das edificações inválida. As opções são: CB1 Riscos desprezíveis, CB2 Sujeitas a propagação de incêndio, CB3 Sujeitas a movimentação, CB4 Flexíveis ou instáveis."
                    }
                )

        return data


class ListaImagensPorRelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ["id", "img"]


class ListaCircuitosPorRelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = [
            "id",
            "modelo",
            "fase",
            "disjuntor",
            "descricao",
            "condutor",
            "corrente",
        ]
