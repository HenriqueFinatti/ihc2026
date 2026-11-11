## Avaliação geral

A equipe selecionou três interfaces relacionadas ao domínio do projeto - CVAT, Roboflow e Supervisely - e apresentou uma síntese comparativa acompanhada de quatro recomendações identificadas. Há uma tentativa concreta de transformar observações em decisões sobre explicação de métricas, histórico, apresentação de dados e acompanhamento do processamento. Esse é o propósito central da atividade.

Entretanto, a entrega está **parcialmente atendida**. Os três produtos estão atribuídos aos três integrantes, mas as análises individuais são apenas referenciadas por links locais cujos arquivos não estão no material recebido. Portanto, não é possível confirmar o requisito de uma análise completa por aluno. As evidências visuais existem, inclusive vídeos do Supervisely, mas sua ligação com os comentários é insuficiente e algumas conclusões excedem aquilo que elas demonstram. O item 5 tem recomendações pertinentes, porém precisa tornar mais precisa sua origem e sua adaptação ao uso por integrantes do Baja FEI.

| Aspecto prioritário | Resultado da verificação |
|---|---|
| Uma interface por integrante | Três atribuições identificadas para três alunos; completude das análises individuais não verificável nos arquivos recebidos. |
| Recomendações derivadas | RC01–RC04 presentes, com produto de origem declarado; fundamentação e adequação ao recorte parcialmente atendidas. |
| Capturas e análise visual | Quatro PNGs e dois vídeos disponíveis; faltam referências a arquivos/estados específicos e associação clara entre cada evidência e os pontos positivos, negativos ou padrões observados. |

## Pontos positivos

- **Continuidade das alternativas:** os três produtos já citados na Entrega 01 foram mantidos, preservando a ligação com o tema de visão computacional.
- **Divisão declarada de responsabilidade:** Tiago está associado ao CVAT, Henrique ao Roboflow e Mateus ao Supervisely.
- **Comparação por critérios comuns:** navegação, feedback, recuperação de erros, terminologia, acessibilidade e eficiência aparecem na síntese, permitindo organizar a discussão de IHC.
- **Recomendações identificáveis:** RC01–RC04 citam produtos de origem e propõem mudanças que podem apoiar a compreensão e o acompanhamento dos resultados.
- **Evidências de interface, não apenas identificação de marcas:** o material apresenta controles, formulários, indicadores, tabelas e gráficos. O vídeo de treinamento mostra mudanças de estado, e a captura atribuída ao Roboflow apresenta uma interação conversacional contextualizada em trilhas off-road.
- **Alguma cautela com complexidade:** a equipe reconhece riscos de excesso de informações e admite que administração/CRUD pode acrescentar funcionalidades desnecessárias.

## Correções prioritárias

### 1. Disponibilizar as análises individuais e demonstrar o requisito por aluno

**Natureza: conformidade com a entrega. Seções relacionadas: entrada da Entrega 01, 1 e 2.**

A Entrega 01 identifica três integrantes. Nesta entrega, a distribuição declarada corresponde ao mínimo quantitativo, mas um link para um arquivo não substitui o conteúdo da análise.

| Integrante | Interface atribuída | Arquivo referenciado | Situação no material recebido |
|---|---|---|---|
| Tiago Fagundes dos Santos | CVAT | `entrega_2/02_Tiago.md` | Não fornecido. |
| Henrique Finatti Silveira Belo Trebbi | Roboflow | `entrega_2/02_Henrique.md` | Não fornecido. |
| Mateus Marana Assuena | Supervisely | `entrega_2/02_Mateus.md` | Não fornecido. |

A equipe precisa incluir esses documentos ou incorporar suas análises ao arquivo principal, preservando a autoria. Separar os textos em arquivos é aceitável; o problema é a ausência dos conteúdos necessários à conferência. Não concluo que os integrantes deixaram de realizar o trabalho, mas que **a realização completa por todos não está comprovada nesta submissão**.

