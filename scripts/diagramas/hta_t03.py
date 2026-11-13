"""HTA da T03 — Comparar o resultado de uma imagem entre configurações (P01, Tiago).
Tabela correspondente: docs/05_analise_tarefas.md, seção 2.1."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/05_tarefas/hta_t03_comparar_configuracoes.svg"

s = Svg("HTA — T03: Comparar o resultado de uma imagem entre configurações",
        "HTA da tarefa T03 por Tiago Fagundes dos Santos. Objetivos retangulares, operações com traço duplo "
        "e planos. Uso proposto pelo analista de segmentação (P01) a partir do cenário C01. Inclui T02 "
        "(objetivo 2) e T01 (objetivo 3). Condições completas na tabela da Entrega 5.")
s.header("HTA — T03: Comparar o resultado de uma imagem entre configurações",
         "Tiago Fagundes dos Santos · 22.123.017-0 · P01, Rafael Pereira · C01 · Uso proposto [H]")

y = s.section(100, "Visão geral")
y = s.tree(N(["0. Comparar o resultado de uma imagem", "entre configurações"],
             "Plano 0: 1 > (2 > 3) > 4; repetir 2 > 3 por configuração"),
           [N(["1. Preparar a", "comparação"], "1.1 > 1.2"),
            N(["2. Obter o resultado de", "uma configuração (T02)"], "2.1 > 2.2 > 2.3"),
            N(["3. Avaliar o", "resultado (T01)"], "3.1 > 3.2 > 3.3"),
            N(["4. Concluir a", "comparação"], "4.1 > 4.2 > 4.3")],
           y, gap=36, pw=600)
y = s.note(y + 20, ["Planos abreviados; condições, repetições e término na tabela da Entrega 5, seção 2.1.",
                    "3 só ocorre para a configuração cuja execução terminou com resultado pronto (2.3.1)."]) + 10

y = s.section(y, "Expansões dos objetivos 1 e 2 — preparar e obter o resultado (T02)")
ya = s.tree(N(["1. Preparar a comparação"], "Plano 1: 1.1 > 1.2"),
            [N(["1.1. Selecionar a", "imagem de campo"], op=True),
             N(["1.2. Escolher as", "configurações", "a comparar"], op=True)],
            y, 40, 500, pw=360)
yb = s.tree(N(["2. Obter o resultado de uma configuração (T02)"], "Plano 2: 2.1 > 2.2 > 2.3"),
            [N(["2.1. Iniciar a", "segmentação com", "a configuração"], op=True),
             N(["2.2. Acompanhar o", "processamento"], op=True),
             N(["2.3. Conferir o", "desfecho da execução"], "2.3.1 / 2.3.2")],
            y, 560, 1400, gap=24, pw=520)
y = max(ya, yb) + 20
ya = s.tree(N(["2.3. Conferir o desfecho da execução"], "Plano 2.3: 2.3.1 / 2.3.2"),
            [N(["2.3.1. Reconhecer o", "resultado pronto"], op=True),
             N(["2.3.2. Tratar a falha", "da execução"], "2.3.2.1 > 2.3.2.2")],
            y, 40, 680, pw=460)
yb = s.tree(N(["2.3.2. Tratar a falha da execução"], "Plano 2.3.2: 2.3.2.1 > 2.3.2.2"),
            [N(["2.3.2.1. Ler a causa", "da falha"], op=True),
             N(["2.3.2.2. Decidir repetir", "ou retirar a configuração"], op=True)],
            y, 740, 1400, pw=460)
y = max(ya, yb) + 20

y = s.section(y, "Expansão do objetivo 3 — avaliar o resultado (detalhada no GOMS de T01)")
y = s.tree(N(["3. Avaliar o resultado (T01)"], "Plano 3: 3.1 > 3.2 > 3.3"),
           [N(["3.1. Visualizar o resultado", "sobre a imagem"], "3.1.1 / 3.1.2"),
            N(["3.2. Interpretar as", "classes pela legenda"], op=True),
            N(["3.3. Julgar a qualidade", "da segmentação"], "3.3.1 / 3.3.2 / 3.3.3")],
           y, gap=40, pw=560) + 20
ya = s.tree(N(["3.1. Visualizar o resultado sobre a imagem"], "Plano 3.1: 3.1.1 / 3.1.2"),
            [N(["3.1.1. Comparar", "lado a lado"], op=True),
             N(["3.1.2. Sobrepor a", "máscara com opacidade"], op=True)],
            y, 40, 600, pw=480)
yb = s.tree(N(["3.3. Julgar a qualidade da segmentação"], "Plano 3.3: 3.3.1 / 3.3.2 / 3.3.3"),
            [N(["3.3.1. Julgar pela", "inspeção visual"], op=True),
             N(["3.3.2. Consultar a", "confiança do", "modelo [H]"], op=True),
             N(["3.3.3. Conferir as", "métricas por", "classe"], op=True)],
            y, 660, 1400, gap=24, pw=480)
y = max(ya, yb) + 20

y = s.section(y, "Expansão do objetivo 4 — concluir a comparação")
y = s.tree(N(["4. Concluir a comparação"], "Plano 4: 4.1 > 4.2 > 4.3"),
           [N(["4.1. Comparar as", "configurações na", "mesma região"], op=True),
            N(["4.2. Registrar a", "conclusão"], "4.2.1 / 4.2.2 / 4.2.3"),
            N(["4.3. Comunicar a", "conclusão à equipe"], op=True)],
           y, gap=40, pw=560) + 20
y = s.tree(N(["4.2. Registrar a conclusão"], "Plano 4.2: 4.2.1 / 4.2.2 / 4.2.3"),
           [N(["4.2.1. Indicar a", "configuração mais", "adequada"], op=True),
            N(["4.2.2. Registrar que", "nenhuma é adequada"], op=True),
            N(["4.2.3. Registrar", "resultado", "inconclusivo"], op=True)],
           y, 380, 1060, gap=24, pw=480) + 10

H = s.hta_legend(y)
s.save(OUT, H)
print(OUT.name, H)
