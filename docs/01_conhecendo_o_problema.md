# Entrega 1 — Conhecendo o projeto, o usuário e o problema

**Data:** 17/08/2026
**Status:** 🟦 revisada após feedback
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

| Nome completo | Matrícula | GitHub |
|---|---:|---|
| Henrique Finatti Silveira Belo Trebbi | 22.123.030-3 | [@HenriqueFinatti](https://github.com/HenriqueFinatti) |
| Mateus Marana Assuena | 22.123.026-1 | [@MatMarana](https://github.com/MatMarana) |
| Tiago Fagundes dos Santos | 22.123.017-0 | [@TiagoFagundes19](https://github.com/TiagoFagundes19) |

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
- [ ] outro.

**Descrição:** O TCC desenvolve um sistema de segmentação semântica que identifica automaticamente, em imagens e vídeos de vias off-road, **a região de trilha** e a separa do restante da cena. A segmentação é **binária**: cada pixel é classificado como *Trilha* (classe `Trail` dos datasets Freiburg Forest e Synthetic Offroad) ou *Fora da trilha*. O sistema compara dois modelos de deep learning, **FCN** e **DeepLabV3+**, ambos com backbone ResNet152, quanto à qualidade da segmentação e ao tempo de inferência. [F] — documento e repositório do TCC.

## 0.5 O TCC já previa desenvolvimento de interface com usuário?

- [x] Sim, a interface já faz parte do TCC.
- [ ] Parcialmente; existe alguma interação, mas ainda não está bem definida.
- [ ] Não. O TCC é predominantemente técnico e não previa interface.

**Explique o que está formalmente previsto no TCC:** O TCC prevê o desenvolvimento de um sistema interativo que permita aos integrantes da equipe Baja FEI selecionar imagens ou vídeos de vias off-road, configurar e treinar os modelos (FCN e DeepLabV3+, ambos com ResNet152), executar a segmentação semântica, visualizar os resultados e comparar o desempenho entre eles. A interface faz parte do escopo formal do TCC como ferramenta de apoio à análise e validação dos resultados da segmentação.

> Esta resposta serve para separar o compromisso do TCC do projeto da disciplina. Mesmo quando a opção for **não**, a equipe irá definir uma interface para exercitar IHC.

---

# 1. Entendendo a contribuição do projeto

## 1.1 Explique o TCC em uma frase, sem citar linguagem de programação, framework ou banco de dados.

Segmentar caminhos em vias não urbanas.

## 1.2 Qual situação, atividade ou problema do mundo real motivou o TCC?

O desenvolvimento de um carro autônomo para a equipe Baja FEI.

[F] — documento do TCC (introdução).

## 1.3 Qual é a **capacidade/contribuição central** produzida pelo TCC?

Segmentar imagens; comparar modelos; analisar resultados

## 1.4 O que se espera que esteja diferente **para pessoas, organizações ou processos** se essa contribuição for bem-sucedida?

Os integrantes da equipe Baja FEI poderão avaliar visualmente a qualidade da segmentação semântica, identificar falhas de classificação em regiões específicas e selecionar a configuração (modelo e parâmetros de treino, §7.1) a usar nos testes do veículo, com base nas métricas do conjunto de teste anotado e na inspeção visual de imagens das pistas, sem depender da execução manual de scripts. Isso permitirá uma decisão mais rápida e fundamentada sobre qual configuração adotar.

[H]

## 1.5 O que é mérito técnico/científico do TCC e o que seria uma possível aplicação prática?

| Mérito/contribuição técnica | Possível aplicação/valor em uso |
|-|-|
| Modelo de IA para segmentação semântica| Apoiar sistemas de percepção de veículos autônomos em ambientes off-road|
| Métricas de desempenho dos modelos | Facilitar a comparação entre modelos e a compreensão da qualidade das segmentações   |
| Visualização dos resultados da segmentação | Tornar mais fácil para os estudantes do Baja FEI analisar e validar os resultados gerados pelo modelo |

---

# 2. Entendendo as pessoas envolvidas

## 2.1 Quem interage diretamente com o produto, se já existe interface prevista?

Integrantes da equipe Baja FEI. No recorte de IHC, o usuário direto priorizado é o analista de segmentação (§7.2).

[F] — documento do TCC: a interface prevista se destina aos integrantes da equipe Baja FEI (§0.5).

## 2.2 Quem poderia **usar, configurar, administrar, operar, interpretar ou tomar decisões** a partir da contribuição técnica?

Considere perfis profissionais e stakeholders, não apenas consumidores finais.

| Perfil | Relação com a contribuição | O que faria | Status/evidência |
|---|---|---|---|
| Analista de segmentação (Baja FEI) | Interpretar | Avaliar a qualidade da segmentação, identificar falhas de classificação e selecionar a configuração a usar nos testes do veículo (§7.3) | H |
| Pesquisador(a) de modelos (Baja FEI / orientação do TCC) | Configurar e experimentar | Definir configurações de treino (§7.1), treinar os modelos e comparar os resultados em imagens e vídeos dos testes. Adicionar novas arquiteturas e ajustar parâmetros internos do treino acontece no código do TCC e fica **fora do recorte de IHC** (§7.1 e Delimitação) | H |
| Gestor de projeto (Baja FEI) | Decidir | Consultar resultados consolidados e decidir qual configuração adotar nos testes do veículo | H |

## 2.3 Existem pessoas afetadas que não usariam a interface diretamente?

| Stakeholder | Como é afetado | Usa interface? | Status/evidência |
|---|---|---|---|
| Pilotos do Baja | Receberiam informações sobre as condições do terreno para planejar estratégias de pilotagem | não (informações indiretas via relatórios) | H |
| Mecânicos do Baja | Receberiam dados sobre o tipo de terreno para ajustes no veículo | não (informações indiretas via equipe técnica) | H |

## 2.4 Que características desses perfis podem influenciar a interação?

**Perfil prioritário: Analista de segmentação (Baja FEI)**
- **Conhecimento do domínio:** Conhece as condições do terreno off-road e as necessidades do projeto Baja, mas pode não possuir conhecimento aprofundado sobre arquiteturas de redes neurais.
- **Conhecimento de programação:** intermediário. Pode programar, mas não atua como desenvolvedor do modelo e prefere interfaces gráficas a executar scripts e comandos no terminal.
- **Frequência de uso:** Utiliza o sistema durante os ciclos de teste do veículo, com necessidade de analisar múltiplas imagens em sequência.
- **Responsabilidade:** Precisa indicar qual configuração utilizar com base na qualidade da segmentação.
- **Conhecimento de segmentação e métricas:** Compreende conceitos básicos de desempenho (acurácia, IoU), mas precisa de orientação para interpretá-los adequadamente. Esse conhecimento é independente do anterior: saber programar não garante interpretar bem o resultado, e é possível interpretar o terreno sem dominar scripts (H02, H04).

[H]

---

# 3. Entendendo objetivos e atividades

## 3.1 O que o usuário está tentando conseguir no mundo real?
<!--Não responda “usar o algoritmo”, “clicar no sistema” ou “ver o dashboard”. -->
No mundo real, o usuário tem como objetivo avaliar a qualidade da segmentação semântica gerada pelo modelo, interpretar a região de trilha delimitada e comparar métricas e resultados entre configurações, para selecionar a configuração a usar nos testes do veículo. As métricas vêm do conjunto de teste anotado; em imagens novas das pistas, a avaliação é visual (§9.2, AC04).

[H]

## 3.2 Quais são as atividades mais importantes?

| ID | Atividade/objetivo | Quem realiza | Frequência/criticidade inicial | Status/evidência |
|---|---|---|---|---|
| A01 | Selecionar e enviar uma imagem ou vídeo para análise | Analista de segmentação | Conforme a necessidade dos testes do Baja · criticidade média: um arquivo errado leva a analisar outra cena | [H] |
| A02 | Iniciar e acompanhar o processamento da segmentação | Analista de segmentação (inicia); Sistema (executa) | Conforme a necessidade dos testes do Baja · criticidade média: o usuário precisa perceber se a execução terminou ou falhou | [H] |
| A03 | Analisar e interpretar os resultados da segmentação | Analista de segmentação | Conforme a necessidade dos testes do Baja · **criticidade alta** (§3.4) | [H] |
| A04 | Comparar resultados entre diferentes modelos ou configurações | Analista de segmentação | Quando é preciso selecionar a configuração · criticidade alta: sustenta a seleção | [H] |
| A05 | Definir uma configuração de treino e treinar o modelo com ela | Pesquisador(a) de modelos (define e inicia); Sistema (treina) | Quando uma nova configuração precisa ser testada · criticidade média: uma configuração mal definida gera resultados que serão comparados depois | [H] |

## 3.3 Qual atividade parece mais frequente? Por quê?
A atividade de análise dos resultados parece ser pelo menos tão frequente quanto a de envio, pois cada imagem enviada gera um resultado que precisa ser interpretado. No entanto, a frequência real depende de fatores como o número de imagens processadas por sessão e se o usuário realiza múltiplas análises da mesma imagem. Essa investigação será aprofundada nas próximas entregas.

[H]

## 3.4 Qual parece mais crítica? Que consequência existe se for mal executada?
A atividade mais crítica parece ser a interpretação dos resultados (A03), pois é nela que o usuário precisa compreender o que as cores e regiões segmentadas significam em relação ao terreno real. Uma interpretação incorreta pode levar à seleção de um modelo inadequado ou a uma leitura equivocada da região de trilha. Diferentemente de falhas técnicas (que impedem o uso) ou dificuldades de interação (que tornam o uso lento), uma interpretação incorreta gera resultados plausíveis mas equivocados, o que é mais difícil de detectar.

[H]

---

# 4. Entendendo o problema ou processo atual

## 4.1 Como essas atividades são realizadas hoje, antes da interface imaginada na disciplina?
<!--Pode existir software concorrente, linha de comando, planilha, notebook, script, painel técnico, processo manual, consulta a logs, análise visual, troca de mensagens, decisão por especialista etc.-->
Atualmente, o processamento e a segmentação das imagens são realizados por meio de scripts e ferramentas técnicas, sem uma interface gráfica voltada aos integrantes do Baja FEI. Para executar o modelo e visualizar os resultados, é necessário configurar parâmetros, selecionar arquivos e executar códigos, o que exige conhecimento técnico de programação.

[F] (observação da equipe sobre o processo atual)

## 4.2 O que é difícil, demorado, confuso, repetitivo, arriscado ou pouco transparente?
O principal problema é a dificuldade enfrentada por pessoas que não conhecem o código ou não possuem conhecimentos técnicos de programação. Sem uma interface gráfica, o processo de selecionar uma imagem ou um vídeo, executar o modelo e visualizar o resultado da segmentação não é intuitivo nem transparente.

[H]

## 4.3 Que informações o profissional precisa interpretar para tomar decisão?
O profissional precisa interpretar as classes apresentadas pela segmentação e as métricas de desempenho para avaliar o resultado do modelo. Esse resultado serve à análise do modelo; ele não autoriza, por si só, uma conclusão operacional sobre a segurança ou a transitabilidade de um trajeto.

[H]

## 4.4 O que acontece quando a atividade falha ou quando o resultado é interpretado incorretamente?
Quando o processamento falha ou o resultado é interpretado incorretamente, a equipe pode comparar configurações com base em uma leitura inadequada ou registrar uma avaliação incorreta do modelo. Isso prejudica a análise e a seleção do modelo, mas não permite concluir que um trajeto é seguro ou inseguro.

[H]

## 4.5 Conte uma situação concreta.
<!--Escreva uma pequena narrativa com pessoa, objetivo, atividade, contexto, dificuldade e consequência. **Não descreva ainda a futura solução.** -->
Um integrante da equipe Baja FEI precisa analisar uma imagem de uma via off-road para avaliar o resultado de uma segmentação. Para isso, ele executa o modelo por meio de scripts, mas possui pouco conhecimento técnico sobre o código e seus parâmetros. Durante o processo, ocorre uma configuração incorreta, gerando uma segmentação imprecisa. Como o resultado não apresenta informações claras sobre a confiabilidade do processamento, o estudante registra uma avaliação inadequada e tem dificuldade para comparar o desempenho das configurações do modelo.

[H] (situação hipotética construída para ilustrar o problema)

## 4.6 Que evidência existe hoje?

| Evidência/fonte | O que sustenta | Limitação |
|---|---|---|
| Scripts utilizados atualmente no projeto (observação da equipe) | Mostram que a execução do modelo exige conhecimento técnico para configurar arquivos, parâmetros e comandos. | Não demonstram diretamente as dificuldades enfrentadas pelos usuários finais. |
| Observação do processo de segmentação pela equipe (2-3 integrantes) | Indica que a execução e a interpretação dos resultados dependem de conhecimentos prévios sobre o modelo. | Baseia-se na experiência da própria equipe, com poucos usuários observados. Data e detalhes da observação não foram registrados [?]. |

---

# 5. Entendendo o contexto de uso

## 5.1 Onde e em quais situações a interação poderia ocorrer?
O contexto prioritário é a **análise no laboratório da FEI, depois dos testes de campo**: o integrante leva ao computador as imagens e os vídeos capturados nas pistas off-road da FEI e avalia se o modelo delimita corretamente a região de trilha. O uso da interface na própria pista, entre um teste e outro, não foi definido e fica como lacuna. O uso em tempo real durante a operação do veículo está fora do recorte (Delimitação). O resultado da segmentação serve à análise do modelo e não indica, por si só, se um trecho é transitável ou seguro (§4.3 e §5.6).

[F] os testes do veículo ocorrem nos laboratórios e pistas off-road da FEI (observação da equipe); [H] a análise no laboratório, após os testes, como contexto prioritário de uso da interface; [?] o uso na pista.

## 5.2 Em quais dispositivos/equipamentos?
A interação ocorreria principalmente em computadores ou notebooks capazes de executar o software e processar as imagens ou os vídeos. Também seriam utilizadas câmeras instaladas no veículo Baja ou dispositivos móveis para registrar o percurso off-road.
[H]

## 5.3 Existem condições físicas relevantes?
<!--Considere iluminação, ruído, mobilidade, conexão, privacidade, uso compartilhado, interrupções, pressão de tempo etc. -->
Uma boa iluminação se faz necessária para conseguir registrar imagens e vídeos de ótima qualidade. Para quem utiliza a interface, condições como visibilidade da tela em ambientes externos e possíveis interrupções durante a análise são fatores a serem investigados.

[H]

## 5.4 Existem fatores sociais ou organizacionais?
<!--Considere papéis, chefias, equipes, permissões, aprovação, responsabilidade profissional, auditoria, turnos e colaboração. -->
A interface seria usada por papéis diferentes dentro da equipe Baja FEI: o analista de segmentação executa e avalia a segmentação, o pesquisador de modelos define configurações e treina os modelos, e o gestor de projeto consulta os resultados para decidir qual configuração adotar (§2.2). Ainda não se sabe se há permissões, aprovações ou divisão formal dessas funções (H07).

[H]

## 5.5 Existe necessidade de histórico, rastreabilidade ou auditoria?
Ainda não se sabe. A equipe levantou a hipótese de que manter o histórico das imagens e vídeos processados, junto com os resultados da segmentação, ajudaria a comparar registros, identificar falhas e acompanhar a evolução do modelo ao longo dos testes (**H08**). Até a coleta da Entrega 7, o histórico fica **fora do recorte**.

[H]

## 5.6 Um erro pode produzir consequência relevante? Qual?
Sim. Um erro de processamento ou de interpretação pode comprometer a avaliação e a comparação entre configurações do modelo. A consequência operacional no percurso não foi demonstrada e não deve ser inferida apenas da segmentação ou de suas métricas.

[H]

---

# 6. Entendendo mercado e alternativas existentes

> Nesta entrega faça apenas um **levantamento inicial**. A análise aprofundada ocorre na Entrega 2.

## 6.1 Como pessoas resolvem problemas semelhantes hoje?

| Alternativa atual | Quem usa | Para quê | Status/evidência |
|---|---|---|---|
| Scripts em Python e notebooks | Desenvolvedores e pesquisadores de IA | Executar modelos, processar imagens e visualizar máscaras de segmentação | [F] Processo atualmente utilizado no projeto |
| CVAT | Equipes de visão computacional | Anotar imagens, vídeos e 3D, produzindo as máscaras de referência para treino | [F] Entrega 2, §2 (C01) e evidências E1–E2 |
| Roboflow | Desenvolvedores e equipes de visão computacional | Ciclo completo (dataset, treino e implantação), incluindo testar um modelo com imagens próprias | [F] Entrega 2, §2 (C02) e evidências E3–E4 |
| Supervisely | Pesquisadores e profissionais de visão computacional | Ciclo completo de visão computacional, incluindo configurar e acompanhar treinos e analisar dados do projeto | [F] Entrega 2, §2 (C03) e evidências E5–E6 |

## 6.2 Existem produtos que atuam na mesma área, mesmo sem serem equivalentes ao TCC?
Existem produtos relacionados à visão computacional e a segmentação semântica, como os exemplos citados acima. Essas ferramentas permitem realizar atividades como anotação de imagens, organização de conjuntos de dados, treinamento de modelos e visualização de resultados.

[F] — análise de concorrência (Entrega 2, §2).

## 6.3 Quais interfaces profissionais esse público já conhece?
<!--Exemplos possíveis: ferramentas de banco, IDEs, consoles de nuvem, dashboards, plataformas de dados, ferramentas de monitoramento, painéis de IA, sistemas administrativos.** -->

Os integrantes do Baja FEI com noções básicas de programação devem estar familiarizados com interfaces como VS Code, terminais de linha de comando e GitHub. Também podem conhecer alguns sistemas de telemetria e ferramentas utilizadas para análise de dados e acompanhamento dos testes do veículo.
[H]

## 6.4 O que essas soluções parecem fazer bem?
As soluções pesquisadas centralizam atividades relacionadas à visão computacional, como envio e organização de imagens, anotação, treinamento e visualização dos resultados. [F] — análise de concorrência (Entrega 2).

Esses recursos podem facilitar a compreensão dos resultados e reduzir a necessidade de executar comandos manualmente. [H]

## 6.5 O que parecem fazer mal, dificultar ou não atender?
Por serem ferramentas genéricas e profissionais, essas soluções podem apresentar muitas funcionalidades, configurações e termos técnicos desnecessários para um integrante do Baja FEI que deseja apenas processar uma imagem ou um vídeo e visualizar o resultado.

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

O recorte da disciplina será o fluxo de configuração, treino, envio, processamento, visualização e comparação de resultados de imagens ou vídeos de vias off-road. O pesquisador de modelos (§2.2) poderá definir uma configuração e treinar o modelo com ela. O analista de segmentação, perfil prioritário (§7.2), poderá selecionar um arquivo e iniciar a segmentação com uma ou mais **configurações disponíveis**; visualizar a imagem original e o resultado lado a lado, com uma legenda das classes; consultar as métricas de desempenho de cada configuração; e comparar os resultados entre modelos e configurações. A interface pretende tornar o processo mais acessível e facilitar a compreensão dos resultados, sem exigir que o usuário interaja diretamente com o código ou insira novos modelos.

Neste projeto, **configuração** = modelo (FCN ou DeepLabV3+, ambos com ResNet152) + parâmetros de treino expostos ao usuário: número de épocas, early stopping e paciência, datasets de treino (Freiburg Forest e/ou Synthetic Offroad), batch size e geração de gráficos. Esses parâmetros fazem parte da configuração de treino do TCC [F]. O pesquisador define uma configuração e treina o modelo com ela; a configuração treinada passa a estar disponível para a segmentação e a comparação. Os demais parâmetros do arquivo (taxa de aprendizado, pesos das classes, tamanho da imagem, número de *workers*, modo de execução de teste e rótulos dos datasets) são internos e ficam fora da interface, assim como adicionar novas arquiteturas de modelo.

## 7.2 Qual perfil será priorizado no projeto de IHC?

O perfil priorizado será o do **analista de segmentação da equipe Baja FEI**, um integrante que possui conhecimento básico do domínio off-road e do projeto Baja, mas que pode não dominar programação. Esse perfil é responsável por avaliar a qualidade da segmentação e selecionar a configuração mais adequada, sendo o principal beneficiário de uma interface que elimine a necessidade de executar scripts manualmente.

[H]

## 7.3 Qual objetivo desse usuário será priorizado?

Avaliar a qualidade da segmentação semântica em diferentes imagens das pistas, identificando falhas de classificação e comparando o desempenho entre configurações, para selecionar a configuração a usar nos testes do veículo. A seleção se apoia nas métricas do conjunto de teste anotado e na inspeção visual; ela não indica se um trajeto é seguro (§4.3).

[H]

## 7.4 Que interface será explorada na disciplina?

Complete:

> **Para fins da disciplina de IHC, será projetada uma interface que permita ao `analista de segmentação da equipe Baja FEI` utilizar `o modelo de segmentação semântica e suas métricas de desempenho` para `avaliar a qualidade da segmentação e selecionar a configuração a usar nos testes do veículo`, no contexto de `análise, no laboratório da FEI, das imagens e vídeos capturados nos testes do veículo Baja nas pistas off-road`.**

## 7.5 Qual é a relação dessa interface com o TCC?

- [X] Já fazia parte do TCC.
- [ ] É um aprofundamento de algo parcialmente previsto.
- [ ] É uma extensão conceitual criada para a disciplina.
- [ ] É um protótipo demonstrativo de aplicação potencial.
- [ ] Outra.

> **Declaração:** a interface desenvolvida nesta disciplina é um artefato de aprendizagem de IHC baseado no tema do TCC. Sua inclusão ou implementação no TCC somente ocorrerá se isso for posteriormente decidido pela equipe e pelo orientador.
>
> **No nosso caso:** a interface já está prevista no TCC (§0.5). A declaração vale para o design produzido na disciplina: telas, fluxos e decisões só passam para o TCC se a equipe e o orientador decidirem.

---

# 8. Levantando possibilidades de interação — sem desenhar ainda

A equipe pode registrar possibilidades para investigação. **Não significa que todas serão implementadas.**

Marque apenas as que parecem plausíveis e explique o objetivo correspondente.

| Possibilidade | Pode fazer sentido? | Objetivo/tarefa que justificaria | Evidência atual |
|---|---|---|---|
| Dashboard/visão geral | talvez | Comparar o desempenho de diferentes modelos e visualizar métricas consolidadas | [H] |
| Configuração/parametrização | sim | Definir a configuração de treino com os parâmetros expostos ao usuário (§7.1) e escolher a configuração usada na execução. Parâmetros internos ficam fora | [H] |
| Entrada/upload/seleção de dados | sim | Enviar imagens ou vídeos de vias off-road para análise | [H] |
| Acompanhamento de processamento | sim | Acompanhar o estado da segmentação e do treino e perceber quando algo falhou (F03 da rastreabilidade) | [H] |
| Relatório/resultados | sim | Visualizar métricas de desempenho e resultados da segmentação | [H] |
| Histórico com busca/filtros | talvez | Consultar análises anteriores para comparar evolução ou reprocessar imagens. Fora do recorte até a Entrega 7 responder a H08 | [H] |
| Comparação de resultados | sim | São duas comparações diferentes, ambas no recorte: (a) imagem original × segmentação da mesma imagem, para interpretar o resultado (AC03); (b) resultados e métricas entre configurações, para selecionar a configuração (AC05). A interface apoia a comparação; a decisão continua com o usuário | [H] |
| Explicabilidade/detalhamento | talvez | Investigar por que uma região foi classificada de determinada forma | [H] |
| Administração/configurações globais | não | Adicionar novas arquiteturas ou alterar parâmetros internos acontece no código do TCC, fora do recorte (§7.1) | [H] |
| Usuários/perfis/permissões | não | Sistema local com uso restrito à equipe, sem necessidade de perfis; a existência de papéis ou permissões na equipe ainda depende da H07 | [H] |
| CRUD de entidade do domínio | não | Não há entidades complexas a serem gerenciadas no escopo atual | [H] |
| Auditoria/logs | talvez | Consultar um registro detalhado de erros e diagnósticos. A comunicação das falhas do fluxo não depende disso: ela acontece no acompanhamento (F03) | [H] |
| Alertas/ocorrências | talvez | Uma central de alertas separada. Falhas relevantes ao fluxo (arquivo inválido, falha na execução ou no treino) são comunicadas de qualquer forma no acompanhamento (F03) | [H] |
| Ajuda/documentação | talvez | Orientar usuários menos experientes sobre o uso do sistema | [H] |

> **Atenção:** “login + dashboard + CRUD” não é uma solução universal. Cada padrão deve surgir de uma tarefa real.

---

# 9. Benefícios e ações iniciais

## 9.1 Qual benefício concreto o projeto de IHC pretende oferecer?

| Benefício esperado | Problema/necessidade | Usuário | Status/evidência |
|---|---|---|---|
| Facilitar a execução da segmentação sem exigir interação direta com o código | Atualmente, é necessário executar scripts e possuir conhecimento técnico | Analista de segmentação | Processo atual do projeto [F]; benefício esperado [H] |
| Apresentar o resultado da segmentação de maneira clara e compreensível | Dificuldade para identificar e interpretar a região de trilha delimitada pelo modelo | Analista de segmentação | Deve ser validado com os usuários [H] |
| Permitir a comparação entre configurações para selecionar a que será usada | Necessidade de avaliar qual configuração apresenta melhor desempenho | Analista de segmentação | Levantamento inicial [H] |

## 9.2 Que ações o usuário deverá conseguir realizar?

| ID | O usuário precisa conseguir... | Para alcançar... | Prioridade inicial |
|---|---|---|---|
| AC01 | Selecionar e enviar uma imagem ou um vídeo | Inserir o arquivo que será analisado pelo modelo | alta |
| AC02 | Iniciar o processamento da segmentação | Gerar o resultado da segmentação sem executar scripts manualmente | alta |
| AC03 | Visualizar a imagem original e o resultado segmentado lado a lado | Interpretar como o modelo classificou cada região da imagem | alta |
| AC04 | Visualizar métricas de desempenho de cada modelo: IoU e acurácia **no conjunto de teste anotado** e tempo de inferência, com explicação do que cada métrica indica e não indica (F04 da rastreabilidade) | Avaliar a qualidade da segmentação e comparar configurações. Imagens novas de campo não têm anotação de referência; nelas a avaliação é visual. Exibir os números não garante que sejam compreendidos; isso será avaliado (H04, RC01) | alta |
| AC05 | Comparar resultados entre diferentes modelos ou configurações | Selecionar a configuração a usar nos testes do veículo | média |
| AC06 | (pesquisador de modelos) Definir uma configuração de treino e treinar o modelo com ela | Obter configurações para comparar sem precisar alterar código | média |

## 9.3 Tecnologias/restrições já definidas no TCC

A tecnologia aparece **agora**, depois do entendimento do uso.

| Tecnologia/restrição | Por que existe | Possível impacto na interação |
|---|---|---|
| Python | É a linguagem utilizada no desenvolvimento e na execução do modelo | A interface deverá se comunicar com o código responsável pelo processamento |
| FCN e DeepLabV3+ | São as duas arquiteturas comparadas pelo TCC; cada uma classifica os pixels em *Trilha* ou *Fora da trilha* | O processamento pode levar tempo, sobretudo com o backbone ResNet152. A interface precisa de indicador de progresso por modelo e deve avisar quando o resultado estiver pronto |
| ResNet152 | É o backbone usado pelos dois modelos para extrair características das imagens | Aumenta o tempo de processamento e o consumo de memória, especialmente em computadores sem GPU |
| Métricas do TCC | O TCC avalia os modelos no conjunto de teste anotado (IoU/mIoU, acurácia, recall, F1 e matriz de confusão) e mede o tempo de inferência [F] (metodologia do TCC) | As métricas por modelo vêm desse conjunto. Imagens novas de campo não têm anotação de referência e são avaliadas visualmente |
| Configuração de treino | O treino usa os parâmetros da configuração (§7.1) e registra loss, acurácia e mIoU a cada época [F] | A interface expõe só os parâmetros do usuário, com valores padrão, e mostra o progresso por época |
| Saída do modelo | Uma máscara binária por imagem; vídeos são segmentados quadro a quadro [F] | Sobreposição colorida e legenda são recursos da interface |

---

# 10. Hipóteses e dúvidas prioritárias

| ID | Hipótese/dúvida | Por que importa | Como poderá ser investigada |
|---|---|---|---|
| H01 | A decisão sobre qual modelo usar é tomada com base em números dispersos e sem critério explícito *(reformulada em 08/11/2026; texto anterior: "O que se espera que esteja diferente para pessoas, organizações ou processos se essa contribuição for bem-sucedida?")* | Define se a interface precisa reunir as métricas e explicitar o critério de comparação. A H12 trata do benefício esperado | Entrega 4 (cenário C02) e Entrega 7 (coleta de dados) |
| H02 | O perfil prioritário (analista de segmentação) possui conhecimento básico do domínio mas pode não dominar programação | Direciona o nível de complexidade da interface | Entrega 3 (personas e contexto) |
| H03 | O piloto Baja FEI seria beneficiado indiretamente, sem interagir diretamente com a interface | Esclarece stakeholders e impactos indiretos | Entrega 3 (personas e contexto) |
| H04 | Conhecimento técnico, experiência com ferramentas e familiaridade com métricas influenciam a interação | Define requisitos de design para acessibilidade e usabilidade | Entrega 3 (personas e contexto) |
| H05 | As atividades são realizadas atualmente por meio de scripts que exigem conhecimento técnico | Base do problema de interação que a interface deve resolver | Entrega 2 (investigada parcialmente) e Entrega 7 (com o público) |
| H06 | Dificuldades principais: configurar parâmetros, selecionar arquivos, interpretar resultados sem orientação | Identifica pontos críticos de interação | Entrega 4 (situações problemáticas) |
| H07 | Existem fatores sociais ou organizacionais como papéis, permissões e colaboração na equipe | Pode afetar design e governança da interface | Entrega 7 (coleta de dados) |
| H08 | Existe necessidade de histórico para comparar análises e acompanhar evolução | Define se interface precisa de funcionalidades de busca e armazenamento | Entrega 7 (investigação) e Entrega 8 (engenharia de usabilidade) |
| H09 | Interfaces conhecidas pelo público: VS Code, terminais, GitHub, ferramentas de telemetria | Estabelece padrões e expectativas do usuário | Entrega 7 (coleta de dados) |
| H10 | Ferramentas genéricas como CVAT e Roboflow podem ser complexas para o perfil priorizado | Justifica a necessidade de uma interface simplificada | Entrega 7 (coleta de dados) |
| H11 | Padrões familiares: seleção de arquivo, botão de processamento, barra de progresso, comparação lado a lado | Direciona elementos de interface a serem incluídos | Entrega 7 (coleta de dados) |
| H12 | Benefício esperado: eliminar necessidade de código, apresentar resultados claramente, permitir comparação entre modelos | Define métricas de sucesso do projeto | Investigação contínua ao longo do projeto |

Registre em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

---

# 11. Síntese da equipe

| Pergunta | Síntese atual |
|---|---|
| Qual é a contribuição central do TCC? | Desenvolver um sistema de segmentação semântica (binária: trilha × fora da trilha) de vias off-road e comparar o desempenho entre FCN e DeepLabV3+ |
| O TCC já previa interface? | Sim |
| Quem é o usuário prioritário de IHC? | Analista de segmentação da equipe Baja FEI |
| O que ele precisa alcançar? | Avaliar a qualidade da segmentação, identificar falhas de classificação e selecionar a configuração a usar nos testes do veículo |
| Qual problema/atividade será estudado? | A dificuldade de interpretar resultados de segmentação sem uma interface adequada, e a necessidade de comparar modelos |
| Como isso acontece hoje? | Através de scripts Python que exigem conhecimento técnico |
| Qual é o contexto de uso? | Análise no laboratório da FEI, depois dos testes de campo, das imagens e vídeos capturados nas pistas off-road (uso na pista: [?]) |
| Que interface/recorte será explorado? | Configuração e treino dos modelos (pesquisador de modelos), upload de dados, processamento, visualização lado a lado, métricas de desempenho e comparação entre modelos e configurações |
| Como a interface se relaciona ao TCC? | Facilita a utilização do sistema de segmentação desenvolvido no TCC, sem exigir interação direta com código |
| Quais pontos ainda são hipóteses? | H01, H02, H03, H04, H06, H07, H08, H09, H10, H11, H12 |

### Delimitação

**Dentro do escopo de IHC:** Definição da configuração de treino (parâmetros expostos ao usuário, §7.1) e treino dos modelos, upload de imagens/vídeos, execução da segmentação com um ou mais modelos disponíveis, visualização lado a lado (original × segmentação), exibição de métricas de desempenho (no conjunto de teste anotado) e comparação entre os modelos disponíveis.

**Fora do escopo de IHC:** Adição de novas arquiteturas de modelo, ajuste dos parâmetros internos do treino (taxa de aprendizado, pesos das classes, tamanho da imagem, entre outros), anotação de datasets, integração com hardware do veículo, processamento em tempo real durante corridas e, até a Entrega 7 responder a H08, histórico de análises.

**Dentro do escopo formal do TCC:** Desenvolvimento dos modelos de segmentação semântica (FCN e DeepLabV3+, ambos com ResNet152), comparação de desempenho entre eles, métricas de avaliação, sistema de interface para configuração, visualização e análise dos resultados.

**Interface da disciplina será implementada no TCC?** Sim — a interface faz parte do escopo formal do TCC como ferramenta de apoio à análise dos resultados. O que for desenhado na disciplina só entra no TCC por decisão da equipe e do orientador (§7.5).

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

1. **Problema/atividade humana:** Integrantes da equipe Baja FEI precisam avaliar a qualidade da segmentação semântica de vias off-road para selecionar a configuração mais adequada, mas atualmente dependem de scripts técnicos que dificultam a interpretação dos resultados.

2. **Contribuição técnica do TCC:** Desenvolvimento de um sistema de segmentação semântica (trilha × fora da trilha) com comparação de desempenho entre FCN e DeepLabV3+ e métricas de avaliação.

3. **Como uma pessoa poderia utilizar essa contribuição:** Através de uma interface visual, o analista envia imagens do terreno, acompanha o processamento e compara os resultados lado a lado, identificando falhas de classificação e selecionando a configuração mais adequada sem precisar executar comandos no terminal.

Essa síntese ajuda a apresentar o projeto para público não especializado sem reduzir seu mérito técnico.

---

# Checklist de qualidade

- [X] Está clara a diferença entre tema do TCC, escopo formal do TCC e escopo de IHC.
- [X] A equipe declarou se o TCC já previa interface.
- [X] A interface de IHC não foi apresentada como obrigação automática do TCC.
- [X] A contribuição do TCC foi descrita sem começar por tecnologias de implementação.
- [X] Usuários diretos e stakeholders foram diferenciados.
- [X] Foram considerados profissionais que configuram, administram, interpretam ou decidem, quando pertinente.
- [X] Objetivo do usuário não foi confundido com objetivo do projeto.
- [X] Processo/problema atual foi descrito antes da solução.
- [X] Existe situação concreta de uso/problema (identificada como hipotética).
- [X] Contexto físico, social/organizacional, dispositivos e consequências de erro foram considerados.
- [X] Mercado/alternativas existentes foram levantados inicialmente.
- [X] Possibilidades como dashboard, relatório, histórico, filtros e CRUD foram tratadas como hipóteses de solução, não como requisitos automáticos.
- [X] Cada possibilidade de interface tem um objetivo/tarefa que poderia justificá-la.
- [X] Afirmações relevantes estão marcadas `[F]`, `[H]` ou `[?]`.
- [X] Hipóteses prioritárias receberam IDs únicos e estão na rastreabilidade.
- [X] O recorte de IHC é viável para modelar, prototipar e avaliar no semestre.
- [X] A equipe consegue explicar problema humano → contribuição computacional → forma de uso.

# Histórico de revisões

| Data | O que mudou | Motivo |
|---|---|---|
| 26/09/2026 | Perfil prioritário (analista de segmentação), objetivo humano além de "segmentar", consolidação do recorte, correção de IDs e marcações, delimitação preenchida | Feedback do professor sobre a Entrega 1 |
| 28/09/2026 | Histórico e comparação de resultados passaram para "talvez/sim" na §8; versionamento de modelos saiu do recorte; perfil padronizado como "analista de segmentação da equipe Baja FEI" | Feedback do professor e resultados da Entrega 2 |
| 08/11/2026 | Classes, modelos e métricas alinhados ao repositório do TCC (§0.4, §0.5, §9.2, §9.3, §11): segmentação binária *Trilha* × *Fora da trilha*, modelos FCN e DeepLabV3+, métricas por modelo só no conjunto de teste anotado. "Configuração" definida como modelo + parâmetros de treino expostos ao usuário (§7.1, §9.3); configurar e treinar entram no recorte (§2.2, §8, §9.2 AC06, Delimitação); novas arquiteturas e parâmetros internos ficam fora. §7.5 explica que a declaração da disciplina vale para o design produzido nela, já que a interface está prevista no TCC. §5.1, §5.2 e §6.4 deixam de marcar como [F] afirmações hipotéticas. §5.5 reescrita como hipótese (H08). H01 reformulada como afirmação testável | Revisão de consistência (`PENDENCIAS.md`: INC-11, INC-12, INC-14, INC-15, INC-16, INC-18, INC-52) e leitura do repositório do TCC |
| 08/11/2026 | Fase 2 da revisão de pendências: IDs das ações da §9.2 passam a AC01–AC06 (as atividades da §3.2 continuam A01–A04); §7.1 descreve o recorte completo (configuração e treino, execução, visualização, métricas e comparação); origem dos [F] da §1.2 e da §2.1; "Onde investigar" da H05 e da H08 alinhado à RAST; correções de grafia | Revisão de consistência (`PENDENCIAS.md`: INC-06, INC-10, INC-13, INC-17, INC-19) |
| 10/11/2026 | Parecer da Entrega 01 conferido contra o estado atual e aplicado nos pontos que ainda valiam. Seleção descrita como escolha da configuração a usar nos testes do veículo, apoiada nas métricas do conjunto de teste e na inspeção visual (§1.4, §2.2, §2.4, §3.1, §7.2–§7.4, §9.1, §9.2, §11, §13). Configurar e treinar atribuídos ao pesquisador de modelos (§7.1, AC06); nova atividade A05 e criticidade preenchida na §3.2. §5.4 descreve os papéis (H07). Contexto prioritário: análise no laboratório depois dos testes de campo; uso na pista vira lacuna (§5.1, §7.4, §11). §6.1 e §6.2 citam a Entrega 2. §8 separa as duas comparações e liga alertas e logs ao acompanhamento (F03). §2.4 separa conhecimento de programação e de segmentação. §4.6 registra que os detalhes da observação não foram anotados. Coluna de responsabilidades da §0.1 removida; resíduos do template e grafia corrigidos | Feedback do professor sobre a Entrega 1 (itens 1, 3, 4, 5, 6, 7 e recomendações; itens 2 e 8 já estavam atendidos) |
