# Entrega 10 — MoLIC

**Data:** 14/11/2026 (início)  
**Status:** 🟨 em andamento  
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
**Signos relevantes:** imagem; formato aceito; configuração (nome, descrição, métricas no conjunto de teste); estado da execução (processando, concluído, falhou); progresso; causa da falha; imagem original; máscara; legenda (*Trilha*, *Fora da trilha*); sobreposição; transparência; região ampliada; anotação de referência; IoU e acurácia; avaliação da imagem (correta, duvidosa); origem do problema (imagem/captura ou modelo); imagem inconclusiva; conclusão do tipo validação (Entrega 9, seção 4)

### Diagrama

![MoLIC M01](../assets/10_molic/molic_m01.svg)

*Figura — MoLIC M01, por Tiago Fagundes dos Santos.*

**Fonte editável:** [`scripts/diagramas/molic_m01.py`](../scripts/diagramas/molic_m01.py),
 que usa os elementos de MoLIC de [`molic_svg.py`](../scripts/diagramas/molic_svg.py).

### Leitura do diagrama

Explique em texto o caminho principal e pelo menos os caminhos alternativos/rupturas mais importantes.

O diagrama tem um ponto de abertura e **uma única conversa**, que começa com `gco: executar a segmentação (O03)` e termina com `gcc: validar a segmentação (O03–O05, O08)`. Dentro dela, Rafael passa por quatro objetivos: executa a segmentação das imagens do teste (O03), avalia cada imagem (O04), compara as imagens duvidosas com outra configuração (O05) e registra a conclusão da validação (O08). A entrada em cada novo objetivo é marcada por um `gco` na fala de transição. A coluna da esquerda é o caminho principal; a do centro tem as cenas de alerta e a O04.2; a da direita, a comparação (O05). Descarregar as imagens das câmeras e informar o grupo da equipe acontecem fora do sistema (RQ09).

#### Caminho principal

1. **Ponto de abertura → O03.1 Enviar as entradas e escolher as configurações.** Com `u: segmentar as imagens do teste` (`gco: executar a segmentação, O03`), o sistema mostra as configurações disponíveis, cada uma com descrição e métricas no conjunto de teste. Rafael envia as imagens do teste e escolhe a configuração.
2. **O03.1 → processo do sistema.** Com `u: executar`, o sistema confere se todas as imagens estão em formato aceito.
3. **Processo → O03.2 Acompanhar o processamento.** Com `d: imagens aceitas`, o sistema mostra o estado da execução (processando, concluído ou falhou), o progresso e a configuração em execução.
4. **O03.2 → O04.1 Ver o resultado sobre a imagem.** Com `d: concluído` e a precondição "execução inicial" (`gco: avaliar a segmentação, O04`), o sistema mostra a imagem original e a máscara, com a legenda *Trilha* e *Fora da trilha*. Rafael escolhe a sobreposição, a transparência e a região ampliada.
5. **O04.1 ⇄ O04.2 Conferir se há métricas.** Com `u: qual é o IoU?`, o sistema mostra IoU e acurácia quando a imagem tem anotação de referência. Rafael volta com `u: voltar à imagem`.
6. **O04.1 → O04.3 Registrar a avaliação da imagem.** Com `u: avaliar esta imagem`, Rafael marca a imagem como correta ou duvidosa e, se for o caso, a origem do problema: imagem (captura) ou modelo. Com `u: próxima imagem`, volta à O04.1 para a imagem seguinte; esse laço se repete até todas as imagens estarem avaliadas.
7. **O04.3 → O08.1 Informar a conclusão (validação).** Com `u: registrar a conclusão` (`gco: registrar a conclusão, O08`), Rafael informa a configuração mais adequada, as imagens inconclusivas e as que tiveram problema na imagem (captura). O tipo de conclusão é validação.
8. **O08.1 → processo → O08.2 Conferir a conclusão.** Com `u: registrar`, o sistema confere se todas as imagens têm avaliação, guarda a conclusão e responde `d: conclusão registrada`, mostrando o que foi registrado.
9. **O08.2 → encerramento.** Com `u: confirmar` (`gcc: validar a segmentação, O03–O05 e O08`), a conversa termina.

