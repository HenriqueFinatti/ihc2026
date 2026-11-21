"""MoLIC M02 — P03 (Larissa) a partir do CI02 (Entrega 10, Henrique).
Leitura do diagrama: docs/10_molic.md, seção M02. Cenas com os IDs do mapa consolidado da Entrega 9."""
from pathlib import Path
from ihc_svg import Svg
from molic_svg import Molic

OUT = Path(__file__).resolve().parents[2] / "assets/10_molic/molic_m02.svg"

s = Svg("MoLIC M02 — Comparar, recomendar e registrar a decisão (P03, CI02)",
        "Diagrama MoLIC por Henrique Finatti Silveira Belo Trebbi a partir do cenário de interação CI02. "
        "Conversa 1: comparar o desempenho consolidado das configurações do ciclo e registrar a recomendação "
        "(O06, O07, O08). Conversa 2: apresentar a recomendação à coordenação e registrar a decisão (O09, O10).")
s.header("MoLIC M02 — Comparar, recomendar e registrar a decisão",
         "Henrique Finatti Silveira Belo Trebbi · 22.123.030-3 · P03, Larissa Camargo · CI02 · O06–O10 · Proposta [H]")
m = Molic(s)

L, M, R = 280, 800, 1230          # centros das colunas
WL, WM, WR = 340, 320, 340

# ---------------------------------------------------------------- conversa 1 (coluna L e M)
op = m.opening(L, 150)
c1 = m.scene(L, 240, WL, ["O06.1 Escolher as", "configurações"],
             ["d+u: ciclo de testes", "d+u: configurações com execução concluída", "       (nome, conjunto de teste, data da", "       avaliação)"])
m.arrow([(L, op["b"]), (L, c1["y"])], ["u: comparar as configurações do ciclo", "gco: recomendar uma configuração"],
        at=(L + 12, 182))
p1 = m.process(L, c1["b"] + 75)
m.arrow([(L, c1["b"]), (L, p1["y"])], ["u: comparar as selecionadas"], at=(L + 12, c1["b"] + 32))

end_ce = m.closing(50, p1["cy"])
m.arrow([(p1["x"], p1["cy"]), (end_ce["r"], p1["cy"])],
        ["d: [CE] sem avaliação no", "conjunto de teste: qual;", "peça a avaliação à P02"], at=(70, p1["cy"] - 58), dashed=True)
end_ce2 = m.closing(50, p1["cy"] + 100)
m.arrow([(L - 8, p1["b"]), (L - 8, end_ce2["cy"]), (end_ce2["r"], end_ce2["cy"])],
        ["d: [CE] execução faltante", "no ciclo: qual; peça a", "execução ao integrante", "técnico"], at=(70, end_ce2["cy"] + 22), dashed=True)

c2 = m.scene(M, p1["cy"] - 40, WM, ["O06.2 Conferir se a", "comparação é válida"],
             ["d: [AL] conjuntos de teste", "    diferentes: conjunto de cada", "    configuração"], dashed=True)
m.arrow([(p1["r"], p1["cy"]), (c2["x"], p1["cy"])], ["d: [AL] conjuntos de", "teste diferentes"],
        at=(p1["r"] + 40, p1["cy"] + 22))
m.arrow([(M, c2["y"]), (M, c1["y"] + 60), (c1["r"], c1["y"] + 60)], ["u: escolher outras configurações"],
        at=(c1["r"] + 12, c1["y"] + 50), dashed=True)

c3 = m.scene(L, p1["b"] + 210, WL, ["O06.3 Ler o desempenho de cada", "configuração"],
             ["d: IoU médio e por classe, acurácia,", "    tempo de inferência (conjunto de teste)",
              "d: valor de referência e sua origem:", "    configuração em uso (a última", "    executada)",
              "d: maior valor (não é recomendação);", "    diferença entre configurações",
              "u: tabela | gráfico", "d+u: o que é este termo? (O07.1)"])
m.arrow([(L, p1["b"]), (L, c3["y"])], ["d: avaliadas no mesmo", "conjunto de teste"], at=(L + 12, p1["b"] + 95))
m.arrow([(M, c2["b"]), (M, c2["b"] + 36), (c3["r"] + 70, c2["b"] + 36), (c3["r"] + 70, c3["y"] + 26), (c3["r"], c3["y"] + 26)],
        ["u: comparar mesmo assim"], at=(c3["r"] + 80, c2["b"] + 28))

c4 = m.scene(M, c3["y"] + 70, WM, ["O07.2 Julgar a diferença entre", "configurações"],
             ["d: diferença entre configurações", "d: o que a métrica indica e o", "    que não indica",
              "d+u: o que é este termo? (O07.1)"])
