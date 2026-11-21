"""MoLIC M03 — P02 (Andreia) a partir do CI03 (Entrega 10, Mateus).
Leitura do diagrama: docs/10_molic.md, seção M03. Cenas com os IDs do mapa consolidado da Entrega 9.
Revisado em 20/11/2026 (pareceres das Entregas 10 e 11): três conversas, cada uma com um par gco/gcc;
rupturas da execução e conferência do conjunto de teste desenhadas; conversa O11 (tela Datasets)."""
from pathlib import Path
from ihc_svg import Svg
from molic_svg import Molic

OUT = Path(__file__).resolve().parents[2] / "assets/10_molic/molic_m03.svg"

s = Svg("MoLIC M03 — Preparar os dados, treinar uma configuração e compará-la (P02, CI03)",
        "Diagrama MoLIC por Mateus Marana Assuena a partir do cenário de interação CI03. Três conversas: "
        "treinar e avaliar uma nova configuração (O01, O02), preparar os dados de treino e de teste (O11) e "
        "comparar a nova configuração e concluir o experimento (O03, O05, O06, O07, O08).")
s.header("MoLIC M03 — Preparar os dados, treinar e comparar",
         "Mateus Marana Assuena · 22.123.026-1 · P02, Andreia Silva · CI03 · O01–O03, O05–O08, O11 · Proposta [H]")
m = Molic(s)

L, M, M2, R = 300, 830, 800, 1230          # centros das colunas
WL, WM, WR = 360, 330, 330
TERMO = "d+u: o que é este termo? (O07.1)"

# ================================================================ conversa 1: treinar e avaliar
op = m.opening(L, 150)
c1 = m.scene(L, 230, WL, ["O01.1 Escolher o modelo e os", "parâmetros"],
             ["d+u: modelo", "d+u: parâmetros de treino, com os",
              "       valores padrão: épocas, early", "       stopping e paciência, datasets",
              "       de treino, batch size, gráficos", "d: [PA] só datasets montados; pelo",
              "    menos um para continuar", TERMO])
m.arrow([(L, op["b"]), (L, c1["y"])], ["u: treinar uma nova configuração", "gco: treinar e avaliar uma nova configuração"],
        at=(L + 12, 182))
c2 = m.scene(L, c1["b"] + 90, WL, ["O01.2 Nomear a configuração"],
             ["d: nome sugerido: modelo + épocas", "    (nunca repete um nome)", "d+u: nome (a sugestão pode ser",
              "       editada)"])
m.arrow([(L, c1["b"]), (L, c2["y"])], ["u: continuar"], at=(L + 12, c1["b"] + 50))
p1 = m.process(L, c2["b"] + 75)
m.arrow([(L, c2["b"]), (L, p1["y"])], ["u: iniciar o treino"], at=(L - 12, c2["b"] + 32), anchor="end")
m.arrow([(p1["r"], p1["cy"]), (540, p1["cy"]), (540, c2["cy"]), (c2["r"], c2["cy"])],
        ["d: [RA] nome editado já", "existe: escolha outro"], at=(552, c2["cy"] + 30), dashed=True)

c3 = m.scene(L, p1["b"] + 130, WL, ["O02.1 Acompanhar o treino"],
             ["d: estado do treino: na fila |", "    treinando | concluído | falhou",
              "d: época atual e total; gráficos", "    de treino e validação",
              "d: avaliação no conjunto de teste:", "    na fila | processando | concluída",
              "d: [PP] o treino continua só enquanto", "    o programa estiver aberto"])
m.arrow([(L, p1["b"]), (L, c3["y"])], ["d: treino na fila", "ou iniciado"], at=(L - 12, p1["b"] + 45), anchor="end")

au1 = m.ubiquitous(M, p1["cy"])
m.arrow([(M, au1["b"]), (M, c3["y"] - 40), (420, c3["y"] - 40), (420, c3["y"])],
        ["u: em que ponto está o treino?", "(retoma a conversa)"], at=(M + 12, au1["b"] + 22))

c4 = m.scene(M, c3["y"] + 40, WM, ["Treino ou avaliação interrompidos"],
             ["d: [RA] causa (ex.: falta de memória,", "    programa fechado) e etapa",
              "d: configuração mantida", "d: ajuste sugerido (ex.: batch", "    size menor)"], dashed=True)
yA = c4["y"] + 30
m.arrow([(c3["r"], yA), (c4["x"], yA)], ["d: [RA] falhou"], at=(c3["r"] + 12, yA - 8))
yB = c3["b"] - 24
m.arrow([(c4["x"], yB), (c3["r"], yB)], ["u: reiniciar (com", "o ajuste)"], at=(c3["r"] + 12, yB - 28), dashed=True)