**Comparação com outra configuração (O05).** É o caminho que Rafael segue no CI01 quando há muitas imagens duvidosas, entre os passos 6 e 7:

1. **O04.3 → O05.1 Escolher as configurações a comparar.** Com `u: comparar as duvidosas` (`gco: comparar, O05`), o sistema mostra as configurações disponíveis, com descrição e métricas no conjunto de teste, e indica quais já foram executadas nestas imagens. Rafael escolhe a outra configuração e as imagens duvidosas.
2. **O05.1 → O03.2 Acompanhar o processamento.** Com `u: executar nas imagens duvidosas`, a conversa volta à **mesma cena** da execução inicial (reuso): Rafael não aprende um caminho novo para executar.
3. **O03.2 → O05.2 Comparar na mesma imagem e região.** Com `d: concluído` e a precondição "comparação", o sistema mostra as configurações lado a lado, na mesma região ampliada, com a avaliação já registrada da imagem.
4. **O05.2 → O04.3.** Com `u: voltar à avaliação`, Rafael revê a avaliação das imagens à luz da comparação e segue para a conclusão (passo 7).

A precondição é o que diferencia as duas saídas da O03.2: o mesmo `d: concluído` leva à avaliação depois da execução inicial e à comparação depois da execução de outra configuração.

#### Alternativas e rupturas

| Situação | Onde ocorre | Como o usuário percebe | Caminho de recuperação/saída |
|---|---|---|---|
| Imagens em formato não aceito | Processo depois da O03.1 | `d: [AL] formato não aceito` — cena de alerta "Imagens fora do formato aceito", com quais imagens não são aceitas e quais formatos são aceitos | `u: trocar os arquivos` volta à O03.1 (seta tracejada); `u: seguir sem elas` segue para a O03.2 com as outras imagens, por decisão dele |
| A execução falha em uma imagem | O03.2 | `d: [RA] falhou` — cena de alerta "Falha na execução", com a causa e a imagem afetada; as outras imagens seguem | `u: tentar de novo / deixar de fora` volta à O03.2 (seta tracejada). Quando a solução está fora do sistema, o diálogo diz o que fazer (`[CE]`) |
| Imagem sem anotação de referência | O04.2 | `d: [PP] sem anotação: não há métricas; avaliação visual` | Prevenção passiva: não há erro a recuperar. Rafael volta à O04.1 e avalia visualmente, com a sobreposição e a região ampliada |
| Imagens sem avaliação ao registrar a conclusão | Processo depois da O08.1 | `d: [AL] imagens sem avaliação` — cena de alerta com quantas imagens ainda não têm avaliação | `u: avaliá-las antes` volta à O04.3 (seta tracejada), de onde `u: próxima imagem` leva às imagens; `u: concluir assim mesmo` segue para a O08.2 com a conclusão registrada |
| A comparação muda a avaliação de uma imagem | O05.2 | Vê as duas configurações na mesma região, ao lado da avaliação registrada | `u: voltar à avaliação` leva à O04.3, onde a avaliação pode ser alterada |
| A conclusão registrada tem um erro | O08.2 | Vê o registro na conferência e percebe o erro | `u: corrigir` volta à O08.1 (seta tracejada), com o que já foi informado |

### Checklist específico de modelagem

