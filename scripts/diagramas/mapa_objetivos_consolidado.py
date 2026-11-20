"""Mapa de objetivos consolidado da equipe (Entrega 9, parte da equipe).
Junta os mapas individuais (mapa_objetivos_ci01.py, _ci02.py e _ci03.py).
Texto correspondente: docs/09_modelo_conceitual.md, seção 3.2 (dicionário de objetivos)."""
from pathlib import Path
from ihc_svg import Svg, N

OUT = Path(__file__).resolve().parents[2] / "assets/09_modelo_conceitual/mapa_objetivos.svg"

# Objetivos consolidados (IDs reutilizados nas Entregas 10 a 12), escritos como resultados.
O = {
    "O01": ["O01. Configuração de", "treino definida", "e nomeada"],
    "O02": ["O02. Nova configuração", "treinada, disponível", "e avaliada no", "conjunto de teste"],
    "O03": ["O03. Imagens", "segmentadas com as", "configurações", "escolhidas"],
    "O04": ["O04. Imagens", "avaliadas, com a", "origem de cada", "problema"],
    "O05": ["O05. Saber qual", "configuração delimita", "melhor a trilha nas", "mesmas imagens"],
    "O06": ["O06. Saber como as", "configurações se", "saem no conjunto", "de teste"],
    "O07": ["O07. Entender o que", "as métricas e a", "diferença indicam"],
    "O08": ["O08. Conclusão", "registrada junto", "da análise"],
    "O09": ["O09. Recomendação", "apresentada à", "coordenação"],
    "O10": ["O10. Decisão da", "coordenação", "registrada"],
}


def d(k):
    return N(O[k])


def i(k):
    return N(O[k], kind="indireto")


s = Svg("Mapa de objetivos consolidado — Equipe 17",
        "Mapa de objetivos consolidado das personas P01, P02 e P03, a partir dos mapas individuais dos "
        "cenários CI01, CI02 e CI03. Objetivo geral, objetivo final de cada persona e objetivos "
        "instrumentais O01 a O10, diretos e indiretos, escritos como resultados desejados. Caixas "
        "tracejadas são objetivos alcançados fora do sistema.")
s.header("Mapa de objetivos consolidado — Equipe 17",
         "Henrique Finatti Silveira Belo Trebbi · Mateus Marana Assuena · Tiago Fagundes dos Santos · "
         "P01, P02 e P03 · CI01–CI03 · Proposta [H]")

y = s.section(100, "Objetivo geral e objetivos finais das personas")
y = s.tree(N(["Configuração usada nos testes do Baja", "escolhida com evidência"], kind="final"),
           [N(["P01. Equipe sabe se a", "configuração em uso", "pode continuar"], kind="final"),
            N(["P02. Saber se a nova", "configuração melhora", "e qual seguir no", "próximo experimento"], kind="final"),
            N(["P03. Configuração do", "ciclo escolhida e", "sustentada perante", "a coordenação"], kind="final")],
           y, 80, 1360, gap=40, pw=600) + 20

y = s.section(y, "Objetivos instrumentais diretos — P01 (Rafael)")
y = s.tree(N(["P01. Equipe sabe se a configuração", "em uso pode continuar"], kind="final"),
           [d("O04"), d("O05"), d("O08"),
            N(["Grupo da", "equipe", "informado"], dashed=True)],
           y, 160, 1280, gap=30, pw=560) + 20

y = s.section(y, "Objetivos instrumentais diretos — P03 (Larissa)")
y = s.tree(N(["P03. Configuração do ciclo escolhida", "e sustentada perante a coordenação"], kind="final"),
           [d("O06"), d("O08"), d("O10")],
           y, 280, 1160, gap=40, pw=560) + 20

y = s.section(y, "Objetivos instrumentais diretos — P02 (Andreia)")
y = s.tree(N(["P02. Saber se a nova configuração melhora", "e qual seguir no próximo experimento"], kind="final"),
           [d("O02"), d("O05"), d("O06"), d("O08"),
            N(["Validação em", "campo pedida e", "conclusão levada", "à reunião"], dashed=True)],
           y, 40, 1400, gap=16, pw=640) + 20

y = s.section(y, "Objetivos instrumentais indiretos")
y1 = s.tree(d("O04"), [i("O03"), N(["Entradas obtidas", "(imagens e vídeos)"], dashed=True, kind="indireto")],
            y, 40, 520, gap=20, pw=300)
y2 = s.tree(d("O05"), [i("O03")], y, 580, 860, gap=20, pw=260)
y3 = s.tree(d("O02"), [i("O01")], y, 920, 1180, gap=20, pw=240)
y = max(y1, y2, y3) + 20
y1 = s.tree(d("O06"), [i("O07"), N(["Execuções e", "avaliações pedidas", "a um colega"], dashed=True, kind="indireto")],
            y, 40, 620, gap=20, pw=300)
y2 = s.tree(d("O10"), [i("O09"), N(["Decisão", "discutida na", "reunião"], dashed=True, kind="indireto")],
            y, 720, 1300, gap=20, pw=300)
y = max(y1, y2) + 20

y = s.goal_legend(y, [
    "Um mesmo objetivo pode servir a mais de uma persona (O05, O06 e O08) ou a mais de um objetivo (O03 serve a O04 e a O05); ele aparece em cada lugar.",
    "O05 reúne T03 (P01) e T07 (P02); O08 reúne as conclusões da validação (P01), do experimento (P02) e a recomendação (P03). O07 também apoia O09.",
    "Os IDs O01–O10 e os subtópicos O01.1… (tabela da seção 3.2 da Entrega 9) são os usados nas Entregas 10 a 12.",
    "[H]: proposta derivada de proto-personas, a revisar depois da coleta da Entrega 7."])

s.save(OUT, y)
print(OUT.name, y)
