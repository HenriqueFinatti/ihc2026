# Entrega 12 — Planejamento da avaliação de usabilidade (DECIDE)

**Data:** 16/11/2026 (início) · 20/11/2026 (conclusão)  
**Status:** 🟩 concluída  
**Responsabilidade:** 1 solução por equipe

## Objetivo da atividade

Planejar a avaliação antes de executá-la, ligando perguntas de avaliação a métodos, participantes, tarefas, métricas, aspectos práticos, ética e forma de análise.

## O que está sendo avaliado

<!-- Deixar essa parte comentada -->
<!-- Em projetos cuja interface foi criada ou ampliada para a disciplina, o plano deve declarar explicitamente que a avaliação investiga **a qualidade da interação/protótipo**, não a validade científica ou o desempenho técnico do algoritmo/modelo do TCC.

Exemplos de perguntas:

- o DBA consegue localizar e comparar duas execuções?
- o analista entende o significado de um indicador?
- o administrador consegue alterar uma permissão sem risco de erro não percebido?
- o usuário compreende que o processamento está em andamento e consegue recuperar-se de uma falha?
- os filtros ajudam a localizar o histórico relevante?
- um relatório permite identificar a informação necessária para a decisão?

Se o protótipo utiliza dados ou resultados simulados, documente isso no plano. -->

<!-- ### O que a avaliação investiga -->

A avaliação investiga a **qualidade da interação** com a interface implementada na Entrega 11: se P01 (Rafael), P02 (Andreia) e P03 (Larissa) conseguem executar, interpretar, comparar e registrar conclusões nas tarefas T01–T08 com eficácia e compreensão do que veem (Entrega 8, §3). Ela **não** avalia a validade científica do TCC nem o desempenho dos modelos FCN e DeepLabV3+: IoU, acurácia e tempo de inferência são resultados técnicos do TCC e aparecem no teste como material da tarefa, não como objeto de avaliação.

| Camada | Entra na avaliação? | Como aparece no plano |
|---|---|---|
| Interação com a interface: enviar as entradas e escolher as configurações (TL03), acompanhar o processamento (TL04), ler a máscara e a legenda e registrar a avaliação da imagem (TL05), comparar na mesma imagem (TL06), ler o desempenho consolidado e a diferença entre configurações (TL07), registrar a conclusão (TL08) e a decisão (TL09), consultar os termos (TL10), configurar e acompanhar o treino (TL01, TL02) | Sim | Sucesso, erros e pedidos de ajuda nas tarefas de teste (MU01–MU04, MU08 e MU11) e inspeção das telas na Entrega 13, que verifica também a MU05 |
| Compreensão dos resultados técnicos: o que a máscara mostra, por que uma foto de campo não tem métricas, o que cada métrica indica e não indica, se a segmentação indica segurança do trajeto | Sim | Falas, observação e questionário de compreensão (MQ01–MQ03, MU04, MU08) |
| Valor das métricas e desempenho dos modelos: qual configuração tem o maior IoU, se FCN ou DeepLabV3+ é melhor, quão boa é a segmentação das fotos | Não; a leitura que a pessoa faz das métricas entra (linha anterior) | O desempenho é avaliado no TCC, pelo conjunto de teste. No teste com usuários, o sucesso não depende de qual configuração o participante escolhe, e sim de a escolha citar a configuração, a entrada e a métrica corretas e de a decisão continuar sendo da pessoa (MQ07, RQ08) |
| Duração do processamento e do treino | Não; a forma como a interface comunica a espera entra (estado, progresso e fila na TL04 e na TL02; MQ04) | A duração depende do equipamento e não muda com o design; não é medida no teste |
| Tela de apoio Datasets (TL11), fora dos MoLIC e sem tarefa de usuário (Entrega 11) | Só na inspeção | Entra na avaliação heurística da Entrega 13, que percorre todas as telas e estados; não entra no teste com usuários |

Perguntas que orientam a avaliação (as perguntas detalhadas, com método, evidência e critério, estão na seção B):

- O analista (P01) entende o que a máscara mostra e consegue apontar onde o modelo errou, separando problema da foto e problema do modelo? (MQ01; RQ05)
- Diante de uma foto de campo, ele entende por que não há IoU e avalia visualmente, sem concluir que o trecho é seguro? (MQ02; RQ06)
- Durante a segmentação, a pessoa sabe sempre em que estado está cada configuração? (MQ04; RQ01)
- Ao comparar duas configurações na mesma foto, a pessoa sabe a que configuração e a que foto cada resultado se refere? (MQ05; RQ02, RQ03)
- A gestora (P03) entende o que a diferença entre configurações indica e prepara a recomendação sem atribuir a escolha ao sistema? (MQ03, MQ07; RQ07, RQ08)
- A pesquisadora (P02) define uma configuração de treino entendendo cada parâmetro e, ao voltar, sabe como o treino está? (MQ06; a forma de avaliar a T08 é definida na seção D)

