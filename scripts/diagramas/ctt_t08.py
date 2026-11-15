"""CTT da T08 — Definir uma configuração de treino e treinar o modelo (P02, Mateus).
Leitura da árvore: docs/05_analise_tarefas.md, seção 3.6.3."""
from pathlib import Path
from ihc_svg import Svg

OUT = Path(__file__).resolve().parents[2] / "assets/05_tarefas/ctt_t08_treinar_configuracao.svg"

s = Svg("CTT — T08: Definir uma configuração de treino e treinar o modelo",
        "CTT da tarefa T08 por Mateus Marana Assuena. Painéis de decomposição com tipos de tarefa (abstrata, "
        "usuário, interação, sistema) e relações temporais. Motivação externa M antes da sessão U; treino "
        "acompanhado em janelas curtas; falha tratada com nova tentativa. Modelo hipotético a validar.")
y = s.header("CTT — T08: Definir uma configuração de treino e treinar o modelo",
             "Mateus Marana Assuena · 22.123.026-1 · P02, Andreia Silva · C03 / CI03 · Uso proposto [H]")

y = s.panel(y, "Motivação externa antes da sessão de uso [H]",
            ("A", ["T08. Motivação e sessão de uso"]),
            [("U", ["M. Decidir testar uma", "nova configuração"]),
             ("A", ["U. Sessão de treino"])], ["[]>>"], 200, 1240,
            note=["M acontece fora da interface: depois de um teste com dificuldade nas sombras, Andreia decide o que testar (C03, Q18 e Q28).",
                  "M []>> U: o que testar (modelo, épocas, datasets) passa para a sessão."])
y = s.panel(y, "U — sessão de treino",
            ("A", ["U. Sessão de treino"]),
            [("A", ["1. Definir a", "configuração"]), ("A", ["2. Treinar o", "modelo*"]),
             ("A", ["3. Conferir a", "configuração treinada"])], ["[]>>", "[]>>"],
            note=["2* repete-se quando o treino falha e Andreia reinicia com a configuração ajustada (2.3.2)."])
y = s.panel(y, "1 — Definir a configuração",
            ("A", ["1. Definir a configuração"]),
            [("S", ["S1. Exibir modelos,", "parâmetros e", "valores padrão"]),
             ("I", ["1.1. Escolher", "o modelo"]),
             ("A", ["1.2. Definir os", "parâmetros"]),
             ("S", ["S2. Validar e", "sugerir o nome"]),
             ("I", ["1.3. Nomear a", "configuração"])], ["[]>>", "[]>>", "[]>>", "[]>>"],
            note=["S2 não aceita valores fora do permitido (por exemplo, nenhum dataset de treino) e sugere um nome único (Entrega 9, seção 4)."])
y = s.panel(y, "1.2 — Definir os parâmetros de treino",
            ("A", ["1.2. Definir os parâmetros"]),
            [("I", ["1.2.1. Manter os", "valores padrão"]),
             ("I", ["1.2.2. Alterar os", "parâmetros do", "experimento"])], ["[]"], 200, 1240)
y = s.panel(y, "2* — Treinar o modelo",
            ("A", ["2. Treinar o modelo"]),
            [("I", ["2.1. Iniciar", "o treino"]),
             ("S", ["S3. Treinar e", "informar o estado"]),
             ("I", ["2.2. Acompanhar", "o treino"]),
             ("A", ["2.3. Conferir", "o desfecho"])], ["[]>>", "|[]|", "[]>>"],
            note=["S3 e 2.2 são concorrentes com comunicação: o treino segue enquanto Andreia sai e volta para consultar época e gráficos."])
y = s.panel(y, "2.3 — Conferir o desfecho do treino",
            ("A", ["2.3. Conferir o desfecho"]),
            [("U", ["2.3.1. Reconhecer o", "treino concluído"]),
             ("A", ["2.3.2. Tratar a", "falha do treino"])], ["[]"], 200, 1240)
y = s.panel(y, "2.3.2 — Tratar a falha do treino",
            ("A", ["2.3.2. Tratar a falha"]),
            [("U", ["2.3.2.1. Ler a", "causa da falha"]),
             ("I", ["2.3.2.2. Ajustar a", "configuração e", "reiniciar"])], ["[]>>"], 200, 1240,
            note=["2.3.2.2 encerra esta iteração de 2 e inicia a próxima com a configuração ajustada."])
y = s.panel(y, "3 — Conferir a configuração treinada",
            ("A", ["3. Conferir a configuração treinada"]),
            [("S", ["S4. Exibir gráficos e", "métricas no", "conjunto de teste"]),
             ("U", ["3.1. Ler os gráficos", "de treino e", "validação"]),
             ("U", ["3.2. Ler as", "métricas"])], ["[]>>", "[]>>"])
H = s.ctt_legend(y, ["[]>>  ativação com passagem de informação", "[]  escolha",
                     "|[]|  concorrência com comunicação", "T*  iteração"],
                 ["Letras (M, U, S) marcam nós só do CTT;", "os números seguem o HTA."])

s.save(str(OUT), H)
print(OUT.name, H)
