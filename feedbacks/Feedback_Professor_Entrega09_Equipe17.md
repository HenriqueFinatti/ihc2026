# Feedback do Professor > Entrega 09 > Equipe 17

A equipe cumpriu a quantidade mínima solicitada: apresentou três cenários de interação e três soluções de Design Centrado na Comunicação, com autoria individual identificada, além de mapas de objetivos individuais, um mapa consolidado e um esquema conceitual de signos. A entrega demonstra boa continuidade em relação aos cenários de análise/problema, às personas e às tarefas já modeladas.

Os cenários de interação estão entre os pontos mais bem resolvidos. Em cada caso, vocês identificaram o cenário de origem e explicitaram o que foi mantido, reescrito ou acrescentado pela solução. Também houve cuidado em descrever as ações da pessoa e as respostas do sistema sem antecipar excessivamente componentes visuais. O documento ainda apresenta boa rastreabilidade por meio dos identificadores de personas, cenários, tarefas, requisitos e hipóteses.

As principais revisões concentram-se em dois aspectos. Primeiro, o mapa de objetivos precisa distinguir com mais rigor objetivos finais e objetivos instrumentais, pois parte dos nós atuais descreve passos da interação. Segundo, algumas decisões mais recentes do próprio projeto foram atualizadas em seções isoladas, mas não foram propagadas por completo ao cenário CI03, às conversas e ao esquema de signos. Isso produz contradições na fonte conceitual que deveria orientar as próximas etapas.

## Pontos positivos

- Os três integrantes possuem cenário de interação e solução de Design Centrado na Comunicação identificados nominalmente.
- Cada cenário de interação declara sua origem em um cenário de análise/problema da Entrega 04 e conserva a persona e as tarefas relacionadas.
- As mudanças entre problema e solução são justificadas, com indicação de evidências e de decisões anteriores do projeto.
- As narrativas mostram uma evolução real: os problemas com scripts, arquivos dispersos, compreensão de métricas, comparação de configurações e recuperação de falhas passam a receber intervenções da solução.
- A responsabilidade humana foi preservada. O sistema calcula, organiza, explica e apresenta evidências, enquanto a pessoa avalia relevância, registra conclusões e participa da decisão.
- O Design Centrado na Comunicação usa tópicos, subtópicos, falas do usuário e do preposto do designer, signos e efeitos esperados. As falas são específicas para o domínio do projeto.
- O esquema conceitual de signos é amplo e registra origem, significado, tipo de conteúdo, restrições, valores padrão, prevenção e recuperação.
- Os quatro diagramas de objetivos estão legíveis e possuem relação reconhecível com as personas, tarefas e conversas descritas no texto.
- A rastreabilidade documenta decisões importantes, como a retirada da confiança do modelo e do aviso automático de resultado inconclusivo.

## Correções prioritárias

### 1. Reestruturar o mapa para representar objetivos, e não a sequência de uso

O mapa consolidado possui um objetivo geral pertinente: escolher, com evidências, a configuração usada nos testes do Baja. Os mapas individuais também começam com resultados desejados pelas respectivas personas. Entretanto, diversos nós descendentes descrevem o modo de operar a solução, por exemplo conferir métricas, ler desempenho, enviar entradas ou acompanhar processamento.

Um mapa de objetivos deve representar o que a pessoa deseja alcançar. O detalhamento de como ela conversa com o sistema pertence às tarefas, aos diálogos e, posteriormente, à MoLIC. Quando cada passo da interação é tratado como objetivo, a hierarquia perde sua função e se aproxima de uma decomposição de tarefas.

A equipe precisa revisar os mapas e classificar os objetivos conforme a teoria: objetivos finais, objetivos instrumentais diretos e objetivos instrumentais indiretos. Depois, deve verificar cada nó com uma pergunta simples: este item expressa um resultado desejado pelo usuário ou apenas uma ação executada para chegar a outro resultado? As ações que apenas descrevem o caminho devem permanecer nas tarefas ou nos subtópicos da conversa, sem serem promovidas automaticamente a objetivos.

### 2. Atualizar integralmente o CI03 após a mudança sobre vídeos e quadros

A própria documentação registra, em 16/11/2026, que o sistema passou a aceitar vídeos em MP4 e a extrair seus quadros. Essa decisão foi atualizada no Design Centrado na Comunicação, nos mapas e no esquema de signos, mas o CI03 ainda afirma que Andreia extrai cerca de 40 quadros e que essa extração permanece fora do sistema.

O cenário de interação é a narrativa de referência da solução. Se o mesmo documento apresenta duas versões incompatíveis da atividade, não fica claro qual conversa deve orientar o modelo conceitual e a interface. A equipe deve reescrever o episódio e a seção “O que não muda” do CI03 para mostrar a entrada do vídeo, a extração realizada pelo sistema e o modo como os quadros resultantes passam a compor a sessão de análise.

