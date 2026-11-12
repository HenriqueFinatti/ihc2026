---
name: projeto-ihc-equipe17
description: Base de trabalho do projeto de IHC da Equipe 17 (FEI 2026/2, segmentação semântica off-road para a Baja FEI). Use em qualquer pedido sobre as entregas, IDs, pendências ou rastreabilidade do repositório ihc2026.
---

# Projeto de IHC da Equipe 17

Esta skill prepara a IA para trabalhar no repositório da disciplina de Interação Humano-Computador da Equipe 17 (FEI, 2026/2). O projeto aplica os métodos de IHC ao TCC *Segmentação Semântica em Vias Off-Road*, cuja interface atende a equipe Baja FEI.

Para aplicar um parecer do professor, use também a skill `aplicar-feedback-professor`. Esta skill vale para a tudo.

## 1. Antes de qualquer resposta

Leia os arquivos da raiz. Eles definem o que cada entrega pede e como contribuir, e prevalecem sobre esta skill quando houver conflito:

| Arquivo | Para que serve |
|---|---|
| `README.md` | Identificação, relação TCC × IHC, tabela de entregas com status |
| `GUIA_DE_USO.md` | Estrutura padrão de cada entrega, autoria, imagens, [F]/[H]/[?], erros comuns, estados |
| `GUIA_ESCOPO_IHC.md` | Como o escopo de IHC deriva do TCC; catálogo de padrões de interface |
| `CONTRIBUTING.md` | Estilo de commit, autoria dentro do artefato, registro de mudanças de escopo |
| `CHECKLIST_FINAL.md` | Critérios de qualidade de todo o projeto |
| `BIBLIOGRAFIA.md` | Fontes da disciplina (Barbosa e Silva, 2010, e outras) |
| `RASTREABILIDADE.md` | Matriz que liga TCC → hipóteses → personas → tarefas → telas; registro de mudanças (§5) |
| `PENDENCIAS.md` | Inconsistências `INC-xx` e decisões da equipe (D1–D8); o painel é a fonte de verdade do status |

Leia também:

- o arquivo da entrega pedida (`docs/NN_*.md`), inteiro, incluindo o checklist do fim;
- as entregas anteriores das quais ela depende (por exemplo, a E9 parte das personas da E3, das tarefas da E5 e das metas da E8);
- o parecer em `feedbacks/` da entrega, se existir;
- `.claude/skills/projeto-ihc-equipe17/CONTEXTO.md`, se existir (estado atual das decisões por entrega).

Antes de editar, confira se o arquivo tem alterações não commitadas ou se mudou desde a última leitura. Se mudou, parta da versão atual e preserve as edições da pessoa.

## 2. Regra de trabalho: uma parte por vez

A IA nunca faz mais do que uma parte de uma vez. Ela faz uma parte, pede para a pessoa validar e só segue quando a pessoa instruir.

- **O que é uma parte:** cada seção `##` do arquivo da entrega, na ordem do template. Quando uma seção `##` tiver subseções independentes (uma por integrante, por instrumento ou por persona), cada subseção é uma parte.
- **Exemplo com a Entrega 8:**
  1. A IA escreve `## Delimitação do sistema interativo` e pede validação.
  2. Depois da validação e da instrução para seguir, escreve `## 1. Características da plataforma` e pede validação de novo.
  3. Segue assim até o `## Checklist`.
- **Antes da primeira parte:** explique em poucas linhas como vai fazer a entrega (fontes que vai usar, ordem das partes, dúvidas que dependem da pessoa) e espere a resposta.
- **Ao terminar cada parte**, a mensagem de validação traz:
  - o que foi escrito e de onde veio cada informação;
  - os itens marcados `[H]` ou `[?]` que a pessoa precisa confirmar com a equipe;
  - os arquivos de acompanhamento que foram atualizados (seção 6);
  - a pergunta de validação, e nada além disso. A próxima parte não começa na mesma resposta.
- **Correções e pendências:** apresente a lista com comentário e sugestão para cada item e aplique só o que a pessoa decidir. Se ela autorizar vários itens de uma vez, aplique esses itens e relate um por um.
- **Ajustes pedidos na validação:** aplique na mesma parte e peça validação de novo antes de seguir.

## 3. Princípios do projeto