tmp = m.closing_temp(50, c3["b"] + 80)
m.arrow([(140, c3["b"]), (140, tmp["cy"]), (tmp["r"], tmp["cy"])],
        ["u: sair", "(o treino continua", "com o programa", "aberto)"], at=(152, c3["b"] + 18))

c5 = m.scene(L, c3["b"] + 130, WL, ["O02.2 Conferir o resultado do", "treino"],
             ["d: época de término e motivo do", "    término (early stopping)",
              "d: configuração disponível e avaliada:", "    IoU da Trilha, acurácia, tempo de",
              "    inferência e matriz de confusão", "    no conjunto de teste", TERMO])
m.arrow([(L, c3["b"]), (L, c5["y"])], ["d: treino concluído e", "avaliado no conjunto de teste"],
        at=(L + 12, c3["b"] + 40))
end1 = m.closing(M, c5["cy"])
m.arrow([(c5["r"], c5["cy"]), (end1["x"], c5["cy"])],
        ["u: concluir por agora", "gcc: treinar e avaliar uma", "nova configuração"], at=(c5["r"] + 12, c5["cy"] - 46))

# ================================================================ conversa 3: preparar os dados (O11)
au2 = m.ubiquitous(R, 150)
d1 = m.scene(R, 230, WR, ["O11.1 Conferir os datasets"],
             ["d: imagens de treino e de teste de", "    cada dataset; conjunto de teste",
              "    atual", "d: configurações sem avaliação", "    no conjunto de teste"])
m.arrow([(R, au2["b"]), (R, d1["y"])], ["u: preparar os dados (Datasets)", "gco: preparar os dados de treino e de teste"],
        at=(R - 12, au2["b"] + 18), anchor="end")
d2 = m.scene(M2, 250, WM, ["Confirmar a remontagem"],
             ["d: [AL] o conjunto de teste pode", "    mudar; as configurações avaliadas",
              "    terão de ser avaliadas de novo"], dashed=True)
m.arrow([(d1["x"], d2["y"] + 30), (d2["r"], d2["y"] + 30)], ["u: remontar"], at=(d2["r"] + 8, d2["y"] + 22))
m.arrow([(d2["r"], d2["b"] - 20), (d1["x"], d2["b"] - 20)], ["u: cancelar"], at=(d2["r"] + 8, d2["b"] - 28),
        dashed=True)
pd = m.process(M2, d2["b"] + 50)
m.arrow([(M2, d2["b"]), (M2, pd["y"])], ["u: confirmar"], at=(M2 + 12, d2["b"] + 30))
d3 = m.scene(M2, pd["b"] + 60, WM, ["O11.2 Montar o dataset"],
             ["d: estado: processando | concluído |", "    falhou; progresso", "d: conjunto de teste atual"])
m.arrow([(M2, pd["b"]), (M2, d3["y"])], ["d: montagem iniciada"], at=(M2 + 12, pd["b"] + 36))
m.arrow([(d3["r"], d3["cy"]), (1100, d3["cy"]), (1100, d1["b"])], ["d: dataset", "montado"],
        at=(d3["r"] + 12, d3["cy"] - 28))
d4 = m.scene(R, 640, WR, ["O11.3 Avaliar as configurações no", "conjunto de teste"],
             ["d+u: configurações sem avaliação", "d: conjunto de teste atual"])
m.arrow([(R + 60, d1["b"]), (R + 60, d4["y"])], ["u: avaliar as", "selecionadas"], at=(R + 48, d4["y"] - 40),
        anchor="end")
pe = m.process(R, d4["b"] + 60)
m.arrow([(R, d4["b"]), (R, pe["y"])], ["u: avaliar"], at=(R - 12, d4["b"] + 34), anchor="end")
m.arrow([(pe["r"], pe["cy"]), (1420, pe["cy"]), (1420, d4["cy"]), (d4["r"], d4["cy"])],
        ["d: [RA] falhou:", "tentar de novo"], at=(1412, d4["b"] + 20), anchor="end", dashed=True)
end3 = m.closing(R, pe["b"] + 80)
m.arrow([(R, pe["b"]), (R, end3["y"])], ["d: avaliação concluída", "gcc: preparar os dados de", "treino e de teste"],
        at=(R - 12, pe["b"] + 22), anchor="end")

# ================================================================ conversa 2: comparar e concluir
c6 = m.scene(L, c5["b"] + 170, WL, ["O03.1 Enviar as entradas e escolher", "as configurações"],
             ["d+u: imagens ou vídeos do teste", "       (o sistema extrai os quadros)",
              "d+u: configurações a comparar, com", "       descrição e métricas no", "       conjunto de teste", TERMO])
