## Avaliação geral

A equipe apresenta uma aproximação inicial pertinente entre a contribuição do TCC e uma situação de uso por integrantes do Baja FEI. O fluxo de selecionar um arquivo, acompanhar a segmentação e interpretar o resultado é uma base plausível para o projeto de IHC. Entretanto, o entendimento ainda oscila entre desenvolver a tecnologia, operar essa tecnologia e apoiar uma decisão humana. Essa oscilação aparece nos objetivos, no perfil de usuário e, principalmente, no recorte: algumas respostas propõem analisar imagens com modelos prontos; outras incluem treinamento, configuração de datasets e inclusão de modelos.

A entrega precisa de revisão antes de ser considerada consolidada. As prioridades são definir o resultado que o usuário pretende alcançar, harmonizar o escopo e corrigir a classificação das afirmações e a rastreabilidade. Há também campos obrigatórios ainda sem resposta. Não se exige que vocês já tenham entrevistas, personas, modelos de tarefas ou protótipos concluídos: nesta etapa, o essencial é apresentar um recorte coerente e distinguir o que já foi definido, o que é hipótese e o que permanece desconhecido.


## Pontos positivos

- **Ligação explícita com o TCC e com um público identificado.** Vocês relacionam a segmentação de vias off-road ao projeto Baja FEI, evitando uma aplicação sem conexão com o trabalho de origem.
- **Contribuição descrita sem começar pela implementação.** As seções 1.1 e 1.3 destacam segmentação, comparação de modelos e análise de resultados antes de apresentar tecnologias.
- **Problema de interação plausível.** As seções 4.1 e 4.2 levantam a dificuldade de executar scripts e configurar parâmetros por pessoas que não dominam o código, identificando uma questão investigável de IHC.
- **Reconhecimento dos limites das evidências.** A seção 4.6 registra que os scripts não demonstram diretamente dificuldades dos usuários e que a observação da própria equipe possui alcance limitado. Essa cautela deve ser preservada e aplicada ao restante do documento.
- **Fluxo inicial compreensível.** O Caminho A e as ações F01–F04 articulam entrada, execução e interpretação dos resultados. A comparação entre imagem original e segmentação tem uma justificativa inicial ligada à compreensão da saída.
- **Consideração de rupturas e restrições.** Vocês mencionam arquivos inválidos, demora, interrupção e classificação incorreta, além de relacionar o tempo de processamento à necessidade de informar o estado da execução.

## Correções prioritárias

### 1. Definir o objetivo humano além de “segmentar os caminhos”

**Natureza: problema conceitual de IHC. Seções relacionadas: 1.4, 3.1, 7.3, 7.4, 9.2 e 11.**

Na seção 3.1, o objetivo é “visualizar a via segmentada” para futuramente desenvolver carros autônomos. Na seção 7.3, é “Segmentar a trilha das corridas”. Essas formulações dizem o que a tecnologia entrega, mas ainda não esclarecem suficientemente o que a pessoa precisa concluir ou decidir a partir disso. Desenvolver um carro autônomo, por sua vez, é um objetivo amplo do projeto, que não delimita uma situação de interação.

Conforme a distinção trabalhada no capítulo 8, o objetivo expressa uma condição que a pessoa deseja alcançar; a tarefa é um meio para chegar a ela. Perguntem: **depois de visualizar a segmentação, o integrante precisa decidir o quê?** Identificar falhas de classificação, avaliar a adequação de um modelo e interpretar o terreno são possibilidades diferentes, que precisam ser escolhidas e justificadas pela equipe.

Revisem o objetivo prioritário e o benefício esperado de forma consistente entre essas seções. Isso evitará que o projeto avance para telas que exibem resultados sem esclarecer qual atividade humana será apoiada. A interface não termina sua missão quando a imagem fica colorida: alguém ainda precisa entender o que fazer com ela.

### 2. Consolidar o recorte e completar a delimitação exigida

**Natureza: conformidade com a entrega e coerência conceitual. Seções relacionadas: 0.4, 0.5, 7.1, 8, 9 e 11.**

O Caminho A apresenta envio, processamento e visualização de arquivos. Já a seção 8 inclui envio de vídeos para treinamento, acompanhamento do treinamento e configuração de datasets. No Caminho B aparece a possibilidade de inserir novos modelos, enquanto a seção 9.2 se concentra em executar a segmentação. Essas atividades envolvem conhecimentos e decisões distintos e não podem aparecer como se fossem um único fluxo já definido.

