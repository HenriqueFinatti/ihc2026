# Entrega 12 — Planejamento da avaliação de usabilidade (DECIDE)

**Data:** 16/11/2026 (início) · 20/11/2026 (conclusão; revisão após feedback)  
**Status:** 🟦 revisada após feedback  
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
| Interação com a interface: enviar as entradas e escolher as configurações (TL03), acompanhar o processamento (TL04), ler a máscara e a legenda e registrar a avaliação da imagem (TL05), comparar na mesma imagem (TL06), ler o desempenho consolidado e a diferença entre configurações (TL07), registrar a conclusão (TL08) e a decisão (TL09), consultar os termos (TL10), configurar e acompanhar o treino (TL01, TL02) | Sim | Sucesso, erros e pedidos de ajuda nas tarefas de teste (MU01–MU04, MU07, MU08 e MU11), facilidade percebida depois de cada tarefa e satisfação geral (MU09 e MU10) e inspeção das telas na Entrega 13, que verifica também a MU05 |
| Compreensão dos resultados técnicos: o que a máscara mostra, por que uma foto de campo não tem métricas, o que cada métrica indica e não indica, se a segmentação indica segurança do trajeto | Sim | Falas, observação e questionário de compreensão (MQ01–MQ03, MU04, MU08) |
| Valor das métricas e desempenho dos modelos: qual configuração tem o maior IoU, se FCN ou DeepLabV3+ é melhor, quão boa é a segmentação das fotos | Não; a leitura que a pessoa faz das métricas entra (linha anterior) | O desempenho é avaliado no TCC, pelo conjunto de teste. No teste com usuários, o sucesso não depende de qual configuração o participante escolhe, e sim de a escolha citar a configuração, a entrada e a métrica corretas e de a decisão continuar sendo da pessoa (MQ07, RQ08) |
| Duração do processamento e do treino | Não; a forma como a interface comunica a espera entra (estado, progresso e fila na TL04 e na TL02; MQ04) | A duração depende do equipamento e não muda com o design; não é medida no teste |
| Preparação dos dados na tela Datasets (TL11), a conversa O11 do M03 (Entrega 10 revista), sem tarefa de teste | Só na inspeção | Entra na avaliação heurística da Entrega 13, que percorre todas as telas e estados; não entra no teste com usuários, porque a preparação dos dados é feita antes de cada sessão (E.6) |

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
| **D — Determine the goals** | **Objetivo geral:** verificar se a interface implementada na Entrega 11 permite que P01 (Rafael), P02 (Andreia) e P03 (Larissa) façam as tarefas T01–T08 com eficácia e compreensão do que veem, e encontrar os problemas que impedem isso, para corrigi-los no protótipo (Entrega 8, §4).<br>**Objetivos específicos**, ligados às metas da Entrega 8: (1) compreensão do resultado e dos seus limites: máscara, legenda, estado "sem métricas" e o que a segmentação não indica (MQ01, MQ02, MU04, MU08); (2) execução e acompanhamento da segmentação com sensação de controle (MQ04, MU01); (3) comparação na mesma imagem sem perder a referência de configuração e entrada (MQ05, MU02); (4) leitura das métricas e preparo da recomendação, com a decisão continuando com a pessoa (MQ03, MQ07, MU03); (5) definição e acompanhamento do treino (MQ06, MU11, conforme a tarefa da seção D); (6) ajuda necessária, facilidade percebida e satisfação com a interface (MU07, MU09 e MU10).<br>A recuperação de falha na execução (MU05 e parte da MQ04) e a falta de memória no treino (parte da MQ06 e da MU11) são verificadas só na inspeção (ver "Dados usados na avaliação"). |
| **E — Explore the questions** | As perguntas partem das metas da Entrega 8 e das rupturas previstas nos MoLIC da Entrega 10.<br>**No teste com usuários:** as seis perguntas de "O que está sendo avaliado" (compreensão da máscara, estado "sem métricas", estado da execução, comparação na mesma imagem, leitura da diferença entre configurações e treino) e quanta ajuda cada participante precisou e como avalia a facilidade das tarefas e a interface.<br>**Na inspeção:** a interface mostra o estado do sistema, previne e explica os erros previstos (formato não aceito, nome repetido, conjuntos de teste diferentes, configuração sem avaliação no conjunto de teste, condição obrigatória) e usa os mesmos termos em todas as telas? Os critérios de acessibilidade que a Entrega 11 deixou para conferir (percurso de cada tarefa só com teclado, leitor de tela e ampliação de 200%) são atendidos?<br>Na seção B, cada pergunta vira um item QA com método, evidência e critério. |
| **C — Choose the evaluation paradigm and techniques** | Dois métodos complementares.<br>**Inspeção (Entrega 13):** avaliação heurística com as 10 heurísticas de Nielsen, feita por cada integrante sozinho, em todas as telas e estados TL01–TL11, com a verificação dos critérios da WCAG 2.2 AA da Entrega 8, §2. Não depende de recrutar participantes, encontra problemas que podem ser corrigidos antes do teste e cobre os estados que o teste não vai provocar, como a falha na execução. Como o avaliador não é o usuário, ela não mostra se a pessoa entende a máscara ou se atribui a escolha ao sistema.<br>**Observação de usuários (Entrega 14):** teste de usabilidade em laboratório, com as tarefas da seção D, protocolo de pensar em voz alta `[H]` e registro de sucesso, erros e pedidos de ajuda (MU07); escala de facilidade de 1 a 7 e pergunta aberta depois de cada tarefa (MU09); questionário de compreensão (MU08); conversa curta pós-teste; e SUS ao final (MU10). É o método que verifica as metas qualitativas de compreensão e de controle da decisão (MQ01–MQ07).<br>O estudo de campo à beira da pista fica fora, porque esse contexto ainda é `[?]` (Entrega 8, §1). |
| **I — Identify the practical issues** | **Participantes:** 3, o mesmo número de integrantes, membros da equipe Baja FEI que não são autores deste projeto nem do TCC (Entrega 8, §3.2; Entrega 7, exclusão dos autores) ou, se faltar alguém de um perfil, o participante aproximado previsto na seção C. Perfis e critérios na seção C.<br>**Recrutamento:** convite pelos mesmos canais da Entrega 7 `[H]`; participação voluntária.<br>**Ambiente e equipamento:** presencial, no laboratório da FEI, contexto prioritário da análise (Entrega 8, §2), no computador que executa os modelos, com a interface aberta sobre a cópia completa dos dados do TCC; configuração do computador, tela e navegador na tabela "Cronograma, equipamento e responsáveis" (seção C).<br>**Responsáveis:** em cada sessão, um integrante modera e outro anota, nunca a mesma pessoa; cada integrante modera uma sessão, e ninguém modera a sessão da persona que escreveu (seção C).<br>**Piloto:** em duas passagens, uma técnica, com um integrante, e outra de compreensão, com uma pessoa de fora do projeto (seção C).<br>**Cronograma:** Entrega 13, correção dos problemas de severidade 3 ou 4 com novo commit, piloto técnico, piloto de compreensão e Entrega 14, nessa ordem; datas na seção C. A coleta não começa enquanto houver campo `[?]` nessa tabela (`PENDENCIAS.md`, INC-76).<br>**Riscos técnicos:** com a cópia completa, segmentar e treinar com o ResNet152 leva tempo e pode alongar a sessão, por isso cada tarefa usa poucas fotos e a duração do treino é tratada na seção D; fechar o programa interrompe treino e execução, por isso o computador fica dedicado à sessão; a espera do processamento é tratada como pausa técnica, sem contar como dificuldade de interação (E.2); a falta de memória no treino não pode ser provocada no equipamento (Entrega 11). |
| **D — Decide how to deal with ethical issues** | **Base:** atividade de ensino, sem finalidade de pesquisa científica; não é registrada no sistema CEP/Conep (Resolução CNS 510/2016, art. 1º, parágrafo único), mas segue os mesmos princípios e a LGPD (Lei 13.709/2018), como na Entrega 7.<br>**Consentimento:** termo adaptado do modelo da disciplina, lido e aceito antes da sessão, com objetivo, duração, registros e contato (e-mails institucionais dos três responsáveis, os mesmos da Entrega 7).<br>**Abertura da sessão:** quem está sendo avaliada é a interface, não a pessoa; ela pode parar a qualquer momento, pular uma tarefa e pedir a exclusão dos seus dados até o fim do semestre letivo.<br>**Registros:** gravação da tela da interface e do áudio só com autorização no termo `[H]`; sem vídeo do rosto; sem autorização, só anotações.<br>**Anonimização:** códigos U01 a U03 nos documentos; a lista que liga código e nome fica fora do repositório. Como a equipe é pequena, o desempenho de cada participante não é repassado à liderança nem à coordenação da equipe Baja.<br>**Imagens dos testes:** só fotos sem pessoas reconhecíveis ou com autorização de quem aparece nelas (Entrega 8, §2).<br>**Armazenamento e descarte:** registros brutos em uma pasta privada dos três autores, fora do repositório; gravações apagadas depois da análise; anotações e lista de códigos apagadas ao fim do semestre letivo. |
| **E — Evaluate, interpret and present the data** | **Inspeção:** cada avaliador registra, no formulário E.5, o local, a condição, a heurística, a consequência, a evidência (captura), a severidade (0 a 4, escala de Nielsen) e a recomendação; a equipe junta os problemas duplicados sem apagar quem encontrou cada um nem a severidade que cada avaliador deu.<br>**Teste:** sucesso, erros, ajudas, facilidade percebida e falas registrados por participante e por tarefa na planilha de observação (E.3); falas codificadas pelas metas MQ01–MQ07; SUS pontuado para cada participante. Cada meta MU é comparada ao critério da seção B (atingida ou não atingida), e cada meta MQ recebe as evidências observadas.<br>**Interpretação:** com 3 participantes, os números não têm valor estatístico; servem para comparar com as metas e apontar problemas, não para generalizar. A ausência de problemas encontrados não comprova alta usabilidade: indica só que o estudo, com esse escopo e esses participantes, não revelou outros problemas. Os problemas são priorizados pela severidade e pela frequência (quantos participantes ou avaliadores os encontraram).<br>**Apresentação:** na Entrega 14, uma tabela com o resultado de cada pergunta da seção B e uma por problema, com a mudança proposta para cada problema prioritário, registrada na coluna "Decisão/melhoria" da `RASTREABILIDADE.md`, §3 (Entrega 8, §4). Os critérios detalhados estão na seção F. |

