"""HTA da T05 — Decidir e justificar a adoção de um modelo (P03, Henrique).
Tabela correspondente: docs/05_analise_tarefas.md, seção 1.1."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/05_tarefas/hta_t05_decidir_modelo.svg"

s = Svg("HTA — T05: Decidir e justificar a adoção de um modelo",
        "HTA da tarefa T05 por Henrique Finatti Silveira Belo Trebbi. Objetivos retangulares, operações com "
        "traço duplo e planos. Uso proposto pela gestora de projeto (P03) a partir do cenário C02. Condições "
        "completas na tabela da Entrega 5.")
s.header("HTA — T05: Decidir e justificar a adoção de um modelo",
         "Henrique Finatti Silveira Belo Trebbi · 22.123.030-3 · P03, Larissa Camargo · C02 · Uso proposto [H]")

y = s.section(100, "Visão geral")
y = s.tree(N(["0. Decidir e justificar a adoção de um", "modelo para o ciclo de testes"], "Plano 0: 1 > 2 > 3 > 4"),
           [N(["1. Reunir os resultados", "do ciclo"], "1.1 > 1.2"),
            N(["2. Comparar o desempenho", "consolidado (T04)"], "2.1 > 2.2 > 2.3"),
            N(["3. Formar a", "recomendação"], "3.1 / 3.2 / 3.3"),
            N(["4. Apresentar e sustentar", "a recomendação"], "4.1 > 4.2 > 4.3")],
           y, gap=36, pw=560)
y = s.note(y + 20, ["Planos abreviados; condições, repetições e término na tabela da Entrega 5, seção 1.1.",
                    "1.2 só ocorre se faltar execução de algum modelo; depois da resposta, repetir 1.1."]) + 10

y = s.section(y, "Expansões dos objetivos 1 e 3")
ya = s.tree(N(["1. Reunir os resultados do ciclo"], "Plano 1: 1.1 > 1.2"),
            [N(["1.1. Conferir as", "execuções disponíveis", "do ciclo"], op=True),
             N(["1.2. Solicitar execuções", "faltantes ao integrante", "técnico"], op=True)],
            y, 40, 640, pw=420)
yb = s.tree(N(["3. Formar a recomendação"], "Plano 3: 3.1 / 3.2 / 3.3"),
            [N(["3.1. Recomendar o", "modelo de melhor", "desempenho"], op=True),
             N(["3.2. Recomendar com", "ressalva de", "incerteza"], op=True),
             N(["3.3. Adiar e pedir", "novas execuções"], op=True)],
            y, 700, 1400, gap=24, pw=420)
y = max(ya, yb) + 20

y = s.section(y, "Expansão do objetivo 2 — comparação consolidada (detalhada no GOMS de T04)")
y = s.tree(N(["2. Comparar o desempenho consolidado (T04)"], "Plano 2: 2.1 > 2.2 > 2.3"),
           [N(["2.1. Abrir a comparação", "dos modelos do ciclo"], op=True),
            N(["2.2. Ler o desempenho", "de cada modelo"], "2.2.1 / 2.2.2"),
            N(["2.3. Avaliar se a", "diferença é relevante"], "2.3.1 / 2.3.2 / 2.3.3")],
           y, gap=40, pw=560) + 20
ya = s.tree(N(["2.2. Ler o desempenho de cada modelo"], "Plano 2.2: 2.2.1 / 2.2.2"),
            [N(["2.2.1. Ler as", "métricas na tabela"], op=True),
             N(["2.2.2. Ler as", "métricas no gráfico"], op=True)],
            y, 40, 560, pw=440)
yb = s.tree(N(["2.3. Avaliar se a diferença é relevante"], "Plano 2.3: 2.3.1 / 2.3.2 / 2.3.3"),
            [N(["2.3.1. Julgar a", "diferença pela", "referência"], op=True),
             N(["2.3.2. Consultar a", "explicação e julgar"], "2.3.2.1 > 2.3.2.2"),
             N(["2.3.3. Pedir", "interpretação ao", "integrante técnico"], op=True)],
            y, 620, 1400, gap=24, pw=460)
y = max(ya, yb) + 20
y = s.tree(N(["2.3.2. Consultar a explicação e julgar"], "Plano 2.3.2: 2.3.2.1 > 2.3.2.2"),
           [N(["2.3.2.1. Consultar a explicação", "do termo ou do aviso"], op=True),
            N(["2.3.2.2. Julgar a diferença", "com a explicação"], op=True)],
           y, 620, 1400, pw=460) + 20

y = s.section(y, "Expansão do objetivo 4")
y = s.tree(N(["4. Apresentar e sustentar a recomendação"], "Plano 4: 4.1 > 4.2 > 4.3"),
           [N(["4.1. Preparar o material", "para a reunião"], "4.1.1 / 4.1.2"),
            N(["4.2. Apresentar a", "recomendação e", "seus limites"], op=True),
            N(["4.3. Registrar a", "decisão da", "coordenação"], op=True)],
           y, gap=40, pw=560) + 20
y = s.tree(N(["4.1. Preparar o material para a reunião"], "Plano 4.1: 4.1.1 / 4.1.2"),
           [N(["4.1.1. Exportar o resumo", "da comparação [H]"], op=True),
            N(["4.1.2. Anotar modelo,", "métricas e ressalvas"], op=True)],
           y, 40, 700, pw=440) + 10

H = s.hta_legend(y)
s.save(OUT, H)
print(OUT.name, H)
