# Entrega 2 — Público-alvo e análise de concorrência

**Data:** 16/09/2026 (primeira versão) · 28/09/2026 (revisão após feedback) · 10/11/2026 (aplicação final do parecer)  
**Status:** 🟦 revisada após feedback  
**Responsabilidade mínima:** cada integrante analisa pelo menos 1 concorrente/interface representativa; a equipe produz síntese comparativa.

## Objetivo da atividade

Compreender soluções do mesmo domínio **e também interfaces familiares ao público-alvo**. O objetivo não é copiar telas, mas identificar convenções, padrões, affordances percebidas, problemas recorrentes, expectativas e oportunidades de design.

> **Concorrente não precisa ser idêntico ao produto.** Pode atuar na mesma área, resolver objetivo semelhante ou disputar a mesma necessidade. Quando não houver concorrente direto, use produtos análogos e softwares que o público já utiliza.

## Histórico de revisões

- **28/09/2026:** corrigidas atribuições de evidências e recomendações após feedback; RC02 foi rebaixada a pendência e RC03/RC04 foram recalibradas.
- **15/10/2026:** registrada a pendência de capturas estáticas e removidas conclusões que tratavam observações de concorrentes como confirmação sobre o público Baja.
- **08/11/2026 (Fase 2):** E5 e E6 passam a apontar para as capturas estáticas já extraídas, e a pendência das capturas foi fechada; tempos de vídeo retirados do texto; nota repetida da seção 1 unificada; análises individuais ajustadas (H10 refinada, evidência do indicador de progresso, afirmações sobre instalação e custo marcadas como hipótese, referências internas e grafia); preços conferidos nos sites oficiais e citações confirmadas pela equipe; captura E3 do Roboflow mantida como recorte parcial. Ver `PENDENCIAS.md`, INC-06 e INC-20 a INC-30.
- **08/11/2026:** RC03 rebaixada de "alta" para "média": a captura E6 mostra uma tabela de estatística do **dataset** (matriz *Class Co-Occurrence*), não métricas de desempenho de modelo. A seleção de modelo da Supervisely deixou de constar como comprovada, porque a captura E5 mostra progresso e gráficos de treino, mas não a lista de modelos. Classes do exemplo da RC01 alinhadas ao TCC (*Trilha* × *Fora da trilha*). Configurar e treinar os modelos entrou no recorte: atualizadas as notas de escopo da RC02 e da RC04. Ver `PENDENCIAS.md`, INC-12, INC-22, INC-23 e INC-61.
- **10/11/2026:** parecer da Entrega 02 conferido contra o estado atual e aplicado nos pontos que ainda valiam. Nova §3.2 com a leitura analítica de cada evidência (positivo, negativo ou padrão; atividade da Entrega 1; aprendizado). Origem das imagens do CVAT (E1, E2) corrigida: são material de divulgação do site oficial, e não uso próprio. E5 e E6 citam o vídeo de origem. RC01 ganhou origem concreta (ícones de ajuda do CVAT, texto explicativo da E6, legendas técnicas da E5), a lista de termos que o usuário precisa entender e o acesso à explicação por mouse, teclado e toque. RC02 inclui configuração treinada; RC03 delimita o gráfico (curvas da E5) e registra cor + número na E6; RC04 detalha como distinguir os estados e separa execução (analista) de treino (pesquisador de modelos). §1 e §2 alinhadas à revisão da Entrega 1 de 10/11/2026. Análises individuais: ressalvas de verificação atualizadas nas três; origem da E1/E2, modelos do TCC e ícones de ajuda (Tiago); módulo analisado, vídeos de origem e concordância (Mateus); descrição da E3 e grafia (Henrique).

## Entrada obrigatória da Entrega 1