## B. Perguntas de avaliação

Cada pergunta só usa evidência de quem tem o perfil da persona da tarefa. No teste com usuários há um participante por perfil: U01 (perfil P01) faz a UT01 e a UT02; U02 (perfil P02) faz a UT02 e a UT04; U03 (perfil P03) faz a UT03 (tarefas na seção D; perfis e participante aproximado na seção C). Por isso os critérios valem para cada participante e são lidos caso a caso, sem pretensão de generalizar. As perguntas QA09 a QA13 são respondidas só pela inspeção da Entrega 13. A QA14 vale para os três participantes.

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
| QA14 | Quanta ajuda cada participante precisou, e como ele avalia a facilidade de cada tarefa e a interface como um todo? | Observação, escala pós-tarefa e SUS (UT01 a UT04; U01, U02 e U03) | Ajudas solicitadas e oferecidas por tarefa; nota de 1 a 7 e comentário depois de cada tarefa; pontuação do SUS | Para cada participante: no máximo uma ajuda por tarefa (MU07); nota de pelo menos 5 em cada tarefa (MU09); SUS de pelo menos 68 (MU10) |
| QA13 | A interface atende aos critérios de acessibilidade da Entrega 8, incluindo os que a Entrega 11 deixou para conferir? | Inspeção (WCAG 2.2 AA, Entrega 13) | Percurso da UT01 à UT04 só com teclado; uso com leitor de tela; ampliação de 200% | Todos os cinco pontos prioritários da Entrega 8, §2, atendidos |

