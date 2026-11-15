# Feedback do Professor > Entrega 06 > Grupo 17

**Projeto:** Segmentação Semântica em Vias Off-Road  
**Entrega:** Prototipação em papel  
**Versão examinada:** projeto disponibilizado em 15/11/2026.

## Avaliação geral

A equipe apresenta três telas fotografadas e identificadas como P01, P02 e P03: entrada/configuração, resultado da segmentação e comparação de modelos. As imagens estão acessíveis em `assets/06_prototipos/` e permitem analisar a proposta. Portanto, o requisito fundamental de apresentar telas está atendido.

Todas as seções principais do modelo possuem conteúdo, mas algumas estão apenas parcialmente desenvolvidas. O escopo e os fluxos estão definidos; a documentação apresenta o caminho principal entre as telas. Já os estados de erro e retorno, a descrição da simulação e a demonstração das alterações precisam ser completados. A entrega é integrada, e não há necessidade de produzir um protótipo separado por integrante.

O trabalho oferece uma base pertinente para discutir a interação. Entretanto, ainda não demonstra de maneira suficientemente clara o ciclo completo de construir, simular, observar e revisar. As duas observações registradas são úteis, mas o relato da atividade é insuficiente e as mudanças aparecem como intenções futuras.

## Pontos positivos

- As três telas são desenhos em papel, adequados à exploração em baixa fidelidade. A avaliação não depende de acabamento gráfico ou de uma aplicação funcional.
- P01 oferece seleção de arquivo, escolha do modelo e comando para iniciar a segmentação. P02 reúne original, resultado e indicadores. P03 apresenta comparação entre dois modelos com tabela e gráficos.
- O fluxo P01 → P02 → P03 informa os comandos que permitem avançar: “Executar Segmentação” e “Comparar Modelo”. A numeração aparece nas próprias imagens.
- As observações sobre os rótulos “Modelo A/B” e sobre a seleção de mais de um modelo são específicas e encontram correspondência nas telas apresentadas.
- A seção 5 relaciona cada observação a uma decisão de revisão. A seleção múltipla também foi incorporada ao nome de T02 e à rastreabilidade F01.
- O histórico reconhece que as classes ilustradas e a apresentação de métricas precisam ser alinhadas ao domínio real. Registrar essa diferença é melhor do que apresentar o desenho antigo como se já estivesse atualizado.

## Correções prioritárias

### 1. Explicar como a simulação foi realizada

O item 4 mantém a instrução do modelo e apresenta duas falas, mas não descreve a sessão. Não é possível confirmar, pelo registro, se a pessoa participou da elaboração das telas, qual tarefa recebeu, como percorreu o protótipo e em que momento surgiram as dificuldades.

Em `PENDENCIAS.md`, INC-59, vocês afirmam que a Entrega 06 foi validada com o professor. Essa informação precisa ser integrada ao relato: esclareçam se essa validação corresponde ao walkthrough do item 4 ou se foi outra atividade. A afirmação de validação, isoladamente, não substitui a descrição do procedimento.

Acrescentem um relato breve com o perfil e o papel da pessoa, sem necessidade de divulgar dados pessoais; indiquem se ela não participou da elaboração das telas, a tarefa proposta, a sequência percorrida e as intervenções necessárias. Diferenciem uma dificuldade observada durante a execução de uma preferência expressa ao comentar a tela.

A coluna “Evidência” atualmente descreve características do desenho — por exemplo, o uso de Modelo A/B —, mas pouco informa sobre o comportamento da pessoa. Relatem o que ela fez, perguntou ou interpretou. Não é obrigatório produzir vídeo: um registro textual preciso da sessão é suficiente para tornar a observação compreensível e verificável.

### 2. Demonstrar a revisão, preservando a versão inicial

Na seção 5, “Trocaremos” e “Iremos incluir” indicam decisões futuras. As imagens continuam mostrando seleção de um único modelo e rótulos A/B. O histórico confirma que os rascunhos não foram alterados.

Preservar o protótipo inicial é adequado para mostrar a evolução, mas vocês precisam distinguir claramente **versão simulada**, **alterações decididas** e **alterações aplicadas**. Incluam uma revisão simples ou anotações visuais que demonstrem como as mudanças se traduzem em interação. Não é necessário apagar os desenhos originais nem antecipar o acabamento da Entrega 11.

A seleção múltipla exige uma decisão adicional: selecionar vários modelos em um único pedido não significa necessariamente processá-los simultaneamente. Expliquem se haverá fila ou execução paralela, como a pessoa acompanha cada modelo e como reconhece uma falha parcial. A melhoria precisa responder à dificuldade relatada sem prometer um comportamento que não foi definido.

### 3. Completar estados e caminhos de retorno

O item 3 mostra o caminho de sucesso, mas não representa o que acontece durante o processamento, diante de arquivo inválido ou quando uma execução falha. Também não explica como retornar para corrigir a entrada, escolher outra configuração ou reiniciar a análise.

Esses estados são relevantes para T02 e para as situações de falha descritas na análise de tarefas. A mensagem de processamento concluído em P02 não substitui um estado de espera ou de erro.

