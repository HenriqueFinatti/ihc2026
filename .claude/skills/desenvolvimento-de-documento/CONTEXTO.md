# Contexto atual do projeto

**Última atualização:** 15/11/2026

Este arquivo resume o estado do projeto para a IA e para a equipe. Ele **aponta** para onde cada decisão está registrada e não substitui as entregas. Se houver diferença entre este arquivo e uma entrega, a entrega e o `RASTREABILIDADE.md` valem, e este arquivo deve ser corrigido.

Atualize este arquivo quando o status de uma entrega mudar, quando a equipe tomar uma decisão nova ou quando uma pendência abrir ou fechar.

## Equipe e autoria

| Integrante | Matrícula | Persona | Cenário (E4) | Tarefas na E5 | E7 (Parte A / instrumento) | Cenário de interação (E9) | MoLIC (E10) |
|---|---|---|---|---|---|---|---|
| Henrique Finatti Silveira Belo Trebbi | 22.123.030-3 | P03 | C02 | T04, T05 | A01 / I01 | CI02 | M02 |
| Tiago Fagundes dos Santos | 22.123.017-0 | P01 | C01 | T01, T02, T03 | A02 / I02 | CI01 | M01 |
| Mateus Marana Assuena | 22.123.026-1 | P02 | C03 | T06, T07, T08 | A03 / I03 | CI03 | M03 |

## Decisões vigentes

| Decisão | Resumo | Onde está registrada |
|---|---|---|
| TCC ideal | As entregas descrevem o TCC previsto, não o estado atual do código | `PENDENCIAS.md` ("Como usar") |
| D1 — classes | Segmentação binária: *Trilha* × *Fora da trilha* | `PENDENCIAS.md`; RAST §5 |
| D2 — configuração | Configuração = modelo + parâmetros de treino expostos ao usuário (épocas, early stopping e paciência, datasets de treino, batch size, gráficos). Configurar e treinar estão dentro do recorte; novas arquiteturas e parâmetros internos ficam fora. Datasets de treino: Freiburg Forest, Synthetic Offroad e CaSSeD (CaSSeD incluído em 14/11/2026). Valores padrão do TCC: 200 épocas, paciência 5, batch size 4, early stopping e gráficos ligados | `PENDENCIAS.md` (INC-65); E1 §0.4 e §7.1; E5 premissa 5; E9 §4; RAST §5 e R04 |
| D3 — P02 | Andreia é pesquisadora/coordenadora que configura, treina e compara os modelos | `PENDENCIAS.md`; E3 |
| D4 — H01 | H01 reescrita como afirmação: decisão com números dispersos e sem critério explícito | E1 §10; RAST §2 |
| D5 — métricas | Métricas só no conjunto de teste. Na interface (a partir da E9), o termo é "conjunto de teste"; as entregas anteriores usam "conjunto de teste anotado" | `PENDENCIAS.md`; RAST §5; E9 §4 |
| D6 — histórico | Histórico (F05) fora do recorte até a coleta da E7 confirmar a H08 | E1 §8; RAST §4 |
| D7 — RC03 | Rebaixada para sustentação "média" | RAST §6 |
| D8 — tarefas | T03 e T07 separadas na E5; IDs do C03 alinhados à E5; T02 renomeada. Na E9, T03 e T07 correspondem a um único objetivo (O05) | RAST §5; E9 §3.2 |
| Exportação | Fora do recorte até a coleta da E7 (H12); decisões da E3 marcadas como condicionadas | `PENDENCIAS.md` (INC-63); E3; RAST §5 |
| Confiança do modelo | Retirada: o TCC previsto não a exibe; imagens sem anotação de referência são avaliadas visualmente | `PENDENCIAS.md` (INC-66); E5 §2; E9 §4; RAST §5 |
| Relevância da diferença | O sistema calcula e mostra a "diferença entre configurações" e explica as métricas, mas não julga se a diferença é relevante; não há aviso automático de "resultado inconclusivo" | `PENDENCIAS.md` (INC-67); E3 (decisão 5 da P03); E5 §1 e RQ07; E9 §4; RAST §5 |
| Nome da configuração | Modelo + número de épocas (ex.: DeepLabV3+ – 50 épocas), sugerido pelo sistema, editável e único `[H]` | E9 §4 |
| Status | 🟦 só quando um parecer do professor foi aplicado; revisões internas mantêm o status e entram no "Histórico de revisões" | `PENDENCIAS.md` (INC-01) |
| Referências | As entregas não têm seção de Referências | `PENDENCIAS.md` (INC-03) |
| Diagramas | HTA, CTT e mapas de objetivos são gerados por scripts em `scripts/diagramas/`: alterar o script e regenerar, não o SVG | `scripts/diagramas/README.md` |

## Personas e tarefas

- **P01 — Rafael:** analista de segmentação; persona prioritária (E3).
- **P02 — Andreia:** pesquisadora/coordenadora que configura e treina (E3).
- **P03 — Larissa:** gestão; acessa a interface para comparar e decidir (E3).
- **Tarefas:**