- **TCC ideal.** Os documentos descrevem o TCC previsto, não o estado atual da implementação. Não cite terminal, edição manual de arquivos, scripts, tempos medidos nem recursos que ainda não existem no código. Limitações momentâneas do TCC não viram pendência nem texto nas entregas.
- **TCC previsto:**
  - segmentação semântica **binária**, *Trilha* × *Fora da trilha*;
  - comparação entre **FCN** e **DeepLabV3+**, ambos com ResNet152;
  - métricas calculadas só no conjunto de teste anotado: IoU/mIoU, acurácia, recall, F1, matriz de confusão e tempo de inferência;
  - a interface faz parte do escopo formal do TCC, prevista e ainda não aplicada.
- **Configuração** = modelo + parâmetros de treino expostos ao usuário (épocas, early stopping e paciência, datasets de treino, batch size, gráficos). Definir a configuração e treinar pela interface estão **dentro** do recorte. Novas arquiteturas e parâmetros internos ficam fora.
- **Cadeia de derivação** (`GUIA_DE_USO.md`): contribuição do TCC → usuário plausível → objetivo → tarefa → contexto → necessidade de interação → interface. Uma entrega não reinicia o projeto: personas, tarefas e telas continuam coerentes com as entregas anteriores, salvo quando uma evidência justificar a mudança (e a mudança é registrada).
- **Proto-personas e dados hipotéticos.** O projeto é de aprendizagem. Quando faltar informação, a IA pode propor hipóteses plausíveis, sempre marcadas `[H]`, para a pessoa validar com a equipe. Nunca apresente como fato observado um dado que ninguém coletou.
- **Evidência antes de padrão.** Dashboard, histórico, filtros, CRUD ou relatório só entram com tarefa e evidência que os justifiquem (`RASTREABILIDADE.md` §4). Histórico (F05) depende da H08 e ficou fora do recorte até a coleta da E7.

## 4. IDs do projeto

Use sempre o ID estável junto do nome na primeira menção da seção (ex.: "P01 (Rafael)", "T08, definir uma configuração e treinar"). Não crie um ID que já existe com outro sentido; antes de criar, procure o maior número em uso.

| Família | Significado | Onde é definido |
|---|---|---|
| `H01`–`H12` | Hipóteses da Entrega 1 | E1 §10 e `RASTREABILIDADE.md` §2 (estado de cada hipótese) |
| `A01`–`A04` | Atividades da E1 §3.2 | E1 §3.2 |
| `AC01`–`AC06` | Ações da E1 §9.2 | E1 §9.2 (renomeadas de A0x para não colidir) |
| `RC01`–`RC04` | Recomendações da análise de concorrência | E2 e `RASTREABILIDADE.md` §6 |
| `E1`–`E6` dentro da RAST §7 | **Evidências visuais** da E2 (capturas em `assets/02_concorrencia/`), não entregas | `RASTREABILIDADE.md` §7 |
| `P01`–`P03` | Personas: P01 Rafael (analista de segmentação, prioritária), P02 Andreia (pesquisadora/coordenadora que configura e treina), P03 Larissa (gestão que compara e decide) | E3 |
| `C01`–`C03` | Cenários de problema: C01 → P01, C02 → P03, C03 → P02 | E4 |
| `T01`–`T08` | Tarefas do usuário | E3 (contexto de uso) e E5 |
| `RQ01`–`RQ09`, `UT01`–`UT03` | Requisitos e tarefas de teste de usabilidade propostos | Síntese da E5; `instrumentos/` |
| `PF01`–`PF03` | Fluxos do protótipo em papel | E6 |
| `R01`–`R04` | Linhas da matriz capacidade → necessidade → artefatos | `RASTREABILIDADE.md` §3 |
| `F01`–`F07` | Padrões de interface (sustentados, pendentes ou descartados) | `RASTREABILIDADE.md` §4 |
| `A01`–`A03` dentro da E7 | Planejamento por persona da Parte A (não confundir com as atividades da E1) | E7, Parte A |
| `I01`–`I03` | Instrumentos de coleta | E7, Parte B |
| `G1…`, `S1…`, `A1…`, `T1…`, `PQ1…` | Códigos de participantes anonimizados | E7, procedimento de cada instrumento |
| `INC-01`… | Pendências e inconsistências | `PENDENCIAS.md` (painel + detalhamento) |
| `D1`–`D8` | Decisões da equipe que destravaram pendências | `PENDENCIAS.md` e `RASTREABILIDADE.md` §5 |

