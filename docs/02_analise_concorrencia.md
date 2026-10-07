# Entrega 2 — Público-alvo e análise de concorrência

**Data:** 16/09/2026 (primeira versão) · 28/09/2026 (revisão após feedback)
**Status:** 🟦 revisada após feedback
**Responsabilidade mínima:** cada integrante analisa pelo menos 1 concorrente/interface representativa; a equipe produz síntese comparativa.

## Objetivo da atividade

Compreender soluções do mesmo domínio **e também interfaces familiares ao público-alvo**. O objetivo não é copiar telas, mas identificar convenções, padrões, affordances percebidas, problemas recorrentes, expectativas e oportunidades de design.

> **Concorrente não precisa ser idêntico ao produto.** Pode atuar na mesma área, resolver objetivo semelhante ou disputar a mesma necessidade. Quando não houver concorrente direto, use produtos análogos e softwares que o público já utiliza.

## Histórico de revisões

**Revisão de 28/09/2026 — a partir do feedback do professor sobre a Entrega 02:**

| Correção solicitada | O que foi feito |
|---|---|
| As análises individuais não foram disponibilizadas | Os três arquivos foram reescritos e agora estão completos: [`entrega_2/02_Tiago.md`](entrega_2/02_Tiago.md) (CVAT), [`entrega_2/02_Henrique.md`](entrega_2/02_Henrique.md) (Roboflow) e [`entrega_2/02_Mateus.md`](entrega_2/02_Mateus.md) (Supervisely). Cada um contém autoria, classificação, contexto, funcionalidades com evidência, opiniões de UX com fonte, modelo de negócio e lições. |
| Evidências visuais não foram vinculadas aos argumentos | A seção 3 agora descreve **cada** arquivo de `assets/02_concorrencia/`, indicando o que comprova, o que **não** comprova e a origem. Cada análise individual traz legenda de figura. |
| RC01–RC04 sem origem observável, objetivo e adaptação | A seção 5 foi reescrita com a cadeia **observação → dificuldade/oportunidade → objetivo do usuário → recomendação**. RC02 foi rebaixada a pendente; RC03 foi corrigida pela própria evidência; RC04 teve a origem corrigida. |
| Afirmações não comprovadas na síntese ("poucos atalhos", "contraste ruim", "difícil desfazer") | Removidas ou reescritas com fonte verificável na seção 4. |
| Público-alvo repetia a lista de produtos | A seção 1 agora descreve o público e a sua relação com o nosso usuário. |
| Mudanças de escopo e hipóteses não registradas | Registradas em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md), seção 5, e vinculadas às hipóteses na seção 6. |
| Faltavam datas de acesso e módulo analisado | Cada análise individual agora registra módulo/versão, data de acesso e módulo exato. |

## Entrada obrigatória da Entrega 1

| Item citado na Entrega 1 | Onde foi analisado | Decisão |
|---|---|---|
| CVAT | [`entrega_2/02_Tiago.md`](entrega_2/02_Tiago.md) | Mantido como **análogo** — referência de padrões (seleção de modelo, indicadores de progresso) |
| Roboflow | [`entrega_2/02_Henrique.md`](entrega_2/02_Henrique.md) | Mantido como **análogo** — o mais próximo do nosso perfil de usuário |
| Supervisely | [`entrega_2/02_Mateus.md`](entrega_2/02_Mateus.md) | Mantido como **análogo** — contraponto de densidade funcional |

## 1. Público-alvo desta análise

O público-alvo do **nosso projeto** é o *analista de segmentação da equipe Baja FEI* — um integrante que conhece o domínio off-road e o projeto Baja, mas que pode não dominar programação (ver [`01_conhecendo_o_problema.md`](01_conhecendo_o_problema.md), seção 7.2).

**Este ponto foi corrigido nesta revisão.** A versão anterior escrevia "Estudante FEI" na rastreabilidade e descrevia o perfil por "interesse em participar do projeto Baja". Houve uma **imprecisão de redação, e não uma mudança de escolha**: o perfil sempre foi um integrante da equipe Baja que executa a análise de segmentação. Interessar-se pelo projeto não equivale a executar a atividade de análise.

