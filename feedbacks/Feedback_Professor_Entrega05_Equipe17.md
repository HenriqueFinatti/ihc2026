# Feedback do Professor > Entrega 05 > Equipe 17

A equipe apresenta os nove modelos solicitados, distribuídos entre os três integrantes:

- **Henrique:** HTA e CTT de T05, com GOMS de T04.
- **Tiago:** HTA e CTT de T03, com GOMS de T01.
- **Mateus:** HTA e CTT de T07, com GOMS de T06.

A quantidade formal está atendida, e as tarefas escolhidas são relevantes para os objetivos das personas. Modelar tarefas diferentes nas três técnicas é permitido; nesse caso, é necessário explicar corretamente a correspondência entre os recortes.

O trabalho apresenta qualidade desigual. Henrique e Tiago desenvolveram HTAs estruturados e CTTs com motivação externa, tarefas de sistema e relações temporais. Os três GOMS estão em texto indentado, possuem GOAL 0, metas subordinadas e verificações ao final dos blocos de operadores. Entretanto, a seção de Mateus mantém divergências graves entre diagrama, tabela, explicação e registros de revisão. Também há ajustes conceituais nas regras de seleção e nos caminhos de exceção dos outros modelos. A entrega precisa ser consolidada antes de ser considerada concluída.

## Pontos positivos

- Os HTAs T03 e T05 possuem tarefa 0, decomposições com dois ou mais filhos, planos nos objetivos decompostos e grifo nas operações terminais. As visões gerais e expansões conservam os identificadores, permitindo reconhecer a mesma hierarquia. As setas de decomposição, nesse caso, não transformam os modelos em fluxogramas.
- Nas tabelas auxiliares desses dois HTAs, **Input, Plano e Feedback** aparecem na tarefa 0. Nas filhas, vocês utilizam ações, problemas, recomendações e planos, conforme necessário.
- Os GOMS distinguem metas de ações e apresentam alternativas reconhecíveis, como leitura por tabela ou gráfico e inspeção lado a lado ou por sobreposição. Não foram substituídos por diagramas.
- Os CTTs T03 e T05 usam abstrações nos nós decompostos e distinguem usuário, interação e sistema. A motivação de Rafael e a preparação da recomendação de Larissa aparecem antes da sessão de uso.
- A síntese da equipe produz implicações concretas, como comparar a mesma entrada, manter legenda consistente e distinguir processamento, conclusão e falha. A ressalva sobre métricas dependerem de referência anotada é pertinente.

## Correções prioritárias

### 1. Mateus: corrigir a decomposição e os planos do HTA T07

O diagrama apresentado em `assets/05_tarefas/hta-task-06.svg` possui a tarefa “Comparar métricas” decomposta somente em “Consultar métricas disponíveis”. Essa relação de pai com um único filho não atende ao formalismo solicitado. Vocês devem decidir se a tarefa já é uma operação terminal ou se existe uma decomposição real em duas ou mais subtarefas. Não acrescentem uma tarefa artificial apenas para completar a quantidade.

As folhas possuem grifo, o que deve ser preservado. O problema principal está nos planos e na correspondência com a tabela da seção 3.1:

- O plano da raiz do SVG é `1 > 2`, embora a raiz tenha também o filho 3. A comparação de métricas fica sem participação definida no plano.
- A tabela apresenta `1 > 2 > 3 > 4`, mas não define a tarefa 4.
- A tarefa 1 recebe o plano `1.1 + 1.2`, mas essas filhas não estão descritas na tabela nem na árvore apresentada.
- A tarefa 3 tem uma filha 3.1, mas não possui plano associado.
- A tabela chama a tarefa 1 de “Selecionar a entrada”, enquanto o diagrama a chama de “Segmentar imagem com mais de um modelo”. São atividades diferentes.
- A verificação afirma que não há paralelismo, embora a tabela utilize `+`. Na notação adotada, esse operador precisa ter um significado consistente.

Reconstruam uma única decomposição de T07 e façam diagrama, numeração, planos e tabela descreverem exatamente essa estrutura.

### 2. Mateus: completar o Feedback da tarefa 0 e o resultado humano da comparação

Na tabela auxiliar de T07, a tarefa 0 possui Input e Plano, mas **não apresenta Feedback**. A descrição anterior informa como término a disponibilização das segmentações para comparação. Isso encerra a preparação dos resultados, mas ainda não demonstra que Andreia comparou os modelos e chegou a uma conclusão.