### Dados usados na avaliação

Nenhuma parte da avaliação é simulada. A interface roda sobre uma cópia completa dos dados do TCC, e as métricas exibidas são os resultados reais no conjunto de teste. As imagens de campo são fotos reais dos testes da equipe Baja. Falhas não serão provocadas no teste com usuários; por isso, a recuperação de falha na execução (MU05 e a parte de falha da MQ04) e a falta de memória no treino (parte da MQ06 e da MU11) são avaliadas só na inspeção heurística da Entrega 13 (`PENDENCIAS.md`, INC-71).

## A. Método DECIDE

| Etapa | Aplicação no projeto |
|---|---|
| **D — Determine the goals** | **Objetivo geral:** verificar se a interface implementada na Entrega 11 permite que P01 (Rafael), P02 (Andreia) e P03 (Larissa) façam as tarefas T01–T08 com eficácia e compreensão do que veem, e encontrar os problemas que impedem isso, para corrigi-los no protótipo (Entrega 8, §4).<br>**Objetivos específicos**, ligados às metas da Entrega 8: (1) compreensão do resultado e dos seus limites: máscara, legenda, estado "sem métricas" e o que a segmentação não indica (MQ01, MQ02, MU04, MU08); (2) execução e acompanhamento da segmentação com sensação de controle (MQ04, MU01); (3) comparação na mesma imagem sem perder a referência de configuração e entrada (MQ05, MU02); (4) leitura das métricas e preparo da recomendação, com a decisão continuando com a pessoa (MQ03, MQ07, MU03); (5) definição e acompanhamento do treino (MQ06, MU11, conforme a tarefa da seção D).<br>A recuperação de falha na execução (MU05 e parte da MQ04) e a falta de memória no treino (parte da MQ06 e da MU11) são verificadas só na inspeção (ver "Dados usados na avaliação"). |
| **E — Explore the questions** | As perguntas partem das metas da Entrega 8 e das rupturas previstas nos MoLIC da Entrega 10.<br>**No teste com usuários:** as seis perguntas de "O que está sendo avaliado" (compreensão da máscara, estado "sem métricas", estado da execução, comparação na mesma imagem, leitura da diferença entre configurações e treino).<br>**Na inspeção:** a interface mostra o estado do sistema, previne e explica os erros previstos (formato não aceito, nome repetido, conjuntos de teste diferentes, configuração sem avaliação no conjunto de teste, condição obrigatória) e usa os mesmos termos em todas as telas? Os critérios de acessibilidade que a Entrega 11 deixou para conferir (percurso de cada tarefa só com teclado, leitor de tela e ampliação de 200%) são atendidos?<br>Na seção B, cada pergunta vira um item QA com método, evidência e critério. |
| **C — Choose the evaluation paradigm and techniques** | Dois métodos complementares.<br>**Inspeção (Entrega 13):** avaliação heurística com as 10 heurísticas de Nielsen, feita por cada integrante sozinho, em todas as telas e estados TL01–TL11, com a verificação dos critérios da WCAG 2.2 AA da Entrega 8, §2. Não depende de recrutar participantes, encontra problemas que podem ser corrigidos antes do teste e cobre os estados que o teste não vai provocar, como a falha na execução. Como o avaliador não é o usuário, ela não mostra se a pessoa entende a máscara ou se atribui a escolha ao sistema.<br>**Observação de usuários (Entrega 14):** teste de usabilidade em laboratório, com as tarefas da seção D, protocolo de pensar em voz alta `[H]` e registro de sucesso, erros e pedidos de ajuda; questionário de compreensão (MU08) e conversa curta pós-teste. É o método que verifica as metas qualitativas de compreensão e de controle da decisão (MQ01–MQ07).<br>O estudo de campo à beira da pista fica fora, porque esse contexto ainda é `[?]` (Entrega 8, §1). |
| **I — Identify the practical issues** | **Participantes:** 3, o mesmo número de integrantes, membros da equipe Baja FEI que não são autores deste projeto nem do TCC (Entrega 8, §3.2; Entrega 7, exclusão dos autores) ou, se faltar alguém de um perfil, o participante aproximado previsto na seção C. Perfis e critérios na seção C.<br>**Recrutamento:** convite pelos mesmos canais da Entrega 7 `[H]`; participação voluntária.<br>**Ambiente e equipamento:** presencial, no laboratório da FEI, contexto prioritário da análise (Entrega 8, §2), no computador que executa os modelos, com a interface aberta sobre a cópia completa dos dados do TCC.<br>**Responsáveis:** em cada sessão, um integrante modera e outro anota; cada integrante modera ao menos uma sessão.<br>**Piloto:** antes da Entrega 14, com uma pessoa que não conta na amostra (pode ser um integrante, conforme a Entrega 14). Valida o roteiro, as instruções, a duração da sessão e o preparo da cópia dos dados.<br>**Cronograma:** Entrega 13, correção dos problemas prioritários, piloto e Entrega 14, nessa ordem; datas `[?]`.<br>**Riscos técnicos:** com a cópia completa, segmentar e treinar com o ResNet152 leva tempo e pode alongar a sessão, por isso cada tarefa usa poucas fotos e a duração do treino é tratada na seção D; fechar o programa interrompe treino e execução, por isso o computador fica dedicado à sessão; a falta de memória no treino não pode ser provocada no equipamento (Entrega 11). |
| **D — Decide how to deal with ethical issues** | **Base:** atividade de ensino, sem finalidade de pesquisa científica; não é registrada no sistema CEP/Conep (Resolução CNS 510/2016, art. 1º, parágrafo único), mas segue os mesmos princípios e a LGPD (Lei 13.709/2018), como na Entrega 7.<br>**Consentimento:** termo adaptado do modelo da disciplina, lido e aceito antes da sessão, com objetivo, duração, registros e contato (e-mails institucionais dos três responsáveis, os mesmos da Entrega 7).<br>**Abertura da sessão:** quem está sendo avaliada é a interface, não a pessoa; ela pode parar a qualquer momento, pular uma tarefa e pedir a exclusão dos seus dados até o fim do semestre letivo.<br>**Registros:** gravação da tela da interface e do áudio só com autorização no termo `[H]`; sem vídeo do rosto; sem autorização, só anotações.<br>**Anonimização:** códigos U01 a U03 nos documentos; a lista que liga código e nome fica fora do repositório. Como a equipe é pequena, o desempenho de cada participante não é repassado à liderança nem à coordenação da equipe Baja.<br>**Imagens dos testes:** só fotos sem pessoas reconhecíveis ou com autorização de quem aparece nelas (Entrega 8, §2).<br>**Armazenamento e descarte:** registros brutos em uma pasta privada dos três autores, fora do repositório; gravações apagadas depois da análise; anotações e lista de códigos apagadas ao fim do semestre letivo. |
| **E — Evaluate, interpret and present the data** | **Inspeção:** cada avaliador registra o local, a heurística, a evidência (captura), a severidade (0 a 4, escala de Nielsen) e a recomendação; a equipe junta os problemas duplicados sem apagar quem encontrou cada um.<br>**Teste:** sucesso, erros e pedidos de ajuda registrados por participante e por tarefa na planilha de observação; falas codificadas pelas metas MQ01–MQ07. Cada meta MU é comparada ao critério da seção B (atingida ou não atingida), e cada meta MQ recebe as evidências observadas.<br>**Interpretação:** com 3 participantes, os números não têm valor estatístico; servem para comparar com as metas e apontar problemas, não para generalizar. Os problemas são priorizados pela severidade e pela frequência (quantos participantes ou avaliadores os encontraram).<br>**Apresentação:** na Entrega 14, uma tabela com o resultado de cada pergunta da seção B e uma por problema, com a mudança proposta para cada problema prioritário, registrada na coluna "Decisão/melhoria" da `RASTREABILIDADE.md`, §3 (Entrega 8, §4). Os critérios detalhados estão na seção F. |

