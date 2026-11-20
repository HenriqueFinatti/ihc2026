# Feedback do Professor > Entrega 10 > Grupo 17

**Entrega:** MoLIC  
**Projeto:** Segmentação Semântica em Vias Off-Road  
**Equipe:** Henrique Finatti Silveira Belo Trebbi, Mateus Marana Assuena e Tiago Fagundes dos Santos  
**Versão avaliada:** 20/11/2026

## Avaliação geral

A equipe cumpriu a responsabilidade individual da entrega. Foram apresentados três diagramas MoLIC, um para cada integrante, com autoria, matrícula, persona, cenário de interação, objetivos e tarefas claramente identificados. M01 foi elaborado por Tiago a partir do CI01, M02 por Henrique a partir do CI02 e M03 por Mateus a partir do CI03. Portanto, não há aluno sem diagrama e não se aplica divisão da nota por entrega coletiva única.

Os diagramas utilizam corretamente a identidade visual e os principais elementos gráficos ensinados: cenas com tópico e diálogos, cenas de alerta tracejadas, falas de transição `u:` e `d:`, processos do sistema em caixas pretas, acessos ubíquos, pontos de abertura e encerramento e indicações de `gco` e `gcc`. Também há relação concreta com o Design Centrado na Comunicação e com o esquema de signos da Entrega 09. A documentação textual é detalhada e ajuda a compreender caminhos principais, alternativas, rupturas e decisões de consolidação.

A principal revisão necessária não está na aparência dos diagramas, que está adequada, mas na consistência semântica. Algumas decisões registradas depois da elaboração inicial dos MoLIC não foram propagadas aos diagramas. Além disso, o uso de `gco` e `gcc`, principalmente no M03, deixa objetivos abertos ou associa o início de uma conversa à resposta do sistema, quando a motivação já partiu do usuário. Há também caminhos do M03 que dependem de referências textuais aos outros diagramas em vez de serem representados graficamente.

## Pontos positivos

- Todos os integrantes entregaram um diagrama individual e assumiram responsabilidade nominal pelo artefato.
- Cada MoLIC declara o cenário de interação de origem e mantém coerência reconhecível com a persona e as tarefas correspondentes.
- O estilo gráfico acompanha o material da disciplina: cenas, cenas de alerta, processos, acessos ubíquos, abertura, encerramento e falas nas setas estão visualmente distinguíveis.
- As cenas apresentam tópicos e signos, e não apenas nomes genéricos de telas.
- As falas internas identificam dados comunicados pelo sistema com `d:` e signos manipulados na conversa com `d+u:`.
- As falas que saem das cenas identificam adequadamente quem motiva a transição, usando `u:` ou `d:`.
- As saídas dos processos internos são comunicadas por falas `d:`, como “imagens aceitas”, “recomendação registrada”, “decisão registrada” e “conclusão registrada”.
- Os três diagramas contemplam rupturas. Há setas de recuperação tracejadas, cenas de alerta, prevenção ativa, prevenção passiva, recuperação apoiada e captura de erro.
- O M01 oferece caminhos para formato não aceito, falha de execução, ausência de anotação, imagens sem avaliação e correção da conclusão.
- O M02 representa corretamente dois momentos da atividade: comparação e recomendação antes da reunião, seguida da apresentação e do registro da decisão.
- O M03 contempla o acompanhamento de uma operação longa, saída durante o treino, retorno por acesso ubíquo e recuperação após interrupção.
- A equipe preserva o julgamento humano. O sistema apresenta métricas, diferenças e explicações, mas não decide automaticamente qual configuração é melhor.
- A consolidação identifica cenas compartilhadas entre personas e busca manter conversas semelhantes com soluções de interação semelhantes.

## Correções prioritárias

### 1. Atualizar os três MoLIC conforme as decisões atuais do projeto

Os diagramas ainda representam uma versão anterior de alguns comportamentos. A rastreabilidade registra decisões posteriores que já fazem parte da solução atual e precisam retornar ao modelo de interação.

No M01, a cena O04.2 ainda admite IoU e acurácia quando uma imagem possui anotação de referência. A solução atual estabelece que apenas imagens de campo são enviadas nessa atividade; por isso, essa cena deve comunicar “sem métricas” e orientar a avaliação visual. As métricas ficam na avaliação consolidada do conjunto de teste. O estado “na fila”, adotado porque treino e execução ocorrem um de cada vez, também precisa aparecer no acompanhamento do processamento.

