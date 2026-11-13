"""Mapa de objetivos da P03 (Larissa) a partir do CI02 (Entrega 9, Henrique).
Texto correspondente: docs/09_modelo_conceitual.md, seções 2.2 (tópicos e subtópicos) e 3.1."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/09_modelo_conceitual/mapa_objetivos_ci02.svg"

s = Svg("Mapa de objetivos — P03, Larissa Camargo (CI02)",
        "Mapa de objetivos individual por Henrique Finatti Silveira Belo Trebbi. Objetivo geral da P03, "
        "dois objetivos, os tópicos de conversa da seção 2.2 da Entrega 9 e seus subtópicos. Caixas "
        "tracejadas são objetivos alcançados fora do sistema.")
s.header("Mapa de objetivos — P03, Larissa Camargo (CI02)",
         "Henrique Finatti Silveira Belo Trebbi · 22.123.030-3 · origem: C02 → CI02 · T04 e T05 · Proposta [H]")

y = s.section(100, "Visão geral")
y = s.tree(N(["Decidir e sustentar a configuração", "do ciclo de testes"]),
           [N(["1. Decidir qual configuração", "recomendar"]),
            N(["2. Sustentar a recomendação", "perante a coordenação"])],
           y, 200, 1240, gap=80, pw=560) + 20

y = s.section(y, "Objetivo 1 — decidir qual configuração recomendar (T04 e T05)")
y = s.tree(N(["1. Decidir qual configuração recomendar"]),
           [N(["1.1. Comparar o", "desempenho das", "configurações do ciclo"]),
            N(["1.2. Entender o que", "os números", "significam"]),
            N(["1.3. Registrar a", "recomendação"]),
            N(["1.4. Pedir execução ou", "conferência ao", "integrante técnico"], dashed=True)],
           y, gap=36, pw=560) + 20

y = s.section(y, "Objetivo 2 — sustentar a recomendação perante a coordenação (T05)")
y = s.tree(N(["2. Sustentar a recomendação perante a coordenação"]),
           [N(["2.1. Apresentar a", "recomendação à", "coordenação"]),
            N(["2.2. Discutir a", "decisão na reunião"], dashed=True),
            N(["2.3. Registrar a", "decisão da", "coordenação"])],
           y, 160, 1280, gap=40, pw=620) + 20

y = s.section(y, "Subtópicos de conversa (seção 2.2)")
ya = s.tree(N(["1.1. Comparar o desempenho", "das configurações do ciclo"]),
            [N(["1.1.1. Escolher o", "que comparar"]),
             N(["1.1.2. Conferir se a", "comparação é", "válida"]),
             N(["1.1.3. Ler o", "desempenho de cada", "configuração"])],
            y, 40, 760, gap=24, pw=460)
yb = s.tree(N(["1.2. Entender o que", "os números significam"]),
            [N(["1.2.1. Entender", "um termo"]),
             N(["1.2.2. Julgar a diferença", "entre as configurações"])],
            y, 820, 1400, gap=24, pw=420)
y = max(ya, yb) + 20
ya = s.tree(N(["1.3. Registrar a recomendação"]),
            [N(["1.3.1. Informar a", "recomendação e", "a ressalva"]),
             N(["1.3.2. Conferir a", "recomendação"])],
            y, 40, 640, gap=30, pw=420)
yb = s.tree(N(["2.1. Apresentar a recomendação", "à coordenação"]),
            [N(["2.1.1. Retomar a", "comparação"]),
             N(["2.1.2. Responder a uma", "dúvida da coordenação", "(reutiliza 1.2.2)"])],
            y, 700, 1400, gap=30, pw=460)
y = max(ya, yb) + 20

y = s.section(y, "Legenda")
s.box(140, y, 180, 50, ["objetivo"])
s.box(360, y, 180, 50, ["fora do sistema"], dashed=True)
s.text(480, y + 22, "Caixa contínua: objetivo apoiado pelo sistema; vira tópico ou subtópico de conversa (seção 2.2).",
       size=14, anchor="start")
s.text(480, y + 44, "Caixa tracejada: objetivo da persona alcançado entre pessoas, fora do sistema (RQ09).",
       size=14, anchor="start")
y = s.note(y + 80, ["Numeração provisória deste mapa; os IDs O01… são atribuídos no mapa consolidado da equipe.",
                    "2.3 não tem subtópicos: é um único diálogo. 1.2.2 também responde à dúvida da coordenação (2.1.2).",
                    "[H]: proposta derivada de proto-persona, a revisar depois da coleta da Entrega 7."]) + 20

s.save(OUT, y)
print(OUT.name, y)