### 3. Separar configuração treinada de configuração avaliada no conjunto de teste

No CI03, a configuração aparece disponível após o treino “já com as métricas no conjunto de teste”. Contudo, a documentação mais recente registra uma atividade própria para preparar os conjuntos e avaliar a configuração, além da ruptura “configuração sem avaliação no conjunto de teste”. Portanto, terminar o treino não implica, por si só, possuir métricas de teste.

Essa distinção é essencial para a comunicação da interface. “Treinada”, “disponível para execução” e “avaliada no conjunto de teste” representam estados diferentes e produzem ações e falas diferentes. A equipe deve definir essa sequência, corrigir o CI03 e representar no esquema de signos o estado “sem avaliação no conjunto de teste”, sua prevenção ou captura de erro e a forma de recuperação.

### 4. Propagar as decisões atuais para os signos de referência e situação da configuração

O esquema ainda afirma que uma configuração fica “em uso” a partir da decisão da coordenação e mantém como lacuna a origem do valor de referência. A rastreabilidade mais recente, porém, define que a configuração em uso é a última executada, que a decisão da coordenação não altera esse estado e que o valor de referência corresponde às métricas dessa configuração.

Essas definições alteram a interpretação de signos centrais da comparação. A equipe precisa atualizar “situação da configuração”, “valor de referência” e “origem da referência” no esquema, nas falas do CI02 e nos pontos em aberto. Também deve acrescentar o estado “na fila”, registrado para treino e execução, e explicitar que a continuidade do treino ao sair da tela depende de o programa permanecer aberto.

### 5. Harmonizar o vocabulário dos diálogos com o esquema de signos

As listas ao final dos diálogos introduzem denominações como “imagem inconclusiva”, “execução concluída”, “métrica” e “recomendação”, enquanto o esquema consolidado usa outras estruturas ou trata algumas dessas expressões apenas como valores de signos mais gerais. Há ainda uma dependência implícita do conceito de execução para associar configuração, conjunto de teste, data e métricas, mas essa entidade não está definida claramente no esquema.

A equipe deve produzir um vocabulário único. Se “imagem inconclusiva” for apenas uma imagem cuja avaliação permanece duvidosa após a comparação, isso precisa ser declarado do mesmo modo nos diálogos e no esquema. Da mesma forma, vocês devem decidir se “execução” será um signo próprio, com relações e atributos, ou se seus dados serão absorvidos por sessão, estado e resultado. O importante é que cada termo usado nas falas possua uma definição inequívoca no esquema.

## Recomendações de melhoria

- Nos diálogos reutilizados entre personas, indiquem com precisão a conversa de origem, as condições de entrada e o efeito de saída. A expressão “mesmo diálogo” economiza texto, mas pode esconder diferenças de intenção entre Rafael, Larissa e Andreia.
- Revisem a classificação de prevenção e recuperação do nome da configuração. O documento diz que o sistema evita nomes repetidos ao sugerir um nome e também prevê recuperação quando ocorre duplicidade. As duas situações podem coexistir se a pessoa editar a sugestão, mas essa condição precisa ficar explícita.
- Mantenham as hipóteses marcadas enquanto a coleta ainda não tiver produzido evidências. Os exemplos numéricos e as situações construídas funcionam bem como hipóteses de design, desde que não sejam tratados como comportamento comprovado dos usuários.
- Preservem a decisão de que a interface não recomenda automaticamente a melhor configuração. Essa separação entre evidência calculada e julgamento humano está coerente com o projeto e deve permanecer nos próximos modelos.
- Ao atualizar uma decisão transversal, façam uma busca pelos termos afetados em cenários, diálogos, mapas, esquema de signos, síntese e pontos em aberto. Isso evitará que uma correção parcial crie novas contradições.

## Pontos que devem alimentar as próximas entregas

- O modelo de interação deve incluir a ruptura da configuração ainda não avaliada no conjunto de teste e mostrar como a pessoa retoma a atividade.
- Os estados de treino e execução precisam ser únicos e consistentes: na fila, processando, concluído, falhou e, quando aplicável, interrompido por early stopping.
- A relação entre configuração, execução, conjunto de teste, sessão, resultado e métricas precisa chegar às próximas entregas sem ambiguidade.
- A origem do valor de referência já definida no projeto deve aparecer nas falas da interface de maneira compreensível, sem induzir a interpretação de que referência significa recomendação.
- A extração de quadros a partir do vídeo e a exportação do vídeo segmentado precisam ser refletidas na continuação do fluxo, inclusive nas situações de formato inválido ou falha de processamento.
- O resultado da coleta com usuários deverá confirmar ou revisar as hipóteses que sustentam explicações de métricas, comparação visual, histórico e exportação.

