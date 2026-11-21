# Entrega 10 — MoLIC

**Data:** 14/11/2026 (início) · 16/11/2026 (primeira versão completa) · 20/11/2026 (revisão após feedback)  
**Status:** 🟦 revisada após feedback  
**Responsabilidade:** 1 solução completa por integrante

## Objetivo da atividade

Modelar a interação como uma **conversa entre usuário e preposto do designer**, oferecendo visão global dos caminhos que permitem ao usuário atingir seus objetivos — incluindo alternativas e rupturas relevantes. MoLIC não deve ser reduzida a um fluxograma de telas.

> Use a **notação MoLIC ensinada na disciplina**. Este template foca critérios de qualidade e não substitui a legenda/notação apresentada em aula.

## Atenção a TCCs sem interface original

O MoLIC não modela o algoritmo por dentro. Ele modela a **conversa de interação necessária para que uma pessoa use a contribuição**.

Exemplos de conversas:

- usuário escolhe dados/parâmetros → sistema valida → usuário inicia análise → sistema comunica processamento → usuário interpreta resultado;
- usuário consulta histórico → refina filtros → abre execução → compara com outra;
- administrador seleciona perfil → altera permissão → sistema comunica consequências → administrador confirma/cancela;
- analista recebe alerta → examina evidências → classifica ocorrência → registra decisão.

Modele também rupturas plausíveis: entrada inválida, falha de processamento, ausência de resultado, permissão insuficiente, filtro sem resultados, conflito de alteração, cancelamento ou necessidade de recuperação.

## M01 — Executar, avaliar e comparar a segmentação

**Autor(a):** Tiago Fagundes dos Santos — 22.123.017-0  
**Cenário de interação de origem:** CI01 — Validação de segmentação e comparação de configurações sem scripts (P01, Rafael)  
**Objetivo(s):** O03, O04, O05, O08  
**Tarefa(s) relacionada(s):** T01, T02 (compartilhada com a P02), T03  
**Signos relevantes:** imagem; vídeo; formato aceito; configuração (nome, descrição, métricas no conjunto de teste); estado da execução (na fila, processando, concluído, falhou); progresso; causa da falha; imagem original; máscara; legenda (*Trilha*, *Fora da trilha*); sobreposição; transparência; região ampliada; anotação de referência (sem métricas nas imagens de campo); avaliação da imagem (correta, duvidosa); origem do problema (imagem/captura ou modelo); imagem inconclusiva; conclusão do tipo validação (Entrega 9, seção 4)

### Diagrama

![MoLIC M01](../assets/10_molic/molic_m01.svg)

*Figura — MoLIC M01, por Tiago Fagundes dos Santos.*

**Fonte editável:** [`scripts/diagramas/molic_m01.py`](../scripts/diagramas/molic_m01.py),
 que usa os elementos de MoLIC de [`molic_svg.py`](../scripts/diagramas/molic_svg.py).

### Leitura do diagrama

Explique em texto o caminho principal e pelo menos os caminhos alternativos/rupturas mais importantes.

O diagrama tem um ponto de abertura e **uma única conversa**, sobre o objetivo final de Rafael: validar as imagens do teste, para dizer à equipe se a configuração em uso pode continuar (Entrega 9, mapa da P01). Ela começa com `gco: validar as imagens do teste` e termina com `gcc: validar as imagens do teste`. Os objetivos instrumentais são alcançados dentro dela e aparecem nos IDs das cenas: executar a segmentação das imagens do teste (O03), avaliar cada imagem (O04), comparar as imagens duvidosas com outra configuração (O05) e registrar a conclusão da validação (O08). A coluna da esquerda é o caminho principal; a do centro tem as cenas de alerta e a O04.2; a da direita, a comparação (O05). Nas cenas com termos técnicos, o diálogo `d+u: o que é este termo? (O07.1)` mostra a explicação sem mudar de cena. Descarregar as imagens das câmeras e informar o grupo da equipe acontecem fora do sistema (RQ09).

#### Caminho principal

1. **Ponto de abertura → O03.1 Enviar as entradas e escolher as configurações.** Com `u: segmentar as imagens do teste` (`gco: validar as imagens do teste`), o sistema mostra as configurações disponíveis, cada uma com descrição e métricas no conjunto de teste. Rafael envia as imagens ou os vídeos do teste (o sistema extrai os quadros de cada vídeo) e escolhe a configuração.
2. **O03.1 → processo do sistema.** Com `u: executar`, o sistema confere se todos os arquivos estão em formato aceito.
3. **Processo → O03.2 Acompanhar o processamento.** Com `d: imagens aceitas`, o sistema mostra o estado da execução de cada configuração (na fila, processando, concluído ou falhou), o progresso e a configuração em execução.
4. **O03.2 → O04.1 Ver o resultado sobre a imagem.** Com `d: concluído` e a precondição "execução inicial", o sistema mostra a imagem original e a máscara, com a legenda *Trilha* e *Fora da trilha*. Rafael escolhe a sobreposição, a transparência e a região ampliada. Quando a entrada é um vídeo, ele pode baixar o vídeo com a sobreposição, em MP4.
5. **O04.1 ⇄ O04.2 Conferir se há métricas.** Com `u: qual é o IoU?`, o sistema informa que a imagem é de campo e não tem anotação de referência: não há IoU nem acurácia, e a avaliação é visual. As métricas ficam no desempenho consolidado, calculadas no conjunto de teste. Rafael volta com `u: voltar à imagem`.
6. **O04.1 → O04.3 Registrar a avaliação da imagem.** Com `u: avaliar esta imagem`, Rafael marca a imagem como correta ou duvidosa e, se for o caso, a origem do problema: imagem (captura) ou modelo. Com `u: próxima imagem`, volta à O04.1 para a imagem seguinte; esse laço se repete até todas as imagens estarem avaliadas.
7. **O04.3 → O08.1 Informar a conclusão (validação).** Com `u: registrar a conclusão`, Rafael informa a configuração mais adequada, as imagens inconclusivas e as que tiveram problema na imagem (captura). O tipo de conclusão é validação.
8. **O08.1 → processo → O08.2 Conferir a conclusão.** Com `u: registrar`, o sistema confere se todas as imagens têm avaliação, guarda a conclusão e responde `d: conclusão registrada`, mostrando o que foi registrado.
9. **O08.2 → encerramento.** Com `u: confirmar` (`gcc: validar as imagens do teste`), a conversa termina.

**Comparação com outra configuração (O05).** É o caminho que Rafael segue no CI01 quando há muitas imagens duvidosas, entre os passos 6 e 7:

