# Feedback do Professor > Entrega 12 > Grupo 17

A equipe construiu um planejamento consistente e bastante detalhado para avaliar a interface de segmentação semântica *off-road*. As seis etapas do DECIDE foram contextualizadas, e não apenas descritas pela sigla. O plano contempla corretamente os dois métodos exigidos: avaliação heurística por inspeção e teste de usabilidade por observação de usuários.

O documento delimita bem que a avaliação examina a qualidade da interação, a compreensão das informações e o apoio às tarefas dos usuários. O desempenho científico dos modelos FCN e DeepLabV3+ não é tratado como resultado de usabilidade. Também há uma boa ligação entre personas, tarefas, metas, perguntas de avaliação, evidências e critérios esperados.

Entretanto, a entrega ainda não representa um planejamento completo e imediatamente executável. A equipe marcou o documento como concluído, mas deixou desmarcado o item que confirma a preparação dos instrumentos. Apenas o termo de consentimento foi efetivamente adaptado. O roteiro do moderador, a planilha de observação, as duas versões do questionário de compreensão e o formulário da avaliação heurística continuam sendo modelos gerais. Esse problema é decisivo porque as evidências das perguntas QA03, QA06 e QA09 a QA13 dependem diretamente desses instrumentos.

Também permanece uma inconsistência com a Entrega 8. Nela, eficiência e satisfação foram definidas como dimensões da usabilidade e receberam metas e pesos. Nesta entrega, tempo, pedidos de ajuda, facilidade percebida e SUS foram retirados da avaliação por decisão da equipe. Uma mudança é possível, mas precisa ser justificada e propagada para as metas de usabilidade, para a priorização e para a rastreabilidade. Do modo atual, o plano deixa parte das metas anteriores sem qualquer forma de verificação.

## Pontos positivos

- A equipe diferenciou corretamente avaliação de IHC e avaliação técnica dos modelos de visão computacional.
- O DECIDE foi aplicado ao projeto em todas as suas etapas: objetivos, perguntas, escolha dos métodos, questões práticas, ética, interpretação e apresentação.
- Os dois métodos exigidos estão previstos e são usados de forma complementar. A inspeção cobre problemas potenciais, estados excepcionais e acessibilidade; a observação investiga experiências reais de uso e compreensão.
- As perguntas QA01 a QA13 informam método, evidência e critério esperado. Essa organização permite saber antecipadamente como cada pergunta será respondida.
- Os perfis U01, U02 e U03 estão relacionados às personas e às tarefas que fazem sentido para cada papel.
- As tarefas UT01 a UT04 descrevem objetivos do usuário sem indicar diretamente menus ou botões. A UT04 corrige uma lacuna anterior ao incluir a configuração e o acompanhamento do treino.
- A preparação do estado inicial de cada sessão reduz variações desnecessárias entre participantes e evita depender de improvisação durante o teste.
- O plano reconhece que três participantes não sustentam generalização estatística e propõe interpretar cada perfil como um caso.
- As definições de sucesso total, sucesso parcial, falha, erro, erro crítico, dúvida, ajuda e abandono estão claras e foram estabelecidas antes da coleta.
- A separação entre falhas que serão observadas com usuários e falhas que serão verificadas somente na inspeção evita provocar situações técnicas artificiais ou difíceis de controlar.
- O termo de consentimento está adaptado ao projeto e explica objetivo, duração, gravação, privacidade, voluntariedade, descarte e contato institucional.
- O plano prevê anonimização, armazenamento privado e proteção dos participantes diante da liderança da equipe Baja.
- A equipe especificou como consolidará duplicidades, severidade, evidências e decisões de melhoria na rastreabilidade.

## Correções prioritárias

### 1. Os instrumentos E.2 a E.5 precisam ser produzidos antes da execução

A seção E lista cinco instrumentos, mas somente o E.1 foi desenvolvido. Os arquivos ligados como E.2, E.3 e E.5 são modelos gerais com campos como `{{...}}`, e não formulários preparados para este estudo. O E.4, questionário de compreensão, não foi apresentado em nenhuma das duas versões anunciadas.

Essa pendência impede a execução uniforme do plano. Sem o roteiro adaptado, moderadores diferentes podem fornecer explicações diferentes. Sem a planilha preparada, os observadores podem registrar categorias incompatíveis. Sem os questionários, não existe a evidência prevista para QA03, QA06 e MU08. Sem o formulário heurístico adaptado, não fica estabelecido como QA09 a QA13 serão examinadas e consolidadas.