Definam o estado final que permite reconhecer o cumprimento da tarefa: o que a pesquisadora consegue concluir, justificar ou reconhecer como inconclusivo depois de comparar? A tabela deve registrar esse Feedback na tarefa 0. Nas filhas, mantenham ações e recomendações, sem distribuir Input e Feedback por toda a hierarquia.

A comparação visual também precisa explicitar a relação entre resultados de modelos diferentes. Consultar original e máscara é necessário para inspecionar uma segmentação, mas não explica, sozinho, como Andreia compara duas configurações sobre a mesma entrada.

### 3. Mateus: incluir no CTT a motivação externa e o processamento do sistema

O arquivo `assets/05_tarefas/ctt_t07_comparar_modelos.svg` apresenta abstrações nos nós decompostos e relações `>>`, `|||` e `|=|`. Esses elementos estão presentes e podem ser aproveitados. Contudo, a árvore começa diretamente pela interação “Segmentar imagem com mais de um modelo”: **não há tarefa externa que motive o uso nem tarefa explicitamente classificada como processamento do sistema**.

A segmentação foi colocada inteira em uma tarefa de interação. É necessário distinguir a ação da pessoa que solicita o processamento do trabalho que o sistema realiza em seguida. Também deve aparecer a situação externa que leva Andreia a iniciar a comparação.

A explicação não corresponde ao desenho: a seção 3.3 afirma inicialmente que não existem tarefas do sistema nem ciclos, mas depois lista S1–S4, C, tarefas 1 a 4 e uma estrutura com repetição que não estão nessa figura. A seção 3.4 e a síntese retomam esses mesmos elementos ausentes da árvore apresentada.

Escolham a versão efetiva do modelo e atualizem todas as representações. Expliquem também a diferença entre concorrência e independência de ordem: `|=|` permite realizar ambas em qualquer ordem, mas exige concluir a primeira antes de começar a outra. Isso não é equivalente ao paralelismo `+` anunciado para o HTA.

### 4. Henrique: distinguir método alternativo de recuperação após outro método

O GOMS de T04 possui a estrutura textual exigida e alternativas adequadas na leitura por tabela ou gráfico. A dificuldade está na meta 3: o método 3.C só pode ocorrer depois de 3.B, quando a explicação não resolve a dúvida. O próprio texto afirma que ele nunca é escolhido no lugar de 3.B.

Nesse formato, 3.C representa uma continuação condicional do caminho de consulta, e não uma alternativa independente equivalente às demais. Organizem o atendimento da meta de forma que o leitor enxergue o método completo e, dentro dele, o tratamento da dúvida persistente. A regra de seleção deve explicar quando escolher um caminho capaz de alcançar a meta.

Revisem também o plano 2.3 do HTA, que apresenta as três opções com `/`, apesar da dependência entre consultar a explicação e pedir ajuda. O CTT já expressa o recurso ao colega como suspensão, mas a retomada precisa deixar claro quando a informação recebida basta e quando é necessário conferir novamente os resultados.

### 5. Tiago: compatibilizar os métodos de julgamento com o resultado inconclusivo

O GOMS de T01 está organizado e termina os blocos com verificações. Porém, o método 3.A pode ser selecionado quando a imagem não possui anotação de referência e manda “decidir se o resultado é adequado ou inadequado”. O texto explicativo e o encerramento geral admitem também um resultado inconclusivo.

Quando a inspeção não permite decidir e não há anotação, o método precisa conseguir terminar legitimamente como inconclusivo. Também não deve obrigar Rafael a determinar a origem do erro quando a evidência visual não permite distinguir problema do modelo de problema da captura. Ajustem os operadores e o critério de verificação para preservar essa incerteza.

A regra de 3.B depende de uma inspeção visual anterior. Deixem explícito, na organização da meta, quais ações são comuns e em que condição ocorre a consulta adicional às métricas. Evitem apresentar uma sequência obrigatória como se fossem caminhos inteiramente independentes.

### 6. Alinhar as relações do CTT aos percursos que o texto permite

Nos modelos T03 e T05, as relações temporais estão efetivamente desenhadas, e há tarefas de sistema. O ajuste necessário é fazer a árvore expressar com precisão os percursos descritos.

No CTT de T03, a relação `C = 2 []>> 3` habilita a avaliação após obter o resultado, mas as notas também permitem retirar uma configuração após falha e encerrar C sem avaliação. Explicitem a condição de sucesso e o caminho de retirada na estrutura e na legenda, para que a sequência não pareça obrigar a avaliação de um resultado inexistente.