1. **O04.3 → O05.1 Escolher as configurações a comparar.** Com `u: comparar as duvidosas`, o sistema mostra as configurações disponíveis, com descrição e métricas no conjunto de teste, e indica quais já foram executadas nestas imagens. Rafael escolhe a outra configuração e as imagens duvidosas.
2. **O05.1 → O03.2 Acompanhar o processamento.** Com `u: executar nas imagens duvidosas`, a conversa volta à **mesma cena** da execução inicial (reuso): Rafael não aprende um caminho novo para executar.
3. **O03.2 → O05.2 Comparar na mesma imagem e região.** Com `d: concluído` e a precondição "comparação", o sistema mostra as configurações lado a lado, na mesma região ampliada, com a avaliação já registrada da imagem.
4. **O05.2 → O04.3.** Com `u: voltar à avaliação`, Rafael revê a avaliação das imagens à luz da comparação e segue para a conclusão (passo 7).

A precondição é o que diferencia as duas saídas da O03.2: o mesmo `d: concluído` leva à avaliação depois da execução inicial e à comparação depois da execução de outra configuração.

#### Alternativas e rupturas

| Situação | Onde ocorre | Como o usuário percebe | Caminho de recuperação/saída |
|---|---|---|---|
| Arquivos em formato não aceito | Processo depois da O03.1 | `d: [AL] formato não aceito` — cena de alerta "Arquivos fora do formato aceito", com quais arquivos não são aceitos e os formatos aceitos (imagens JPG ou PNG, vídeos MP4) | `u: trocar os arquivos` volta à O03.1 (seta tracejada); `u: seguir sem eles` segue para a O03.2: os arquivos aceitos entram na fila de execução, e os outros ficam fora da sessão |
| A execução falha em uma imagem | O03.2 | `d: [RA] falhou` — cena de alerta "Falha na execução", com a causa e a imagem afetada; as outras imagens seguem | `u: tentar de novo / deixar de fora` volta à O03.2 (seta tracejada). Quando a falha atinge a configuração inteira (por exemplo, pesos ausentes) ou a solução está fora do sistema, o diálogo diz o que fazer (`[CE]`) |
| Imagem de campo, sem anotação de referência | O04.2 | `d: [PP] imagem de campo, sem anotação de referência: sem métricas; avaliação visual` | Prevenção passiva: não há erro a recuperar. Rafael volta à O04.1 e avalia visualmente, com a sobreposição e a região ampliada |
| Imagens sem avaliação ao registrar a conclusão | Processo depois da O08.1 | `d: [AL] imagens sem avaliação` — cena de alerta com quantas imagens ainda não têm avaliação | `u: avaliá-las antes` volta à O04.3 (seta tracejada), de onde `u: próxima imagem` leva às imagens; `u: concluir assim mesmo` segue para a O08.2 com a conclusão registrada |
| A comparação muda a avaliação de uma imagem | O05.2 | Vê as duas configurações na mesma região, ao lado da avaliação registrada | `u: voltar à avaliação` leva à O04.3, onde a avaliação pode ser alterada |
| A conclusão registrada tem um erro | O08.2 | Vê o registro na conferência e percebe o erro | `u: corrigir` volta à O08.1 (seta tracejada), com o que já foi informado |

### Checklist específico de modelagem

- [x] Existe **ponto de abertura** coerente com o início do objetivo. *(A conversa começa no ponto de abertura do sistema com `u: segmentar as imagens do teste`, que é o primeiro passo do CI01 depois de as imagens chegarem das câmeras.)*
- [x] As **cenas de conversa** representam tópicos/assuntos, não nomes de páginas apenas. *(Os tópicos usam os nomes oficiais da tabela de subtópicos da Entrega 9, seção 3.2. As cenas de alerta têm o assunto da ruptura no título, sem ID, porque não são subtópicos.)*
- [x] As transições/falas deixam claro o que o usuário ou o sistema comunica. *(Falas `u:` e `d:` tiradas da conversa da Entrega 9, seção 2.1.)*
- [x] Há **ponto(s) de encerramento** para objetivos concluídos/abandonados quando aplicável. *(Um: fim da conversa (`gcc: validar as imagens do teste`), que fecha o único `gco`. Não há saída por abandono: todas as rupturas do CI01 têm recuperação dentro do sistema, e a falha em uma imagem não encerra a validação, porque as outras imagens seguem.)*
- [x] Processamentos do sistema estão representados conforme a notação adotada em aula, sem “inventar” fala do usuário. *(Dois processos: conferir o formato dos arquivos e conferir as avaliações antes de registrar a conclusão; as saídas são só falas `d:`. O fim da execução é uma fala `d:` que sai da O03.2.)*
- [x] Rupturas (breakdowns) relevantes têm feedback e caminho de recuperação, não becos sem saída. *(Formato não aceito: alerta com duas saídas; falha na execução: recuperação apoiada, com captura de erro quando a solução está fora do sistema; imagens sem avaliação: alerta com duas saídas; conclusão errada: `u: corrigir`; imagem sem anotação: prevenção passiva na O04.2.)*
- [x] Acessos ubíquos/atalhos só aparecem quando semanticamente justificáveis. *(Nenhum: no CI01 a conversa é uma sequência só, sem ponto que precise ser alcançado de qualquer cena. A explicação de termos (O07.1) é um diálogo das cenas O03.1 e O04.2, e não um acesso ubíquo.)*
- [x] O diagrama cobre caminhos alternativos importantes, e não apenas o “happy path”. *(Comparação com outra configuração (O05) e as rupturas em "Alternativas e rupturas".)*
- [x] Nomes de objetivos, tópicos e signos são coerentes com a Entrega 9. *(Cenas O03.1–O08.2 e signos da seção 4; nomes alinhados em 14/11/2026, `PENDENCIAS.md`, INC-68.)*
- [x] O diagrama é legível em tamanho normal no GitHub. *(SVG gerado por script e conferido com `scripts/diagramas/verificar.js`: nenhum texto fora das caixas, sobreposto ou passando da borda.)*
- [x] O MoLIC representa a conversa usuário–sistema, não o fluxo interno do algoritmo. *(A inferência do modelo não aparece; a O03.2 mostra só o estado e o progresso da execução, e o sistema responde com falas `d:`.)*
- [x] Processamento, filtros, administração, relatórios e históricos incluem retornos/rupturas quando relevantes. *(O processamento tem saídas de erro e a reexecução reaproveita a O03.2. Filtros, administração, relatórios exportáveis e histórico estão fora do recorte (Entrega 1, seção 8; `PENDENCIAS.md`, INC-63; H08). A única exportação no recorte é o vídeo com a sobreposição, em MP4, na O04.1 (desde 16/11/2026).)*