A equipe precisa decidir se o recorte inclui apenas o uso de modelos disponíveis ou também seu treinamento e configuração. Não há obrigação de adotar todas essas possibilidades. Registrem o que está dentro e fora do escopo de IHC e o que pertence ao compromisso formal do TCC: os três campos de delimitação da seção 11 permanecem com `{{...}}`. Também faltam a descrição da seção 0.4 e a explicação do que está formalmente previsto na seção 0.5.

Como vocês declararam que o TCC já previa interface, o Caminho A é o caminho aplicável. As reflexões adicionais do Caminho B podem ser aproveitadas, mas precisam ser apresentadas como complemento coerente, sem introduzir compromissos conflitantes.

Há ainda uma inconsistência interna que afeta as opções oferecidas ao usuário: a seção 9.3 descreve ResNet152 como backbone do DeepLabv3+, enquanto 7.1 e 11 mencionam dois modelos. Esclareçam quais alternativas realmente serão selecionadas ou comparadas. O ponto não é julgar a arquitetura do TCC, mas evitar que a interface apresente componentes e modelos como escolhas equivalentes sem uma definição clara.

### 3. Especificar o perfil prioritário dentro da equipe Baja FEI

**Natureza: problema conceitual de IHC. Seções relacionadas: 2.1–2.4, 5.4 e 7.2.**

“Integrantes da equipe Baja FEI” identifica um grupo real de interesse, mas ainda reúne pessoas potencialmente diferentes. O documento ora considera alguém com pouco conhecimento do código, ora alguém capaz de configurar modelos. Na seção 2.4, vocês apenas enumeram frequência, responsabilidade e familiaridade com métricas, sem explicar quais características estão sendo inicialmente atribuídas ao perfil escolhido.

Definam provisoriamente qual papel dentro da equipe realizará a atividade central, que conhecimento se presume necessário e que resultado essa pessoa deverá interpretar. O aprofundamento pertence às próximas entregas; agora é suficiente uma caracterização inicial, marcada como hipótese quando ainda não investigada.

Revisem também os stakeholders. Mecânicos e pilotos aparecem como não usuários, mas as descrições dizem que utilizarão segmentações ou métricas. Expliquem se receberiam informações por intermédio de outra pessoa ou se interagiriam com a interface. “Empresas do agro” descreve uma organização potencialmente beneficiária, não um perfil de interação específico, e sua participação está marcada como fato sem origem indicada. Essa expansão pode permanecer como possibilidade, sem competir com o público prioritário.

### 4. Separar atividades humanas, processamento e criticidade de uso

**Natureza: problema conceitual de IHC. Seções relacionadas: 3.2–3.4 e 4.3–4.5.**

Na tabela 3.2, A02 é “Processamento de imagem ou vídeo”, realizado pelo sistema. Esse passo pode ser descrito como parte do funcionamento, mas não substitui a atividade humana que o inicia, acompanha ou interpreta. Na seção 3.4, a criticidade é atribuída principalmente ao processamento incorreto, deslocando a análise para o desempenho do modelo.

Revisem quais ações e interpretações da pessoa merecem atenção: o que ela escolhe, o que precisa compreender e como percebe que algo falhou. Distingam falha técnica, dificuldade de interação e interpretação inadequada do resultado. Essa separação será necessária para que a futura avaliação de IHC examine o uso da interface, sem tentar substituir a avaliação científica da segmentação.

A seção 3.3 afirma como fato que as atividades têm a mesma frequência porque ocorrem em sequência. Essa sequência não comprova a frequência real: ainda é preciso investigar repetições, novas análises e outras variações do uso. Registrem a frequência como hipótese ou lacuna quando não houver conhecimento suficiente. Não é necessário produzir medições nesta entrega.

### 5. Revisar fatos, hipóteses e alcance das evidências

**Natureza: conformidade com a classificação exigida e coerência do conhecimento registrado. Seções relacionadas: 2, 4, 6, 8, 9 e 11.**

A equipe utiliza as marcações, mas nem sempre mantém o mesmo estatuto para a mesma informação. O processo por scripts aparece como hipótese em 4.1, como evidência existente em 4.6 e como fato em 6.1 e 9.1. A seção 2.1 está marcada como fato, mas é listada entre as hipóteses na síntese. Na seção 8, todas as possibilidades recebem “F”, inclusive afirmações como “O sistema é simples de usar” e ausência de necessidade de determinados recursos.