> **Registro de imprecisão:** a Entrega 1 e a matriz de rastreabilidade usavam formulações diferentes para o mesmo perfil. Optamos por "analista de segmentação da equipe Baja FEI" em ambos os arquivos. Ver [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md), seção 5.

Os três produtos analisados têm **públicos próprios, diferentes do nosso**:

| Produto | Público real do produto | Semelhança com o nosso perfil |
|---|---|---|
| C01 — CVAT | Engenheiros de ML, pesquisadores e equipes de anotação; documentação concentrada em usuários técnicos | **Baixa.** Exige auto-hospedagem/Docker e tem curva de aprendizado íngreme. Serve como referência de *padrões*, não de familiaridade. |
| C02 — Roboflow | Desenvolvedores de IA, equipes de visão computacional e pequenas empresas sem MLOps dedicado | **Média.** É apontado publicamente como acessível a não especialistas, o que o torna o análogo mais próximo do nosso perfil. |
| C03 — Supervisely | Empresas e pesquisadores que desenvolvem modelos de segmentação próprios | **Baixa.** Curva de aprendizado íngreme e grande densidade funcional. |

> `[?]` **Lacuna:** não temos evidência de que o nosso público conheça ou utilize qualquer um dos três produtos. Eles são **análogos de referência**, não software conhecido pelo usuário. A familiaridade permanece como **hipótese H09** e deve ser investigada na Entrega 7.

## 2. Concorrentes diretos/indiretos

**Nenhum dos três produtos é concorrente direto do nosso recorte.** Todos atuam antes ou ao redor da etapa que nos interessa.

| ID | Produto | Módulo analisado | Atua em | Relação com o nosso recorte |
|---|---|---|---|---|
| **C01** | CVAT | CVAT Online e documentação da Community (v2.74.0) | **Anotação** de imagens, vídeo e 3D | Indireta. Produz o ground truth; não executa nem interpreta a segmentação do nosso usuário. |
| **C02** | Roboflow | "Test Your Model" (upload de imagem/webcam) e seleção de modelo por assistente conversacional | Ciclo completo: dataset → treinamento → implantação | Indireta. O módulo de teste de modelo é o ponto mais próximo da nossa atividade de entrada de dados, mas diluído em um fluxo maior. |
| **C03** | Supervisely | Configuração de treinamento e aba de análise do projeto | Ciclo completo de visão computacional | Indireta. A etapa "segmentar e interpretar" não é o centro do produto. |

**Achado de IHC:** a atividade central do nosso usuário — *executar a segmentação e compreender o resultado para decidir qual modelo usar* — **não é o centro de nenhuma dessas plataformas**. Elas concentram-se em anotar, treinar e implantar. Isso justifica o nosso recorte: tratar a interpretação do resultado como objetivo principal, e não como etapa intermediária.

## 3. Evidências visuais e o que cada uma comprova

Os arquivos estão em `assets/02_concorrencia/`. A coluna "o que **não** comprova" é tão importante quanto a anterior: evita que uma captura seja usada para sustentar uma afirmação que ela não sustenta.

