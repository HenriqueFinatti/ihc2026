# Entrega 4 — Cenários de análise/problema

**Data:** {{dd/mm/aaaa}}  
**Status:** ⬜ não iniciada  
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

<!-- > Repita para C02, C03... com autoria individual. -->

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
