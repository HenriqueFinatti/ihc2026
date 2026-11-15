"""MoLIC M03 — P02 (Andreia) a partir do CI03 (Entrega 10, Mateus).
Leitura do diagrama: docs/10_molic.md, seção M03. Cenas com os IDs do mapa consolidado da Entrega 9."""
from pathlib import Path
from ihc_svg import Svg
from molic_svg import Molic

OUT = Path(__file__).resolve().parents[2] / "assets/10_molic/molic_m03.svg"

s = Svg("MoLIC M03 — Treinar uma configuração e compará-la nos quadros de sombra (P02, CI03)",
        "Diagrama MoLIC por Mateus Marana Assuena a partir do cenário de interação CI03. "
        "Definir uma configuração de treino (O01), treinar o modelo (O02), executar e comparar as configurações "
        "nos mesmos quadros (O03, O05), comparar o desempenho no conjunto de teste (O06, O07) e registrar a "
        "conclusão do experimento (O08).")
s.header("MoLIC M03 — Treinar uma configuração e compará-la",
         "Mateus Marana Assuena · 22.123.026-1 · P02, Andreia Silva · CI03 · O01–O03, O05–O08 · Proposta [H]")
m = Molic(s)

L, M = 300, 830                    # centros das colunas
WL, WM = 360, 330

# ---------------------------------------------------------------- O01: definir a configuração de treino
op = m.opening(L, 150)
c1 = m.scene(L, 230, WL, ["O01.1 Escolher o modelo e os", "parâmetros"],
             ["d+u: modelo", "d+u: parâmetros de treino, com os",
              "       valores padrão: épocas, early", "       stopping e paciência, datasets",
              "       de treino, batch size, gráficos", "d: [PA] pelo menos um dataset de", "    treino para continuar"])
m.arrow([(L, op["b"]), (L, c1["y"])], ["u: treinar uma nova configuração", "gco: definir uma configuração de treino (O01)"],
        at=(L + 12, 182))
c2 = m.scene(L, c1["b"] + 90, WL, ["O01.2 Nomear a configuração"],
             ["d: nome sugerido: modelo + épocas", "d+u: nome da configuração"])
m.arrow([(L, c1["b"]), (L, c2["y"])], ["u: continuar"], at=(L + 12, c1["b"] + 50))
p1 = m.process(L, c2["b"] + 75)
m.arrow([(L, c2["b"]), (L, p1["y"])], ["u: iniciar o treino"], at=(L - 12, c2["b"] + 32), anchor="end")
m.arrow([(p1["r"], p1["cy"]), (540, p1["cy"]), (540, c2["cy"]), (c2["r"], c2["cy"])],
        ["d: [RA] nome repetido:", "escolha outro"], at=(552, c2["cy"] + 30), dashed=True)

# ---------------------------------------------------------------- O02: treinar o modelo
c3 = m.scene(L, p1["b"] + 120, WL, ["O02.1 Acompanhar o treino"],
             ["d: estado do treino: treinando |", "    concluído | falhou", "d: época atual e total",
              "d: gráficos de treino e validação"])
m.arrow([(L, p1["b"]), (L, c3["y"])], ["d: treino iniciado", "gco: treinar o modelo (O02)"],
        at=(L - 12, p1["b"] + 45), anchor="end")

au = m.ubiquitous(M, p1["cy"])
m.arrow([(M, au["b"]), (M, c3["y"] - 44), (420, c3["y"] - 44), (420, c3["y"])],
        ["u: em que ponto está o treino?", "gco: treinar o modelo (O02)"], at=(M + 12, au["b"] + 22))

c4 = m.scene(M, c3["y"] + 26, WM, ["Treino interrompido"],
             ["d: [RA] causa e época em que o", "    treino parou", "d: configuração mantida",
              "d: ajuste sugerido (ex.: batch", "    size menor)"], dashed=True)
yA = c4["y"] + 30
m.arrow([(c3["r"], yA), (c4["x"], yA)], ["d: [RA] falhou"], at=(c3["r"] + 12, yA - 8))
yB = c3["b"] - 24
m.arrow([(c4["x"], yB), (c3["r"], yB)], ["u: reiniciar com", "o ajuste"], at=(c3["r"] + 12, yB - 28), dashed=True)

end0 = m.closing(50, c3["b"] + 80)
m.arrow([(140, c3["b"]), (140, end0["cy"]), (end0["r"], end0["cy"])],
        ["u: sair (o treino", "continua)", "gcc: definir (O01)"], at=(152, c3["b"] + 22))

c5 = m.scene(L, c3["b"] + 130, WL, ["O02.2 Conferir o resultado do", "treino"],
             ["d: época de término e motivo do", "    término (early stopping)",
              "d: IoU da Trilha, acurácia, tempo de", "    inferência e matriz de confusão",
              "    no conjunto de teste", "d: configuração entre as disponíveis"])
m.arrow([(L, c3["b"]), (L, c5["y"])], ["d: treino concluído"], at=(L + 12, c3["b"] + 40))

# ---------------------------------------------------------------- O03 e O05: executar e comparar nos quadros
c6 = m.scene(L, c5["b"] + 130, WL, ["O03.1 Enviar as entradas e escolher", "as configurações"],
             ["d+u: quadros", "d+u: configurações a comparar, com", "       descrição e métricas no",
              "       conjunto de teste"])
m.arrow([(L, c5["b"]), (L, c6["y"])], ["u: comparar com outra configuração", "nestes quadros",
                                        "gco: comparar configurações (O05)"], at=(L + 12, c5["b"] + 30))
