# Entrega 12 — Planejamento da avaliação de usabilidade (DECIDE)

**Data:** 16/11/2026 (início)  
**Status:** 🟨 em andamento  
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

A avaliação investiga a **qualidade da interação** com a interface implementada na Entrega 11: se P01 (Rafael), P02 (Andreia) e P03 (Larissa) conseguem executar, interpretar, comparar e registrar conclusões nas tarefas T01–T08 com eficácia, eficiência e satisfação (Entrega 8, §2 e §3). Ela **não** avalia a validade científica do TCC nem o desempenho dos modelos FCN e DeepLabV3+: IoU, acurácia e tempo de inferência são resultados técnicos do TCC e aparecem no teste como material da tarefa, não como objeto de avaliação.

| Camada | Entra na avaliação? | Como aparece no plano |
|---|---|---|
| Interação com a interface: enviar as entradas e escolher as configurações (TL03), acompanhar o processamento (TL04), ler a máscara e a legenda e registrar a avaliação da imagem (TL05), comparar na mesma imagem (TL06), ler o desempenho consolidado e a diferença entre configurações (TL07), registrar a conclusão (TL08) e a decisão (TL09), consultar os termos (TL10), configurar e acompanhar o treino (TL01, TL02) | Sim | Sucesso, tempo, erros, pedidos de ajuda e satisfação nas tarefas de teste (MU01–MU11) e inspeção das telas na Entrega 13 |
| Compreensão dos resultados técnicos: o que a máscara mostra, por que uma foto de campo não tem métricas, o que cada métrica indica e não indica, se a segmentação indica segurança do trajeto | Sim | Falas, observação e questionário de compreensão (MQ01–MQ03, MU04, MU08) |
| Valor das métricas e desempenho dos modelos: qual configuração tem o maior IoU, se FCN ou DeepLabV3+ é melhor, quão boa é a segmentação das fotos | Não; a leitura que a pessoa faz das métricas entra (linha anterior) | O desempenho é avaliado no TCC, pelo conjunto de teste. No teste com usuários, o sucesso não depende de qual configuração o participante escolhe, e sim de a escolha citar a configuração, a entrada e a métrica corretas e de a decisão continuar sendo da pessoa (MQ07, RQ08) |
| Duração do processamento e do treino | Não; a forma como a interface comunica a espera entra (estado, progresso e fila na TL04 e na TL02; MQ04) | A duração depende do equipamento e não muda com o design; é descontada dos tempos de interação (MU06) |
| Tela de apoio Datasets (TL11), fora dos MoLIC e sem tarefa de usuário (Entrega 11) | Só na inspeção | Entra na avaliação heurística da Entrega 13, que percorre todas as telas e estados; não entra no teste com usuários |

Perguntas que orientam a avaliação (as perguntas detalhadas, com método, evidência e critério, estão na seção B):

- O analista (P01) entende o que a máscara mostra e consegue apontar onde o modelo errou, separando problema da foto e problema do modelo? (MQ01; RQ05)
- Diante de uma foto de campo, ele entende por que não há IoU e avalia visualmente, sem concluir que o trecho é seguro? (MQ02; RQ06)
- Durante a segmentação, a pessoa sabe sempre em que estado está cada configuração? (MQ04; RQ01)
- Ao comparar duas configurações na mesma foto, a pessoa sabe a que configuração e a que foto cada resultado se refere? (MQ05; RQ02, RQ03)
- A gestora (P03) entende o que a diferença entre configurações indica e prepara a recomendação sem atribuir a escolha ao sistema? (MQ03, MQ07; RQ07, RQ08)
- A pesquisadora (P02) define uma configuração de treino entendendo cada parâmetro e, ao voltar, sabe como o treino está? (MQ06; a forma de avaliar a T08 é definida na seção D)

### Dados usados na avaliação

Nenhuma parte da avaliação é simulada. A interface roda sobre uma cópia completa dos dados do TCC, e as métricas exibidas são os resultados reais no conjunto de teste. As imagens de campo são fotos reais dos testes da equipe Baja. A falha na execução não será provocada no teste com usuários; por isso, a recuperação de falha (MU05) é avaliada só na inspeção heurística da Entrega 13 (`PENDENCIAS.md`, INC-71).

## A. Método DECIDE