## B. Perguntas de avaliação

Cada pergunta só usa evidência de quem tem o perfil da persona da tarefa. No teste com usuários há um participante por perfil: U01 (perfil P01) faz a UT01 e a UT02; U02 (perfil P02) faz a UT02 e a UT04; U03 (perfil P03) faz a UT03 (tarefas na seção D; perfis e participante aproximado na seção C). Por isso os critérios valem para cada participante e são lidos caso a caso, sem pretensão de generalizar. As perguntas QA09 a QA13 são respondidas só pela inspeção da Entrega 13.

| ID | Pergunta | Método | Métrica/evidência | Critério esperado |
|---|---|---|---|---|
| QA01 | O participante de perfil P01 executa a segmentação de fotos de campo e avalia o resultado sem ajuda? | Observação com pensar em voz alta (UT01, U01) | Sucesso, pedidos de ajuda e erros; avaliação registrada na TL05 | U01 conclui sem ajuda e aponta ao menos uma região mal classificada (MU01) |
| QA02 | Ele entende o que a máscara mostra e separa problema da foto de problema do modelo? | Observação com pensar em voz alta (UT01, U01) | Falas; origem do problema registrada na avaliação da imagem (RQ05) | Explica com as próprias palavras o que é *Trilha* e *Fora da trilha*, sem pedir ajuda para ler a legenda (MQ01) |
| QA03 | Diante de uma foto de campo, ele entende por que não há métricas e não conclui que o trecho é seguro? | Observação com pensar em voz alta e questionário de compreensão (UT01, U01) | Falas; respostas ao questionário (versão do U01, sobre a máscara e a foto sem métricas); erros críticos | Nenhum erro crítico (MU04); pelo menos 3 de 4 acertos no questionário (MU08); avalia visualmente sem procurar IoU (MQ02) |
| QA04 | Durante a segmentação, a pessoa sabe em que estado está cada configuração? | Observação com pensar em voz alta (UT01 e UT02, U01 e U02) | Perguntas como "travou?", comando repetido sem motivo, falas sobre o estado | Nenhuma pergunta sobre o estado e nenhum comando repetido sem motivo (MQ04, sem a parte de falha) |
| QA05 | Ao comparar duas configurações na mesma foto, a pessoa sabe a que configuração e a que foto cada resultado se refere? | Observação com pensar em voz alta (UT02, U01 e U02) | Sucesso; perguntas como "qual é qual?"; conclusão registrada na TL08 | Cada participante conclui sem ajuda, e a conclusão cita a configuração e a foto corretas (MU02, MQ05); nenhum resultado atribuído à configuração errada (MU04) |
| QA06 | O participante de perfil P03 lê o desempenho consolidado e interpreta a diferença entre configurações sem que o sistema julgue a relevância por ele? | Observação com pensar em voz alta e questionário de compreensão (UT03, U03) | Falas; consultas à explicação dos termos (TL10); respostas ao questionário (versão do U03, sobre o valor de referência e a diferença entre configurações) | Cita a métrica e o que ela indica e julga com as próprias palavras se a diferença importa (MQ03); pelo menos 3 de 4 acertos no questionário (MU08) |
| QA07 | Ele prepara e registra a recomendação sem atribuir a escolha ao sistema? | Observação com pensar em voz alta e conversa pós-teste (UT03, U03) | Recomendação registrada na TL08; fala pós-tarefa | U03 conclui sem ajuda e a recomendação cita a métrica e uma ressalva (MU03); não atribui a escolha ao sistema (MQ07) |
| QA08 | O participante de perfil P02 define uma configuração de treino entendendo cada parâmetro e, ao voltar, identifica o estado do treino? | Observação com pensar em voz alta (UT04, U02) | Sucesso, pedidos de ajuda; falas sobre os parâmetros e o estado | U02 conclui sem ajuda e identifica se o treino está em andamento ou terminou, e por que terminou (por exemplo, pelo early stopping) (MU11 e MQ06, sem a falha por falta de memória, que fica na QA09) |
| QA09 | A interface mostra o estado e ajuda a se recuperar de falhas na execução e no treino (falha na execução, treino interrompido, falta de memória)? | Inspeção heurística (Entrega 13) | Violações de H1 e H9 na TL02 e na TL04 | Nenhuma violação de severidade 3 ou 4 (MU05 e parte de falha da MQ04, da MQ06 e da MU11, verificadas só por inspeção) |
| QA10 | A interface previne e explica os erros previstos nos MoLIC (formato não aceito, nome repetido, conjuntos de teste diferentes, configuração sem avaliação no conjunto de teste, condição obrigatória)? | Inspeção heurística (Entrega 13) | Violações de H5 e H9 na TL01, TL03, TL07, TL09 e TL11 | Nenhuma violação de severidade 3 ou 4 |
| QA11 | Os termos, a legenda e as cores são os mesmos em todas as telas e explicados no ponto de uso? | Inspeção heurística (Entrega 13) | Violações de H2, H4 e H10 em todas as telas | Nenhuma violação de severidade 3 ou 4 (RQ04, RQ07) |
| QA12 | A interface deixa a decisão com a pessoa (maior valor sem ar de recomendação, diferença sem julgamento, conclusão registrada pela pessoa)? | Inspeção heurística (Entrega 13) | Violações de H2 e H3 na TL07, TL08 e TL09, à luz da linha de interação humano-IA da Entrega 8, §2 | Nenhuma violação de severidade 3 ou 4 (RQ08) |
| QA13 | A interface atende aos critérios de acessibilidade da Entrega 8, incluindo os que a Entrega 11 deixou para conferir? | Inspeção (WCAG 2.2 AA, Entrega 13) | Percurso da UT01 à UT04 só com teclado; uso com leitor de tela; ampliação de 200% | Todos os cinco pontos prioritários da Entrega 8, §2, atendidos |

