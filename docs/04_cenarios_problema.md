# Entrega 4 — Cenários de análise/problema

**Data:** 20/10/2026  
**Status:** 🟩 concluída
**Responsabilidade:** 1 solução completa por integrante

## Objetivo da atividade

Descrever situações atuais em que o usuário tenta alcançar um objetivo e encontra dificuldades. O cenário de análise/problema deve tornar visível **o contexto, os atores, as ações e as rupturas**, sem antecipar a interface que será projetada.

> **Regra central:** cenário de problema é a “história do problema”. Se o texto já diz “o sistema mostra”, “o aplicativo resolve” ou descreve botões/telas futuras, provavelmente está misturando problema com solução.

Sempre que possível, o cenário deve aprofundar uma **situação concreta já registrada na Entrega 1**.

### Quando o TCC não possuía interface

O cenário continua sendo uma história de **problema/atividade humana**, não uma história do futuro sistema. Descreva como o profissional realiza hoje uma atividade semelhante ou como lida atualmente com dados, resultados, configurações, logs, decisões e limitações que o tema do TCC pretende apoiar.

Exemplo: em vez de “o DBA abre o novo dashboard e executa o algoritmo”, descreva “o DBA precisa investigar uma consulta lenta, reúne informações em ferramentas distintas, compara planos manualmente e tem dificuldade para estimar o impacto de uma mudança”.

A interface da disciplina aparecerá somente depois, nos cenários de interação.

Se o integrante escolher um novo problema/situação, explique por que ele passou a ser relevante e indique a evidência que motivou sua inclusão.

## Convenção de marcação do refinamento

Vale para todos os cenários desta entrega. O objetivo é mostrar, no próprio texto, **o que cada questão de refinamento acrescentou ou alterou** em relação ao cenário inicial.

| Marcação | Significado |
|---|---|
| `[Qn]` antes do trecho | O trecho responde à questão de refinamento Qn. |
| Texto normal | Mantido do cenário inicial, sem alteração de conteúdo. |
| **Negrito** | Informação **nova**, trazida pela resposta à questão. |
| *Itálico* | Trecho do cenário inicial **reescrito ou especificado** pela resposta. |

Depois do cenário refinado, uma tabela **Resumo do refinamento** indica, para cada questão, se ela trouxe informação nova, alterou um trecho ou não acrescentou nada. Questões "sem acréscimo" devem ser reformuladas ou investigadas na Entrega 7.

## Cenário C01 — Validação manual de segmentação em campo

**Autor(a):** Tiago Fagundes dos Santos — 22.123.017-0  
**Persona(s) relacionada(s):** P01 — Rafael Pereira  
**Necessidade relacionada:** R01, R02 e R03  
**Situação concreta da Entrega 1 relacionada:** seção 4.5 (situação concreta, hipotética)  
**Hipóteses ainda presentes:** H02, H04, H05, H06

### 1. Cenário inicial

Rafael acompanha os testes do Baja em terrenos off‑road dentro da FEI, ele coleta imagens com câmeras acopladas ao veículo e precisa validar se o modelo de segmentação está delimitando corretamente a região de trilha. Atualmente, esse processo depende de scripts em Python, Rafael precisa abrir cada imagem, rodar o código manualmente e gerar a máscara de segmentação. Quando o script quebra ou apresenta erro, ele perde tempo depurando, mesmo não sendo desenvolvedor. Além disso, cada execução gera arquivos separados que precisam ser organizados manualmente em pastas, sem padrão definido. Em uma das execuções, o script termina, mas a máscara gerada cobre quase toda a pista com uma única cor. Sem informação sobre a confiança do resultado, Rafael não consegue dizer se a falha é do modelo ou da imagem. Ele tenta rodar novamente com outra configuração, abre as duas máscaras em janelas separadas e compara manualmente, mas as métricas ficaram em planilhas diferentes e ele perde o fio da comparação. Esse processo improvisado de comparação manual gera frustração, ele sente que perde tempo com tarefas repetitivas e que a análise não é clara o bastante para apoiar decisões rápidas da equipe.

### 2. Questões de refinamento

Use os tipos de questões/taxonomia definidos na aula. As perguntas devem revelar informações **ainda ausentes** do cenário, não repetir o que já foi respondido.

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| Q1 | Por que Rafael precisa validar a segmentação e o que espera obter com isso? | Para entender o objetivo real da atividade e os resultados esperados. | Entrevista com integrante que faz a análise de segmentação (perfil P01). |
| Q2 | Que consequência uma falha na execução tem para o teste do dia? | Para dimensionar o impacto da falha, separado dos erros em si (Q8). | Entrevista com integrante que faz a análise de segmentação (perfil P01) e com a equipe. |
| Q3 | Como Rafael organiza atualmente os arquivos gerados pelos scripts? | Para revelar detalhes da sequência de ações e dificuldades com gestão de dados. | Análise dos diretórios. |
| Q4 | O que a equipe faz com o resultado da validação? Que decisão depende dele? | Para entender o uso do resultado, separado de quem o recebe (Q6). | Entrevista com a equipe Baja FEI. |
| Q5 | Como Rafael decide qual modelo ou versão comparar em cada teste? | Para entender o planejamento e critérios de escolha. | Discussões técnicas na Equipe Baja FEI. |
| Q6 | Quem participa da validação, quem fornece as imagens e quem consome ou precisa ser notificado do resultado? | Para mapear atores envolvidos e dependências. | Equipe Baja FEI. |
| Q7 | Como Rafael decide se uma máscara está correta e como sabe que a validação foi concluída com sucesso? O que faz quando não tem certeza? | Para definir critérios de avaliação e indicadores de confiança. | Equipe Baja FEI e Métricas de acurácia. |
| Q8 | Quais são os passos e pré-condições da execução? Que erros podem ocorrer, como Rafael os identifica e contorna? |Para detalhar sequência de ações e falhas comuns. | Entrevista com integrante que faz a análise de segmentação (perfil P01) + logs, se existirem. |
| Q9 | Quando, onde e por que a validação acontece? |Para detalhar o ambiente/contexto e suas limitações. | Entrevista com a equipe Baja FEI. |

