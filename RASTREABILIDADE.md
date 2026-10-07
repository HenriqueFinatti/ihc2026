# Matriz de rastreabilidade de IHC

A matriz deve ser atualizada ao longo do semestre. Ela ajuda a demonstrar que a interface não surgiu arbitrariamente e registra **como o conhecimento da equipe evoluiu**.

Para projetos cujo TCC não previa interface, esta matriz é especialmente importante: deve ficar visível a passagem da **contribuição técnica do TCC** para um **cenário de uso plausível**, e desse cenário para as decisões de interação.

## 1. Derivação do escopo de IHC a partir do TCC

| Elemento | Registro da equipe | Evidência/justificativa | Estado |
|---|---|---|---|
| Tema do TCC | Segmentação Semântica em vias off-road | Documento do TCC | definido |
| Resultado técnico esperado | Sistema de segmentação semântica com comparação de modelos | Documento do TCC | definido |
| O TCC previa interface? | Sim | Documento do TCC | definido |
| Capacidade/contribuição central | Segmentar vias off-road e comparar desempenho entre modelos | Documento do TCC | definido |
| Possíveis beneficiários/stakeholders | Equipe Baja FEI (analistas, desenvolvedores, gestores) | Fonte: observação da equipe | F |
| Usuário escolhido para IHC | Analista de segmentação da equipe Baja FEI | Perfil que avalia qualidade da segmentação e seleciona modelos | H |
| Objetivo principal do usuário | Avaliar qualidade da segmentação, identificar falhas e selecionar modelo adequado | Derivado da contribuição técnica | H |
| Contexto de uso adotado | Laboratórios FEI e pistas off-road durante testes do veículo Baja | Observação da equipe | F |
| Interface/recorte de IHC | Upload de dados, processamento, visualização lado a lado, métricas e comparação entre modelos | Derivado das necessidades do usuário | H |
| Relação com o TCC | Parte prevista — interface faz parte do escopo formal do TCC | Documento do TCC | definido |

> Se o escopo de IHC mudar ao longo do semestre, preserve a decisão anterior no histórico e registre **qual evidência motivou a mudança**.

## 2. Registro de hipóteses e lacunas da Entrega 1

Use esta tabela para itens importantes marcados como `[H]` ou `[?]`. Preserve o histórico: não apague uma hipótese refutada.