**Limitação conhecida:** na cena de alerta "Imagens sem avaliação", `u: avaliá-las antes` está desenhada até a O04.3, de onde `u: próxima imagem` leva à O04.1; na interação, o sistema pode abrir direto a primeira imagem sem avaliação.


## M02 — Comparar, recomendar e registrar a decisão

**Autor(a):** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3  
**Cenário de interação de origem:** CI02 — Recomendação de configuração a partir da comparação consolidada (P03, Larissa)  
**Objetivo(s):** O06, O07, O08, O09, O10  
**Tarefa(s) relacionada(s):** T04, T05  
**Signos relevantes:** ciclo de testes; configuração (nome, conjunto de teste, data da avaliação); execução e avaliação no conjunto de teste; IoU, acurácia e tempo de inferência; valor de referência e sua origem (configuração em uso, a última executada); maior valor; diferença entre configurações; conclusão do tipo recomendação; configuração indicada; ressalva; decisão da coordenação; condição (Entrega 9, seção 4)

### Diagrama

![MoLIC M02](../assets/10_molic/molic_m02.svg)

*Figura — MoLIC M02, por Henrique Finatti Silveira Belo Trebbi.*

**Fonte editável:** [`scripts/diagramas/molic_m02.py`](../scripts/diagramas/molic_m02.py),
 que usa os elementos de MoLIC de [`molic_svg.py`](../scripts/diagramas/molic_svg.py).

### Leitura do diagrama

Explique em texto o caminho principal e pelo menos os caminhos alternativos/rupturas mais importantes.

O diagrama tem um ponto de abertura do sistema e duas conversas, cada uma sobre um objetivo de Larissa e com um par de abertura (`gco`) e fechamento (`gcc`). A **conversa 1** (colunas da esquerda e do centro), **recomendar uma configuração**, acontece antes da reunião: Larissa compara as configurações do ciclo e registra a recomendação (O06, O07 e O08). A **conversa 2** (coluna da direita), **apresentar e registrar a decisão**, acontece na reunião: ela retoma a análise e registra a decisão da coordenação (O09, O07 e O10). A conversa 1 começa no ponto de abertura; a conversa 2, em um acesso ubíquo. Nas cenas com termos técnicos, o diálogo `d+u: o que é este termo? (O07.1)` mostra a explicação sem mudar de cena.

#### Caminho principal

**Conversa 1 — comparar e recomendar**

1. **Ponto de abertura → O06.1 Escolher as configurações.** Com `u: comparar as configurações do ciclo` (`gco: recomendar uma configuração`), o sistema mostra o ciclo de testes e as configurações com execução concluída, cada uma com nome, conjunto de teste e data da avaliação.
2. **O06.1 → processo do sistema.** Larissa escolhe as configurações e diz `u: comparar as selecionadas`. O sistema confere se todas têm execução concluída no ciclo, se foram avaliadas no conjunto de teste e se foram avaliadas no mesmo conjunto.
3. **Processo → O06.3 Ler o desempenho de cada configuração.** Com `d: avaliadas no mesmo conjunto de teste`, o sistema mostra IoU médio e por classe, acurácia e tempo de inferência; o valor de referência e sua origem (as métricas da configuração em uso, a última executada); o maior valor, que não é recomendação; e a diferença entre configurações, em tabela ou em gráfico.
4. **O06.3 ⇄ O07.2 Julgar a diferença entre configurações.** Com `u: a diferença importa?`, o sistema mostra a diferença e o que a métrica indica e não indica, sem julgar se ela é relevante. Larissa volta com `u: voltar à análise`.
5. **O06.3 → O08.1 Informar a conclusão (recomendação).** Com `u: registrar a recomendação`, Larissa informa a configuração indicada e, se quiser, uma ressalva.
6. **O08.1 → processo → O08.2 Conferir a conclusão.** Com `u: registrar`, o sistema guarda a recomendação e responde `d: recomendação registrada`, mostrando o que foi registrado.
7. **O08.2 → encerramento.** Com `u: confirmar` (`gcc: recomendar uma configuração`), a conversa termina.

**Conversa 2 — apresentar e decidir**

1. **Acesso ubíquo → O09.1 Retomar a análise.** Com `u: apresentar a recomendação` (`gco: apresentar e registrar a decisão`), o sistema mostra a comparação do ciclo, a recomendação e a ressalva registradas.
2. **O09.1 ⇄ O07.2 Julgar a diferença entre configurações.** Se a coordenação pergunta se a diferença importa (O09.2), Larissa abre a **mesma cena** da conversa 1 e volta com `u: voltar à apresentação`.
3. **O09.1 → O10 Registrar a decisão da coordenação.** Com `u: registrar a decisão`, Larissa informa se a recomendação foi aceita, aceita com condição ou adiada e, se for o caso, a condição.
4. **O10 → processo → encerramento.** Com `u: registrar`, o sistema guarda a decisão e responde `d: decisão registrada` (`gcc: apresentar e registrar a decisão`).

**Explicação dos termos (O07.1):** nas cenas com termos técnicos (O06.3, O07.2 e O09.1), o diálogo `d+u: o que é este termo?` mostra o que o termo indica e o que não indica na própria cena. A conversa não muda de cena, por isso não há retorno a desenhar: Larissa continua de onde estava. Na revisão de 20/11/2026, a O07.1 deixou de ser um acesso ubíquo com volta fixa para a O06.3.

#### Alternativas e rupturas

| Situação | Onde ocorre | Como o usuário percebe | Caminho de recuperação/saída |
|---|---|---|---|
| Uma configuração escolhida não tem execução concluída no ciclo | Processo depois da O06.1 | `d: [CE] execução faltante no ciclo` — o sistema diz qual configuração falta e o que fazer fora dele | Encerramento da conversa. Larissa pede a execução ao integrante técnico (fora do sistema) e volta depois pelo ponto de abertura |
| Uma configuração escolhida não foi avaliada no conjunto de teste atual | Processo depois da O06.1 | `d: [CE] sem avaliação no conjunto de teste` — o sistema diz qual configuração não tem métricas e que a avaliação é feita por quem prepara os datasets (P02, M03, O11.3) | Encerramento da conversa. Larissa pede a avaliação a Andreia (fora do sistema) e volta depois pelo ponto de abertura |
| As configurações foram avaliadas em conjuntos de teste diferentes | Processo depois da O06.1 | `d: [AL] conjuntos de teste diferentes` — cena de alerta **O06.2 Conferir se a comparação é válida**, com o conjunto de teste de cada configuração | `u: escolher outras configurações` volta à O06.1 (seta tracejada); `u: comparar mesmo assim` segue para a O06.3, por decisão dela |
| Larissa não entende um termo (IoU, acurácia, referência) | O06.3, O07.2 ou O09.1 | Pede a explicação no próprio termo (`d+u: o que é este termo?`) | A explicação aparece na mesma cena (O07.1, prevenção passiva), e a conversa continua de onde estava |
| Larissa não sabe se a diferença entre as configurações importa | O06.3 ou O09.1 | `u: a diferença importa?` | **O07.2** mostra a diferença e os limites da métrica; o julgamento é dela, e ela pode registrar a incerteza como ressalva na O08.1 |
| A recomendação registrada tem um erro | O08.2 | Vê o registro na conferência e percebe o erro | `u: corrigir` volta à O08.1 (seta tracejada), com o que já foi informado |
| Decisão "aceita com condição" sem a condição | O10 | O sistema não aceita registrar a decisão sem a condição (`[PA]`, no diálogo da cena) | Prevenção ativa: a ruptura é evitada, por isso não há seta de erro |