| Item citado na Entrega 1 | Onde foi analisado | Decisão |
|---|---|---|
| CVAT | [`entrega_2/02_Tiago.md`](entrega_2/02_Tiago.md) | **análogo** — referência de padrões (seleção de modelo, indicadores de progresso) |
| Roboflow | [`entrega_2/02_Henrique.md`](entrega_2/02_Henrique.md) | **análogo** — o mais próximo do nosso perfil de usuário |
| Supervisely | [`entrega_2/02_Mateus.md`](entrega_2/02_Mateus.md) | **análogo** — contraponto de densidade funcional |

## 1. Público-alvo desta análise

O público-alvo do **nosso projeto** é o *analista de segmentação da equipe Baja FEI* — um integrante que conhece o domínio off-road e o projeto Baja, mas que pode não dominar programação (ver [`01_conhecendo_o_problema.md`](01_conhecendo_o_problema.md), seção 7.2). As observações sobre treino (Supervisely, E5) interessam sobretudo ao **pesquisador de modelos**, perfil secundário que define configurações e treina os modelos (Entrega 1, §2.2 e §7.1).

**Esta correção foi registrada na rastreabilidade.** A versão anterior utilizava "Estudante FEI" em parte da documentação, o que foi padronizado para "analista de segmentação da equipe Baja FEI". Ver [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md), seção 5.

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

**Achado de IHC:** a atividade central do nosso usuário — *executar a segmentação e compreender o resultado para decidir qual configuração usar* — **não é o centro de nenhuma dessas plataformas**. Elas concentram-se em anotar, treinar e implantar. Isso justifica o nosso recorte: tratar a interpretação do resultado como objetivo principal, e não como etapa intermediária.

## 3. Evidências visuais e o que cada uma comprova

Os arquivos estão em `assets/02_concorrencia/`. A coluna "o que **não** comprova" é tão importante quanto a anterior: evita que uma captura seja usada para sustentar uma afirmação que ela não sustenta.