Confiram nesses textos os componentes previstos no modelo: autoria, classificação da alternativa, contexto, funcionalidades com evidências, observações de UX com origem identificável, modelo de negócio e lições para o projeto. No material consolidado, também não se encontram datas de acesso por produto nem identificação precisa do módulo analisado. A data geral da entrega não esclarece isso.

### 2. Vincular as evidências visuais às afirmações e corrigir o alcance da interpretação

**Natureza: conformidade e fundamentação da análise. Seções relacionadas: 3, 3.1 e 4.**

A coluna de prints aponta somente para `assets/02_concorrencia/`. Esse endereço genérico obriga o leitor a adivinhar qual imagem comprova cada observação. O diretório contém os seguintes materiais:

| Evidência | O que permite observar | Limite ou correção necessária |
|---|---|---|
| `cvat_selecao_modelo.png` | Seleção de modelo para anotação automática, correspondência de rótulos, controles e indicação de progresso. | Relacionar cada observação ao trecho correspondente. A composição não demonstra, sozinha, eficiência por atalhos ou experiência em modo escuro. |
| `cvat_metricas.png` | Quantidade de objetos e imagens, tempo de trabalho, velocidade de anotação, tabela de eventos e filtros. | São indicadores do trabalho de anotação; não comprovam acurácia ou comparação do desempenho de modelos de segmentação. |
| `roboflow_input_imagens.png` | Recorte de “Test Your Model”, com opções de arquivo e webcam, no contexto “Off-Road Trail Segmentation”. | O recorte de 341 × 192 pixels mostra apenas uma parte da tela; não permite avaliar o fluxo completo nem resultados de processamento. |
| `roboflow_selecionar_modelos.png` | Resposta conversacional com opções de modelos e justificativas resumidas para trilhas. | Demonstra a apresentação de sugestões; não comprova execução da troca, treinamento concluído, desempenho obtido ou dificuldade de desfazer alterações. |
| `analise-metricas.mp4` | Nos quadros inspecionados, navegação no Supervisely, filtros, estatísticas de dataset, tabelas e visualizações por classe. | Identificar os instantes usados na análise. Há tabelas no próprio produto; a crítica à dependência de gráficos precisa ser delimitada. |
| `treinamento.webm` | Nos quadros inspecionados, configuração de treinamento no Supervisely, seleção de modelos, barras de progresso e gráficos de treinamento/validação. | Sustenta observações sobre acompanhamento da execução; não demonstra, nos trechos inspecionados, recuperação efetiva por checkpoint ou histórico de execuções. |

As evidências dos vídeos foram examinadas por quadros distribuídos ao longo de sua duração. Eles são material complementar válido, mas, para atender ao pedido de prints, incluam também capturas estáticas dos estados do Supervisely utilizados como argumento, com legenda e referência ao vídeo de origem.

Indiquem, para cada evidência, **o que é positivo, negativo ou um padrão observado, qual tarefa está envolvida e qual aprendizado se transfere ao projeto**. Não é obrigatório desenhar setas em todas as imagens: uma legenda precisa ou uma tabela com referência inequívoca pode cumprir essa função. As capturas atuais não possuem essa associação analítica suficientemente explícita.

Informem ainda se a imagem foi obtida por uso próprio, documentação ou demonstração pública. As imagens do CVAT têm apresentação composta; isso não as invalida, mas torna especialmente importante identificar sua origem.

### 3. Refinar RC01–RC04: origem observável, objetivo e adaptação ao Baja FEI

**Natureza: ponto central da Entrega 02 - consistência das recomendações derivadas. Seção relacionada: 5.**

Vocês já fazem mais do que listar funcionalidades: identificam recomendações e apontam produtos de origem. Falta demonstrar a passagem completa **observação → dificuldade/oportunidade → objetivo do usuário → recomendação para o projeto**.

