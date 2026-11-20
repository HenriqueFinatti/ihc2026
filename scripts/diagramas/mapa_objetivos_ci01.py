"""Mapa de objetivos da P01 (Rafael) a partir do CI01 (Entrega 9, Tiago).
Texto correspondente: docs/09_modelo_conceitual.md, seções 2.1 (tópicos e subtópicos) e 3.1."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/09_modelo_conceitual/mapa_objetivos_ci01.svg"

s = Svg("Mapa de objetivos — P01, Rafael Pereira (CI01)",
        "Mapa de objetivos individual por Tiago Fagundes dos Santos. Objetivo final da P01, objetivos "
        "instrumentais diretos e indiretos, todos escritos como resultados desejados. Caixas tracejadas "
        "são objetivos alcançados fora do sistema.")
s.header("Mapa de objetivos — P01, Rafael Pereira (CI01)",
         "Tiago Fagundes dos Santos · 22.123.017-0 · origem: C01 → CI01 · T01, T02 e T03 · Proposta [H]")

y = s.section(100, "Objetivo final e objetivos instrumentais diretos")
y = s.tree(N(["Equipe sabe, antes do próximo teste, se a", "configuração em uso pode continuar"], kind="final"),
           [N(["A. Imagens do teste", "avaliadas, com a origem", "de cada problema"]),
            N(["B. Saber se outra", "configuração delimita", "melhor a trilha nas", "imagens duvidosas"]),
            N(["C. Conclusão da", "validação registrada"]),
            N(["D. Grupo da equipe", "informado da", "conclusão"], dashed=True)],
           y, 40, 1400, gap=24, pw=640) + 20

y = s.section(y, "Objetivos instrumentais indiretos")
ya = s.tree(N(["A. Imagens do teste avaliadas, com", "a origem de cada problema"]),
            [N(["A1. Imagens do teste", "segmentadas com a", "configuração em uso"], kind="indireto"),
             N(["A2. Imagens do teste", "obtidas das câmeras"], dashed=True, kind="indireto")],
            y, 40, 700, gap=30, pw=460)
yb = s.tree(N(["B. Saber se outra configuração", "delimita melhor a trilha"]),
            [N(["B1. Imagens duvidosas", "segmentadas também", "com a outra", "configuração"], kind="indireto")],
            y, 900, 1260, gap=30, pw=360)
y = max(ya, yb) + 20

y = s.goal_legend(y, [
    "Letras: numeração deste mapa; os IDs O01… do mapa consolidado estão na tabela de correspondência da seção 3.2 da Entrega 9.",
    "[H]: proposta derivada de proto-persona, a revisar depois da coleta da Entrega 7."])

s.save(OUT, y)
print(OUT.name, y)