| Evidência | Arquivo | O que permite observar | O que **não** comprova | Tipo | Origem |
|---|---|---|---|---|---|
| **E1** | [`cvat_selecao_modelo.png`](../assets/02_concorrencia/cvat_selecao_modelo.png) | Seleção de modelo para anotação automática, correspondência de rótulos, controles e indicação de progresso | Eficiência por atalhos; experiência em modo escuro; comportamento em uso real (é material de divulgação, com dados de exemplo) | Imagem de divulgação composta, com as legendas do próprio site | Site oficial do CVAT (https://www.cvat.ai/), material de divulgação, acesso 27/08/2026 |
| **E2** | [`cvat_metricas.png`](../assets/02_concorrencia/cvat_metricas.png) | Quantidade de objetos e imagens, tempo de trabalho, velocidade de anotação, tabela de eventos e filtros | **Acurácia de modelo; comparação de desempenho entre modelos.** São métricas de produtividade de anotação — objeto diferente do nosso. Também não mostra uso real: os dados são de exemplo | Imagem de divulgação | Site oficial do CVAT (https://www.cvat.ai/), material de divulgação, acesso 27/08/2026 |
| **E3** | [`roboflow_input_imagens.png`](../assets/02_concorrencia/roboflow_input_imagens.png) | Recorte de "Test Your Model", com opções de arquivo e webcam, no contexto "Off-Road Trail Segmentation" | O fluxo completo e os resultados do processamento — o recorte tem 341 × 192 px e mostra só parte da tela | Print (recorte parcial) | Uso próprio da equipe, 27/08/2026 |
| **E4** | [`roboflow_selecionar_modelos.png`](../assets/02_concorrencia/roboflow_selecionar_modelos.png) | Resposta conversacional com opções de modelos e justificativas resumidas para trilhas | Que a troca foi executada; que o treinamento terminou; o desempenho obtido; dificuldade de desfazer alterações | Print | Uso próprio da equipe, 27/08/2026 |
| **E5** | [`treinamento-supervisely.png`](../assets/02_concorrencia/treinamento-supervisely.png) | Acompanhamento do treinamento no Supervisely: **barras de progresso de época e lote** e gráficos de treino/validação | Seleção de modelo (não aparece na captura); recuperação efetiva por checkpoint; histórico de execuções | Print extraído da gravação `treinamento.webm`, por volta de 12–18 s | Uso próprio da equipe, 03/09/2026 |
| **E6** | [`analise-metricas-supervisely.png`](../assets/02_concorrencia/analise-metricas-supervisely.png) | Aba de análise do Supervisely: **tabela** de estatística do dataset (*Class Co-Occurrence*) e menu de estatísticas por classe | Tabela de métricas de desempenho do modelo; que o produto dependa de gráficos — **as tabelas existem e contrariam essa leitura** | Print extraído da gravação `analise-metricas.mp4`, por volta de 8 s | Uso próprio da equipe, 03/09/2026 |

> **Capturas estáticas:** atendendo à observação do professor de que a entrega pede *capturas estáticas*, as evidências E5 e E6 foram extraídas das gravações de tela de 03/09/2026 (`treinamento.webm` e `analise-metricas.mp4`) e salvas em `assets/02_concorrencia/` (`treinamento-supervisely.png` e `analise-metricas-supervisely.png`). As gravações continuam como material complementar da equipe.

### 3.1 Padrões de interface observados, por produto

O padrão só é atribuído ao produto **onde foi verificado**. A versão anterior atribuía os mesmos cinco padrões a "CVAT, Roboflow e Supervisely" sem conferir o objeto de cada funcionalidade.

| Padrão | C01 CVAT | C02 Roboflow | C03 Supervisely | Tarefa que serve | Aplicável ao nosso escopo? |
|---|---|---|---|---|---|
| Seleção de modelo em lista explícita | **Sim** (E1) | Parcialmente — via assistente conversacional (E4) | Não comprovado — a captura E5 mostra progresso e gráficos de treino, não a lista de modelos | Escolher qual modelo executar | **Sim** — e preferencialmente em lista, não por chat |
| Indicador de progresso da execução | **Sim** (E1) | Não observado (E4 mostra estado textual, não barra) | **Sim** (E5) | Saber que a segmentação está em curso | **Sim** |
| Tabela de métricas | Não observada (E2 é de produtividade) | Sim — relatado por usuário | Parcial — a E6 mostra tabela de estatística do dataset (*Class Co-Occurrence*), não de desempenho do modelo | Consultar e comparar valores | **Sim** |
| Gráfico de métricas | Não no recorte analisado | Sim — "evaluation graphs" | **Sim** (E6) | Comparar desempenho visualmente | **Sim**, como complemento |
| Filtros | **Sim** (E2) | Não observada | **Sim** (E6) | Restringir o conjunto de dados analisado | **Condicional** — depende de H08 |
| Histórico/versionamento | Não verificado | **Sim** — versionamento de datasets (fonte: G2, via SearchTools.ai) | **Não verificado** — checkpoints não aparecem nos trechos | Recuperar estado anterior | **Condicional** — ver RC02 |
| Administração / CRUD de projetos | Sim — fora do recorte analisado | Sim — fora do recorte analisado | Sim — fora do recorte analisado | Gerenciar projetos e datasets | **Não** — fora do nosso recorte |

> **Sobre "verificado" e "não observado":** a ausência de um elemento no recorte analisado **não prova** que ele não existe no produto. Escrevemos "não observado" ou "não verificado" para não repetir o erro de afirmar ausência a partir de uma captura parcial.

### 3.2 Leitura analítica de cada evidência

Para cada evidência: o que é positivo, negativo ou apenas um padrão observado, qual atividade do nosso usuário está envolvida (Entrega 1, §3.2) e o que se transfere ao projeto. A leitura usa feedback, consistência e relevância do conteúdo como critérios, sem antecipar uma avaliação heurística formal.

| Evidência | Positivo, negativo ou padrão | Atividade envolvida (E1 §3.2) | Aprendizado para o projeto |
|---|---|---|---|
| **E1** — CVAT, seleção de modelo | **Padrão positivo:** modelo escolhido em lista ("Model: SAM 3"); estado em texto ("Automatic annotation is in progress") junto da barra; ícones "?" ao lado de termos técnicos (*Threshold*, mapeamento de rótulos). **Limite:** imagem de divulgação, não uso real. | A02 (iniciar e acompanhar); A04 (escolher o que comparar) | Escolher a configuração em lista; mostrar o estado em texto, e não só na barra; oferecer ajuda no ponto do termo (RC01, RC04). |
| **E2** — CVAT, painel de anotação | **Padrão positivo:** cartões com valor numérico e "?" ao lado de cada indicador; gráficos rotulados com o próprio valor ("150 objects"). **Negativo para o nosso uso:** são números de produtividade de anotação e poderiam ser confundidos com qualidade do modelo. | A03 (interpretar) | Rotular gráficos com o valor e explicar cada indicador; nunca apresentar produtividade como qualidade da segmentação. |
| **E3** — Roboflow, *Test Your Model* | **Padrão positivo:** a entrada de dados é a primeira ação, com duas fontes explícitas (*File* e *Webcam*). **Limite:** recorte parcial; o painel "SAM3" ao lado não mostra conteúdo. | A01 (selecionar e enviar) | Entrada por arquivo como ação primária e visível. A webcam não se aplica ao nosso contexto (análise no laboratório, Entrega 1 §5.1). |
| **E4** — Roboflow, assistente conversacional | **Padrão com ressalva:** cada opção traz uma descrição curta ("Best Match", número de imagens e classes); o estado aparece em texto com tempo decorrido ("Considering trail options (5s)"). **Negativo:** a escolha depende de descobrir o chat e de conversar com ele. | A04 (comparar e escolher) | Descrever cada configuração em uma linha ao lado do nome; escolher por lista, não por conversa (F01). |
| **E5** — Supervisely, treino | **Positivo:** progresso por época e por lote, com contagem e tempo restante ("13/100 [01:18<07:01]"); aviso que explica valores NaN/Inf nos gráficos. **Negativo:** notação técnica ("4.84s/it") e legendas sem explicação ("box loss", "cls loss", "dfl loss"); o valor exato de uma época não é legível nas curvas. | A05 (treinar); A02 (acompanhar) | Progresso com contagem e tempo restante em linguagem simples; explicar os termos dos gráficos (RC01); oferecer os valores também em tabela (RC03). |
| **E6** — Supervisely, *Class Co-Occurrence* | **Positivo:** texto acima da matriz explica o que ela mostra e o que acontece ao clicar em uma célula; cada célula combina cor e número, então a cor não carrega a informação sozinha. **Limite:** é estatística do dataset, não desempenho do modelo. | A03 (interpretar); A04 (comparar) | Explicar cada visualização no próprio lugar (RC01); combinar cor e valor numérico em métricas e legendas (RC03). |

## 4. Síntese comparativa da equipe

Os quatro critérios originais foram mantidos, mas as afirmações que dependiam de impressões não comprovadas foram corrigidas.

| Critério | C01 — CVAT | C02 — Roboflow | C03 — Supervisely | Oportunidade para o projeto |
|---|---|---|---|---|
| **Navegação** | Densa; muitos módulos e tipos de anotação | Integrada em um fluxo único (dataset → implantação) | Densa e orientada a workspace/projeto | Interface simples, com **um fluxo principal** e navegação previsível. |
| **Feedback/estado** | Indicador de progresso na seleção de modelo (E1) e eventos no painel (E2) | O recorte analisado mostra estado **textual** em conversa (E4), não barra | Barras de progresso de época/lote e gráficos de treino (E5) | Unificar em um único indicador que distinga **processando**, **concluído** e **falhou**. |
| **Recuperação de erro** | *Não verificado nas evidências* | Relatam **versionamento de datasets** com retorno a anotações anteriores (fonte: G2, via SearchTools.ai) | *Checkpoints não aparecem nos trechos inspecionados* | Não assumir recuperação sem antes definir **o que** precisa ser recuperado (**RC02**). |
| **Terminologia** | Técnica (rótulos, correspondência, tarefas) | Mais acessível, com justificativas por uso | Técnica e orientada a especialista | Traduzir o essencial: **o que cada classe significa** e **o que as métricas indicam e não indicam**. |
| **Acessibilidade** | *Não verificado* — as capturas não permitem avaliar contraste, modo escuro ou atalhos | Relatos de lentidão e instabilidade com conjuntos grandes (fonte: G2) | Relatos de lentidão (fonte: G2) | Oferecer **tabela como alternativa ao gráfico** (E6 mostra que é possível) e garantir contraste em todas as representações. |
| **Eficiência** | **Correção:** a equipe havia atribuído "excelente suporte a atalhos". As fontes públicas descrevem o sistema de atalhos como **complexo**, demandando tempo para novos anotadores | Relatos de rotulagem assistida por IA reduzindo trabalho manual (fonte: G2) | Integração de etapas em um só ambiente (fonte: G2) | **Não prometer atalhos como diferencial.** Se incluídos, documentá-los. O ganho de eficiência vem de remover o script, não de adicionar atalhos. |

> **Delimitações desta síntese:** as colunas de Roboflow e Supervisely que citam "lentidão" e "versionamento" vêm de **avaliações públicas de terceiros**, não de teste do nosso público. Servem para gerar hipóteses, não para afirmar o comportamento do nosso usuário. Nenhuma afirmação sobre atalhos, contraste ou facilidade foi mantida sem fonte.

## 5. Recomendações derivadas

Cada recomendação segue a cadeia **observação → dificuldade/oportunidade → objetivo do usuário → recomendação**, e declara seu grau de sustentação.

### RC01 — Tradução dos termos técnicos com apoio contextual

| Elemento | Conteúdo |
|---|---|
| **Observação** | Os três produtos usam terminologia técnica, e dois deles já oferecem apoio no ponto de uso. No CVAT, termos como *Threshold* e o mapeamento de rótulos (E1) e cada indicador do painel (E2) têm um ícone "?" ao lado; o conteúdo da ajuda não aparece nas imagens. Na Supervisely, um texto acima da matriz explica o que ela mostra (E6), e um aviso explica valores NaN/Inf nos gráficos de treino (E5). Na mesma E5, as legendas "box loss", "cls loss" e "dfl loss" e a notação "s/it" aparecem sem explicação. |
| **Dificuldade/oportunidade** | O nosso usuário pode não saber o que significa uma classe (no TCC, *Trilha* × *Fora da trilha*) nem o que uma métrica **indica — e o que não indica**. Os termos que ele precisará compreender são: as duas classes; IoU e acurácia, calculadas só no conjunto de teste anotado; e tempo de inferência. Para o pesquisador de modelos, também os termos do treino (época, early stopping, loss). Nenhum desses números indica, sozinho, se um trajeto é seguro (Entrega 1, §4.3). |
| **Objetivo do usuário** | Compreender o que a segmentação está mostrando e avaliar o desempenho sem depender de conhecimento prévio em IA. |
| **Recomendação** | Exibir explicação contextual dos termos no ponto em que aparecem, em vez de apenas "tooltip". A explicação deve abrir com o mouse, com o foco do teclado e com clique ou toque, e não só ao passar o mouse. **Proposta sujeita a investigação** — a Entrega 7 deve verificar quais termos realmente geram dúvida antes de adotá-la. |
| **Sustentação** | **Média.** A observação é verificável e o apoio contextual existe em dois produtos (E1, E2, E6), mas a dificuldade **específica do nosso usuário** ainda não foi demonstrada. |
| **Hipótese relacionada** | H04, H12 |

### RC02 — Histórico e recuperação de análises anteriores *(rebaixada a pendente)*

| Elemento | Conteúdo |
|---|---|
| **Observação** | O Roboflow oferece **versionamento de datasets**, permitindo reverter a um conjunto de anotações anterior (fonte: G2). A Supervisely **não** foi verificada quanto a checkpoints ou histórico nos trechos inspecionados. |
| **Correção de escopo** | A versão anterior desta recomendação propunha "versionamento ou histórico de **modelos**". Nosso recorte é **executar modelos já disponíveis** — não treinamos modelos nem produzimos versões. Portanto, **versionamento de modelos está fora do escopo**. |
| **Dúvida que permanece** | O que precisaria ser recuperado: uma **segmentação passada**, uma **configuração treinada**, ou o **resultado de uma execução**? Cada opção implica funcionalidades diferentes. |
| **Atualização de escopo (08/11/2026)** | Configurar e treinar os modelos entrou no recorte (Entrega 1, §7.1). O argumento "não treinamos modelos" deixa de valer, e guardar mais de uma configuração treinada passa a ser uma pergunta concreta para a H08. |
| **Estado** | **Não é uma recomendação confirmada.** Fica como **pendência vinculada** à hipótese **H08**, a ser investigada na Entrega 7. Só vira recomendação se a equipe demonstrar a necessidade. |
| **Hipótese relacionada** | H08 |

### RC03 — Tabela como alternativa ao gráfico *(corrigida pela própria evidência)*

| Elemento | Conteúdo |
|---|---|
| **Correção** | A versão anterior derivava RC03 da crítica "dependência de gráficos" da Supervisely. Mas **E6 mostra que a Supervisely já oferece tabelas**. A crítica original era injusta com o produto. |
| **Observação corrigida** | Tabelas e filtros coexistem com gráficos na aba de análise da Supervisely (E6) e no Roboflow (relatos de usuário sobre tabelas e gráficos de avaliação). **Limite da evidência:** a tabela visível na E6 é a matriz *Class Co-Occurrence*, uma estatística do dataset (quantas vezes duas classes aparecem juntas); não é uma tabela de métricas de desempenho do modelo. **Qual gráfico dificulta qual leitura:** nas curvas de treino e validação da E5, a tendência é visível, mas o valor exato de uma época não é legível na captura; há controles de zoom, e não verificamos se o valor aparece ao passar o mouse `[?]`. Na E6, cada célula traz cor e número. |
| **Oportunidade** | O padrão **já existe nos produtos analisados** — portanto é uma **solução positiva observada**, e não apenas uma correção de limitação. |
| **Objetivo do usuário** | Consultar e comparar valores exatos de métricas, especialmente quando o gráfico não permite ler um número (como nas curvas da E5). |
| **Recomendação** | Oferecer a métrica **em tabela e em gráfico**, deixando o usuário alternar. **Ressalva:** tabela não é garantia automática de acessibilidade — exige hierarquia visual, rótulos e contraste adequados, e a informação não deve depender só de cor (a E6 mostra cor e número juntos). |
| **Sustentação** | **Média** *(rebaixada de alta em 08/11/2026)* — a E6 comprova que o produto organiza estatísticas em tabela ao lado de gráficos; não comprova uma tabela de métricas de modelo. O apoio a métricas em tabela vem de relatos de usuário do Roboflow (G2), ainda a confirmar. |
| **Hipótese relacionada** | H04, H12 |

### RC04 — Estados de processamento com indicação visual de progresso

| Elemento | Conteúdo |
|---|---|
| **Correção de origem** | A versão anterior atribuía RC04 ao CVAT e ao Roboflow. O **apoio mais direto é da Supervisely** (E5, barras de época e lote); o CVAT tem indicador na seleção de modelo (E1). O recorte do Roboflow (E4) mostra **estado textual em conversa**, e **não** comprova a barra proposta. |
| **Observação** | Barras de progresso por etapa e gráficos de treino/validação na Supervisely (E5); indicador de progresso na seleção de modelo do CVAT (E1); estado em texto com tempo decorrido no assistente do Roboflow (E4). |
| **Dificuldade/oportunidade** | O processamento de segmentação pode demorar. Sem feedback, o usuário não sabe se está executando, terminou ou falhou. |
| **Objetivo do usuário** | Saber em que estado está a execução e evitar repetir ou abandonar uma segmentação desnecessariamente. |
| **Adaptação ao recorte** | Os textos devem descrever a **nossa** atividade. Na execução, feita pelo analista: enviar imagem → processando → resultado pronto → falha. No treino, feito pelo pesquisador de modelos (Entrega 1, §7.1 e A05): treinando (época x de n) → concluído → falha. *Atualização (08/11/2026):* o treino entrou no recorte, então o progresso por época e lote observado na E5 se aplica à tarefa de treinar uma configuração. |
| **Como distinguir os estados** | Cada estado tem rótulo em texto e ícone próprios, sem depender só de cor. O progresso mostra a contagem (como "13/100" na E5) e o tempo restante em linguagem simples, e não em notação técnica como "4.84s/it". A falha diz o que falhou e o que fazer em seguida. |
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
| **H01 / H05** — benefício esperado e processo atual | A análise de concorrência não confirma nenhuma das duas hipóteses para o público Baja. H01 permanece aberta; H05 continua sustentada apenas pela observação interna do processo atual, cuja limitação está registrada na matriz. | **Sem confirmação pela análise de concorrência.** |

> **Ponto de honestidade epistemológica:** encontrar uma funcionalidade em um concorrente **não** confirma, por si só, um benefício para o nosso usuário nem o processo atual dos integrantes do Baja. Por isso, H01 continua aberta e H05 mantém apenas a evidência interna limitada registrada na matriz.

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
| CVAT — preços | https://www.cvat.ai/pricing | 08/11/2026 |
| Roboflow — preços | https://roboflow.com/pricing | 08/11/2026 |
| Supervisely — preços | https://supervisely.com/pricing | 08/11/2026 |
| G2 — Supervisely | https://www.g2.com/sellers/supervisely | 03/09/2026 e 28/09/2026 |

> Fontes marcadas como **secundárias** são agregadoras que reproduzem avaliações do G2. Elas foram usadas para localizar avaliações, mas **as citações devem ser confirmadas na página primária** antes da entrega. *Atualização (08/11/2026): os preços de CVAT, Roboflow e Supervisely foram conferidos nos sites oficiais; as citações foram confirmadas pela equipe nas páginas de origem em 09/11/2026.*

## Checklist

- [X] O mapa inicial de alternativas da Entrega 1 foi revisado e aprofundado.
- [X] Há pelo menos uma análise completa por integrante, com os três arquivos depositados no repositório.
- [X] Cada análise identifica autoria, classificação da alternativa, módulo analisado, contexto, funcionalidades com evidência, opiniões de UX com fonte, modelo de negócio e lições.
- [X] Cada análise contém prints legíveis da interface. *(A captura E3 do Roboflow é um recorte parcial; a limitação está registrada na própria evidência e o fluxo completo não é citado.)*
- [X] Prints mostram telas/estados relevantes **e há captura estática do Supervisely** (E5 e E6, extraídas das gravações de tela).
- [X] Foram analisados concorrentes e/ou interfaces representativas ao público.
- [X] Cada padrão foi atribuído **apenas** ao produto em que foi verificado, com marcação "não observado" quando o recorte não permite concluir.
- [X] As evidências estão vinculadas a observações específicas, com indicação do que **não** comprovaram e sua origem.
- [X] Cada evidência tem leitura analítica: positivo, negativo ou padrão, atividade envolvida e aprendizado (§3.2).
- [X] Opiniões de UX têm fonte identificável.
- [X] As recomendações seguem a cadeia observação → dificuldade → objetivo do usuário → recomendação.
- [X] RC02 foi rebaixada a pendência por conflito com o escopo; RC03 foi corrigida pela evidência; RC04 teve a origem corrigida e o texto adaptado.
- [X] A síntese compara critérios comuns e produz recomendações.
- [X] Não há "copiar porque o concorrente faz"; há justificativa de adequação ao público/contexto.
- [X] O público-alvo foi explicitado e a imprecisão "Estudante FEI" × "integrante Baja" foi registrada.
- [X] Mudanças de escopo e hipóteses afetadas foram registradas na rastreabilidade.
