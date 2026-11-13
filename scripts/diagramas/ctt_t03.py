"""CTT da T03 — Comparar o resultado de uma imagem entre configurações (P01, Tiago).
Leitura da árvore: docs/05_analise_tarefas.md, seção 2.3."""
from pathlib import Path
from ihc_svg import Svg

OUT = Path(__file__).resolve().parents[2] / "assets/05_tarefas/ctt_t03_comparar_configuracoes.svg"

s = Svg("CTT — T03: Comparar o resultado de uma imagem entre configurações",
        "CTT da tarefa T03 por Tiago Fagundes dos Santos. Painéis de decomposição com tipos de tarefa "
        "(abstrata, usuário, interação, sistema) e relações temporais. Motivação externa M antes da sessão R; "
        "iteração por configuração; processamento do sistema comunicando o estado. Modelo hipotético a validar.")
y = s.header("CTT — T03: Comparar o resultado de uma imagem entre configurações",
             "Tiago Fagundes dos Santos · 22.123.017-0 · P01, Rafael Pereira · C01 · Uso proposto [H]")

y = s.panel(y, "Motivação externa antes da sessão de uso [H]",                                   # 0
            ("A", ["T03. Motivação e sessão de uso"]),
            [("U", ["M. Desconfiar de um resultado", "e decidir comparar configurações"]),
             ("A", ["R. Sessão de comparação"])], ["[]>>"], 200, 1240,
            note=["M é ação de Rafael fora da interface: no teste de campo, uma segmentação parece errada (ex.: a pista coberta por uma única cor, C01).",
                  "M []>> R: a imagem e a dúvida passam para a sessão; R é detalhada nos painéis seguintes."])
y = s.panel(y, "R — sessão de comparação",                                                       # 1
            ("A", ["R. Sessão de comparação"]),
            [("A", ["1. Preparar a", "comparação"]),
             ("A", ["V. Executar e avaliar", "cada configuração"]),
             ("A", ["4. Concluir a", "comparação"])], ["[]>>", "[]>>"], 120, 1320)
y = s.panel(y, "1 — Preparar a comparação",                                                      # 2
            ("A", ["1. Preparar a comparação"]),
            [("I", ["1.1. Selecionar a", "imagem de campo"]),
             ("S", ["S1. Exibir as", "configurações", "disponíveis"]),
             ("I", ["1.2. Escolher as", "configurações a comparar"])], ["[]>>", "[]>>"], 120, 1320)
y = s.panel(y, "V — repetir para cada configuração",                                             # 3
            ("A", ["V. Executar e avaliar cada configuração"]),
            [("A", ["C*. Executar e avaliar", "uma configuração"]),
             ("U", ["F. Reconhecer que todas as", "configurações foram tratadas"])], ["[>"], 200, 1240,
            note=["C* repete-se para cada configuração escolhida em 1.2. F desativa a repetição quando não resta configuração a tratar."])
y = s.panel(y, "C — uma configuração",                                                           # 4
            ("A", ["C. Executar e avaliar uma configuração"]),
            [("A", ["2. Obter o resultado (T02)"]), ("A", ["3. Avaliar o resultado (T01)"])], ["[]>>"], 200, 1240,
            note=["3 só é habilitada se 2 terminar com resultado pronto (2.3.1). Se a configuração for retirada em 2.3.2.2, C termina sem 3."])
y = s.panel(y, "2 — Obter o resultado de uma configuração (T02)",                                # 5
            ("A", ["2. Obter o resultado de uma configuração"]),
            [("I", ["2.1. Iniciar a segmentação", "com a configuração"]),
             ("A", ["P. Processamento"]),
             ("A", ["2.3. Conferir o desfecho", "da execução"])], ["[]>>", "[]>>"], 120, 1320)
y0 = y
ya = s.panel(y0, "P e 2.3 — processamento e desfecho",                                           # 6
             ("A", ["P. Processamento"]),
             [("S", ["S2. Processar", "a imagem"]), ("I", ["2.2. Acompanhar", "o estado"])], ["|[]|"], 40, 680,
             note=["S2 informa o estado a 2.2: processando,", "concluído ou falhou."])