No M02, a ruptura foi descrita como “configuração sem execução”. A decisão mais recente distingue uma configuração treinada ou executável de uma configuração efetivamente avaliada no conjunto de teste. O problema relevante para a comparação é “configuração sem avaliação no conjunto de teste”. O diagrama deve indicar qual configuração não possui avaliação, comunicar a impossibilidade da comparação e orientar a pessoa para a atividade que produz as métricas.

No M03, a cena O02.2 apresenta IoU, acurácia, tempo de inferência e matriz de confusão imediatamente após a conclusão do treino. Essa sequência não é consistente com a atividade separada de avaliação no conjunto de teste. Terminar o treino deve comunicar que a configuração foi treinada e está disponível para a próxima etapa; as métricas só devem aparecer depois de sua avaliação. A equipe precisa inserir essa conversa ou representar a ruptura que impede a comparação quando a avaliação ainda não ocorreu.

Também deve ser explicitado no M03 que “sair e deixar o treino continuar” só funciona enquanto o programa local permanece aberto. Sem essa condição, a fala promete uma continuidade mais ampla do que a plataforma oferece.

### 2. Revisar o pareamento entre GCO e GCC

Os diagramas usam `gco` para marcar vários objetivos sucessivos e, em alguns casos, encerram todos eles com um único `gcc`. Essa opção precisa ser revista para que cada abertura de conversa tenha um fechamento semanticamente reconhecível ou para que os objetivos instrumentais sejam tratados dentro de uma única conversa sobre o objetivo final.

O problema aparece com maior clareza no M03. A conversa O01 é aberta no início. Depois, `gco: treinar o modelo (O02)` aparece na resposta `d: treino iniciado`, embora a iniciativa já tenha ocorrido na fala anterior `u: iniciar o treino`. Se Andreia permanece até o fim do treino, não há um `gcc` explícito para O01 ou O02. Se ela sai, o encerramento é identificado somente como `gcc: definir (O01)`, apesar de o treino ainda estar em andamento. No encerramento final, aparecem O03 e O05–O08, mas O02 não é fechado.

A equipe deve decidir quais são as conversas relacionadas aos objetivos finais e quais objetivos são instrumentais. Depois, deve posicionar o `gco` na fala que efetivamente inicia cada conversa e o `gcc` quando aquela conversa é concluída. Não basta usar os marcadores como etiquetas de passagem entre partes do fluxo; eles precisam representar a abertura e o fechamento de uma conversa orientada a um objetivo do usuário.

### 3. Tornar o M03 compreensível como diagrama individual completo

O M03 inclui observações como “formato não aceito: como no M01” e “falha na execução: como no M01”, mas não desenha as falas, cenas de alerta e caminhos de recuperação correspondentes. A consolidação também afirma que a conferência do conjunto de teste vale para a entrada do M03 na O06.3, embora esse caminho não esteja representado.

O reuso conceitual é uma boa decisão: a mesma conversa não deve receber soluções diferentes sem justificativa. Entretanto, cada integrante precisava entregar um diagrama MoLIC que pudesse ser analisado. Uma anotação lateral não substitui a representação gráfica da ruptura. O M03 deve reutilizar os mesmos elementos gráficos do M01 e do M02 ou empregar uma referência visual formal que deixe origem, destino, falas e recuperação inequivocamente definidos.

Em especial, a entrada na comparação de desempenho precisa verificar se as configurações foram avaliadas no mesmo conjunto de teste. A hipótese de que isso sempre ocorrerá no CI03 não elimina a necessidade de modelar a condição ou a ruptura, pois a própria solução já reconhece configurações sem avaliação e conjuntos incompatíveis.

### 4. Corrigir o retorno do acesso ubíquo de explicação no M02

O acesso ubíquo para “o que é este termo?” é pertinente porque termos técnicos aparecem em mais de uma cena. Entretanto, o retorno está desenhado somente para O06.3, embora a descrição diga que a pessoa volta à cena de origem. Se o acesso pode ser acionado de qualquer ponto, o retorno fixo para uma cena específica altera o contexto da conversa.

A equipe deve representar que a explicação devolve a pessoa ao contexto de onde ela veio ou limitar explicitamente o acesso às cenas para as quais o retorno desenhado é válido. A anotação de “limitação conhecida” demonstra que vocês perceberam o problema, mas a limitação precisa ser resolvida no modelo.