## C. Escopo e participantes

| Item | Planejamento |
|---|---|
| Perfis | Os mesmos perfis principais da coleta da Entrega 7, um para cada persona:<br>**U01 — perfil P01 (Rafael):** integrante da equipe Baja FEI que analisa os resultados da segmentação depois dos testes (Entrega 7, A02). Faz a UT01 e a UT02.<br>**U02 — perfil P02 (Andreia):** pessoa que define configurações e treina modelos de visão computacional ligados à Baja FEI (Entrega 7, A03). Faz a UT02 e a UT04.<br>**U03 — perfil P03 (Larissa):** integrante que prepara ou toma a decisão sobre a configuração usada nos testes (Entrega 7, A01). Faz a UT03. |
| Critérios de inclusão/exclusão | **Inclusão**, os mesmos critérios da Entrega 7: U01 executou ou analisou resultados de segmentação no último semestre; U02 definiu ou acompanhou o treino de pelo menos um modelo de visão computacional no último ano; U03 participou de pelo menos uma escolha de configuração de modelo no último semestre. Todos têm 18 anos ou mais e aceitam o termo de consentimento.<br>**Exclusão:** autores deste projeto e do TCC (as respostas deles confirmariam as próprias hipóteses, Entrega 7); quem participou do teste piloto; quem já usou a interface da Entrega 11 `[H]`. Ter participado da coleta da Entrega 7 não exclui `[H]`.<br>**Se faltar alguém do perfil:** entra o participante aproximado (proxy) que a Entrega 7 previu para o mesmo perfil: P01, aluno de Ciência da Computação da FEI com experiência em visão computacional fora da Baja; P02, pesquisador de visão computacional da FEI fora da Baja; P03, ex-integrante que exerceu esse papel ou gestor de outra equipe de competição da FEI. O proxy é registrado como limitação na Entrega 14 e seu resultado é lido separadamente. Um participante de outro perfil nunca substitui o perfil que falta. |
| Nº de participantes | 3, o mesmo número de integrantes (Entrega 14), um por perfil. A UT02 tem dois casos (U01 e U02); a UT01, a UT03 e a UT04 têm um caso cada. A pessoa do piloto não conta. |
| Ambiente | Presencial, no laboratório da FEI, que é o contexto prioritário da análise (Entrega 8, §2), em uma sala sem interrupções `[H]`. Em cada sessão, um integrante modera e outro anota. Duração prevista de até 60 minutos por sessão `[H]`, conferida no piloto. |
| Dispositivo | O computador que executa os modelos, com mouse e teclado, e a interface aberta no navegador desse computador, em endereço local e sem internet (Entrega 8, §1; Entrega 11, "Como executar"). A interface roda sobre a cópia completa dos dados do TCC e o computador fica dedicado à sessão. Configuração do computador (processador gráfico, memória, tamanho da tela): `[?]`. |
| Protótipo/versão | Interface implementada na Entrega 11: repositório https://github.com/HenriqueFinatti/Segmentacao-Semantica-Off-Road, ramo `interface`, commit `d11c155`. As três sessões usam a mesma versão. Se problemas da Entrega 13 forem corrigidos antes do teste, o novo commit é registrado aqui e na Entrega 14. O estado inicial da interface em cada tarefa (sessão, configurações e treinos já existentes) é definido na seção D. |
| Teste piloto | **Quem:** uma pessoa que não faz parte da amostra; pode ser um integrante que não modera a sessão piloto (Entrega 14) `[H]`.<br>**Quando:** depois das correções da Entrega 13 e antes da primeira sessão da Entrega 14; data `[?]`.<br>**O que validar:** se as instruções da UT01 à UT04 são entendidas sem dizer onde clicar; a duração da sessão e o tempo do treino na UT04; o preparo da cópia dos dados e do estado inicial de cada tarefa; o roteiro do moderador, a planilha de observação, as duas versões do questionário de compreensão e a gravação. As respostas do piloto não entram na análise, e as mudanças feitas depois dele são registradas na Entrega 14 (passo 4). |