| Recomendação | Avaliação da consistência e pertinência | Direção de revisão |
|---|---|---|
| **RC01 - tooltips para métricas e gráficos** | É coerente com a preocupação sobre linguagem técnica e com o objetivo de facilitar a interpretação. Os indicadores e termos técnicos são observáveis. Porém, não foi demonstrado quais termos causaram dificuldade nem que os usuários do Baja precisam especificamente de tooltips. | Identifiquem os termos ou indicadores de origem e expliquem o que o usuário precisará compreender. Apresentem tooltip como proposta de apoio, sujeita a investigação, e não como solução já validada. |
| **RC02 - versionamento ou histórico de modelos** | Pode apoiar comparação e recuperação, mas reúne necessidades distintas. Histórico de execuções, versões de modelos e retorno a checkpoints não são equivalentes. A justificativa cita histórico no Supervisely sem apontar a evidência específica. | Definam o que deve ser recuperado e para qual decisão. Se o recorte apenas executa modelos disponíveis, não assumam treinamento ou produção de versões. Localizem a evidência da capacidade observada ou mantenham essa origem como pendente. |
| **RC03 - tabelas como alternativa a gráficos** | É pertinente para consultar e comparar valores. Entretanto, `analise-metricas.mp4` já mostra tabelas no Supervisely, inclusive por volta de 8 segundos. A própria evidência permite uma análise mais equilibrada do produto. | Delimitem qual gráfico dificultou qual leitura e reconheçam as tabelas existentes. A recomendação pode derivar de uma solução positiva observada, além de uma limitação. Não tratem tabela como garantia automática de acessibilidade. |
| **RC04 - estados e barras de progresso** | É a recomendação com apoio visual mais direto: a imagem do CVAT mostra progresso, e `treinamento.webm` apresenta barras de épocas e lotes, por volta de 12–18 segundos. A origem declarada cita CVAT e Roboflow, mas o apoio adicional claro está no Supervisely. | Corrijam ou complementem a origem. A captura conversacional do Roboflow mostra um estado textual, não comprova as barras propostas. Adaptem os estados à atividade do projeto: não incluam “treinando” se o usuário apenas executar segmentação. |

As quatro propostas podem contribuir para o projeto, mas **não possuem o mesmo grau de sustentação**. RC02 precisa de maior revisão de escopo; RC03 precisa incorporar o que a própria evidência mostra; RC01 precisa especificar a dificuldade de compreensão; RC04 precisa corrigir a atribuição e explicitar a atividade acompanhada.

Não é necessário implementar essas recomendações agora. É necessário justificar por que cada uma merece entrar no projeto. Escolher um padrão porque ele apareceu em uma ferramenta não basta: a recomendação precisa sobreviver à pergunta “qual tarefa do nosso usuário ela melhora?”.

### 4. Retomar o público e distinguir observação de hipótese

**Natureza: conformidade e problema conceitual de IHC. Seções relacionadas: 1, 3 e 4.**

A seção “Público-alvo” repete a lista de produtos e links, sem descrever quem usará a interface. Na rastreabilidade, o perfil aparece como “Estudante FEI”, definido por interesse em participar do Baja, enquanto a Entrega 01 priorizava integrantes da equipe. Esclareçam se houve mudança ou apenas imprecisão de redação. Interesse no projeto não equivale a executar sua atividade de análise de segmentação.

A seção 3 descreve para que os produtos servem, mas não demonstra que esse público os utiliza no cotidiano. Eles podem ser referências análogas pertinentes mesmo sem uso comprovado pelo Baja. Registrem a familiaridade como hipótese quando ainda não conhecida.

Na síntese, “poucos atalhos”, “contraste ruim no modo escuro”, “difícil desfazer mudanças” e redução do tempo de trabalho precisam de tela, procedimento de inspeção ou fonte identificável. Não estão demonstrados pelas capturas disponíveis. O fato de não aparecer um atalho no recorte também não prova sua ausência no produto.

A frase “É mais simples por conta do chat” precisa ser limitada: o chat oferece uma forma conversacional de interação, mas sua facilidade depende da tarefa e do usuário. Da mesma maneira, “cores simples” não explica como melhorar a leitura. Descrevam o problema visual concreto, sem transformar impressões em conclusões universais.

### 5. Registrar mudanças de escopo e atualizar a rastreabilidade com evidências reais