| ID | Afirmação / dúvida inicial | Tipo | Por que importa | Como/onde investigar | Evidência obtida | Estado atual | Impacto no projeto |
|---|---|---|---|---|---|---|---|
| H01 | O que se espera que esteja diferente para pessoas, organizações ou processos se essa contribuição for bem-sucedida? | H | Define o benefício concreto que a interface deve proporcionar | Entrega 4; expectativa já registrada em 01, seção 9.1 | **Nenhuma que sustente.** A Entrega 2 mostra que funcionalidades parecidas existem em concorrentes, mas isso não comprova benefício para o Baja. | **aberta** (rebaixada de "sustentada" em 28/09/2026) | Direciona o projeto para uma interface que elimine a necessidade de código e facilite a comparação de modelos. A expectativa está registrada em 01, seção 9.1; a investigação é da Entrega 4. |
| H02 | O perfil prioritário (analista de segmentação) possui conhecimento básico do domínio mas pode não dominar programação | H | Direciona o nível de complexidade da interface | Entrega 3 | PENDENTE | aberta | A interface deve ser acessível para usuários sem conhecimento técnico avançado. |
| H03 | O piloto Baja FEI seria beneficiado indiretamente, sem interagir diretamente com a interface | H | Esclarece stakeholders e impactos indiretos | Entrega 3 | PENDENTE | aberta | Define que pilotos não são usuários diretos da interface. |
| H04 | Conhecimento técnico, experiência com ferramentas e familiaridade com métricas influenciam a interação | H | Define requisitos de design para acessibilidade e usabilidade | Entrega 3; Entrega 7 | PENDENTE. A Entrega 2 gerou duas recomendações derivadas desta hipótese (RC01 tradução de termos, RC03 tabela), mas nenhuma as confirma. | aberta | A interface deve utilizar visualizações, tabelas e linguagem acessível. |
| H05 | As atividades são realizadas atualmente por meio de scripts que exigem conhecimento técnico | H | Base do problema de interação que a interface deve resolver | Entrega 2; Entrega 7 | **Observação própria da equipe** (Entrega 1, seção 4.6): os scripts do projeto exigem configuração de arquivos, parâmetros e comandos. Limitação: primeira mão, sem verificação com usuários externos. | sustentada | A interface deve eliminar a necessidade de executar scripts. |
| H06 | Dificuldades principais: configurar parâmetros, selecionar arquivos, interpretar resultados sem orientação | H | Identifica pontos críticos de interação | Entrega 4 | PENDENTE. A Entrega 2 mostrou que ferramentas profissionais têm terminologia densa, o que é indício, não comprovação. | aberta | A interface deve simplificar essas atividades. |
| H07 | Existem fatores sociais ou organizacionais como papéis, permissões e colaboração na equipe | H | Pode afetar design e governança da interface | Entrega 7 | PENDENTE. A Entrega 2 mostra que os concorrentes oferecem perfis e permissões, mas isso descreve os produtos, não a nossa equipe. | aberta | Pode influenciar necessidade de perfis ou permissões. |
| H08 | Existe necessidade de histórico para comparar análises e acompanhar evolução | H | Define se interface precisa de funcionalidades de busca e armazenamento | Entrega 7 (investigação) e Entrega 8 | **Origem observada, necessidade não demonstrada.** A Roboflow oferece versionamento de datasets (fonte: G2, Entrega 2). Isso mostra que o padrão existe, não que o Baja precisa dele. | **aberta — investigação antecipada para a Entrega 7** | **RC02 foi rebaixada a pendência** porque conflita com o escopo (não produzimos nem versionamos modelos) e porque falta definir *o que* seria recuperado. |
| H09 | Interfaces conhecidas pelo público: VS Code, terminais, GitHub, ferramentas de telemetria | H | Estabelece padrões e expectativas do usuário | Entrega 7 | **Entrega 2:** nenhum dos três produtos analisados (CVAT, Roboflow, Supervisely) é comprovadamente conhecido pelo Baja. São análogos de referência, não software do usuário. | aberta | A interface não pode assumir familiaridade com nenhuma das ferramentas analisadas. |
| H10 | Ferramentas genéricas como CVAT e Roboflow podem ser complexas para o perfil priorizado | H | Justifica a necessidade de uma interface simplificada | Entrega 7 | **Entrega 2 (fontes públicas):** a Supervisely é apontada como de curva íngreme e excesso de funcionalidades; o CVAT exige Docker e tem sistema de atalhos complexo; a Roboflow é apontada como acessível a não especialistas. | **refinada** — a complexidade **não é uniforme**, depende do produto | Interface restrita a um fluxo principal. Usar a Supervisely como referência de "excesso", e a Roboflow como referência de "acessível". |
| H11 | Padrões familiares: seleção de arquivo, botão de processamento, barra de progresso, comparação lado a lado | H | Direciona elementos de interface a serem incluídos | Entrega 7 | **Entrega 2:** seleção de modelo por lista, barra de progresso e tabela de métricas foram **observados** nos produtos, mas isso descreve os produtos, não o que o Baja já conhece. | aberta | Interface deve oferecer esses padrões, mas a familiaridade com eles continua não comprovada. |
| H12 | Benefício esperado: eliminar necessidade de código, apresentar resultados claramente, permitir comparação entre modelos | H | Define métricas de sucesso do projeto | Investigação contínua | PENDENTE. Registrado como expectativa em 01, seção 9.1 — não como benefício comprovado. | aberta | Define critérios de avaliação do projeto. |

## 3. Rastreabilidade entre contribuição técnica, necessidades e artefatos

> **Estado atual: PENDENTE por projeto.** As colunas de persona, cenário, tarefa, modelo e avaliação serão preenchidas nas entregas correspondentes. Não é necessário produzir esses artefatos na Entrega 2. O que já é possível registrar hoje é a passagem da capacidade técnica até a necessidade de interação — feita na seção 1 e nas seções 6 e 7.

| ID | Capacidade do TCC utilizada | Necessidade/problema | Persona | Cenário problema | Objetivo/tarefa | HTA/GOMS/CTT | Cenário de interação / signos | MoLIC | Tela(s) Figma | Heurística / problema | Tarefa no teste | Decisão/melhoria |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | Segmentar vias off-road (DeepLabv3+ + ResNet152) | H06, H05 — dificuldade de interpretar o resultado sem apoio visual | PENDENTE (E3) | PENDENTE (E4) | T01 — avaliar a qualidade da segmentação | PENDENTE (E5) | PENDENTE (E9) | PENDENTE (E10) | PENDENTE (E11) | PENDENTE (E13) | PENDENTE (E14) | PENDENTE |
| R02 | Executar a segmentação sem depender de script | H05 — processo atual exige execução de scripts | PENDENTE (E3) | PENDENTE (E4) | T02 — enviar imagem e iniciar a execução | PENDENTE (E5) | PENDENTE (E9) | PENDENTE (E10) | PENDENTE (E11) | PENDENTE (E13) | PENDENTE (E14) | PENDENTE |
| R03 | Comparar desempenho entre modelos | H01, H12 — selecionar o modelo adequado | PENDENTE (E3) | PENDENTE (E4) | T03 — comparar métricas entre modelos | PENDENTE (E5) | PENDENTE (E9) | PENDENTE (E10) | PENDENTE (E11) | PENDENTE (E13) | PENDENTE (E14) | PENDENTE |

