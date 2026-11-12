# Contexto atual do projeto

**Última atualização:** 12/11/2026

Este arquivo resume o estado do projeto para a IA e para a equipe. Ele **aponta** para onde cada decisão está registrada e não substitui as entregas. Se houver diferença entre este arquivo e uma entrega, a entrega e o `RASTREABILIDADE.md` valem, e este arquivo deve ser corrigido.

Atualize este arquivo quando o status de uma entrega mudar, quando a equipe tomar uma decisão nova ou quando uma pendência abrir ou fechar.

## Equipe e autoria

| Integrante | Matrícula | Persona | Cenário | Tarefas na E5 | E7 (Parte A / instrumento) |
|---|---|---|---|---|---|
| Henrique Finatti Silveira Belo Trebbi | 22.123.030-3 | P03 | C02 | T04, T05 | A01 / I01 |
| Tiago Fagundes dos Santos | 22.123.017-0 | P01 | C01 | T01, T02, T03 | A02 / I02 |
| Mateus Marana Assuena | 22.123.026-1 | P02 | C03 | T06, T07 | A03 / I03 |

## Decisões vigentes

| Decisão | Resumo | Onde está registrada |
|---|---|---|
| TCC ideal | As entregas descrevem o TCC previsto, não o estado atual do código | `PENDENCIAS.md` ("Como usar") |
| D1 — classes | Segmentação binária: *Trilha* × *Fora da trilha* | `PENDENCIAS.md`; RAST §5 |
| D2 — configuração | Configuração = modelo + parâmetros de treino expostos ao usuário (épocas, early stopping e paciência, datasets de treino, batch size, gráficos). Configurar e treinar estão dentro do recorte; novas arquiteturas e parâmetros internos ficam fora | `PENDENCIAS.md`; E1 §2.2 e §7.1; RAST R04 |
| D3 — P02 | Andreia é pesquisadora/coordenadora que configura, treina e compara os modelos | `PENDENCIAS.md`; E3 |
| D4 — H01 | H01 reescrita como afirmação: decisão com números dispersos e sem critério explícito | E1 §10; RAST §2 |
| D5 — métricas | Métricas só no conjunto de teste anotado | `PENDENCIAS.md`; RAST §5 |
| D6 — histórico | Histórico (F05) fora do recorte até a coleta da E7 confirmar a H08 | E1 §8; RAST §4 |
| D7 — RC03 | Rebaixada para sustentação "média" | RAST §6 |
| D8 — tarefas | T03 e T07 separadas; IDs do C03 alinhados à E5; T02 renomeada | RAST §5 |
| Status | 🟦 só quando um parecer do professor foi aplicado; revisões internas mantêm 🟩 e entram no "Histórico de revisões" | `PENDENCIAS.md` (INC-01) |
| Referências | As entregas não têm seção de Referências | `PENDENCIAS.md` (INC-03) |

## Personas e tarefas

- **P01 — Rafael:** analista de segmentação; persona prioritária (E3).
- **P02 — Andreia:** pesquisadora/coordenadora que configura e treina (E3).
- **P03 — Larissa:** gestão; acessa a interface para comparar e decidir (E3).
- **Tarefas:**

| ID | Tarefa |
|---|---|
| T01 | Avaliar a qualidade da segmentação de uma imagem |
| T02 | Executar a segmentação com uma ou mais configurações disponíveis |
| T03 | Comparar o resultado de uma imagem entre configurações |
| T04 | Comparar o desempenho consolidado entre modelos |
| T05 | Decidir e justificar a escolha |
| T06 | Analisar visualmente os resultados |
| T07 | Comparar modelos |
| T08 | Definir uma configuração de treino e treinar o modelo (C03; ainda sem HTA/GOMS/CTT) |

## Estado das entregas

| Entrega | Status | O que a próxima entrega precisa saber |
|---|---|---|
| E1 | 🟦 | Hipóteses H01–H12 (§10); recorte da interface (§11) |
| E2 | 🟦 | Recomendações RC01–RC04; evidências E1–E6 na RAST §7 |
| E3 | 🟦 | Personas P01–P03, contexto de uso e jornada |
| E4 | 🟦 | Cenários C01–C03; T08 criada no C03 |
| E5 | 🟩 | HTA/GOMS/CTT de T01–T07; requisitos RQ01–RQ09; tarefas de teste UT01–UT03; diagramas gerados por `scripts/diagramas/` |
| E6 | 🟩 | Fluxos PF01–PF03 do protótipo em papel |
| E7 | 🟨 | Planejamento completo. Falta validar com a equipe os `[H]` (papéis e quantidade de pessoas) e revisar as partes de cada autor. Questionário I02: https://forms.gle/pAMyXCdebYo9aHmq9. Os estados das hipóteses só mudam depois da coleta |
| E8 | ⬜ | Em elaboração |
| E9–E14 | ⬜ | — |

## Pendências abertas

| ID | Entrega | Resumo |
|---|---|---|
| INC-53 | E5 | Figura da seção 3.1 não corresponde à tabela do HTA da T07 |
| INC-54 | E5 | HTA da T07: planos divergentes, falta Feedback na tarefa 0 e o passo de comparar |
| INC-55 | E5 | GOMS T06 trata métodos como combináveis; CTT T07 sem motivação externa |
| INC-59 | E6 → E11 | Rascunhos em papel usam classes ilustrativas; corrigir no protótipo da E11, sem redesenhar a E6 |
| INC-61 | E5 ou E9 | Falta modelar a T08 (HTA/GOMS/CTT); o modelo de sequência da I03 deve servir de base |

O status de cada pendência é o do painel de `PENDENCIAS.md`.