- [x] Existe **ponto de abertura** coerente com o início do objetivo. *(A conversa começa no ponto de abertura do sistema com `u: segmentar as imagens do teste`, que é o primeiro passo do CI01 depois de as imagens chegarem das câmeras.)*
- [x] As **cenas de conversa** representam tópicos/assuntos, não nomes de páginas apenas. *(Os tópicos usam os nomes oficiais da tabela de subtópicos da Entrega 9, seção 3.2. As cenas de alerta têm o assunto da ruptura no título, sem ID, porque não são subtópicos.)*
- [x] As transições/falas deixam claro o que o usuário ou o sistema comunica. *(Falas `u:` e `d:` tiradas da conversa da Entrega 9, seção 2.1.)*
- [x] Há **ponto(s) de encerramento** para objetivos concluídos/abandonados quando aplicável. *(Um: fim da conversa (`gcc` O03–O05 e O08). Não há saída por abandono: todas as rupturas do CI01 têm recuperação dentro do sistema, e a falha em uma imagem não encerra a validação, porque as outras imagens seguem.)*
- [x] Processamentos do sistema estão representados conforme a notação adotada em aula, sem “inventar” fala do usuário. *(Dois processos: conferir o formato das imagens e conferir as avaliações antes de registrar a conclusão; as saídas são só falas `d:`. O fim da execução é uma fala `d:` que sai da O03.2.)*
- [x] Rupturas (breakdowns) relevantes têm feedback e caminho de recuperação, não becos sem saída. *(Formato não aceito: alerta com duas saídas; falha na execução: recuperação apoiada, com captura de erro quando a solução está fora do sistema; imagens sem avaliação: alerta com duas saídas; conclusão errada: `u: corrigir`; imagem sem anotação: prevenção passiva na O04.2.)*
- [x] Acessos ubíquos/atalhos só aparecem quando semanticamente justificáveis. *(Nenhum: no CI01 a conversa é uma sequência só, sem ponto que precise ser alcançado de qualquer cena. A explicação de termos (O07.1) não é objetivo da P01 e está no M02.)*
- [x] O diagrama cobre caminhos alternativos importantes, e não apenas o “happy path”. *(Comparação com outra configuração (O05) e as rupturas em "Alternativas e rupturas".)*
- [x] Nomes de objetivos, tópicos e signos são coerentes com a Entrega 9. *(Cenas O03.1–O08.2 e signos da seção 4; nomes alinhados em 14/11/2026, `PENDENCIAS.md`, INC-68.)*
- [x] O diagrama é legível em tamanho normal no GitHub. *(SVG gerado por script e conferido com `scripts/diagramas/verificar.js`: nenhum texto fora das caixas, sobreposto ou passando da borda.)*
- [x] O MoLIC representa a conversa usuário–sistema, não o fluxo interno do algoritmo. *(A inferência do modelo não aparece; a O03.2 mostra só o estado e o progresso da execução, e o sistema responde com falas `d:`.)*
- [x] Processamento, filtros, administração, relatórios e históricos incluem retornos/rupturas quando relevantes. *(O processamento tem saídas de erro e a reexecução reaproveita a O03.2. Filtros, administração, relatórios exportáveis e histórico estão fora do recorte (Entrega 1, seção 8; `PENDENCIAS.md`, INC-63; H08).)*

**Limitação conhecida:** na cena de alerta "Imagens sem avaliação", `u: avaliá-las antes` está desenhada até a O04.3, de onde `u: próxima imagem` leva à O04.1; na interação, o sistema pode abrir direto a primeira imagem sem avaliação.


## M02 — Comparar, recomendar e registrar a decisão

**Autor(a):** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3  
**Cenário de interação de origem:** CI02 — Recomendação de configuração a partir da comparação consolidada (P03, Larissa)  
**Objetivo(s):** O06, O07, O08, O09, O10  
**Tarefa(s) relacionada(s):** T04, T05  
**Signos relevantes:** ciclo de testes; configuração (nome, conjunto de teste, data da execução); IoU, acurácia e tempo de inferência; valor de referência e sua origem; maior valor; diferença entre configurações; conclusão do tipo recomendação; configuração indicada; ressalva; decisão da coordenação; condição (Entrega 9, seção 4)

### Diagrama

![MoLIC M02](../assets/10_molic/molic_m02.svg)

*Figura — MoLIC M02, por Henrique Finatti Silveira Belo Trebbi.*

**Fonte editável:** [`scripts/diagramas/molic_m02.py`](../scripts/diagramas/molic_m02.py),
 que usa os elementos de MoLIC de [`molic_svg.py`](../scripts/diagramas/molic_svg.py).

### Leitura do diagrama

Explique em texto o caminho principal e pelo menos os caminhos alternativos/rupturas mais importantes.

O diagrama tem um ponto de abertura do sistema e duas conversas sobre objetivos, cada uma com sua abertura (`gco`) e seu fechamento (`gcc`). A **conversa 1** (colunas da esquerda e do centro) acontece antes da reunião: Larissa compara as configurações do ciclo e registra a recomendação (O06, O07 e O08). A **conversa 2** (coluna da direita) acontece na reunião: ela retoma a análise e registra a decisão da coordenação (O09, O07 e O10). A conversa 1 começa no ponto de abertura; a conversa 2, em um acesso ubíquo.

