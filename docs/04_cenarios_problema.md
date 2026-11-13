# Entrega 4 — Cenários de análise/problema

**Data:** 20/10/2026 · 11/11/2026 (revisão após feedback)  
**Status:** 🟦 revisada após feedback  
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

Cada questão indica o **elemento do cenário** que investiga: ambiente/contexto, atores, objetivos, planejamento, ações, eventos ou avaliação. Cada cenário tem pelo menos uma questão válida para cada elemento. **Planejamento** é o plano mental (escolher uma estratégia de comparação); **ação** é o comportamento observável (abrir arquivos). **Evento** é o que acontece fora do controle do usuário (um retorno inesperado da execução); **avaliação** é como ele interpreta o que aconteceu e decide se a atividade foi concluída.

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

| # | Elemento | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|---|
| Q1 | Objetivos | Por que Rafael precisa validar a segmentação e o que espera obter com isso? | Para entender o objetivo real da atividade e os resultados esperados. | Entrevista com integrante que faz a análise de segmentação (perfil P01). |
| Q2 | Eventos | Que consequência uma falha na execução tem para o teste do dia? | Para dimensionar o impacto da falha, separado dos erros em si (Q8). | Entrevista com integrante que faz a análise de segmentação (perfil P01) e com a equipe. |
| Q3 | Ações | Como Rafael organiza atualmente os arquivos gerados pelos scripts? | Para revelar detalhes da sequência de ações e dificuldades com gestão de dados. | Análise dos diretórios. |
| Q4 | Atores | Quem decide a partir do resultado da validação, que decisão é essa e quem só precisa ser informado? | Para separar quem analisa, quem decide e quem é informado (Q6 trata de quem participa da validação). | Entrevista com a equipe Baja FEI. |
| Q5 | Planejamento | Por que Rafael escolhe determinada configuração para comparar e que critério usa? | Para entender o planejamento e o critério de escolha. | Discussões técnicas na Equipe Baja FEI. |
| Q6 | Atores | Quem participa da validação e quem fornece as imagens? | Para mapear atores envolvidos e dependências. | Equipe Baja FEI. |
| Q7 | Avaliação | Como Rafael decide se uma máscara está correta e como sabe que a validação foi concluída com sucesso? O que faz quando não tem certeza? | Para definir critérios de avaliação e indicadores de confiança. | Equipe Baja FEI e Métricas de acurácia. |
| Q8 | Ações e eventos | Quais são os passos e pré-condições da execução? Que erros podem ocorrer, como Rafael os identifica e contorna? |Para detalhar sequência de ações e falhas comuns. | Entrevista com integrante que faz a análise de segmentação (perfil P01) + logs, se existirem. |
| Q9 | Ambiente/contexto | Quando, onde e por que a validação acontece? |Para detalhar o ambiente/contexto e suas limitações. | Entrevista com a equipe Baja FEI. |

### 3. Cenário refinado