| Evidência | Arquivo | O que permite observar | O que **não** comprova | Tipo | Origem |
|---|---|---|---|---|---|
| **E1** | [`cvat_selecao_modelo.png`](../assets/02_concorrencia/cvat_selecao_modelo.png) | Seleção de modelo para anotação automática, correspondência de rótulos, controles e indicação de progresso | Eficiência por atalhos; experiência em modo escuro | Print composto (marcado pela equipe) | Uso próprio da equipe, 27/08/2026 |
| **E2** | [`cvat_metricas.png`](../assets/02_concorrencia/cvat_metricas.png) | Quantidade de objetos e imagens, tempo de trabalho, velocidade de anotação, tabela de eventos e filtros | **Acurácia de modelo; comparação de desempenho entre modelos.** São métricas de produtividade de anotação — objeto diferente do nosso | Print | Uso próprio da equipe, 27/08/2026 |
| **E3** | [`roboflow_input_imagens.png`](../assets/02_concorrencia/roboflow_input_imagens.png) | Recorte de "Test Your Model", com opções de arquivo e webcam, no contexto "Off-Road Trail Segmentation" | O fluxo completo e os resultados do processamento — o recorte tem 341 × 192 px e mostra só parte da tela | Print (recorte parcial) | Uso próprio da equipe, 27/08/2026 |
| **E4** | [`roboflow_selecionar_modelos.png`](../assets/02_concorrencia/roboflow_selecionar_modelos.png) | Resposta conversacional com opções de modelos e justificativas resumidas para trilhas | Que a troca foi executada; que o treinamento terminou; o desempenho obtido; dificuldade de desfazer alterações | Print | Uso próprio da equipe, 27/08/2026 |
| **E5** | [`treinamento.webm`](../assets/02_concorrencia/treinamento.webm) | Configuração de treinamento no Supervisely, seleção de modelos, **barras de progresso de época e lote (~12–18 s)** e gráficos de treino/validação | Recuperação efetiva por checkpoint; histórico de execuções — não aparecem nos trechos inspecionados | **Vídeo** (frames citados por instante) | Uso próprio da equipe, 03/09/2026 |
| **E6** | [`analise-metricas.mp4`](../assets/02_concorrencia/analise-metricas.mp4) | Navegação na aba de análise do Supervisely: filtros, estatísticas de dataset, **tabelas (~8 s)** e visualizações por classe | Que o produto dependa de gráficos — **as tabelas existem e contrariam essa leitura** | **Vídeo** (frames citados por instante) | Uso próprio da equipe, 03/09/2026 |

> **Pendência material antes da entrega:** o professor observou que a entrega pede *capturas estáticas* e que os dois vídeos, embora válidos como material complementar, não a substituem. A equipe deve extrair e salvar em `assets/02_concorrencia/` os quadros citados acima (ex.: `supervisely_treinamento_progresso.png` a partir de `treinamento.webm` ~12–18 s; `supervisely_analise_tabela.png` a partir de `analise-metricas.mp4` ~8 s), com legenda e referência ao vídeo de origem. Enquanto isso não for feito, o item correspondente do checklist permanece aberto.

### 3.1 Padrões de interface observados, por produto

O padrão só é atribuído ao produto **onde foi verificado**. A versão anterior atribuía os mesmos cinco padrões a "CVAT, Roboflow e Supervisely" sem conferir o objeto de cada funcionalidade.

| Padrão | C01 CVAT | C02 Roboflow | C03 Supervisely | Tarefa que serve | Aplicável ao nosso escopo? |
|---|---|---|---|---|---|
| Seleção de modelo em lista explícita | **Sim** (E1) | Parcialmente — via assistente conversacional (E4) | **Sim** (E5) | Escolher qual modelo executar | **Sim** — e preferencialmente em lista, não por chat |
| Indicador de progresso da execução | **Sim** (E1) | Não observado (E4 mostra estado textual, não barra) | **Sim** (E5) | Saber que a segmentação está em curso | **Sim** |
| Tabela de métricas | Não observada (E2 é de produtividade) | Sim — relatado por usuário | **Sim** (E6, ~8 s) | Consultar e comparar valores | **Sim** |
| Gráfico de métricas | Não no recorte analisado | Sim — "evaluation graphs" | **Sim** (E6) | Comparar desempenho visualmente | **Sim**, como complemento |
| Filtros | **Sim** (E2) | Não observada | **Sim** (E6) | Restringir o conjunto de dados analisado | **Condicional** — depende de H08 |
| Histórico/versionamento | Não verificado | **Sim** — versionamento de datasets (fonte: G2) | **Não verificado** — checkpoints não aparecem nos trechos | Recuperar estado anterior | **Condicional** — ver RC02 |
| Administração / CRUD de projetos | Sim — fora do recorte analisado | Sim — fora do recorte analisado | Sim — fora do recorte analisado | Gerenciar projetos e datasets | **Não** — fora do nosso recorte |

> **Sobre "verificado" e "não observado":** a ausência de um elemento no recorte analisado **não prova** que ele não existe no produto. Escrevemos "não observado" ou "não verificado" para não repetir o erro de afirmar ausência a partir de uma captura parcial.

## 4. Síntese comparativa da equipe

Os quatro critérios originais foram mantidos, mas as afirmações que dependiam de impressões não comprovadas foram corrigidas.