**Natureza: continuidade e conformidade. Documentos relacionados: Entregas 01 e 02 e matriz de rastreabilidade.**

Na Entrega 01, a tabela de possibilidades descartava histórico com busca e comparação de resultados. Na Entrega 02, histórico, filtros e comparação aparecem como aplicáveis, e RC02 propõe histórico/versionamento. Essa evolução é permitida e pode ser produtiva, mas a matriz de mudanças continua vazia. Registrem qual observação motivou a mudança e quais limites do recorte foram revistos.

Há avanço no preenchimento inicial da matriz e nas formulações de H01–H05. Contudo, H01 e H05 estão marcadas como “sustentada”, e o campo “Evidência obtida” apenas repete essa palavra. Um estado não é uma evidência. Encontrar uma funcionalidade em um concorrente também não confirma, por si só, benefício ou processo atual dos integrantes do Baja.

Relacionem os achados e RC01–RC04 às hipóteses pertinentes, especialmente H08 sobre histórico e às dúvidas de familiaridade e compreensão. Corrijam o ID H10 duplicado e as linhas cujos campos permanecem desalinhados. Não se exigem personas, MoLIC ou testes prontos nesta entrega; o necessário é registrar o que a análise de concorrência efetivamente acrescentou.

O checklist deve refletir esse estado: não é possível confirmar, no conjunto recebido, todas as análises completas, fontes de opiniões e hipóteses atualizadas com evidências.

## Recomendações de melhoria

- Identifiquem explicitamente **C01 = CVAT, C02 = Roboflow e C03 = Supervisely** junto à síntese, incluindo módulo e versão quando conhecidos. No Roboflow, o recorte conversacional precisa ser distinguido de outras partes da plataforma.
- Evitem atribuir os mesmos padrões a todos os produtos sem verificar o objeto da funcionalidade. Uma tabela de eventos de anotação não equivale a comparação de modelos.
- Acrescentem referências diretas a telas, documentação ou demonstrações utilizadas. Os três endereços institucionais, sozinhos, não localizam a origem das opiniões de UX.
- Quando abordarem ajuda contextual, considerem como ela seria acessada por diferentes formas de interação. Quando abordarem progresso, indiquem como o usuário distinguiria processamento, conclusão e falha. São refinamentos pedagógicos, não exigência de protótipo nesta etapa.
- Usem as orientações do capítulo 10 sobre feedback, consistência e conteúdo relevante para explicar a consequência de cada observação, sem transformar esta entrega em uma avaliação heurística formal antecipada.

## Pontos que devem alimentar as próximas entregas

- **Perfis e contexto:** investigar quem efetivamente analisa imagens no Baja, sua familiaridade com métricas e se reconhece as interfaces estudadas.
- **Cenários e tarefas:** distinguir envio de imagens, execução da segmentação, interpretação de resultados e eventual comparação entre modelos; decidir se treinamento pertence ao recorte.
- **Coleta de dados:** investigar a necessidade de histórico, quais informações precisam ser recuperadas e quais termos geram dúvida.
- **Modelagem e prototipação:** levar adiante RC01–RC04 apenas após esclarecer tarefa, origem e limites, preservando os identificadores.
- **Avaliação futura:** verificar compreensão dos resultados e estados, recuperação de informação e adequação das representações, sem confundir qualidade da interface com qualidade científica do modelo.

## Síntese das ações recomendadas

1. Incluir os três arquivos individuais e permitir verificar uma análise completa por integrante.
2. Relacionar os arquivos de `assets/02_concorrencia/` a observações específicas, acrescentando prints do Supervisely e origem dos materiais.
3. Revisar RC01–RC04 conforme evidência, objetivo do usuário e escopo de uso, com atenção especial a RC02 e RC03.
4. Corrigir a interpretação das métricas do CVAT e delimitar afirmações não comprovadas sobre atalhos, contraste, recuperação e facilidade do chat.
5. Explicitar o público e registrar mudanças, achados e recomendações na rastreabilidade; atualizar o checklist.