Representem, em baixa fidelidade, os estados necessários aos fluxos escolhidos e seus controles de recuperação. Identifiquem também o efeito de “Atualizar” em P03: atualizar a visualização de resultados existentes ou solicitar novas execuções são ações diferentes. O leitor deve conseguir acompanhar o percurso sem precisar adivinhar o comportamento dos controles.

### 4. Alinhar as informações das telas ao recorte atual

O histórico reconhece que P02 e P03 apresentam “Transitável”, “Vegetação” e “Céu”, enquanto o projeto passou a definir “Trilha” e “Fora da trilha”. Também reconhece que IoU e acurácia dependem de anotação de referência. Essa ressalva deve orientar a versão revisada e a interpretação do protótipo inicial.

P01 oferece “Calcular métricas” para um arquivo enviado, sem esclarecer a condição necessária. P02 apresenta IoU e acurácia como resultados disponíveis. Mostrem a diferença entre uma entrada para a qual existem métricas válidas e uma imagem de campo cuja avaliação deve ser visual. Números ilustrativos são aceitáveis, mas não devem ensinar um comportamento incompatível com o projeto.

Além disso, P01 inclui “Salvar resultado no histórico”, e P02/P03 oferecem exportação e salvamento de relatórios. O projeto atual condiciona histórico e exportação à investigação. Identifiquem esses controles como alternativas exploratórias ainda não incorporadas ao recorte, ou retirem-nos da versão vigente. Ter proposto uma alternativa não é um erro; apresentá-la como funcionalidade decidida quando o restante do projeto a mantém pendente é a inconsistência a corrigir.

### 5. Distinguir a comparação por imagem da comparação consolidada

PF03 está associado a T04, a comparação do desempenho consolidado usada por Larissa. Entretanto, P03 apresenta original e resultado de cada modelo, sem identificar claramente o conjunto de teste que sustenta os indicadores. Essa organização se aproxima também da comparação por imagem de T03/T07.

Expliquem qual tarefa a tela realmente cobre e como o usuário reconhece a origem dos dados comparados. A pessoa deve conseguir verificar se compara a mesma entrada ou resultados agregados do mesmo conjunto. Não é necessário criar duas telas por obrigação; é necessário tornar a distinção compreensível.

A caixa “Conclusão” afirma que DeepLabV3+ apresenta desempenho ligeiramente melhor, enquanto a tabela ilustrativa favorece FCN em IoU e acurácia e DeepLabV3+ em tempo. Falta explicitar o critério que sustenta essa conclusão e quem a formulou. Identifiquem a conclusão como julgamento da pessoa e indiquem como ela a registra ou modifica. Evitem que o desenho pareça atribuir ao sistema a decisão de qual modelo é melhor.

### 6. Consolidar a documentação da versão apresentada

Existe um gerador de uma versão 2 em `scripts/prototipos/`, com previsão de telas de processamento, falha e comparação consolidada. Contudo, a Entrega 06 apresenta apenas as três fotografias, sem integrar essa versão ao relato, à navegação ou ao registro de revisão.

A equipe precisa seguir a regra de manter no GitHub todos os artefatos que apresenta como parte da entrega, com referências internas consistentes. O código gerador não substitui as imagens de interface que o leitor deve conseguir consultar diretamente. Publiquem e vinculem a versão efetivamente adotada, ou identifiquem o gerador como trabalho ainda não incorporado. Não confundam a existência de um arquivo auxiliar com a conclusão da revisão.

O código também contém notas atribuídas à simulação sobre conexão entre telas, progresso e visualização das imagens segmentadas, além das duas observações do item 4. Esclareçam a origem dessas notas: se vieram de outra sessão, documentem-na; se são propostas da equipe, registrem-nas como propostas, sem tratá-las como falas observadas.

## Recomendações de melhoria

- Reformulem os objetivos do item 1 em termos do que a pessoa pretende alcançar, como executar uma análise e interpretar seu resultado. “Disponibilizar uma tela” descreve a solução, não o objetivo do usuário.
- No item 1.1, delimitem os recursos efetivamente explorados. Selecionar a família “relatório/resultados” não justifica automaticamente incluir exportação; escolher uma configuração disponível não equivale a configurar treinamento.
- Acrescentem legendas às fotografias com ID, tarefa coberta, versão e principais controles. Os desenhos são compreensíveis, embora algumas anotações a lápis tenham contraste baixo.
- Para uma próxima simulação de interpretação visual, utilizem exemplos simples de original e máscara nos espaços atualmente vazios. Não é necessário executar o algoritmo, mas a pessoa precisa ter algo concreto para comparar.
- Revisem o checklist com base no conteúdo demonstrado. O item sobre dashboard/CRUD/login está desmarcado, mas não há justificativa para entender se isso representa uma pendência real ou apenas preenchimento incompleto.

## Pontos que devem alimentar as próximas entregas

