# Entrega 4 — Cenários de análise/problema

**Data:** 20/10/2026  
**Status:** 🟨 em andamento 
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

## Cenário C01 — Validação manual de segmentação em campo

**Autor(a):** Tiago - 22.123.017-0
**Persona(s) relacionada(s):** Rafael Pereira  
**Necessidade relacionada:** {{R01}}?  
**Situação concreta da Entrega 1 relacionada:** {{seção 4.4 / H01 / outra ou “nova situação justificada”}}?  
**Hipóteses ainda presentes:** {{H01, H02 ou —}}?

### 1. Cenário inicial

Rafael acompanha os testes do Baja em terrenos off‑road dentro da FEI, ele coleta imagens com câmeras acopladas ao veículo e precisa validar se o modelo de segmentação está identificando corretamente áreas transitáveis. Atualmente, esse processo depende de scripts em Python, Rafael precisa abrir cada imagem, rodar o código manualmente e gerar a máscara de segmentação. Quando o script quebra ou apresenta erro, ele perde tempo depurando, mesmo não sendo desenvolvedor. Além disso, cada execução gera arquivos separados que precisam ser organizados manualmente em pastas, sem padrão definido. Em uma das execuções, o script termina, mas a máscara gerada cobre quase toda a pista com uma única cor. Sem informação sobre a confiança do resultado, Rafael não consegue dizer se a falha é do modelo ou da imagem. Ele tenta rodar novamente com outra configuração, abre as duas máscaras em janelas separadas e compara manualmente, mas as métricas ficaram em planilhas diferentes e ele perde o fio da comparação. Esse processo improvisado de comparação manual gera frustração, ele sente que perde tempo com tarefas repetitivas e que a análise não é clara o bastante para apoiar decisões rápidas da equipe.

### 2. Questões de refinamento

Use os tipos de questões/taxonomia definidos na aula. As perguntas devem revelar informações **ainda ausentes** do cenário, não repetir o que já foi respondido.

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| Q1 | Por que Rafael precisa validar a segmentação e o que espera obter com isso? | Para entender o objetivo real da atividade e os resultados esperados. | Entrevista com Rafael. |
| Q2 | Quais problemas surgem quando o script falha em campo? | Para detalhar erros, consequências e estratégias alternativas. | logs de execução. |
| Q3 | Como Rafael organiza atualmente os arquivos gerados pelos scripts? | Para revelar detalhes da sequência de ações e dificuldades com gestão de dados. | Análise dos diretórios. |
| Q4 | Quem depende diretamente dos resultados das análises de Rafael? | Para mapear atores que consomem as informações e precisam ser notificados. | Entrevista com Equipe Baja FEI. |
| Q5 | Como Rafael decide qual modelo ou versão comparar em cada teste? | Para entender o planejamento e critérios de escolha. | Discussões técnicas na Equipe Baja FEI. |
| Q6 | Quem participa da validação, quem fornece as imagens e quem consome ou precisa ser notificado do resultado? | Para mapear atores envolvidos e dependências. | Equipe Baja FEI. |
| Q7 | Como Rafael decide se uma máscara está correta e como sabe que a validação foi concluída com sucesso? O que faz quando não tem certeza? | Para definir critérios de avaliação e indicadores de confiança. | Equipe Baja FEI e Métricas de acurácia. |
| Q8 | Quais são os passos e pré-condições da execução? Que erros podem ocorrer, como Rafael os identifica e contorna? |Para detalhar sequência de ações e falhas comuns. | Entrevista com Rafael e logs. |
| Q9 | Quando, onde e por que a validação acontece? |Para detalhar o ambiente/contexto e suas limitações. | Entrevista com Equipe Baja Fei |

### 3. Cenário refinado

