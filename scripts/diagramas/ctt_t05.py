"""CTT da T05 — Decidir e justificar a adoção de um modelo (P03, Henrique).
Leitura da árvore: docs/05_analise_tarefas.md, seção 1.3."""
from pathlib import Path
from ihc_svg import Svg

OUT = Path(__file__).resolve().parents[2] / "assets/05_tarefas/ctt_t05_decidir_modelo.svg"

s = Svg("CTT — T05: Decidir e justificar a adoção de um modelo",
        "CTT da tarefa T05 por Henrique Finatti Silveira Belo Trebbi. Painéis de decomposição com tipos de "
        "tarefa (abstrata, usuário, interação, sistema) e relações temporais. Motivação externa M antes da "
        "sessão U; recurso ao integrante técnico como suspensão. Modelo hipotético a validar.")
y = s.header("CTT — T05: Decidir e justificar a adoção de um modelo",
             "Henrique Finatti Silveira Belo Trebbi · 22.123.030-3 · P03, Larissa Camargo · C02 · Uso proposto [H]")

y = s.panel(y, "Motivação externa antes da sessão de uso [H]",                                   # 0
            ("A", ["T05. Motivação e sessão de uso"]),
            [("U", ["M. Decidir preparar a recomendação", "ao receber a pauta da reunião"]),
             ("A", ["U. Sessão de decisão"])], ["[]>>"], 200, 1240,
            note=["M é ação de Larissa fora da interface: a reunião semanal com a coordenação pede a definição do modelo para o próximo ciclo.",
                  "M []>> U: o ciclo de testes e a data da reunião passam para a sessão; U é detalhada nos painéis seguintes."])
y = s.panel(y, "Sessão de decisão e recurso ao integrante técnico",                              # 1
            ("A", ["U. Sessão de decisão"]),
            [("A", ["R. Percurso da decisão"]), ("A", ["E. Recorrer ao", "integrante técnico"])], ["|>"], 200, 1240,
            note=["E suspende R quando faltam execuções (1.2) ou quando a dúvida persiste (2.3.3); com a resposta, R é retomado do ponto em que parou."])
y = s.panel(y, "R — percurso da decisão",                                                        # 2
            ("A", ["R. Percurso da decisão"]),
            [("A", ["1. Reunir os", "resultados do ciclo"]), ("A", ["2. Comparar o", "desempenho (T04)"]),
             ("A", ["3. Formar a", "recomendação"]), ("A", ["4. Apresentar e", "sustentar"])],
            ["[]>>", "[]>>", "[]>>"])
y = s.panel(y, "1 — Reunir os resultados do ciclo",                                              # 3
            ("A", ["1. Reunir os resultados do ciclo"]),
            [("I", ["C. Consultar as", "execuções do ciclo"]),
             ("S", ["S1. Exibir modelos com", "execução concluída", "e conjunto de imagens"]),
             ("U", ["1.1. Conferir se os", "modelos candidatos têm", "execução no mesmo conjunto"])],
            ["[]>>", "[]>>"], note=["Se faltar execução, Larissa recorre a E (1.2) e R fica suspenso até a resposta."])
y = s.panel(y, "2 — Comparar o desempenho consolidado (T04)",                                    # 4
            ("A", ["2. Comparar o desempenho consolidado"]),
            [("I", ["2.1. Abrir a", "comparação do ciclo"]),
             ("S", ["S2. Exibir métricas", "agregadas por modelo", "e a referência"]),
             ("A", ["2.2. Ler o", "desempenho"]), ("A", ["2.3. Avaliar a", "relevância"])],
            ["[]>>", "[]>>", "[]>>"])
y0 = y
ya = s.panel(y0, "2.2 e 2.3 — ler e avaliar",                                                    # 5
             ("A", ["2.2. Ler o desempenho"]),
             [("I", ["2.2.1. Ler as", "métricas na tabela"]), ("I", ["2.2.2. Ler as", "métricas no gráfico"])],
             ["[]"], 40, 680)