## D. Lista de tarefas de avaliação

As tarefas UT01 a UT03 foram propostas na Entrega 5 (síntese), e a UT04 foi criada nesta entrega para a T08. O moderador lê o cenário em voz alta e entrega uma cópia impressa; as palavras entre colchetes são preenchidas antes da sessão. Os cenários não usam os nomes dos itens do menu nem dos botões da interface (por exemplo, "Segmentar imagens", "Comparar o desempenho", "Treinar uma configuração" e "Apresentar a recomendação").

| ID | Cenário neutro entregue ao usuário | Objetivo oculto da avaliação | Critério de sucesso | Tempo-limite (se houver) |
|---|---|---|---|---|
| UT01 | "Você voltou do teste de campo de com as fotos que estão na pasta. A equipe quer saber se a configuração que está sendo usada hoje delimita bem a trilha nessas fotos. Analise as fotos e deixe registrado, para cada uma, se o resultado está bom e, quando houver algum problema, de onde ele vem." | T02 e T01 (O03 e O04; M01; TL03, TL04 e TL05). Verifica MQ01, MQ02 e MQ04 (QA01 a QA04) | U01, sem ajuda: envia as fotos e executa com a configuração em uso; registra a avaliação de cada foto; aponta ao menos uma região mal classificada; não trata a falta de métricas como erro nem conclui que o trecho é seguro | Sem tempo-limite; o tempo não é medido, e o abandono é definido na seção F |
| UT02 | "A foto deixou dúvida sobre o resultado. A equipe tem outra configuração treinada e quer saber se ela delimita melhor a trilha nessa foto. Veja o resultado das duas configurações nessa foto e deixe registrada a sua conclusão." | T03 e T07 (O05 e O08; M01 e M03; TL06, TL04 e TL08). Verifica MQ04 e MQ05 (QA04 e QA05) | U01 e U02, cada um sem ajuda: executa a outra configuração na mesma foto; vê as duas na mesma região; registra a conclusão (uma das duas configurações, nenhuma ou inconclusiva) citando a configuração e a foto corretas; não atribui um resultado à configuração errada | Sem tempo-limite |
| UT03 | "Amanhã a coordenação vai decidir qual configuração usar nos próximos testes. As configurações usadas nos testes  já foram avaliadas. Veja como elas se saíram e deixe registrado o que você indicaria à coordenação, por que e o que ainda não se sabe sobre essa escolha." | T04 e T05, até a recomendação (O06, O07 e O08; M02; TL07, TL10 e TL08). Verifica MQ03 e MQ07 (QA06 e QA07) | U03, sem ajuda: lê o desempenho das configurações do ciclo; registra uma recomendação (uma configuração, nenhuma ou adiar) que cita ao menos uma métrica e uma ressalva; julga com as próprias palavras se a diferença importa; não atribui a escolha ao sistema | Sem tempo-limite |
| UT04 | **Parte 1:** "Antes de rodar o experimento completo, você quer um teste rápido do DeepLabV3+ treinado só com as imagens do Freiburg Forest, que termine durante esta sessão. Prepare esse treino e deixe-o rodando." **Parte 2**, depois das outras atividades da sessão: "Você voltou ao computador. Diga como está o treino que você deixou rodando." | T08 (O01 e O02; M03; TL01 e TL02). Verifica MQ06 (QA08) | U02, sem ajuda: escolhe o DeepLabV3+, só o Freiburg Forest e um número de épocas compatível com um teste rápido; inicia o treino; na parte 2, identifica se o treino está em andamento ou terminou e, se terminou, por quê (por exemplo, pelo early stopping) | Sem tempo-limite |