Rafael acompanha os testes do Baja em terrenos off-road dentro da FEI e coleta imagens com câmeras acopladas ao veículo. [Q9] Ele é quem realiza a validação, as imagens são fornecidas pelas câmeras do veículo, e o resultado é consumido pela equipe, que precisa ser informada para tomar decisões rápidas. [Q6] [Q4] O objetivo é validar se o modelo de segmentação está identificando corretamente as áreas transitáveis. [Q1] Para isso, ele depende de scripts em Python. Rafael abre cada imagem, roda o código manualmente e gera a máscara de segmentação. [Q8] Quando o script quebra ou apresenta erro, ele perde tempo depurando, mesmo não sendo desenvolvedor. [Q2] Cada execução gera arquivos separados, que precisam ser organizados manualmente em pastas, sem um padrão definido. [Q3] Em uma das execuções, o script termina, mas a máscara gerada cobre quase toda a pista com uma única cor. Sem informação sobre a confiança do resultado, Rafael não consegue dizer se a falha é do modelo ou da imagem. [Q7] Ele tenta rodar novamente com outra configuração, abre as duas máscaras em janelas separadas e compara manualmente, mas as métricas ficaram em planilhas diferentes e ele perde o fio da comparação. [Q5] [Q7] Esse processo improvisado de comparação manual gera frustração: ele sente que perde tempo com tarefas repetitivas e que a análise não é clara o bastante para apoiar decisões rápidas da equipe. [Q4]

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | Rafael e Equipe Baja FEI |
| Objetivo(s) | Validar se o modelo de segmentação está identificando corretamente as áreas transitáveis e apoiar nas decisões rápidas da equipe. |
| Contexto | Testes do Baja em terrenos off-road dentro da FEI, o processo depende de scripts em Python e cada execução gera arquivos separados, sem um padrão definido. |
| Recursos/informações |  Câmeras acopladas ao veículo, scripts em Python, máscara de segmentação e  métricas do resultado |
| Ações | Abrir cada imagem; rodar o código manualmente; gerar a máscara de segmentação; organizar manualmente os arquivos, comparar resultados manualmente; informar a equipe sobre o resultado. |
| Problemas/rupturas | O script quebra ou apresenta erro e Rafael perde tempo depurando, mesmo não sendo desenvolvedor; arquivos ficam sem um padrão definido; a máscara cobre quase toda a pista com uma única cor; sem informação sobre a confiança do resultado, não consegue dizer se a falha é do modelo ou da imagem; as métricas em planilhas diferentes fazem perder o fio da comparação; a comparação é manual e improvisada. |
| Consequências | Rafael perde tempo com tarefas repetitivas, sente frustração, perde o fio da comparação e a análise não é clara o bastante para apoiar decisões rápidas da equipe. |

### 5. Implicações para as próximas entregas

<!-- Quais tarefas merecem análise? Quais informações precisam ser coletadas? **Não desenhe a solução ainda.** -->
#### Tarefas que merecem análise

| ID | Tarefa | Origem no cenário | Por que merece análise | Prioridade |
|---|---|---|---|---|
| **T01** | Avaliar a qualidade da segmentação de uma imagem | C01; Q1, Q7; R01 | É o núcleo da validação: comparar imagem e máscara, interpretar classes/métricas e decidir se o resultado é confiável. A ausência de informação de confiança e de critério explícito torna a tarefa crítica. | Alta |
| **T02** | Executar a segmentação de imagens com uma configuração disponível | C01; Q2, Q8; R02 | É a entrada da atividade: abrir cada imagem, rodar o script, gerar a máscara e lidar com falhas. A depuração interrompe o fluxo e consome tempo. | Alta |
| **T03** | Comparar resultados entre configurações/modelos | C01; Q4, Q5, Q7; R03 | Sustenta a decisão da equipe sobre qual configuração usar. Hoje a comparação é manual, as métricas ficam dispersas e Rafael perde o fio da comparação. | Alta |

#### Informações que precisam ser coletadas

| Informação | Origem | Para que serve | Como coletar |
|---|---|---|---|
| Quando, onde e com que frequência a validação acontece; duração e quantidade de imagens por sessão | Q9, Q2 | Define o contexto real e as restrições da tarefa | Entrevista com Rafael + observação |
| Quem executa, quem fornece as imagens, quem consome o resultado, quem decide e quem precisa ser notificado | Q4, Q6 | Mapeia atores, dependências e destinatários | Entrevista com Rafael e com a equipe |
| Como Rafael escolhe a configuração a comparar e quem decide a adoção | Q5 | Entende o planejamento e a autoridade de decisão | Entrevista com Rafael e com a gestão |
| Critérios para considerar uma máscara correta; sinais de confiança; o que faz quando tem dúvida | Q7 | Define o que é “sucesso” na validação | Entrevista + observação |
| Passos, pré-condições e erros da execução; como identifica e contorna cada erro | Q8, Q2 | Identifica pontos de falha e recuperação | Observação + entrevista + logs, se existirem |
| Estrutura de pastas, nomes dos arquivos e local onde ficam as métricas | Q3 | Entende como os resultados são organizados e recuperados | Análise dos diretórios/planilhas + entrevista |
| Métricas usadas (IoU, acurácia, por classe), como são lidas e comparadas | Q7 | Define quais informações sustentam a avaliação | Entrevista + análise das planilhas/saídas |
| Consequências da falha ou de uma validação inconclusiva | Q2, Q4 | Dimensiona o impacto e a criticidade | Entrevista com Rafael e com a equipe |

