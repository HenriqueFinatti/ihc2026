"""CTT da T07 — Comparar o resultado de diferentes modelos (P02, Mateus).
Leitura da árvore: docs/05_analise_tarefas.md, seção 3.3."""
from pathlib import Path
from ihc_svg import Svg

OUT = Path(__file__).resolve().parents[2] / "assets/05_tarefas/ctt_t07_comparar_modelos.svg"

s = Svg("CTT — T07: Comparar o resultado de diferentes modelos",
        "CTT da tarefa T07 por Mateus Marana Assuena. Painéis de decomposição com tipos de tarefa (abstrata, "
        "usuário, interação, sistema) e relações temporais. Motivação externa M antes da sessão U; obtenção "
        "do resultado repetida por configuração. Modelo hipotético a validar.")
y = s.header("CTT — T07: Comparar o resultado de diferentes modelos",
             "Mateus Marana Assuena · 22.123.026-1 · P02, Andreia Silva · C03 · Uso proposto [H]")

y = s.panel(y, "Motivação externa antes da sessão de uso [H]",
            ("A", ["T07. Motivação e sessão de uso"]),
            [("U", ["M. Decidir comparar configurações", "para um experimento"]),
             ("A", ["U. Sessão de comparação"])], ["[]>>"], 200, 1240,
            note=["M acontece fora da interface: Andreia quer saber se uma nova configuração melhora a trilha em sombra (C03, Q28).",
                  "M []>> U: o objetivo do experimento passa para a sessão; U é detalhada nos painéis seguintes."])
y = s.panel(y, "U — sessão de comparação",
            ("A", ["U. Sessão de comparação"]),
            [("A", ["1. Preparar a", "comparação"]), ("A", ["2. Obter o resultado", "de cada configuração*"]),
             ("A", ["3. Comparar", "visualmente (T06)"]), ("A", ["4. Comparar", "as métricas"]),
             ("A", ["5. Concluir a", "comparação"])],
            ["[]>>", "[]>>", "[]>>", "[]>>"],
            note=["2* repete-se para cada configuração escolhida em 1.2 que ainda não foi executada sobre a entrada."])
y = s.panel(y, "1 — Preparar a comparação",
            ("A", ["1. Preparar a comparação"]),
            [("I", ["1.1. Selecionar", "a entrada"]),
             ("S", ["S1. Exibir as", "configurações", "disponíveis"]),
             ("I", ["1.2. Escolher as", "configurações"])], ["[]>>", "[]>>"])
y = s.panel(y, "2* — Obter o resultado de cada configuração (T02)",
            ("A", ["2. Obter o resultado de uma configuração"]),
            [("I", ["2.1. Iniciar a", "segmentação"]),
             ("S", ["S2. Executar e", "informar o estado"]),
             ("I", ["2.2. Acompanhar o", "processamento"]),
             ("A", ["2.3. Conferir o", "desfecho"])], ["[]>>", "[]>>", "[]>>"])
y = s.panel(y, "2.3 — Conferir o desfecho da execução",
            ("A", ["2.3. Conferir o desfecho da execução"]),
            [("U", ["2.3.1. Reconhecer o", "resultado pronto"]),
             ("I", ["2.3.2. Repetir ou retirar", "a configuração"])], ["[]"], 200, 1240,
            note=["Com resultado pronto, a configuração entra na comparação. Com falha, S2 informa a causa; repetir inicia nova ocorrência de 2,",
                  "retirar exclui a configuração. Se restar menos de duas configurações com resultado, Andreia volta a 1.2."])
y = s.panel(y, "3 — Comparar os resultados visualmente (T06)",
            ("A", ["3. Comparar os resultados visualmente"]),
            [("S", ["S3. Exibir original,", "máscaras e", "sobreposição"]),
             ("I", ["3.1. Visualizar o", "resultado de cada", "configuração"]),
             ("I", ["3.2. Comparar na", "mesma região"])], ["[]>>", "[]>>"],
            note=["3.1 é detalhada no GOMS da T06 (meta 2: imagem original, máscara ou sobreposição)."])
y = s.panel(y, "4 — Comparar as métricas no conjunto de teste",
            ("A", ["4. Comparar as métricas"]),
            [("S", ["S4. Exibir métricas e", "diferença entre", "configurações"]),
             ("U", ["4.1. Ler a diferença", "entre as", "configurações"]),
             ("I", ["[4.2]. Consultar a", "matriz de confusão"])], ["[]>>", "[]>>"],
            note=["4.2 é opcional: só quando Andreia precisa entender onde cada configuração erra."])
y = s.panel(y, "5 — Concluir a comparação",
            ("A", ["5. Concluir a comparação"]),
            [("U", ["5.1. Julgar se a", "diferença é relevante"]),
             ("I", ["5.2. Registrar a", "conclusão"])], ["[]>>"], 200, 1240,
            note=["5.1 pode concluir que a nova configuração é melhor, igual, pior ou que a comparação é inconclusiva.",
                  "O sistema mostra a diferença, mas não julga se ela é relevante (RQ08)."])
H = s.ctt_legend(y, ["[]>>  ativação com passagem de informação", "[]  escolha", "T*  iteração", "[T]  opcional"],
                 ["Letras (M, U, S) marcam nós só do CTT;", "os números seguem o HTA."])

s.save(str(OUT), H)
print(OUT.name, H)