| Critério | C01 — CVAT | C02 — Roboflow | C03 — Supervisely | Oportunidade para o projeto |
|---|---|---|---|---|
| **Navegação** | Densa; muitos módulos e tipos de anotação | Integrada em um fluxo único (dataset → implantação) | Densa e orientada a workspace/projeto | Interface simples, com **um fluxo principal** e navegação previsível. |
| **Feedback/estado** | Indicador de progresso na seleção de modelo (E1) e eventos no painel (E2) | O recorte analisado mostra estado **textual** em conversa (E4), não barra | Barras de progresso de época/lote e gráficos de treino (E5) | Unificar em um único indicador que distinga **processando**, **concluído** e **falhou**. |
| **Recuperação de erro** | *Não verificado nas evidências* | Relatam **versionamento de datasets** com retorno a anotações anteriores (fonte: G2) | *Checkpoints não aparecem nos trechos inspecionados* | Não assumir recuperação sem antes definir **o que** precisa ser recuperado (**RC02**). |
| **Terminologia** | Técnica (rótulos, correspondência, tarefas) | Mais acessível, com justificativas por uso | Técnica e orientada a especialista | Traduzir o essencial: **o que cada classe significa** e **o que as métricas indicam e não indicam**. |
| **Acessibilidade** | *Não verificado* — as capturas não permitem avaliar contraste, modo escuro ou atalhos | Relatos de lentidão e instabilidade com conjuntos grandes (fonte: G2) | Relatos de lentidão (fonte: G2) | Oferecer **tabela como alternativa ao gráfico** (E6 mostra que é possível) e garantir contraste em todas as representações. |
| **Eficiência** | **Correção:** a equipe havia atribuído "excelente suporte a atalhos". As fontes públicas descrevem o sistema de atalhos como **complexo**, demandando tempo para novos anotadores | Relatos de rotulagem assistida por IA reduzindo trabalho manual (fonte: G2) | Integração de etapas em um só ambiente (fonte: G2) | **Não prometer atalhos como diferencial.** Se incluídos, documentá-los. O ganho de eficiência vem de remover o script, não de adicionar atalhos. |

> **Delimitações desta síntese:** as colunas de Roboflow e Supervisely que citam "lentidão" e "versionamento" vêm de **avaliações públicas de terceiros**, não de teste do nosso público. Servem para gerar hipóteses, não para afirmar o comportamento do nosso usuário. Nenhuma afirmação sobre atalhos, contraste ou facilidade foi mantida sem fonte.

## 5. Recomendações derivadas

Cada recomendação segue a cadeia **observação → dificuldade/oportunidade → objetivo do usuário → recomendação**, e declara seu grau de sustentação.

### RC01 — Tradução dos termos técnicos com apoio contextual

| Elemento | Conteúdo |
|---|---|
| **Observação** | Os três produtos apresentam terminologia técnica. No CVAT, a seleção de modelo traz "correspondência de rótulos" (E1); a Supervisely organiza a análise por projeto e métricas (E6). |
| **Dificuldade/oportunidade** | O nosso usuário pode não saber o que significa uma classe (pista, vegetação, intransitável) nem o que uma métrica **indica — e o que não indica**. |
| **Objetivo do usuário** | Compreender o que a segmentação está mostrando e avaliar o desempenho sem depender de conhecimento prévio em IA. |
| **Recomendação** | Exibir explicação contextual dos termos no ponto em que aparecem, em vez de apenas "tooltip". **Proposta sujeita a investigação** — a Entrega 7 deve verificar quais termos realmente geram dúvida antes de adoptá-la. |
| **Sustentação** | **Média.** A observação é verificável, mas a dificuldade **específica do nosso usuário** ainda não foi demonstrada. |
| **Hipótese relacionada** | H04, H12 |

### RC02 — Histórico e recuperação de análises anteriores *(rebaixada a pendente)*