| ID | Tarefa | Modelos na E5 |
|---|---|---|
| T01 | Avaliar a qualidade da segmentação de uma imagem | GOMS (§2.2) |
| T02 | Executar a segmentação com uma ou mais configurações disponíveis | Objetivo 2 do HTA/CTT da T03 e da T07 |
| T03 | Comparar o resultado de uma imagem entre configurações | HTA e CTT (§2) |
| T04 | Comparar o desempenho consolidado entre modelos | GOMS (§1.2) |
| T05 | Decidir e justificar a escolha | HTA e CTT (§1) |
| T06 | Analisar visualmente os resultados | GOMS (§3.2) |
| T07 | Comparar modelos | HTA e CTT (§3.1 e §3.3) |
| T08 | Definir uma configuração de treino e treinar o modelo | HTA, GOMS e CTT (§3.6) |

## IDs criados nas Entregas 8 e 9

| Família | Significado | Onde |
|---|---|---|
| MQ01–MQ07 | Metas qualitativas de usabilidade | E8 §3.1 |
| MU01–MU11 | Metas quantitativas de usabilidade | E8 §3.2 |
| CI01–CI03 | Cenários de interação (CI01 → P01, CI02 → P03, CI03 → P02) | E9 §1 |
| O01–O10 | Objetivos do mapa consolidado (subtópicos O01.1…), agrupados em A (preparar configurações), B (executar e avaliar), C (comparar) e D (concluir e decidir) | E9 §3.2 |
| M01–M03 | Diagramas MoLIC previstos (M01 Tiago/CI01, M02 Henrique/CI02, M03 Mateus/CI03) | E9, Síntese; E10 |

Nos mapas individuais da E9, a numeração por letras (A1, A1.1…) é provisória; os IDs definitivos são O01–O10.

## Estado das entregas

| Entrega | Status | O que a próxima entrega precisa saber |
|---|---|---|
| E1 | 🟦 | Hipóteses H01–H12 (§10); recorte da interface (§11) |
| E2 | 🟦 | Recomendações RC01–RC04; evidências E1–E6 na RAST §7 |
| E3 | 🟦 | Personas P01–P03, contexto de uso e jornada; exportação condicionada à E7 |
| E4 | 🟦 | Cenários C01–C03; T08 criada no C03 |
| E5 | 🟦 | HTA/GOMS/CTT de T01–T08; requisitos RQ01–RQ09; tarefas de teste UT01–UT03. Parecer aplicado em 15/11/2026: passos condicionais com colchetes (`[2.3.3]` na T05, `[3.3.2]` na T03, `[4.2]` na T07), julgamentos que podem terminar como inconclusivos, desfecho da execução (sucesso ou falha) na T03 e na T07 e conclusão guardada só na sessão (histórico depende da H08) |
| E6 | 🟦 | Fluxos PF01–PF03 do protótipo em papel. Parecer aplicado em 15/11/2026: fotos mantidas como versão simulada e revisão por anotações (`assets/06_prototipos/anotacoes/`, gerador `scripts/prototipos/anotacoes.py`), com estados P01-E, P01-P, P02-S, P03-I, P03-C e P03-F; seleção múltipla com execução em fila; P03 dividida em comparação na mesma imagem (T03/T07) e no conjunto de teste (T04); conclusão registrada pela pessoa. O gerador `wireframes.py` não foi incorporado |
| E7 | 🟦 | Planejamento da coleta (I01 entrevista, I02 questionário em https://forms.gle/pAMyXCdebYo9aHmq9, I03 investigação contextual). Os estados das hipóteses só mudam depois da coleta. Parecer aplicado em 15/11/2026: grupos separados (I02: A segmentação, O outros dados, T acompanha os testes; I01: G e D por triagem na 1.2), só o público principal muda hipóteses, critérios de H02/H05/H07/H08 revistos, I03 sem gravação de tela. Formulário on-line a atualizar (INC-69); e-mails de contato já nos termos |
| E8 | 🟩 | Características da plataforma (§1), princípios (§2), metas MQ01–MQ07 e MU01–MU11 (§3) |
| E9 | 🟩 | Cenários de interação CI01–CI03 encadeados (CI03 cria a configuração candidata → CI01 valida em campo → CI02 compara as candidatas); conversas U:/D: (§2); mapa consolidado O01–O10 (§3.2); esquema de signos (§4); a Síntese lista, para cada MoLIC, os objetivos, as rupturas (com PP/PA/AL/RA/CE) e os signos obrigatórios |
| E10 | 🟩 | M01 (Tiago), M02 (Henrique) e M03 (Mateus) com leitura e checklist; cenas reusadas entre diagramas; consolidação (O05.1 × O03.1, O06.2 vale para a P02 [H], O08 único com tipo de conclusão); “Preparação para o Figma” lista 9 telas com estados de feedback e erro |
| E11–E14 | ⬜ | — |

## Pendências abertas

| ID | Entrega | Resumo |
|---|---|---|
| INC-59 | E6 → E11 | Rascunhos em papel usam classes ilustrativas e IoU para qualquer arquivo; em andamento: anotações da E6 já mostram a correção; redesenhar no protótipo da E11 (legenda binária, métricas só no conjunto de teste, estado "sem métricas"), sem redesenhar a E6 |

Resolvidas em 14/11/2026: INC-53, 54, 55 e 61 (diagramas do Mateus e T08), INC-63 (exportação), 64 (E5 §3), 65 (CaSSeD), 66 (confiança do modelo) e 67 (aviso de inconclusivo).

O status de cada pendência é o do painel de `PENDENCIAS.md`.