A equipe deve preparar e preservar no projeto:

- o roteiro completo do moderador, com abertura, perguntas de perfil, instruções UT01–UT04, regras de intervenção e conversa pós-teste;
- a planilha de observação com campos para tarefa, sucesso, erro, ajuda, dúvida, fala, tela, meta e evidência;
- o questionário do U01, com as quatro questões de compreensão previstas em QA03;
- o questionário do U03, com as quatro questões previstas em QA06;
- o formulário da inspeção com versão da interface, telas e estados examinados, heurística, descrição, consequência, evidência, severidade, justificativa e recomendação;
- os campos necessários à verificação por teclado, leitor de tela e ampliação de 200%.

Depois disso, o checklist deve ser atualizado de acordo com a situação real.

### 2. Eficiência e satisfação foram retiradas sem revisão das metas da Entrega 8

A Entrega 8 definiu MU06 para tempo, MU07 para pedidos de ajuda, MU09 para facilidade percebida e MU10 para satisfação geral pelo SUS. Essas metas receberam pesos na priorização. A Entrega 12 declara que tempo e satisfação não serão medidos e registra que essas quatro metas deixam de ser verificadas.

O problema não é simplesmente escolher menos métricas. O problema é manter metas anteriores como parte da engenharia de usabilidade e, ao mesmo tempo, retirar os instrumentos que permitiriam avaliá-las. Há ainda uma incoerência interna: o plano afirma que MU07 não será medida, mas registra pedidos de ajuda em várias perguntas e usa “sem ajuda” como critério de sucesso.

A equipe deve escolher uma direção e propagá-la em todos os artefatos. Se eficiência e satisfação continuam sendo metas, o plano precisa incluir suas medidas. Se deixaram de ser pertinentes, a Entrega 8 deve ser revisada com justificativa, novos pesos e indicação explícita do que será avaliado no lugar. Uma alternativa simples seria manter a contagem de ajuda, uma pergunta curta de facilidade após cada tarefa e uma medida de satisfação geral. O tempo de interação pode ser separado do tempo de processamento para não medir o desempenho do modelo.

### 3. O plano ainda possui questões práticas em aberto

O DECIDE exige que as questões práticas sejam administradas antes da avaliação. No documento, o cronograma mantém datas como `[?]`, a data do piloto não foi definida, a configuração do computador permanece desconhecida e a duração do treino da UT04 ainda depende de confirmação.

Essas informações afetam diretamente a execução. O equipamento interfere no tempo de processamento e na possibilidade de concluir a UT04 durante a sessão. A ausência de datas pode inverter a ordem planejada entre inspeção, correções, piloto e teste. A equipe deve registrar datas, responsáveis, equipamento, resolução de tela, versão final da interface e parâmetros do treino rápido antes de iniciar a coleta.

### 4. O piloto precisa verificar a compreensão com alguém que não conheça a solução

O plano permite que um integrante da própria equipe seja o participante do piloto. Essa pessoa pode ajudar a testar gravação, dados e tempo técnico, mas já conhece os conceitos, os fluxos e os rótulos da interface. Por isso, não oferece boa evidência de que os cenários e perguntas são compreensíveis para um participante real.

Sugiro que o piloto de compreensão seja feito com uma pessoa externa ao projeto, preferencialmente próxima de um dos perfis. Se um integrante for usado para o ensaio técnico, a equipe deve registrar essa limitação e realizar uma segunda passagem curta com alguém que não conheça a interface.

### 5. A amostra permite estudos de caso, mas não repetição dentro de cada perfil

O plano prevê três participantes, um por persona. Isso respeita a quantidade prevista, distribui os perfis e é apresentado corretamente como estudo sem pretensão estatística. Entretanto, qualquer resultado observado em U01, U02 ou U03 pode decorrer de características individuais e não do perfil representado.

A equipe deve manter a linguagem de relato por caso e evitar frases como “os usuários P01 conseguem”. O texto correto será que “o participante U01 conseguiu nas condições avaliadas”. Caso seja possível recrutar mais pessoas, a repetição dentro de cada perfil aumentará a confiança. Participantes aproximados devem permanecer identificados e analisados separadamente, como o plano já propõe.