| Elemento | Conteúdo |
|---|---|
| **Observação** | O Roboflow oferece **versionamento de datasets**, permitindo reverter a um conjunto de anotações anterior (fonte: G2). A Supervisely **não** foi verificada quanto a checkpoints ou histórico nos trechos inspecionados. |
| **Correção de escopo** | A versão anterior desta recomendação propunha "versionamento ou histórico de **modelos**". Nosso recorte é **executar modelos já disponíveis** — não treinamos modelos nem produzimos versões. Portanto, **versionamento de modelos está fora do escopo**. |
| **Dúvida que permanece** | O que precisaria ser recuperado: uma **segmentação passada**, um **modelo**, ou o **resultado de uma execução**? Cada opção implica funcionalidades diferentes. |
| **Estado** | **Não é uma recomendação confirmada.** Fica como **pendência vinculada** à hipótese **H08**, a ser investigada na Entrega 7. Só vira recomendação se a equipe demonstrar a necessidade. |
| **Hipótese relacionada** | H08 |

### RC03 — Tabela como alternativa ao gráfico *(corrigida pela própria evidência)*

| Elemento | Conteúdo |
|---|---|
| **Correção** | A versão anterior derivava RC03 da crítica "dependência de gráficos" da Supervisely. Mas **E6 mostra que a Supervisely já oferece tabelas** (visíveis por volta de ~8 s). A crítica original era injusta com o produto. |
| **Observação corrigida** | Tabelas e filtros coexistem com gráficos na aba de análise da Supervisely (E6) e no Roboflow (relatos de usuário sobre tabelas e gráficos de avaliação). |
| **Oportunidade** | O padrão **já existe nos produtos analisados** — portanto é uma **solução positiva observada**, e não apenas uma correção de limitação. |
| **Objetivo do usuário** | Consultar e comparar valores exatos de métricas, especialmente quando o gráfico não permite ler um número. |
| **Recomendação** | Oferecer a métrica **em tabela e em gráfico**, deixando o usuário alternar. **Ressalva:** tabela não é garantia automática de acessibilidade — exige hierarquia visual, rótulos e contraste adequados. |
| **Sustentação** | **Alta** — apoiada em evidência visual direta (E6). |
| **Hipótese relacionada** | H04, H12 |

### RC04 — Estados de processamento com indicação visual de progresso

| Elemento | Conteúdo |
|---|---|
| **Correção de origem** | A versão anterior atribuía RC04 ao CVAT e ao Roboflow. O **apoio mais direto é da Supervisely** (E5, barras de época e lote entre ~12 e ~18 s); o CVAT tem indicador na seleção de modelo (E1). O recorte do Roboflow (E4) mostra **estado textual em conversa**, e **não** comprova a barra proposta. |
| **Observação** | Barras de progresso por etapa e gráficos de treino/validação na Supervisely (E5); indicador de progresso na seleção de modelo do CVAT (E1). |
| **Dificuldade/oportunidade** | O processamento de segmentação pode demorar. Sem feedback, o usuário não sabe se está executando, terminou ou falhou. |
| **Objetivo do usuário** | Saber em que estado está a execução e evitar repetir ou abandonar uma segmentação desnecessariamente. |
| **Adaptação ao recorte** | Os textos devem descrever a **nossa** atividade: enviar imagem → processando → resultado pronto → falha. **Não usar "treinando"**, porque o nosso usuário apenas **executa** a segmentação. |
| **Sustentação** | **Alta** — apoiada em evidência visual direta (E5, E1). |
| **Hipótese relacionada** | H06, H11 |

> **Nota sobre a identificação C01/C02/C03:** o professor recomendou explicitar esta identificação junto à síntese, incluindo módulo e versão. Feito na seção 2 e no cabeçalho de cada análise individual.

## 6. O que esta entrega acrescentou às hipóteses

| Hipótese | O que a análise de concorrência acrescentou | Novo estado |
|---|---|---|
| **H10** — ferramentas genéricas podem ser complexas para o nosso perfil | A Supervisely é o caso mais claro: fontes públicas apontam curva de aprendizado íngreme e excesso de funcionalidades. A Roboflow é o contraponto (apontada como acessível a não especialistas). A complexidade **não é uniforme** — depende do produto. | **Refinada:** o risco depende do produto; usar como referência um produto denso, não todos. |
| **H09** — quais interfaces o público conhece | Descobrimos que o CVAT exige Docker e a Supervisely tem curva íngreme; a Roboflow é a mais acessível. Mas **isso descreve os produtos, não o nosso usuário**. | **Aberta** — nenhum destes três é software conhecido pelo Baja. |
| **H08** — necessidade de histórico | A Roboflow mostra versionamento como prática madura, mas **não** define o que o nosso usuário precisaria recuperar. | **Aberta** — RC02 virou pendência vinculada a esta hipótese. |
| **H04** — familiaridade com métricas influencia a interação | RC03 (tabela) e RC01 (tradução de termos) decorrem diretamente desta hipótese. | **Aberta** — sustentada como hipótese de projeto, ainda sem teste. |
| **H01 / H05** — benefício esperado e processo atual | Ver [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md): a análise de concorrência **não** confirma H01 nem H05, e os estados foram corrigidos. | **Corrigidas** — sem evidência suficiente. |

