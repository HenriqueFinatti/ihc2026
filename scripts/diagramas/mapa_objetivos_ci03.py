"""Mapa de objetivos da P02 (Andreia) a partir do CI03 (Entrega 9, Mateus).
Texto correspondente: docs/09_modelo_conceitual.md, seções 2.3 (tópicos e subtópicos) e 3.1."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/09_modelo_conceitual/mapa_objetivos_ci03.svg"

s = Svg("Mapa de objetivos — P02, Andreia Silva (CI03)",
        "Mapa de objetivos individual por Mateus Marana Assuena. Objetivo final da P02, objetivos "
        "instrumentais diretos e indiretos, todos escritos como resultados desejados. Caixas tracejadas "
        "são objetivos alcançados fora do sistema.")
s.header("Mapa de objetivos — P02, Andreia Silva (CI03)",
         "Mateus Marana Assuena · 22.123.026-1 · origem: C03 → CI03 · T08, T02, T06 e T07 · Proposta [H]")

y = s.section(100, "Objetivo final e objetivos instrumentais diretos")
y = s.tree(N(["Saber se a nova configuração melhora a trilha", "em sombra e qual seguir no próximo experimento"], kind="final"),
           [N(["A. Nova configuração", "treinada, disponível", "e avaliada no", "conjunto de teste"]),
            N(["B. Saber se a nova", "configuração delimita", "melhor a trilha nos", "quadros de sombra"]),
            N(["C. Saber como as", "configurações se", "saem no conjunto", "de teste"]),
            N(["D. Conclusão do", "experimento", "registrada"]),
            N(["E. Validação em", "campo pedida e", "conclusão levada", "à reunião"], dashed=True)],
           y, 40, 1400, gap=16, pw=720) + 20

y = s.section(y, "Objetivos instrumentais indiretos")
y1 = s.tree(N(["A. Nova configuração treinada"]),
            [N(["A1. Configuração de", "treino definida", "e nomeada"], kind="indireto"),
             N(["A2. Dados de treino", "e de teste prontos e", "configurações", "avaliadas no", "conjunto de teste"], kind="indireto")],
            y, 40, 620, gap=20, pw=400)
y2 = s.tree(N(["B. Saber se delimita melhor", "a trilha nos quadros"]),
            [N(["B1. Quadros extraídos", "do vídeo e segmentados", "com as duas", "configurações"], kind="indireto")],
            y, 660, 1020, gap=20, pw=340)
y3 = s.tree(N(["C. Saber como se saem", "no conjunto de teste"]),
            [N(["C1. Entender o que", "a diferença entre", "as configurações", "indica"], kind="indireto")],
            y, 1060, 1400, gap=20, pw=320)
y = max(y1, y2, y3) + 20

y = s.goal_legend(y, [
    "B1: desde 16/11/2026, o sistema extrai os quadros do vídeo enviado (antes, a extração ficava fora do sistema).",
    "A2: incluído em 20/11/2026 (atividade da tela Datasets da Entrega 11); também apoia C, porque só configurações avaliadas entram na comparação.",
    "Letras: numeração deste mapa; os IDs O01… do mapa consolidado estão na tabela de correspondência da seção 3.2 da Entrega 9.",
    "[H]: proposta derivada de proto-persona, a revisar depois da coleta da Entrega 7."])

s.save(OUT, y)
print(OUT.name, y)