## 4. Rastreabilidade de padrões de interface

Use esta tabela quando o projeto incorporar padrões como dashboard, relatório, histórico, filtros ou administração. O objetivo é **justificar o padrão**, não apenas listar telas.

> **Estado atual:** apenas os padrões que a Entrega 2 observou e decidiu recomendar estão registrados. Os padrões ainda não sustentados por evidência permanecem como pergunta, e não como decisão.

| ID da tela/fluxo | Padrão de interface | Objetivo/tarefa que justifica | Informação/ação principal | Evidência de necessidade | Artefatos relacionados |
|---|---|---|---|---|---|
| F01 | Seleção de modelo em **lista explícita** | T01/T03 — escolher qual modelo executar | Lista de modelos com descrição curta | **E1** (lista no CVAT); **E4** (conversacional no Roboflow, preferido evitar) | E9, E10, E11 |
| F02 | **Tabela** de métricas, como alternativa ao gráfico | T01/T03 — consultar e comparar valores exatos | Métricas por classe, em tabela e em gráfico | **E6** (~8 s) — a Supervisely já oferece tabelas | E9, E10, E11 |
| F03 | **Indicador de estado** da execução | T02 — saber se está processando, concluído ou falhou | Barra de progresso e estado textual | **E5** (~12–18 s) e **E1** | E9, E10, E11 |
| F04 | Explicação contextual de termos | T01 — compreender o que a segmentação e as métricas indicam | Texto de apoio no ponto de uso | **RC01** — sustentação média; a dificuldade do usuário **ainda não foi demonstrada** | E9, E10, E11 |
| F05 | Histórico com filtros | *A definir* | *A definir* | **NÃO sustentado.** RC02 foi rebaixada a pendência; depende de **H08** | PENDENTE — a investigar na E7 |
| F06 | Administração / CRUD | *Não se aplica* | — | **Descartado** na Entrega 1 (seção 8): o sistema é local e de uso restrito à equipe | — |
| F07 | Usuários / perfis / permissões | *Não se aplica* | — | **Descartado** na Entrega 1 (seção 8): sem necessidade de guardar informação individual | — |

## 5. Registro de mudanças de escopo

| Data | O que mudou | Evidência/feedback que motivou | Artefatos afetados | Responsável |
|---|---|---|---|---|
| 26/09/2026 | Revisão da Entrega 1 conforme feedback do professor: definição do perfil prioritário (analista de segmentação), objetivo humano além de "segmentar", consolidação do recorte, correção de IDs e marcações, preenchimento da delimitação | Feedback do professor sobre a Entrega 1 | 01_conhecendo_o_problema.md, RASTREABILIDADE.md | Equipe |
| 28/09/2026 | **Histórico com busca/filtros e comparação de resultados passaram de "não" para "talvez/sim"** na tabela de possibilidades da Entrega 1. Na Entrega 1, a equipe havia descartado histórico ("não há necessidade de busca") e comparação de resultados ("a comparação irá acontecer, mas por parte do usuário"). | A Entrega 2 mostrou que os três produtos analisados oferecem filtros, tabelas e versionamento — e que a comparação entre modelos é a atividade central do nosso objetivo, não algo opcional. | 01_conhecendo_o_problema.md seção 8; 02_analise_concorrencia.md seções 3.1 e 5 | Equipe |
| 28/09/2026 | **Limite do recorte explicitado:** "versionamento/histórico de **modelos**" saiu do escopo, porque o recorte é **executar** modelos já disponíveis — não treinamos modelos nem produzimos versões. | Feedback do professor: RC02 reunia necessidades distintas e não deveria assumir treinamento. | 02_analise_concorrencia.md RC02; 01_conhecendo_o_problema.md seção 11 | Equipe |
| 28/09/2026 | **Perfil do usuário padronizado** como "analista de segmentação da equipe Baja FEI". A rastreabilidade usava "Estudante FEI", definido apenas por interesse em participar do projeto Baja. | Feedback do professor: interesse no projeto não equivale a executar a atividade de análise de segmentação. Registro de **imprecisão de redação**, e não de mudança de escolha de perfil. | 01_conhecendo_o_problema.md seções 2.4 e 7.2; RASTREABILIDADE.md seção 1 | Equipe |
| 28/09/2026 | **Três hipóteses rebaixadas ou refinadas** após a Entrega 2: H01 (sustentada → aberta), H10 (aberta → refinada), H08 (investigação antecipada). H05 permaneceu sustentada, mas com evidência e limitação explicitadas. | Feedback do professor: "um estado não é uma evidência"; encontrar funcionalidade em concorrente não confirma benefício nem processo atual do Baja. | RASTREABILIDADE.md seção 2 | Equipe |