> **Ponto de honestidade epistemológica:** encontrar uma funcionalidade em um concorrente **não** confirma, por si só, um benefício para o nosso usuário nem o processo atual dos integrantes do Baja. É por isso que H01 e H05 foram rebaixadas na matriz de rastreabilidade.

## 7. Referências

| Fonte | Link | Data de acesso |
|---|---|---|
| CVAT (site oficial) | https://www.cvat.ai/ | 27/08/2026 |
| G2 — CVAT Reviews | https://www.g2.com/products/cvat/reviews | 28/09/2026 |
| Oryndex — CVAT *(secundária)* | https://oryndex.co/tools/cvat | 28/09/2026 |
| Francis Okafor — CVAT Review *(secundária)* | https://www.francisokafor.com/tools/cvat | 28/09/2026 |
| Roboflow (site oficial) | https://roboflow.com/ | 27/08/2026 |
| G2 — Roboflow Reviews | https://www.g2.com/products/roboflow/reviews | 28/09/2026 |
| Oryndex — Roboflow *(secundária)* | https://oryndex.co/tools/roboflow | 28/09/2026 |
| SearchTools.ai — Roboflow *(secundária)* | https://searchtools.ai/t/roboflow | 28/09/2026 |
| AppCritica — Roboflow *(secundária)* | https://www.appcritica.com/review/roboflow/ | 28/09/2026 |
| Supervisely (site oficial) | https://supervisely.com/ | 03/09/2026 |
| G2 — Supervisely | https://www.g2.com/sellers/supervisely | 03/09/2026 e 28/09/2026 |

> Fontes marcadas como **secundárias** são agregadoras que reproduzem avaliações do G2. Elas foram usadas para localizar avaliações, mas **as citações devem ser confirmadas na página primária** antes da entrega.

## Checklist

- [X] O mapa inicial de alternativas da Entrega 1 foi revisado e aprofundado.
- [X] Há pelo menos uma análise completa por integrante, com os três arquivos depositados no repositório.
- [X] Cada análise identifica autoria, classificação da alternativa, módulo analisado, contexto, funcionalidades com evidência, opiniões de UX com fonte, modelo de negócio e lições.
- [X] Cada análise contém prints legíveis da interface.
- [ ] Prints mostram telas/estados relevantes **e há captura estática do Supervisely**. As duas gravações de vídeo precisam ser convertidas em prints estáticos dos estados citados (E5, E6). **Pendente.**
- [X] Foram analisados concorrentes e/ou interfaces representativas ao público.
- [X] Cada padrão foi atribuído **apenas** ao produto em que foi verificado, com marcação "não observado" quando o recorte não permite concluir.
- [X] As evidências estão vinculadas a observações específicas, com indicação do que **não** comprovaram e sua origem.
- [X] Opiniões de UX têm fonte identificável.
- [X] As recomendações seguem a cadeia observação → dificuldade → objetivo do usuário → recomendação.
- [X] RC02 foi rebaixada a pendência por conflito com o escopo; RC03 foi corrigida pela evidência; RC04 teve a origem corrigida e o texto adaptado.
- [X] A síntese compara critérios comuns e produz recomendações.
- [X] Não há "copiar porque o concorrente faz"; há justificativa de adequação ao público/contexto.
- [X] O público-alvo foi explicitado e a imprecisão "Estudante FEI" × "integrante Baja" foi registrada.
- [X] Mudanças de escopo e hipóteses afetadas foram registradas na rastreabilidade.
