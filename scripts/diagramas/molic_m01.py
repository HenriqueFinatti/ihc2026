"""MoLIC M01 — P01 (Rafael) a partir do CI01 (Entrega 10, Tiago).
Leitura do diagrama: docs/10_molic.md, seção M01. Cenas com os IDs do mapa consolidado da Entrega 9."""
from pathlib import Path
from ihc_svg import Svg
from molic_svg import Molic

OUT = Path(__file__).resolve().parents[2] / "assets/10_molic/molic_m01.svg"

s = Svg("MoLIC M01 — Executar, avaliar e comparar a segmentação das imagens do teste (P01, CI01)",
        "Diagrama MoLIC por Tiago Fagundes dos Santos a partir do cenário de interação CI01. "
        "Uma conversa: executar a segmentação das imagens do teste (O03), avaliar cada imagem (O04), "
        "comparar as imagens duvidosas com outra configuração (O05) e registrar a conclusão da validação (O08).")
s.header("MoLIC M01 — Executar, avaliar e comparar a segmentação",
         "Tiago Fagundes dos Santos · 22.123.017-0 · P01, Rafael Pereira · CI01 · O03, O04, O05, O08 · Proposta [H]")
m = Molic(s)

L, M, R = 300, 830, 1230          # centros das colunas
WL, WM, WR = 360, 330, 330
XR = 1425                          # corredor da direita (reuso de O03.2)

# ---------------------------------------------------------------- O03: executar a segmentação
op = m.opening(L, 150)
c1 = m.scene(L, 230, WL, ["O03.1 Enviar as entradas e escolher", "as configurações"],
             ["d+u: imagens ou vídeos do teste", "       (o sistema extrai os quadros)", "d+u: configurações disponíveis, com",
              "       descrição e métricas no", "       conjunto de teste"])
m.arrow([(L, op["b"]), (L, c1["y"])], ["u: segmentar as imagens do teste", "gco: executar a segmentação (O03)"],
        at=(L + 12, 182))
p1 = m.process(L, c1["b"] + 75)
m.arrow([(L, c1["b"]), (L, p1["y"])], ["u: executar"], at=(L - 12, c1["b"] + 32), anchor="end")

c2 = m.scene(M, p1["cy"] - 40, WM, ["Imagens fora do formato aceito"],
             ["d: [AL] quais imagens não são", "    aceitas e quais formatos são", "    aceitos"], dashed=True)
m.arrow([(p1["r"], p1["cy"]), (c2["x"], p1["cy"])], ["d: [AL] formato", "não aceito"],
        at=(p1["r"] + 30, p1["cy"] - 30))
m.arrow([(M, c2["y"]), (M, c1["y"] + 60), (c1["r"], c1["y"] + 60)], ["u: trocar os arquivos"],
        at=(c1["r"] + 12, c1["y"] + 50), dashed=True)

c3 = m.scene(L, 600, WL, ["O03.2 Acompanhar o processamento"],
             ["d: estado: processando | concluído |", "    falhou", "d: progresso (imagens concluídas)",
              "d: configuração em execução"])
m.arrow([(L, p1["b"]), (L, c3["y"])], ["d: imagens", "aceitas"], at=(L - 12, p1["b"] + 45), anchor="end")
ys = c2["b"] - 20
m.arrow([(c2["x"], ys), (380, ys), (380, c3["y"])], ["u: seguir sem elas"], at=(c2["x"] - 10, ys - 8), anchor="end")

c4 = m.scene(M, c3["y"] + 20, WM, ["Falha na execução"],
             ["d: [RA] causa da falha e imagem", "    afetada; as outras seguem",
              "d: [CE] se a solução está fora do", "    sistema, diz o que fazer",
              "u: tentar de novo | deixar a", "    imagem de fora"], dashed=True)
yA = c3["y"] + 40
m.arrow([(c3["r"], yA), (c4["x"], yA)], ["d: [RA] falhou"], at=(c3["r"] + 12, yA - 8))
yB = c3["b"] - 24
m.arrow([(c4["x"], yB), (c3["r"], yB)], ["u: tentar de novo /", "deixar de fora"],
        at=(c3["r"] + 12, yB - 36), dashed=True)

# ---------------------------------------------------------------- O04: avaliar cada imagem
c5 = m.scene(L, c3["b"] + 130, WL, ["O04.1 Ver o resultado sobre a", "imagem"],
             ["d: imagem original e máscara, com a", "    legenda (Trilha, Fora da trilha)",
              "d+u: sobreposição e transparência", "d+u: região ampliada",
              "u: baixar o vídeo com a sobreposição", "    (MP4, quando a entrada é vídeo)"])
m.arrow([(L, c3["b"]), (L, c5["y"])], ["d: concluído", "precond: execução inicial", "gco: avaliar a segmentação (O04)"],
        at=(L - 12, c3["b"] + 28), anchor="end")

c6 = m.scene(M, c5["y"] + 17, WM, ["O04.2 Conferir se há métricas"],
             ["d: IoU e acurácia, se a imagem tem", "    anotação de referência",
              "d: [PP] sem anotação: não há", "    métricas; avaliação visual"])
y1 = c6["y"] + 40
m.arrow([(c5["r"], y1), (c6["x"], y1)], ["u: qual é o IoU?"], at=(c5["r"] + 12, y1 - 8))
y2 = c6["b"] - 24
m.arrow([(c6["x"], y2), (c5["r"], y2)], ["u: voltar à imagem"], at=(c5["r"] + 12, y2 - 8))