Os textos dos GOMS permitem repetir a meta de visualização para alternar entre lado a lado e sobreposição, ou entre tabela e gráfico. Nos CTTs correspondentes, a escolha `[]` desabilita a outra alternativa naquela ocorrência. Se a pessoa pode voltar e consultar a outra visão na mesma análise, representem ou delimitem essa repetição. A árvore deve distinguir uma escolha única de uma escolha que pode ser feita novamente.

Em T03, “Registrar a conclusão” termina em folhas classificadas como tarefa de usuário, apesar de o projeto prever registro na interface. Separem o julgamento mental da ação de inserir ou confirmar a conclusão. Essa distinção evita esconder a interação sob um rótulo genérico.

### 7. Consolidar os arquivos e corrigir os registros de conclusão

`PENDENCIAS.md` marca INC-53, INC-54 e INC-55 como resolvidos e afirma que o HTA e o CTT de T07 foram refeitos e incorporados. Existem scripts com novas estruturas em `scripts/diagramas/hta_t07.py` e `ctt_t07.py`, mas o documento continua apontando para o HTA antigo, o CTT apresentado mantém a estrutura anterior e a tabela continua divergente. O registro de resolução ainda não corresponde aos artefatos apresentados.

A linha R04 de `RASTREABILIDADE.md` também remete a HTA, GOMS e CTT de T08 na seção 3.6, mas essa seção não está no documento. A própria Entrega 05 afirma que T08 ainda não foi modelada. Como o requisito mínimo é um modelo de cada técnica por integrante, não estou exigindo um segundo conjunto para Mateus; é necessário, porém, corrigir a afirmação de conclusão ou incorporar os artefatos correspondentes de forma consistente.

Revisem ainda afirmações remanescentes, como a de que as classes não estão definidas no item 3.2 do HTA T03, enquanto a premissa 5 já estabelece “Trilha” e “Fora da trilha”. O status e o checklist devem refletir o conteúdo efetivamente disponível, não apenas a intenção de revisão.

## Recomendações de melhoria

- Preservem as visões gerais e os detalhamentos de T03 e T05: os IDs permitem acompanhar a decomposição sem exigir a leitura de uma imagem enorme de uma só vez.
- Nos operadores de GOMS, indiquem o objeto concreto de ações como abrir, selecionar e registrar. Operadores perceptivos e cognitivos são pertinentes, mas não devem ocultar conjuntos de ações que precisam ser decompostos.
- Em T06, esclareçam o critério de conclusão de cada método de visualização e a necessidade de retornar à meta 2. As três vistas são alternativas para uma consulta, mas podem ser complementares para concluir a análise completa.
- Diferenciem o registro temporário da conclusão na sessão de um histórico persistente. Isso ajuda a manter coerência com o escopo sem retirar uma ação necessária à tarefa.

## Pontos que devem alimentar as próximas entregas

Os requisitos RQ01–RQ09 constituem uma boa base para prototipação e avaliação, desde que sejam associados aos modelos corrigidos. Priorizem a compreensão dos estados de execução, a comparação da mesma entrada e a possibilidade de declarar uma conclusão inconclusiva.

A ampliação do escopo para configuração e treinamento foi registrada nesta versão; ela não deve ser tratada como proibida por decisões antigas já revogadas. Entretanto, seus efeitos sobre tarefas e modelos precisam ser consolidados antes de apresentar T08 como concluída.

Investiguem com os perfis correspondentes os critérios de comparação e relevância das diferenças, a necessidade de alternar visualizações e as situações em que se recorre a colegas. A interpretação e a escolha devem permanecer com a pessoa, sem atribuir ao sistema decisões que ele apenas apoia.

## Síntese das ações recomendadas

1. Unificar diagrama, tabela e planos do HTA T07, eliminando o filho único e completando o Feedback da tarefa 0.
2. Corrigir o CTT T07, incluindo motivação externa, processamento do sistema e explicação compatível com a figura.
3. Reorganizar os métodos que são continuações condicionais e assegurar o término inconclusivo no GOMS de T01.
4. Compatibilizar escolhas, repetições, falhas e registro da conclusão nos CTTs.
5. Atualizar os arquivos apresentados, as pendências e a rastreabilidade antes de marcar a entrega como concluída.