## Cenário C02 — Decisão de modelo a partir de resultados dispersos

**Autor(a):** Henrique — 22.123.030-3  
**Persona(s) relacionada(s):** P03 — Larissa Camargo  
**Necessidade relacionada:** R03 — comparar desempenho entre modelos (P03: decidir)  
**Situação concreta da Entrega 1 relacionada:** **Nova situação justificada** — perfil "Gestor de projeto" (01 §2.2 `[H]`) e contexto organizacional (01 §5.4); a E1 não registra situação observada da P03.  
**Hipóteses ainda presentes:** H01, H04, H06, H12

> **Justificativa da nova situação:** a E1 reconhece o perfil "Gestor de projeto" (§2.2) como quem consulta resultados consolidados e decide qual modelo usar, mas não descreve uma situação concreta desse perfil. A decisão é condição para os testes do veículo e depende do resultado produzido pela P01. Por isso o cenário é relevante. A situação é **hipotética** (P03 é proto-persona) e precisa ser validada na Entrega 7.

### 1. Cenário inicial

Larissa Camargo é gestora de projeto da equipe Baja FEI. Antes de um ciclo de testes do veículo, ela precisa definir qual configuração do modelo de segmentação será adotada. A decisão é discutida com a coordenação em uma reunião semanal, mas quem executa os modelos é um integrante técnico da equipe — Larissa não escreve código nem domina machine learning ou estatística.

Para decidir, ela recebe desse integrante, por mensagens e planilhas separadas, números de IoU e acurácia de cada configuração testada, cada uma em uma execução diferente. Os valores chegam sem uma referência do que seria um bom resultado e sem indicar o que cada métrica significa na prática. Larissa compara os números manualmente, em abas e arquivos distintos, e não consegue avaliar se a diferença entre dois modelos é relevante ou apenas variação do teste.

Quando precisa levar a decisão à coordenação, ela tem dificuldade de explicar por que um modelo é melhor que outro e de sustentar a escolha. Sem critério claro, a decisão é adiada ou tomada pelo número aparentemente maior, sem justificativa. Isso aumenta o risco de adotar um modelo inadequado ao terreno e de a equipe refazer a análise depois. Larissa sente que depende dos colegas técnicos para entender o resultado e que decide sem segurança.

### 2. Questões de refinamento

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| Q10 | Por que a decisão precisa ocorrer antes do teste e o que se espera dela? | Entender o objetivo real da decisão e o que seria uma escolha bem-sucedida. | Entrevista com Larissa e coordenação. |
| Q11 | Como os resultados chegam até Larissa hoje: formato, quem envia e com que frequência? | Revelar o fluxo atual de informação e as dependências entre os atores. | Entrevista com Larissa + análise das planilhas e mensagens. |
| Q12 | Quem participa da decisão e qual é a autoridade de Larissa em relação à coordenação? | Mapear papéis, responsabilidades e quem tem a palavra final. | Entrevista com Larissa e coordenação. |
| Q13 | Quais métricas ela recebe e como interpreta cada uma? | Identificar o que ela entende e onde precisa de apoio. | Entrevista + análise das saídas de segmentação. |
| Q14 | Como ela compara modelos ou versões e define qual é o "melhor"? | Entender o critério atual de comparação e suas limitações. | Observação da reunião + entrevista. |
| Q15 | Que termos técnicos ela não entende e precisa que alguém explique? | Delimitar a barreira de terminologia (RC01). | Entrevista com Larissa. |
| Q16 | O que acontece quando a decisão é adiada ou errada? | Dimensionar a consequência e a criticidade da decisão. | Entrevista com Larissa e coordenação. |
| Q17 | O que ela leva para a reunião e como justifica a escolha? | Entender o material de apoio e a dificuldade de sustentar a recomendação. | Observação + análise dos materiais levados. |