A seleção de vários modelos, a identificação pelo nome real e a origem das métricas devem ser retomadas no protótipo seguinte. A comparação precisa permitir uma conclusão justificada ou inconclusiva, sem confundir desempenho de segmentação com segurança do trajeto.

Investiguem a necessidade de histórico e exportação antes de incorporá-los como parte definitiva da interface. Preservem o vínculo entre observação, decisão de design e tela revisada. A simulação formativa desta etapa ajuda a encontrar problemas iniciais, mas não substitui a avaliação posterior com os participantes definidos para o projeto.

## Síntese das ações recomendadas

1. Completar o relato do walkthrough, esclarecendo participante, tarefa, percurso e observações.
2. Mostrar as alterações aplicadas, mantendo identificada a versão original.
3. Representar processamento, erros e caminhos de retorno relevantes.
4. Alinhar classes, métricas, histórico, exportação e autoria da conclusão ao recorte atual.
5. Consolidar a versão do protótipo e sua relação com T03/T07 e T04.

**Parecer geral:** a equipe entregou telas em papel e explorou atividades centrais do projeto, atendendo à base visual esperada para esta etapa. As observações registradas geraram decisões pertinentes, mas a documentação ainda precisa demonstrar melhor como ocorreu a simulação e como suas conclusões foram incorporadas. O principal avanço necessário é transformar os três desenhos em um fluxo revisado e consistente, incluindo estados relevantes e informações compatíveis com o domínio. Considero a entrega parcialmente atendida, com uma base útil e correções importantes de validação, interação e consolidação.

---

## Tratamento dos comentários

*Registro da equipe, 15/11/2026. Cada item foi conferido contra o estado atual de `docs/06_prototipacao_papel.md`, das fotos em `assets/06_prototipos/` e do gerador em `scripts/prototipos/` antes de qualquer alteração. A E6 não tinha mudado desde 08/11/2026, e os pontos do parecer continuavam válidos.*

| Item do parecer | Situação em 15/11/2026 | O que foi feito |
|---|---|---|
| 1. Explicar a simulação | Não atendido | Nova seção 4.1: participantes (colegas da disciplina, que não desenharam as telas), tarefa (carregar uma imagem e ver os resultados), percurso P01 → P02 → P03, intervenção (ajuda para seguir o fluxo entre as telas) e registro textual. A "validação com o professor" da INC-59 é esta mesma sessão. A tabela de observações passa a separar dificuldade observada de preferência expressa e a dizer o que a pessoa fez ou disse; a ajuda com o fluxo entrou como observação. Número de participantes e data ficaram como `[?]`. |
| 2. Demonstrar a revisão | Não atendido | As fotos foram mantidas como versão simulada, e a revisão foi feita por anotações sobre cada foto (`assets/06_prototipos/anotacoes/`, gerador `scripts/prototipos/anotacoes.py`). A seção 5 separa alteração decidida, situação (aplicada na anotação) e onde ver. Seleção múltipla: as configurações rodam em fila, uma de cada vez, cada uma com o seu estado; a falha de uma não interrompe as outras e aparece na linha dela, com "Repetir" e "Retirar". |
| 3. Estados e caminhos de retorno | Não atendido | Estados desenhados em baixa fidelidade nas anotações: P01-E (arquivo inválido), P01-P (processando em fila, com falha parcial), P02-S (sem métricas), P03-F (configuração sem resultado). Fluxo com caminhos de volta na seção 3.4. "Atualizar" foi retirado: trocar a seleção atualiza a visualização; executar é um comando explícito. |
| 4. Alinhar as telas ao recorte | Não atendido (a divergência só estava registrada no histórico) | Anotações: legenda *Trilha* × *Fora da trilha*; "Calcular métricas" retirado; métricas só com anotação de referência; "Distribuição das classes" retirada; histórico, exportação, "Salvar relatório/comparação" e "Configurações avançadas" marcados como fora do recorte. Seção 1.1 delimita o que foi explorado. |
| 5. Comparação por imagem × consolidada | Não atendido | Seção 2 explica que a P03 em papel mistura as duas. Na anotação, ela passa a ter duas visões com a origem dos dados escrita: P03-I (mesma imagem, T03/T07) e P03-C (conjunto de teste, T04). A "Conclusão" vira um campo preenchido pela pessoa (melhor, nenhuma ou inconclusiva, com o motivo); registrado que o exemplo do rascunho contradizia a tabela. |
| 6. Consolidar a versão apresentada | Não atendido | A versão vigente são as fotos com as anotações, publicadas e vinculadas na seção 3. O gerador `wireframes.py` foi identificado, na E6 e no README de `scripts/prototipos/`, como não incorporado e desatualizado; as notas que citam a simulação foram registradas como propostas da equipe. |
| Recomendações | Atendido | Objetivos reescritos pelo que a pessoa quer alcançar; famílias de interface delimitadas (exportação e configurar treino fora); legendas com ID, tarefa, versão e controles em cada foto; checklist revisto, com justificativa no item de dashboard/CRUD/login. Os espaços vazios de imagem continuam nas fotos; exemplos concretos de original e máscara ficam para o protótipo da Entrega 11. |