O significado exato de cada ID está no arquivo indicado. Leia a definição antes de usar um ID, porque nomes e descrições podem ter sido revisados.

Entregas são citadas como E1 a E14 (ex.: "E5, seção 3"). Na RAST §7, `E1`–`E6` são evidências; deixe claro qual é qual quando os dois aparecerem juntos.

## 5. Convenções de escrita

- **Marcação de conhecimento:** `[F]` fato com origem indicada, `[H]` hipótese, `[?]` lacuna. Um `[F]` sem origem é erro.
- **Autoria:** toda seção individual tem `**Autor(a):** Nome completo — matrícula`. Preserve as linhas de autoria existentes.
- **Status no topo da entrega e no README:**
  - `⬜ não iniciada`, `🟨 em andamento`, `🟩 concluída`;
  - `🟦 revisada após feedback` só quando a revisão aplicou um parecer do professor em `feedbacks/`;
  - revisões internas mantêm 🟩 e entram na seção **Histórico de revisões** da entrega.
- **Sem seção de Referências** nas entregas (decisão da equipe, INC-03). Cite a fonte no próprio texto quando necessário.
- **Falas de participantes** (simulações, entrevistas) são mantidas como foram ditas.
- **Links externos** (Figma, Forms, vídeos) precisam de cópia ou evidência local no repositório (`GUIA_DE_USO.md`).
- **Imagens e diagramas:** em `assets/NN_*/`, com legenda que diga o que a imagem comprova. Diagramas gerados por script (E5, `scripts/diagramas/`) são alterados no script e regenerados, nunca no SVG.
- **Quebras de linha:** preserve a do arquivo (os `.md` das entregas usam CRLF; `PENDENCIAS.md` usa LF).
- **Linguagem:** português, frases diretas, termos técnicos explicados na primeira ocorrência. O usuário do projeto é a equipe Baja, não "qualquer pessoa".

## 6. Manter o acompanhamento atualizado

Toda parte concluída revisa estes arquivos e lista na mensagem de validação o que mudou neles:

- **`PENDENCIAS.md`**
  - Inconsistência nova encontrada: abra o próximo `INC-xx` no painel (severidade, entrega, pendência, status ⬜) e no detalhamento (problema e sugestão).
  - Pendência corrigida: mude o status no painel e preencha "Resolução" com a data e o que foi feito.
  - Nunca apague itens. Itens descartados recebem ➖ e a justificativa.
- **`RASTREABILIDADE.md`**
  - Mudança de hipótese, persona, escopo, tarefa ou recomendação: registre na §5 com data, motivo e evidência, sem apagar a versão anterior.
  - Novos artefatos ligados a uma linha R0x ou F0x: preencha a coluna correspondente nas §3 e §4.
  - O estado de uma hipótese (§2) só muda com evidência de coleta.
- **`README.md`**
  - Atualize o status da entrega na tabela "Entregas" sempre que mudar no topo do arquivo.
  - Atualize a tabela "Relação entre TCC e projeto de IHC" se o usuário principal ou o recorte mudar.
- **Entrega anterior afetada:** não altere sem pedido. Abra uma pendência e avise a pessoa.
- **`.claude/skills/projeto-ihc-equipe17/CONTEXTO.md`, se existir:** atualize o estado da entrega e as decisões novas.

## 7. O que a IA não faz

- Não faz commit, push nem pull request.
- Não apaga arquivos nem trechos sem pedido da pessoa. Itens de `PENDENCIAS.md` nunca são apagados.
- Não sobrescreve edições da pessoa nem altera a autoria de uma seção.
- Não muda o escopo do TCC; mudanças no escopo de IHC são registradas na RAST §5.
- Não avança para a próxima parte sem a instrução da pessoa.

## 8. Formato da resposta

- **Ao planejar:** como vai fazer, de onde vêm as informações e quais perguntas precisam de resposta.
- **Ao entregar uma parte:** o resumo da seção 2, curto, com os `[H]` a validar e os arquivos de acompanhamento atualizados.
- **Ao encerrar a entrega:** o que foi feito, o que ficou como `[H]` ou `[?]`, as pendências abertas e o que a pessoa deve conferir antes de marcar o checklist.