Vocês podem registrar como fatos as decisões já definidas no TCC, sem precisar apresentar provas externas para cada uma. Contudo, uma decisão de projeto não comprova facilidade de uso, necessidade do público ou benefício alcançado. Na primeira linha de 9.1, por exemplo, o processo atual pode ser conhecido, enquanto a facilitação prometida pela interface continua sendo um benefício esperado.

A narrativa de 4.5 é útil, mas está marcada como fato e não identifica a origem daquele episódio específico. Se ocorreu, indiquem sucintamente a observação que o sustenta; se foi construído para ilustrar o problema, classifiquem-no como situação hipotética. As evidências gerais de 4.6 não demonstram, por si, toda a sequência narrada.

No levantamento de alternativas, indiquem a origem das funcionalidades atribuídas às ferramentas ou assumam seu caráter preliminar. Não se cobra a análise aprofundada da Entrega 02 agora. O objetivo desta revisão é impedir que suposições sejam herdadas pelas próximas etapas como conhecimento confirmado.

### 6. Delimitar o contexto de uso e o significado dos resultados

**Natureza: problema conceitual de IHC. Seções relacionadas: 4.3–4.5, 5, 7.1, 9.2 e 11.**

O texto alterna laboratórios, pista de testes, corridas e apoio a decisões sobre percurso. A síntese registra “Carros e robôs autônomos off-road” como contexto, mas isso informa o domínio de aplicação, sem esclarecer a situação em que uma pessoa utiliza a interface.

Escolham um contexto prioritário: quando ocorre a análise, onde está o usuário, em qual equipamento e com qual responsabilidade? A análise de registros após um teste e a consulta durante a operação exigem decisões de interação diferentes. Não presumam uso operacional em tempo real se esse compromisso não estiver definido.

A seção 5.3 trata da iluminação necessária à captura de imagens. Acrescentem a perspectiva de quem utiliza a interface, identificando condições relevantes a investigar, como visibilidade da tela ou interrupções, sem afirmar que elas já foram observadas.

Também é necessário esclarecer o que o usuário pode concluir das classes e métricas mostradas. O documento aproxima segmentação, transitabilidade e segurança do percurso sem delimitar essa passagem. Não está demonstrado, nas fontes apresentadas pela equipe, que um resultado de segmentação ou uma métrica autorize concluir que um trajeto é seguro. Registrem os limites do uso pretendido e investiguem como comunicá-los. Na ação F04, expliquem quais informações sustentariam a interpretação do desempenho, sem tratar a simples exibição de números como compreensão ou confiança já alcançadas.

### 7. Harmonizar as possibilidades de interação com as necessidades levantadas

**Natureza: coerência conceitual. Seções relacionadas: 5.5, 7.1, 8 e 9.**

Na seção 5.5, manter histórico aparece como hipótese relevante para comparar registros e acompanhar a evolução. Na seção 8, “Histórico com busca/filtros” é descartado porque não haveria necessidade de busca. Histórico e busca não são a mesma decisão: esclareçam quais partes estão sendo consideradas e o que permanece em investigação.

A comparação de resultados também é descartada com a justificativa de que seria realizada pelo usuário. Justamente por ser uma atividade humana, ela pode exigir apoio da interface. Distingam a comparação entre imagem original e segmentada da comparação entre modelos, e esclareçam qual delas pertence ao recorte. Isso não exige criar uma tela nova nem automatizar a decisão.

Selecionar um modelo para uma execução não implica necessariamente administração ou configuração global. Do mesmo modo, não adotar uma central de alertas não elimina a necessidade de comunicar falhas relevantes ao fluxo. Revisem as justificativas da tabela pelo objetivo de uso, sem transformar os nomes dos padrões em uma lista automática de funcionalidades.

### 8. Tornar a rastreabilidade utilizável e concluir os campos pendentes

**Natureza: conformidade com a Entrega 01. Seções relacionadas: 10, 11, 13, checklist e matriz de rastreabilidade.**

As hipóteses foram parcialmente transferidas para a matriz; portanto, não se trata de ausência completa de registro. Porém, o ID H10 aparece duas vezes, e uma das formulações se repete em H11. Há ainda linhas com conteúdo deslocado em relação às oito colunas da matriz: justificativas aparecem no campo de tipo, etapas no campo de importância e estados continuam como opções do template. Assim, o registro ainda não permite acompanhar adequadamente a evolução do conhecimento.