### Checklist específico de modelagem

- [x] Existe **ponto de abertura** coerente com o início do objetivo. *(A conversa 1 começa no ponto de abertura do sistema; a conversa 2, no acesso ubíquo "apresentar a recomendação", porque a reunião pode começar de qualquer ponto.)*
- [x] As **cenas de conversa** representam tópicos/assuntos, não nomes de páginas apenas. *(Os tópicos usam os nomes oficiais da tabela de subtópicos da Entrega 9, seção 3.2.)*
- [x] As transições/falas deixam claro o que o usuário ou o sistema comunica. *(Falas `u:` e `d:` tiradas da conversa da Entrega 9, seção 2.2.)*
- [x] Há **ponto(s) de encerramento** para objetivos concluídos/abandonados quando aplicável. *(Quatro: fim da conversa 1 (`gcc: recomendar uma configuração`), fim da conversa 2 (`gcc: apresentar e registrar a decisão`) e duas saídas por captura de erro: execução faltante no ciclo e configuração sem avaliação no conjunto de teste.)*
- [x] Processamentos do sistema estão representados conforme a notação adotada em aula, sem “inventar” fala do usuário. *(Três processos: validar a comparação, registrar a recomendação e registrar a decisão; as saídas são só falas `d:`.)*
- [x] Rupturas (breakdowns) relevantes têm feedback e caminho de recuperação, não becos sem saída. *(Conjuntos diferentes: alerta com duas saídas; execução faltante e configuração sem avaliação: capturas de erro que dizem qual configuração e o que fazer; recomendação errada: `u: corrigir`; condição obrigatória: prevenção ativa no diálogo.)*
- [x] Acessos ubíquos/atalhos só aparecem quando semanticamente justificáveis. *(Um: apresentação da recomendação na reunião, que pode começar de qualquer ponto. A explicação de termos é um diálogo das cenas, e não um acesso ubíquo, para que a pessoa continue na cena de onde pediu a explicação.)*
- [x] O diagrama cobre caminhos alternativos importantes, e não apenas o “happy path”. *(Ver "Alternativas e rupturas".)*
- [x] Nomes de objetivos, tópicos e signos são coerentes com a Entrega 9. *(Cenas O06.1–O10 e signos da seção 4; nomes alinhados em 14/11/2026, `PENDENCIAS.md`, INC-68.)*
- [x] O diagrama é legível em tamanho normal no GitHub. *(SVG gerado por script e conferido com `scripts/diagramas/verificar.js`: nenhum texto fora das caixas, sobreposto ou passando da borda.)*
- [x] O MoLIC representa a conversa usuário–sistema, não o fluxo interno do algoritmo. *(O cálculo das métricas não aparece; o sistema só exibe resultados e responde com falas `d:`.)*
- [x] Processamento, filtros, administração, relatórios e históricos incluem retornos/rupturas quando relevantes. *(Os processamentos têm saídas de erro. Filtros, administração, relatórios exportáveis e histórico estão fora do recorte (Entrega 1, seção 8; `PENDENCIAS.md`, INC-63; H08); a única exportação adotada, o vídeo com a sobreposição em MP4, está no M01.)*


## M03 — Preparar os dados, treinar uma configuração e compará-la

**Autor(a):** Mateus Marana Assuena — 22.123.026-1  
**Cenário de interação de origem:** CI03 — Treino e comparação de uma nova configuração em uma janela curta (P02, Andreia)  
**Objetivo(s):** O01, O02, O11, O03, O05, O06 (O06.2, O06.3, O06.4), O07 (O07.2), O08  
**Tarefa(s) relacionada(s):** T02 (compartilhada com a P01), T06, T07, T08  
**Signos relevantes:** modelo; parâmetros de treino (épocas, early stopping e paciência, datasets de treino, batch size, geração de gráficos) e seus valores padrão; nome da configuração; estado (na fila, treinando ou processando, concluído, falhou); época; gráficos de treino e validação; causa da falha; motivo do término do treino; situação da configuração (disponível); avaliação no conjunto de teste (avaliada, sem avaliação); dataset montado; conjunto de teste; imagem; vídeo; quadro; formato aceito; imagem original; máscara; sobreposição; legenda (*Trilha*, *Fora da trilha*); região ampliada; IoU, acurácia e tempo de inferência no conjunto de teste; valor de referência e sua origem; maior valor; anotação de referência; diferença entre configurações; matriz de confusão; conclusão do tipo experimento; configuração candidata; ressalva; próximo experimento (Entrega 9, seção 4)

### Diagrama

![MoLIC M03](../assets/10_molic/molic_m03.svg)

*Figura — MoLIC M03, por Mateus Marana Assuena.*

**Fonte editável:** [`scripts/diagramas/molic_m03.py`](../scripts/diagramas/molic_m03.py),
 que usa os elementos de MoLIC de [`molic_svg.py`](../scripts/diagramas/molic_svg.py).

### Leitura do diagrama

Explique em texto o caminho principal e pelo menos os caminhos alternativos/rupturas mais importantes.

O diagrama tem um ponto de abertura, dois acessos ubíquos e **três conversas**, cada uma sobre um objetivo de Andreia e com um par de abertura (`gco`) e fechamento (`gcc`):

- **Conversa 1, treinar e avaliar uma nova configuração** (coluna da esquerda, em cima): O01 e O02. Ao fim do treino, o sistema avalia a configuração no conjunto de teste, e só então as métricas aparecem.
- **Conversa 3, preparar os dados de treino e de teste** (coluna da direita, em cima): O11, a atividade da tela Datasets. É aberta pelo acesso ubíquo do menu.
- **Conversa 2, comparar e concluir o experimento** (coluna da esquerda, embaixo): O03, O05, O06, O07 e O08. As cenas O03.1, O03.2 e O05.2 são as mesmas do M01, e a O06.2, a O06.3 e a O07.2 são as mesmas do M02 (reuso), desenhadas aqui com as mesmas rupturas.