**Parecer geral:** a Entrega 02 apresenta uma seleção pertinente de três interfaces, evidências visuais aproveitáveis e recomendações com potencial de aplicação ao projeto de segmentação off-road. O atendimento, porém, é parcial: há três responsabilidades declaradas, mas as análises individuais não foram disponibilizadas; as imagens e vídeos de `assets/02_concorrencia/` não estão suficientemente vinculados aos argumentos; e parte das recomendações exige revisão de origem e escopo. A prioridade é tornar verificável o caminho entre aquilo que cada integrante analisou, o que as telas realmente mostram e o que a equipe decidiu aprender para seu próprio usuário. Com esses ajustes, a síntese poderá orientar as próximas etapas com maior consistência.

---

## Tratamento dos comentários

*Registro da equipe, 10/11/2026. Cada item foi conferido contra o estado atual de `docs/02_analise_concorrencia.md`, das análises individuais em `docs/entrega_2/` e das capturas em `assets/02_concorrencia/` antes de qualquer alteração. Boa parte já tinha sido resolvida nas revisões de 28/09, 15/10 e 08/11/2026.*

| Item do parecer | Situação em 10/11/2026 | O que foi feito |
|---|---|---|
| 1. Análises individuais | Já atendido (28/09) | Os três arquivos estão em `docs/entrega_2/`, com autoria, classificação, módulo, datas de acesso, funcionalidades com evidência, opiniões com fonte, modelo de negócio e lições. Nesta revisão, as três "ressalvas de verificação" foram atualizadas (as citações foram confirmadas em 09/11). Tiago: modelos do TCC corrigidos para FCN e DeepLabV3+. Mateus: o módulo analisado deixa de citar seleção de modelo, que não aparece na captura estática. |
| 2. Evidências vinculadas às afirmações | Parcialmente atendido | Nova §3.2 com a leitura de cada evidência (positivo, negativo ou padrão; atividade da Entrega 1; aprendizado). A origem de E1 e E2 foi corrigida: são imagens de divulgação do site do CVAT, não uso próprio (consolidado, análise do Tiago e RAST §7). E5 e E6 citam o vídeo de origem (`treinamento.webm`, `analise-metricas.mp4`). Na análise do Henrique, a descrição da E3 deixou de mencionar uma "prévia do resultado" que o recorte não mostra. As capturas estáticas da Supervisely já existiam desde 08/11. |
| 3. RC01–RC04 | Parcialmente atendido | RC01: origem concreta (ícones "?" do CVAT na E1 e na E2, texto explicativo da E6, legendas técnicas da E5), lista dos termos que o usuário precisa entender e acesso à explicação por mouse, teclado e toque. RC02: "configuração treinada" entre o que poderia ser recuperado. RC03: o gráfico que dificulta a leitura são as curvas da E5; registrado que a E6 combina cor e número. RC04: como distinguir processando, concluído e falha, com estados de execução (analista) separados dos de treino (pesquisador). Graus de sustentação inalterados. |
| 4. Público e observação × hipótese | Já atendido (28/09 e 15/10) | §1 explicita o público e registra a imprecisão "Estudante FEI". A familiaridade é a H09. Atalhos, contraste, "desfazer", "mais simples pelo chat" e "cores simples" não aparecem mais sem fonte. Nesta revisão, §1 e §2 só foram alinhadas à Entrega 1 revisada (pesquisador de modelos e "qual configuração usar"). |
| 5. Mudanças de escopo e rastreabilidade | Já atendido (28/09 e 08/11) | RAST §5 registra as mudanças; H01 e H05 têm evidência descrita; H10 sem duplicidade; RC01–RC04 ligadas às hipóteses. Nesta revisão: RAST §6 (origem da RC01, estado da RC04), §7 (origem de E1 e E2, vídeos de E5 e E6), nova linha na §5 e item novo no checklist. |
| Recomendações | Atendido | C01/C02/C03 com módulo e versão já estavam na §2. Ajuda contextual por diferentes formas de interação (RC01) e distinção entre processamento, conclusão e falha (RC04) incorporadas. A §3.2 explica a consequência de cada observação. |
