# Geradores dos diagramas das Entregas 5 e 9

Os SVGs de HTA e CTT em `assets/05_tarefas/` e os mapas de objetivos em `assets/09_modelo_conceitual/` são **gerados** por estes scripts. Para alterar um diagrama, edite o script da tarefa e gere de novo; não edite o SVG à mão (a alteração se perde na próxima geração).

| Arquivo | Gera | Autor do modelo |
|---|---|---|
| `ihc_svg.py` | Biblioteca comum (desenho de HTA, CTT e mapa de objetivos, legenda, recortes) | — |
| `hta_t03.py` | `hta_t03_comparar_configuracoes.svg` | Tiago Fagundes dos Santos |
| `ctt_t03.py` | `ctt_t03_comparar_configuracoes.svg` + visão geral e detalhamentos | Tiago Fagundes dos Santos |
| `hta_t05.py` | `hta_t05_decidir_modelo.svg` | Henrique Finatti Silveira Belo Trebbi |
| `ctt_t05.py` | `ctt_t05_decidir_modelo.svg` + visão geral e detalhamentos | Henrique Finatti Silveira Belo Trebbi |
| `mapa_objetivos_ci02.py` | `mapa_objetivos_ci02.svg` (Entrega 9, mapa da P03) | Henrique Finatti Silveira Belo Trebbi |
| `verificar.js` | Confere texto fora das caixas, sobreposição e texto passando da borda | — |

O GOMS não tem gerador: ele é textual e fica direto em `docs/05_analise_tarefas.md`.

## Como gerar

Requer só Python 3 (biblioteca padrão). Rode a partir desta pasta:

```bash
cd scripts/diagramas
python3 hta_t03.py
python3 ctt_t03.py
python3 hta_t05.py
python3 ctt_t05.py
python3 mapa_objetivos_ci02.py
```

## Como verificar (opcional)

Requer Node.js e Playwright com Chromium:

```bash
npm install playwright
npx playwright install chromium
node verificar.js ../../assets/05_tarefas/*.svg ../../assets/09_modelo_conceitual/*.svg
# para salvar PNGs de conferência: node verificar.js ../../assets/05_tarefas/*.svg --png /tmp
```

A saída `OK` para cada arquivo indica que nenhum texto sai da caixa, se sobrepõe a outro ou passa da borda.

## Como alterar um diagrama

**HTA** — cada nó é `N(linhas, plano, op)`:

```python
N(["2.3. Avaliar se a", "diferença é relevante"], "2.3.1 / 2.3.2 / 2.3.3")   # objetivo decomposto
N(["2.3.1. Julgar a", "diferença pela", "referência"], op=True)              # operação (folha)
```

`s.tree(pai, [filhos], y, x0, x1)` desenha um pai e seus filhos na faixa horizontal `[x0, x1]`. Para pôr duas expansões lado a lado, chame `tree` duas vezes com o mesmo `y` e faixas diferentes.

**CTT** — cada painel é um pai e seus filhos, com os operadores entre irmãs:

```python
s.panel(y, "Título do painel", ("A", ["2.3. Avaliar a relevância"]),
        [("U", ["2.3.1. Julgar"]), ("A", ["2.3.2. Consultar"])], ["[]"])
```

Tipos: `A` abstrata, `U` usuário, `I` interação, `S` sistema. Ao incluir ou remover um painel com título, revise os índices da lista `save_crops` no fim do script, que definem a visão geral e os detalhamentos.

**Mapa de objetivos** — usa a mesma função `tree` do HTA, sem plano. Objetivos alcançados fora do sistema usam `dashed=True`:

```python
N(["1.4. Pedir execução ou", "conferência ao", "integrante técnico"], dashed=True)
```

**Mantenha a correspondência:** depois de alterar um diagrama, atualize a tabela HTA, o GOMS e a tabela de correspondência da mesma seção em `docs/05_analise_tarefas.md`.