Nas cenas com termos técnicos, o diálogo `d+u: o que é este termo? (O07.1)` mostra a explicação sem mudar de cena. Pedir a validação em campo e levar a conclusão à reunião acontecem fora do sistema (RQ09); os quadros dos vídeos são extraídos pelo sistema quando o vídeo é enviado (O03.1).

#### Caminho principal

**Conversa 1 — treinar e avaliar uma nova configuração**

1. **Ponto de abertura → O01.1 Escolher o modelo e os parâmetros.** Com `u: treinar uma nova configuração` (`gco: treinar e avaliar uma nova configuração`), o sistema mostra os modelos e os parâmetros de treino, com os valores padrão. Só os datasets montados podem ser escolhidos, e pelo menos um é obrigatório (`[PA]`).
2. **O01.1 → O01.2 Nomear a configuração.** Com `u: continuar`, o sistema sugere um nome a partir do modelo e das épocas, que nunca repete um nome existente. Andreia mantém a sugestão ou a edita.
3. **O01.2 → processo do sistema.** Com `u: iniciar o treino`, o sistema confere o nome e inicia o treino, ou o coloca na fila se houver outra execução em andamento.
4. **Processo → O02.1 Acompanhar o treino.** Com `d: treino na fila ou iniciado`, o sistema mostra o estado do treino (na fila, treinando, concluído ou falhou), a época atual e o total, os gráficos de treino e validação e, ao fim do treino, o estado da avaliação no conjunto de teste. Avisa que o treino continua só enquanto o programa estiver aberto (`[PP]`).
5. **O02.1 → O02.2 Conferir o resultado do treino.** Com `d: treino concluído e avaliado no conjunto de teste`, o sistema mostra em que época o treino terminou e por quê (por exemplo, o early stopping) e, porque a configuração já foi avaliada, o IoU da classe *Trilha*, a acurácia, o tempo de inferência e a matriz de confusão no conjunto de teste.
6. **O02.2 → encerramento ou conversa 2.** Com `u: concluir por agora` (`gcc: treinar e avaliar uma nova configuração`), a conversa termina. Com `u: comparar com outra configuração no vídeo`, a conversa 1 fecha e a conversa 2 abre na mesma fala (`gcc: treinar e avaliar uma nova configuração`; `gco: comparar e concluir o experimento`).

**Sair durante o treino e voltar depois.** Em O02.1, `u: sair` leva a um **encerramento temporário**: Andreia sai, mas o treino continua enquanto o programa estiver aberto. O símbolo é diferente do encerramento comum, porque a atividade do sistema não terminou. Quando ela volta, o acesso ubíquo `u: em que ponto está o treino?` retoma a mesma conversa na O02.1, de qualquer ponto do sistema.

**Conversa 3 — preparar os dados de treino e de teste (O11)**

1. **Acesso ubíquo → O11.1 Conferir os datasets.** Com `u: preparar os dados (Datasets)` (`gco: preparar os dados de treino e de teste`), o sistema mostra as imagens de treino e de teste de cada dataset, o conjunto de teste atual e as configurações sem avaliação no conjunto de teste.
2. **O11.1 → Confirmar a remontagem → processo → O11.2 Montar o dataset.** Com `u: remontar`, o sistema avisa que o conjunto de teste pode mudar e que as configurações avaliadas terão de ser avaliadas de novo (`[AL]`). Com `u: confirmar`, inicia a montagem e mostra o estado e o progresso; com `d: dataset montado`, a conversa volta à O11.1. Com `u: cancelar`, volta à O11.1 sem mudar nada.
3. **O11.1 → O11.3 Avaliar as configurações no conjunto de teste.** Com `u: avaliar as selecionadas`, Andreia escolhe as configurações sem avaliação.
4. **O11.3 → processo → encerramento.** Com `u: avaliar`, o sistema avalia as configurações uma de cada vez e responde `d: avaliação concluída` (`gcc: preparar os dados de treino e de teste`). As configurações avaliadas passam a entrar na comparação de desempenho.

**Conversa 2 — comparar e concluir o experimento**

1. **O02.2 → O03.1 Enviar as entradas e escolher as configurações.** Andreia envia o vídeo do teste (o sistema extrai os quadros) e escolhe as configurações a comparar, cada uma com descrição e métricas no conjunto de teste.
2. **O03.1 → processo → O03.2 Acompanhar o processamento.** Com `u: executar`, o sistema confere o formato dos arquivos e responde `d: entradas aceitas (quadros extraídos)`, mostrando o estado de cada execução (na fila, processando, concluído ou falhou) e o progresso.
3. **O03.2 → O05.2 Comparar na mesma imagem e região.** Com `d: concluído` e a precondição "comparação", o sistema mostra a imagem original, a máscara de cada configuração e a sobreposição ao mesmo tempo. Andreia escolhe o quadro e a região ampliada.
4. **O05.2 → processo → O06.3 Ler o desempenho de cada configuração.** Com `u: comparar as métricas`, o sistema confere se as configurações foram avaliadas no conjunto de teste e se no mesmo conjunto. Com `d: avaliadas no mesmo conjunto de teste`, mostra IoU, acurácia e tempo de inferência; o valor de referência e sua origem (a configuração em uso, a última executada); o maior valor, que não é recomendação; a diferença entre configurações; e o aviso de que os quadros não têm anotação de referência (`[PP]`).
5. **O06.3 ⇄ O07.2 e O06.3 ⇄ O06.4.** Com `u: a diferença importa?`, o sistema mostra a diferença e o que a métrica indica e não indica, sem julgá-la; com `u: onde cada uma erra?`, mostra a matriz de confusão de cada configuração. Andreia volta com `u: voltar à análise`.
6. **O06.3 → O08.1 Informar a conclusão (experimento).** Com `u: registrar a conclusão`, Andreia informa a conclusão, a configuração candidata (ou nenhuma), a ressalva e o próximo experimento.
7. **O08.1 → processo → O08.2 Conferir a conclusão → encerramento.** Com `u: registrar`, o sistema guarda a conclusão junto da comparação e responde `d: conclusão registrada`. Com `u: confirmar` (`gcc: comparar e concluir o experimento`), a conversa termina.

#### Alternativas e rupturas