## C. Escopo e participantes

| Item | Planejamento |
|---|---|
| Perfis | Os mesmos perfis principais da coleta da Entrega 7, um para cada persona:<br>**U01 — perfil P01 (Rafael):** integrante da equipe Baja FEI que analisa os resultados da segmentação depois dos testes (Entrega 7, A02). Faz a UT01 e a UT02.<br>**U02 — perfil P02 (Andreia):** pessoa que define configurações e treina modelos de visão computacional ligados à Baja FEI (Entrega 7, A03). Faz a UT02 e a UT04.<br>**U03 — perfil P03 (Larissa):** integrante que prepara ou toma a decisão sobre a configuração usada nos testes (Entrega 7, A01). Faz a UT03. |
| Critérios de inclusão/exclusão | **Inclusão**, os mesmos critérios da Entrega 7: U01 executou ou analisou resultados de segmentação no último semestre; U02 definiu ou acompanhou o treino de pelo menos um modelo de visão computacional no último ano; U03 participou de pelo menos uma escolha de configuração de modelo no último semestre. Todos têm 18 anos ou mais e aceitam o termo de consentimento.<br>**Exclusão:** autores deste projeto e do TCC (as respostas deles confirmariam as próprias hipóteses, Entrega 7); quem participou do teste piloto; quem já usou a interface da Entrega 11 `[H]`. Ter participado da coleta da Entrega 7 não exclui `[H]`.<br>**Se faltar alguém do perfil:** entra o participante aproximado (proxy) que a Entrega 7 previu para o mesmo perfil: P01, aluno de Ciência da Computação da FEI com experiência em visão computacional fora da Baja; P02, pesquisador de visão computacional da FEI fora da Baja; P03, ex-integrante que exerceu esse papel ou gestor de outra equipe de competição da FEI. O proxy é registrado como limitação na Entrega 14 e seu resultado é lido separadamente. Um participante de outro perfil nunca substitui o perfil que falta. |
| Nº de participantes | 3, o mesmo número de integrantes (Entrega 14), um por perfil. A UT02 tem dois casos (U01 e U02); a UT01, a UT03 e a UT04 têm um caso cada. As pessoas dos pilotos não contam. Se for possível recrutar mais de uma pessoa por perfil, a repetição aumenta a confiança nos resultados; cada pessoa continua sendo lida como um caso. |
| Ambiente | Presencial, no laboratório da FEI, que é o contexto prioritário da análise (Entrega 8, §2), em uma sala sem interrupções `[H]`. Em cada sessão, um integrante modera e outro anota. Duração prevista de até 60 minutos por sessão `[H]`, conferida no piloto. |
| Dispositivo | O computador que executa os modelos, com mouse e teclado, e a interface aberta no navegador desse computador, em endereço local e sem internet (Entrega 8, §1; Entrega 11, "Como executar"). A interface roda sobre a cópia completa dos dados do TCC, e o computador fica dedicado à sessão. Configuração do computador, tela e navegador: tabela "Cronograma, equipamento e responsáveis", abaixo. |
| Protótipo/versão | Interface implementada na Entrega 11: repositório https://github.com/HenriqueFinatti/Segmentacao-Semantica-Off-Road, ramo `interface`, commit `16a5bc1` (20/11/2026), mostrado no rodapé de cada tela; é a mesma versão inspecionada na Entrega 13. As três sessões usam a mesma versão. Se problemas da Entrega 13 forem corrigidos antes do teste, o novo commit é registrado na tabela abaixo e na Entrega 14. O estado inicial da interface em cada tarefa é definido na seção D e conferido na folha de preparação (E.6). |
| Teste piloto | **Duas passagens, depois das correções da Entrega 13 e antes da primeira sessão da Entrega 14.**<br>**1. Piloto técnico**, com um integrante que não modera essa passagem: confere a gravação, a preparação dos dados e do estado inicial (E.6), a duração da sessão e o tempo do treino rápido da UT04. Como o integrante conhece os conceitos, os fluxos e os rótulos da interface, ele não serve para conferir se os cenários e as perguntas são compreendidos; essa limitação é registrada na Entrega 14.<br>**2. Piloto de compreensão**, com uma pessoa de fora do projeto que não conhece a interface, de preferência próxima de um dos perfis (por exemplo, um aluno de Ciência da Computação da FEI com experiência em visão computacional fora da Baja `[H]`): confere se as instruções da UT01 à UT04, o questionário de compreensão (E.4) e as perguntas pós-tarefa são entendidos sem dizer onde clicar.<br>Pessoas e datas: tabela abaixo. As respostas dos pilotos não entram na análise, e as mudanças feitas depois deles são registradas na Entrega 14 (passo 4). |

### Cronograma, equipamento e responsáveis

Os campos `[?]` são preenchidos antes do piloto técnico (`PENDENCIAS.md`, INC-76); a coleta não começa enquanto algum deles estiver em aberto. Na distribuição das sessões, ninguém modera a sessão da persona que escreveu, para não conduzir o participante para o fluxo que imaginou `[H]`.