#### Caminho principal

**Conversa 1 — comparar e recomendar**

1. **Ponto de abertura → O06.1 Escolher as configurações.** Com `u: comparar as configurações do ciclo` (`gco: comparar o desempenho, O06`), o sistema mostra o ciclo de testes e as configurações com execução concluída, cada uma com nome, conjunto de teste e data.
2. **O06.1 → processo do sistema.** Larissa escolhe as configurações e diz `u: comparar as selecionadas`. O sistema confere se todas têm execução concluída e se foram avaliadas no mesmo conjunto de teste.
3. **Processo → O06.3 Ler o desempenho de cada configuração.** Com `d: mesmo conjunto de teste`, o sistema mostra IoU médio e por classe, acurácia e tempo de inferência, o valor de referência e sua origem, o maior valor e a diferença entre configurações, em tabela ou em gráfico.
4. **O06.3 ⇄ O07.2 Julgar a diferença entre configurações.** Com `u: a diferença importa?`, o sistema mostra a diferença e o que a métrica indica e não indica, sem julgar se ela é relevante. Larissa volta com `u: voltar à análise`.
5. **O06.3 → O08.1 Informar a conclusão (recomendação).** Com `u: registrar a recomendação` (`gco: registrar a conclusão, O08`), Larissa informa a configuração indicada e, se quiser, uma ressalva.
6. **O08.1 → processo → O08.2 Conferir a conclusão.** Com `u: registrar`, o sistema guarda a recomendação e responde `d: recomendação registrada`, mostrando o que foi registrado.
7. **O08.2 → encerramento.** Com `u: confirmar` (`gcc: comparar e recomendar, O06 e O08`), a conversa termina.

**Conversa 2 — apresentar e decidir**

1. **Acesso ubíquo → O09.1 Retomar a análise.** Com `u: apresentar a recomendação` (`gco: apresentar, O09`), o sistema mostra a comparação do ciclo, a recomendação e a ressalva registradas.
2. **O09.1 ⇄ O07.2 Julgar a diferença entre configurações.** Se a coordenação pergunta se a diferença importa (O09.2), Larissa abre a **mesma cena** da conversa 1 e volta com `u: voltar à apresentação`.
3. **O09.1 → O10 Registrar a decisão da coordenação.** Com `u: registrar a decisão` (`gco: registrar a decisão, O10`), Larissa informa se a recomendação foi aceita, aceita com condição ou adiada e, se for o caso, a condição.
4. **O10 → processo → encerramento.** Com `u: registrar`, o sistema guarda a decisão e responde `d: decisão registrada` (`gcc: apresentar e decidir, O09 e O10`).

**Acesso ubíquo à explicação dos termos:** de qualquer cena, `u: o que é este termo?` leva a **O07.1 Entender um termo**, que mostra o que o termo indica e o que não indica. Com `u: voltar à cena anterior`, Larissa retorna à cena de onde veio; o diagrama desenha esse retorno para a O06.3, onde os termos aparecem com mais frequência.

#### Alternativas e rupturas

| Situação | Onde ocorre | Como o usuário percebe | Caminho de recuperação/saída |
|---|---|---|---|
| Uma configuração escolhida não tem execução concluída no ciclo | Processo depois da O06.1 | `d: [CE] configuração sem execução: peça ao integrante técnico` — o sistema diz qual configuração falta e o que fazer fora dele | Encerramento da conversa. Larissa pede a execução ao integrante técnico (fora do sistema) e volta depois pelo ponto de abertura |
| As configurações foram avaliadas em conjuntos de teste diferentes | Processo depois da O06.1 | `d: [AL] conjuntos de teste diferentes` — cena de alerta **O06.2 Conferir se a comparação é válida**, com o conjunto de teste de cada configuração | `u: escolher outras configurações` volta à O06.1 (seta tracejada); `u: comparar mesmo assim` segue para a O06.3, por decisão dela |
| Larissa não entende um termo (IoU, acurácia, referência) | Qualquer cena com métricas | Pede a explicação pelo acesso ubíquo | **O07.1** explica o que o termo indica e não indica (prevenção passiva) e ela volta à cena anterior |
| Larissa não sabe se a diferença entre as configurações importa | O06.3 ou O09.1 | `u: a diferença importa?` | **O07.2** mostra a diferença e os limites da métrica; o julgamento é dela, e ela pode registrar a incerteza como ressalva na O08.1 |
| A recomendação registrada tem um erro | O08.2 | Vê o registro na conferência e percebe o erro | `u: corrigir` volta à O08.1 (seta tracejada), com o que já foi informado |
| Decisão "aceita com condição" sem a condição | O10 | O sistema não aceita registrar a decisão sem a condição (`[PA]`, no diálogo da cena) | Prevenção ativa: a ruptura é evitada, por isso não há seta de erro |