### 5. Propagar os novos signos e estados para a consolidação

A seção de preparação para o protótipo ainda associa as métricas ao término do treino e não incorpora integralmente os estados “na fila”, “sem avaliação no conjunto de teste” e a origem atual do valor de referência. Como essa seção traduz as conversas em estados de interface, manter a versão anterior pode levar as próximas entregas a implementar comportamentos que o próprio projeto já revogou.

Depois de corrigir os diagramas, a equipe deve atualizar a cobertura dos objetivos, as rupturas consolidadas, a preparação para o protótipo e a rastreabilidade. A documentação textual e os SVGs precisam expressar a mesma solução.

## Recomendações de melhoria

- Diferenciem visualmente o encerramento de uma conversa concluída do encerramento temporário porque a pessoa decidiu sair enquanto uma atividade continua. Os dois casos produzem expectativas diferentes.
- Revisem a descrição “nome repetido” como recuperação apoiada. Se o processo detecta a duplicidade depois de `u: iniciar o treino`, a mensagem e a volta para nomear novamente estão adequadas; convém explicitar que a sugestão automática pode ter sido alterada pela pessoa, caso contrário a prevenção e a recuperação parecem contraditórias.
- No M01, indiquem de forma mais direta o que acontece quando Rafael escolhe “seguir sem elas”: quais entradas permanecem na sessão e qual estado de processamento será iniciado.
- No M02, mantenham explícita a origem do valor de referência e evitem que “maior valor” pareça recomendação automática. Essa distinção está bem defendida no texto e deve permanecer visível no diálogo.
- Reduzam notas explicativas externas ao diagrama quando a informação puder ser representada com a própria notação. O MoLIC deve sustentar a leitura do caminho sem depender de um texto paralelo extenso.
- Após cada mudança, executem uma revisão cruzada entre cenário de interação, Design Centrado na Comunicação, esquema de signos, MoLIC e protótipo. Neste projeto, uma pequena decisão sobre métricas altera várias conversas.

## Pontos que devem alimentar as próximas entregas

- A atividade de avaliar uma configuração no conjunto de teste deve possuir uma conversa de interação definida, pois ela separa “treinada” de “avaliada”.
- A ruptura “configuração sem avaliação no conjunto de teste” precisa chegar ao protótipo e às avaliações posteriores.
- Os estados “na fila”, “processando”, “concluído” e “falhou” devem manter os mesmos nomes nas falas, nos signos e na interface.
- A referência apresentada junto às métricas deve declarar sua origem sem sugerir que o sistema tomou a decisão pelo usuário.
- O acesso ubíquo para explicações precisa preservar o contexto de retorno em todas as telas nas quais for disponibilizado.
- A continuidade do treino depende de o programa permanecer aberto; essa restrição deve ser comunicada antes de a pessoa sair.
- As tarefas de avaliação devem exercitar as rupturas importantes por inspeção ou por teste adequado, mantendo coerência com o planejamento ético e operacional da equipe.

## Síntese das ações recomendadas

1. Separar nos MoLIC os estados de configuração treinada e configuração avaliada no conjunto de teste.
2. Atualizar M01, M02 e M03 com “na fila”, “sem métricas” para imagens de campo e “sem avaliação no conjunto de teste”.
3. Reorganizar os marcadores `gco` e `gcc`, com atenção especial ao fechamento de O01 e O02 no M03.
4. Desenhar no M03 os caminhos de ruptura hoje indicados apenas por “como no M01” e incluir a validação do conjunto de teste.
5. Corrigir o retorno do acesso ubíquo de explicação no M02.
6. Propagar as correções para a consolidação, a preparação do protótipo e a rastreabilidade.

**Parecer geral:** A Entrega 10 está completa em quantidade, possui boa apresentação gráfica e demonstra que a equipe compreendeu a MoLIC como uma conversa entre usuário e sistema, incluindo signos, objetivos, processamentos, alternativas e rupturas. Os três integrantes apresentaram contribuições individualizadas, e os diagramas constituem uma base consistente para o projeto. Para que essa base se torne conceitualmente confiável, vocês precisam corrigir o pareamento entre GCO e GCC, tornar o M03 autossuficiente e atualizar os modelos conforme as decisões mais recentes sobre avaliação no conjunto de teste, métricas e estados de processamento. Não há desconto individual por ausência de entrega e não se aplica divisão da nota, pois cada integrante apresentou seu próprio diagrama.