### 6. A rastreabilidade precisa resolver, e não apenas registrar, as inconsistências abertas

O `PENDENCIAS.md` identifica corretamente INC-71, INC-72 e INC-73. Contudo, as três continuam abertas enquanto o documento principal aparece como concluído. Também permanece a divergência entre a Entrega 8, que descreve partes simuladas, e a Entrega 12, que afirma que nenhum processamento ou dado será simulado.

Antes da avaliação, a equipe deve atualizar a Entrega 8, o planejamento e a rastreabilidade para que todos indiquem a mesma versão da solução, as mesmas metas e os mesmos métodos. Uma pendência bem documentada continua sendo uma pendência; o registro não substitui a correção.

## Recomendações de melhoria

- Incluir uma folha de preparação por sessão com os arquivos, configurações, ciclo de testes e estado inicial que deverão existir antes da chegada do participante.
- Definir uma regra padronizada para pausas técnicas longas, principalmente durante treino e segmentação, sem confundir espera do algoritmo com dificuldade de interação.
- Registrar separadamente ajuda solicitada, ajuda oferecida e simples releitura do cenário. A definição já existe e deve aparecer como campo no instrumento.
- Acrescentar uma pergunta pós-tarefa aberta, como “O que tornou esta atividade fácil ou difícil?”, mesmo que a equipe opte por não usar uma escala de satisfação.
- Documentar quais integrantes realizarão cada inspeção, moderação e observação, evitando que a mesma pessoa modere e registre simultaneamente.
- Na consolidação heurística, preservar a avaliação individual antes da reunião de consenso, inclusive quando a equipe discordar sobre heurística ou severidade.
- Informar que a ausência de problemas encontrados não comprova alta usabilidade; indica apenas que o estudo, com aquele escopo e participantes, não revelou outros problemas.

## Pontos que devem alimentar as próximas entregas

- A Entrega 13 deve usar um formulário definitivo e registrar cobertura de todas as telas e estados, incluindo TL11, falha na execução, treino interrompido e falta de memória.
- Problemas de severidade alta encontrados na inspeção devem ser corrigidos antes do piloto e do teste com usuários. O novo commit precisa constar no planejamento e na Entrega 14.
- A Entrega 14 deve relatar cada participante por perfil, sem generalização, e separar claramente participante real de participante aproximado.
- As respostas aos questionários de compreensão precisam ser relacionadas a QA03 e QA06, com gabarito e regra de pontuação definidos antes das sessões.
- As observações sobre pedidos de ajuda devem ser comparadas à decisão sobre MU07, pois o plano já coleta esse dado.
- A regra “valor de referência = última configuração executada” e a atividade da TL11 devem receber atenção, pois foram decisões introduzidas na implementação e ainda possuem limitações de modelagem.
- Alterações decorrentes da avaliação devem voltar à rastreabilidade, aos MoLIC e ao modelo conceitual quando modificarem o fluxo ou os signos.

## Síntese das ações recomendadas

1. Produzir e preservar os instrumentos E.2 a E.5 já adaptados ao projeto.
2. Resolver a relação entre o plano e as metas de eficiência e satisfação da Entrega 8.
3. Preencher datas, equipamento, versão final e parâmetros técnicos do piloto e das sessões.
4. Executar um piloto de compreensão com uma pessoa que não conheça a interface.
5. Resolver INC-71, INC-72 e INC-73 antes de marcar o planejamento como concluído.
6. Iniciar a Entrega 13 somente com o formulário heurístico definitivo e executar a Entrega 14 somente depois das correções e do piloto.

## Parecer geral sobre a entrega

De forma geral, a Entrega 12 demonstra ótimo entendimento do DECIDE e apresenta uma ligação cuidadosa entre pessoas, tarefas, perguntas, métodos, evidências e critérios de análise. O planejamento dos cenários e a distinção entre inspeção e observação estão acima de uma simples reprodução do modelo. Ainda assim, um plano de avaliação só está completo quando pode ser executado por outra pessoa sem improvisar instrumentos ou decisões. A equipe precisa transformar os modelos genéricos nos formulários reais do estudo, resolver as inconsistências com as metas da Entrega 8 e fechar as questões práticas que permanecem abertas. Com essas correções, o material terá condições de orientar avaliações consistentes e produzir evidências confiáveis para a evolução da interface.