| Situação | Onde ocorre | Como o usuário percebe | Caminho de recuperação/saída |
|---|---|---|---|
| Nenhum dataset de treino escolhido | O01.1 | O sistema só oferece os datasets montados e não deixa continuar sem pelo menos um (`[PA]`, no diálogo da cena) | Prevenção ativa: a ruptura é evitada, por isso não há seta de erro |
| Nome de configuração repetido | Processo depois da O01.2 | `d: [RA] nome editado já existe: escolha outro`. A sugestão do sistema nunca repete um nome; a ruptura só acontece quando Andreia edita a sugestão | A seta tracejada volta à O01.2, onde ela informa outro nome |
| O treino ou a avaliação são interrompidos | O02.1 | `d: [RA] falhou` — cena de alerta "Treino ou avaliação interrompidos", com a causa (falta de memória ou programa fechado), a etapa, a configuração mantida e um ajuste sugerido (ex.: batch size menor) | `u: reiniciar (com o ajuste)` volta à O02.1 (seta tracejada), sem refazer a configuração |
| Andreia precisa sair durante o treino | O02.1 | O sistema avisa que o treino continua só enquanto o programa estiver aberto | `u: sair` leva ao encerramento temporário; o acesso ubíquo retoma a conversa na O02.1 |
| A remontagem pode mudar o conjunto de teste | O11.1 | `[AL]` — cena de alerta "Confirmar a remontagem" | `u: confirmar` segue para a montagem; `u: cancelar` volta à O11.1 (seta tracejada) |
| A avaliação no conjunto de teste falha | Processo depois da O11.3 | `d: [RA] falhou: tentar de novo` | A seta tracejada volta à O11.3 |
| Arquivos em formato não aceito | Processo depois da O03.1 | `d: [AL] formato não aceito` — cena de alerta "Arquivos fora do formato aceito" | `u: trocar os arquivos` volta à O03.1 (seta tracejada); `u: seguir sem eles` segue para a O03.2, e os arquivos aceitos entram na fila |
| A execução falha em um quadro ou numa configuração inteira | O03.2 | `d: [RA] falhou` — cena de alerta "Falha na execução"; `[CE]` quando a falha atinge a configuração inteira ou a solução está fora do sistema | `u: tentar de novo / deixar de fora` volta à O03.2 (seta tracejada) |
| Uma configuração não foi avaliada no conjunto de teste | Processo depois da O05.2 | `d: [CE] sem avaliação no conjunto de teste` — o sistema diz qual configuração | Encerramento da conversa; Andreia avalia a configuração na conversa 3 (O11.3) e volta |
| As configurações foram avaliadas em conjuntos de teste diferentes | Processo depois da O05.2 | `d: [AL] conjuntos de teste diferentes` — cena de alerta **O06.2 Conferir se a comparação é válida** | `u: voltar aos quadros` volta à O05.2 (seta tracejada); `u: comparar mesmo assim` segue para a O06.3, por decisão dela |
| Quadros sem anotação de referência | O06.3 | `d: [PP] quadros sem anotação de referência: avaliação visual` | Prevenção passiva: as métricas valem para o conjunto de teste, e os quadros são avaliados visualmente na O05.2 |
| A conclusão registrada tem um erro | O08.2 | Vê o registro na conferência e percebe o erro | `u: corrigir` volta à O08.1 (seta tracejada), com o que já foi informado |

### Checklist específico de modelagem

- [x] Existe **ponto de abertura** coerente com o início do objetivo. *(A conversa 1 começa no ponto de abertura do sistema com `u: treinar uma nova configuração`; a conversa 3, no acesso ubíquo "Datasets"; a conversa 2, na saída da O02.2, quando Andreia decide comparar.)*
- [x] As **cenas de conversa** representam tópicos/assuntos, não nomes de páginas apenas. *(Os tópicos usam os nomes oficiais da tabela de subtópicos da Entrega 9, seção 3.2. As cenas de alerta têm o assunto da ruptura no título, sem ID, exceto a O06.2, que é subtópico.)*
- [x] As transições/falas deixam claro o que o usuário ou o sistema comunica. *(Falas `u:` e `d:` tiradas da conversa da Entrega 9, seção 2.3. Cada `gco` está na fala `u:` que inicia a conversa, e cada `gcc`, na fala que a conclui.)*
- [x] Há **ponto(s) de encerramento** para objetivos concluídos/abandonados quando aplicável. *(Quatro encerramentos e um encerramento temporário: fim da conversa 1 (`u: concluir por agora`), fim da conversa 3, fim da conversa 2 e saída por captura de erro quando falta avaliação no conjunto de teste. O encerramento temporário marca a saída durante o treino, que continua enquanto o programa estiver aberto.)*
- [x] Processamentos do sistema estão representados conforme a notação adotada em aula, sem “inventar” fala do usuário. *(Seis processos: iniciar o treino, montar o dataset, avaliar no conjunto de teste, executar nos quadros, conferir a avaliação e o conjunto de teste e registrar a conclusão; as saídas são só falas `d:`. O fim do treino e da execução são falas `d:` que saem da O02.1 e da O03.2.)*
- [x] Rupturas (breakdowns) relevantes têm feedback e caminho de recuperação, não becos sem saída. *(Todas desenhadas no próprio diagrama, sem remeter ao M01 ou ao M02; ver "Alternativas e rupturas".)*
- [x] Acessos ubíquos/atalhos só aparecem quando semanticamente justificáveis. *(Dois: "em que ponto está o treino?", porque o treino é longo e Andreia volta de qualquer ponto do sistema (CI03 [3]); e "Datasets", porque preparar os dados não depende de onde ela está.)*
- [x] O diagrama cobre caminhos alternativos importantes, e não apenas o “happy path”. *(Saída e volta durante o treino, preparação dos dados, consulta à matriz de confusão e as rupturas em "Alternativas e rupturas".)*
- [x] Nomes de objetivos, tópicos e signos são coerentes com a Entrega 9. *(Cenas O01.1–O11.3 e signos da seção 4, revista em 20/11/2026: estado "na fila", avaliação no conjunto de teste e dataset montado.)*
- [x] O diagrama é legível em tamanho normal no GitHub. *(SVG gerado por script e conferido com `scripts/diagramas/verificar.js`: nenhum texto fora das caixas, sobreposto ou passando da borda.)*
- [x] O MoLIC representa a conversa usuário–sistema, não o fluxo interno do algoritmo. *(O treino e a avaliação aparecem só pelo estado, pela época e pelos resultados; parâmetros internos e a arquitetura do modelo ficam fora, como no recorte da Entrega 1.)*
- [x] Processamento, filtros, administração, relatórios e históricos incluem retornos/rupturas quando relevantes. *(Treino, montagem, avaliação e execução têm saídas de erro e retorno. Filtros, administração, relatórios exportáveis e histórico estão fora do recorte (Entrega 1, seção 8; `PENDENCIAS.md`, INC-63; H08); a única exportação adotada, o vídeo com a sobreposição em MP4, está no M01.)*