yA = c4["y"] + 46
m.arrow([(c3["r"], yA), (c4["x"], yA)], ["u: a diferença", "importa?"], at=(c3["r"] + 14, yA - 26))
yB = c4["b"] - 24
m.arrow([(c4["x"], yB), (c3["r"], yB)], ["u: voltar à", "análise"], at=(c3["r"] + 14, yB - 30))

c6 = m.scene(L, c3["b"] + 120, WL, ["O08.1 Informar a conclusão", "(recomendação)"],
             ["d+u: configuração indicada", "d+u: ressalva (opcional)", "d: tipo de conclusão: recomendação"])
m.arrow([(L, c3["b"]), (L, c6["y"])], ["u: registrar a recomendação"],
        at=(L + 12, c3["b"] + 40))
p2 = m.process(L, c6["b"] + 60)
m.arrow([(L, c6["b"]), (L, p2["y"])], ["u: registrar"], at=(L + 12, c6["b"] + 32))
c7 = m.scene(L, p2["b"] + 70, WL, ["O08.2 Conferir a conclusão"],
             ["d: configuração, métricas, referência", "    e ressalva registradas"])
m.arrow([(L, p2["b"]), (L, c7["y"])], ["d: recomendação registrada"], at=(L + 12, p2["b"] + 40))
xc = c7["r"] + 50
m.arrow([(c7["r"], c7["cy"]), (xc, c7["cy"]), (xc, c6["cy"]), (c6["r"], c6["cy"])], ["u: corrigir"],
        at=(xc + 8, (c7["cy"] + c6["cy"]) / 2), dashed=True)
end1 = m.closing(L, c7["b"] + 80)
m.arrow([(L, c7["b"]), (L, end1["y"])], ["u: confirmar", "gcc: recomendar uma configuração"],
        at=(L + 12, c7["b"] + 28))

# ---------------------------------------------------------------- conversa 2 (coluna R)
au2 = m.ubiquitous(R, 300)
c8 = m.scene(R, 430, WR, ["O09.1 Retomar a análise"],
             ["d: comparação do ciclo de testes", "d: recomendação e ressalva registradas",
              "d+u: o que é este termo? (O07.1)"])
m.arrow([(R, au2["b"]), (R, c8["y"])], ["u: apresentar a recomendação", "gco: apresentar e registrar a decisão"],
        at=(R - 12, au2["b"] + 30), anchor="end")
xq = c4["r"] + 50
m.arrow([(c8["x"], c8["b"] - 20), (xq, c8["b"] - 20), (xq, c4["y"] + 20), (c4["r"], c4["y"] + 20)],
        ["u: a diferença importa?", "(O09.2)"], at=(xq - 10, c4["y"] - 22), anchor="end")
xb = c4["r"] + 90
m.arrow([(c4["r"], c4["b"] - 20), (xb, c4["b"] - 20), (xb, c8["b"] + 50), (c8["x"] + 40, c8["b"] + 50), (c8["x"] + 40, c8["b"])],
        ["u: voltar à apresentação"], at=(xb + 10, c4["b"] - 8))
c9 = m.scene(R, max(c8["b"] + 260, c4["b"] + 60), WR, ["O10 Registrar a decisão da", "coordenação"],
             ["d+u: decisão: aceita | aceita com", "       condição | adiada",
              "d+u: condição [PA: obrigatória se", "       a decisão é condicionada]"])
m.arrow([(R + 60, c8["b"]), (R + 60, c9["y"])], ["u: registrar a decisão"],
        at=(R + 48, c8["b"] + 110), anchor="end")
p3 = m.process(R, c9["b"] + 60)
m.arrow([(R, c9["b"]), (R, p3["y"])], ["u: registrar"], at=(R + 12, c9["b"] + 32))
end2 = m.closing(R, p3["b"] + 90)
m.arrow([(R, p3["b"]), (R, end2["y"])], ["d: decisão registrada", "gcc: apresentar e registrar a decisão"],
        at=(R - 12, p3["b"] + 30), anchor="end")

y = max(end1["b"], end2["b"]) + 40
y = s.note(y, ["Conversa 1 (colunas da esquerda e do centro), sobre o objetivo de recomendar uma configuração: Larissa compara as",
               "configurações do ciclo e registra a recomendação. Conversa 2 (coluna da direita), sobre apresentar e registrar a decisão:",
               "na reunião, retoma a análise e registra a decisão da coordenação. Cada conversa tem um par gco/gcc.",
               "O07.2 é a mesma cena nas duas conversas. O07.1 (entender um termo) é um diálogo das cenas que mostram termos técnicos:",
               "a explicação aparece na própria cena, que continua a mesma. Proposta derivada de proto-persona [H]."]) + 20
H = m.legend(y)
s.save(OUT, H)
print(OUT.name, H)