**Parecer geral:** vocês escolheram tarefas pertinentes e demonstram avanço na modelagem da interação, especialmente nas estruturas de Henrique e Tiago e na organização textual dos três GOMS. A quantidade foi atendida, mas a entrega ainda não apresenta consistência suficiente entre todas as contribuições. A prioridade é corrigir os problemas formais de T07 e consolidar as versões, além de ajustar os caminhos condicionais e a representação da incerteza. Com essas revisões, os modelos poderão orientar o projeto de interface com maior precisão e confiabilidade.

---

## Tratamento dos comentários

*Registro da equipe, 15/11/2026. Cada item foi conferido contra o estado atual de `docs/05_analise_tarefas.md`, dos scripts em `scripts/diagramas/` e dos SVGs em `assets/05_tarefas/` antes de qualquer alteração. Os diagramas do Mateus já tinham sido refeitos em 14/11/2026, depois do envio deste parecer.*

| Item do parecer | Situação em 15/11/2026 | O que foi feito |
|---|---|---|
| 1. HTA T07: decomposição e planos | Já atendido em 14/11 (HTA refeito por script, sem nó de filho único; diagrama, numeração, planos e tabela iguais; sem `+`) | Novo objetivo 2.3 (desfecho da execução: `2.3.1 / 2.3.2`) e plano 4 como `4.1 > [4.2]`, para que o diagrama mostre a falha e o passo opcional que a tabela já descrevia. |
| 2. HTA T07: Feedback e resultado humano | Parcialmente atendido em 14/11 (Feedback na tarefa 0; comparação na mesma região em 3.2) | A conclusão passa a admitir "inconclusiva" no Resultado, no Feedback da tarefa 0, em 5.1 e em 5.2; 5.2 guarda a conclusão na sessão (histórico depende da H08). |
| 3. CTT T07: motivação externa e sistema | Já atendido em 14/11 (motivação `T07 = M []>> U`, S1–S4, texto compatível com a figura; `\|=\|` e `+` não são mais usados) | Desfecho `2.3 = 2.3.1 [] 2.3.2` no ramo 2 e `[4.2]` no desenho; legenda e tabelas revistas. |
| 4. Henrique: método alternativo × continuação | Não atendido | HTA T05: plano 2.3 como `2.3.1 / (2.3.2 > [2.3.3])`. GOMS T04: o antigo método 3.C virou a submeta condicional 3.B.5, dentro do 3.B; a regra de seleção escolhe entre 3.A e 3.B no início. CTT T05: a retomada depois de E diz quando a resposta basta (volta a 2.3.2.2) e quando é preciso conferir os resultados de novo (volta a 2.1). |
| 5. Tiago: término inconclusivo no GOMS T01 | Não atendido | Meta 3 em caminho único: inspeção visual comum (OP. 3.1–3.3) que pode terminar inconclusiva, consulta às métricas como submeta condicional 3.4 (só com anotação de referência) e origem do erro apontada só quando a evidência permite (OP. 3.5). HTA T03: plano 3.3 como `3.3.1 > [3.3.2]`. A citação da E9 ao GOMS da T01 foi atualizada. |
| 6. CTTs: escolhas, repetições, falhas e registro | Não atendido | T03: avaliação só no ramo de sucesso (`2.3 = D [] 2.3.2`, `D = 2.3.1 []>> 3`), retirada encerra C; `3.1* = (3.1.1 [] 3.1.2)*`; `[3.3.2]`; registro separado em julgamento (J), interação (4.2.4) e sistema (S5, conclusão guardada na sessão). T05: `2.2* = (2.2.1 [] 2.2.2)*`. T07: desfecho da execução (item 3). |
| 7. Consolidação e registros | Parcialmente atendido em 14/11 (a seção 3.6 com a T08 existe; INC-53 a 55 correspondem aos artefatos atuais) | Item 3.2 do HTA T03 cita *Trilha* e *Fora da trilha*; entradas T01–T08 e R01–R04; ordem das premissas; status "revisada após feedback"; checklist com dois itens novos; resolução de INC-53 a 55 complementada em `PENDENCIAS.md`. O arquivo antigo `hta-task-06.svg` não é citado por nenhum documento. |
| Recomendações | Atendido | Visões gerais e detalhamentos de T03 e T05 preservados e regenerados; critério de conclusão e retorno à meta 2 no GOMS da T06; registro na sessão diferenciado do histórico persistente (T03 4.2 e T07 5.2); requisitos RQ05 e RQ06 associados aos modelos corrigidos. |