### 3. Cenário refinado

> P03 é proto-persona: as respostas abaixo são **hipóteses de trabalho**, não relatos. Precisam ser validadas na Entrega 7.

Larissa Camargo é gestora de projeto da equipe Baja FEI. [Q10] A decisão precisa ocorrer antes de cada ciclo de testes porque a configuração escolhida será usada no veículo; o que se espera é uma escolha defensável, não apenas o maior número. [Q12] A decisão é compartilhada com a coordenação: Larissa reúne e recomenda, e a palavra final é discutida no grupo. [Q11] Hoje os resultados chegam por mensagens e planilhas separadas, enviados pelo integrante que executa os modelos, cada configuração em uma execução. [Q13] Ela recebe IoU e acurácia, mas não tem referência de comparação nem explicação do que cada valor significa na prática. **[NOVO: quando a diferença entre dois modelos é pequena, ela não sabe dizer se é relevante.]** [Q14] Para comparar, abre as planilhas lado a lado e escolhe pelo número maior quando não há outro critério. [Q15] Termos como IoU, acurácia por classe e "transitável × não transitável" geram dúvida e dependem de um colega para serem explicados. [Q17] Na reunião, leva os números e tenta justificar a escolha, mas tem dificuldade de sustentar a recomendação. [Q16] Quando adia ou escolhe sem critério, o teste pode usar um modelo inadequado e a equipe precisa refazer a análise depois. Larissa sente que depende dos colegas técnicos e que decide sem segurança.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | Larissa (gestora), o integrante técnico que executa os modelos e a coordenação na decisão. |
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
| **T04** | Comparar resultados entre configurações/modelos | C02; Q13, Q14; R03 | É a base da decisão da gestora. Hoje a comparação é manual, os números vêm dispersos e sem referência, e ela não consegue avaliar se a diferença é relevante. | Alta |
| **T05** | Decidir e justificar a adoção de um modelo | C02; Q12, Q16, Q17; R03 | A decisão é o objetivo central da P03 e envolve autoridade compartilhada com a coordenação; será detalhada na Entrega 5. | Alta |

#### Informações que precisam ser coletadas

| Informação | Origem | Para que serve | Como coletar |
|---|---|---|---|
| Quem decide, com quem e qual a autoridade de Larissa | Q12 | Entender a governança da decisão e o que cabe à gestora | Entrevista com Larissa e coordenação |
| Formato, frequência e autoria dos resultados que ela recebe | Q11 | Dimensionar a dependência dos colegas técnicos e o fluxo atual | Entrevista + análise das planilhas/mensagens |
| Quais métricas ela usa, como lê e o que não entende | Q13, Q15 | Delimitar a barreira de interpretação e terminologia | Entrevista + análise das saídas |
| Critério atual para considerar um modelo "melhor" e como lida com diferenças pequenas | Q14 | Revelar o critério implícito e onde ele falha | Observação da reunião + entrevista |
| O que ela leva para a reunião e como sustenta a escolha | Q17 | Entender as necessidades de justificativa perante a coordenação | Observação + análise dos materiais |
| Consequências de uma decisão adiada ou errada | Q16 | Dimensionar impacto e criticidade | Entrevista com Larissa e coordenação |
| Antecedência e momento em que a decisão precisa estar tomada | Q10 | Definir o contexto temporal da tarefa | Entrevista + calendário de testes |

## Checklist

- [ ] Há um cenário completo por integrante.
- [ ] Cada cenário tem título, ator, objetivo, contexto e problema.
- [ ] O cenário possui origem rastreável na Entrega 1 ou justifica claramente a inclusão de uma nova situação.
- [ ] O texto descreve a situação atual, sem antecipar a solução.
- [ ] Para TCC sem interface original, o cenário descreve uma prática humana plausível relacionada à contribuição técnica, e não “a falta de uma tela”.
- [ ] Questões de refinamento acrescentam informação nova.
- [ ] O refinamento mostra claramente o que foi adicionado/alterado.
- [ ] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [ ] Cada cenário está ligado a persona/necessidade na matriz de rastreabilidade.