| Item | Definição | Data |
|---|---|---|
| Inspeção individual (Entrega 13) | AV01 Henrique, AV02 Tiago e AV03 Mateus, cada um sozinho, com o formulário E.5 | `[?]` |
| Consolidação e correção dos problemas de severidade 3 ou 4 | Equipe; o novo commit é registrado nesta tabela e na Entrega 14 | `[?]` |
| Piloto técnico | Integrante: `[?]`; moderador da passagem: `[?]` | `[?]` |
| Piloto de compreensão | Pessoa de fora do projeto, que não conhece a interface: `[?]` (perfil mais próximo: `[?]`) | `[?]` |
| Sessão do U01 (perfil P01) | Moderador: Henrique; anotador: Mateus `[H]` | `[?]` |
| Sessão do U02 (perfil P02) | Moderador: Tiago; anotador: Henrique `[H]` | `[?]` |
| Sessão do U03 (perfil P03) | Moderador: Mateus; anotador: Tiago `[H]` | `[?]` |
| Computador | Processador gráfico: `[?]`; memória: `[?]`; sistema operacional: `[?]` | — |
| Tela e navegador | Tamanho e resolução da tela: `[?]`; navegador e versão: `[?]` | — |
| Versão da interface | Commit `16a5bc1`; depois das correções da Entrega 13: `[?]` | — |
| Treino rápido da UT04 | DeepLabV3+, só o Freiburg Forest; épocas: `[?]`; batch size: `[?]`; demais parâmetros no valor padrão; duração medida no piloto técnico: `[?]` | — |

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

Na UT04, o treino roda no mesmo processador gráfico que a execução da segmentação; por isso a UT02 vem antes da UT04 na sessão do U02. Os parâmetros do treino rápido e a sua duração no computador da sessão são definidos no piloto técnico (tabela "Cronograma, equipamento e responsáveis", seção C).

## E. Instrumentos

Os instrumentos foram adaptados dos modelos da disciplina em `instrumentos/` e estão completos nesta seção.

| Instrumento | Para quê | Quando | Modelo de origem |
|---|---|---|---|
| E.1 Convite e termo de consentimento | Convidar e registrar o consentimento de U01 a U03 e das pessoas dos pilotos | Antes da sessão | [Modelo de termo de consentimento](../instrumentos/termo_consentimento_modelo.md) e termo da I01 (Entrega 7) |
| E.2 Roteiro do moderador | Abertura, perfil pré-teste, pensar em voz alta, aplicação das tarefas, regras de intervenção e de pausa técnica, perguntas pós-tarefa, conversa pós-teste e SUS | Durante a sessão | [Roteiro de teste](../instrumentos/roteiro_teste_usabilidade.md) |
| E.3 Planilha de observação | Registrar sucesso, erros, ajudas, dúvidas, falas, pausas técnicas, facilidade e SUS por participante e tarefa (QA01 a QA08 e QA14) | Durante a sessão | [Planilha de observação](../instrumentos/planilha_observacao_modelo.md) |
| E.4 Questionário de compreensão | Verificar a MU08, em duas versões: U01 e U03 (QA03 e QA06), com gabarito e regra de pontuação | Depois da UT01 (U01) e da UT03 (U03) | Meta MU08 (Entrega 8, §3.2) |
| E.5 Formulário de avaliação heurística | Registrar a inspeção de cada integrante, os percursos de acessibilidade e a consolidação, e responder às QA09 a QA13 | Entrega 13 | [Formulário de avaliação heurística](../instrumentos/formulario_heuristica_modelo.md) |
| E.6 Folha de preparação da sessão | Conferir a versão, os dados, as configurações, os arquivos e o estado inicial antes de cada sessão | Antes de cada sessão (e dos pilotos) | Roteiro de teste, item "Antes da sessão" |

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

### E.2 Roteiro do moderador

**Papéis:** o moderador conduz a sessão e só diz o que está neste roteiro; o anotador preenche a planilha de observação (E.3) e não fala com o participante. A mesma pessoa nunca modera e anota a mesma sessão (quem faz cada papel está em "Cronograma, equipamento e responsáveis", na seção C).

#### 1. Antes da sessão, sem o participante

- Conferir a folha de preparação da sessão (E.6): versão da interface no rodapé, cópia dos dados, estado inicial da tarefa e arquivos na pasta.
- Testar a gravação da tela e do áudio.
- Abrir a planilha de observação (E.3) com o código do participante e separar as cópias impressas dos cenários (seção D), do questionário de compreensão da versão certa (E.4) e do SUS (item 8 deste roteiro).
- Fechar no computador tudo o que não faz parte do teste.

#### 2. Abertura (ler para o participante)

> "Obrigado por vir. Hoje vamos testar uma interface para analisar a segmentação das imagens dos testes do Baja. Quem está sendo avaliada é a interface, não você: se algo for difícil, é um problema da interface, e é isso que queremos descobrir. Não estamos avaliando os modelos de segmentação nem se os resultados deles são bons. As imagens e os números que você vai ver são reais, dos dados do TCC e dos testes da equipe. Vou pedir algumas atividades parecidas com o trabalho da equipe. Enquanto faz, fale em voz alta o que está pensando, o que procura e o que espera que aconteça. Durante as atividades, vou evitar responder perguntas sobre a interface, porque quero ver como seria se você estivesse sozinho(a); no fim, respondo tudo. Você pode parar a qualquer momento ou pular uma atividade."

Em seguida, entregar o termo (E.1), esperar a leitura, tirar dúvidas e registrar o aceite e a escolha sobre a gravação. Sem aceite, a sessão não começa.