> Uma boa instrução descreve o objetivo do participante sem dizer **onde clicar** ou usar o rótulo exato do controle que está sendo testado.

### Preparação e ordem das tarefas

Toda a preparação é feita pelo moderador, na própria interface e sobre a cópia completa dos dados, antes da sessão; nada é simulado.

| Participante | Estado inicial da interface | Ordem da sessão |
|---|---|---|
| U01 (perfil P01) | Nenhuma sessão aberta (estado vazio da TL05). Configurações do TCC disponíveis, uma delas em uso. Pasta com 3 fotos reais de um teste de campo da Baja `[H]`, sem pessoas reconhecíveis, em que a configuração em uso erra visivelmente em ao menos uma; a foto da UT02 é uma delas | Termo e perfil pré-teste → UT01 → questionário de compreensão (versão do U01) → UT02, na sessão criada na UT01 → conversa pós-teste |
| U02 (perfil P02) | Sessão já criada com as mesmas fotos, executada com a configuração em uso e com a avaliação das fotos registrada, a foto da UT02 marcada como duvidosa. Nenhum treino em andamento | Termo e perfil pré-teste → UT02 → UT04, parte 1 → conversa pós-teste, enquanto o treino roda → UT04, parte 2 |
| U03 (perfil P03) | Ciclo de testes com duas configurações (FCN e DeepLabV3+) executadas no ciclo e avaliadas no mesmo conjunto de teste, uma delas em uso; nenhuma recomendação registrada | Termo e perfil pré-teste → UT03 → questionário de compreensão (versão do U03) → conversa pós-teste |

Na UT04, o treino roda no mesmo processador gráfico que a execução da segmentação; por isso a UT02 vem antes da UT04 na sessão do U02. A duração do treino com poucas épocas é conferida no piloto `[?]`.

