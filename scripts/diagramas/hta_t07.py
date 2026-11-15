"""HTA da T07 — Comparar o resultado de diferentes modelos (P02, Mateus).
Tabela correspondente: docs/05_analise_tarefas.md, seção 3.1."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/05_tarefas/hta_t07_comparar_modelos.svg"

s = Svg("HTA — T07: Comparar o resultado de diferentes modelos",
        "HTA da tarefa T07 por Mateus Marana Assuena. Objetivos retangulares, operações com traço duplo e "
        "planos. Uso proposto pela pesquisadora e coordenadora (P02) a partir do cenário C03. Condições "
        "completas na tabela da Entrega 5.")
s.header("HTA — T07: Comparar o resultado de diferentes modelos",
         "Mateus Marana Assuena · 22.123.026-1 · P02, Andreia Silva · C03 · Uso proposto [H]")

y = s.section(100, "Visão geral")
y = s.tree(N(["0. Comparar o resultado de diferentes", "modelos sobre a mesma entrada"], "Plano 0: 1 > 2* > 3 > 4 > 5"),
           [N(["1. Preparar a", "comparação"], "1.1 > 1.2"),
            N(["2. Obter o resultado de", "cada configuração (T02)"], "2.1 > 2.2 > 2.3"),
            N(["3. Comparar os", "resultados", "visualmente (T06)"], "3.1 > 3.2"),
            N(["4. Comparar as", "métricas no", "conjunto de teste"], "4.1 > [4.2]"),
            N(["5. Concluir a", "comparação"], "5.1 > 5.2")],
           y, gap=24, pw=560)
y = s.note(y + 20, ["2* repete-se para cada configuração escolhida em 1.2 que ainda não foi executada sobre a entrada.",
                    "Planos abreviados; condições e exceções na tabela da Entrega 5, seção 3.1."]) + 10

y = s.section(y, "Expansões dos objetivos 1 e 2")
ya = s.tree(N(["1. Preparar a comparação"], "Plano 1: 1.1 > 1.2"),
            [N(["1.1. Selecionar a", "entrada (imagens", "ou quadros)"], op=True),
             N(["1.2. Escolher as", "configurações a", "comparar"], op=True)],
            y, 40, 680, pw=440)
yb = s.tree(N(["2. Obter o resultado de cada configuração"], "Plano 2: 2.1 > 2.2 > 2.3"),
            [N(["2.1. Iniciar a", "segmentação"], op=True),
             N(["2.2. Acompanhar o", "processamento"], op=True),
             N(["2.3. Conferir o", "desfecho da", "execução"], "2.3.1 / 2.3.2")],
            y, 720, 1400, gap=20, pw=480)
y = max(ya, yb) + 20
y = s.tree(N(["2.3. Conferir o desfecho da execução"], "Plano 2.3: 2.3.1 / 2.3.2"),
           [N(["2.3.1. Reconhecer o", "resultado pronto"], op=True),
            N(["2.3.2. Repetir ou", "retirar a configuração"], op=True)],
           y, 720, 1400, pw=480) + 20

y = s.section(y, "Expansões dos objetivos 3, 4 e 5")
ya = s.tree(N(["3. Comparar os resultados visualmente"], "Plano 3: 3.1 > 3.2"),
            [N(["3.1. Visualizar o", "resultado de cada", "configuração"], op=True),
             N(["3.2. Comparar na", "mesma região"], op=True)],
            y, 40, 680, pw=460)
yb = s.tree(N(["4. Comparar as métricas no conjunto de teste"], "Plano 4: 4.1 > [4.2]"),
            [N(["4.1. Ler a diferença", "entre as configurações"], op=True),
             N(["4.2. Consultar a", "matriz de confusão"], op=True)],
            y, 740, 1400, pw=500)
y = max(ya, yb) + 20
y = s.tree(N(["5. Concluir a comparação"], "Plano 5: 5.1 > 5.2"),
           [N(["5.1. Julgar se a", "diferença é relevante"], op=True),
            N(["5.2. Registrar a", "conclusão"], op=True)],
           y, 280, 1160, gap=60, pw=480) + 10
y = s.note(y + 10, ["[4.2] só ocorre quando Andreia precisa entender onde cada configuração erra ([ ] = passo condicional).",
                    "5.1 pode concluir que a nova configuração é melhor, igual, pior ou que a comparação é inconclusiva."]) + 10

H = s.hta_legend(y)
s.save(OUT, H)
print(OUT.name, H)