#### 3. Perfil pré-teste (perguntar e anotar na planilha)

| # | Pergunta | Para quê |
|---|---|---|
| P1 | Qual é o seu papel na equipe Baja hoje e há quanto tempo? (Para quem não é da equipe: qual é a sua experiência com visão computacional?) | Confirmar o perfil (U01, U02 ou U03) ou registrar o participante aproximado |
| P2 | No último semestre, você executou ou analisou resultados de segmentação? Treinou algum modelo? Participou de uma escolha de configuração para os testes? | Conferir o critério de inclusão do perfil (seção C) |
| P3 | Você já usou esta interface antes? | Critério de exclusão |
| P4 | Que ferramentas você costuma usar para analisar imagens ou resultados (por exemplo, scripts, planilhas, notebooks)? | Contexto para interpretar as dificuldades |
| P5 | Há alguma necessidade de acessibilidade que devamos considerar, como ampliar a tela? | Ajustar o ambiente; não é usada para excluir ninguém |

Se a resposta à P2 não corresponder ao perfil previsto, o participante é registrado como aproximado (proxy), e o resultado dele é lido à parte (seção C).

#### 4. Pensar em voz alta (ler antes da primeira atividade)

> "Lembre-se de ir falando o que está pensando, mesmo que pareça óbvio. Se você ficar em silêncio por um tempo, eu só vou lembrar você de falar."

#### 5. Atividades

O moderador lê o cenário da seção D em voz alta, entrega a cópia impressa (com as palavras entre colchetes já preenchidas na folha de preparação, E.6) e o anotador marca o início.

| Tarefa | Participante | O moderador pode | O moderador não diz |
|---|---|---|---|
| UT01 | U01 | Reler o cenário; dizer em que pasta estão as fotos | Nomes de menus, botões ou telas (por exemplo, "Segmentar imagens", "Sessão atual"); o que é *Trilha*; que a foto não tem métricas |
| UT02 | U01 e U02 | Reler o cenário; dizer qual é "a foto que deixou dúvida", se o participante perguntar | Onde comparar; qual configuração escolher |
| UT03 | U03 | Reler o cenário; dizer qual é o ciclo de testes | O que é IoU; qual configuração indicar; se a diferença é grande ou pequena |
| UT04, parte 1 | U02 | Reler o cenário; confirmar que "teste rápido" é um treino que termina durante a sessão | Quantas épocas usar; onde fica o treino |
| UT04, parte 2 | U02 | Reler o cenário | Onde ver o estado do treino; o que é early stopping |

**Regras de intervenção** (definições de ajuda, dúvida e abandono na seção F):

- Durante a tarefa, não responder perguntas sobre a interface. Podem ser ditas, e não contam como ajuda: a releitura do cenário; "Continue falando o que está pensando"; "O que você faria se estivesse sozinho(a)?".
- Dar ajuda só quando o participante pedir ou ficar parado sem progresso por cerca de 2 minutos `[H]`. A ajuda é a menor possível (dizer em que parte da tela procurar, e não o que clicar). O anotador registra se ela foi **solicitada** pelo participante ou **oferecida** pelo moderador.
- Se, depois de uma ajuda, o participante continuar sem progresso, encerrar a tarefa como abandono e seguir para a próxima atividade.
- Não corrigir erros nem confirmar se uma ação está certa.

**Pausa técnica:** enquanto a segmentação, a avaliação no conjunto de teste ou o treino processam, a espera é do sistema, e não do participante. O moderador diz: "Enquanto processa, pode comentar o que está vendo ou o que espera". O anotador registra o início e o fim da pausa técnica, e a espera não conta como hesitação nem como dificuldade. Se a espera passar de 10 minutos `[H]`, o moderador interrompe a tarefa, segue para a parte seguinte da sessão (questionário ou conversa) e volta à tarefa quando o processamento terminar. Na UT04, a espera do treino é preenchida pela conversa pós-teste, como prevê a ordem da sessão (seção D).

#### 6. Depois de cada tarefa

1. "De 1 a 7, em que 1 é muito difícil e 7 é muito fácil, quão fácil foi fazer esta atividade?" (MU09)
2. "O que tornou esta atividade fácil ou difícil?"

Na UT04, as duas perguntas vêm depois da parte 2.

#### 7. Questionário de compreensão

O U01 responde depois da UT01, e o U03, depois da UT03 (E.4). O moderador entrega a versão impressa; o participante responde por escrito, com a interface aberta na última tela da tarefa, e o moderador não comenta as respostas.

#### 8. Conversa pós-teste e SUS

| # | Pergunta | Participantes | Meta |
|---|---|---|---|
| C1 | Se você precisasse fazer isso de novo na semana que vem, sozinho(a), como seria? | U01, U02, U03 | MQ04 |
| C2 | Teve algum momento em que você não soube o que o sistema estava fazendo? Qual? | U01, U02, U03 | MQ04, MQ06 |
| C3 | Como você explicaria à equipe a conclusão que registrou? | U01, U02 | MQ05 |
| C4 | Como você explicaria à coordenação a recomendação que registrou? Como foi a escolha da configuração que você indicou? | U03 | MQ03, MQ07 |
| C5 | Como seria, no seu dia a dia, deixar um treino rodando e voltar depois? | U02 | MQ06 |
| C6 | O que você mudaria na interface? | U01, U02, U03 | — |

Por fim, o participante responde ao SUS (*System Usability Scale*; Brooke, 1996) sobre a interface como um todo (MU10), marcando cada afirmação de 1 (discordo totalmente) a 5 (concordo totalmente). Os itens abaixo são uma tradução da equipe:

1. Eu acho que gostaria de usar este sistema com frequência.
2. Eu achei o sistema desnecessariamente complexo.
3. Eu achei o sistema fácil de usar.
4. Eu acho que precisaria da ajuda de uma pessoa com conhecimentos técnicos para usar o sistema.
5. Eu achei que as várias funções do sistema estão bem integradas.
6. Eu achei que o sistema apresenta muita inconsistência.
7. Eu imagino que a maioria das pessoas aprenderia a usar este sistema rapidamente.
8. Eu achei o sistema muito complicado de usar.
9. Eu me senti muito confiante usando o sistema.
10. Eu precisei aprender várias coisas antes de conseguir usar o sistema.

**Pontuação:** nos itens ímpares, nota − 1; nos pares, 5 − nota; a soma é multiplicada por 2,5, resultando em um valor de 0 a 100.

#### 9. Encerramento

- Responder às dúvidas que ficaram; agora o moderador pode explicar a interface.
- Lembrar como os dados serão usados, a anonimização e o direito de pedir a exclusão (E.1).
- Agradecer.
- Depois que o participante sai: salvar a gravação e a planilha com o código, restaurar a cópia dos dados para a sessão seguinte (E.6) e codificar as falas, moderador e anotador cada um sozinho (seção F).

### E.3 Planilha de observação

Uma planilha por sessão. O anotador preenche o registro de eventos durante a sessão e o resumo ao fim de cada tarefa; as definições de cada tipo de evento estão na seção F.

**Cabeçalho**

| Campo | Registro |
|---|---|
| Participante | U0__ · perfil P0__ · participante real ou aproximado (se aproximado, qual) |
| Data, início e fim da sessão | |
| Moderador e anotador | |
| Versão da interface (rodapé) | commit ________ |
| Gravação autorizada? | sim / não |
| Perfil pré-teste (P1 a P5) | resumo, sem nome |

**Registro de eventos** (uma linha por evento, na ordem em que acontecem)

| Minuto da gravação | Tarefa | Tela (TL) | Tipo | Descrição ou fala literal | Meta / QA | Evidência |
|---|---|---|---|---|---|---|
| | | | | | | |

Tipos de evento: erro de execução; erro de interpretação; erro crítico (um dos três da MU04); erro percebido e corrigido pelo participante; dúvida; ajuda solicitada; ajuda oferecida; releitura do cenário ou lembrete (não é ajuda); pausa técnica (início e fim); fala relevante; compreensão correta.

**Resumo por tarefa**

| Tarefa | Itens do critério de sucesso cumpridos (seção D) | Resultado (total, parcial, falha ou abandono) | Erros de execução / de interpretação | Erros críticos | Ajudas solicitadas / oferecidas (MU07) | Pausas técnicas (min) | Facilidade de 1 a 7 (MU09) | O que tornou fácil ou difícil | QA atingida? |
|---|---|---|---|---|---|---|---|---|---|
| UT01 | | | | | | | | | |
| UT02 | | | | | | | | | |
| UT03 | | | | | | | | | |
| UT04 | | | | | | | | | |

**Questionário, SUS e conversa**

| Item | Registro |
|---|---|
| Questionário de compreensão (versão U01 ou U03) | ___ de 4 acertos (E.4), nota do moderador e do anotador |
| SUS (MU10) | respostas dos 10 itens e pontuação de 0 a 100 |
| Conversa pós-teste (C1 a C6) | respostas resumidas, com as falas literais relevantes |

**Codificação depois da sessão** (seção F)

| Fala ou observação | Código do moderador | Código do anotador | Código comum (ou os dois, se não houver acordo) |
|---|---|---|---|
| | | | |

### E.4 Questionários de compreensão

As perguntas são abertas, respondidas por escrito e com as próprias palavras; não há alternativas, para não ensinar a resposta. Cada pergunta vale 1 ponto quando a resposta contém a ideia central do gabarito; resposta parcial, em branco ou "não sei" vale 0. Moderador e anotador pontuam separadamente e discutem as divergências; sem acordo, vale a menor nota, e a divergência é registrada. O gabarito não é mostrado ao participante. Meta: pelo menos 3 de 4 acertos para cada um (MU08).

**Versão do U01** (QA03; depois da UT01, com a última foto analisada na tela)

| # | Pergunta | Ideia central esperada (gabarito) |
|---|---|---|
| 1 | Nesta tela, o que significa a área marcada como *Trilha*? | É a região que o modelo classificou como trilha; é a classificação do modelo, e não uma confirmação de que ali há trilha |
| 2 | Por que esta foto não mostra IoU nem acurácia? | Porque é uma foto de campo, sem a marcação correta de referência; as métricas só são calculadas no conjunto de teste, e a foto é avaliada visualmente |
| 3 | Numa foto duvidosa, como você diferencia um problema da foto de um problema do modelo? Dê um exemplo. | Problema da foto: a captura atrapalha (sol contra a câmera, desfoque, poeira). Problema do modelo: a foto está boa, mas a máscara erra a trilha (por exemplo, sombra marcada como *Fora da trilha*) |
| 4 | O resultado desta foto permite dizer que o trecho é seguro para o veículo passar? Por quê? | Não; a segmentação só separa *Trilha* de *Fora da trilha* e não avalia segurança nem se o trecho é transitável |

**Versão do U03** (QA06; depois da UT03, com o desempenho consolidado na tela)