## Síntese das ações recomendadas

1. Reclassificar os objetivos em finais, instrumentais diretos e instrumentais indiretos, retirando do mapa os nós que representam apenas passos de interação.
2. Atualizar todo o CI03 para incorporar a entrada de vídeo e a extração de quadros pelo sistema.
3. Separar, no cenário e nos signos, os estados de configuração treinada, disponível e avaliada no conjunto de teste.
4. Corrigir a situação “em uso”, a referência de métricas, o estado “na fila” e a condição de o programa permanecer aberto.
5. Unificar os nomes dos signos usados nos diálogos e no esquema conceitual, definindo claramente o conceito de execução.
6. Propagar essas decisões para a rastreabilidade e para os modelos posteriores.

**Parecer geral:** A Entrega 09 está completa, bem organizada e demonstra domínio crescente da passagem entre problema, interação e comunicação. Os cenários e diálogos são específicos para o projeto, preservam o julgamento humano e constituem uma base consistente para a continuidade. Para atingir maior maturidade conceitual, a equipe precisa tornar o mapa efetivamente orientado a objetivos e eliminar as divergências criadas por decisões posteriores que foram aplicadas apenas em partes do documento. Com essas revisões, a entrega terá condições de funcionar como uma fonte conceitual única e confiável para os próximos artefatos.

## Tratamento dos comentários

*Registro da equipe, 20/11/2026. Cada item foi conferido contra o estado atual de `docs/09_modelo_conceitual.md`, dos scripts dos mapas e das decisões de 16/11/2026 (Entrega 11; `RASTREABILIDADE.md`, §5) antes de qualquer alteração. A E9 não tinha mudado desde 16/11/2026, e todos os pontos do parecer continuavam válidos.*

| Item do parecer | Situação em 20/11/2026 | O que foi feito |
|---|---|---|
| 1. Mapa de objetivos, e não sequência de uso | Não atendido | Os quatro mapas foram refeitos nos scripts `mapa_objetivos_*.py` e gerados de novo. Cada caixa é um resultado desejado, classificado como objetivo final, instrumental direto ou instrumental indireto; os grupos A–D e os subtópicos saíram dos diagramas. Os passos ficam nos diálogos da seção 2 e na tabela de subtópicos. Os IDs O01–O10 e os subtópicos foram mantidos, porque nomeiam as cenas da E10 e as telas da E11; o dicionário ganhou as colunas "Tipo" e "Serve a" |
| 2. CI03 com vídeo e quadros | Não atendido | Episódio, "Diferenças relevantes", "O que não muda" e diálogo da seção 2.3 reescritos: Andreia envia o vídeo, o sistema extrai os quadros, que entram na sessão como imagens; diálogo "enviar o vídeo e escolher as configurações" (O03.1) e ruptura de formato do vídeo |
| 3. Treinada × disponível × avaliada | Não atendido | A configuração fica disponível para execução ao fim do treino e entra na comparação de desempenho depois de avaliada no conjunto de teste, o que o sistema faz automaticamente ao fim de um treino feito pela interface. Novo signo "avaliação no conjunto de teste", com o estado "sem avaliação" (configuração treinada fora da interface ou conjunto de teste alterado), prevenção (PP) e captura de erro (CE); ruptura no CI02 e na Síntese |
| 4. Em uso, referência, fila e programa aberto | Não atendido (decisões de 16/11 só na E11) | "Em uso" = a última configuração executada; a decisão da coordenação não a altera. Valor de referência = métricas dessa configuração, apresentado como ponto de comparação, e não recomendação. Estado "na fila" para treino, execução e avaliação; o treino continua fora da tela só com o programa aberto (aviso e ruptura "programa fechado"). Atualizados o esquema, as falas e as "Diferenças" do CI02 e os pontos em aberto |
| 5. Vocabulário único | Não atendido | Novos signos "execução" e "avaliação no conjunto de teste" e parágrafo com a relação entre configuração, sessão, execução, avaliação, resultado e métricas. Nas listas dos diálogos: "imagem inconclusiva" = avaliação que continua "duvidosa"; "execução concluída" = execução no estado "concluído"; "métrica" = nome do grupo; "recomendação" = conclusão da P03 |
| Recomendações | Atendido | Os diálogos reutilizados indicam o diálogo de origem, a entrada e a saída; nome da configuração com PA (sugestão sem repetição) e RA (quando a pessoa edita a sugestão e repete um nome); marcas `[H]` mantidas; a interface continua sem recomendar automaticamente; busca pelos termos afetados em toda a E9 e na E11 (signo da TL11 ajustado) |