yb = s.panel(y0 + 54, None,
             ("A", ["2.3. Conferir o desfecho"]),
             [("U", ["2.3.1. Reconhecer o", "resultado pronto"]), ("A", ["2.3.2. Tratar a", "falha da execução"])],
             ["[]"], 760, 1400)
s.divider(720, y0 + 54, max(ya, yb) - 10)
y = max(ya, yb)
y = s.panel(y, "2.3.2 — tratar a falha da execução",                                             # 7
            ("A", ["2.3.2. Tratar a falha da execução"]),
            [("I", ["2.3.2.1. Ler a causa da falha"]),
             ("U", ["2.3.2.2. Decidir repetir ou", "retirar a configuração"])], ["[]>>"], 200, 1240,
            note=["Repetir volta a 2.1 com a mesma configuração; retirar encerra C para essa configuração sem avaliação."])
y = s.panel(y, "3 — Avaliar o resultado (T01)",                                                  # 8
            ("A", ["3. Avaliar o resultado"]),
            [("S", ["S3. Exibir imagem,", "máscara e legenda"]),
             ("A", ["3.1. Visualizar", "o resultado"]),
             ("I", ["3.2. Interpretar as", "classes pela legenda"]),
             ("A", ["3.3. Julgar a", "qualidade"])], ["[]>>", "[]>>", "[]>>"])
y0 = y
ya = s.panel(y0, "3.1 e 3.3 — visualizar e julgar",                                              # 9
             ("A", ["3.1. Visualizar o resultado"]),
             [("I", ["3.1.1. Comparar", "lado a lado"]), ("I", ["3.1.2. Sobrepor com", "opacidade"])],
             ["[]"], 40, 640)
yb = s.panel(y0 + 54, None,
             ("A", ["3.3. Julgar a qualidade"]),
             [("U", ["3.3.1. Julgar", "pela inspeção", "visual"]),
              ("I", ["3.3.2. Consultar", "a confiança", "do modelo [H]"]),
              ("I", ["3.3.3. Conferir", "as métricas", "por classe"])],
             ["[]", "[]"], 700, 1400)
s.divider(670, y0 + 54, max(ya, yb) - 10)
y = max(ya, yb)
y = s.panel(y, "4 — Concluir a comparação",                                                      # 10
            ("A", ["4. Concluir a comparação"]),
            [("I", ["Q. Abrir a comparação", "entre configurações"]),
             ("S", ["S4. Exibir os", "resultados lado", "a lado"]),
             ("I", ["4.1. Comparar as", "configurações na", "mesma região"]),
             ("A", ["4.2. Registrar a", "conclusão"]),
             ("U", ["4.3. Comunicar a", "conclusão à equipe"])], ["[]>>", "[]>>", "[]>>", "[]>>"])
y = s.panel(y, "4.2 — registrar a conclusão",                                                    # 11
            ("A", ["4.2. Registrar a conclusão"]),
            [("U", ["4.2.1. Indicar a", "configuração", "mais adequada"]),
             ("U", ["4.2.2. Registrar que", "nenhuma é adequada"]),
             ("U", ["4.2.3. Registrar", "resultado inconclusivo"])], ["[]", "[]"], 120, 1320,
            note=["4.3 acontece fora da interface (mensagem ou reunião da equipe)."])
H = s.ctt_legend(y, ["[]>>  ativação com passagem de informação", "[]  escolha",
                     "|[]|  concorrência com comunicação", "[>  desativação", "T*  iteração"],
                 ["Letras (M, R, V, C, F, P, Q, S) marcam nós só do CTT;", "os números seguem o HTA."])

s.save(str(OUT), H)
s.save_crops(str(OUT), H, [
    ("visao_geral", 0, 2, "CTT T03 — visão geral: motivação e sessão"),
    ("detalhe_01", 2, 5, "CTT T03 — detalhamento 1: preparar e repetir por configuração"),
    ("detalhe_02", 5, 8, "CTT T03 — detalhamento 2: obter o resultado (T02)"),
    ("detalhe_03", 8, 10, "CTT T03 — detalhamento 3: avaliar o resultado (T01)"),
    ("detalhe_04", 10, None, "CTT T03 — detalhamento 4: concluir a comparação e legenda"),
])
print(OUT.name, H)