### Checklist específico de modelagem

- [x] Existe **ponto de abertura** coerente com o início do objetivo. *(A conversa 1 começa no ponto de abertura do sistema; a conversa 2, no acesso ubíquo "apresentar a recomendação", porque a reunião pode começar de qualquer ponto.)*
- [x] As **cenas de conversa** representam tópicos/assuntos, não nomes de páginas apenas. *(Os tópicos usam os nomes oficiais da tabela de subtópicos da Entrega 9, seção 3.2.)*
- [x] As transições/falas deixam claro o que o usuário ou o sistema comunica. *(Falas `u:` e `d:` tiradas da conversa da Entrega 9, seção 2.2.)*
- [x] Há **ponto(s) de encerramento** para objetivos concluídos/abandonados quando aplicável. *(Três: fim da conversa 1 (`gcc` O06 e O08), fim da conversa 2 (`gcc` O09 e O10) e saída por captura de erro quando falta execução.)*
- [x] Processamentos do sistema estão representados conforme a notação adotada em aula, sem “inventar” fala do usuário. *(Três processos: validar a comparação, registrar a recomendação e registrar a decisão; as saídas são só falas `d:`.)*
- [x] Rupturas (breakdowns) relevantes têm feedback e caminho de recuperação, não becos sem saída. *(Conjuntos diferentes: alerta com duas saídas; execução faltante: captura de erro com orientação; recomendação errada: `u: corrigir`; condição obrigatória: prevenção ativa no diálogo.)*
- [x] Acessos ubíquos/atalhos só aparecem quando semanticamente justificáveis. *(Dois: explicação de termos, que aparecem em várias cenas (RC01), e apresentação da recomendação na reunião.)*
- [x] O diagrama cobre caminhos alternativos importantes, e não apenas o “happy path”. *(Ver "Alternativas e rupturas".)*
- [x] Nomes de objetivos, tópicos e signos são coerentes com a Entrega 9. *(Cenas O06.1–O10 e signos da seção 4; nomes alinhados em 14/11/2026, `PENDENCIAS.md`, INC-68.)*
- [x] O diagrama é legível em tamanho normal no GitHub. *(SVG gerado por script e conferido com `scripts/diagramas/verificar.js`: nenhum texto fora das caixas, sobreposto ou passando da borda.)*
- [x] O MoLIC representa a conversa usuário–sistema, não o fluxo interno do algoritmo. *(O cálculo das métricas não aparece; o sistema só exibe resultados e responde com falas `d:`.)*
- [x] Processamento, filtros, administração, relatórios e históricos incluem retornos/rupturas quando relevantes. *(Os processamentos têm saídas de erro. Filtros, administração, relatórios exportáveis e histórico estão fora do recorte (Entrega 1, seção 8; `PENDENCIAS.md`, INC-63; H08).)*

**Limitação conhecida:** a volta do acesso ubíquo O07.1 (`u: voltar à cena anterior`) está desenhada até a O06.3, onde os termos aparecem com mais frequência; na interação, ela leva de volta à cena de onde a pessoa veio.

## M03 — Treinar uma configuração e compará-la

**Autor(a):** Mateus Marana Assuena — 22.123.026-1  
**Cenário de interação de origem:** CI03 — Treino e comparação de uma nova configuração em uma janela curta (P02, Andreia)  
**Objetivo(s):** O01, O02, O03, O05, O06 (O06.3, O06.4), O07 (O07.2), O08  
**Tarefa(s) relacionada(s):** T02 (compartilhada com a P01), T06, T07, T08  
**Signos relevantes:** modelo; parâmetros de treino (épocas, early stopping e paciência, datasets de treino, batch size, geração de gráficos) e seus valores padrão; nome da configuração; treino e estado do treino (treinando, concluído, falhou); época; gráficos de treino e validação; causa da falha; motivo do término do treino; quadro; imagem original; máscara; sobreposição; legenda (*Trilha*, *Fora da trilha*); região ampliada; IoU, acurácia e tempo de inferência no conjunto de teste; anotação de referência; diferença entre configurações; matriz de confusão; conclusão do tipo experimento; configuração candidata; ressalva; próximo experimento (Entrega 9, seção 4)

