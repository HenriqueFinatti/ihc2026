"""Mapa de objetivos da P01 (Rafael) a partir do CI01 (Entrega 9, Tiago).
Texto correspondente: docs/09_modelo_conceitual.md, seções 2.1 (tópicos e subtópicos) e 3.1."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/09_modelo_conceitual/mapa_objetivos_ci01.svg"

s = Svg("Mapa de objetivos — P01, Rafael Pereira (CI01)",
        "Mapa de objetivos individual por Tiago Fagundes dos Santos. Objetivo geral da P01, dois objetivos, "
        "os tópicos de conversa da seção 2.1 da Entrega 9 e seus subtópicos. Caixas tracejadas são "
        "objetivos alcançados fora do sistema.")
s.header("Mapa de objetivos — P01, Rafael Pereira (CI01)",
         "Tiago Fagundes dos Santos · 22.123.017-0 · origem: C01 → CI01 · T01, T02 e T03 · Proposta [H]")

y = s.section(100, "Visão geral")
y = s.tree(N(["Dizer à equipe, antes do próximo teste,", "se a configuração em uso pode continuar"]),
           [N(["A. Validar a segmentação", "das imagens do teste"]),
            N(["B. Concluir o que dizer", "à equipe"])],
           y, 200, 1240, gap=80, pw=600) + 20

y = s.section(y, "Objetivo A — validar a segmentação das imagens do teste (T02 e T01)")
y = s.tree(N(["A. Validar a segmentação das imagens do teste"]),
           [N(["A1. Obter as imagens", "do teste"], dashed=True),
            N(["A2. Executar a", "segmentação das", "imagens do teste"]),
            N(["A3. Avaliar a", "segmentação de", "cada imagem"])],
           y, 160, 1280, gap=40, pw=600) + 20

y = s.section(y, "Objetivo B — concluir o que dizer à equipe (T03)")
y = s.tree(N(["B. Concluir o que dizer à equipe"]),
           [N(["B1. Comparar com", "outra configuração"]),
            N(["B2. Registrar a", "conclusão da", "validação"]),
            N(["B3. Informar o", "grupo da equipe"], dashed=True)],
           y, 160, 1280, gap=40, pw=560) + 20

y = s.section(y, "Desdobramento dos tópicos em subtópicos")
ya = s.tree(N(["A2. Executar a segmentação", "das imagens do teste"]),
            [N(["A2.1. Enviar as", "imagens e escolher", "a configuração"]),
             N(["A2.2. Acompanhar o", "processamento"])],
            y, 40, 640, gap=30, pw=440)
yb = s.tree(N(["A3. Avaliar a segmentação", "de cada imagem"]),
            [N(["A3.1. Ver o", "resultado sobre", "a imagem"]),
             N(["A3.2. Conferir se", "há métricas"]),
             N(["A3.3. Registrar a", "avaliação da", "imagem"])],
            y, 700, 1400, gap=24, pw=460)
y = max(ya, yb) + 20
y = s.tree(N(["B1. Comparar com outra configuração"]),
           [N(["B1.1. Escolher a", "outra configuração"]),
            N(["B1.2. Executar a outra", "configuração nas imagens", "duvidosas (reutiliza A2.2)"]),
            N(["B1.3. Comparar na", "mesma região"])],
           y, 160, 1280, gap=40, pw=560) + 20

y = s.section(y, "Legenda")
s.box(140, y, 180, 50, ["objetivo"])
s.box(360, y, 180, 50, ["fora do sistema"], dashed=True)
s.text(480, y + 22, "Caixa contínua: objetivo apoiado pelo sistema; vira tópico ou subtópico de conversa (tabela da seção 2.1 da Entrega 9).",
       size=14, anchor="start")
s.text(480, y + 44, "Caixa tracejada: objetivo da persona alcançado entre pessoas, fora do sistema (RQ09).",
       size=14, anchor="start")
y = s.note(y + 80, ["Numeração provisória deste mapa (letras, para não confundir com seções do documento nem com o HTA); os IDs O01… são atribuídos no mapa consolidado da equipe.",
                    "B2 não tem subtópicos: é um único diálogo. B1.2 usa o mesmo diálogo de A2.2 (acompanhar o processamento).",
                    "[H]: proposta derivada de proto-persona, a revisar depois da coleta da Entrega 7."]) + 20

s.save(OUT, y)
print(OUT.name, y)