## Consolidação da equipe

### Cobertura dos objetivos

| Objetivo | MoLIC que cobre | Lacunas/duplicidades | Decisão |
|---|---|---|---|
| O01 | M03 | Nenhuma: O01.1 e O01.2 aparecem só no M03, com as duas rupturas da Síntese da Entrega 9 (dataset faltando e nome repetido). | Objetivo exclusivo da P02; fica no M03. |
| O02 | M03 | Nenhuma: O02.1 e O02.2 aparecem só no M03, com a ruptura de treino ou avaliação interrompidos, o encerramento temporário (o treino continua enquanto o programa estiver aberto) e o acesso ubíquo para voltar durante o treino. As métricas só aparecem depois da avaliação no conjunto de teste, feita pelo sistema ao fim do treino. | Objetivo exclusivo da P02; fica no M03. |
| O11 | M03 | Nenhuma: O11.1, O11.2 e O11.3 aparecem só no M03, numa conversa própria aberta pelo acesso ubíquo "Datasets", com o alerta da remontagem e a falha na avaliação. | Objetivo da P02 que serve a O02 (dados para treinar) e a O06 (configurações avaliadas no mesmo conjunto de teste). A captura de erro "sem avaliação no conjunto de teste" do M02 e do M03 aponta para a O11.3. |
| O03 | M01, M03 | Sem duplicidade: O03.1 e O03.2 são as mesmas cenas nos dois diagramas. As duas personas enviam imagens ou vídeos do teste, e o sistema extrai os quadros dos vídeos; as rupturas da execução estão desenhadas nos dois. | Cada cena é única, e seu conteúdo é a união dos diálogos dos dois diagramas; "entradas" cobre imagens e vídeos. As rupturas de formato e de falha valem para as duas personas; os arquivos aceitos entram na fila. |
| O04 | M01 | Nenhuma: só a P01 avalia imagem a imagem. A P02 olha os quadros na O05.2, mas não registra avaliação por quadro (CI03). | Objetivo exclusivo da P01; fica no M01. |
| O05 | M01, M03 | Possível duplicidade na escolha das configurações: a P01 escolhe na O05.1, e a P02, na O03.1. | Os dois caminhos ficam: a O05.1 é usada quando a entrada já está no sistema e a comparação nasce da avaliação (P01); a O03.1, quando a comparação começa com entradas novas (P02). A O05.2 é a mesma cena nos dois diagramas. |
| O06 | M02, M03 | Uma lacuna: a O06.4 (matriz de confusão) só aparece no M03. | A conferência da O06.2 (avaliação e mesmo conjunto de teste) está desenhada nos dois diagramas, com a captura de erro quando falta avaliação. A O06.4 é aberta a partir da O06.3 por qualquer persona; o M02 não a desenha porque o CI02 não a usa. |
| O07 | M01, M02, M03 | Sem duplicidade: a O07.1 (entender um termo) aparece nos três diagramas como o diálogo `d+u: o que é este termo? (O07.1)`, dentro das cenas com termos técnicos. A O07.2 é a mesma cena no M02 e no M03. | A explicação do termo é mostrada na própria cena, sem mudar de tópico, por isso é diálogo e não cena; a conversa não perde o ponto em que estava. |
| O08 | M01, M02, M03 | Sem duplicidade: O08.1 e O08.2 são as mesmas cenas nos três diagramas. Mudam os campos de cada tipo de conclusão, e o alerta de imagens sem avaliação só existe no M01. | Uma única conversa, em que o tipo de conclusão define os campos: validação (configuração mais adequada, imagens inconclusivas e com problema de captura), recomendação (configuração indicada e ressalva) e experimento (configuração candidata, ressalva e próximo experimento). O alerta de imagens sem avaliação vale só para a validação. |
| O09 | M02 | Nenhuma: O09.1 aparece no M02, e a O09.2 usa a mesma cena O07.2. | Objetivo exclusivo da P03; fica no M02. |
| O10 | M02 | Nenhuma: a condição obrigatória é tratada por prevenção ativa no diálogo da cena. | Objetivo exclusivo da P03; fica no M02. |

As doze rupturas listadas na Síntese da Entrega 9 aparecem em pelo menos um diagrama: formato não aceito e falha na execução no M01 e no M03; imagens sem avaliação no M01; imagem sem anotação de referência no M01 (O04.2) e no M03 (O06.3); execução faltante no ciclo no M02; configuração sem avaliação no conjunto de teste e configurações avaliadas em conjuntos diferentes no M02 e no M03; valor fora do permitido, nome repetido, treino interrompido, remontagem do dataset e falha na avaliação no conjunto de teste no M03.

### Preparação para o Figma

Liste os estados/telas que serão necessários **a partir das conversas modeladas**, incluindo feedback, confirmação, erro e recuperação.

Cada grupo de cenas abaixo corresponde a uma tela ou região de tela do protótipo da Entrega 11. Os estados vêm das falas `d:` e das rupturas dos três MoLIC; nenhum fluxo novo foi acrescentado. As cenas reusadas (O03.1, O03.2, O05.2, O06.2, O06.3, O07.2, O08.1 e O08.2) viram uma única tela, usada por mais de uma persona.

