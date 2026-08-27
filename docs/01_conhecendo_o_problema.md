# Entrega 1 — Conhecendo o projeto, o usuário e o problema

**Data:** {{17/08/2026}}
**Status:** 🟨 em andamento
**Responsabilidade:** 1 solução consolidada por equipe

## Objetivo da atividade

Reinterpretar o tema do TCC sob a perspectiva de Interação Humano-Computador e construir um **entendimento comum entre os integrantes da equipe**.

A disciplina utiliza preferencialmente o tema do TCC para os exercícios de IHC. Isso vale tanto para TCCs que já preveem uma interface quanto para trabalhos cujo resultado principal é algoritmo, modelo, API, biblioteca, análise de dados, infraestrutura, estudo experimental ou outro artefato técnico.

> **Importante:** a interface projetada na disciplina é um artefato de aprendizagem de IHC. Ela **não se torna automaticamente uma obrigação do TCC**. Sua incorporação ao trabalho de conclusão depende de decisão da equipe e do orientador.

Antes de preencher, leia [`../GUIA_ESCOPO_IHC.md`](../GUIA_ESCOPO_IHC.md).

Nesta primeira semana a equipe **não deve começar desenhando telas**. Primeiro deverá compreender:

- o que o TCC realmente produz;
- quem poderia obter valor dessa contribuição;
- quais pessoas interagem, administram, configuram, interpretam ou são afetadas;
- o que essas pessoas precisam alcançar;
- como atividades relacionadas acontecem hoje;
- problemas, limitações e contexto;
- alternativas existentes;
- qual recorte de interação fará sentido para a disciplina.

Ao final desta entrega, a equipe deve diferenciar:

- **tema do TCC** × **escopo formal do TCC** × **escopo de IHC da disciplina**;
- **objetivo do projeto** × **objetivo do usuário**;
- **problema do usuário** × **solução tecnológica**;
- **fato conhecido** × **hipótese** × **lacuna de conhecimento**;
- **capacidade técnica** × **forma de uso dessa capacidade**;
- **funcionalidade** × **atividade/resultado que o usuário precisa alcançar**;
- **usuário direto** × **stakeholders**.

---

## Como classificar as respostas

Sempre que a resposta fizer uma afirmação sobre usuários, problemas, atividades, necessidades, contexto ou mercado, use:

- **[F] Fato conhecido** — existe evidência/fonte.
- **[H] Hipótese** — afirmação plausível que ainda precisa ser investigada.
- **[?] Não sabemos ainda** — lacuna relevante.

Quando usar `[F]`, informe a origem. Hipóteses prioritárias devem receber IDs (`H01`, `H02`...) e também ser registradas em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

> **Exemplo:** `[H] H01 — DBAs considerariam útil comparar automaticamente o plano atual de execução com uma recomendação produzida pelo algoritmo.`

Uma hipótese explicitada é melhor do que uma suposição escondida.

---

# 0. Identificação do TCC e da equipe

## 0.1 Membros