### Diagrama

![MoLIC M03](../assets/10_molic/molic_m03.svg)

*Figura — MoLIC M03, por Mateus Marana Assuena.*

**Fonte editável:** [`scripts/diagramas/molic_m03.py`](../scripts/diagramas/molic_m03.py),
 que usa os elementos de MoLIC de [`molic_svg.py`](../scripts/diagramas/molic_svg.py).

### Leitura do diagrama

Explique em texto o caminho principal e pelo menos os caminhos alternativos/rupturas mais importantes.

O diagrama tem um ponto de abertura, um acesso ubíquo e dois encerramentos. A conversa começa com `gco: definir uma configuração de treino (O01)` e passa por cinco objetivos: definir a configuração (O01), treinar o modelo (O02), executar e comparar as configurações nos mesmos quadros (O03 e O05), comparar o desempenho no conjunto de teste (O06 e O07) e registrar a conclusão do experimento (O08). Como o treino é longo, Andreia pode sair enquanto ele roda e voltar depois pelo acesso ubíquo "em que ponto está o treino?". As cenas O03.1, O03.2 e O05.2 são as mesmas do M01, e a O06.3 e a O07.2 são as mesmas do M02 (reuso). Extrair os quadros dos vídeos, pedir a validação em campo e levar a conclusão à reunião acontecem fora do sistema (RQ09).

#### Caminho principal

**Treinar a nova configuração**

1. **Ponto de abertura → O01.1 Escolher o modelo e os parâmetros.** Com `u: treinar uma nova configuração` (`gco: definir uma configuração de treino, O01`), o sistema mostra os modelos e os parâmetros de treino que podem ser ajustados, com os valores padrão: épocas, early stopping e paciência, datasets de treino, batch size e geração de gráficos.
2. **O01.1 → O01.2 Nomear a configuração.** Com `u: continuar`, o sistema sugere um nome a partir do modelo e das épocas, e Andreia mantém ou altera o nome.
3. **O01.2 → processo do sistema.** Com `u: iniciar o treino`, o sistema confere se o nome já existe e inicia o treino.
4. **Processo → O02.1 Acompanhar o treino.** Com `d: treino iniciado` (`gco: treinar o modelo, O02`), o sistema mostra o estado do treino (treinando, concluído ou falhou), a época atual e o total, e os gráficos de treino e validação.
5. **O02.1 → O02.2 Conferir o resultado do treino.** Com `d: treino concluído`, o sistema mostra em que época o treino terminou e por quê (por exemplo, o early stopping), o IoU da classe *Trilha*, a acurácia, o tempo de inferência e a matriz de confusão no conjunto de teste, e informa que a configuração está entre as disponíveis.

**Comparar com outra configuração e concluir**