Corrijam a estrutura das tabelas, atribuam IDs únicos e mantenham os mesmos identificadores nos dois arquivos. Perguntas podem permanecer como lacunas `[?]`; hipóteses `[H]` devem expressar uma suposição compreensível. Não basta copiar o enunciado quando o documento já apresenta uma hipótese mais específica. A seção 1 da matriz, dedicada à derivação do escopo, também permanece sem preenchimento e deve registrar as decisões iniciais da equipe.

A hipótese H12 remete o benefício à Entrega 13, mas a própria seção 9.1 já apresenta benefícios esperados. Registrem essa expectativa agora e planejem sua investigação ao longo do projeto. A avaliação heurística posterior não substitui o entendimento inicial das necessidades do público.

Completem as três frases da seção 13 sobre problema humano, contribuição técnica e forma de uso. Atualizem o checklist conforme o conteúdo efetivo: a delimitação ainda vazia e a confusão entre objetivo e funcionalidade não sustentam todos os itens marcados como atendidos. Nas partes da matriz referentes a personas, modelos, protótipos e avaliações futuras, indiquem pendências quando pertinente; não é necessário produzir esses artefatos nesta entrega.

## Recomendações de melhoria

- **Aprimorar a apresentação das evidências existentes.** Em 4.6, um registro breve do contexto da observação e do que foi efetivamente observado ajudaria a delimitar seu alcance. Não é necessário transformar essa seção em um relatório de pesquisa completo.
- **Separar conhecimento de programação e conhecimento de segmentação.** Uma pessoa pode compreender o terreno sem dominar scripts, ou executar código sem interpretar adequadamente os resultados. Essa distinção ajudará a investigar o perfil prioritário.
- **Dar precisão ao vocabulário.** Utilizem de maneira consistente “modelo”, “treinamento”, “execução da segmentação”, “classe” e “métrica”. A terminologia precisa corresponder às atividades previstas, antes de ser levada às telas.
- **Revisar a apresentação em Markdown.** A tabela de 1.5 está sem linha separadora do cabeçalho; a linha H02 da seção 10 contém conteúdo excedente; há marcações residuais e pequenos erros de escrita. Corrijam esses pontos após resolver as questões conceituais. A coluna adicional de responsabilidades pode ser preenchida ou removida: ela não é uma exigência do modelo oficial consultado.

## Pontos que devem alimentar as próximas entregas

Os encaminhamentos abaixo são investigações futuras, e não exigências de resultados antecipados para concluir a Entrega 01.

| Etapa | Questões a retomar |
|---|---|
| Entrega 02 - alternativas | Comparar o apoio oferecido ao fluxo escolhido, distinguindo anotação, treinamento e análise de resultados. Investigar a hipótese de complexidade excessiva das ferramentas citadas. |
| Entrega 03 - perfis e contexto | Refinar o papel prioritário no Baja FEI, seus conhecimentos e o ambiente efetivo de uso. Retomar H02–H04 e as dúvidas sobre interfaces conhecidas. |
| Entrega 04 - situações problemáticas | Aprofundar a narrativa de 4.5, mantendo explícita sua origem observada ou hipotética, e distinguir dificuldade com código de dificuldade para interpretar resultados. |
| Entrega 05 - tarefas | Modelar as ações e decisões humanas do recorte consolidado, deixando claro o papel do processamento automático. |
| Entrega 07 - coleta de dados | Investigar as hipóteses prioritárias sobre dificuldades, práticas atuais, familiaridade, colaboração e eventual necessidade de histórico, preservando seus IDs. |
| Entrega 08 - usabilidade | Derivar metas de uso do problema humano identificado. Não utilizar desempenho do modelo como substituto de qualidade da interação. |
| Entregas 09–14 - modelos, protótipos e avaliação | Verificar se a interface ajuda a compreender resultados, reconhecer limitações e lidar com falhas, mantendo rastreabilidade com necessidades e evidências anteriores. |

## Síntese das ações recomendadas

1. Definir o papel prioritário no Baja FEI e o resultado humano que a interface deverá apoiar.
2. Escolher um recorte coerente, harmonizando execução, treinamento, comparação de modelos e contexto de uso.
3. Completar a descrição do TCC e a delimitação, distinguindo atividades humanas, operações do sistema e limites dos resultados.
4. Revisar as marcações `[F]`, `[H]` e `[?]`, incluindo a origem da narrativa e o caráter esperado dos benefícios.
5. Corrigir IDs e colunas da rastreabilidade, preencher sua derivação inicial e alinhar as possibilidades de interface às necessidades levantadas.
6. Concluir a síntese para comunicação do projeto e atualizar o checklist após a revisão.

