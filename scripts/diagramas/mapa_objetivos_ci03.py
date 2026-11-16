"""Mapa de objetivos da P02 (Andreia) a partir do CI03 (Entrega 9, Mateus).
Texto correspondente: docs/09_modelo_conceitual.md, seções 2.3 (tópicos e subtópicos) e 3.1."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/09_modelo_conceitual/mapa_objetivos_ci03.svg"

s = Svg("Mapa de objetivos — P02, Andreia Silva (CI03)",
        "Mapa de objetivos individual por Mateus Marana Assuena. Objetivo geral da P02, dois objetivos, "
        "os tópicos de conversa da seção 2.3 da Entrega 9 e seus subtópicos. Caixas tracejadas são "
        "objetivos alcançados fora do sistema.")
s.header("Mapa de objetivos — P02, Andreia Silva (CI03)",
         "Mateus Marana Assuena · 22.123.026-1 · origem: C03 → CI03 · T08, T02, T06 e T07 · Proposta [H]")

y = s.section(100, "Visão geral")
y = s.tree(N(["Decidir qual configuração seguir no próximo", "experimento e qual levar à reunião"]),
           [N(["A. Experimentar uma", "nova configuração"]),
            N(["B. Avaliar a nova", "configuração"])],
           y, 200, 1240, gap=80, pw=640) + 20

y = s.section(y, "Objetivo A — experimentar uma nova configuração (T08)")
y = s.tree(N(["A. Experimentar uma nova configuração"]),
           [N(["A1. Definir uma", "configuração de", "treino"]),
            N(["A2. Treinar o", "modelo"])],
           y, 280, 1160, gap=60, pw=560) + 20

y = s.section(y, "Objetivo B — avaliar a nova configuração (T02, T06 e T07)")
y = s.tree(N(["B. Avaliar a nova configuração"]),
           [N(["B1. Extrair os quadros", "dos vídeos"]),
            N(["B2. Comparar as", "configurações nos", "quadros de sombra"]),
            N(["B3. Registrar a", "conclusão do", "experimento"]),
            N(["B4. Pedir validação em", "campo e levar à", "reunião"], dashed=True)],
           y, gap=36, pw=560) + 20

y = s.section(y, "Desdobramento dos tópicos em subtópicos")
ya = s.tree(N(["A1. Definir uma configuração", "de treino"]),
            [N(["A1.1. Escolher o", "modelo e os", "parâmetros"]),
             N(["A1.2. Nomear a", "configuração"])],
            y, 40, 640, gap=30, pw=440)
yb = s.tree(N(["A2. Treinar o modelo"]),
            [N(["A2.1. Acompanhar", "o treino"]),
             N(["A2.2. Conferir o", "resultado do", "treino"])],
            y, 700, 1400, gap=30, pw=420)
y = max(ya, yb) + 20
y = s.tree(N(["B2. Comparar as configurações nos quadros de sombra"]),
           [N(["B2.1. Executar as", "configurações nos", "mesmos quadros", "(reutiliza P01 A2.2)"]),
            N(["B2.2. Analisar", "um quadro"]),
            N(["B2.3. Comparar as", "métricas no", "conjunto de teste", "(reutiliza P03 A2.2)"]),
            N(["B2.4. Consultar a", "matriz de", "confusão"])],
           y, gap=30, pw=640) + 20

y = s.section(y, "Legenda")
s.box(140, y, 180, 50, ["objetivo"])
s.box(360, y, 180, 50, ["fora do sistema"], dashed=True)
s.text(480, y + 22, "Caixa contínua: objetivo apoiado pelo sistema; vira tópico ou subtópico de conversa (tabela da seção 2.3 da Entrega 9).",
       size=14, anchor="start")
s.text(480, y + 44, "Caixa tracejada: objetivo da persona alcançado entre pessoas, fora do sistema (RQ09).",
       size=14, anchor="start")
y = s.note(y + 80, ["Numeração provisória deste mapa (letras, para não confundir com seções do documento nem com o HTA); os IDs O01… são atribuídos no mapa consolidado da equipe.",
                    "A2 inclui o início do treino; B3 não tem subtópicos: é um único diálogo.",
                    "B1 passou para o sistema em 16/11/2026: o vídeo é enviado na execução (O03.1), e o sistema extrai os quadros.",
                    "B2.1 reutiliza o diálogo de execução da P01 (CI01); B2.3, o diálogo de julgar a diferença da P03 (CI02).",
                    "[H]: proposta derivada de proto-persona, a revisar depois da coleta da Entrega 7."]) + 20

s.save(OUT, y)
print(OUT.name, y)