## E. Instrumentos

Os instrumentos foram adaptados dos modelos da disciplina em `instrumentos/`.

| Instrumento | Para quê | Quando | Modelo de origem |
|---|---|---|---|
| E.1 Convite e termo de consentimento | Convidar e registrar o consentimento de U01 a U03 e da pessoa do piloto | Antes da sessão | [Modelo de termo de consentimento](../instrumentos/termo_consentimento_modelo.md) e termo da I01 (Entrega 7) |
| E.2 Roteiro do moderador | Abertura, perfil pré-teste, pensar em voz alta, aplicação das tarefas e conversa pós-teste | Durante a sessão | [Roteiro de teste](../instrumentos/roteiro_teste_usabilidade.md) |
| E.3 Planilha de observação | Registrar sucesso, erros, pedidos de ajuda e falas por participante e tarefa (QA01 a QA08) | Durante a sessão | [Planilha de observação](../instrumentos/planilha_observacao_modelo.md) |
| E.4 Questionário de compreensão | Verificar a MU08, em duas versões: U01 e U03 (QA03 e QA06) | Depois da UT01 (U01) e da UT03 (U03) | Meta MU08 (Entrega 8, §3.2) |
| E.5 Formulário de avaliação heurística | Registrar a inspeção de cada integrante e responder às QA09 a QA13 | Entrega 13 | [Formulário de avaliação heurística](../instrumentos/formulario_heuristica_modelo.md) |

### E.1 Termo de consentimento

> **Projeto:** Interface para análise de segmentação semântica de vias off-road — disciplina de Interação Humano-Computador, FEI.  
> **Atividade:** teste de usabilidade da interface.  
> **Responsáveis:** Henrique Finatti Silveira Belo Trebbi, Mateus Marana Assuena e Tiago Fagundes dos Santos.
>
> **Convite e objetivo.** Você está sendo convidado(a) a usar a interface de análise de segmentação em algumas atividades parecidas com o trabalho da equipe Baja, para descobrirmos o que nela é fácil ou difícil de usar e de entender. **Estamos avaliando a interface, não a sua capacidade.** Não há respostas certas ou erradas, e qualquer dificuldade nos ajuda a melhorar a interface.
>
> **O que será solicitado.** Fazer de uma a três atividades na interface, falando em voz alta o que está pensando, responder a algumas perguntas curtas e conversar sobre a experiência. A sessão dura até 60 minutos, presencialmente, no laboratório da FEI. A interface mostra fotos dos testes de campo da equipe Baja, sem pessoas reconhecíveis.
>
> **Registros.** Com a sua autorização, gravaremos a tela da interface e o áudio da sessão, apenas para conferir as anotações; não haverá vídeo do seu rosto. Sem autorização, faremos só anotações. O que você registrar na interface fica numa cópia dos dados usada só no teste. Apenas os três responsáveis terão acesso aos registros, que ficam fora do repositório do projeto. As gravações são apagadas depois da análise, e as anotações e a cópia dos dados, ao fim do semestre letivo.
>
> **Privacidade.** Seu nome não aparece em nenhum documento: você recebe um código (U01, U02…). Como a equipe é pequena, descreveremos o seu papel de forma genérica. O seu desempenho nas atividades não será informado à liderança nem à coordenação da equipe.
>
> **Voluntariedade.** A participação é voluntária. Você pode pular uma atividade ou pergunta, interromper a sessão a qualquer momento e pedir, mesmo depois, que seus dados sejam excluídos, sem justificar. Para dúvidas ou pedidos de exclusão, escreva para o e-mail institucional de qualquer um dos responsáveis: Henrique (unifhtrebbi@fei.edu.br), Tiago (uniftsantos@fei.edu.br) ou Mateus (unimassuena@fei.edu.br), até o fim do semestre letivo.
>
> **Devolutiva.** Você poderá receber a síntese anonimizada dos resultados.
>
> **Consentimento.** Declaro que tenho 18 anos ou mais, que recebi informações suficientes e que concordo em participar.  
> ( ) Autorizo a gravação da tela e do áudio. ( ) Não autorizo a gravação.  
> Código do participante: ______ Data: ___/___/______ Aceite: ______________________

## F. Plano de análise

As definições abaixo valem para todos os moderadores e anotadores e foram fixadas antes dos testes. Elas são usadas na planilha de observação (E.3) e na consolidação da Entrega 14.