| Etapa | Aplicação no projeto |
|---|---|
| **D — Determine the goals** | **Objetivo geral:** verificar se a interface implementada na Entrega 11 permite que P01 (Rafael), P02 (Andreia) e P03 (Larissa) façam as tarefas T01–T08 com eficácia, eficiência e satisfação, e encontrar os problemas que impedem isso, para corrigi-los no protótipo (Entrega 8, §4).<br>**Objetivos específicos**, ligados às metas da Entrega 8: (1) compreensão do resultado e dos seus limites: máscara, legenda, estado "sem métricas" e o que a segmentação não indica (MQ01, MQ02, MU04, MU08); (2) execução e acompanhamento da segmentação com sensação de controle (MQ04, MU01, MU07); (3) comparação na mesma imagem sem perder a referência de configuração e entrada (MQ05, MU02); (4) leitura das métricas e preparo da recomendação, com a decisão continuando com a pessoa (MQ03, MQ07, MU03); (5) definição e acompanhamento do treino (MQ06, MU11, conforme a tarefa da seção D); (6) eficiência e satisfação com a interface como um todo (MU06, MU09, MU10).<br>A recuperação de falha (MU05) é verificada só na inspeção (ver "Dados usados na avaliação"). |
| **E — Explore the questions** | As perguntas partem das metas da Entrega 8 e das rupturas previstas nos MoLIC da Entrega 10.<br>**No teste com usuários:** as seis perguntas de "O que está sendo avaliado" (compreensão da máscara, estado "sem métricas", estado da execução, comparação na mesma imagem, leitura da diferença entre configurações e treino).<br>**Na inspeção:** a interface mostra o estado do sistema, previne e explica os erros previstos (formato não aceito, nome repetido, conjuntos de teste diferentes, configuração sem avaliação no conjunto de teste, condição obrigatória) e usa os mesmos termos em todas as telas? Os critérios de acessibilidade que a Entrega 11 deixou para conferir (percurso de cada tarefa só com teclado, leitor de tela e ampliação de 200%) são atendidos?<br>Na seção B, cada pergunta vira um item QA com método, evidência e critério. |
| **C — Choose the evaluation paradigm and techniques** | Dois métodos complementares.<br>**Inspeção (Entrega 13):** avaliação heurística com as 10 heurísticas de Nielsen, feita por cada integrante sozinho, em todas as telas e estados TL01–TL11, com a verificação dos critérios da WCAG 2.2 AA da Entrega 8, §2. Não depende de recrutar participantes, encontra problemas que podem ser corrigidos antes do teste e cobre os estados que o teste não vai provocar, como a falha na execução. Como o avaliador não é o usuário, ela não mostra se a pessoa entende a máscara ou se atribui a escolha ao sistema.<br>**Observação de usuários (Entrega 14):** teste de usabilidade em laboratório, com as tarefas da seção D, protocolo de pensar em voz alta `[H]` e registro de sucesso, tempo, erros e pedidos de ajuda; pergunta de facilidade após cada tarefa (MU09), questionário de compreensão (MU08), SUS ao final (MU10) e conversa curta pós-teste. É o método que verifica as metas de compreensão e satisfação (MQ01–MQ07).<br>O estudo de campo à beira da pista fica fora, porque esse contexto ainda é `[?]` (Entrega 8, §1). |
| **I — Identify the practical issues** | **Participantes:** 3, o mesmo número de integrantes, membros da equipe Baja FEI que não são autores deste projeto nem do TCC (Entrega 8, §3.2; Entrega 7, exclusão dos autores). Perfis e critérios na seção C.<br>**Recrutamento:** convite pelos mesmos canais da Entrega 7 `[H]`; participação voluntária.<br>**Ambiente e equipamento:** presencial, no laboratório da FEI, contexto prioritário da análise (Entrega 8, §2), no computador que executa os modelos, com a interface aberta sobre a cópia completa dos dados do TCC.<br>**Responsáveis:** em cada sessão, um integrante modera e outro anota; cada integrante modera ao menos uma sessão.<br>**Piloto:** antes da Entrega 14, com uma pessoa que não conta na amostra (pode ser um integrante, conforme a Entrega 14). Valida o roteiro, as instruções, a duração e o preparo da cópia dos dados, e recalibra os tempos da MU06.<br>**Cronograma:** Entrega 13, correção dos problemas prioritários, piloto e Entrega 14, nessa ordem; datas `[?]`.<br>**Riscos técnicos:** com a cópia completa, segmentar e treinar com o ResNet152 leva tempo e pode alongar a sessão, por isso cada tarefa usa poucas fotos e a duração do treino é tratada na seção D; fechar o programa interrompe treino e execução, por isso o computador fica dedicado à sessão; a falta de memória no treino não pode ser provocada no equipamento (Entrega 11). |
| **D — Decide how to deal with ethical issues** | **Base:** atividade de ensino, sem finalidade de pesquisa científica; não é registrada no sistema CEP/Conep (Resolução CNS 510/2016, art. 1º, parágrafo único), mas segue os mesmos princípios e a LGPD (Lei 13.709/2018), como na Entrega 7.<br>**Consentimento:** termo adaptado do modelo da disciplina, lido e aceito antes da sessão, com objetivo, duração, registros e contato (e-mails institucionais dos três responsáveis, os mesmos da Entrega 7).<br>**Abertura da sessão:** quem está sendo avaliada é a interface, não a pessoa; ela pode parar a qualquer momento, pular uma tarefa e pedir a exclusão dos seus dados até o fim do semestre letivo.<br>**Registros:** gravação da tela da interface e do áudio só com autorização no termo `[H]`; sem vídeo do rosto; sem autorização, só anotações.<br>**Anonimização:** códigos U01 a U03 nos documentos; a lista que liga código e nome fica fora do repositório. Como a equipe é pequena, o desempenho de cada participante não é repassado à liderança nem à coordenação da equipe Baja.<br>**Imagens dos testes:** só fotos sem pessoas reconhecíveis ou com autorização de quem aparece nelas (Entrega 8, §2).<br>**Armazenamento e descarte:** registros brutos em uma pasta privada dos três autores, fora do repositório; gravações apagadas depois da análise; anotações e lista de códigos apagadas ao fim do semestre letivo. |
| **E — Evaluate, interpret and present the data** | **Inspeção:** cada avaliador registra o local, a heurística, a evidência (captura), a severidade (0 a 4, escala de Nielsen) e a recomendação; a equipe junta os problemas duplicados sem apagar quem encontrou cada um.<br>**Teste:** sucesso, tempo, erros e pedidos de ajuda registrados por participante e por tarefa na planilha de observação; falas codificadas pelas metas MQ01–MQ07. Cada meta MU é comparada ao valor da Entrega 8 (atingida ou não atingida), e cada meta MQ recebe as evidências observadas.<br>**Interpretação:** com 3 participantes, os números não têm valor estatístico; servem para comparar com as metas e apontar problemas, não para generalizar. Os problemas são priorizados pela severidade e pela frequência (quantos participantes ou avaliadores os encontraram).<br>**Apresentação:** na Entrega 14, uma tabela por meta e uma por problema, com a mudança proposta para cada problema prioritário, registrada na coluna "Decisão/melhoria" da `RASTREABILIDADE.md`, §3 (Entrega 8, §4). Os critérios detalhados estão na seção F. |

