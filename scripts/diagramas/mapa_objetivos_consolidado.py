"""Mapa de objetivos consolidado da equipe (Entrega 9, parte da equipe).
Junta os mapas individuais (mapa_objetivos_ci01.py, _ci02.py e _ci03.py).
Texto correspondente: docs/09_modelo_conceitual.md, seção 3.2 (dicionário de objetivos)."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/09_modelo_conceitual/mapa_objetivos.svg"

s = Svg("Mapa de objetivos consolidado — Equipe 17",
        "Mapa de objetivos consolidado das personas P01, P02 e P03, a partir dos mapas individuais dos "
        "cenários CI01, CI02 e CI03. Objetivo geral, quatro grupos, objetivos O01 a O10 e seus subtópicos. "
        "Caixas tracejadas são objetivos alcançados fora do sistema.")
s.header("Mapa de objetivos consolidado — Equipe 17",
         "Henrique Finatti Silveira Belo Trebbi · Mateus Marana Assuena · Tiago Fagundes dos Santos · "
         "P01, P02 e P03 · CI01–CI03 · Proposta [H]")

y = s.section(100, "Visão geral")
y = s.tree(N(["Escolher, com evidência, a configuração", "do modelo usada nos testes do Baja"]),
           [N(["A. Preparar", "configurações"]),
            N(["B. Executar e", "avaliar resultados"]),
            N(["C. Comparar", "configurações"]),
            N(["D. Concluir e", "decidir"])],
           y, gap=36, pw=600) + 20

y = s.section(y, "Grupos A e B — preparar configurações; executar e avaliar resultados")
ya = s.tree(N(["A. Preparar configurações"]),
            [N(["O01. Definir uma", "configuração de", "treino (P02)"]),
             N(["O02. Treinar o", "modelo (P02)"])],
            y, 40, 600, gap=30, pw=420)
yb = s.tree(N(["B. Executar e avaliar resultados"]),
            [N(["Obter as entradas", "(imagens e quadros)", "(P01, P02)"], dashed=True),
             N(["O03. Executar a", "segmentação", "(P01, P02)"]),
             N(["O04. Avaliar a", "segmentação de uma", "imagem (P01, P02)"])],
            y, 660, 1400, gap=24, pw=460)
y = max(ya, yb) + 20

y = s.section(y, "Grupos C e D — comparar configurações; concluir e decidir")
ya = s.tree(N(["C. Comparar configurações"]),
            [N(["O05. Comparar", "configurações sobre a", "mesma entrada", "(P01, P02)"]),
             N(["O06. Comparar o", "desempenho", "consolidado", "(P03, P02)"]),
             N(["O07. Entender o", "que os números", "significam", "(P03, P02)"])],
            y, 40, 760, gap=20, pw=460)
yb = s.tree(N(["D. Concluir e decidir"]),
            [N(["O08. Registrar a", "conclusão", "(P01, P02, P03)"]),
             N(["O09. Apresentar a", "recomendação à", "coordenação (P03)"]),
             N(["O10. Registrar a", "decisão da", "coordenação (P03)"])],
            y, 820, 1400, gap=16, pw=460)
y = max(ya, yb) + 20
y = s.tree(N(["Fora do sistema (grupos C e D)"], dashed=True),
           [N(["Pedir execução,", "conferência ou validação", "a um colega (P02, P03)"], dashed=True),
            N(["Comunicar as", "conclusões ao grupo", "(P01)"], dashed=True),
            N(["Discutir a decisão", "na reunião de", "coordenação (P02, P03)"], dashed=True)],
           y, 160, 1280, gap=40, pw=520) + 20

y = s.section(y, "Desdobramento dos objetivos em subtópicos")
ya = s.tree(N(["O01. Definir uma configuração", "de treino"]),
            [N(["O01.1. Escolher o", "modelo e os", "parâmetros"]),
             N(["O01.2. Nomear a", "configuração"])],
            y, 40, 640, gap=30, pw=440)
yb = s.tree(N(["O02. Treinar o modelo"]),
            [N(["O02.1. Acompanhar", "o treino"]),
             N(["O02.2. Conferir o", "resultado do treino"])],
            y, 700, 1400, gap=30, pw=420)
y = max(ya, yb) + 20
ya = s.tree(N(["O03. Executar a segmentação"]),
            [N(["O03.1. Enviar as", "entradas e escolher", "as configurações"]),
             N(["O03.2. Acompanhar", "o processamento"])],
            y, 40, 640, gap=30, pw=420)
yb = s.tree(N(["O04. Avaliar a segmentação", "de uma imagem"]),
            [N(["O04.1. Ver o", "resultado sobre", "a imagem"]),
             N(["O04.2. Conferir se", "há métricas"]),
             N(["O04.3. Registrar a", "avaliação da", "imagem"])],
            y, 700, 1400, gap=24, pw=460)
y = max(ya, yb) + 20
ya = s.tree(N(["O05. Comparar configurações", "sobre a mesma entrada"]),
            [N(["O05.1. Escolher as", "configurações a", "comparar"]),
             N(["O05.2. Comparar na", "mesma imagem", "e região"])],
            y, 40, 560, gap=30, pw=440)
yb = s.tree(N(["O06. Comparar o desempenho consolidado"]),
            [N(["O06.1. Escolher as", "configurações"]),
             N(["O06.2. Conferir se", "a comparação", "é válida"]),
             N(["O06.3. Ler o", "desempenho de", "cada uma"]),
             N(["O06.4. Consultar", "a matriz de", "confusão"])],
            y, 620, 1400, gap=16, pw=480)
y = max(ya, yb) + 20
ya = s.tree(N(["O07. Entender o que os", "números significam"]),
            [N(["O07.1. Entender", "um termo"]),
             N(["O07.2. Julgar a", "diferença entre", "configurações"])],
            y, 40, 640, gap=30, pw=420)
yb = s.tree(N(["O08. Registrar a conclusão"]),
            [N(["O08.1. Informar a", "conclusão"]),
             N(["O08.2. Conferir a", "conclusão"])],
            y, 700, 1400, gap=30, pw=420)
y = max(ya, yb) + 20
y = s.tree(N(["O09. Apresentar a recomendação à coordenação"]),
           [N(["O09.1. Retomar", "a análise"]),
            N(["O09.2. Responder a uma", "dúvida (reutiliza O07.2)"])],
           y, 280, 1160, gap=60, pw=560) + 20

y = s.section(y, "Legenda")
s.box(140, y, 180, 50, ["objetivo"])
s.box(360, y, 180, 50, ["fora do sistema"], dashed=True)
s.text(480, y + 22, "Caixa contínua: objetivo apoiado pelo sistema, com ID O01–O10 (subtópicos O01.1…), usado nas Entregas 10 e 11.",
       size=14, anchor="start")
s.text(480, y + 44, "Caixa tracejada: objetivo alcançado entre pessoas, fora do sistema (RQ09); não recebe ID.",
       size=14, anchor="start")
y = s.note(y + 80, ["Entre parênteses: personas que têm o objetivo. Correspondência com os mapas individuais na seção 3.2 da Entrega 9.",
                    "O05 reúne T03 (P01) e T07 (P02); O08 reúne as conclusões da validação (P01), do experimento (P02) e a recomendação (P03).",
                    "O10 não tem subtópicos: é um único diálogo.",
                    "[H]: proposta derivada de proto-personas, a revisar depois da coleta da Entrega 7."]) + 20

s.save(OUT, y)
print(OUT.name, y)