m.arrow([(L, c5["b"]), (L, c6["y"])], ["u: comparar com outra configuração no vídeo",
                                        "gcc: treinar e avaliar uma nova configuração",
                                        "gco: comparar e concluir o experimento"], at=(L + 12, c5["b"] + 40))
p2 = m.process(L, c6["b"] + 75)
m.arrow([(L, c6["b"]), (L, p2["y"])], ["u: executar"], at=(L - 12, c6["b"] + 32), anchor="end")
a1 = m.scene(M, p2["cy"] - 40, WM, ["Arquivos fora do formato aceito"],
             ["d: [AL] quais arquivos não são aceitos", "    e os formatos aceitos (imagens JPG",
              "    ou PNG, vídeos MP4)"], dashed=True)
m.arrow([(p2["r"], p2["cy"]), (a1["x"], p2["cy"])], ["d: [AL] formato", "não aceito"],
        at=(p2["r"] + 30, p2["cy"] - 30))
m.arrow([(M, a1["y"]), (M, c6["y"] + 60), (c6["r"], c6["y"] + 60)], ["u: trocar os arquivos"],
        at=(c6["r"] + 12, c6["y"] + 50), dashed=True)
c7 = m.scene(L, a1["b"] + 75, WL, ["O03.2 Acompanhar o processamento"],
             ["d: estado: na fila | processando |", "    concluído | falhou", "d: progresso (quadros concluídos)",
              "d: configuração em execução"])
m.arrow([(L, p2["b"]), (L, c7["y"])], ["d: entradas aceitas", "(quadros extraídos)"], at=(L - 12, p2["b"] + 40),
        anchor="end")
ys = a1["b"] - 20
m.arrow([(a1["x"], ys), (380, ys), (380, c7["y"])], ["u: seguir sem eles", "(os aceitos entram na fila)"],
        at=(a1["x"] - 10, ys - 25), anchor="end")
a2 = m.scene(M, c7["y"] + 20, WM, ["Falha na execução"],
             ["d: [RA] causa da falha e quadro", "    afetado; os outros seguem",
              "d: [CE] falha na configuração inteira", "    ou solução fora do sistema: diz", "    o que fazer",
              "u: tentar de novo | deixar de fora"], dashed=True)
yA = c7["y"] + 40
m.arrow([(c7["r"], yA), (a2["x"], yA)], ["d: [RA] falhou"], at=(c7["r"] + 12, yA - 8))
yB = c7["b"] - 24
m.arrow([(a2["x"], yB), (c7["r"], yB)], ["u: tentar de novo /", "deixar de fora"], at=(c7["r"] + 12, yB - 36),
        dashed=True)

c8 = m.scene(L, max(c7["b"], a2["b"]) + 110, WL, ["O05.2 Comparar na mesma imagem", "e região"],
             ["d: imagem original, máscara de cada", "    configuração e sobreposição, ao", "    mesmo tempo",
              "d: legenda (Trilha, Fora da trilha)", "d+u: quadro e região ampliada"])
m.arrow([(L, c7["b"]), (L, c8["y"])], ["d: concluído", "precond: comparação"], at=(L + 12, c7["b"] + 40))

p3 = m.process(L, c8["b"] + 110)
m.arrow([(L, c8["b"]), (L, p3["y"])], ["u: comparar as", "métricas"], at=(L + 12, c8["b"] + 30))
end_ce = m.closing(50, p3["cy"])
m.arrow([(p3["x"], p3["cy"]), (end_ce["r"], p3["cy"])],
        ["d: [CE] sem avaliação no", "conjunto de teste: qual;", "avaliá-la em Datasets", "(O11.3)"],
        at=(70, p3["cy"] - 75), dashed=True)
a3 = m.scene(M, p3["cy"] - 40, WM, ["O06.2 Conferir se a", "comparação é válida"],
             ["d: [AL] conjuntos de teste", "    diferentes: conjunto de cada", "    configuração"], dashed=True)
m.arrow([(p3["r"], p3["cy"]), (a3["x"], p3["cy"])], ["d: [AL] conjuntos de", "teste diferentes"],
        at=(p3["r"] + 40, p3["cy"] + 22))
m.arrow([(M, a3["y"]), (M, c8["y"] + 60), (c8["r"], c8["y"] + 60)], ["u: voltar aos quadros"],
        at=(c8["r"] + 12, c8["y"] + 50), dashed=True)