c7 = m.scene(L, c5["b"] + 110, WL, ["O04.3 Registrar a avaliação da", "imagem"],
             ["d+u: avaliação: correta | duvidosa", "d+u: origem do problema: imagem", "       (captura) | modelo"])
m.arrow([(L, c5["b"]), (L, c7["y"])], ["u: avaliar esta imagem"], at=(L + 12, c5["b"] + 40))
m.arrow([(c7["x"], c7["cy"]), (80, c7["cy"]), (80, c5["cy"]), (c5["x"], c5["cy"])], ["u: próxima", "imagem"],
        at=(88, c5["b"] + 42))

# ---------------------------------------------------------------- O05: comparar com outra configuração
c9 = m.scene(R, c6["y"], WR, ["O05.2 Comparar na mesma imagem", "e região"],
             ["d: as configurações lado a lado, na", "    mesma região ampliada", "d: avaliação registrada da imagem"])
yc = c4["b"] + 31
m.arrow([(440, c3["b"]), (440, yc), (R, yc), (R, c9["y"])], ["d: concluído", "precond: comparação"],
        at=(452, c3["b"] + 28))

c8 = m.scene(R, c7["y"] - 17, WR, ["O05.1 Escolher as configurações a", "comparar"],
             ["d: configurações disponíveis, com", "    descrição e métricas no conjunto", "    de teste",
              "d: configurações já executadas", "    nestas imagens", "u: imagens duvidosas"])
yv = c7["y"] + 33
m.arrow([(c9["x"], c9["b"] - 25), (1030, c9["b"] - 25), (1030, yv), (c7["r"], yv)], ["u: voltar à avaliação"],
        at=(c7["r"] + 12, yv - 8))
yd = c7["b"] - 32
m.arrow([(c7["r"], yd), (c8["x"], yd)], ["u: comparar as duvidosas", "gco: comparar (O05)"],
        at=(c7["r"] + 12, yd - 25))
yr = c3["y"] - 30
m.arrow([(c8["r"], c8["y"] + 40), (XR, c8["y"] + 40), (XR, yr), (440, yr), (440, c3["y"])],
        ["u: executar nas imagens duvidosas (reuso de O03.2)"], at=(c2["x"] + 30, yr - 8))

# ---------------------------------------------------------------- O08: registrar a conclusão
c10 = m.scene(L, c7["b"] + 130, WL, ["O08.1 Informar a conclusão", "(validação)"],
              ["d+u: configuração mais adequada", "d+u: imagens inconclusivas e com",
               "       problema na imagem (captura)", "d: tipo de conclusão: validação"])
m.arrow([(L, c7["b"]), (L, c10["y"])], ["u: registrar a conclusão", "gco: registrar a conclusão (O08)"],
        at=(L + 12, c7["b"] + 35))
p3 = m.process(L, c10["b"] + 65)
m.arrow([(L, c10["b"]), (L, p3["y"])], ["u: registrar"], at=(L - 12, c10["b"] + 34), anchor="end")

c11 = m.scene(M, p3["cy"] - 40, WM, ["Imagens sem avaliação"],
              ["d: [AL] quantas imagens ainda não", "    têm avaliação"], dashed=True)
m.arrow([(p3["r"], p3["cy"]), (c11["x"], p3["cy"])], ["d: [AL] imagens", "sem avaliação"],
        at=(p3["r"] + 30, p3["cy"] - 30))
xa = M - 100
ya = c7["b"] - 12
m.arrow([(xa, c11["y"]), (xa, ya), (c7["r"], ya)], ["u: avaliá-las antes"], at=(xa + 12, c10["y"] + 30), dashed=True)

c12 = m.scene(L, p3["b"] + 90, WL, ["O08.2 Conferir a conclusão"],
              ["d: configuração, imagens inconclusivas", "    e problemas de captura registrados"])
m.arrow([(L, p3["b"]), (L, c12["y"])], ["d: conclusão registrada"], at=(L + 12, p3["b"] + 40))
m.arrow([(M, c11["b"]), (M, c12["y"] + 30), (c12["r"], c12["y"] + 30)], ["u: concluir assim mesmo"],
        at=(M + 12, c11["b"] + 30))
m.arrow([(c12["x"], c12["cy"] + 15), (80, c12["cy"] + 15), (80, c10["cy"]), (c10["x"], c10["cy"])],
        ["u: corrigir"], at=(88, c10["b"] + 40), dashed=True)
end = m.closing(L, c12["b"] + 80)
m.arrow([(L, c12["b"]), (L, end["y"])], ["u: confirmar", "gcc: validar a segmentação (O03–O05, O08)"],
        at=(L + 12, c12["b"] + 28))

y = end["b"] + 40
y = s.note(y, ["Uma conversa, aberta pelo objetivo de executar a segmentação: Rafael executa, avalia imagem a imagem,",
               "compara as imagens duvidosas com outra configuração e registra a conclusão da validação.",
               "O03.2 é a mesma cena na execução inicial e na execução da outra configuração (reuso); a precondição",
               "diz para onde a conversa segue quando o processamento termina.",
               "Fora do sistema: descarregar as imagens das câmeras e informar o grupo da equipe (RQ09). Proposta [H]."]) + 20
H = m.legend(y)
s.save(OUT, H)
print(OUT.name, H)