## B. Perguntas de avaliação

| ID | Pergunta | Método | Métrica/evidência | Critério esperado |
|---|---|---|---|---|
| QA01 | {{usuários completam T01 sem ajuda?}} | observação | sucesso, ajuda, erro | {{MU01}} |
| QA02 | {{há problemas de feedback?}} | heurística | violações H1 | {{...}} |

## C. Escopo e participantes

| Item | Planejamento |
|---|---|
| Perfis | {{...}} |
| Critérios de inclusão/exclusão | {{...}} |
| Nº de participantes | {{...}} |
| Ambiente | presencial/remoto/campo/laboratório |
| Dispositivo | {{...}} |
| Protótipo/versão | {{...}} |
| Teste piloto | {{quem, quando, o que validar}} |

## D. Lista de tarefas de avaliação

| ID | Cenário neutro entregue ao usuário | Objetivo oculto da avaliação | Critério de sucesso | Tempo-limite (se houver) |
|---|---|---|---|---|
| UT01 | {{...}} | {{T01/O01}} | {{...}} | {{...}} |

> Uma boa instrução descreve o objetivo do participante sem dizer **onde clicar** ou usar o rótulo exato do controle que está sendo testado.

## E. Instrumentos

- [Modelo de termo de consentimento](../instrumentos/termo_consentimento_modelo.md)
- [Roteiro de teste](../instrumentos/roteiro_teste_usabilidade.md)
- [Planilha de observação](../instrumentos/planilha_observacao_modelo.md)
- [Formulário de avaliação heurística](../instrumentos/formulario_heuristica_modelo.md)
- {{questionário pré/pós-teste}}

## F. Plano de análise

Defina antes dos testes:

- sucesso total / parcial / falha;
- o que conta como erro, dúvida, ajuda e abandono;
- como tempo será medido;
- escala de satisfação pós-tarefa;
- como observações/falas serão codificadas;
- como problemas serão priorizados;
- como comparar resultados às metas de usabilidade.

## Checklist

- [ ] As seis etapas DECIDE foram contextualizadas, não apenas expandidas por sigla.
- [ ] Perguntas de avaliação têm método e evidência correspondentes.
- [ ] O plano distingue avaliação de IHC de avaliação técnica/científica do TCC.
- [ ] Dados ou processamentos simulados no protótipo estão declarados.
- [ ] Tarefas vêm de objetivos/cenários relevantes.
- [ ] Critérios de sucesso foram definidos antes da coleta.
- [ ] Questões práticas e éticas estão resolvidas.
- [ ] Instrumentos estão prontos antes da Entrega 13/14.
- [ ] Plano diz como dados serão analisados e apresentados.