> P01 é proto-persona: as respostas abaixo são **hipóteses de trabalho**, não relatos. Precisam ser validadas na Entrega 7.
>
> Marcação conforme a [convenção de refinamento](#convenção-de-marcação-do-refinamento): texto normal = mantido; **negrito** = novo; *itálico* = reescrito/especificado.

Rafael acompanha os testes do Baja em terrenos off-road dentro da FEI e coleta imagens com câmeras acopladas ao veículo. [Q9] **A validação acontece no laboratório, no mesmo dia do teste ou no dia seguinte, sobre algumas dezenas de imagens escolhidas dos trechos mais difíceis do percurso.** [Q6] **Rafael é quem executa a validação, sozinho; as imagens são descarregadas das câmeras por quem acompanhou o teste.** [Q1] Ele precisa validar se o modelo de segmentação está delimitando corretamente a região de trilha **para dizer à equipe, antes do próximo teste, se a configuração em uso pode continuar sendo usada.** [Q4] **Quem decide se a configuração é mantida ou se é preciso compará-la com outra é a gestão (P03), com a coordenação (P02), na reunião semanal; o grupo da equipe, incluindo quem pilota, só precisa ser informado da configuração que vai para o próximo teste.** Atualmente, esse processo depende de scripts em Python: Rafael precisa abrir cada imagem, rodar o código manualmente e gerar a máscara de segmentação. [Q8] **Antes de rodar, confere se as imagens estão na pasta esperada e qual modelo está selecionado; os erros mais comuns são imagem em formato não aceito e arquivo fora da pasta esperada, e ele só percebe quando a execução para.** Quando o script quebra ou apresenta erro, ele perde tempo depurando, *pois, embora programe em Python no curso, não conhece os scripts do projeto por dentro*. [Q2] **Se a falha acontece no dia do teste, a equipe fica sem a resposta e segue com a configuração anterior sem saber se ela está adequada.** [Q3] Cada execução gera arquivos separados, que precisam ser organizados manualmente em pastas, sem um padrão definido; **ele nomeia as pastas pela data do teste, mas as métricas ficam em planilhas à parte.** Em uma das execuções, o script termina, mas a máscara gerada cobre quase toda a pista com uma única cor. Sem informação sobre a confiança do resultado, Rafael não consegue dizer se a falha é do modelo ou da imagem. [Q7] **Ele considera uma máscara correta quando a borda da trilha coincide com o que vê na imagem original; quando não tem certeza, pede a opinião de um colega e marca a imagem como duvidosa. Considera a validação concluída quando todas as imagens escolhidas estão marcadas como corretas ou duvidosas e a resposta foi enviada ao grupo; quando as duvidosas são muitas, percebe que não conseguiu concluir e que precisa comparar com outra configuração.** [Q5] Ele tenta rodar novamente com outra configuração, *em geral a mais recente que alguém da equipe treinou*. **Supõe que a mais recente seja a melhor e não confere as métricas antes de escolher, porque elas estão em outra planilha.** Depois, abre as duas máscaras em janelas separadas e compara manualmente, mas as métricas ficaram em planilhas diferentes e ele perde o fio da comparação. Esse processo improvisado de comparação manual gera frustração: ele sente que perde tempo com tarefas repetitivas e que a análise não é clara o bastante para apoiar decisões rápidas da equipe.

#### Resumo do refinamento

| Questão | Resultado | O que mudou no cenário |
|---|---|---|
| Q1 | Novo | Para que serve a validação: dizer à equipe, antes do próximo teste, se a configuração em uso pode continuar. |
| Q2 | Novo | Consequência de uma falha no dia do teste: a equipe segue sem saber se a configuração está adequada. |
| Q3 | Novo | Como os arquivos são organizados hoje: pastas por data do teste e métricas em planilhas à parte. |
| Q4 | Novo | Quem decide (gestão com a coordenação, na reunião), qual decisão (manter a configuração ou pedir comparação) e quem só é informado (o grupo da equipe). |
| Q5 | Reescrito e novo | Reescrito: a "outra configuração" é, em geral, a mais recente treinada pela equipe. Novo: o critério é a suposição de que a mais recente é a melhor, sem conferir as métricas. |
| Q6 | Novo | Rafael executa sozinho; quem acompanhou o teste fornece as imagens. |
| Q7 | Novo | Critério de correção (borda da trilha coincide com a imagem), o que ele faz na dúvida (consulta um colega e marca a imagem) e quando considera a validação concluída ou percebe que não concluiu. |
| Q8 | Novo | Pré-condições (imagens na pasta, modelo selecionado) e erros mais comuns, percebidos só quando a execução para. |
| Q9 | Novo | Quando e onde: no laboratório, no dia do teste ou no seguinte, com algumas dezenas de imagens dos trechos mais difíceis. |
| — | Reescrito | "Mesmo não sendo desenvolvedor" passa a "programa em Python no curso, mas não conhece os scripts do projeto por dentro", compatível com a P01. |

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ambiente/contexto | Laboratório da FEI, no dia do teste ou no seguinte, depois de testes off-road dentro da FEI; o processo depende de scripts em Python (Q9). |
| Atores | Rafael (executa a validação), quem acompanhou o teste (fornece as imagens), gestão e coordenação (decidem) e grupo da equipe (é informado) (Q4, Q6). |
| Objetivos | Dizer à equipe, antes do próximo teste, se a configuração em uso pode continuar (Q1). |
| Planejamento | Escolhe imagens dos trechos mais difíceis; para comparar, escolhe a configuração mais recente, supondo que seja a melhor (Q5, Q9). |
| Ações | Confere pasta e modelo; abre cada imagem; roda o script; organiza as saídas em pastas por data; abre as máscaras em janelas separadas; envia a resposta ao grupo (Q3, Q8). |
| Eventos | A execução para por imagem em formato não aceito ou fora da pasta; a máscara cobre quase toda a pista com uma única cor (Q2, Q8). |
| Avaliação | Considera a máscara correta quando a borda da trilha coincide com a imagem; marca as duvidosas; conclui quando todas estão marcadas e a resposta foi enviada, ou percebe que não concluiu (Q7). |
| Recursos/informações |  Câmeras acopladas ao veículo, scripts em Python, máscara de segmentação e métricas de cada modelo (IoU e acurácia só existem para imagens com anotação de referência; para imagens novas de campo, a avaliação é visual) |
| Ações | Abrir cada imagem; rodar o código manualmente; gerar a máscara de segmentação; organizar manualmente os arquivos, comparar resultados manualmente; informar a equipe sobre o resultado. |
| Problemas/rupturas | O script quebra ou apresenta erro e Rafael perde tempo depurando, sem conhecer os scripts do projeto por dentro; arquivos ficam sem um padrão definido; a máscara cobre quase toda a pista com uma única cor; sem informação sobre a confiança do resultado, não consegue dizer se a falha é do modelo ou da imagem; as métricas em planilhas diferentes fazem perder o fio da comparação; a comparação é manual e improvisada. |
| Consequências | Rafael perde tempo com tarefas repetitivas, sente frustração, perde o fio da comparação e a análise não é clara o bastante para apoiar decisões rápidas da equipe; se a falha ocorre no dia do teste, a equipe segue com a configuração anterior sem saber se ela está adequada (Q2). |

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

| # | Elemento | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|---|
| Q10 | Objetivos | Por que a decisão precisa ocorrer antes do teste e o que se espera dela? | Entender o objetivo real da decisão e o que seria uma escolha bem-sucedida. | Entrevista com integrante de gestão (perfil P03) e com a coordenação. |
| Q11 | Ambiente/contexto | Com que antecedência os resultados chegam antes da reunião de decisão? | Saber se há tempo para entender os números e tirar dúvidas antes de decidir. | Entrevista com integrante de gestão (perfil P03) + análise das mensagens. |
| Q12 | Atores | Quem participa da decisão e qual é a autoridade de Larissa em relação à coordenação? | Mapear papéis, responsabilidades e quem tem a palavra final. | Entrevista com integrante de gestão (perfil P03) e com a coordenação. |
| Q13 | Avaliação | Quais métricas ela recebe e não usa, e por quê? | Identificar o que é descartado por falta de entendimento ou de critério. | Entrevista + análise das saídas de segmentação. |
| Q14 | Planejamento | Como ela compara modelos ou versões e define qual é o "melhor"? | Entender o critério atual de comparação e suas limitações. | Observação da reunião + entrevista. |
| Q15 | Avaliação | Que termos técnicos ela não entende e precisa que alguém explique? | Delimitar a barreira de terminologia (RC01). | Entrevista com integrante de gestão (perfil P03). |
| Q16 | Eventos | Já houve uma decisão revista depois do teste? O que motivou a revisão? | Dimensionar a consequência de uma decisão errada a partir de um caso concreto. | Entrevista com integrante de gestão (perfil P03) e com a coordenação. |
| Q17 | Ações | O que ela leva para a reunião e como justifica a escolha? | Entender o material de apoio e a dificuldade de sustentar a recomendação. | Observação + análise dos materiais levados. |

### 3. Cenário refinado

> P03 é proto-persona: as respostas abaixo são **hipóteses de trabalho**, não relatos. Precisam ser validadas na Entrega 7.
>
> Marcação conforme a [convenção de refinamento](#convenção-de-marcação-do-refinamento): texto normal = mantido; **negrito** = novo; *itálico* = reescrito/especificado.

Larissa Camargo é gestora de projeto da equipe Baja FEI e não escreve código nem domina machine learning ou estatística. [Q10] **A decisão precisa ocorrer antes de cada ciclo de testes porque a configuração escolhida será usada no veículo; o que se espera é uma escolha defensável, não apenas o maior número.** [Q12] **A decisão é compartilhada com a coordenação: Larissa reúne os resultados e recomenda, e a palavra final é discutida no grupo.**

**O episódio a seguir é uma situação construída pela equipe `[H]`.** [Q11] Na semana anterior a um ciclo de testes, os resultados chegam por mensagens e planilhas separadas, enviados pelo integrante que executa os modelos, cada configuração em uma execução. **Chegam na véspera da reunião, sem tempo para ela tirar dúvidas com quem executou. São duas configurações: uma com IoU médio de 0,78 e outra com 0,76, ambos calculados no conjunto de teste anotado.** [Q13] Ela recebe IoU e acurácia, mas não tem referência de comparação nem explicação do que cada valor significa na prática. **Também recebe o tempo de inferência e números por classe, mas ignora os dois, porque não sabe como pesam na decisão.** [Q15] **Termos como IoU, acurácia por classe e o que a região de "trilha" representa geram dúvida e dependem de um colega para serem explicados.** [Q14] Para comparar, *abre as duas planilhas lado a lado e procura o maior valor de cada métrica*; **como a diferença é de 0,02, não sabe dizer se é relevante e decide recomendar a configuração de 0,78, por falta de outro critério.** [Q17] Na reunião, **leva um print das duas planilhas, com o maior valor destacado à mão. A coordenação (P02) pergunta se 0,02 de diferença importa e se a configuração foi vista em imagens com sombra; Larissa não sabe responder e repete que o número é maior. A recomendação é aceita sem convicção, e Larissa sai da reunião sabendo que não conseguiu sustentar a escolha.** [Q16] **No teste seguinte, a configuração escolhida falha nos trechos de sombra do percurso; a decisão é revista depois do teste e a equipe precisa refazer a análise.** Larissa sente que depende dos colegas técnicos e que decide sem segurança.

#### Resumo do refinamento

| Questão | Resultado | O que mudou no cenário |
|---|---|---|
| Q10 | Parcial | Explicita o motivo de decidir antes do teste e o que se espera (escolha defensável); a relação entre a escolha e os testes já estava no cenário inicial. |
| Q11 | Novo | Os resultados chegam na véspera da reunião, sem tempo para tirar dúvidas; no episódio, são duas configurações com IoU de 0,78 e 0,76 no conjunto de teste. |
| Q12 | Novo | Divisão de papéis: Larissa reúne e recomenda; a palavra final é discutida com a coordenação. |
| Q13 | Novo | Ela ignora o tempo de inferência e os números por classe por não saber como pesam na decisão. |
| Q14 | Especificado | A comparação manual já existia; passa a ser concreta: planilhas lado a lado, busca do maior valor e uma diferença de 0,02 que ela não sabe julgar. |
| Q15 | Novo | Termos específicos que geram dúvida e a dependência de um colega para explicá-los. |
| Q16 | Novo | Desfecho do episódio: a configuração falha nos trechos de sombra e a decisão é revista depois do teste. |
| Q17 | Novo | O material levado (print das planilhas com o maior valor destacado), a pergunta da coordenação que ela não soube responder e o momento em que percebe que não sustentou a escolha. |
| — | Reescrito | O cenário refinado passa a narrar uma ocorrência concreta (uma reunião e seu desfecho), em vez de uma rotina com resultados alternativos. |


### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ambiente/contexto | Semana anterior a um ciclo de testes; os resultados chegam na véspera; reunião semanal com a coordenação (Q11). |
| Atores | Larissa (reúne e recomenda), o integrante técnico que executa os modelos (P01) e a coordenação (P02), que discute e decide com ela (Q12). |
| Objetivos | Chegar à reunião com uma escolha de configuração defensável para o próximo ciclo (Q10). |
| Planejamento | Estratégia de comparação: procurar o maior valor de cada métrica nas planilhas lado a lado (Q14). |
| Ações | Receber os resultados; abrir as planilhas; destacar o maior valor; pedir explicação dos termos; levar o print à reunião; justificar a escolha (Q17). |
| Eventos | Os resultados chegam na véspera; na reunião, a coordenação pergunta se a diferença importa; no teste seguinte, a configuração falha nas sombras (Q11, Q16, Q17). |
| Avaliação | Não sabe julgar se 0,02 é relevante; ignora métricas que não entende; percebe, na reunião, que não sustentou a escolha (Q13, Q14, Q15, Q17). |
| Recursos/informações | Métricas do conjunto de teste anotado (IoU, acurácia, valores por classe, tempo de inferência), planilhas, mensagens com resultados de execuções e conhecimento dos colegas técnicos. |
| Problemas/rupturas | Resultados dispersos e sem referência; termos que ela não entende; dúvida se a diferença entre modelos é relevante; dependência de colegas técnicos; dificuldade de justificar a escolha. |
| Consequências | Decisão frágil, revista depois do teste; retrabalho da equipe; insegurança de Larissa. |

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
**Necessidade relacionada:** R03 — comparar desempenho entre modelos (P02: experimentar) e R04 — treinar com uma configuração definida pelo usuário  
**Situação concreta da Entrega 1 relacionada:** **Nova situação justificada** — perfil "Pesquisador(a) de modelos" (01 §2.2 `[H]`) e atividade A05 (definir uma configuração e treinar, 01 §3.2); a E1 não registra situação observada da P02.  
**Hipóteses ainda presentes:** H01, H04, H08

> **Justificativa da nova situação:** a E1 atribui ao pesquisador de modelos a definição de configurações e o treino (§7.1, A05), mas não descreve uma situação concreta desse perfil. As configurações que ele treina são as que a P01 usa e a P03 compara; por isso o cenário é relevante. A situação é **hipotética** (P02 é proto-persona) e precisa ser validada na Entrega 7.
>
> **Diferença em relação ao C01:** Rafael decide se a configuração em uso pode continuar no próximo teste; Andreia decide o que mudar no próximo treino e se uma nova configuração vale ser levada à reunião de decisão.

### 1. Cenário inicial

Andreia é professora e coordenadora da equipe Baja FEI, onde acompanha pesquisas e desenvolvimentos voltados à construção de um veículo Baja autônomo. Com formação avançada em Engenharia Mecânica e experiência em Visão Computacional, ela utiliza seus conhecimentos para desenvolver e avaliar modelos de inteligência artificial capazes de interpretar o ambiente off-road.

Durante suas pesquisas, Andreia precisa analisar imagens e vídeos gravados durante os testes do veículo, verificando se diferentes modelos de segmentação conseguem delimitar corretamente a região de trilha. Para isso, utiliza modelos pré-treinados e scripts em Python, executando os modelos e visualizando as máscaras geradas para avaliar seus resultados.

Entretanto, quando deseja experimentar diferentes modelos, precisa realizar configurações e execuções separadamente, utilizando ferramentas e códigos que nem sempre oferecem uma forma prática de visualizar e comparar os resultados. Para analisar uma mesma imagem com modelos diferentes, precisa executar cada um individualmente e alternar entre as saídas geradas, dificultando a identificação de diferenças na segmentação.

Sua rotina como professora e coordenadora também limita o tempo disponível para desenvolver e treinar novos modelos do zero. Assim, ela gostaria de aproveitar modelos pré-treinados e concentrar seus esforços na experimentação, análise e identificação de oportunidades de melhoria.

Em uma de suas análises, Andreia precisa verificar qual modelo apresenta melhores resultados para determinada entrada. Para isso, executa os modelos separadamente, observa as máscaras geradas e consulta métricas para avaliar o desempenho de cada um. Entretanto, como as imagens originais, as máscaras, as sobreposições e as métricas ficam em saídas separadas, a comparação dos resultados fica difícil.

Esse processo fragmentado consome parte do tempo que Andreia poderia dedicar à pesquisa e ao desenvolvimento do veículo autônomo.

### 2. Questões de refinamento

| # | Elemento | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|---|
| Q18 | Planejamento | Quais características Andreia considera mais importantes ao escolher um modelo de segmentação para determinado experimento? | Para identificar os critérios utilizados na seleção dos modelos. | Entrevista com pesquisador(a) ou coordenador(a) da equipe (perfil P02). |
| Q19 | Ações | Como Andreia realiza atualmente a comparação entre diferentes modelos e quais dificuldades encontra nesse processo? | Para compreender o fluxo atual de experimentação e comparação. | Entrevista e observação das execuções. |
| Q20 | Avaliação | Quais métricas Andreia utiliza para avaliar a qualidade da segmentação e como interpreta seus resultados? | Para identificar quais informações técnicas precisam ser apresentadas pela ferramenta. | Entrevista e análise das métricas utilizadas. |
| Q21 | Ambiente/contexto (entradas) | Quais formatos, resoluções e características os vídeos e imagens utilizados nos experimentos apresentam? | Para identificar requisitos e possíveis limitações do processamento das entradas. | Entrevista e análise dos arquivos utilizados. |
| Q22 | Avaliação e ações | Como Andreia identifica que um modelo apresenta resultados insatisfatórios e quais ações realiza após identificar esses problemas? | Para compreender como os resultados orientam as melhorias nos modelos. | Entrevista e observação. |
| Q23 | Ações | Como Andreia organiza e registra os resultados dos experimentos para consultá-los posteriormente? | Para entender se existe uma necessidade real de histórico e registro de observações. | Entrevista e análise dos registros de pesquisa. |
| Q24 | Avaliação | Quais informações Andreia precisa visualizar simultaneamente para analisar uma segmentação de maneira eficiente? | Para identificar as necessidades de visualização e apresentação dos resultados. | Entrevista e observação. |
| Q25 | Atores | Quem participa das decisões ligadas à pesquisa e quem usa as conclusões de Andreia? | Para mapear atores e dependências, separados do objetivo do experimento (Q28). | Entrevista com pesquisador(a) ou coordenador(a) da equipe (perfil P02) e com a equipe Baja FEI. |
| Q26 | Ações e eventos | Quais etapas e configurações são necessárias para executar os modelos sobre imagens e vídeos, e quais dificuldades técnicas podem ocorrer durante o processamento? | Para identificar pré-condições, dependências e possíveis falhas durante a execução. | Entrevista, observação e análise dos scripts. |
| Q27 | Ambiente/contexto | Onde, quando e com quanto tempo Andreia realiza um experimento? | Para detalhar o ambiente e a restrição de tempo da atividade. | Entrevista com pesquisador(a) ou coordenador(a) da equipe (perfil P02) + observação. |
| Q28 | Objetivos | O que Andreia quer concluir com um experimento específico e como isso se liga à decisão sobre a configuração dos testes? | Para separar o objetivo do experimento do objetivo maior da pesquisa (o veículo autônomo). | Entrevista com pesquisador(a) ou coordenador(a) da equipe (perfil P02). |

### 3. Cenário refinado

> P02 é proto-persona: as respostas abaixo são **hipóteses de trabalho**, não relatos. Precisam ser validadas na Entrega 7.
>
> Marcação conforme a [convenção de refinamento](#convenção-de-marcação-do-refinamento): texto normal = mantido; **negrito** = novo; *itálico* = reescrito/especificado.

Andreia é professora em tempo integral e coordenadora da equipe Baja FEI, onde acompanha pesquisas voltadas ao desenvolvimento de um veículo autônomo para terrenos off-road. Com formação avançada em Engenharia Mecânica e especialização em Visão Computacional, possui conhecimentos para desenvolver modelos próprios e implementar scripts em Python. *O veículo autônomo é o objetivo maior da pesquisa; neste cenário, ela trabalha com os modelos do TCC (FCN e DeepLabV3+), ajustando a configuração de treino e comparando resultados.* [Q27] **Faz os experimentos na sala dos professores ou no laboratório, entre aulas, em janelas curtas: inicia um treino e volta horas depois para ver se terminou.**

**O episódio a seguir é uma situação construída pela equipe `[H]`.** [Q28] **Depois do teste em que a configuração em uso falhou nos trechos de sombra (C02), Andreia quer saber se mais épocas de treino e a inclusão do dataset Synthetic Offroad melhoram a trilha em sombra, para decidir se vale levar a nova configuração à reunião de coordenação.** [Q18] **Ao escolher o que testar, prioriza a qualidade da borda da trilha em sombra e vegetação densa e, em segundo lugar, o tempo de inferência, pensando no uso futuro no veículo.** [Q21] **As entradas são vídeos das câmeras do veículo, com resoluções diferentes conforme a câmera; ela extrai cerca de 40 quadros dos trechos de sombra.**

[Q26] Para experimentar uma configuração diferente, precisa configurá-la e executá-la separadamente, por meio de scripts em Python. **Ajusta a configuração de treino (50 épocas em vez de 30, com Freiburg Forest e Synthetic Offroad), inicia o treino e vai dar aula. Ao voltar, o treino parou no meio por falta de memória; ela reduz o batch size e reinicia, perdendo a tarde.** [Q19] **Quando o treino termina, executa as duas configurações sobre os mesmos quadros e, para comparar, abre as saídas de cada uma em janelas lado a lado e anota as diferenças à mão.** [Q24] *Alternar entre a imagem original, a máscara, a sobreposição e as métricas, em janelas diferentes, faz com que ela perca diferenças pequenas na borda da trilha*; **para julgar um quadro, precisa ver essas quatro informações ao mesmo tempo.**

[Q20] Depois das execuções, consulta as métricas: **o IoU da classe trilha e a acurácia, calculados no conjunto de teste anotado, sobem só 0,01; quando o IoU cai em algum caso, ela olha a matriz de confusão para entender onde o modelo erra. Nos quadros de campo, que não têm anotação de referência, a avaliação é visual.** [Q22] **Considera um resultado insatisfatório quando a máscara perde a trilha em sombras ou em trechos estreitos. Nos quadros, a nova configuração melhora nas sombras largas, mas ainda perde a trilha nos trechos estreitos; ela conclui que o resultado é inconclusivo e anota que o próximo experimento deve testar outro conjunto de dados.** [Q23] **Registra o experimento no caderno de pesquisa, com data, configuração e observações; as saídas ficam em pastas separadas, e para comparar com o experimento anterior ela precisa procurar a pasta pela data.** [Q25] **Leva a conclusão à reunião de coordenação, onde Larissa (P03) prepara a decisão sobre qual configuração usar nos testes; Rafael (P01), que usa as configurações treinadas, é informado do resultado.** **Considera o experimento concluído quando consegue dizer se a nova configuração deve ou não ir para a reunião; desta vez, só consegue levar um "talvez".**

Esse processo fragmentado consome parte do tempo que Andreia tem para a pesquisa: a falha no treino custou uma tarde, e a comparação manual não lhe deu uma conclusão clara.

**Resumo do refinamento**

| Questão | Resultado | O que mudou no cenário |
|---|---|---|
| Q18 | Novo | Critério de escolha: qualidade da borda em sombra e vegetação densa, depois tempo de inferência. |
| Q19 | Novo | Como compara: mesmos quadros, saídas em janelas lado a lado e anotações à mão. |
| Q20 | Novo | Métricas usadas (IoU da classe trilha e acurácia, no conjunto de teste anotado), ganho de só 0,01 e uso da matriz de confusão; quadros de campo avaliados visualmente. |
| Q21 | Novo | Entradas: vídeos das câmeras do veículo com resoluções diferentes. |
| Q22 | Novo | Critério de resultado insatisfatório e o desfecho do episódio: inconclusivo, com novo experimento planejado. |
| Q23 | Novo | Registro no caderno e pastas por data; recuperar o experimento anterior exige procurar pela data (relevante para a H08). |
| Q24 | Reescrito e novo | A "falta de visualização conjunta" vira a dificuldade concreta (perder diferenças pequenas ao alternar janelas); novo: as quatro informações de que precisa para julgar um quadro. |
| Q25 | Novo | Atores: a conclusão vai à reunião de coordenação, onde Larissa prepara a decisão; Rafael é informado. |
| Q26 | Novo | Etapas e configuração do experimento (épocas, datasets, batch size) e o evento: o treino para por falta de memória e ela perde a tarde. |
| Q27 | Novo | Contexto: sala dos professores ou laboratório, entre aulas, em janelas curtas. |
| Q28 | Novo | Objetivo do experimento (melhorar a trilha em sombra e decidir se leva a configuração à reunião), separado do objetivo maior da pesquisa. |
| — | Removido | Os trechos sobre falta de experiência com interfaces e sobre uma "ferramenta centralizada" saíram do cenário inicial e do refinado: antecipavam a solução. |

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| **Ambiente/contexto** | Sala dos professores ou laboratório, entre aulas, em janelas curtas; as entradas são vídeos das câmeras com resoluções diferentes (Q21, Q27). |
| **Atores** | Andreia (treina e compara), Larissa (prepara a decisão), a coordenação (decide com a gestão) e Rafael (usa as configurações e é informado) (Q25). |
| **Objetivos** | Saber se mais épocas e o Synthetic Offroad melhoram a trilha em sombra e decidir se leva a nova configuração à reunião; o veículo autônomo é o objetivo maior, fora do recorte (Q28). |
| **Planejamento** | Escolhe o que testar pela borda em sombra e, depois, pelo tempo de inferência; seleciona quadros dos trechos de sombra (Q18, Q21). |
| **Ações** | Ajusta a configuração; treina; executa as duas configurações; abre as saídas em janelas lado a lado; anota as diferenças; registra no caderno; leva a conclusão à reunião (Q19, Q23, Q26). |
| **Eventos** | O treino para no meio por falta de memória; o ganho no conjunto de teste é de só 0,01 (Q20, Q26). |
| **Avaliação** | Considera insatisfatório perder a trilha em sombras ou trechos estreitos; julga o resultado inconclusivo; considera o experimento concluído quando sabe se leva a configuração à reunião, e desta vez só leva um "talvez" (Q20, Q22, Q24). |
| **Recursos/informações** | Vídeos e quadros extraídos, modelos do TCC, scripts em Python, máscaras, métricas do conjunto de teste anotado, matriz de confusão e caderno de pesquisa. |
| **Problemas/rupturas** | Treino que falha no meio; comparação em janelas separadas, que esconde diferenças pequenas; métricas do conjunto de teste que não mostram o problema nos quadros de campo; experimentos anteriores difíceis de recuperar. |
| **Consequências** | Perde uma tarde; chega à reunião sem conclusão clara; sobra menos tempo para a pesquisa. |

### 5. Implicações para as próximas entregas

**Tarefas que merecem análise**

| ID | Tarefa | Origem no cenário | Por que merece análise | Prioridade |
|---|---|---|---|---|
| T02 | Executar a segmentação com uma ou mais configurações disponíveis *(tarefa compartilhada com o C01; antes T07 neste cenário)* | C03; P02; Q18, Q21, Q26 | É a atividade central da experimentação. Andreia precisa executar diferentes modelos sobre entradas para avaliar seus resultados. | Alta |
| T06 | Analisar visualmente os resultados da segmentação *(antes T08)* | C03; P02; Q22, Q24 | Permite identificar erros e verificar se o modelo está identificando corretamente as regiões de interesse. A visualização da imagem original, máscara e sobreposição pode facilitar essa atividade. | Alta |
| T07 | Comparar os resultados de diferentes modelos de segmentação *(antes T09)* | C03; P02; Q18, Q19, Q20 | É fundamental para identificar quais modelos apresentam melhor desempenho e podem contribuir para o desenvolvimento do veículo autônomo. | Alta |
| T08 | Definir uma configuração de treino e treinar o modelo *(criada em 08/11/2026; não confundir com o antigo T08 deste cenário, hoje T06)* | C03; P02; Q18, Q26, Q28 | Andreia quer experimentar modelos sem gastar tempo desenvolvendo e treinando do zero; definir a configuração (modelo, épocas, early stopping, datasets, batch size) e treinar pela interface é o que permite comparar alternativas depois. | Média |

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
| Quem participa das decisões ligadas à pesquisa e quem usa as conclusões | Q25 | Mapeia os atores que dependem dos resultados. | Entrevista com pesquisador(a) ou coordenador(a) da equipe (perfil P02) e com a equipe. |
| Recursos computacionais e dependências necessárias para executar os modelos | Q26 | Identifica possíveis limitações técnicas durante o processamento. | Análise dos scripts e ambiente de execução. |
| Onde, quando e com quanto tempo os experimentos acontecem | Q27 | Define o contexto e a restrição de tempo da atividade. | Entrevista + observação. |
| O que cada experimento pretende concluir e como se liga à decisão dos testes | Q28 | Separa o objetivo do experimento do objetivo maior da pesquisa. | Entrevista com pesquisador(a) ou coordenador(a) da equipe (perfil P02). |

## Checklist

- [X] Há um cenário completo por integrante.
- [X] Cada cenário tem título, ator, objetivo, contexto e problema.
- [X] O cenário possui origem rastreável na Entrega 1 ou justifica claramente a inclusão de uma nova situação.
- [X] O texto descreve a situação atual, sem antecipar a solução.
- [ ] Para TCC sem interface original, o cenário descreve uma prática humana plausível relacionada à contribuição técnica, e não “a falta de uma tela”. *(Não se aplica: o TCC prevê interface.)*
- [X] Questões de refinamento acrescentam informação nova.
- [X] O refinamento mostra claramente o que foi adicionado/alterado.
- [X] Cada cenário tem pelo menos uma questão válida para cada um dos sete elementos (ambiente/contexto, atores, objetivos, planejamento, ações, eventos e avaliação).
- [X] Cada cenário refinado narra uma ocorrência concreta e o momento em que o usuário conclui, ou percebe que não concluiu, a atividade.
- [X] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [X] Cada cenário está ligado a persona/necessidade na matriz de rastreabilidade.

## Histórico de revisões

| Data | O que mudou | Motivo |
|---|---|---|
| 30/10/2026 | T03 e T04 renomeadas para deixarem de ter o mesmo nome; convenção de marcação do refinamento; nomes completos na autoria; fonte "Entrevista com Larissa" substituída por perfil (C02) | Revisão de consistência (`PENDENCIAS.md`: INC-02, INC-04, INC-47, INC-48) |
| 08/11/2026 | IDs das tarefas do C03 alinhados aos da Entrega 5 (T07 → T02 compartilhada, T08 → T06, T09 → T07) e origem corrigida para C03; marcações do refinamento do C03 trocadas pelas questões do próprio cenário (Q19–Q26). T02 renomeada para "Executar a segmentação com uma ou mais configurações disponíveis". Classes alinhadas ao TCC (região de trilha). "Coordenação" do C02 ligada à P02. Métricas do C01 restritas a imagens com anotação de referência | Revisão de consistência (`PENDENCIAS.md`: INC-05, INC-12, INC-49, INC-52, INC-56, INC-58) e leitura do repositório do TCC |
| 09/11/2026 | Criada a T08 no C03 (definir uma configuração de treino e treinar o modelo), depois que configurar e treinar entrou no recorte | Revisão de consistência (`PENDENCIAS.md`: INC-61) |
| 10/11/2026 | Cabeçalho do C01 preenchido; Q2 e Q4 do C01 reformuladas; refinamentos do C01 e do C03 reescritos com respostas hipotéticas marcadas e resumo do que mudou; Q11, Q13 e Q16 do C02 reformuladas e respondidas; fontes deixam de citar personas como entrevistados; checklist revisto | Revisão de consistência (`PENDENCIAS.md`: INC-04, INC-44, INC-45, INC-46, INC-50, INC-51, INC-62). Rascunhos do C01 e do C03 a revisar pelo Tiago e pelo Mateus |
| 11/11/2026 | Coluna "Elemento" nas questões e "Elementos extraídos" pelos sete elementos nos três cenários. C01: Q4 e Q6 separadas (quem decide × quem participa), critério da Q5, momento de conclusão na Q7 e "mesmo não sendo desenvolvedor" compatibilizado com a P01. C02: refinado narra um episódio concreto (duas configurações com IoU de 0,78 e 0,76, reunião e desfecho), com Q10 e Q14 reclassificadas como parcial/especificado e Q17 detalhada. C03: cabeçalho como nova situação justificada (R03 e R04), Q25 restrita a atores e novas Q27 (contexto) e Q28 (objetivo); refinado narra um experimento concreto (treino que falha, comparação inconclusiva); trechos que antecipavam a solução retirados também do cenário inicial. Métricas restritas ao conjunto de teste anotado no C02 e no C03 | Feedback do professor sobre a Entrega 4 |