**Parecer geral:** a Entrega 01 apresenta uma base pertinente para um projeto de IHC ligado ao Baja FEI, especialmente ao reconhecer dificuldades no uso de scripts e propor um fluxo inicial de interpretação de segmentações. Entretanto, ainda não demonstra um entendimento suficientemente consolidado de usuário, objetivo, contexto e escopo, e mantém lacunas de preenchimento e inconsistências na rastreabilidade. Considero a entrega parcialmente atendida, com necessidade de revisão dos pontos prioritários antes de utilizá-la como referência estável para as próximas atividades. O avanço esperado é transformar o foco atual em executar e visualizar a segmentação em uma justificativa clara de como uma pessoa utilizará esses resultados para alcançar um objetivo definido, mantendo transparentes as hipóteses e os limites do conhecimento disponível.

---

## Tratamento dos comentários

*Registro da equipe, 10/11/2026. Cada item foi conferido contra o estado atual de `docs/01_conhecendo_o_problema.md` antes de qualquer alteração, já que boa parte foi resolvida nas revisões de 26/09, 28/09 e 08/11/2026.*

| Item do parecer | Situação em 10/11/2026 | O que foi feito |
|---|---|---|
| 1. Objetivo humano | Parcialmente atendido em 26/09 | Objetivo unificado em §1.4, §2.2, §2.4, §3.1, §7.2–§7.4, §9.1, §9.2, §11 e §13: selecionar a **configuração** a usar nos testes do veículo, com base nas métricas do conjunto de teste anotado e na inspeção visual. Saiu "mais adequado às condições do terreno", que afirmava mais do que as métricas permitem. |
| 2. Recorte e delimitação | Já atendido (26/09 e 08/11) | Nenhuma alteração. §0.4, §0.5 e §11 preenchidas, Caminho B removido e ResNet152 descrito como backbone dos dois modelos. |
| 3. Perfil prioritário | Parcialmente atendido | Configurar e treinar atribuídos ao pesquisador de modelos (§7.1, AC06), e não ao analista prioritário, que pode não dominar código. §5.4 descreve os papéis de analista, pesquisador e gestor, ligada à H07. Os stakeholders já tinham sido corrigidos. |
| 4. Atividades humanas × processamento | Parcialmente atendido | Criada a A05 (treino) na §3.2 e preenchida a criticidade de cada atividade. A02, §3.3 e §3.4 já estavam corrigidas. |
| 5. Fatos, hipóteses e evidências | Parcialmente atendido | §6.1 e §6.2 passam a citar a Entrega 2 como origem dos [F]. Saiu a afirmação não verificada sobre polígonos no CVAT. §4.6 registra que data e detalhes da observação não foram anotados [?]. §4.1, §4.5, §8 e §9.1 já estavam corrigidas. |
| 6. Contexto e significado dos resultados | Parcialmente atendido | Contexto prioritário definido como análise no laboratório da FEI depois dos testes de campo; uso na pista vira lacuna e tempo real continua fora (§5.1, §7.4, §11 e RAST §1). AC04 explica o que as métricas indicam e não indicam. Os limites sobre segurança do trajeto e a §5.3 já estavam corrigidos. |
| 7. Possibilidades × necessidades | Parcialmente atendido | §8 separa a comparação original × segmentação (AC03) da comparação entre configurações (AC05). Alertas e logs passam a depender do acompanhamento (F03) para comunicar falhas do fluxo. "Usuários/perfis" passa a citar a H07. A tensão entre histórico e busca já estava resolvida (H08). |
| 8. Rastreabilidade e campos pendentes | Já atendido (26/09 e 08/11) | Nenhuma alteração estrutural. IDs únicos, colunas alinhadas, RAST §1 e §13 preenchidas. A RAST §1 recebeu só o novo contexto, o objetivo e o responsável pelo treino. |
| Recomendações | Parcialmente atendido | §2.4 separa conhecimento de programação e de segmentação. Coluna de responsabilidades da §0.1 removida, `{{...}}` residuais retirados, "VS Code" e pontuação corrigidos. A tabela da §1.5 e a linha H02 já estavam corretas. |