| # | Pergunta | Ideia central esperada (gabarito) |
|---|---|---|
| 1 | O que o IoU médio de uma configuração indica, e o que ele não mostra? | Indica quanto as regiões marcadas coincidem com a referência no conjunto de teste, em média (acerto geral); não mostra em que tipo de trecho a configuração erra |
| 2 | De onde vem o valor de referência mostrado ao lado das métricas? Ele é uma recomendação? | São as métricas da configuração em uso (a última executada); é um ponto de comparação, e não uma recomendação |
| 3 | A diferença de IoU médio entre as configurações desta comparação basta para dizer que uma é melhor? Quem decide isso? | Não necessariamente: a diferença sozinha não mostra onde cada uma erra; quem julga se ela importa é a pessoa (e a equipe), e não o sistema |
| 4 | Essas métricas valem para as fotos dos testes de campo da Baja? Elas garantem que o trajeto é seguro? | Não: foram calculadas no conjunto de teste do TCC, e nenhuma métrica garante a segurança do trajeto |

### E.5 Formulário de avaliação heurística

O formulário é o modelo de cada avaliador na Entrega 13, que já traz estes campos. Cada avaliador preenche o seu sozinho, sem conhecer os achados dos outros; a consolidação só começa quando os três terminam.

**Cabeçalho:** avaliador (AV01 a AV03); data; versão (commit no rodapé); computador, tela, resolução e navegador (os da tabela "Cronograma, equipamento e responsáveis"); tempo gasto na inspeção.

**Telas e estados examinados:** cada estado listado na Entrega 13 (seção 2, "Telas/estados"), da TL01 à TL11, é marcado como examinado ou não, com o motivo quando não for examinado. A falta de memória no treino não pode ser provocada no equipamento: é examinada pela mensagem implementada (Entrega 11) e marcada como "examinada sem reproduzir". Os estados de falha na execução, de treino interrompido e da tela Datasets (TL11) são obrigatórios.

**Matriz de cobertura:**

| Heurística | Telas e estados examinados | Houve violação? | IDs dos achados | Exemplo de boa prática, se não houve violação |
|---|---|---|---|---|

**Violações:**

| ID | Heurística | Tela/estado | Ação ou condição | Problema observado | Consequência para quem usa | Evidência (captura) | Severidade (0–4) | Justificativa da severidade | Recomendação |
|---|---|---|---|---|---|---|---:|---|---|

**Percursos de acessibilidade** (os sete percursos da Entrega 11, "Percursos completos a confirmar"):

| Percurso | Só com teclado: concluído? Onde parou? | Foco visível e na ordem da tela? | Ampliação de 200%: conteúdo legível, sem rolagem horizontal? | Leitor de tela: anuncia estados e mensagens? | IDs das violações |
|---|---|---|---|---|---|

**Consolidação da equipe:** cada problema consolidado (HC01…) preserva os achados individuais, citados como "V01 (AV02)", e a heurística e a severidade dadas por cada avaliador antes da discussão. A severidade final é decidida em consenso; quando não houver acordo sobre a heurística ou a severidade, as posições ficam registradas lado a lado. As perguntas QA09 a QA13 são respondidas a partir da consolidação: QA09, pelas violações de H1 e H9 nos estados de falha da TL02, da TL04 e da TL11; QA10, pelas de H5 e H9 nos erros previstos; QA11, pelas de H2, H4 e H10; QA12, pelas de H2 e H3 na TL07, na TL08 e na TL09; QA13, pelos percursos de acessibilidade.

### E.6 Folha de preparação da sessão

Preenchida e conferida pelo moderador antes de cada sessão, na própria interface e sobre a cópia completa dos dados do TCC.

