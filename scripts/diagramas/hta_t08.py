"""HTA da T08 — Definir uma configuração de treino e treinar o modelo (P02, Mateus).
Tabela correspondente: docs/05_analise_tarefas.md, seção 3.6.1."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/05_tarefas/hta_t08_treinar_configuracao.svg"

s = Svg("HTA — T08: Definir uma configuração de treino e treinar o modelo",
        "HTA da tarefa T08 por Mateus Marana Assuena. Objetivos retangulares, operações com traço duplo e "
        "planos. Uso proposto pela pesquisadora e coordenadora (P02) a partir do cenário C03 e do cenário "
        "de interação CI03 da Entrega 9. Condições completas na tabela da Entrega 5.")
s.header("HTA — T08: Definir uma configuração de treino e treinar o modelo",
         "Mateus Marana Assuena · 22.123.026-1 · P02, Andreia Silva · C03 / CI03 · Uso proposto [H]")

y = s.section(100, "Visão geral")
y = s.tree(N(["0. Definir uma configuração de treino", "e treinar o modelo"], "Plano 0: 1 > 2 > 3"),
           [N(["1. Definir a", "configuração"], "1.1 > 1.2 > 1.3"),
            N(["2. Treinar o", "modelo"], "2.1 > 2.2 > 2.3"),
            N(["3. Conferir a", "configuração treinada"], "3.1 > 3.2")],
           y, gap=40, pw=560)
y = s.note(y + 20, ["Se 2.3 terminar em 2.3.2 (falha), Andreia ajusta a configuração e volta a 2.1.",
                    "Planos abreviados; condições e exceções na tabela da Entrega 5, seção 3.6.1."]) + 10

y = s.section(y, "Expansão do objetivo 1 — definir a configuração")
y = s.tree(N(["1. Definir a configuração"], "Plano 1: 1.1 > 1.2 > 1.3"),
           [N(["1.1. Escolher o", "modelo"], op=True),
            N(["1.2. Definir os", "parâmetros de treino"], "1.2.1 / 1.2.2"),
            N(["1.3. Nomear a", "configuração"], op=True)],
           y, gap=40, pw=560) + 20
y = s.tree(N(["1.2. Definir os parâmetros de treino"], "Plano 1.2: 1.2.1 / 1.2.2"),
           [N(["1.2.1. Manter os", "valores padrão"], op=True),
            N(["1.2.2. Alterar os", "parâmetros do", "experimento"], op=True)],
           y, 280, 1160, gap=60, pw=520) + 20

y = s.section(y, "Expansão do objetivo 2 — treinar o modelo")
y = s.tree(N(["2. Treinar o modelo"], "Plano 2: 2.1 > 2.2 > 2.3"),
           [N(["2.1. Iniciar o", "treino"], op=True),
            N(["2.2. Acompanhar o", "treino"], op=True),
            N(["2.3. Conferir o", "desfecho do treino"], "2.3.1 / 2.3.2")],
           y, gap=40, pw=560) + 20
y = s.tree(N(["2.3. Conferir o desfecho do treino"], "Plano 2.3: 2.3.1 / 2.3.2"),
           [N(["2.3.1. Reconhecer o", "treino concluído"], op=True),
            N(["2.3.2. Tratar a", "falha do treino"], "2.3.2.1 > 2.3.2.2")],
           y, 40, 760, gap=40, pw=520)
y = s.tree(N(["2.3.2. Tratar a falha do treino"], "Plano 2.3.2: 2.3.2.1 > 2.3.2.2"),
           [N(["2.3.2.1. Ler a", "causa da falha"], op=True),
            N(["2.3.2.2. Ajustar a", "configuração e", "reiniciar"], op=True)],
           y, 800, 1400, gap=30, pw=480) + 20

y = s.section(y, "Expansão do objetivo 3 — conferir a configuração treinada")
y = s.tree(N(["3. Conferir a configuração treinada"], "Plano 3: 3.1 > 3.2"),
           [N(["3.1. Ler os gráficos de", "treino e validação"], op=True),
            N(["3.2. Ler as métricas no", "conjunto de teste"], op=True)],
           y, 280, 1160, gap=60, pw=520) + 10

H = s.hta_legend(y)
s.save(OUT, H)
print(OUT.name, H)