| Nome completo | Matrícula | GitHub | Responsabilidade principal |
|---|---:|---|---|
| Henrique Finatti Silveira Belo Trebbi | 22.123.030-3 | [@HenriqueFinatti](https://github.com/HenriqueFinatti) |  |
| Mateus Marana Assuena | 22.123.026-1 | [@MatMarana](https://github.com/MatMarana) |  |
| Tiago Fagundes dos Santos | 22.123.017-0 |[@TiagoFagundes19](https://github.com/TiagoFagundes19) | |

## 0.2 Título atual do TCC

Segmentação Semântica em Vias Off-Road

## 0.3 Orientador(a)

Isaac Jesus

## 0.4 Qual é o resultado principal atualmente previsto no TCC?

Marque e descreva:

- [x] sistema/aplicação interativa;
- [ ] algoritmo;
- [x] modelo de IA/ML/LLM;
- [ ] biblioteca/API/framework;
- [ ] análise de dataset;
- [x] estudo/benchmark/avaliação experimental;
- [ ] infraestrutura/backend;
- [ ] componente embarcado/IoT;
- [ ] outro: {{...}}.

**Descrição:** {{...}}

## 0.5 O TCC já previa desenvolvimento de interface com usuário?

- [x] Sim, a interface já faz parte do TCC.
- [ ] Parcialmente; existe alguma interação, mas ainda não está bem definida.
- [ ] Não. O TCC é predominantemente técnico e não previa interface.

**Explique o que está formalmente previsto no TCC:** {{...}}

> Esta resposta serve para separar o compromisso do TCC do projeto da disciplina. Mesmo quando a opção for **não**, a equipe irá definir uma interface para exercitar IHC.

---

# 1. Entendendo a contribuição do projeto

## 1.1 Explique o TCC em uma frase, sem citar linguagem de programação, framework ou banco de dados.

Segmentar caminhos em vias não urbanas.

## 1.2 Qual situação, atividade ou problema do mundo real motivou o TCC?

O desenvolvimento de um carro autônomo pra equipe do Baja Fei

[F]

## 1.3 Qual é a **capacidade/contribuição central** produzida pelo TCC?

Segmentar imagens; comparar modelos; analisar resultados

## 1.4 O que se espera que esteja diferente **para pessoas, organizações ou processos** se essa contribuição for bem-sucedida?
disponibilidade da análise da rota segmentada por diferentes modelos e suas respectivas métricas.

[H]

## 1.5 O que é mérito técnico/científico do TCC e o que seria uma possível aplicação prática?

| Mérito/contribuição técnica | Possível aplicação/valor em uso |
| Modelo de IA para segmentação semântica| Apoiar sistemas de percepção de veículos autônomos em ambientes off-road|
| Métricas de desempenho dos modelos | Facilitar a comparação entre modelos e a compreensão da qualidade das segmentações   |
| Visualização dos resultados da segmentação | Tornar mais fácil para os estudantes do Baja FEI analisar e validar os resultados gerados pelo modelo |

---

# 2. Entendendo as pessoas envolvidas

## 2.1 Quem interage diretamente com o produto, se já existe interface prevista?

Estudantes do projeto Baja FEI

[F]

## 2.2 Quem poderia **usar, configurar, administrar, operar, interpretar ou tomar decisões** a partir da contribuição técnica?

Considere perfis profissionais e stakeholders, não apenas consumidores finais.

| Perfil | Relação com a contribuição | O que faria | Status/evidência |
|---|---|---|---|
| Equipe do Baja | Interpretar | Utilizaria a segmentação e as análises para melhores resultados nas competições | F |
| Equipe do Baja | Usar | Produção do Baja autônomo | F |
|  Analista | analisar e comparar | Comparar os resultados da segmentação com outros modelos | H |
|  Empresas do agro | analisar e comparar | Utilizar a segmentação para desenvolver robôs off-road autônomos | F |

## 2.3 Existem pessoas afetadas que não usariam a interface diretamente?

| Stakeholder | Como é afetado | Usa interface? | Status/evidência |
|---|---|---|---|
| Mecânicos do Baja | utilizar a segmentação para desenvolver o carro autônomo | não | F |
| Pilotos do Baja | utilizar as métricas de análise para melhorar sua performance | não | H |

## 2.4 Que características desses perfis podem influenciar a interação?

Considere conhecimento do domínio, experiência tecnológica, frequência de uso, necessidades de acessibilidade, responsabilidade profissional, familiaridade com métricas, linguagem técnica, urgência etc.

Frequência de uso, responsabilidade profissional e familiaridade com métricas.
[H]

---

# 3. Entendendo objetivos e atividades

## 3.1 O que o usuário está tentando conseguir no mundo real?
<!--Não responda “usar o algoritmo”, “clicar no sistema” ou “ver o dashboard”. -->
No mundo real o usuário tem como objetivo visualizar a via segmentada para futuramente usar a aplicação para desenvolver carros autônomos.

[F]

## 3.2 Quais são as atividades mais importantes?

| ID | Atividade/objetivo | Quem realiza | Frequência/criticidade inicial | Status/evidência |
|---|---|---|---|---|
| A01 | Escolha de imagem ou vídeo para realizar segmentação | Estudantes baja FEI | Conforme a necessidade | [F] |
| A02 | Processamento de imagem ou vídeo | Sistema | Conforme a necessidade | [F] |
| A03 | Analisar e validar resultados | Estudantes baja FEI | Conforme a necessidade | [F] |

## 3.3 Qual atividade parece mais frequente? Por quê?
Ambas atividades possuem a mesma frequência, visto que para cada imagem ou vídeo resultado é necessário que os estudantes analisem os resultados, uma atividade ocorre logo após a outra.
[F]

## 3.4 Qual parece mais crítica? Que consequência existe se for mal executada?
A atividade mais crítica é o processamento das imagens ou dos vídeos, pois é nessa etapa que são gerados os resultados da segmentação semântica. Caso ela seja mal executada, o sistema poderá classificar incorretamente os elementos presentes na via off-road, produzindo resultados imprecisos ou difíceis de interpretar. Consequentemente, a imagem segmentada não agregará valor ao usuário final e poderá comprometer a análise e a tomada de decisões no contexto do projeto Baja FEI.
[F]

---

# 4. Entendendo o problema ou processo atual

## 4.1 Como essas atividades são realizadas hoje, antes da interface imaginada na disciplina?
<!--Pode existir software concorrente, linha de comando, planilha, notebook, script, painel técnico, processo manual, consulta a logs, análise visual, troca de mensagens, decisão por especialista etc.-->
Atualmente, o processamento e a segmentação das imagens são realizados por meio de scripts e ferramentas técnicas, sem uma interface gráfica voltada aos integrantes do Baja FEI. Para executar o modelo e visualizar os resultados, é necessário configurar parâmetros, selecionar arquivos e executar códigos, o que exige conhecimento técnico de programação

[H]

## 4.2 O que é difícil, demorado, confuso, repetitivo, arriscado ou pouco transparente?
O principal problema é a dificuldade enfrentada por pessoas que não conhecem o código ou não possuem conhecimentos técnicos de programação. Sem uma interface gráfica, o processo de selecionar uma imagem ou um vídeo, executar o modelo e visualizar o resultado da segmentação não é intuitivo nem transparente.

[H]

## 4.3 Que informações o profissional precisa interpretar para tomar decisão?
O profissional precisa interpretar o resultado da segmentação, identificando quais regiões da imagem foram classificadas como áreas transitáveis ou não transitáveis pelo veículo.

[F]

## 4.4 O que acontece quando a atividade falha ou quando o resultado é interpretado incorretamente?
Quando o processamento falha ou o resultado é interpretado incorretamente, regiões transitáveis e não transitáveis podem ser identificadas de forma errada. Isso pode levar o usuário a tomar decisões inadequadas sobre o percurso do veículo, além de dificultar a avaliação do modelo.

[F]

## 4.5 Conte uma situação concreta.
<!--Escreva uma pequena narrativa com pessoa, objetivo, atividade, contexto, dificuldade e consequência. **Não descreva ainda a futura solução.** -->
Um integrante da equipe Baja FEI precisa analisar uma imagem de uma via off-road para identificar as regiões transitáveis pelo veículo. Para isso, ele executa o modelo de segmentação por meio de scripts, mas possui pouco conhecimento técnico sobre o código e seus parâmetros. Durante o processo, ocorre uma configuração incorreta, gerando uma segmentação imprecisa. Como o resultado não apresenta informações claras sobre a confiabilidade do processamento, o estudante interpreta algumas áreas não transitáveis como seguras, comprometendo a análise do percurso e a avaliação do desempenho do modelo.

[F]

## 4.6 Que evidência existe hoje?

| Evidência/fonte | O que sustenta | Limitação |
|---|---|---|
| Scripts utilizados atualmente no projeto| Mostram que a execução do modelo exige conhecimento técnico para configurar arquivos, parâmetros e comandos. | Não demonstram diretamente as dificuldades enfrentadas pelos usuários. |
| Observação do processo de segmentação pela equipe| Indica que a execução e a interpretação dos resultados dependem de conhecimentos prévios sobre o modelo. | Baseia-se na experiência da própria equipe e envolve poucos usuários.|

---

# 5. Entendendo o contexto de uso

## 5.1 Onde e em quais situações a interação poderia ocorrer?
A interação poderia ocorrer nos laboratórios FEI ou nas pista off-road da FEI, onde são realizados os testes do veículo. O sistema seria utilizado principalmente para analisar imagens e vídeos capturados durante esses percursos, permitindo que os integrantes da equipe avaliem a segmentação do terreno e identifiquem regiões transitáveis e não transitáveis.

[F]

## 5.2 Em quais dispositivos/equipamentos?
A interação ocorreria principalmente em computadores ou notebooks capazes de executar o software e processar as imagens ou os vídeos. Também seriam utilizadas câmeras instaladas no veículo Baja ou dispositivos móveis para registrar o percurso off-road.
[F]

## 5.3 Existem condições físicas relevantes?
<!--Considere iluminação, ruído, mobilidade, conexão, privacidade, uso compartilhado, interrupções, pressão de tempo etc. -->
Uma boa iluminação se faz necessário para conseguir registrar imagens e videos de ótima qualidade.

[F]

## 5.4 Existem fatores sociais ou organizacionais?
<!--Considere papéis, chefias, equipes, permissões, aprovação, responsabilidade profissional, auditoria, turnos e colaboração. -->
A aplicação poderia ser executada por qualquer membro da equipe Baja FEI.

[H]

## 5.5 Existe necessidade de histórico, rastreabilidade ou auditoria?
Existe a necessidade de manter o histórico das images e vídeos processado, junto com os resultados da segementação, com o objetivo de comparar diferentes registros, assim sendo possivel identificar possíveis falhas e acompanhar a evolução do modelo ao longo dos testes realizados pela equipe Baja FEI.

[H]

## 5.6 Um erro pode produzir consequência relevante? Qual?
Sim, um erro na segmentação pode fazer com que uma região não transitável seja classificada como via para o veículo, isso pode comprometer a análise do percurso, gerar decisões inadequadas pela equipe e prejudicar a avaliação do modelo.

[F]

---

# 6. Entendendo mercado e alternativas existentes

> Nesta entrega faça apenas um **levantamento inicial**. A análise aprofundada ocorre na Entrega 2.

## 6.1 Como pessoas resolvem problemas semelhantes hoje?

| Alternativa atual | Quem usa | Para quê | Status/evidência |
|---|---|---|---|
| Scripts em Python e notebooks | Desenvolvedores e pesquisadores de IA | Executar modelos, processar imagens e visualizar máscaras de segmentação | [F] Processo atualmente utilizado no projeto |
| CVAT | Equipes de visão computacional | Anotar imagens e criar máscaras para treinamento de modelos | [F] Possui ferramentas de anotação por polígonos |
| Roboflow | Desenvolvedores e equipes de visão computacional | Anotar dados, treinar modelos e executar segmentação | [F] Oferece um fluxo para segmentação semântica |
| Supervisely | Pesquisadores e profissionais de visão computacional | Organizar dados, realizar anotações, treinar modelos e analisar resultados | [F] Plataforma voltada a projetos de visão computacional |


## 6.2 Existem produtos que atuam na mesma área, mesmo sem serem equivalentes ao TCC?
Existem produtos relacionados à visão computacional e a segmentação semântica, como os exemplos citados acima. Essas ferramentas permitem realizar atividades como anotação de imagens, organização de conjuntos de dados, treinamento de modelos e visualização de resultados.

[F]

## 6.3 Quais interfaces profissionais esse público já conhece?
<!-Exemplos possíveis: ferramentas de banco, IDEs, consoles de nuvem, dashboards, plataformas de dados, ferramentas de monitoramento, painéis de IA, sistemas administrativos.** -->

Os integrantes do Baja FEI com noções básicas de programação devem estar familiarizados com interfaces como VScode, terminais de linha de comando e GitHub. Também podem conhecer alguns sistemas de telemetria e ferramentas utilizadas para análise de dados e acompanhamento dos testes do veículo.
[H]}

## 6.4 O que essas soluções parecem fazer bem?
As soluções pesquisadas centralizam atividades relacionadas à visão computacional, como envio e organização de imagens, anotação, treinamento e visualização dos resultados.Esses recursos podem facilitar a compreensão dos resultados e reduzir a necessidade de executar comandos manualmente.

[F]

## 6.5 O que parecem fazer mal, dificultar ou não atender?
Por serem ferramentas genéricas e profissionais, essas soluções podem apresentar muitas funcionalidades, configurações e termos técnicos desnecessários para um integrante do Baja FEI que deseja apenas processar uma imagem ou um vídeo e visualizar o resultado

[H]

## 6.6 Que padrões de interface ou vocabulário parecem familiares a esse público?
Alguns padrões que podem ser familiares aos integrantes da equipe são:
- Seleção ou envio de imagens e vídeos
- Botão para iniciar o processamento
- Barra de progresso durante a segmentação
- Comparação entre a imagem original e a imagem segmentada

[H]

---

# 7. Derivando o escopo de IHC da disciplina

## 7.1 Escolha o caminho do projeto

### Caminho A — TCC já possui interface

O recorte da disciplina será o fluxo de envio, processamento e visualização de imagens ou vídeos de vias off-road. O usuário deverá selecionar um arquivo, iniciar a segmentação e visualizar a comparação entre a imagem original e o resultado produzido pelo modelo, com uma legenda indicando as classes identificadas. A interface pretende tornar o processo mais acessível e facilitar a compreensão dos resultados, sem exigir que o usuário interaja diretamente com o código.

### Caminho B — TCC não possui interface prevista

Faça o exercício de transferência de uso:

> **Imagine que o TCC foi concluído com sucesso e uma empresa, laboratório ou organização quer transformar a contribuição em algo utilizável. Quem precisaria interagir com ela e para quê?**

Responda:

1. quem poderia contratar/adotar a solução? A equipe Baja FEI e possíveis grupos de pesquisas em veículos autônomos que realizam testes em ambiente off-road.
2. quem seria o usuário direto? Equipe Baja FEI
3. quem administraria/configuraria? A ideia com a interface também é que além dos desenvolvedores da aplicação, os participantes do Baja FEI com conhecimento de programação também conseguir configurar os diferentes tipos de modelos.
4. quem interpretaria resultados? Integrantes do Baja FEI e grupos de pesquisas para analisar como modelo classificou as diferentes regiões do terreno
5. quem tomaria decisões? Os integrantes do Baja FEI
6. quais dados/entradas seriam necessários? Imagens ou vídeos de vias off-road capturados por câmeras durante os testes do veículo. Também se necessário os usuários poderiam inserir um novo modelo, visto que atualmente temos apenas o DeepLabv3+ e ResNet.
7. quais resultados deveriam ser compreendidos? Os usuários deverão compreender quais regiões foram classificadas como transitáveis ou não transitáveis, além de interpretar a acurácia apresentada pelo modelo.
8. que erros/rupturas seriam possíveis? Poderiam ocorrer envio de arquivos inválidos, formatos não suportados, imagens com baixa qualidade, processamento demorado, interrupção durante a análise ou classificação incorreta do terreno.

## 7.2 Qual perfil será priorizado no projeto de IHC?

O perfil priorizado será o dos integrantes da equipe Baja FEI, pois a proposta inicial do TCC é desenvolver um sistema de segmentação semântica de vias off-road voltado às necessidades da equipe Baja.

## 7.3 Qual objetivo desse usuário será priorizado?

Segmentar a trilha das corridas off-road que eles particibarem.

## 7.4 Que interface será explorada na disciplina?

Complete:

> **Para fins da disciplina de IHC, será projetada uma interface que permita a `{{equipe baja}}` utilizar `{{O modelo e analise de segmentações semânticas}}` para `{{segmentar os caminhos}}`, no contexto de `{{corridas baja}}`.**

## 7.5 Qual é a relação dessa interface com o TCC?

- [X] Já fazia parte do TCC.
- [ ] É um aprofundamento de algo parcialmente previsto.
- [ ] É uma extensão conceitual criada para a disciplina.
- [ ] É um protótipo demonstrativo de aplicação potencial.
- [ ] Outra: {{...}}.

> **Declaração:** a interface desenvolvida nesta disciplina é um artefato de aprendizagem de IHC baseado no tema do TCC. Sua inclusão ou implementação no TCC somente ocorrerá se isso for posteriormente decidido pela equipe e pelo orientador.

---

# 8. Levantando possibilidades de interação — sem desenhar ainda

A equipe pode registrar possibilidades para investigação. **Não significa que todas serão implementadas.**

Marque apenas as que parecem plausíveis e explique o objetivo correspondente.

| Possibilidade | Pode fazer sentido? | Objetivo/tarefa que justificaria | Evidência atual |
|---|---|---|---|
| Dashboard/visão geral | talvez | Comparar o desempenho de diferentes modelos e diferentes treinamentos | {{...}} |
| Configuração/parametrização | talvez | Configurar quais datasets e quais modelos serão usados no treinamento e segmentação | {{...}} |
| Entrada/upload/seleção de dados | sim | Fazer o upload de vídeos a serem treinados | {{...}} |
| Acompanhamento de processamento | sim | Acompanhar o treinamento dos modelos | {{...}} |
| Relatório/resultados | sim | Registrar a métricas do treinamento e da segmentação | {{...}} |
| Histórico com busca/filtros | não | Não há necessidade de busca | {{...}} |
| Comparação de resultados | não | A comparação irá acontecer, mas por parte do usuário, considerando que os resultados dependem do contexto que o usuário estiver | {{...}} |
| Explicabilidade/detalhamento | sim/não/talvez | NÃO ENTENDI| {{...}} |
| Administração/configurações globais | sim/não/talvez | NÃO ENTENDI | {{...}} |
| Usuários/perfis/permissões | não | Não há necessidade de perfis considerando que apenas um software para análise, não vamos guardar informações individuais | {{...}} |
| CRUD de entidade do domínio | não | Não há necessidade de CRUD | {{...}} |
| Auditoria/logs | sim/não/talvez | NÃO ENTENDI | {{...}} |
| Alertas/ocorrências | não | não há necessidade de alertas no uso | {{...}} |
| Ajuda/documentação | talvez | O sistema é simples de usar, mas ter documentação é sempre bom | {{...}} |

> **Atenção:** “login + dashboard + CRUD” não é uma solução universal. Cada padrão deve surgir de uma tarefa real.

---

# 9. Benefícios e ações iniciais

## 9.1 Qual benefício concreto o projeto de IHC pretende oferecer?

| Benefício esperado | Problema/necessidade | Usuário | Status/evidência |
|---|---|---|---|
| Facilitar a execução da segmentação sem exigir interação direta com o código | Atualmente, é necessário executar scripts e possuir conhecimento técnico | Integrantes do Baja FEI | Processo atual do projeto [F] |
|Apresentar o resultado da segmentação de maneira clara e compreensível|Dificuldade para identificar e interpretar as classes do terreno|Integrantes do Baja FEI|Deve ser validado com os usuários [H]|
|Permitir a comparação entre a imagem original e a imagem segmentada|Necessidade de verificar visualmente como o modelo classificou o terreno|Integrantes do Baja FEI e pesquisadores|Levantamento inicial [H]|

## 9.2 Que ações o usuário deverá conseguir realizar?

| ID | O usuário precisa conseguir... | Para alcançar... | Prioridade inicial |
|---|---|---|---|
| F01 | Selecionar e enviar uma imagem ou um vídeo | Inserir o arquivo que será analisado pelo modelo | alta |
| F02 | Iniciar o processamento da imagem ou do vídeo | Gerar o resultado da segmentação sem executar scripts manualmente | alta |
| F03 | Visualizar a imagem original e o resultado segmentado| Comparar a entrada com a classificação produzida pelo modelo | alta |
| F04 | Visualizar informações e métricas do resultado | Avaliar o desempenho e a confiabilidade do modelo | alta |

## 9.3 Tecnologias/restrições já definidas no TCC

A tecnologia aparece **agora**, depois do entendimento do uso.

| Tecnologia/restrição | Por que existe | Possível impacto na interação |
|---|---|---|
| Python | É a linguagem utilizada no desenvolvimento e na execução do modelo | A interface deverá se comunicar com o código responsável pelo processamento |
| DeepLabv3+ | É a arquitetura responsável por realizar a segmentação semântica e classificar cada região da imagem | O processamento pode levar algum tempo, exigindo que a interface apresente um indicador de carregamento e informe quando o resultado estiver pronto |
| ResNet152 | É o backbone utilizado pelo DeepLabv3+ para extrair características das imagens | Pode aumentar o tempo de processamento e o consumo de memória, especialmente em computadores sem GPU |

---

# 10. Hipóteses e dúvidas prioritárias

| ID | Hipótese/dúvida | Por que importa | Como poderá ser investigada |
|---|---|---|---|
| H01 | O que se espera que esteja diferente **para pessoas, organizações ou processos** se essa contribuição for bem-sucedida? | Principal motivo de uso da nossa aplicação | Entrega 4 |
| H02 | Perfil de usuário (Analista) | Precisamos definir quem poderá usar a interface | Entrega 3 | Que características desses perfis podem influenciar a interação?
| H03 | Perfil de usuário (Piloto Baja FEI) | Precisamos definir quem será afetado pela interface sem usá-la interface | Entrega 3 |
| H04 | Que características desses perfis podem influenciar a interação? | Precisamos definir as características dos perfis de usuários que influenciam na interface | Entrega 3 |
| H05 | Como essas atividades são realizadas hoje, antes da interface imaginada na disciplina? | Não sabemos como é realizado as atividades | Entrega 2 |
| H06 | O que é difícil, demorado, confuso, repetitivo, arriscado ou pouco transparente? | Não sabemos cos problemas existentes | Entrega 4 |
| H07 | Existem fatores sociais ou organizacionais? | Pesquisar melhor os fatores sociais e organizacionais | Entrega 7 |
| H08 | Existe necessidade de histórico, rastreabilidade ou auditoria? | Não sabemos se existe a necessidade | Entrega 8 |
| H09 | Quais interfaces profissionais esse público já conhece? | Não temos certeza de quais ferramentas ele já conhecem | Entrega 7 |
| H10 | O que parecem fazer mal, dificultar ou não atender? | Não temos certeza de quais ferramentas ele já conhecem | Entrega 7 |
| H10 | Que padrões de interface ou vocabulário parecem familiares a esse público? | Não conhecemos os familiares desse público | Entrega 7 |
| H11 | Que padrões de interface ou vocabulário parecem familiares a esse público? | Não conhecemos os familiares desse público | Entrega 7 |
| H12 | Qual benefício concreto o projeto de IHC pretende oferecer? | Não sabemos quais os benefícios o projeto pode oferecer| Entrega 13 |

Registre em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

---

# 11. Síntese da equipe

| Pergunta | Síntese atual |
|---|---|
| Qual é a contribuição central do TCC? | Realizar a segmentação semântica de vias off-road por dois modelos e compará-los |
| O TCC já previa interface? | Sim |
| Quem é o usuário prioritário de IHC? | A Equipe do Baja FEI |
| O que ele precisa alcançar? | Precisa realizar a segmentação da via com o modelo selecionado e aprensentar métricas de resultados |
| Qual problema/atividade será estudado? | A segmentação das vias off-road e a comparação entre modelos de segmentação |
| Como isso acontece hoje? | Atráves de scripts python |
| Qual é o contexto de uso? | Carros e robôs autônomos off-road |
| Que interface/recorte será explorado? |  |
| Como a interface se relaciona ao TCC? | Através da seleção de novos vídeos pela equipe do Baja e realizando a segmentação dos mesmos |
| Quais pontos ainda são hipóteses? | {{H01...}} |

### Delimitação

**Dentro do escopo de IHC:** {{...}}
**Fora do escopo de IHC:** {{...}}
**Dentro do escopo formal do TCC:** {{...}}
**Interface da disciplina será implementada no TCC?** não definido / sim / não — {{justificativa, se houver}}

---

# 12. Como esta entrega alimenta as próximas

- **Entrega 2:** verifica mercado, concorrentes e interfaces profissionais representativas.
- **Entrega 3:** detalha perfis e contexto.
- **Entrega 4:** aprofunda situações problemáticas.
- **Entrega 5:** modela tarefas centrais.
- **Entrega 6:** experimenta alternativas em baixa fidelidade.
- **Entrega 7:** investiga hipóteses com dados.
- **Entrega 8:** define restrições e metas de usabilidade.
- **Entregas 9–11:** transformam o recorte em modelo de interação e protótipo.
- **Entregas 12–14:** avaliam a interface construída na disciplina.

A Entrega 1 é uma **fotografia inicial do conhecimento**. Ela pode e deve ser revisada quando surgirem evidências.

---

# 13. Relação com INOVA e comunicação do projeto

Prepare uma explicação de até três frases:

1. **Problema/atividade humana:** {{...}}
2. **Contribuição técnica do TCC:** {{...}}
3. **Como uma pessoa poderia utilizar essa contribuição:** {{...}}

Essa síntese ajuda a apresentar o projeto para público não especializado sem reduzir seu mérito técnico.

---

# Checklist de qualidade

- [X] Está clara a diferença entre tema do TCC, escopo formal do TCC e escopo de IHC.
- [X] A equipe declarou se o TCC já previa interface.
- [ ] Se não previa, foi derivado um usuário plausível e um objetivo de uso.
- [X] A interface de IHC não foi apresentada como obrigação automática do TCC.
- [X] A contribuição do TCC foi descrita sem começar por tecnologias de implementação.
- [X] Usuários diretos e stakeholders foram diferenciados.
- [X] Foram considerados profissionais que configuram, administram, interpretam ou decidem, quando pertinente.
- [X] Objetivo do usuário não foi confundido com objetivo do projeto.
- [X] Processo/problema atual foi descrito antes da solução.
- [X] Existe situação concreta de uso/problema.
- [X] Contexto físico, social/organizacional, dispositivos e consequências de erro foram considerados.
- [X] Mercado/alternativas existentes foram levantados inicialmente.
- [X] Possibilidades como dashboard, relatório, histórico, filtros e CRUD foram tratadas como hipóteses de solução, não como requisitos automáticos.
- [X] Cada possibilidade de interface tem um objetivo/tarefa que poderia justificá-la.
- [X] Afirmações relevantes estão marcadas `[F]`, `[H]` ou `[?]`.
- [ ] Hipóteses prioritárias receberam IDs e foram para a rastreabilidade.
- [X] O recorte de IHC é viável para modelar, prototipar e avaliar no semestre.
- [X] A equipe consegue explicar problema humano → contribuição computacional → forma de uso.