| Tela ou região | Cenas | MoLIC | Feedback e confirmação | Erro e recuperação |
|---|---|---|---|---|
| Configuração de treino | O01.1, O01.2 | M03 | Valores padrão dos parâmetros já preenchidos; só os datasets montados podem ser escolhidos; nome sugerido (modelo + épocas), que nunca repete um nome existente; "treino na fila" ou "treino iniciado" | Sem dataset de treino: não deixa continuar, na própria tela e com o mesmo comportamento das outras telas com campo obrigatório (PA); nome editado repetido: aponta o nome e pede outro (RA) |
| Estado do treino | O02.1, O02.2 | M03 | Na fila ou treinando: época atual e total, gráficos de treino e validação; aviso de que o treino continua só enquanto o programa estiver aberto (PP); treino concluído: estado da avaliação no conjunto de teste (na fila, processando, concluída); depois da avaliação: época e motivo do término, métricas e matriz de confusão no conjunto de teste | Treino ou avaliação interrompidos: causa (ex.: falta de memória, programa fechado), etapa, configuração mantida e ajuste sugerido, com "reiniciar com o ajuste" (RA); sem métricas antes da avaliação |
| Datasets e avaliação no conjunto de teste | O11.1, O11.2, O11.3 | M03 | Imagens de treino e de teste de cada dataset; conjunto de teste atual; configurações sem avaliação; estado e progresso da montagem e da avaliação; "dataset montado", "avaliação concluída" | Remontagem: alerta de que o conjunto de teste pode mudar e as configurações terão de ser avaliadas de novo, com "confirmar" ou "cancelar" (AL); falha na avaliação: causa, com "tentar de novo" (RA, CE) |
| Entradas e configurações | O03.1 | M01, M03 | Envio de imagens ou vídeos (o sistema extrai os quadros); lista de configurações disponíveis, com descrição e métricas no conjunto de teste (F01) | Arquivos em formato não aceito: quais são e quais formatos são aceitos (JPG, PNG, MP4), com "trocar os arquivos" ou "seguir sem eles"; os aceitos entram na fila (AL) |
| Processamento | O03.2 | M01, M03 | Na fila, processando (com progresso e configuração em execução), concluído (F03) | Falhou: causa e imagem afetada, com "tentar de novo" ou "deixar de fora"; falha na configuração inteira ou solução fora do sistema: o que fazer (RA, CE) |
| Resultado e avaliação da imagem | O04.1, O04.2, O04.3 | M01 | Imagem original, máscara e legenda binária; sobreposição, transparência e região ampliada; métricas da imagem quando há anotação de referência; avaliação registrada; quadros de vídeo, com navegação entre quadros e download do vídeo com a sobreposição (MP4) | Imagens de campo não têm anotação de referência: sempre "sem métricas, avaliação visual"; as métricas ficam no desempenho consolidado (PP) |
| Comparação na mesma imagem | O05.1, O05.2 | M01, M03 | Configurações já executadas nas imagens; configurações lado a lado, na mesma região ampliada, com a avaliação registrada | — |
| Desempenho consolidado | O06.1–O06.4, O07.2 | M02, M03 | Ciclo e configurações com execução concluída; IoU, acurácia e tempo de inferência em tabela ou gráfico (F02); valor de referência e sua origem; maior valor; diferença entre configurações e o que a métrica indica e não indica; matriz de confusão | Configuração sem execução no ciclo: qual falta e o que fazer fora do sistema (CE); configuração sem avaliação no conjunto de teste: qual é e que a avaliação é feita em Datasets (O11.3) (CE); conjuntos de teste diferentes: alerta com "escolher outras" ou "comparar mesmo assim" (AL); quadros sem anotação: avaliação visual (PP) |
| Conclusão | O08.1, O08.2 | M01, M02, M03 | Campos conforme o tipo de conclusão (validação, recomendação ou experimento); conferência do que foi registrado, com "confirmar" | Imagens sem avaliação (só na validação): quantas faltam, com "avaliá-las antes" ou "concluir assim mesmo" (AL); conclusão errada: "corrigir" volta ao formulário com os dados preenchidos |
| Apresentação e decisão | O09.1, O10 | M02 | Comparação, recomendação e ressalva registradas; decisão registrada | Decisão "aceita com condição" sem a condição: não deixa registrar (PA) |

**Acessos ubíquos** — viram elementos sempre visíveis, e não telas próprias:

- "Em que ponto está o treino?" (M03): indicador do treino em andamento, que leva ao estado do treino e retoma a conversa depois do encerramento temporário.
- "Preparar os dados (Datasets)" (M03): item de menu que abre a conversa da O11.
- "Apresentar a recomendação" (M02): item de menu que abre a apresentação.

O diálogo "O que é este termo?" (O07.1, nos três MoLIC) não é acesso ubíquo: vira uma explicação no ponto de uso, junto de cada termo técnico, que abre e fecha sem tirar a pessoa da tela em que está (F04).

A confirmação de ação destrutiva do repertório da Entrega 11 aparece na remontagem do dataset (O11, cena de alerta "Confirmar a remontagem").

**Estados do repertório da Entrega 11 que não aparecem nos MoLIC:**

| Estado | Situação | Decisão |
|---|---|---|
| Vazio/sem dados | Não modelado como estado próprio; a falta de execução no ciclo é tratada pela captura de erro da O06.1 | Prototipar só a mensagem da O06.1 |
| Filtro sem resultados | Não há filtros no recorte (F05 depende da H08) | Não se aplica |
| Permissão insuficiente | Perfis e permissões descartados (F07; Entrega 1, seção 8) | Não se aplica |
| Cancelamento da execução ou do treino na fila | Não aparece nas conversas da Entrega 9 nem nos MoLIC | Não prototipar sem antes incluir no MoLIC |
| Dados desatualizados/conflito | Não modelado; o histórico entre sessões está fora do recorte (H08) | Não se aplica |

Os rascunhos da Entrega 6 que usam classes ilustrativas e IoU para qualquer imagem (`PENDENCIAS.md`, INC-59) são corrigidos por esta lista: legenda binária (*Trilha*, *Fora da trilha*), métricas só no conjunto de teste e o estado "sem métricas, avaliação visual".

## Erros frequentes a evitar

- desenhar apenas caixas com nomes de telas e setas de navegação;
- não modelar falhas, cancelamento, volta ou recuperação;
- usar rótulos genéricos (“Tela 1”, “Processo 2”) sem tópico de conversa;
- criar no Figma fluxos que não existem no MoLIC;
- diagrama sem legenda/fonte editável e com texto ilegível.

## Histórico de revisões

| Data | O que mudou | Motivo |
|---|---|---|
| 16/11/2026 | M01 e M03: na O03.1, a entrada passa a "imagens ou vídeos do teste (o sistema extrai os quadros)"; M01: na O04.1, download do vídeo com a sobreposição (MP4); M03: a extração dos quadros sai da nota "Fora do sistema". Leituras, signos, checklists, consolidação (O03) e "Preparação para o Figma" ajustados; diagramas gerados de novo | Decisões da implementação da Entrega 11 (`RASTREABILIDADE.md`, §5; `PENDENCIAS.md`, INC-63) |
| 20/11/2026 | Os três MoLIC: um par `gco`/`gcc` por conversa sobre um objetivo do usuário; O07.1 passa a diálogo nas cenas com termos técnicos; estado "na fila". M01: O04.2 sempre sem métricas; falha na configuração inteira (CE); arquivos aceitos entram na fila. M02: captura de erro "sem avaliação no conjunto de teste"; origem do valor de referência (configuração em uso). M03: três conversas, com a preparação dos dados (O11, tela Datasets); métricas só depois da avaliação no conjunto de teste; encerramento temporário durante o treino; rupturas da execução e O06.2 desenhadas. Legenda com o encerramento temporário; consolidação e "Preparação para o Figma" ajustadas | Parecer da Entrega 10 e correção 1 do parecer da Entrega 11 (tela Datasets fora da modelagem); revisão da Entrega 9 de 20/11/2026 |