p2 = m.process(L, c6["b"] + 75)
m.arrow([(L, c6["b"]), (L, p2["y"])], ["u: executar"], at=(L - 12, c6["b"] + 32), anchor="end")
s.text(p2["r"] + 16, p2["cy"] + 5, "[AL] formato não aceito: como no M01", size=13, anchor="start")

c7 = m.scene(L, p2["b"] + 110, WL, ["O03.2 Acompanhar o processamento"],
             ["d: estado: processando | concluído |", "    falhou", "d: progresso (quadros concluídos)",
              "d: configuração em execução"])
m.arrow([(L, p2["b"]), (L, c7["y"])], ["d: entradas", "aceitas"], at=(L - 12, p2["b"] + 40), anchor="end")
s.text(c7["r"] + 16, c7["cy"] + 5, "[RA] falha na execução: como no M01", size=13, anchor="start")

c8 = m.scene(L, c7["b"] + 130, WL, ["O05.2 Comparar na mesma imagem", "e região"],
             ["d: imagem original, máscara de cada", "    configuração e sobreposição, ao",
              "    mesmo tempo", "d: legenda (Trilha, Fora da trilha)", "d+u: quadro e região ampliada"])
m.arrow([(L, c7["b"]), (L, c8["y"])], ["d: concluído", "precond: comparação"], at=(L + 12, c7["b"] + 40))

# ---------------------------------------------------------------- O06 e O07: desempenho no conjunto de teste
c9 = m.scene(L, c8["b"] + 130, WL, ["O06.3 Ler o desempenho de cada", "configuração"],
             ["d: IoU da Trilha, acurácia e tempo", "    de inferência (conjunto de teste)",
              "d: diferença entre configurações", "d: [PP] quadros sem anotação de",
              "    referência: avaliação visual"])
m.arrow([(L, c8["b"]), (L, c9["y"])], ["u: comparar as métricas", "gco: comparar o desempenho (O06)"],
        at=(L + 12, c8["b"] + 40))

c10 = m.scene(M, c9["y"] - 70, WM, ["O07.2 Julgar a diferença entre", "configurações"],
              ["d: diferença entre configurações", "d: o que a métrica indica e o", "    que não indica"])
c11 = m.scene(M, c10["b"] + 12, WM, ["O06.4 Consultar a matriz de", "confusão"],
              ["d: matriz de confusão de cada", "    configuração (conjunto de teste)",
               "d: quanto de Trilha foi marcado", "    como Fora da trilha, e o contrário"])
ys = [c9["y"] + 20, c9["y"] + 52, c9["y"] + 97, c9["y"] + 140]
m.arrow([(c9["r"], ys[0]), (c10["x"], ys[0])], ["u: a diferença importa?"], at=(c9["r"] + 8, ys[0] - 7))
m.arrow([(c10["x"], ys[1]), (c9["r"], ys[1])], ["u: voltar à análise"], at=(c9["r"] + 8, ys[1] - 7))
m.arrow([(c9["r"], ys[2]), (c11["x"], ys[2])], ["u: onde cada uma erra?"], at=(c9["r"] + 8, ys[2] - 7))
m.arrow([(c11["x"], ys[3]), (c9["r"], ys[3])], ["u: voltar à análise"], at=(c9["r"] + 8, ys[3] - 7))

# ---------------------------------------------------------------- O08: registrar a conclusão
c12 = m.scene(L, max(c9["b"], c11["b"]) + 120, WL, ["O08.1 Informar a conclusão", "(experimento)"],
              ["d+u: conclusão", "d+u: configuração candidata (ou", "       nenhuma)",
               "d+u: ressalva e próximo experimento", "d: tipo de conclusão: experimento"])
m.arrow([(L, c9["b"]), (L, c12["y"])], ["u: registrar a conclusão", "gco: registrar a conclusão (O08)"],
        at=(L + 12, c9["b"] + 45))
p3 = m.process(L, c12["b"] + 65)
m.arrow([(L, c12["b"]), (L, p3["y"])], ["u: registrar"], at=(L - 12, c12["b"] + 34), anchor="end")
c13 = m.scene(L, p3["b"] + 90, WL, ["O08.2 Conferir a conclusão"],
              ["d: conclusão, configuração candidata,", "    ressalva e próximo experimento",
               "    registrados junto da comparação"])
m.arrow([(L, p3["b"]), (L, c13["y"])], ["d: conclusão registrada"], at=(L + 12, p3["b"] + 40))
m.arrow([(c13["x"], c13["cy"] + 15), (80, c13["cy"] + 15), (80, c12["cy"]), (c12["x"], c12["cy"])],
        ["u: corrigir"], at=(88, c12["b"] + 40), dashed=True)
end = m.closing(L, c13["b"] + 80)
m.arrow([(L, c13["b"]), (L, end["y"])], ["u: confirmar", "gcc: comparar e concluir o experimento (O03, O05–O08)"],
        at=(L + 12, c13["b"] + 28))

y = end["b"] + 40
y = s.note(y, ["Andreia define a configuração e inicia o treino; pode sair durante o treino e voltar pelo acesso ubíquo.",
               "Com o treino concluído, compara a nova configuração com outra nos mesmos quadros e no conjunto de teste",
               "e registra a conclusão do experimento.",
               "O03.1, O03.2 e O05.2 são as mesmas cenas do M01; O06.3 e O07.2, as mesmas do M02 (reuso). As rupturas",
               "da execução (formato não aceito e falha) estão desenhadas no M01.",
               "Fora do sistema: extrair os quadros dos vídeos, pedir a validação em campo e levar a conclusão à reunião",
               "(RQ09). Proposta [H]."]) + 20
H = m.legend(y)
s.save(OUT, H)
print(OUT.name, H)