c9 = m.scene(L, p3["b"] + 130, WL, ["O06.3 Ler o desempenho de cada", "configuração"],
             ["d: IoU da Trilha, acurácia e tempo", "    de inferência (conjunto de teste)",
              "d: valor de referência e sua origem:", "    configuração em uso (a última", "    executada)",
              "d: maior valor (não é recomendação);", "    diferença entre configurações",
              "d: [PP] quadros sem anotação de", "    referência: avaliação visual", TERMO])
m.arrow([(L, p3["b"]), (L, c9["y"])], ["d: avaliadas no mesmo", "conjunto de teste"], at=(L + 12, p3["b"] + 70))
m.arrow([(M, a3["b"]), (M, a3["b"] + 36), (c9["r"] + 70, a3["b"] + 36), (c9["r"] + 70, c9["y"] + 26),
         (c9["r"], c9["y"] + 26)], ["u: comparar mesmo assim"], at=(c9["r"] + 80, a3["b"] + 28))

c10 = m.scene(M, c9["y"] + 10, WM, ["O07.2 Julgar a diferença entre", "configurações"],
              ["d: diferença entre configurações", "d: o que a métrica indica e o", "    que não indica", TERMO])
c11 = m.scene(M, c10["b"] + 12, WM, ["O06.4 Consultar a matriz de", "confusão"],
              ["d: matriz de confusão de cada", "    configuração (conjunto de teste)",
               "d: quanto de Trilha foi marcado", "    como Fora da trilha, e o contrário"])
ys = [c9["y"] + 50, c9["y"] + 130, c9["y"] + 196, c9["y"] + 250]
m.arrow([(c9["r"], ys[0]), (c10["x"], ys[0])], ["u: a diferença importa?"], at=(c9["r"] + 8, ys[0] - 7))
m.arrow([(c10["x"], ys[1]), (c9["r"], ys[1])], ["u: voltar à análise"], at=(c9["r"] + 8, ys[1] - 7))
m.arrow([(c9["r"], ys[2]), (c11["x"], ys[2])], ["u: onde cada uma erra?"], at=(c9["r"] + 8, ys[2] - 7))
m.arrow([(c11["x"], ys[3]), (c9["r"], ys[3])], ["u: voltar à análise"], at=(c9["r"] + 8, ys[3] - 7))

c12 = m.scene(L, max(c9["b"], c11["b"]) + 120, WL, ["O08.1 Informar a conclusão", "(experimento)"],
              ["d+u: conclusão", "d+u: configuração candidata (ou", "       nenhuma)",
               "d+u: ressalva e próximo experimento", "d: tipo de conclusão: experimento"])
m.arrow([(L, c9["b"]), (L, c12["y"])], ["u: registrar a conclusão"], at=(L + 12, c9["b"] + 45))
p4 = m.process(L, c12["b"] + 65)
m.arrow([(L, c12["b"]), (L, p4["y"])], ["u: registrar"], at=(L - 12, c12["b"] + 34), anchor="end")
c13 = m.scene(L, p4["b"] + 90, WL, ["O08.2 Conferir a conclusão"],
              ["d: conclusão, configuração candidata,", "    ressalva e próximo experimento",
               "    registrados junto da comparação"])
m.arrow([(L, p4["b"]), (L, c13["y"])], ["d: conclusão registrada"], at=(L + 12, p4["b"] + 40))
m.arrow([(c13["x"], c13["cy"] + 15), (80, c13["cy"] + 15), (80, c12["cy"]), (c12["x"], c12["cy"])],
        ["u: corrigir"], at=(88, c12["b"] + 40), dashed=True)
end2 = m.closing(L, c13["b"] + 80)
m.arrow([(L, c13["b"]), (L, end2["y"])], ["u: confirmar", "gcc: comparar e concluir o experimento"],
        at=(L + 12, c13["b"] + 28))

y = end2["b"] + 40
y = s.note(y, ["Três conversas, cada uma com um par gco/gcc. (1) Treinar e avaliar uma nova configuração: ao fim do treino, o sistema",
               "avalia a configuração no conjunto de teste, e só então as métricas aparecem. Andreia pode sair durante o treino",
               "(encerramento temporário) e voltar pelo acesso ubíquo, enquanto o programa estiver aberto. (2) Preparar os dados",
               "(tela Datasets, coluna da direita): conferir os datasets, montar o dataset e avaliar configurações sem avaliação.",
               "(3) Comparar e concluir o experimento: O03.1, O03.2, O05.2, O06.2, O06.3 e O07.2 são as mesmas cenas do M01 e do",
               "M02 (reuso), com as mesmas rupturas. O07.1 é um diálogo das cenas que mostram termos técnicos.",
               "Fora do sistema: pedir a validação em campo e levar a conclusão à reunião (RQ09). Proposta [H]."]) + 20
H = m.legend(y)
s.save(OUT, H)
print(OUT.name, H)
