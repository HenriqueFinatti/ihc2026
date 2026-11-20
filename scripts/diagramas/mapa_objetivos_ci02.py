"""Mapa de objetivos da P03 (Larissa) a partir do CI02 (Entrega 9, Henrique).
Texto correspondente: docs/09_modelo_conceitual.md, seções 2.2 (tópicos e subtópicos) e 3.1."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/09_modelo_conceitual/mapa_objetivos_ci02.svg"

s = Svg("Mapa de objetivos — P03, Larissa Camargo (CI02)",
        "Mapa de objetivos individual por Henrique Finatti Silveira Belo Trebbi. Objetivo final da P03, "
        "objetivos instrumentais diretos e indiretos, todos escritos como resultados desejados. Caixas "
        "tracejadas são objetivos alcançados fora do sistema.")
s.header("Mapa de objetivos — P03, Larissa Camargo (CI02)",
         "Henrique Finatti Silveira Belo Trebbi · 22.123.030-3 · origem: C02 → CI02 · T04 e T05 · Proposta [H]")

y = s.section(100, "Objetivo final e objetivos instrumentais diretos")
y = s.tree(N(["Configuração do ciclo de testes escolhida", "e sustentada perante a coordenação"], kind="final"),
           [N(["A. Saber como as", "configurações do ciclo", "se saem no conjunto", "de teste"]),
            N(["B. Recomendação", "registrada, com", "as ressalvas"]),
            N(["C. Decisão da", "coordenação registrada", "junto da recomendação"])],
           y, 80, 1360, gap=40, pw=640) + 20

y = s.section(y, "Objetivos instrumentais indiretos")
ya = s.tree(N(["A. Saber como as configurações", "se saem no conjunto de teste"]),
            [N(["A1. Entender o que", "as métricas e a", "diferença indicam"], kind="indireto"),
             N(["A2. Execuções e", "avaliações faltantes", "pedidas ao integrante", "técnico"], dashed=True, kind="indireto")],
            y, 40, 700, gap=30, pw=460)
yb = s.tree(N(["C. Decisão da coordenação registrada"]),
            [N(["C1. Recomendação", "apresentada à", "coordenação"], kind="indireto"),
             N(["C2. Decisão", "discutida na", "reunião"], dashed=True, kind="indireto")],
            y, 760, 1400, gap=30, pw=460)
y = max(ya, yb) + 20

y = s.goal_legend(y, [
    "Para responder às dúvidas da coordenação, C1 também usa o objetivo A1.",
    "Letras: numeração deste mapa; os IDs O01… do mapa consolidado estão na tabela de correspondência da seção 3.2 da Entrega 9.",
    "[H]: proposta derivada de proto-persona, a revisar depois da coleta da Entrega 7."])

s.save(OUT, y)
print(OUT.name, y)