| Item | U01 | U02 | U03 | Conferido |
|---|---|---|---|---|
| Versão da interface (rodapé) | `16a5bc1`, ou o commit registrado depois das correções da Entrega 13 | igual ao U01 | igual ao U01 | |
| Cópia dos dados | restaurada antes da sessão, para que um participante não veja o que o anterior registrou | igual | igual | |
| Dados de treino e de teste (O11) | dataset montado; configurações do TCC avaliadas no conjunto de teste atual | igual, com o Freiburg Forest disponível para a UT04 | igual | |
| Configurações | as do TCC, uma delas em uso: `[?]` | a configuração em uso e a "outra configuração" da UT02: `[?]` | FCN e DeepLabV3+ executadas no ciclo e avaliadas no mesmo conjunto de teste, uma delas em uso: `[?]` | |
| Ciclo de testes | nome a informar na UT01: `[?]` | ciclo da sessão já criada: `[?]` | ciclo com as duas execuções: `[?]` | |
| Arquivos | pasta com 3 fotos reais de campo, sem pessoas reconhecíveis, em que a configuração em uso erra visivelmente em ao menos uma: `[?]` | as mesmas fotos, já na sessão | — | |
| Estado inicial | nenhuma sessão aberta | sessão com as fotos executadas pela configuração em uso e avaliações registradas, com a foto da UT02 marcada como duvidosa; nenhum treino em andamento; fila vazia | nenhuma recomendação registrada | |
| Palavras entre colchetes dos cenários (seção D) | `[?]` | `[?]` | `[?]` | |
| Gravação de tela e áudio testada | | | | |
| Cenários, questionário, escala pós-tarefa e SUS impressos | | | | |
| Outros programas fechados; computador dedicado à sessão | | | | |

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
| Ajuda | Qualquer intervenção do moderador que dá informação sobre a interface, o caminho ou um termo: mostrar onde fica algo, explicar um termo, confirmar se uma ação está certa. Só é dada quando o participante pede ou fica parado sem progresso (E.2). É registrada como **solicitada** (o participante pediu) ou **oferecida** (o moderador interveio), e a contagem por tarefa é a MU07. Não contam como ajuda, e são registrados à parte: reler o cenário, lembrar de pensar em voz alta e responder "o que você faria se estivesse sozinho?". |
| Abandono | O participante diz que desiste, ou continua sem progresso depois de já ter recebido uma ajuda `[H]`. O moderador encerra a tarefa, registra falha e segue para a próxima atividade. |
| Tempo | Não é medido nas tarefas: o tempo é dominado pelo processamento e pelo treino, que dependem do computador (Entrega 8, §3.2: MU06 retirada). Anota-se o início e o fim de cada sessão, para conferir a duração prevista de até 60 minutos (seção C), e o início e o fim de cada pausa técnica. |
| Pausa técnica | Espera enquanto a segmentação, a avaliação no conjunto de teste ou o treino processam. Não conta como hesitação, dificuldade ou abandono; o que o participante diz durante a espera é registrado como fala (E.2). |
| Satisfação | Depois de cada tarefa, nota de 1 (muito difícil) a 7 (muito fácil) e a pergunta "O que tornou esta atividade fácil ou difícil?" (MU09); no fim da sessão, o SUS (Brooke, 1996), pontuado de 0 a 100 (MU10). O limite de 68 é a média de referência do SUS relatada por Sauro (2011), adotada pela equipe como critério, e não uma fronteira universal entre interface boa e ruim. Com um participante por perfil, cada nota é relatada individualmente, sem médias. O que o participante diz na conversa pós-teste também é codificado como fala. |
| Codificação de observações e falas | As falas são anotadas como foram ditas. Depois de cada sessão, moderador e anotador classificam, cada um sozinho, cada fala e observação por meta (MQ01 a MQ07) e por tipo: compreensão correta, dúvida, erro de interpretação ou comentário sobre a interface. As diferenças são discutidas até chegarem a um código comum; se não houver acordo, registram-se os dois. Nos documentos, as falas aparecem só com o código do participante. |
| Priorização dos problemas | Problema é cada dificuldade observada no teste ou violação encontrada na inspeção da Entrega 13, juntando os duplicados. Cada problema recebe severidade de 0 a 4 (escala de Nielsen), considerando a frequência (quantos participantes ou avaliadores o encontraram), o impacto (impediu a tarefa ou levou a erro?) e a persistência (acontece toda vez?). Problema que causou falha ou erro crítico recebe pelo menos 3. A ordem de correção é: severidade, depois tarefas da P01, persona prioritária, e depois frequência. |
| Comparação com as metas | Cada pergunta da seção B recebe "atingida" ou "não atingida" por participante, com a evidência (trecho da planilha, fala ou captura). Na UT02, os dois casos (U01 e U02) são relatados separadamente. As perguntas QA09 a QA13 são atingidas se, depois da consolidação da Entrega 13, não restar violação de severidade 3 ou 4. Resultados de participante aproximado (seção C) são relatados à parte. Com um participante por perfil, cada resultado é lido como um caso, sem generalizar para a equipe Baja: escreve-se "o participante U01 concluiu a tarefa nas condições avaliadas", e não "os usuários do perfil P01 conseguem". |
| Apresentação | Na Entrega 14: uma tabela com as perguntas QA01 a QA14 e o resultado de cada participante; uma tabela de problemas com severidade, tela, evidência e mudança proposta. A mudança de cada problema prioritário é registrada na coluna "Decisão/melhoria" da `RASTREABILIDADE.md`, §3, e, se vier do fluxo, volta ao MoLIC (Entrega 10) e ao modelo conceitual (Entrega 9). |
| Consolidação heurística | Cada avaliador termina a inspeção individual antes da reunião de consenso. A consolidação preserva os achados individuais, com a heurística e a severidade dadas por cada um; quando não houver acordo sobre a heurística ou a severidade, as posições ficam registradas lado a lado (E.5). |

## Checklist

- [x] As seis etapas DECIDE foram contextualizadas, não apenas expandidas por sigla. 
- [x] Perguntas de avaliação têm método e evidência correspondentes. 
- [x] O plano distingue avaliação de IHC de avaliação técnica/científica do TCC. 
- [x] Dados ou processamentos simulados no protótipo estão declarados. *(Nada é simulado: "Dados usados na avaliação".)* 
- [x] Tarefas vêm de objetivos/cenários relevantes. 
- [x] Critérios de sucesso foram definidos antes da coleta. 
- [x] Questões práticas e éticas estão resolvidas. 
- [x] Instrumentos estão prontos antes da Entrega 13/14. *(E.1 a E.6, nesta seção; os campos `[?]` de cronograma e equipamento são preenchidos antes do piloto técnico, INC-76.)*
- [x] Plano diz como dados serão analisados e apresentados. *(Seção F.)*

## Histórico de revisões

| Data | O que mudou | Motivo |
|---|---|---|
| 20/11/2026 | Aplicação do parecer da Entrega 12. **Instrumentos:** roteiro do moderador (E.2), planilha de observação (E.3), questionários de compreensão do U01 e do U03 com gabarito e pontuação (E.4), formulário heurístico com cobertura de estados, condição, consequência, acessibilidade e consolidação (E.5) e nova folha de preparação da sessão (E.6). **Metas:** MU07 (ajudas por tarefa), MU09 (facilidade de 1 a 7 depois de cada tarefa) e MU10 (SUS) voltam a ser verificadas, na nova QA14; o tempo (MU06) continua fora. **Questões práticas:** versão `16a5bc1`; tabela de cronograma, equipamento e responsáveis, com os campos ainda `[?]` (INC-76); piloto em duas passagens, técnica e de compreensão; pausa técnica. **Análise:** relato caso a caso, ausência de problemas não comprova alta usabilidade, ajuda solicitada × oferecida e consolidação heurística com as posições individuais. Preparação dos dados (TL11) como conversa O11 do M03 | Feedback do professor sobre a Entrega 12 (`PENDENCIAS.md`: INC-73 e INC-75) |