### 3. Cenário refinado

> P01 é proto-persona: as respostas abaixo são **hipóteses de trabalho**, não relatos. Precisam ser validadas na Entrega 7.
>
> Marcação conforme a [convenção de refinamento](#convenção-de-marcação-do-refinamento): texto normal = mantido; **negrito** = novo; *itálico* = reescrito/especificado.

Rafael acompanha os testes do Baja em terrenos off-road dentro da FEI e coleta imagens com câmeras acopladas ao veículo. [Q9] **A validação acontece no laboratório, no mesmo dia do teste ou no dia seguinte, sobre algumas dezenas de imagens escolhidas dos trechos mais difíceis do percurso.** [Q6] **Rafael é quem executa a validação; as imagens são descarregadas das câmeras por quem acompanhou o teste, e o resultado é enviado ao grupo da equipe.** [Q1] Ele precisa validar se o modelo de segmentação está delimitando corretamente a região de trilha **para dizer à equipe, antes do próximo teste, se a configuração em uso pode continuar sendo usada.** [Q4] **A equipe usa essa resposta para decidir se mantém a configuração ou se pede uma comparação com outra.** Atualmente, esse processo depende de scripts em Python: Rafael precisa abrir cada imagem, rodar o código manualmente e gerar a máscara de segmentação. [Q8] **Antes de rodar, confere se as imagens estão na pasta esperada e qual modelo está selecionado; os erros mais comuns são imagem em formato não aceito e arquivo fora da pasta esperada, e ele só percebe quando a execução para.** Quando o script quebra ou apresenta erro, ele perde tempo depurando, mesmo não sendo desenvolvedor. [Q2] **Se a falha acontece no dia do teste, a equipe fica sem a resposta e segue com a configuração anterior sem saber se ela está adequada.** [Q3] Cada execução gera arquivos separados, que precisam ser organizados manualmente em pastas, sem um padrão definido; **ele nomeia as pastas pela data do teste, mas as métricas ficam em planilhas à parte.** Em uma das execuções, o script termina, mas a máscara gerada cobre quase toda a pista com uma única cor. Sem informação sobre a confiança do resultado, Rafael não consegue dizer se a falha é do modelo ou da imagem. [Q7] **Ele considera uma máscara correta quando a borda da trilha coincide com o que vê na imagem original; quando não tem certeza, pede a opinião de um colega e marca a imagem como duvidosa.** [Q5] Ele tenta rodar novamente com outra configuração, *em geral a mais recente que alguém da equipe treinou*, abre as duas máscaras em janelas separadas e compara manualmente, mas as métricas ficaram em planilhas diferentes e ele perde o fio da comparação. Esse processo improvisado de comparação manual gera frustração: ele sente que perde tempo com tarefas repetitivas e que a análise não é clara o bastante para apoiar decisões rápidas da equipe.

#### Resumo do refinamento

| Questão | Resultado | O que mudou no cenário |
|---|---|---|
| Q1 | Novo | Para que serve a validação: dizer à equipe, antes do próximo teste, se a configuração em uso pode continuar. |
| Q2 | Novo | Consequência de uma falha no dia do teste: a equipe segue sem saber se a configuração está adequada. |
| Q3 | Novo | Como os arquivos são organizados hoje: pastas por data do teste e métricas em planilhas à parte. |
| Q4 | Novo | Que decisão depende do resultado: manter a configuração ou pedir uma comparação. |
| Q5 | Reescrito | A "outra configuração" passa a ser especificada: em geral, a mais recente treinada pela equipe. |
| Q6 | Novo | Atores: Rafael executa, quem acompanhou o teste fornece as imagens e o grupo da equipe recebe o resultado. |
| Q7 | Novo | Critério de correção (borda da trilha coincide com a imagem) e o que ele faz na dúvida (consulta um colega e marca a imagem). |
| Q8 | Novo | Pré-condições (imagens na pasta, modelo selecionado) e erros mais comuns, percebidos só quando a execução para. |
| Q9 | Novo | Quando e onde: no laboratório, no dia do teste ou no seguinte, com algumas dezenas de imagens dos trechos mais difíceis. |

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | Rafael e Equipe Baja FEI |
| Objetivo(s) | Validar se o modelo de segmentação está delimitando corretamente a região de trilha e apoiar nas decisões rápidas da equipe. |
| Contexto | Testes do Baja em terrenos off-road dentro da FEI, o processo depende de scripts em Python e cada execução gera arquivos separados, sem um padrão definido. |
| Recursos/informações |  Câmeras acopladas ao veículo, scripts em Python, máscara de segmentação e métricas de cada modelo (IoU e acurácia só existem para imagens com anotação de referência; para imagens novas de campo, a avaliação é visual) |
| Ações | Abrir cada imagem; rodar o código manualmente; gerar a máscara de segmentação; organizar manualmente os arquivos, comparar resultados manualmente; informar a equipe sobre o resultado. |
| Problemas/rupturas | O script quebra ou apresenta erro e Rafael perde tempo depurando, mesmo não sendo desenvolvedor; arquivos ficam sem um padrão definido; a máscara cobre quase toda a pista com uma única cor; sem informação sobre a confiança do resultado, não consegue dizer se a falha é do modelo ou da imagem; as métricas em planilhas diferentes fazem perder o fio da comparação; a comparação é manual e improvisada. |
| Consequências | Rafael perde tempo com tarefas repetitivas, sente frustração, perde o fio da comparação e a análise não é clara o bastante para apoiar decisões rápidas da equipe. |

### 5. Implicações para as próximas entregas

<!-- Quais tarefas merecem análise? Quais informações precisam ser coletadas? **Não desenhe a solução ainda.** -->
#### Tarefas que merecem análise

| ID | Tarefa | Origem no cenário | Por que merece análise | Prioridade |
|---|---|---|---|---|
| **T01** | Avaliar a qualidade da segmentação de uma imagem | C01; Q1, Q7; R01 | É o núcleo da validação: comparar imagem e máscara, interpretar classes/métricas e decidir se o resultado é confiável. A ausência de informação de confiança e de critério explícito torna a tarefa crítica. | Alta |
| **T02** | Executar a segmentação com uma ou mais configurações disponíveis *(nome revisado em 08/11/2026; antes "…com uma configuração disponível")* | C01; Q2, Q8; R02 | É a entrada da atividade: abrir cada imagem, rodar o script, gerar a máscara e lidar com falhas. A depuração interrompe o fluxo e consome tempo. | Alta |
| **T03** | Comparar o resultado de uma imagem entre configurações | C01; Q4, Q5, Q7; R03 | Sustenta a decisão da equipe sobre qual configuração usar. Hoje a comparação é manual, as métricas ficam dispersas e Rafael perde o fio da comparação. | Alta |

#### Informações que precisam ser coletadas

| Informação | Origem | Para que serve | Como coletar |
|---|---|---|---|
| Quando, onde e com que frequência a validação acontece; duração e quantidade de imagens por sessão | Q9, Q2 | Define o contexto real e as restrições da tarefa | Entrevista com integrante que faz a análise de segmentação (perfil P01) + observação |
| Quem executa, quem fornece as imagens, quem consome o resultado, quem decide e quem precisa ser notificado | Q4, Q6 | Mapeia atores, dependências e destinatários | Entrevista com integrante que faz a análise de segmentação (perfil P01) e com a equipe |
| Como Rafael escolhe a configuração a comparar e quem decide a adoção | Q5 | Entende o planejamento e a autoridade de decisão | Entrevista com integrante que faz a análise de segmentação (perfil P01) e com a gestão |
| Critérios para considerar uma máscara correta; sinais de confiança; o que faz quando tem dúvida | Q7 | Define o que é “sucesso” na validação | Entrevista + observação |
| Passos, pré-condições e erros da execução; como identifica e contorna cada erro | Q8, Q2 | Identifica pontos de falha e recuperação | Observação + entrevista + logs, se existirem |
| Estrutura de pastas, nomes dos arquivos e local onde ficam as métricas | Q3 | Entende como os resultados são organizados e recuperados | Análise dos diretórios/planilhas + entrevista |
| Métricas usadas (IoU, acurácia, por classe), como são lidas e comparadas | Q7 | Define quais informações sustentam a avaliação | Entrevista + análise das planilhas/saídas |
| Consequências da falha ou de uma validação inconclusiva | Q2, Q4 | Dimensiona o impacto e a criticidade | Entrevista com integrante que faz a análise de segmentação (perfil P01) e com a equipe |

## Cenário C02 — Decisão de modelo a partir de resultados dispersos

**Autor(a):** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3  
**Persona(s) relacionada(s):** P03 — Larissa Camargo  
**Necessidade relacionada:** R03 — comparar desempenho entre modelos (P03: decidir)  
**Situação concreta da Entrega 1 relacionada:** **Nova situação justificada** — perfil "Gestor de projeto" (01 §2.2 `[H]`) e contexto organizacional (01 §5.4); a E1 não registra situação observada da P03.  
**Hipóteses ainda presentes:** H01, H04, H06, H12

> **Justificativa da nova situação:** a E1 reconhece o perfil "Gestor de projeto" (§2.2) como quem consulta resultados consolidados e decide qual modelo usar, mas não descreve uma situação concreta desse perfil. A decisão é condição para os testes do veículo e depende do resultado produzido pela P01. Por isso o cenário é relevante. A situação é **hipotética** (P03 é proto-persona) e precisa ser validada na Entrega 7.

### 1. Cenário inicial

Larissa Camargo é gestora de projeto da equipe Baja FEI. Antes de um ciclo de testes do veículo, ela precisa definir qual configuração do modelo de segmentação será adotada. A decisão é discutida com a coordenação da equipe (no projeto, a P02, Professora Coordenadora) em uma reunião semanal, mas quem executa os modelos é um integrante técnico da equipe — Larissa não escreve código nem domina machine learning ou estatística.

Para decidir, ela recebe desse integrante, por mensagens e planilhas separadas, números de IoU e acurácia de cada configuração testada, cada uma em uma execução diferente. Os valores chegam sem uma referência do que seria um bom resultado e sem indicar o que cada métrica significa na prática. Larissa compara os números manualmente, em abas e arquivos distintos, e não consegue avaliar se a diferença entre dois modelos é relevante ou apenas variação do teste.

Quando precisa levar a decisão à coordenação, ela tem dificuldade de explicar por que um modelo é melhor que outro e de sustentar a escolha. Sem critério claro, a decisão é adiada ou tomada pelo número aparentemente maior, sem justificativa. Isso aumenta o risco de adotar um modelo inadequado ao terreno e de a equipe refazer a análise depois. Larissa sente que depende dos colegas técnicos para entender o resultado e que decide sem segurança.

### 2. Questões de refinamento

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| Q10 | Por que a decisão precisa ocorrer antes do teste e o que se espera dela? | Entender o objetivo real da decisão e o que seria uma escolha bem-sucedida. | Entrevista com integrante de gestão (perfil P03) e com a coordenação. |
| Q11 | Com que antecedência os resultados chegam antes da reunião de decisão? | Saber se há tempo para entender os números e tirar dúvidas antes de decidir. | Entrevista com integrante de gestão (perfil P03) + análise das mensagens. |
| Q12 | Quem participa da decisão e qual é a autoridade de Larissa em relação à coordenação? | Mapear papéis, responsabilidades e quem tem a palavra final. | Entrevista com integrante de gestão (perfil P03) e com a coordenação. |
| Q13 | Quais métricas ela recebe e não usa, e por quê? | Identificar o que é descartado por falta de entendimento ou de critério. | Entrevista + análise das saídas de segmentação. |
| Q14 | Como ela compara modelos ou versões e define qual é o "melhor"? | Entender o critério atual de comparação e suas limitações. | Observação da reunião + entrevista. |
| Q15 | Que termos técnicos ela não entende e precisa que alguém explique? | Delimitar a barreira de terminologia (RC01). | Entrevista com integrante de gestão (perfil P03). |
| Q16 | Já houve uma decisão revista depois do teste? O que motivou a revisão? | Dimensionar a consequência de uma decisão errada a partir de um caso concreto. | Entrevista com integrante de gestão (perfil P03) e com a coordenação. |
| Q17 | O que ela leva para a reunião e como justifica a escolha? | Entender o material de apoio e a dificuldade de sustentar a recomendação. | Observação + análise dos materiais levados. |

### 3. Cenário refinado

> P03 é proto-persona: as respostas abaixo são **hipóteses de trabalho**, não relatos. Precisam ser validadas na Entrega 7.
>
> Marcação conforme a [convenção de refinamento](#convenção-de-marcação-do-refinamento): texto normal = mantido; **negrito** = novo; *itálico* = reescrito/especificado.

Larissa Camargo é gestora de projeto da equipe Baja FEI e não escreve código nem domina machine learning ou estatística. [Q10] **A decisão precisa ocorrer antes de cada ciclo de testes porque a configuração escolhida será usada no veículo; o que se espera é uma escolha defensável, não apenas o maior número.** [Q12] **A decisão é compartilhada com a coordenação: Larissa reúne os resultados e recomenda, e a palavra final é discutida no grupo.** [Q11] Os resultados chegam por mensagens e planilhas separadas, enviados pelo integrante que executa os modelos, cada configuração em uma execução. **Costumam chegar na véspera da reunião, sem tempo para ela tirar dúvidas com quem executou.** [Q13] Ela recebe IoU e acurácia, mas não tem referência de comparação nem explicação do que cada valor significa na prática. **Também recebe o tempo de inferência e números por classe, mas ignora os dois, porque não sabe como pesam na decisão.** [Q14] Para comparar, **abre as planilhas lado a lado**; *quando a diferença entre dois modelos é pequena, não sabe dizer se é relevante* e escolhe pelo número maior, por falta de outro critério. [Q15] **Termos como IoU, acurácia por classe e o que a região de "trilha" representa geram dúvida e dependem de um colega para serem explicados.** [Q17] Na reunião, **leva os números das planilhas** e tenta justificar a escolha, mas tem dificuldade de sustentar a recomendação. [Q16] Quando adia ou escolhe sem critério, o teste pode usar um modelo inadequado e a equipe precisa refazer a análise depois. **Isso já aconteceu: uma configuração escolhida pelo maior número falhou nos trechos de sombra do percurso, e a decisão foi revista depois do teste.** Larissa sente que depende dos colegas técnicos e que decide sem segurança.

#### Resumo do refinamento

| Questão | Resultado | O que mudou no cenário |
|---|---|---|
| Q10 | Novo | Motivo de a decisão ocorrer antes do teste e o que se espera dela (escolha defensável). |
| Q11 | Novo | Os resultados chegam na véspera da reunião, sem tempo para tirar dúvidas. |
| Q12 | Novo | Divisão de papéis: Larissa reúne e recomenda; a palavra final é discutida com a coordenação. |
| Q13 | Novo | Ela ignora o tempo de inferência e os números por classe por não saber como pesam na decisão. |
| Q14 | Novo e reescrito | Novo: a comparação é feita abrindo as planilhas lado a lado. Reescrito: a dúvida sobre relevância da diferença passa a ser associada a diferenças **pequenas**. |
| Q15 | Novo | Termos específicos que geram dúvida e a dependência de um colega para explicá-los. |
| Q16 | Novo | Caso concreto de decisão revista depois do teste (falha nos trechos de sombra). |
| Q17 | Novo | O que ela leva para a reunião: os números das planilhas. |


### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | Larissa (gestora), o integrante técnico que executa os modelos (P01) e a coordenação da equipe (P02) na decisão. |
| Objetivo(s) | Decidir qual configuração de modelo adotar nos testes e justificar a escolha. |
| Contexto | Antes de um ciclo de testes, em reunião semanal; os resultados chegam por mensagens e planilhas separadas. |
| Recursos/informações | Métricas (IoU, acurácia), planilhas, mensagens com resultados de execuções e conhecimento dos colegas técnicos. |
| Ações | Receber os resultados; abrir as planilhas; comparar números manualmente; pedir explicação dos termos; levar a recomendação à reunião; justificar a escolha. |
| Problemas/rupturas | Resultados dispersos e sem referência; termos que ela não entende; dúvida se a diferença entre modelos é relevante; dependência de colegas técnicos; dificuldade de justificar a escolha. |
| Consequências | Decisão adiada ou frágil; risco de adotar um modelo inadequado ao terreno; retrabalho da equipe; insegurança de Larissa. |

### 5. Implicações para as próximas entregas

#### Tarefas que merecem análise

| ID | Tarefa | Origem no cenário | Por que merece análise | Prioridade |
|---|---|---|---|---|
| **T04** | Comparar o desempenho consolidado entre modelos | C02; Q13, Q14; R03 | É a base da decisão da gestora. Hoje a comparação é manual, os números vêm dispersos e sem referência, e ela não consegue avaliar se a diferença é relevante. | Alta |
| **T05** | Decidir e justificar a adoção de um modelo | C02; Q12, Q16, Q17; R03 | A decisão é o objetivo central da P03 e envolve autoridade compartilhada com a coordenação; será detalhada na Entrega 5. | Alta |

#### Informações que precisam ser coletadas

| Informação | Origem | Para que serve | Como coletar |
|---|---|---|---|
| Quem decide, com quem e qual a autoridade de Larissa | Q12 | Entender a governança da decisão e o que cabe à gestora | Entrevista com integrante de gestão (perfil P03) e com a coordenação |
| Formato, autoria e antecedência dos resultados que ela recebe | Q11 | Dimensionar a dependência dos colegas técnicos e o tempo disponível para entender os números | Entrevista + análise das planilhas/mensagens |
| Quais métricas ela usa, quais ignora e o que não entende | Q13, Q15 | Delimitar a barreira de interpretação e terminologia | Entrevista + análise das saídas |
| Critério atual para considerar um modelo "melhor" e como lida com diferenças pequenas | Q14 | Revelar o critério implícito e onde ele falha | Observação da reunião + entrevista |
| O que ela leva para a reunião e como sustenta a escolha | Q17 | Entender as necessidades de justificativa perante a coordenação | Observação + análise dos materiais |
| Decisões revistas depois do teste e consequências de uma decisão adiada ou errada | Q16 | Dimensionar impacto e criticidade | Entrevista com integrante de gestão (perfil P03) e com a coordenação |
| Antecedência e momento em que a decisão precisa estar tomada | Q10 | Definir o contexto temporal da tarefa | Entrevista + calendário de testes |

## Cenário C03 - Experimentação e análises de modelos para segmentação

**Autor(a):** Mateus Marana Assuena — 22.123.026-1  
**Persona(s) relacionada(s):** P02 — Andreia Silva  
**Necessidade relacionada:** R03 - Experimentar modelos e acompanhar a evolução da pesquisa.  
**Situação concreta da Entrega 1 relacionada:** Perfil de pesquisador(a) de modelos (§2.2; antes "desenvolvedor de modelos") e decisões de design relacionadas à análise e comparação de segmentações.
**Hipóteses ainda presentes:** H01, H04.

### 1. Cenário inicial

Andreia é professora e coordenadora da equipe Baja FEI, onde acompanha pesquisas e desenvolvimentos voltados à construção de um veículo Baja autônomo. Com formação avançada em Engenharia Mecânica e experiência em Visão Computacional, ela utiliza seus conhecimentos para desenvolver e avaliar modelos de inteligência artificial capazes de interpretar o ambiente off-road.

Durante suas pesquisas, Andreia precisa analisar imagens e vídeos gravados durante os testes do veículo, verificando se diferentes modelos de segmentação conseguem delimitar corretamente a região de trilha. Para isso, utiliza modelos pré-treinados e scripts em Python, executando os modelos e visualizando as máscaras geradas para avaliar seus resultados.

Entretanto, quando deseja experimentar diferentes modelos, precisa realizar configurações e execuções separadamente, utilizando ferramentas e códigos que nem sempre oferecem uma forma prática de visualizar e comparar os resultados. Para analisar uma mesma imagem com modelos diferentes, precisa executar cada um individualmente e alternar entre as saídas geradas, dificultando a identificação de diferenças na segmentação.

Além disso, embora tenha conhecimento para implementar modelos e trabalhar com métricas de Visão Computacional, Andreia não possui muita experiência no desenvolvimento de interfaces. Por isso, organizar todas essas funcionalidades em uma ferramenta própria demandaria tempo adicional de desenvolvimento, que poderia ser direcionado às pesquisas e melhorias do projeto.

Sua rotina como professora e coordenadora também limita o tempo disponível para desenvolver e treinar novos modelos do zero. Assim, ela gostaria de aproveitar modelos pré-treinados e concentrar seus esforços na experimentação, análise e identificação de oportunidades de melhoria.

Em uma de suas análises, Andreia precisa verificar qual modelo apresenta melhores resultados para determinada entrada. Para isso, executa os modelos separadamente, observa as máscaras geradas e consulta métricas para avaliar o desempenho de cada um. Entretanto, a ausência de uma interface que reúna as imagens originais, as máscaras, as sobreposições e as métricas dificulta a comparação dos resultados e torna a análise menos prática.

Esse processo fragmentado consome parte do tempo que Andreia poderia dedicar à pesquisa e ao desenvolvimento do veículo autônomo. Ela gostaria de contar com uma ferramenta centralizada, que permitisse selecionar diferentes modelos, processar imagens e vídeos e analisar seus resultados em uma mesma interface, sem precisar desenvolver toda a estrutura de interação por conta própria.

### 2. Questões de refinamento

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| Q18 | Quais características Andreia considera mais importantes ao escolher um modelo de segmentação para determinado experimento? | Para identificar os critérios utilizados na seleção dos modelos. | Entrevista com pesquisador(a) ou coordenador(a) da equipe (perfil P02). |
| Q19 | Como Andreia realiza atualmente a comparação entre diferentes modelos e quais dificuldades encontra nesse processo? | Para compreender o fluxo atual de experimentação e comparação. | Entrevista e observação das execuções. |
| Q20 | Quais métricas Andreia utiliza para avaliar a qualidade da segmentação e como interpreta seus resultados? | Para identificar quais informações técnicas precisam ser apresentadas pela ferramenta. | Entrevista e análise das métricas utilizadas. |
| Q21 | Quais formatos, resoluções e características os vídeos e imagens utilizados nos experimentos apresentam? | Para identificar requisitos e possíveis limitações do processamento das entradas. | Entrevista e análise dos arquivos utilizados. |
| Q22 | Como Andreia identifica que um modelo apresenta resultados insatisfatórios e quais ações realiza após identificar esses problemas? | Para compreender como os resultados orientam as melhorias nos modelos. | Entrevista e observação. |
| Q23 | Como Andreia organiza e registra os resultados dos experimentos para consultá-los posteriormente? | Para entender se existe uma necessidade real de histórico e registro de observações. | Entrevista e análise dos registros de pesquisa. |
| Q24 | Quais informações Andreia precisa visualizar simultaneamente para analisar uma segmentação de maneira eficiente? | Para identificar as necessidades de visualização e apresentação dos resultados. | Entrevista e observação. |
| Q25 | Como Andreia utiliza os resultados das segmentações no desenvolvimento do veículo Baja autônomo e quem participa das decisões relacionadas à pesquisa? | Para compreender como as análises influenciam o projeto e quais atores dependem dos resultados. | Entrevista com pesquisador(a) ou coordenador(a) da equipe (perfil P02) e com a equipe Baja FEI. |
| Q26 | Quais etapas e configurações são necessárias para executar os modelos sobre imagens e vídeos, e quais dificuldades técnicas podem ocorrer durante o processamento? | Para identificar pré-condições, dependências e possíveis falhas durante a execução. | Entrevista, observação e análise dos scripts. |

### 3. Cenário refinado

> P02 é proto-persona: as respostas abaixo são **hipóteses de trabalho**, não relatos. Precisam ser validadas na Entrega 7.
>
> Marcação conforme a [convenção de refinamento](#convenção-de-marcação-do-refinamento): texto normal = mantido; **negrito** = novo; *itálico* = reescrito/especificado.

Andreia é professora em tempo integral e coordenadora da equipe Baja FEI, onde acompanha pesquisas voltadas ao desenvolvimento de um veículo autônomo para terrenos off-road. Com formação avançada em Engenharia Mecânica e especialização em Visão Computacional, possui conhecimentos para desenvolver modelos próprios e implementar scripts em Python. Entretanto, sua rotina de aulas e compromissos com a equipe limita o tempo disponível para desenvolver e treinar novos modelos.

Durante suas pesquisas, Andreia precisa utilizar modelos de segmentação para analisar imagens e vídeos gravados durante os testes do veículo, buscando identificar quais modelos apresentam melhores resultados para o projeto. [Q21] **Os vídeos vêm das câmeras do veículo e têm resoluções diferentes conforme a câmera; para analisar, ela extrai quadros dos trechos que interessam.** [Q18] **Ao escolher um modelo para um experimento, prioriza a qualidade da borda da trilha em sombra e vegetação densa e, em segundo lugar, o tempo de inferência, pensando no uso futuro no veículo autônomo.** Para isso, utiliza modelos pré-treinados e realiza execuções individuais por meio de scripts em Python.

[Q26] Quando deseja experimentar diferentes modelos, precisa configurá-los e executá-los separadamente, o que dificulta a comparação dos resultados. **Para cada experimento, ajusta a configuração de treino, treina, espera o treino terminar e só então executa o modelo sobre as imagens; quando o treino falha no meio, perde o tempo já gasto.** [Q19] **Para comparar, abre as saídas de cada modelo em janelas lado a lado e anota as diferenças à mão.** Além disso, precisa analisar as imagens originais e as máscaras geradas para identificar possíveis erros na segmentação. [Q24] A ausência de uma visualização conjunta dificulta essa análise, pois precisa alternar entre diferentes saídas para observar as diferenças; **para decidir, precisa ver ao mesmo tempo a imagem original, a máscara, a sobreposição e as métricas do modelo.**

[Q20] Após as execuções, Andreia consulta métricas para avaliar a qualidade das segmentações e identificar quais modelos apresentam resultados mais adequados, **principalmente o IoU da classe trilha e a acurácia; quando o IoU cai, olha a matriz de confusão para entender onde o modelo erra.** [Q22] Quando encontra resultados insatisfatórios, precisa investigar as possíveis causas e considerar melhorias para os próximos experimentos. **Considera um resultado insatisfatório quando a máscara perde a trilha em sombras ou em trechos estreitos; nesses casos, anota o problema e muda a configuração de treino (mais épocas ou outro conjunto de dados) no experimento seguinte.** [Q23] **Registra cada experimento em um caderno de pesquisa, com data, modelo e observações; as saídas ficam em pastas separadas, e encontrar um resultado antigo exige procurar pela data.** [Q25] **As conclusões são levadas à reunião de coordenação, onde a gestão prepara a decisão sobre qual modelo usar nos testes (cenário C02).**

Apesar de possuir conhecimento técnico para desenvolver essas soluções, Andreia tem pouca experiência na construção de interfaces. Dessa forma, criar uma ferramenta própria que reúna execução, visualização e comparação dos modelos exigiria um esforço adicional de desenvolvimento.

Esse processo dificulta a experimentação e consome parte do tempo disponível para suas pesquisas. Andreia gostaria de utilizar uma ferramenta centralizada, com navegação intuitiva e acesso às informações técnicas, que permitisse selecionar diferentes modelos pré-treinados, processar imagens e vídeos e analisar os resultados das segmentações em um mesmo ambiente.

**Resumo do refinamento**

| Questão | Resultado | O que mudou no cenário |
|---|---|---|
| Q18 | Novo | Critério de escolha do modelo: qualidade da borda em sombra e vegetação densa, depois tempo de inferência. |
| Q19 | Novo | Como compara hoje: saídas em janelas lado a lado e anotações à mão. |
| Q20 | Novo | Métricas usadas (IoU da classe trilha, acurácia) e o uso da matriz de confusão quando o IoU cai. |
| Q21 | Novo | Origem e formato das entradas: vídeos das câmeras do veículo, com resoluções diferentes, dos quais ela extrai quadros. |
| Q22 | Novo | O que é resultado insatisfatório (perda da trilha em sombras e trechos estreitos) e o que ela faz (muda a configuração de treino no próximo experimento). |
| Q23 | Novo | Registro atual: caderno de pesquisa e pastas por data; recuperar um resultado antigo exige procurar pela data (relevante para a H08). |
| Q24 | Novo | O que precisa ver ao mesmo tempo: imagem original, máscara, sobreposição e métricas. |
| Q25 | Novo | Para onde vão as conclusões: reunião de coordenação, ligada à decisão do C02. |
| Q26 | Novo | Etapas de um experimento (configurar, treinar, executar) e a perda de tempo quando o treino falha. |

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| **Ator(es)** | Andreia Silva e equipe Baja FEI. |
| **Objetivo(s)** | Avaliar diferentes modelos de segmentação para identificar aqueles que apresentam melhores resultados e contribuir para o desenvolvimento de um veículo Baja autônomo. |
| **Contexto** | Pesquisas e testes da equipe Baja FEI voltados à construção de um veículo autônomo para terrenos off-road. Andreia utiliza modelos pré-treinados e scripts em Python, mas possui tempo limitado para desenvolver ferramentas auxiliares. |
| **Recursos/informações** | Imagens, vídeos gravados, modelos pré-treinados, scripts em Python, máscaras de segmentação e métricas de avaliação. |
| **Ações** | Selecionar modelos; configurar execuções; processar imagens e vídeos; visualizar máscaras; analisar métricas; comparar resultados; identificar possíveis melhorias. |
| **Problemas/rupturas** | Execuções individuais para experimentar diferentes modelos; dificuldade para comparar resultados; necessidade de alternar entre diferentes saídas; falta de uma interface centralizada; pouco tempo disponível para desenvolver ferramentas próprias. |
| **Consequências** | Andreia gasta tempo com atividades operacionais, encontra dificuldades para comparar os resultados e possui menos tempo disponível para se dedicar à pesquisa e ao desenvolvimento do veículo autônomo. |

### 5. Implicações para as próximas entregas

**Tarefas que merecem análise**

| ID | Tarefa | Origem no cenário | Por que merece análise | Prioridade |
|---|---|---|---|---|
| T02 | Executar a segmentação com uma ou mais configurações disponíveis *(tarefa compartilhada com o C01; antes T07 neste cenário)* | C03; P02; Q18, Q21, Q26 | É a atividade central da experimentação. Andreia precisa executar diferentes modelos sobre entradas para avaliar seus resultados. | Alta |
| T06 | Analisar visualmente os resultados da segmentação *(antes T08)* | C03; P02; Q22, Q24 | Permite identificar erros e verificar se o modelo está identificando corretamente as regiões de interesse. A visualização da imagem original, máscara e sobreposição pode facilitar essa atividade. | Alta |
| T07 | Comparar os resultados de diferentes modelos de segmentação *(antes T09)* | C03; P02; Q18, Q19, Q20 | É fundamental para identificar quais modelos apresentam melhor desempenho e podem contribuir para o desenvolvimento do veículo autônomo. | Alta |
| T08 | Definir uma configuração de treino e treinar o modelo *(criada em 08/11/2026; não confundir com o antigo T08 deste cenário, hoje T06)* | C03; P02; Q18, Q26 | Andreia quer experimentar modelos sem gastar tempo desenvolvendo e treinando do zero; definir a configuração (modelo, épocas, early stopping, datasets, batch size) e treinar pela interface é o que permite comparar alternativas depois. | Média |

**Informações que precisam ser coletadas**

| Informação | Origem | Para que serve | Como coletar |
|---|---|---|---|
| Critérios utilizados para selecionar os modelos de segmentação | Q18 | Identifica os fatores considerados na escolha dos modelos. | Entrevista com pesquisador(a) ou coordenador(a) da equipe (perfil P02). |
| Processo atual de execução e comparação dos modelos | Q19, Q26 | Compreende as etapas, configurações e dificuldades da experimentação. | Entrevista + observação dos scripts. |
| Métricas utilizadas e critérios de avaliação dos resultados | Q20 | Define quais indicadores devem ser apresentados para apoiar a análise. | Entrevista + análise dos resultados existentes. |
| Formatos, resoluções e características das imagens e vídeos utilizados | Q21 | Identifica requisitos e limitações das entradas aceitas pelo sistema. | Entrevista + análise dos arquivos. |
| Como identifica resultados insatisfatórios e quais melhorias realiza | Q22 | Compreende como a análise dos resultados orienta novas experimentações. | Entrevista + observação. |
| Como registra e recupera resultados de experimentos anteriores | Q23 | Verifica se existe necessidade de histórico, armazenamento e registro de observações. | Entrevista + análise dos registros existentes. |
| Informações visuais necessárias para analisar uma segmentação | Q24 | Define os elementos que precisam estar disponíveis na interface de análise. | Entrevista + prototipação e avaliação. |
| Como os resultados são utilizados nas decisões do projeto Baja | Q25 | Identifica a importância dos resultados para a pesquisa e os demais envolvidos. | Entrevista com pesquisador(a) ou coordenador(a) da equipe (perfil P02) e com a equipe. |
| Recursos computacionais e dependências necessárias para executar os modelos | Q26 | Identifica possíveis limitações técnicas durante o processamento. | Análise dos scripts e ambiente de execução. |

## Checklist

- [X] Há um cenário completo por integrante.
- [X] Cada cenário tem título, ator, objetivo, contexto e problema.
- [X] O cenário possui origem rastreável na Entrega 1 ou justifica claramente a inclusão de uma nova situação.
- [X] O texto descreve a situação atual, sem antecipar a solução.
- [ ] Para TCC sem interface original, o cenário descreve uma prática humana plausível relacionada à contribuição técnica, e não “a falta de uma tela”. *(Não se aplica: o TCC prevê interface.)*
- [X] Questões de refinamento acrescentam informação nova.
- [X] O refinamento mostra claramente o que foi adicionado/alterado.
- [X] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [X] Cada cenário está ligado a persona/necessidade na matriz de rastreabilidade.

## Histórico de revisões

| Data | O que mudou | Motivo |
|---|---|---|
| 30/10/2026 | T03 e T04 renomeadas para deixarem de ter o mesmo nome; convenção de marcação do refinamento; nomes completos na autoria; fonte "Entrevista com Larissa" substituída por perfil (C02) | Revisão de consistência (`PENDENCIAS.md`: INC-02, INC-04, INC-47, INC-48) |
| 08/11/2026 | IDs das tarefas do C03 alinhados aos da Entrega 5 (T07 → T02 compartilhada, T08 → T06, T09 → T07) e origem corrigida para C03; marcações do refinamento do C03 trocadas pelas questões do próprio cenário (Q19–Q26). T02 renomeada para "Executar a segmentação com uma ou mais configurações disponíveis". Classes alinhadas ao TCC (região de trilha). "Coordenação" do C02 ligada à P02. Métricas do C01 restritas a imagens com anotação de referência | Revisão de consistência (`PENDENCIAS.md`: INC-05, INC-12, INC-49, INC-52, INC-56, INC-58) e leitura do repositório do TCC |
| 09/11/2026 | Criada a T08 no C03 (definir uma configuração de treino e treinar o modelo), depois que configurar e treinar entrou no recorte | Revisão de consistência (`PENDENCIAS.md`: INC-61) |
| 10/11/2026 | Cabeçalho do C01 preenchido; Q2 e Q4 do C01 reformuladas; refinamentos do C01 e do C03 reescritos com respostas hipotéticas marcadas e resumo do que mudou; Q11, Q13 e Q16 do C02 reformuladas e respondidas; fontes deixam de citar personas como entrevistados; checklist revisto | Revisão de consistência (`PENDENCIAS.md`: INC-04, INC-44, INC-45, INC-46, INC-50, INC-51, INC-62). Rascunhos do C01 e do C03 a revisar pelo Tiago e pelo Mateus |