yb = s.panel(y0 + 54, None,
             ("A", ["2.3. Avaliar a relevância"]),
             [("U", ["2.3.1. Julgar a", "diferença pela", "referência"]), ("A", ["2.3.2. Consultar a", "explicação e julgar"])],
             ["[]"], 760, 1400)
s.divider(720, y0 + 54, max(ya, yb) - 10)
y = max(ya, yb)
y = s.panel(y, "2.3.2 — consultar a explicação e julgar",                                        # 6
            ("A", ["2.3.2. Consultar a explicação e julgar"]),
            [("I", ["2.3.2.1. Consultar a explicação", "do termo ou do aviso"]),
             ("U", ["2.3.2.2. Julgar a diferença", "com a explicação"])], ["[]>>"], 200, 1240,
            note=["Se a dúvida persistir depois de 2.3.2.2, Larissa recorre a E (2.3.3)."])
y = s.panel(y, "3 — Formar a recomendação",                                                      # 7
            ("A", ["3. Formar a recomendação"]),
            [("U", ["3.1. Recomendar o", "modelo de melhor", "desempenho"]),
             ("U", ["3.2. Recomendar com", "ressalva de incerteza"]), ("U", ["3.3. Adiar e pedir", "novas execuções"])],
            ["[]", "[]"], 120, 1320)
y = s.panel(y, "4 — Apresentar e sustentar a recomendação",                                      # 8
            ("A", ["4. Apresentar e sustentar a recomendação"]),
            [("A", ["4.1. Preparar o material", "para a reunião"]),
             ("U", ["4.2. Apresentar a", "recomendação e", "seus limites"]),
             ("U", ["4.3. Registrar a", "decisão da coordenação"])], ["[]>>", "[]>>"], 120, 1320,
            note=["Com 3.3, 4.2 comunica o adiamento e o que falta executar; 4.3 registra o novo prazo."])
y = s.panel(y, "4.1 — preparar o material",                                                      # 9
            ("A", ["4.1. Preparar o material para a reunião"]),
            [("A", ["4.1.1. Exportar o resumo", "da comparação [H]"]), ("U", ["4.1.2. Anotar modelo,", "métricas e ressalvas"])],
            ["[]"], 200, 1240)
y = s.panel(y, "4.1.1 — exportar o resumo da comparação [H]",                                    # 10
            ("A", ["4.1.1. Exportar o resumo da comparação"]),
            [("I", ["Q. Solicitar o resumo", "da comparação"]),
             ("S", ["S3. Gerar o resumo com", "modelos, métricas,", "referência e limites"]),
             ("U", ["K. Conferir se o resumo", "traz o modelo e", "as ressalvas"])], ["[]>>", "[]>>"], 120, 1320)
y = s.panel(y, "E — recorrer ao integrante técnico (fora da interface)",                         # 11
            ("A", ["E. Recorrer ao integrante técnico"]),
            [("U", ["1.2. Solicitar execuções", "faltantes"]), ("U", ["2.3.3. Pedir interpretação", "da diferença"])],
            ["[]"], 200, 1240,
            note=["Contato por mensagem com o integrante que executa os modelos (P01). A interface não executa nem responde por ele."])
H = s.ctt_legend(y, ["[]>>  ativação com passagem de informação", "[]  escolha", "|>  suspensão / retomada"],
                 ["Letras (M, U, R, E, C, S, Q, K) marcam nós só do CTT;", "os números seguem o HTA."])

s.save(str(OUT), H)
s.save_crops(str(OUT), H, [
    ("visao_geral", 0, 3, "CTT T05 — visão geral: motivação, sessão e percurso"),
    ("detalhe_01", 3, 5, "CTT T05 — detalhamento 1: ramos 1 e 2"),
    ("detalhe_02", 5, 7, "CTT T05 — detalhamento 2: 2.2, 2.3 e 2.3.2"),
    ("detalhe_03", 7, 10, "CTT T05 — detalhamento 3: ramos 3, 4 e 4.1"),
    ("detalhe_04", 10, None, "CTT T05 — detalhamento 4: 4.1.1, E e legenda"),
])
print(OUT.name, H)