6. **O02.2 → O03.1 Enviar as entradas e escolher as configurações.** Com `u: comparar com outra configuração nestes quadros` (`gco: comparar configurações, O05`), Andreia envia os quadros e escolhe as configurações a comparar, cada uma com descrição e métricas no conjunto de teste.
7. **O03.1 → processo → O03.2 Acompanhar o processamento.** Com `u: executar`, o sistema confere o formato dos quadros e responde `d: entradas aceitas`, mostrando o estado e o progresso da execução de cada configuração.
8. **O03.2 → O05.2 Comparar na mesma imagem e região.** Com `d: concluído` e a precondição "comparação", o sistema mostra a imagem original, a máscara de cada configuração e a sobreposição ao mesmo tempo, com a legenda *Trilha* e *Fora da trilha*. Andreia escolhe o quadro e a região ampliada.
9. **O05.2 → O06.3 Ler o desempenho de cada configuração.** Com `u: comparar as métricas` (`gco: comparar o desempenho, O06`), o sistema mostra IoU da classe *Trilha*, acurácia e tempo de inferência no conjunto de teste e a diferença entre configurações.
10. **O06.3 ⇄ O07.2 Julgar a diferença entre configurações.** Com `u: a diferença importa?`, o sistema mostra a diferença e o que a métrica indica e não indica, sem julgar se ela é relevante. Andreia volta com `u: voltar à análise`.
11. **O06.3 ⇄ O06.4 Consultar a matriz de confusão.** Com `u: onde cada uma erra?`, o sistema mostra a matriz de confusão de cada configuração no conjunto de teste: quanto do que era *Trilha* foi marcado como *Fora da trilha*, e o contrário. Andreia volta com `u: voltar à análise`.
12. **O06.3 → O08.1 Informar a conclusão (experimento).** Com `u: registrar a conclusão` (`gco: registrar a conclusão, O08`), Andreia informa a conclusão, a configuração candidata (ou nenhuma), a ressalva e o próximo experimento.
13. **O08.1 → processo → O08.2 Conferir a conclusão.** Com `u: registrar`, o sistema guarda a conclusão junto da comparação e responde `d: conclusão registrada`, mostrando o que foi registrado.
14. **O08.2 → encerramento.** Com `u: confirmar` (`gcc: comparar e concluir o experimento, O03 e O05–O08`), a conversa termina.

**Sair durante o treino e voltar depois.** Em O02.1, `u: sair (o treino continua)` leva a um encerramento (`gcc: definir, O01`): a configuração já foi definida e o treino segue sem Andreia. Quando ela volta, o acesso ubíquo `u: em que ponto está o treino?` (`gco: treinar o modelo, O02`) abre de novo a O02.1, de qualquer ponto do sistema.

#### Alternativas e rupturas

| Situação | Onde ocorre | Como o usuário percebe | Caminho de recuperação/saída |
|---|---|---|---|
| Nenhum dataset de treino escolhido | O01.1 | O sistema não deixa continuar sem pelo menos um dataset de treino (`[PA]`, no diálogo da cena) | Prevenção ativa: a ruptura é evitada, por isso não há seta de erro |
| Nome de configuração repetido | Processo depois da O01.2 | `d: [RA] nome repetido: escolha outro` | A seta tracejada volta à O01.2, onde Andreia informa outro nome |
| O treino é interrompido | O02.1 | `d: [RA] falhou` — cena de alerta "Treino interrompido", com a causa, a época em que o treino parou, a configuração mantida e um ajuste sugerido (ex.: batch size menor) | `u: reiniciar com o ajuste` volta à O02.1 (seta tracejada), sem refazer a configuração |
| Andreia precisa sair durante o treino | O02.1 | O estado do treino continua disponível | `u: sair (o treino continua)` encerra a conversa; o acesso ubíquo leva de volta à O02.1 |
| Quadros sem anotação de referência | O06.3 | `d: [PP] quadros sem anotação de referência: avaliação visual` | Prevenção passiva: as métricas valem para o conjunto de teste, e os quadros são avaliados visualmente na O05.2 |
| Quadros em formato não aceito ou falha na execução | Processo depois da O03.1 e O03.2 | As mesmas falas `[AL]` e `[RA]` do M01 | Os mesmos caminhos do M01 (seção "Alternativas e rupturas" do M01) |
| A conclusão registrada tem um erro | O08.2 | Vê o registro na conferência e percebe o erro | `u: corrigir` volta à O08.1 (seta tracejada), com o que já foi informado |

### Checklist específico de modelagem