## 6. Recomendações da Entrega 2 e sua origem

Cada recomendação só entra no projeto se responder a: *qual tarefa do nosso usuário ela melhora?*

| ID | Recomendação | Evidência de origem | Objetivo do usuário | Grau de sustentação | Hipótese ligada | Estado |
|---|---|---|---|---|---|---|
| RC01 | Traduzir termos técnicos com apoio contextual no ponto de uso | E1 (rótulos e correspondência no CVAT); E6 (métricas por classe na Supervisely) | Compreender o que a segmentação mostra e o que as métricas indicam — e não indicam | **Média** — a observação é verificável, mas a dificuldade do nosso usuário não foi demonstrada | H04, H12 | Proposta, sujeita a investigação na Entrega 7 |
| RC02 | Histórico e recuperação de análises anteriores | Versionamento de datasets na Roboflow (fonte: G2) | *Indefinido* — falta saber o que seria recuperado | **Não confirmada** | H08 | **Pendente.** Rebaixada: conflita com o escopo e depende de H08 |
| RC03 | Oferecer métrica em tabela **e** em gráfico | **E6 (~8 s)** — a Supervisely **já oferece** tabelas; também relatos sobre o Roboflow | Consultar e comparar valores exatos, que o gráfico não permite ler | **Alta** — evidência visual direta | H04, H12 | Recomendada |
| RC04 | Estados de processamento com indicação visual de progresso | **E5 (~12–18 s)** — barras de época/lote na Supervisely; E1 (indicador no CVAT) | Saber se a execução está em curso, terminou ou falhou | **Alta** — evidência visual direta | H06, H11 | Recomendada, com textos adaptados à execução (não "treinando") |

> **Sobre RC03:** a versão anterior a criticava a Supervisely por "depender de gráficos". A própria evidência (E6) mostra tabelas no produto. A recomendação foi corrigida e agora deriva de uma **solução positiva observada**, o que a torna mais defensável.

## 7. Registro de evidências visuais da Entrega 2

| ID | Arquivo | O que comprova | O que **não** comprova |
|---|---|---|---|
| E1 | `assets/02_concorrencia/cvat_selecao_modelo.png` | Lista explícita de modelos, correspondência de rótulos, indicação de progresso | Eficiência de atalhos; modo escuro |
| E2 | `assets/02_concorrencia/cvat_metricas.png` | Indicadores de produtividade de anotação e eventos | Acurácia ou comparação de desempenho de modelos |
| E3 | `assets/02_concorrencia/roboflow_input_imagens.png` | Entrada de imagens/webcam em "Test Your Model" | O fluxo completo e o resultado do processamento (recorte parcial, 341 × 192 px) |
| E4 | `assets/02_concorrencia/roboflow_selecionar_modelos.png` | Sugestão de modelos em formato conversacional, com justificativas | Que a troca foi executada; desempenho obtido; dificuldade de desfazer |
| E5 | `assets/02_concorrencia/treinamento.webm` (~12–18 s) | Barras de progresso de época/lote; gráficos de treino e validação | Recuperação por checkpoint; histórico de execuções |
| E6 | `assets/02_concorrencia/analise-metricas.mp4` (~8 s) | Tabelas, filtros, estatísticas de dataset e visualizações por classe | Que o produto dependa de gráficos — as tabelas existem |

> **Pendência material:** E5 e E6 são gravações de vídeo. A entrega pede capturas estáticas; a equipe deve extrair os frames citados e salvá-los em `assets/02_concorrencia/` com legenda e referência ao vídeo de origem.

## Como usar

- Use identificadores estáveis (`H01`, `P01`, `C01`, `T01`, `M01`, `F01`, `UT01`).
- Quando uma necessidade/problema tiver origem em hipótese da Entrega 1, cite o ID correspondente.
- Em TCC sem interface original, pelo menos uma linha deve mostrar claramente **como uma capacidade técnica chega até uma tarefa de usuário e uma tela/fluxo**.
- Uma linha pode se desdobrar quando um objetivo possui múltiplos caminhos.
- Não force relação inexistente: se algo ainda não foi modelado, marque `PENDENTE`.
- Ao remover uma funcionalidade, registre a decisão em vez de apagar silenciosamente o histórico.
- Dashboard, CRUD, filtros e relatórios só devem aparecer quando houver objetivo/tarefa que os justifique.