| Item | Definição adotada |
|---|---|
| Sucesso total | O participante cumpre todos os itens do critério de sucesso da tarefa (seção D) sem ajuda e sem erro crítico. |
| Sucesso parcial | O participante chega ao resultado da tarefa, mas com uma ajuda do moderador, ou sem ajuda e faltando um item do critério que não é erro crítico (por exemplo, registra a avaliação das fotos, mas não aponta nenhuma região mal classificada). |
| Falha | O participante abandona a tarefa, precisa de mais de uma ajuda, comete um erro crítico sem perceber ou registra uma conclusão que cita a configuração ou a foto erradas. |
| Erro | Ação ou interpretação que se afasta do critério da tarefa. **De execução:** escolher a configuração, a foto ou o dataset errado, ou registrar a informação no lugar errado. **De interpretação:** ler a máscara, a legenda, um estado ou uma métrica de forma incorreta. Um erro que o próprio participante percebe e corrige é registrado, mas não conta como erro crítico. |
| Erro crítico | Os três da MU04 (Entrega 8), quando o participante não os percebe: concluir pela máscara que o trecho é seguro; tratar uma foto de campo como se tivesse métricas; atribuir um resultado à configuração errada. |
| Dúvida | Pergunta ou fala de incerteza do participante sobre a interface ou um termo ("o que é isso?", "não sei se terminou"). O moderador não responde (ver "Ajuda") e a dúvida é registrada com a tela em que ocorreu. |
| Ajuda | Qualquer intervenção do moderador que dá informação sobre a interface, o caminho ou um termo: mostrar onde fica algo, explicar um termo, confirmar se uma ação está certa. Só é dada quando o participante pede ou fica parado sem progresso. Não contam como ajuda: reler o cenário, lembrar de pensar em voz alta e responder "o que você faria se estivesse sozinho?". |
| Abandono | O participante diz que desiste, ou continua sem progresso depois de já ter recebido uma ajuda `[H]`. O moderador encerra a tarefa, registra falha e segue para a próxima atividade. |
| Tempo | Não é medido nas tarefas, por decisão da equipe. Anota-se só o início e o fim de cada sessão, para conferir a duração prevista de até 60 minutos (seção C). |
| Satisfação | Não há escala de satisfação, por decisão da equipe. O que o participante diz na conversa pós-teste sobre a experiência é registrado como fala e codificado como as demais. |
| Codificação de observações e falas | As falas são anotadas como foram ditas. Depois de cada sessão, moderador e anotador classificam, cada um sozinho, cada fala e observação por meta (MQ01 a MQ07) e por tipo: compreensão correta, dúvida, erro de interpretação ou comentário sobre a interface. As diferenças são discutidas até chegarem a um código comum; se não houver acordo, registram-se os dois. Nos documentos, as falas aparecem só com o código do participante. |
| Priorização dos problemas | Problema é cada dificuldade observada no teste ou violação encontrada na inspeção da Entrega 13, juntando os duplicados. Cada problema recebe severidade de 0 a 4 (escala de Nielsen), considerando a frequência (quantos participantes ou avaliadores o encontraram), o impacto (impediu a tarefa ou levou a erro?) e a persistência (acontece toda vez?). Problema que causou falha ou erro crítico recebe pelo menos 3. A ordem de correção é: severidade, depois tarefas da P01, persona prioritária, e depois frequência. |
| Comparação com as metas | Cada pergunta da seção B recebe "atingida" ou "não atingida" por participante, com a evidência (trecho da planilha, fala ou captura). Na UT02, os dois casos (U01 e U02) são relatados separadamente. As perguntas QA09 a QA13 são atingidas se, depois da consolidação da Entrega 13, não restar violação de severidade 3 ou 4. Resultados de participante aproximado (seção C) são relatados à parte. Com um participante por perfil, cada resultado é lido como um caso, sem generalizar para a equipe Baja. |
| Apresentação | Na Entrega 14: uma tabela com as perguntas QA01 a QA13 e o resultado de cada participante; uma tabela de problemas com severidade, tela, evidência e mudança proposta. A mudança de cada problema prioritário é registrada na coluna "Decisão/melhoria" da `RASTREABILIDADE.md`, §3, e, se vier do fluxo, volta ao MoLIC (Entrega 10) e ao modelo conceitual (Entrega 9). |

## Checklist

- [x] As seis etapas DECIDE foram contextualizadas, não apenas expandidas por sigla. 
- [x] Perguntas de avaliação têm método e evidência correspondentes. 
- [x] O plano distingue avaliação de IHC de avaliação técnica/científica do TCC. 
- [x] Dados ou processamentos simulados no protótipo estão declarados. 
- [x] Tarefas vêm de objetivos/cenários relevantes. 
- [x] Critérios de sucesso foram definidos antes da coleta. 
- [x] Questões práticas e éticas estão resolvidas. 
- [ ] Instrumentos estão prontos antes da Entrega 13/14.
- [x] Plano diz como dados serão analisados e apresentados. *(Seção F.)*