- [x] Existe **ponto de abertura** coerente com o início do objetivo. *(A conversa começa no ponto de abertura do sistema com `u: treinar uma nova configuração`, que é o objetivo do experimento no CI03; a volta durante o treino começa no acesso ubíquo "em que ponto está o treino?".)*
- [x] As **cenas de conversa** representam tópicos/assuntos, não nomes de páginas apenas. *(Os tópicos usam os nomes oficiais da tabela de subtópicos da Entrega 9, seção 3.2. A cena de alerta "Treino interrompido" tem o assunto da ruptura no título, sem ID, porque não é subtópico.)*
- [x] As transições/falas deixam claro o que o usuário ou o sistema comunica. *(Falas `u:` e `d:` tiradas da conversa da Entrega 9, seção 2.3.)*
- [x] Há **ponto(s) de encerramento** para objetivos concluídos/abandonados quando aplicável. *(Dois: saída durante o treino (`gcc` O01), com o treino seguindo sem Andreia, e fim da conversa (`gcc` O03 e O05–O08).)*
- [x] Processamentos do sistema estão representados conforme a notação adotada em aula, sem “inventar” fala do usuário. *(Três processos: iniciar o treino, executar as configurações nos quadros e registrar a conclusão; as saídas são só falas `d:`. O fim do treino e o fim da execução são falas `d:` que saem da O02.1 e da O03.2.)*
- [x] Rupturas (breakdowns) relevantes têm feedback e caminho de recuperação, não becos sem saída. *(Dataset faltando: prevenção ativa no diálogo da O01.1; nome repetido: `[RA]` de volta à O01.2; treino interrompido: alerta com causa, configuração mantida e ajuste sugerido; quadros sem anotação: prevenção passiva na O06.3; conclusão errada: `u: corrigir`. As rupturas da execução são as do M01.)*
- [x] Acessos ubíquos/atalhos só aparecem quando semanticamente justificáveis. *(Um: "em que ponto está o treino?", porque o treino é longo e Andreia o acompanha em janelas curtas, voltando de qualquer ponto do sistema (CI03 [3]).)*
- [x] O diagrama cobre caminhos alternativos importantes, e não apenas o “happy path”. *(Saída e volta durante o treino, consulta à matriz de confusão e as rupturas em "Alternativas e rupturas".)*
- [x] Nomes de objetivos, tópicos e signos são coerentes com a Entrega 9. *(Cenas O01.1–O08.2 e signos da seção 4; subtópicos da P02 incluídos na tabela da seção 3.2 em 15/11/2026, `PENDENCIAS.md`, INC-68.)*
- [x] O diagrama é legível em tamanho normal no GitHub. *(SVG gerado por script e conferido com `scripts/diagramas/verificar.js`: nenhum texto fora das caixas, sobreposto ou passando da borda.)*
- [x] O MoLIC representa a conversa usuário–sistema, não o fluxo interno do algoritmo. *(O treino aparece só pelo estado, pela época e pelos gráficos; parâmetros internos e a arquitetura do modelo ficam fora, como no recorte da Entrega 1.)*
- [x] Processamento, filtros, administração, relatórios e históricos incluem retornos/rupturas quando relevantes. *(O treino e a execução têm saídas de erro e retorno. Filtros, administração, relatórios exportáveis e histórico estão fora do recorte (Entrega 1, seção 8; `PENDENCIAS.md`, INC-63; H08).)*

**Limitação conhecida:** as cenas reusadas do M01 (O03.1, O03.2 e O05.2) e do M02 (O06.3 e O07.2) mostram aqui só os diálogos que a P02 usa; o conteúdo completo de cada cena é a união do que aparece nos três diagramas.


## Consolidação da equipe

### Cobertura dos objetivos

| Objetivo | MoLIC que cobre | Lacunas/duplicidades | Decisão |
|---|---|---|---|
| O01 | M03 | {{...}} | {{...}} |
| O02 | M03 | {{...}} | {{...}} |
| O03 | M01, M03 | {{...}} | {{...}} |
| O04 | M01 | {{...}} | {{...}} |
| O05 | M01, M03 | {{...}} | {{...}} |
| O06 | M02, M03 | {{...}} | {{...}} |
| O07 | M02, M03 | {{...}} | {{...}} |
| O08 | M01, M02, M03 | {{...}} | {{...}} |
| O09 | M02 | {{...}} | {{...}} |
| O10 | M02 | {{...}} | {{...}} |

### Preparação para o Figma

Liste os estados/telas que serão necessários **a partir das conversas modeladas**, incluindo feedback, confirmação, erro e recuperação.

## Erros frequentes a evitar

- desenhar apenas caixas com nomes de telas e setas de navegação;
- não modelar falhas, cancelamento, volta ou recuperação;
- usar rótulos genéricos (“Tela 1”, “Processo 2”) sem tópico de conversa;
- criar no Figma fluxos que não existem no MoLIC;
- diagrama sem legenda/fonte editável e com texto ilegível.
