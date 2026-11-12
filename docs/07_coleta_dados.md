# Entrega 7 — Coleta de dados, necessidades e aspectos éticos

**Data:** 11/11/2026 (início)  
**Status:** 🟩 concluída

## Objetivo da atividade

Planejar dados necessários para compreender usuários e requisitos de IHC, escolher técnicas adequadas e documentar instrumentos de modo que a aplicação possa ser reproduzida por pessoas diferentes.

## Para escopos de IHC derivados de TCC técnico

Quando o usuário e a interface foram propostos pela disciplina, uma prioridade da coleta é investigar se esse **cenário de uso realmente faz sentido**. Não trate o exercício de comercialização da Entrega 1 como validação de mercado.

Perguntas úteis incluem:

- esse perfil realmente realiza a atividade imaginada?
- quais ferramentas usa hoje?
- quais informações consulta?
- quais decisões toma?
- que vocabulário utiliza?
- quais parâmetros compreende e quais deveriam ser abstraídos?
- precisa de dashboard, histórico, filtros, relatórios ou comparação? Por quê?
- quais erros são frequentes e quais são críticos?
- existem papéis/permissões diferentes?
- que resultados do algoritmo/modelo seriam úteis ou difíceis de interpretar?

Quando o acesso ao perfil profissional for difícil, discuta com o docente alternativas metodológicas (especialistas próximos, dados secundários, literatura, participantes proxy) e registre as limitações. **Não esconda a limitação da amostra.**

## Hipóteses e lacunas prioritárias herdadas da Entrega 1

Antes de decidir “que dados coletar”, retome os itens `[H]` e `[?]` da Entrega 1 e o registro de hipóteses em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md). A coleta deve responder perguntas reais do projeto, e não apenas produzir um formulário porque a técnica foi solicitada.

> Linhas preenchidas por parte: Henrique (P03/C02), Tiago (P01/C01) e Mateus (P02/C03).

| ID | Hipótese/lacuna | Evidência atual | Decisão que depende da resposta | Prioridade |
|---|---|---|---|---|
| H07 | Existem fatores sociais ou organizacionais como papéis, permissões e colaboração na equipe. **Para a P03:** quem escolhe as configurações candidatas, quem recomenda e quem decide. | Nenhuma. O C02 descreve, como hipótese, que a gestora reúne e recomenda e que a palavra final é discutida com a coordenação. | Se a T05 (decidir e justificar) acontece na interface ou fora dela; se a P03 continua como persona própria ou se funde a outro papel; se é preciso registrar quem fez a recomendação. | alta |
| H01 | A decisão sobre qual modelo usar é tomada com base em números dispersos e sem critério explícito. | Só o cenário C02, construído pela equipe. Nenhum relato de quem decide. | Se o painel consolidado (decisão 1 da P03) e a referência de comparação (decisão 2) são necessários, ou se a equipe já tem um critério que só precisa ser apresentado. | alta |
| H04 | Conhecimento técnico, experiência com ferramentas e familiaridade com métricas influenciam a interação. **Para a P03:** quais métricas e termos quem decide entende. | As personas variam nesse eixo, mas são construção da equipe. A RC01 (termos) tem sustentação média. | Se a explicação dos termos no ponto de uso (decisão 3 da P03) vira requisito, e com qual vocabulário. | alta |
| H06 | Dificuldades principais: configurar parâmetros, selecionar arquivos, interpretar resultados sem orientação. **Para a P03:** julgar se uma diferença entre configurações é relevante. | Dores escritas pela equipe nas personas e no C02; nenhuma relatada por usuários. | De onde vem o valor de referência (decisão 2 da P03) e qual é o critério de resultado "inconclusivo" (decisão 5). | média |
| H12 | Benefício esperado: eliminar necessidade de código, apresentar resultados claramente, permitir comparação entre modelos. **Para a P03:** chegar à reunião com uma escolha que consiga sustentar. | Expectativa registrada na E1 §9.1, sem evidência. | O que conta como sucesso nas metas de usabilidade (Entrega 8) para a tarefa de decisão; se o resumo exportável (decisão 4 da P03) é o que de fato se leva à reunião. | média |
| H02 | O perfil prioritário (analista de segmentação) possui conhecimento básico do domínio mas pode não dominar programação. **Para a P01:** separar o que a pessoa sabe de programação do que sabe para interpretar a segmentação. | Só a P01, que refina a hipótese (programa no curso, mas não conhece os scripts do projeto); nenhum relato de analista. | Quanto da execução precisa ser escondido e se a interface precisa explicar a análise, o código ou os dois. | alta |
| H05 | As atividades são realizadas atualmente por meio de scripts que exigem conhecimento técnico. **Para a P01:** quais passos e erros da execução atrapalham a análise. | Observação interna da equipe (E1 §4.6), sustentada com evidência limitada; não mostra a dificuldade de quem analisa. | Fluxo sem código, estados de execução (RC04) e mensagens de erro (decisões 4 e 5 da P01). | alta |
| H09 | Interfaces conhecidas pelo público: VS Code, terminais, GitHub, ferramentas de telemetria. | Nenhuma sobre o público; a E2 descreve produtos, não o que a equipe usa. | Quais padrões e termos podem ser reaproveitados sem explicação. | média |
| H10 | Ferramentas genéricas como CVAT e Roboflow podem ser complexas para o perfil priorizado. | Refinada pela E2 com fontes públicas: a complexidade varia por produto. Não se sabe se a equipe conhece essas ferramentas. | Se a interface precisa se diferenciar dessas ferramentas ou se a comparação com elas é irrelevante para o público. | baixa |
| H11 | Padrões familiares: seleção de arquivo, botão de processamento, barra de progresso, comparação lado a lado. | Padrões observados nos produtos da E2; familiaridade do público não comprovada. | Estrutura das telas de execução e comparação (decisões 1 e 4 da P01). | média |
| H08 | Existe necessidade de histórico para comparar análises e acompanhar evolução. **Para a P02:** recuperar configurações e resultados de experimentos anteriores. | Nenhuma sobre o público. O versionamento de datasets do Roboflow (E2) mostra que o padrão existe, não que a equipe precisa dele; o C03 (Q23) descreve, como hipótese, um caderno de pesquisa. | Incluir ou não o histórico (decisão 5 da P02, decisão 4 da P01) e o que ele precisaria guardar. Hoje está fora do recorte até esta entrega responder. | alta |

## Parte A — necessidades e requisitos de IHC

> **Responsabilidade:** solução individual por integrante.

### A01 — Henrique Finatti Silveira Belo Trebbi

**Autor(a):** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3  
**Persona e cenário:** P03 — Larissa Camargo; C02 (tarefas T04 e T05)  
**Objetivo desta parte:** verificar se o perfil da P03 existe na equipe Baja FEI como foi descrito, como a escolha da configuração usada nos testes acontece hoje e o que impede uma decisão defensável. As respostas decidem se T04, T05 e as decisões de design 1 a 5 da P03 viram requisitos ou são revistas.

> As afirmações sobre a organização da equipe Baja FEI nesta seção (papéis, reuniões, quantidade de pessoas) são hipóteses `[H]` levantadas para planejar a coleta e serão conferidas com a equipe antes da aplicação.

#### Que dados coletar?

Os dados seguem os cinco grupos de Barbosa e Silva (2010): o próprio usuário, a relação com a tecnologia, o conhecimento do domínio, as tarefas e as motivações e valores. Só entram dados que respondem a uma dúvida do projeto.

| Dado/informação | Hipótese/lacuna relacionada | Por que é necessário | Qual decisão de design pode afetar |
|---|---|---|---|
| **Usuário.** Papel na equipe Baja FEI, há quanto tempo exerce esse papel e se participa das reuniões em que se escolhe a configuração | H07 | Saber se existe alguém que prepara a decisão sem executar os modelos (o perfil da P03) ou se esse papel é exercido por quem executa | Manter a P03 como persona primária, fundi-la a outro perfil ou rebaixá-la |
| **Relação com tecnologia.** Ferramentas usadas hoje para receber e comparar resultados (planilhas, mensagens, slides) e se a pessoa executa scripts ou depende de alguém | H05, H09 | Conhecer os padrões que a pessoa já domina e o grau de dependência de colegas técnicos | Forma de apresentar a comparação (tabela, gráfico, resumo); se a P03 precisa executar algo na interface |
| **Relação com tecnologia.** Onde e em que equipamento a decisão é preparada e discutida (notebook próprio, tela projetada na reunião, conexão disponível) | Ambiente da P03 `[?]` (E3) | O contexto de uso da P03 é hipótese; a reunião com tela compartilhada nunca foi confirmada | Layout legível em projeção; necessidade de funcionar sem internet |
| **Domínio.** Quais métricas a pessoa reconhece (IoU, acurácia, tempo de inferência, valores por classe), como explica cada uma com as próprias palavras e quais ignora | H04, RC01 | O cenário C02 supõe que ela ignora o que não entende; é preciso saber o que de fato é lido | Quais métricas aparecem primeiro; se a explicação no ponto de uso (decisão 3 da P03) vira requisito |
| **Domínio.** Termos que geram dúvida ("configuração", "época", "classe", "trilha", "conjunto de teste") e as palavras que a equipe usa no lugar deles | H04, RC01 | O vocabulário das telas deve ser o da equipe, e não o do código | Rótulos, legenda e textos de ajuda |
| **Domínio.** Como a pessoa julga se uma diferença entre duas configurações é relevante e se usa alguma referência (resultado anterior, meta da equipe, faixa esperada) | H06; decisão 2 da P03 | Sem saber de onde viria a referência, a "métrica com referência" pode ser inventada pela interface | Origem e forma do valor de referência; critério de resultado "inconclusivo" (decisão 5) |
| **Tarefas.** Como a escolha da configuração acontece hoje: quem propõe as configurações candidatas, quem recomenda, quem decide e em qual momento | H07, H01 | O professor pediu que se investigue quem escolhe, quem recomenda e quem decide | Se a T05 acontece na interface ou fora dela; se a recomendação precisa registrar autoria |
| **Tarefas.** Como os resultados chegam a quem decide: formato, quem envia, com que antecedência e com quais números | H01 (C02, Q11 e Q13) | Confirmar se os números chegam dispersos e sem critério, que é a hipótese central da P03 | Painel consolidado (decisão 1 da P03) |
| **Tarefas.** Se a pessoa prefere comparar as configurações ela mesma, na interface, ou receber um material já preparado por quem executou | Feedback da E3 sobre o acesso direto da P03 | A P03 foi definida como usuária direta da interface; isso nunca foi verificado | P03 como usuária direta (T04) ou como destinatária de um relatório (decisão 4) |
| **Tarefas.** Com que frequência a decisão acontece (a cada ciclo de testes, antes de competições) e quanto tempo há para prepará-la | H12 | Uma decisão rara e com pouco tempo de preparo pede outra interface do que uma decisão semanal | Profundidade das explicações; prioridade da T04 e da T05 no protótipo |
| **Tarefas.** O que a pessoa leva para a reunião, quais perguntas costuma ouvir e se já precisou rever uma decisão depois de um teste (o que motivou e qual foi a consequência) | H12 (C02, Q16 e Q17); gravidade dos erros | Dimensionar a consequência de uma decisão mal sustentada e o que precisa ser justificado | Conteúdo do resumo exportável (decisão 4); avisos de limitação (decisão 5); metas da Entrega 8 |
| **Tarefas.** Se, ao decidir, a pessoa consulta decisões ou resultados de ciclos anteriores e como os encontra | H08 | O histórico está fora do recorte até a Entrega 7 responder se ele é necessário | Incluir ou não o histórico e o que ele precisaria recuperar |
| **Motivações e valores.** O que a pessoa considera uma boa decisão, o que mais teme ao decidir e se prefere que o sistema sugira uma opção ou apenas organize os dados | H12; RQ08 (E5) | O projeto definiu que a interface organiza as evidências e não recomenda; isso precisa ser aceitável para quem decide | Manter a decisão humana (sem "modelo recomendado" pelo sistema) ou rever o RQ08 |

**Dados que não serão coletados:** idade exata, notas, dados de contato além do necessário para agendar, opiniões sobre colegas identificados pelo nome e qualquer dado pessoal sensível. Resultados de modelos, planilhas e mensagens só serão vistos se o participante quiser mostrá-los e sem copiar dados de outras pessoas.

#### De quem coletar?

Respostas às perguntas da aula para o recorte da P03 `[H]`:

- **Quem utilizará o sistema?** Para esta parte, quem prepara a decisão sobre a configuração usada nos testes.
- **Quem será afetado por ele?** A equipe que usa a configuração nos testes (pilotos e mecânicos, H03) e quem executa os modelos, que passa a enviar os resultados de outro jeito.
- **Quem decide quais objetivos o sistema deve apoiar?** Os autores do TCC e o orientador, que definem as funcionalidades da interface prevista.
- **Quem definiu o processo atual?** A liderança da equipe e a coordenação, que organizam as reuniões e o ciclo de testes.

| Perfil/stakeholder | Critério de inclusão | Relação com persona/público |
|---|---|---|
| Integrantes da equipe Baja FEI que preparam ou tomam a decisão sobre qual configuração usar nos testes (por exemplo, capitão, gerente de projeto ou líder da área de eletrônica e autonomia `[H]`) | Participou de pelo menos uma escolha de configuração de modelo, ou de outra decisão técnica com base em resultados que não produziu, no último semestre; ter 18 anos ou mais; não ser autor deste projeto | **Perfil principal.** Corresponde à P03 (gestora). Previsão de 2 a 4 pessoas `[H]`, conforme o número de pessoas que de fato exercem o papel |
| Integrantes que executam os modelos e entregam os números para a reunião | Executou a segmentação ou preparou resultados para uma reunião de decisão no último semestre | **Informante secundário.** Corresponde à P01. Confirma como os resultados chegam a quem decide (C02, Q11 e Q13). Uma pessoa basta |
| Coordenação da equipe (professor(a) responsável pela Baja FEI) | Participa das reuniões em que a configuração é escolhida | **Informante secundário, participação opcional.** Corresponde à "coordenação" do C02 (P02). Confirma quem tem a palavra final (H07) |

**Se faltar gente no perfil principal:** caso menos de duas pessoas exerçam o papel, a alternativa é ouvir ex-integrantes que já exerceram esse papel ou gestores de outras equipes de competição da FEI que decidem com base em resultados técnicos. Essas pessoas seriam participantes proxy: a limitação será registrada e nenhuma conclusão sobre a Baja FEI será tirada só delas.

#### Aspectos éticos

O estudo é uma atividade de ensino da disciplina, sem finalidade de pesquisa científica. Segundo a Resolução CNS 510/2016 (art. 1º, parágrafo único), esse tipo de atividade não é registrado no sistema CEP/Conep, mas isso não dispensa os princípios éticos. A aula cita a Resolução 196/96, que foi revogada pela 466/2012; para entrevistas e opiniões, a referência atual é a 510/2016. O tratamento de dados pessoais segue a LGPD (Lei 13.709/2018). Abaixo, o que isso significa para os dados e as pessoas deste projeto.

| Dado ou situação | Risco neste projeto | Cuidado adotado |
|---|---|---|
| Papel na equipe | A equipe é pequena e há poucas pessoas em cada papel; "a gestora" é identificável mesmo sem nome | Na divulgação, usar códigos (G1, G2…) e descrever o papel de forma genérica ("integrante que decide"); nunca combinar papel, semestre e área na mesma frase |
| Relação com a coordenação | As pessoas que participam da coleta são alunos, e a coordenação é um(a) professor(a); alunos são citados na aula como grupo vulnerável | Convite feito pela equipe do projeto, nunca pela coordenação; a coordenação não sabe quem aceitou nem vê respostas individuais; recusar não tem consequência na equipe |
| Opiniões sobre o processo e sobre colegas | Falar de resultados que chegam atrasados ou confusos pode expor quem executa os modelos | Perguntar sobre o processo, e não sobre pessoas; nomes citados são retirados na transcrição |
| Decisões que deram errado | Relatar uma decisão revista pode causar constrangimento | Pergunta opcional; a pessoa escolhe o nível de detalhe e pode pedir que um trecho seja excluído |
| Planilhas, mensagens e slides | Podem conter dados de outras pessoas e resultados ainda não divulgados pela equipe | Só olhar o que a pessoa quiser mostrar; não copiar nem fotografar; anotar apenas a estrutura (que colunas, que números) |
| Gravação | Voz identifica a pessoa | Gravar áudio só com autorização explícita no termo; sem autorização, registrar por anotações. Sem gravação de vídeo |

- **Voluntariedade:** participar é opcional, e a pessoa pode desistir a qualquer momento, inclusive depois da conversa, pedindo a exclusão das suas respostas.
- **Consentimento:** antes de começar, a pessoa lê e aceita o termo de consentimento, adaptado do modelo em [`../instrumentos/termo_consentimento_modelo.md`](../instrumentos/termo_consentimento_modelo.md). O termo explica o objetivo, a duração, o que será registrado e quem terá acesso. O texto final entra na Parte B, junto com o instrumento.
- **Minimização:** coletar só os dados da tabela "Que dados coletar"; o que ficar fora dela não é perguntado.
- **Anonimização:** as pessoas que participam desta coleta não são identificadas nos documentos. Na transcrição, cada uma recebe um código (G1, G2…), e a lista que liga código e nome fica separada das anotações e é apagada ao fim da análise. *(Isso se refere a quem participa da coleta de dados, não a usuários da interface, que não terá cadastro nem login.)*
- **Armazenamento:** gravações, anotações brutas e a tabela de códigos ficam em uma pasta privada, acessível só aos três autores, **fora do repositório**. No repositório entram apenas sínteses anonimizadas.
- **Descarte:** gravações apagadas logo após a transcrição; anotações brutas e tabela de códigos apagadas ao fim do semestre letivo, depois da Entrega 14.
- **Devolutiva:** a síntese anonimizada é compartilhada com quem participou, que pode apontar interpretações erradas antes do uso no projeto.

### A02 — Tiago Fagundes dos Santos

**Autor(a):** Tiago Fagundes dos Santos — 22.123.017-0  
**Persona e cenário:** P01 — Rafael Pereira; C01 (tarefas T01, T02 e T03)  
**Objetivo desta parte:** verificar se existe na equipe Baja FEI quem analise os resultados da segmentação como a P01 foi descrita, como essa análise é feita hoje (execução, inspeção da máscara e comparação entre configurações) e onde ela falha. As respostas decidem o que entra no fluxo principal da interface (T01–T03) e o estado das decisões de design 1 a 5 da P01.

> As afirmações sobre a organização da equipe Baja FEI nesta seção (papéis, quantidade de pessoas, rotina de testes) são hipóteses `[H]` levantadas para planejar a coleta e serão conferidas com a equipe antes da aplicação.

#### Que dados coletar?

Os dados seguem os cinco grupos de Barbosa e Silva (2010). Atendendo ao feedback da Entrega 1, o conhecimento de **programação** e o conhecimento para **interpretar a segmentação** são investigados separadamente.

| Dado/informação | Hipótese/lacuna relacionada | Por que é necessário | Qual decisão de design pode afetar |
|---|---|---|---|
| **Usuário.** Papel na equipe, há quanto tempo analisa resultados de segmentação ou de outros dados de teste e qual curso faz | H02 | Saber se o perfil da P01 existe e se a análise é feita por uma pessoa dedicada ou por quem estiver disponível | Manter a P01 como persona prioritária e o nível de conhecimento assumido nas telas |
| **Relação com tecnologia.** Se programa, em que linguagem, e se consegue rodar e corrigir os scripts do projeto sem ajuda | H02, H05 | A P01 "programa no curso, mas não conhece os scripts por dentro"; é preciso saber se a dificuldade está no código ou na análise | Quanto da execução precisa ser escondido; se mensagens de erro em linguagem de usuário (decisão 5) bastam |
| **Relação com tecnologia.** Como a segmentação é executada hoje: passos, pré-condições, erros mais comuns e como a pessoa os percebe e contorna | H05 (C01, Q2 e Q8) | O processo atual por scripts é a base do problema, mas só tem evidência interna | Fluxo sem código e estados de execução (decisão 4, RC04); mensagens de erro (decisão 5) |
| **Relação com tecnologia.** Ferramentas e interfaces que a pessoa já usa (editor de código, terminal, GitHub, planilhas, CVAT, Roboflow ou similares) e o que acha delas | H09, H10, H11 | Os padrões da E2 foram observados nos produtos, não no nosso público | Padrões de interface que podem ser reaproveitados (seleção de arquivo, barra de progresso, lado a lado) |
| **Relação com tecnologia.** Onde e em que equipamento a análise acontece (laboratório ou beira da pista, computador do laboratório ou notebook), se há internet e se a pessoa é interrompida | Ambiente da P01 `[?]` (E3, seção 3.1) | O professor pediu para esclarecer esse contexto; o uso à beira da pista não está definido | Modo offline e retomada após interrupção (decisão 5); tamanho e legibilidade das telas |
| **Domínio.** Como a pessoa decide se uma máscara está correta, que sinais usa e o que faz quando não tem certeza | H06 (C01, Q7) | O critério de correção é hipótese do C01 | Apoio à avaliação visual da T01; registro de imagem duvidosa (RQ05) |
| **Domínio.** Como a pessoa separa uma falha do modelo de uma falha da imagem (sombra, poeira, desfoque) | H06 (C01) | É a ruptura central do C01, sem evidência | Informação de confiança do resultado (RQ06) e campos para registrar o motivo da dúvida |
| **Domínio.** Quais métricas lê (IoU, acurácia, tempo de inferência), o que entende de cada uma e se sabe que IoU e acurácia dependem de anotação de referência | H04, H02 | A P01 "interpreta métricas", mas sem referência; é preciso saber o que de fato é lido | Painel de métricas (decisão 3) e o estado da tela quando a imagem não tem métricas |
| **Domínio.** Como lê a máscara e a legenda hoje (cores, o que é "trilha"), e que termos geram dúvida | H04, RC01 | A legenda fixa (decisão 2) parte de uma dificuldade ainda não demonstrada | Paleta, rótulos e textos de apoio |
| **Tarefas.** Com que frequência a análise acontece, quantas imagens ou vídeos por sessão e quanto tempo leva | C01, Q9 | O volume define se a tarefa é feita imagem a imagem ou em lote | Processamento de várias imagens de uma vez e prioridade da T01 e da T02 |
| **Tarefas.** Como a pessoa escolhe a outra configuração para comparar e como compara hoje (janelas lado a lado, planilhas) | C01, Q5; T03 | O C01 supõe que se compara com "a mais recente"; o critério real é desconhecido | Comparação de configurações sobre a mesma imagem (T03; tela de comparação da E6) |
| **Tarefas.** Como organiza os arquivos e as métricas e se precisa voltar a análises anteriores | H08 (C01, Q3) | O histórico está fora do recorte até a Entrega 7 responder se ele é necessário | Incluir ou não o histórico (decisão 4) e o que ele precisaria recuperar |
| **Tarefas.** Para quem e em que formato o resultado é entregue (grupo da equipe, reunião, relatório) e o que acontece quando a análise não fica pronta a tempo | C01, Q2 e Q4 | A evidência produzida aqui é a base das decisões da P02 e da P03 | Exportação de imagens e relatórios (decisão 4) |
| **Motivações e valores.** O que a pessoa considera uma análise bem feita, se prefere aprender uma ferramenta nova fazendo ou com explicação e se usa atalhos de teclado | Comportamentos da P01 `[H]` | Preferências escritas pela equipe, nunca verificadas | Atalhos e presets (decisão 5, em investigação); ajuda contextual |

**Dados que não serão coletados:** notas, desempenho acadêmico, opinião sobre a competência técnica de colegas, imagens dos testes em que apareçam pessoas e qualquer dado pessoal sensível. Arquivos, pastas e logs só serão vistos se a pessoa quiser mostrá-los, sem copiar o conteúdo.

#### De quem coletar?

Respostas às perguntas da aula para o recorte da P01 `[H]`:

- **Quem utilizará o sistema?** Quem analisa os resultados da segmentação depois dos testes e responde à equipe se a configuração pode continuar.
- **Quem será afetado por ele?** Quem decide a configuração (P03 e coordenação), que recebe a evidência; quem acompanha os testes e fornece as imagens; e quem pilota, que usa a configuração escolhida (H03).
- **Quem decide quais objetivos o sistema deve apoiar?** Os autores do TCC e o orientador.
- **Quem definiu o processo atual?** Quem escreveu e mantém os scripts de segmentação, junto com a liderança da equipe.

| Perfil/stakeholder | Critério de inclusão | Relação com persona/público |
|---|---|---|
| Integrantes da equipe Baja FEI que analisam resultados de segmentação depois dos testes `[H]` | Executou ou analisou resultados de segmentação, ou analisou outros dados de teste do veículo (imagens, telemetria), no último semestre; ter 18 anos ou mais; não ser autor deste projeto | **Perfil principal.** Corresponde à P01 (analista de segmentação). Previsão de 3 a 6 pessoas `[H]` |
| Integrantes que acompanham os testes de campo e descarregam as imagens das câmeras | Participou de pelo menos um teste de campo no último semestre | **Informante secundário.** Confirma de onde vêm as imagens, em que condições são capturadas e quando chegam a quem analisa (C01, Q6). Uma pessoa basta |
| Integrante que escreveu ou mantém os scripts de segmentação | É responsável pelos scripts ou pelos modelos do projeto | **Informante secundário.** Descreve as pré-condições e os erros mais comuns da execução (C01, Q8), sem ser o usuário-alvo. Coordenar com a parte A03 (P02) para não abordar a mesma pessoa duas vezes |

**Se faltar gente no perfil principal:** se a análise de segmentação ainda for feita por uma ou duas pessoas, a alternativa é incluir alunos de Ciência da Computação da FEI com experiência em visão computacional fora da Baja, como participantes proxy. A limitação será registrada: eles conhecem a técnica, mas não o contexto dos testes.

#### Aspectos éticos

Valem a base normativa e as regras gerais descritas na A01: atividade de ensino (Resolução CNS 510/2016, art. 1º, parágrafo único), LGPD, participação voluntária, termo de consentimento, armazenamento fora do repositório e descarte ao fim do semestre. Abaixo, os riscos próprios desta parte.

| Dado ou situação | Risco neste projeto | Cuidado adotado |
|---|---|---|
| Dificuldade com código e com os scripts | A pessoa pode se sentir avaliada por não saber programar ou por não conseguir corrigir um erro | Deixar claro, no convite e no início, que se avalia o processo e não a pessoa; perguntar sobre o que acontece, e não sobre o que a pessoa "deveria saber" |
| Acompanhar a análise no computador da pessoa | A tela pode mostrar arquivos, mensagens e dados de outros integrantes | A pessoa escolhe o que mostrar e fecha o que não quiser; nada é fotografado ou copiado; anota-se só a sequência de passos |
| Gravação de tela | Mostra nome de usuário, caminhos de pastas e conversas abertas | Só com autorização explícita no termo e com as outras janelas fechadas; apagada logo após a análise |
| Imagens dos testes | Podem mostrar pilotos, outros integrantes e as instalações da FEI | Não copiar as imagens; se for preciso ilustrar algo na entrega, usar apenas imagens sem pessoas e com autorização da equipe |
| Erros que atrasaram uma resposta à equipe | Relatar a falha pode expor a pessoa perante a liderança | Pergunta opcional; o relato é anonimizado e não é repassado à liderança nem à coordenação |
| Comparação entre analistas | Com poucas pessoas, diferenças de critério podem ser atribuídas a alguém específico | Na divulgação, usar códigos (A1, A2…) e apresentar critérios de forma agregada ("parte dos analistas…"), sem ligar um critério a uma pessoa |

- **Anonimização:** as pessoas que participam desta coleta recebem códigos A1, A2… na transcrição, como descrito na A01. *(Isso se refere a quem participa da coleta de dados, não a usuários da interface, que não terá cadastro nem login.)*
- **Devolutiva:** a síntese anonimizada é compartilhada com quem participou antes do uso no projeto.

### A03 — Mateus Marana Assuena

**Autor(a):** Mateus Marana Assuena — 22.123.026-1  
**Persona e cenário:** P02 — Andreia Silva; C03 (tarefas T06, T07 e T08; a T02 é compartilhada com a P01)  
**Objetivo desta parte:** verificar quem, na equipe Baja FEI ou na pesquisa ligada a ela, define configurações de treino e treina os modelos, como os experimentos são feitos e comparados hoje e se essa pessoa usaria uma interface para isso. As respostas decidem o escopo da T08 (definir uma configuração e treinar), quais parâmetros a interface expõe e o estado das decisões de design 1 a 7 da P02, em especial o histórico (decisão 5).

> As afirmações sobre quem treina os modelos e sobre a rotina de pesquisa nesta seção são hipóteses `[H]` levantadas para planejar a coleta e serão conferidas com a equipe antes da aplicação.

#### Que dados coletar?

Os dados seguem os cinco grupos de Barbosa e Silva (2010). Como a P02 é a persona com mais conhecimento técnico, a coleta também precisa verificar se uma interface faz sentido para ela, e não só como a interface deveria ser.

| Dado/informação | Hipótese/lacuna relacionada | Por que é necessário | Qual decisão de design pode afetar |
|---|---|---|---|
| **Usuário.** Papel (coordenação da equipe, orientação de pesquisa, aluno pesquisador), relação com a Baja e tempo disponível por semana para experimentos | Perfil da P02 `[H]`; H07 | A P02 reúne "coordenadora" e "pesquisadora"; na prática, podem ser pessoas diferentes | Manter uma persona só ou separar quem treina de quem coordena (o que também afeta a "coordenação" do C02) |
| **Relação com tecnologia.** Como treina e executa os modelos hoje: ferramentas, ambiente, quanto tempo um treino leva e como acompanha o andamento | H05 (C03, Q26); T08 | O processo de um experimento é hipótese do C03 | Acompanhamento do treino (progresso por época, RC04) e o que mostrar ao voltar para a tela |
| **Relação com tecnologia.** Quais parâmetros de treino ajusta de fato (épocas, early stopping e paciência, datasets de treino, batch size, gráficos) e quais sempre deixa no padrão | T08; definição de configuração (E1, §7.1) | A lista de parâmetros expostos foi definida pela equipe, sem ouvir quem treina | Quais parâmetros a tela de configuração mostra, em que ordem e com quais valores padrão |
| **Relação com tecnologia.** Onde e em que janelas de tempo trabalha (entre aulas, em casa), se deixa treinos rodando e volta depois | Ambiente da P02 `[H]` (E3, seção 3.1; feedback da E3) | O professor pediu para descrever a situação de uso, não só o equipamento | Se o treino precisa continuar sem a pessoa na tela e como o estado é mostrado na volta |
| **Domínio.** Métricas e gráficos que usa para avaliar um experimento (IoU da classe trilha, acurácia, matriz de confusão, curvas de treino, tempo de inferência) | H04 (C03, Q20) | O C03 supõe que ela usa a matriz de confusão quando o IoU cai | Métricas e gráficos da comparação (decisão 3) e quanto detalhe técnico fica visível (decisão 6) |
| **Domínio.** O que considera um resultado insatisfatório e o que muda no experimento seguinte | C03, Q22 | Liga a análise de um resultado (T06) à próxima configuração (T08) | Se a interface precisa levar da análise para uma nova configuração sem recomeçar do zero |
| **Tarefas.** Critérios para escolher quais configurações testar e comparar | C03, Q18; T07 | O critério do C03 (borda da trilha em sombra, depois tempo de inferência) é hipótese | O que a comparação da T07 destaca e como as configurações são identificadas |
| **Tarefas.** Como compara experimentos hoje e quais informações precisa ver ao mesmo tempo | C03, Q19 e Q24 | A visualização conjunta (decisões 1 e 3) parte de uma necessidade não verificada | Composição da tela de comparação |
| **Tarefas.** Como registra os experimentos, se precisa recuperar resultados ou configurações antigas e o que precisaria recuperar | H08 (C03, Q23) | O histórico está fora do recorte até a Entrega 7 responder se ele é necessário; o professor alertou que perguntar sobre registros não basta para concluir que a funcionalidade é necessária | Incluir ou não o histórico (decisão 5) e, se incluir, o que ele guarda |
| **Tarefas.** Tipos de entrada usados nos experimentos (imagens, vídeos, de onde vêm) | C03, Q21 | Define as entradas que a interface precisa aceitar | Processamento de imagens e vídeos gravados (decisão 4) |
| **Tarefas.** Com que frequência faz experimentos, quanto duram e o que acontece quando um treino falha no meio | C03, Q26 e Q27 | A perda de tempo com falhas é a dor central da P02, sem evidência | Recuperação de falhas no treino e prioridade da T08 |
| **Tarefas.** Quem usa as conclusões dos experimentos e como elas chegam à escolha da configuração usada nos testes | H07 (C03, Q25 e Q28) | Liga a P02 à decisão da P03 (C02) e evita que a T07 e a T04 se sobreponham | Fronteira entre comparar para pesquisar (T07) e comparar para decidir (T04 e T05) |
| **Motivações e valores.** Se usaria uma interface para configurar e treinar ou prefere os próprios scripts, e quais informações técnicas não podem ficar escondidas | H12; decisão 6 da P02 | Para quem programa, a interface pode ser vista como limitação; é preciso saber se ela agrega | Manter a P02 como usuária da T08; nível de acesso a parâmetros e detalhes técnicos |

**Dados que não serão coletados:** resultados de pesquisa ainda não publicados (números, imagens, conjuntos de dados), informações sobre alunos orientados, avaliações acadêmicas e qualquer dado pessoal sensível. Para entender o processo, basta a pessoa descrever os passos; não é preciso ver os resultados.

#### De quem coletar?

Respostas às perguntas da aula para o recorte da P02 `[H]`:

- **Quem utilizará o sistema?** Quem define configurações de treino, treina os modelos e compara os experimentos.
- **Quem será afetado por ele?** Quem usa as configurações treinadas: quem analisa (P01), quem decide a configuração dos testes (P03) e, indiretamente, quem pilota (H03).
- **Quem decide quais objetivos o sistema deve apoiar?** Os autores do TCC e o orientador.
- **Quem definiu o processo atual?** Quem escreveu os scripts de treino e a coordenação da pesquisa.

| Perfil/stakeholder | Critério de inclusão | Relação com persona/público |
|---|---|---|
| Pessoas que definem configurações e treinam modelos de visão computacional ligados à Baja FEI (por exemplo, coordenação da equipe, orientação de pesquisa, alunos de iniciação científica ou de mestrado `[H]`) | Definiu ou acompanhou o treino de pelo menos um modelo de visão computacional no último ano; ter 18 anos ou mais; não ser autor deste projeto nem do TCC | **Perfil principal.** Corresponde à P02. Previsão de 1 a 3 pessoas `[H]` |
| Quem recebe as conclusões dos experimentos para decidir a configuração dos testes | Participa das reuniões em que a configuração é escolhida | **Informante secundário.** Corresponde à P03. São as mesmas pessoas da A01: as perguntas desta parte entram na mesma conversa, para não abordar ninguém duas vezes |
| Quem executa as configurações treinadas para analisar os testes | Mesmo critério do perfil principal da A02 | **Informante secundário.** Corresponde à P01. Confirma se as configurações chegam identificadas e prontas para uso (coordenar com a A02) |

**Exclusão dos autores:** os autores deste projeto e do TCC não entram como participantes do perfil principal, mesmo que treinem modelos, porque as respostas deles confirmariam as próprias hipóteses.

**Como o conhecimento dos autores é usado, sem entrar como evidência:**

- **Relato de processo:** os autores podem descrever fatos sobre o treino (passos, ferramentas e parâmetros existentes). Esse relato fica registrado como "relato da equipe", separado das respostas dos participantes, e não conta como evidência sobre necessidades, opiniões ou preferências.
- **Piloto do instrumento:** um autor responde ao instrumento antes da aplicação, para testar clareza e duração. Essas respostas não entram na análise.

**Se faltar gente no perfil principal:** a alternativa é ouvir pesquisadores de visão computacional da FEI fora da Baja (professores, pós-graduandos ou alunos de iniciação científica), como participantes proxy. A limitação será registrada: eles conhecem o treino de modelos, mas não o ciclo de testes do veículo.

#### Aspectos éticos

Valem a base normativa e as regras gerais descritas na A01: atividade de ensino (Resolução CNS 510/2016, art. 1º, parágrafo único), LGPD, participação voluntária, termo de consentimento, armazenamento fora do repositório e descarte ao fim do semestre. Abaixo, os riscos próprios desta parte.

| Dado ou situação | Risco neste projeto | Cuidado adotado |
|---|---|---|
| Participante pode ser professor(a) | A hierarquia se inverte: alunos entrevistando quem pode avaliá-los; o constrangimento pode suavizar as perguntas ou as respostas | Explicar no convite que a coleta é sobre o processo de experimentação, não sobre o trabalho da pessoa; o roteiro é o mesmo para qualquer participante e não se adapta ao cargo |
| Coordenação ou orientação com interesse no resultado | Quem orienta o TCC ou coordena a equipe tem interesse no projeto, o que pode enviesar as respostas | Declarar a relação no registro da coleta e tratar essas respostas como de participante interessado na síntese |
| Papel único na equipe | Se há uma só pessoa na coordenação, ela é identificável mesmo com código | Avisar no termo que o papel pode ser reconhecido; a pessoa escolhe se trechos dela podem ser citados e revisa as citações antes do uso |
| Resultados de pesquisa não publicados | Números, imagens e conjuntos de dados podem ser parte de um trabalho em andamento | Não pedir nem registrar resultados; perguntar só pelo processo; se a pessoa mostrar algo, não copiar |
| Tempo da pessoa | Agenda apertada entre aulas e orientações | Sessão curta, no horário que a pessoa escolher, com possibilidade de interromper e continuar outro dia |
| Tela com treinos em andamento | Pode mostrar arquivos, contas e dados de outros projetos | A pessoa escolhe o que mostrar; nada é fotografado; gravação de tela só com autorização e com as outras janelas fechadas |

- **Anonimização:** as pessoas que participam desta coleta recebem códigos PQ1, PQ2… na transcrição, como descrito na A01. *(Isso se refere a quem participa da coleta de dados, não a usuários da interface, que não terá cadastro nem login.)*
- **Devolutiva:** a síntese anonimizada é compartilhada com quem participou antes do uso no projeto.

## Parte B — ferramentas de coleta

> Cada integrante deve preparar uma técnica/instrumento completo. As técnicas devem ser diferentes entre si e **questionário deve estar entre as técnicas escolhidas**, conforme o enunciado da disciplina.

### Distribuição das técnicas

A escolha considerou o tamanho de cada público, o tipo de dado que cada Parte A pede e as regras da disciplina: técnicas diferentes e um questionário entre elas.

| Instrumento | Integrante | Técnica | Público principal | Por que essa técnica | Hipóteses principais |
|---|---|---|---|---|---|
| I01 | Henrique | Entrevista semiestruturada | Quem prepara ou toma a decisão sobre a configuração (perfil P03) | Poucas pessoas (2 a 4 `[H]`) e dados sobre um processo de decisão, papéis e critérios que pedem respostas abertas, exemplos concretos e aprofundamento | H07, H01, H04, H06, H12 |
| I02 | Tiago | Questionário | Quem analisa resultados de segmentação (perfil P01) | É o público maior (3 a 6 `[H]`) e parte dos dados é comparável entre pessoas: ferramentas conhecidas, familiaridade com métricas e termos, frequência e volume da análise | H02, H05, H09, H10, H11 e H03 |
| I03 | Mateus | Investigação contextual | Quem configura e treina os modelos (perfil P02) | Poucas pessoas (1 a 3 `[H]`) e uma atividade com conhecimento tácito (escolher parâmetros, acompanhar um treino, reagir a uma falha) que se entende melhor vendo a pessoa trabalhar | H08 e as lacunas da T08 |

**Participantes compartilhados:** a mesma pessoa não deve participar de mais de um instrumento como público principal. As perguntas da A03 para quem decide a configuração (como as conclusões dos experimentos chegam à decisão) entram no roteiro da I01. A H03 (piloto como beneficiário indireto) fica no questionário I02, com uma seção para quem acompanha os testes.

**Piloto dos instrumentos:** cada instrumento é testado antes por um autor deste projeto, para conferir clareza e duração. Essas respostas não entram na análise.

### Instrumento I01 — Entrevista semiestruturada

**Autor(a):** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3  
**Técnica:** entrevista semiestruturada (Barbosa e Silva, 2010): roteiro de perguntas abertas organizado em blocos, com aprofundamentos usados quando a resposta for vaga  
**Objetivo:** entender como a equipe Baja FEI escolhe hoje a configuração usada nos testes, quem participa da escolha, que informações chegam a quem decide e como elas são interpretadas, para sustentar, refutar ou refinar H07, H01, H04, H06 e H12 (Parte A, A01)  
**Público:** integrantes que preparam ou tomam a decisão sobre a configuração (perfil P03, 2 a 4 pessoas `[H]`). Blocos curtos são aplicados também a um integrante que executa os modelos e, se aceitar, à coordenação (informantes secundários da A01)  
**Duração prevista:** 30 a 40 minutos para o perfil principal; 10 a 15 minutos para os informantes secundários

#### Procedimento padronizado de aplicação

1. **Preparação**
   - Confirmar com a liderança da equipe quem exerce o papel de decisão (as hipóteses `[H]` da A01) e montar a lista de convidados.
   - Convidar cada pessoa individualmente, por mensagem escrita pela equipe do projeto, nunca pela coordenação, com o texto de convite abaixo.
   - Agendar uma sessão de até 40 minutos, presencial em sala reservada do laboratório (fora do horário de reunião da equipe) ou por videochamada, no horário escolhido pela pessoa.
   - Aplicar o piloto do roteiro com um autor deste projeto e ajustar perguntas confusas.
   - Levar o termo de consentimento, o roteiro e uma folha de anotações sem campo de nome (só o código). Definir dois papéis: um entrevistador, que conduz, e um anotador, que registra.
2. **Apresentação e consentimento**
   - Ler o texto de abertura do roteiro, sem improvisar o objetivo.
   - Entregar o termo, esperar a leitura, tirar dúvidas e registrar o aceite.
   - Perguntar se a pessoa autoriza a gravação de áudio. Se não autorizar, seguir só com anotações.
3. **Aplicação**
   - Seguir os blocos na ordem. As perguntas principais são feitas como estão escritas; os aprofundamentos só quando a resposta for vaga ou geral.
   - Pedir exemplos concretos ("a última vez que…") em vez de opiniões gerais.
   - Não sugerir respostas, não citar as personas nem as hipóteses e não mostrar protótipos ou telas, para não induzir.
   - Respeitar perguntas marcadas como opcionais e pedidos para pular uma pergunta.
4. **Encerramento**
   - Fazer a pergunta aberta final.
   - Lembrar o direito de desistir e de pedir a exclusão das respostas, e explicar a devolutiva.
   - Agradecer.
5. **Armazenamento e anonimização**
   - No mesmo dia, atribuir o código (G1, G2…; S1, S2… para informantes secundários) e guardar a gravação e as anotações na pasta privada da equipe, fora do repositório.
   - Em até dois dias, transcrever ou expandir as anotações, já sem nomes de pessoas.
   - Apagar o áudio depois da transcrição.
   - A lista que liga código e nome fica em arquivo separado e é apagada ao fim do semestre.

#### Instrumento

##### Texto do convite

> Olá, [nome]. Somos Henrique, Mateus e Tiago, da disciplina de Interação Humano-Computador da FEI. Estamos estudando como a equipe Baja escolhe a configuração do modelo de segmentação usada nos testes, para projetar uma interface que apoie essa atividade. Gostaríamos de conversar com você por cerca de 30 minutos, no dia e horário que preferir. A participação é voluntária, e você pode recusar sem nenhuma consequência na equipe. Seu nome não aparece em nenhum documento. Podemos marcar?

##### Termo de consentimento

> **Projeto:** Interface para análise de segmentação semântica de vias off-road — disciplina de Interação Humano-Computador, FEI.  
> **Atividade:** entrevista semiestruturada.  
> **Responsáveis:** Henrique Finatti Silveira Belo Trebbi, Mateus Marana Assuena e Tiago Fagundes dos Santos.
>
> **Convite e objetivo.** Você está sendo convidado(a) a participar de uma entrevista sobre como a equipe Baja FEI escolhe a configuração do modelo usada nos testes. **Estamos estudando o processo, não a sua capacidade.** Não há respostas certas ou erradas.
>
> **O que será solicitado.** Responder a perguntas abertas sobre a sua participação nessas decisões, por cerca de 30 a 40 minutos, presencialmente ou por videochamada.
>
> **Registros.** Com a sua autorização, a conversa será gravada em áudio, apenas para transcrição; o áudio é apagado depois de transcrito. Sem autorização, faremos só anotações. Não haverá gravação de vídeo nem de tela. Apenas os três responsáveis terão acesso aos registros, que ficam fora do repositório do projeto e são apagados ao fim do semestre letivo.
>
> **Privacidade.** Seu nome não aparece em nenhum documento: você recebe um código. Como a equipe é pequena, descreveremos o seu papel de forma genérica para evitar que você seja reconhecido(a). Nomes de colegas citados na conversa serão retirados. Se você mostrar planilhas ou mensagens, nada será copiado ou fotografado.
>
> **Voluntariedade.** A participação é voluntária. Você pode pular perguntas, interromper a entrevista a qualquer momento e pedir, mesmo depois, que suas respostas sejam excluídas, sem justificar. A coordenação da equipe não saberá quem participou.
>
> **Devolutiva.** Você receberá a síntese anonimizada e poderá apontar interpretações erradas antes de usarmos os resultados.
>
> **Consentimento.** Declaro que recebi informações suficientes e concordo em participar.  
> ( ) Autorizo a gravação de áudio. ( ) Não autorizo a gravação de áudio.  
> Código do participante: ______ Data: ___/___/______ Aceite: ______________________

##### Roteiro — texto de abertura (ler para o participante)

> "Obrigado por aceitar. Estamos estudando como a equipe escolhe a configuração do modelo de segmentação que vai para os testes, desde o momento em que os resultados ficam prontos até a decisão. Queremos entender como isso acontece hoje, com as dificuldades e o que funciona bem. Não estamos avaliando você nem ninguém da equipe, e não há resposta certa. Se alguma pergunta não fizer sentido para o seu papel, é só dizer."

##### Roteiro — perfil principal (quem prepara ou toma a decisão)

A coluna "Dado da A01" liga cada pergunta à tabela "Que dados coletar" da Parte A.

**Bloco 1 — Papel na equipe** (cerca de 3 minutos)

| # | Pergunta | Aprofundamentos (se necessário) | Dado da A01 |
|---|---|---|---|
| 1.1 | Qual é o seu papel na equipe Baja hoje e há quanto tempo você o exerce? | O que esse papel inclui no dia a dia? | Papel na equipe (H07) |
| 1.2 | Você participa das conversas em que se escolhe a configuração do modelo usada nos testes? De que forma? | Desde quando? Sempre ou só às vezes? | Papel na equipe (H07) |

**Bloco 2 — A última escolha de configuração** (cerca de 10 minutos)

| # | Pergunta | Aprofundamentos (se necessário) | Dado da A01 |
|---|---|---|---|
| 2.1 | Conte como foi a última vez em que a equipe escolheu qual configuração usar nos testes, desde o começo. | Quando foi? O que estava em jogo naquele teste? | Como a escolha acontece hoje (H07, H01) |
| 2.2 | Nessa ocasião, quem propôs as opções, quem trouxe os resultados e quem bateu o martelo? | Alguém recomendou uma opção? A decisão foi de uma pessoa ou do grupo? | Como a escolha acontece hoje (H07) |
| 2.3 | Resultados de experimentos de pesquisa (de quem treina os modelos) chegaram até essa escolha? Como? | Eles mudaram alguma coisa na decisão? | Pergunta da A03 para quem decide (C03, Q25 e Q28) |
| 2.4 | Com que frequência escolhas como essa acontecem, e quanto tempo você costuma ter para se preparar? | Isso muda perto de competições? | Frequência e tempo de preparo (H12) |

**Bloco 3 — Como os resultados chegam** (cerca de 5 minutos)

| # | Pergunta | Aprofundamentos (se necessário) | Dado da A01 |
|---|---|---|---|
| 3.1 | Naquela ocasião, como os resultados chegaram até você? | Em que formato? Quem enviou? Quanto tempo antes da reunião? | Como os resultados chegam (H01) |
| 3.2 | Que ferramentas você usou para olhar e comparar esses resultados? | Você mesmo(a) roda algum script ou depende de alguém? | Ferramentas usadas hoje (H05, H09) |
| 3.3 | Onde você costuma preparar essa escolha e onde ela é discutida? | Em que equipamento? A tela é compartilhada com o grupo? Há internet nesses lugares? | Onde e em que equipamento (ambiente da P03) |

**Bloco 4 — Leitura dos números** (cerca de 8 minutos)

| # | Pergunta | Aprofundamentos (se necessário) | Dado da A01 |
|---|---|---|---|
| 4.1 | Quando você recebeu esses resultados, o que olhou primeiro? Por quê? | E o que você deixou de lado? | Métricas lidas e ignoradas (H04) |
| 4.2 | Se um colega novo na equipe perguntasse o que esses números indicam, como você explicaria? *(Opcional; deixar claro que não é um teste.)* | Algum deles você nunca usa? | Métricas lidas e ignoradas (H04) |
| 4.3 | Há palavras nesses resultados ou nas conversas da equipe que você já precisou que alguém explicasse? Quais? | Que palavra você usa no lugar delas? | Termos que geram dúvida (H04, RC01) |
| 4.4 | Quando duas opções têm resultados parecidos, como você decide entre elas? | Você compara com alguma coisa: um resultado anterior, uma meta, a opinião de alguém? | Como julga uma diferença (H06) |

**Bloco 5 — A reunião e as consequências** (cerca de 8 minutos)

| # | Pergunta | Aprofundamentos (se necessário) | Dado da A01 |
|---|---|---|---|
| 5.1 | O que você leva para a reunião em que a escolha é discutida? | Que perguntas costumam fazer a você? Alguma você não conseguiu responder? | O que leva à reunião (H12) |
| 5.2 | Já aconteceu de uma escolha precisar ser revista depois de um teste? Pode contar como foi? *(Opcional.)* | O que motivou a revisão? Qual foi a consequência para a equipe? | Decisões revistas (H12; gravidade dos erros) |
| 5.3 | Na hora de decidir, você costuma voltar a escolhas ou resultados de ciclos anteriores? | Se sim: como encontra? O que procura? Se não: por que não? | Consulta a decisões anteriores (H08) |

**Bloco 6 — Preferências e valores** (cerca de 5 minutos)

| # | Pergunta | Aprofundamentos (se necessário) | Dado da A01 |
|---|---|---|---|
| 6.1 | Para preparar a escolha, você prefere comparar as opções você mesmo(a) ou receber um material já preparado por quem executou? Por quê? | O que esse material precisaria ter? | Comparar sozinho × receber material (feedback da E3) |
| 6.2 | Para você, o que é uma boa decisão sobre a configuração? E o que mais preocupa você ao tomá-la? | — | Motivações e valores (H12) |
| 6.3 | Numa escolha como essa, que papel uma ferramenta deveria ter? E que papel ela não deveria ter? | — | Motivações e valores (RQ08) |

**Encerramento**

| # | Pergunta | Dado da A01 |
|---|---|---|
| 7.1 | Tem alguma coisa sobre como a equipe escolhe a configuração que eu não perguntei e que você acha importante? | Lacunas não previstas |

##### Roteiro — informantes secundários (blocos curtos)

**Integrante que executa os modelos e entrega os resultados** (perfil P01)

| # | Pergunta | Aprofundamentos (se necessário) | Dado da A01 |
|---|---|---|---|
| S1.1 | Conte como você preparou os resultados para a última reunião em que se escolheu a configuração. | Em que formato? Com quanta antecedência? | Como os resultados chegam (H01) |
| S1.2 | Que perguntas quem decide costuma fazer a você sobre esses resultados? | Alguma se repete? | Termos e leitura dos números (H04) |

**Coordenação da equipe** *(participação opcional)*

| # | Pergunta | Aprofundamentos (se necessário) | Dado da A01 |
|---|---|---|---|
| S2.1 | Como funciona hoje a escolha da configuração usada nos testes, e qual é o papel da coordenação nela? | Quem tem a palavra final? | Como a escolha acontece hoje (H07) |
| S2.2 | O que você espera receber de quem prepara essa escolha? | — | O que leva à reunião (H12) |

**O que as perguntas evitam de propósito:** nenhuma pergunta cita painel, relatório, gráfico, histórico ou ranking como solução. A necessidade aparece, se existir, nas respostas sobre o que a pessoa faz hoje (blocos 3 a 5) e sobre o que espera (bloco 6).

#### Como os dados serão analisados

1. **Preparação do material:** transcrições ou anotações expandidas, uma por participante, identificadas só pelo código.
2. **Codificação temática dedutiva:** os códigos iniciais são as linhas da tabela "Que dados coletar" da A01 e as hipóteses H07, H01, H04, H06, H08 e H12. Cada trecho relevante recebe um ou mais códigos.
3. **Codificação indutiva:** trechos que não se encaixam em nenhum código inicial formam temas novos, registrados como lacunas não previstas.
4. **Matriz participante × tema:** uma tabela mostra o que cada participante disse sobre cada tema, com um trecho de apoio, para comparar papéis e encontrar convergências e divergências.
5. **Veredito por hipótese:** cada hipótese recebe "sustentada", "refutada", "refinada" ou "sem evidência", sempre com os trechos que justificam. Com 2 a 4 pessoas, os resultados são relatados como contagens ("2 de 3 participantes"), sem porcentagens nem generalização para outras equipes.
6. **Consequência para o design:** cada veredito é ligado à decisão que ele afeta (persona P03, tarefas T04 e T05, decisões de design 1 a 5 da P03, RQ08) e registrado na seção 5 do `RASTREABILIDADE.md`.
7. **Respostas dos informantes secundários:** usadas para triangular, ou seja, confirmar ou contradizer o que disse o perfil principal sobre o mesmo processo; não sustentam sozinhas uma hipótese.

### Instrumento I02 — Questionário

**Autor(a):** Tiago Fagundes dos Santos — 22.123.017-0  
**Técnica:** questionário on-line autoaplicado (Google Forms), com perguntas fechadas (múltipla escolha, caixas de seleção, grades com escala) e algumas abertas opcionais  
**Objetivo:** caracterizar quem analisa os resultados da segmentação na equipe Baja FEI (conhecimento de programação separado do conhecimento para interpretar os resultados, ferramentas conhecidas, familiaridade com métricas e termos, frequência, volume e contexto da análise) e verificar se quem acompanha os testes se beneficia dos resultados, para sustentar, refutar ou refinar H02, H05, H09, H10, H11 e H03 (Parte A, A02)  
**Público:** integrantes que analisam resultados de segmentação ou outros dados dos testes (perfil P01, 3 a 6 pessoas `[H]`) e integrantes que acompanham os testes, pilotam ou descarregam as imagens (seção 8, H03)  
**Duração prevista:** cerca de 10 minutos

#### Procedimento padronizado de aplicação

1. **Preparação**
   - O formulário está no Google Forms, com as mesmas perguntas e desvios da cópia textual abaixo. Configurações de privacidade: não coleta e-mail, não exige login, não permite editar a resposta depois de enviada e não mostra as respostas dos outros a quem responde. Antes da aplicação, conferir os caminhos de resposta no modo de visualização.
   - Aplicar o piloto com um autor deste projeto, cronometrando (meta: até 12 minutos), ajustar perguntas confusas e apagar a resposta do piloto.
   - Confirmar com a liderança da equipe quem analisa resultados e quem acompanha os testes (hipóteses `[H]` da A02) e excluir da lista quem já participa da I01 ou da I03 como público principal.
2. **Apresentação e consentimento**
   - Enviar o link individualmente, por mensagem da equipe do projeto (nunca pela coordenação), com o texto de convite abaixo.
   - A primeira seção do formulário é o termo de consentimento; quem não concordar ou tiver menos de 18 anos é levado direto ao fim, sem responder nada.
3. **Aplicação**
   - O formulário fica aberto por 7 dias. Um único lembrete é enviado no 4º dia, para todos, sem saber quem já respondeu.
   - Ninguém acompanha o preenchimento; dúvidas são respondidas pelos responsáveis, sem sugerir respostas.
4. **Encerramento**
   - No fim do prazo, desativar "Aceitando respostas".
   - A mensagem de confirmação agradece e informa a devolutiva.
5. **Armazenamento e anonimização**
   - O formulário não coleta nome nem e-mail.
   - Exportar as respostas para uma planilha na pasta privada da equipe, fora do repositório, e excluir as respostas do Google Forms.
   - Numerar as respostas (A1, A2… para quem analisa; T1, T2… para quem acompanha os testes) e retirar de respostas abertas qualquer nome ou detalhe que identifique alguém.
   - Apagar a planilha ao fim do semestre letivo.

#### Instrumento

##### Texto do convite

> Olá! Somos Henrique, Mateus e Tiago, da disciplina de Interação Humano-Computador da FEI. Estamos estudando como a equipe Baja analisa os resultados da segmentação das imagens dos testes, para projetar uma interface que apoie essa atividade. Você poderia responder a um questionário de cerca de 10 minutos? Ele não pede nome nem e-mail, e a participação é voluntária: https://forms.gle/pAMyXCdebYo9aHmq9. Obrigado!

##### Questionário (cópia textual)

As perguntas abaixo são as mesmas do formulário on-line, na mesma ordem. A coluna "Dado da A02" liga cada pergunta à tabela "Que dados coletar" da Parte A.

**Título no formulário:** Análise de resultados de segmentação na equipe Baja FEI  
**Link do formulário:** [https://forms.gle/pAMyXCdebYo9aHmq9](https://forms.gle/pAMyXCdebYo9aHmq9)

**Descrição (topo do formulário):** Questionário da disciplina de Interação Humano-Computador (FEI). Queremos entender como a equipe Baja FEI analisa os resultados da segmentação de imagens dos testes, para projetar uma interface que apoie essa atividade. Leva cerca de 10 minutos. Não pedimos nome nem e-mail.

##### Seção 1 — Termo de consentimento

> **Objetivo.** Entender como a equipe analisa os resultados da segmentação de imagens dos testes. **Estamos estudando o processo, não a sua capacidade.** Não há respostas certas ou erradas, e "não sei" é uma resposta válida.
>
> **O que será solicitado.** Responder a perguntas de múltipla escolha e algumas abertas, por cerca de 10 minutos.
>
> **Privacidade.** O formulário não coleta nome nem e-mail. Nas análises, as respostas recebem um código, e combinações de dados que possam identificar alguém (como curso, tempo de equipe e atividade juntos) não são divulgadas. As respostas ficam em uma pasta privada dos três responsáveis, fora do repositório do projeto, e são apagadas ao fim do semestre letivo.
>
> **Voluntariedade.** A participação é voluntária. As perguntas abertas são opcionais, e você pode fechar o formulário a qualquer momento sem enviar. A coordenação da equipe não saberá quem respondeu.
>
> **Responsáveis.** Henrique Finatti Silveira Belo Trebbi, Mateus Marana Assuena e Tiago Fagundes dos Santos.

| # | Pergunta | Tipo | Opções | Obrigatória | Dado da A02 |
|---|---|---|---|:-:|---|
| 1.1 | Você tem 18 anos ou mais e concorda em participar nos termos acima? | Múltipla escolha | Sim, tenho 18 anos ou mais e concordo em participar; Não | sim | Consentimento e critério de inclusão (A02) |

**Desvio na 1.1:** "Sim, tenho 18 anos ou mais e concordo em participar" → Seção 2; "Não" → Enviar formulário.

##### Seção 2 — Sua participação na equipe

| # | Pergunta | Tipo | Opções | Obrigatória | Dado da A02 |
|---|---|---|---|:-:|---|
| 2.1 | Há quanto tempo você está na equipe Baja FEI? | Múltipla escolha | Menos de 6 meses; De 6 meses a 1 ano; De 1 a 2 anos; Mais de 2 anos | sim | Usuário: tempo na equipe (H02) |
| 2.2 | Qual é o seu curso? | Múltipla escolha | Ciência da Computação; Engenharia Mecânica; Engenharia Elétrica; Engenharia de Controle e Automação; Outro | sim | Usuário: curso (H02) |
| 2.3 | No último semestre, qual destas opções descreve melhor a sua participação nos testes do veículo? | Múltipla escolha | Analiso ou executo a segmentação de imagens dos testes; Analiso outros dados dos testes (telemetria, vídeos, fotos), mas não a segmentação; Acompanho os testes, piloto ou descarrego as imagens das câmeras, sem analisar resultados; Nenhuma dessas | sim | Papel na equipe; direciona para o perfil principal (P01) ou para quem acompanha os testes (H03) |

**Desvio na 2.3:** "Analiso ou executo a segmentação de imagens dos testes" → Seção 3; "Analiso outros dados dos testes (telemetria, vídeos, fotos), mas não a segmentação" → Seção 3; "Acompanho os testes, piloto ou descarrego as imagens das câmeras, sem analisar resultados" → Seção 8; "Nenhuma dessas" → Seção 9.

##### Seção 3 — Programação e execução

| # | Pergunta | Tipo | Opções | Obrigatória | Dado da A02 |
|---|---|---|---|:-:|---|
| 3.1 | Com que frequência você programa, em qualquer linguagem? | Múltipla escolha | Nunca; Raramente; Algumas vezes por mês; Toda semana | sim | Programação (H02) |
| 3.2 | Quem executa a segmentação dos resultados que você analisa? | Múltipla escolha | Eu mesmo(a), sem ajuda; Eu mesmo(a), mas às vezes preciso de ajuda; Outra pessoa executa e me envia os resultados; Não analiso segmentação | sim | Execução atual (H02, H05) |
| 3.3 | Indique o quanto você concorda com cada frase. | Grade de múltipla escolha | Linhas: Consigo resolver sozinho(a) um erro que interrompe a execução; Entendo o que os scripts de segmentação do projeto fazem; A execução da segmentação costuma funcionar sem problemas. Colunas: Discordo totalmente; Discordo; Neutro; Concordo; Concordo totalmente; Não se aplica | não | Execução atual e programação × análise (H02, H05) |
| 3.4 | Conte a última vez em que a execução da segmentação falhou ou deu um resultado inesperado. O que aconteceu e o que você fez? | Parágrafo | — | não | Erros mais comuns e como são contornados (H05; C01, Q2 e Q8) |

**Depois desta seção:** Seção 4.

##### Seção 4 — Ferramentas

| # | Pergunta | Tipo | Opções | Obrigatória | Dado da A02 |
|---|---|---|---|:-:|---|
| 4.1 | Quais destas ferramentas você usa pelo menos uma vez por mês? | Caixas de seleção | Editor de código (por exemplo, VS Code); Terminal ou linha de comando; GitHub ou GitLab; Jupyter Notebook ou Google Colab; Planilhas (Excel, Google Planilhas); Ferramentas de telemetria do veículo; Nenhuma dessas; Outro | não | Ferramentas usadas (H09) |
| 4.2 | Você conhece estas ferramentas de visão computacional? | Grade de múltipla escolha | Linhas: CVAT; Roboflow; Supervisely. Colunas: Não conheço; Conheço, mas nunca usei; Já usei; Uso com frequência | não | Ferramentas de visão computacional (H10) |
| 4.3 | Se já usou alguma delas, o que achou mais fácil e o que achou mais difícil? | Parágrafo | — | não | Complexidade das ferramentas (H10) |
| 4.4 | Nas ferramentas que você usa para analisar dados ou imagens, quais destes recursos você costuma usar? | Caixas de seleção | Ver duas imagens ou resultados lado a lado; Barra ou indicador de progresso; Arrastar arquivos para a janela; Atalhos de teclado; Filtrar ou ordenar tabelas; Exportar imagens ou relatórios; Nenhum desses; Outro | não | Padrões familiares (H11); atalhos (decisão 5 da P01) |

**Depois desta seção:** Seção 5.

##### Seção 5 — Como você analisa os resultados

| # | Pergunta | Tipo | Opções | Obrigatória | Dado da A02 |
|---|---|---|---|:-:|---|
| 5.1 | Com que frequência você analisa resultados de segmentação? | Múltipla escolha | Depois de cada teste de campo; Algumas vezes por mês; Raramente; Não analiso segmentação | sim | Frequência (C01, Q9) |
| 5.2 | Em uma análise típica, quantas imagens ou trechos de vídeo você analisa? | Múltipla escolha | Até 10; De 11 a 50; De 51 a 200; Mais de 200; Não sei | não | Volume por sessão (C01, Q9) |
| 5.3 | Onde você costuma fazer essa análise? | Caixas de seleção | Laboratório da FEI; À beira da pista, durante os testes; Em casa; Outro | não | Ambiente da P01 `[?]` |
| 5.4 | Em que equipamento? | Caixas de seleção | Computador do laboratório; Notebook próprio; Celular ou tablet; Outro | não | Ambiente da P01 `[?]` |
| 5.5 | Durante a análise, com que frequência acontece cada situação? | Grade de múltipla escolha | Linhas: Ser interrompido(a); Ficar sem conexão com a internet. Colunas: Nunca; Às vezes; Com frequência; Não sei | não | Interrupções e conectividade (decisão 5 da P01) |
| 5.6 | Como você decide se uma máscara de segmentação está correta? | Parágrafo | — | não | Critério de correção (H06; C01, Q7) |
| 5.7 | Quando um resultado parece errado, com que frequência você consegue dizer se o problema é do modelo ou da imagem (sombra, poeira, desfoque)? | Múltipla escolha | Quase sempre; Às vezes; Raramente; Nunca; Não sei | não | Falha do modelo × falha da imagem (H06) |
| 5.8 | O que você costuma fazer quando não tem certeza se o resultado está certo? | Caixas de seleção | Peço a opinião de um colega; Executo de novo com outra configuração; Consulto as métricas; Marco a imagem para revisar depois; Deixo a imagem de lado; Outro | não | O que faz na dúvida (C01, Q7) |

**Depois desta seção:** Seção 6.

##### Seção 6 — Métricas e termos

*Não há problema em responder "não sei": queremos saber quais termos precisam de explicação, não testar conhecimento.*

| # | Pergunta | Tipo | Opções | Obrigatória | Dado da A02 |
|---|---|---|---|:-:|---|
| 6.1 | Quanto você conhece cada termo? | Grade de múltipla escolha | Linhas: IoU (Intersection over Union); Acurácia; Tempo de inferência; Matriz de confusão; Conjunto de teste anotado; Época (de treino). Colunas: Não conheço; Conheço o nome, mas não sei explicar; Sei explicar; Uso para tomar decisões | não | Métricas e termos (H04, RC01) |
| 6.2 | Na sua opinião, IoU e acurácia podem ser calculadas para qualquer imagem nova capturada em um teste? | Múltipla escolha | Sim; Não, só para imagens que têm uma marcação de referência feita à mão; Não sei | não | Métricas dependem de anotação (H04; INC-52) |
| 6.3 | Que palavras nos resultados de segmentação ou nas conversas da equipe sobre eles já causaram dúvida para você? | Parágrafo | — | não | Termos que geram dúvida (RC01; legenda, decisão 2 da P01) |

**Depois desta seção:** Seção 7.

##### Seção 7 — Comparação, organização e entrega

| # | Pergunta | Tipo | Opções | Obrigatória | Dado da A02 |
|---|---|---|---|:-:|---|
| 7.1 | Quando você compara os resultados de duas configurações, como faz hoje? | Caixas de seleção | Abro as imagens em janelas lado a lado; Comparo números em uma planilha; Alterno entre arquivos; Peço para outra pessoa comparar; Não costumo comparar; Outro | não | Como compara hoje (T03; C01, Q5) |
| 7.2 | Como é escolhida a configuração que você compara com a que está em uso? | Múltipla escolha | É a mais recente treinada; Alguém da equipe indica; É a que teve as melhores métricas antes; Eu não escolho; já recebo definida; Não costumo comparar; Outro | não | Como escolhe a configuração (C01, Q5) |
| 7.3 | Com que frequência você precisa voltar a resultados de análises anteriores? | Múltipla escolha | Nunca; Raramente; Algumas vezes por mês; Toda semana | não | Necessidade de voltar a análises (H08) |
| 7.4 | Quando precisa encontrar um resultado antigo, como você faz? | Parágrafo | — | não | Organização dos arquivos (H08; C01, Q3) |
| 7.5 | Para quem você entrega o resultado da análise? | Caixas de seleção | Grupo de mensagens da equipe; Gestão ou liderança da equipe; Coordenação; Na reunião da equipe; Não entrego; uso só para mim; Outro | não | Destinatários (C01, Q4) |
| 7.6 | Em que formato? | Caixas de seleção | Mensagem de texto; Prints ou imagens; Planilha; Slides; Relatório; Outro | não | Formato da entrega (exportação, decisão 4 da P01) |
| 7.7 | Para aprender uma ferramenta nova, você prefere: | Múltipla escolha | Explorar sozinho(a), fazendo; Seguir um tutorial ou guia; Que alguém me mostre; Outro | não | Motivações: forma de aprender (ajuda contextual) |
| 7.8 | Para você, o que é uma análise de segmentação bem feita? | Parágrafo | — | não | Motivações e valores |

**Depois desta seção:** Seção 9.

##### Seção 8 — Para quem acompanha os testes

| # | Pergunta | Tipo | Opções | Obrigatória | Dado da A02 |
|---|---|---|---|:-:|---|
| 8.1 | Você usa ou consulta os resultados da segmentação no seu trabalho na equipe? | Múltipla escolha | Sim, com frequência; Às vezes; Não | não | Interação direta com os resultados (H03) |
| 8.2 | O resultado da análise de segmentação muda alguma coisa no que você faz nos testes? | Múltipla escolha | Sim; Não; Não sei | não | Benefício indireto (H03) |
| 8.3 | Se respondeu "Sim" na pergunta anterior, o que muda? | Parágrafo | — | não | Benefício indireto (H03) |
| 8.4 | Em que condições as imagens dos testes costumam ser capturadas? | Caixas de seleção | Sol forte; Sombra de vegetação; Poeira; Chuva ou lama; Pouca luz; Não sei; Outro | não | Condições de captura e falhas da imagem (C01, Q6; H06) |
| 8.5 | Quanto tempo depois do teste as imagens chegam a quem analisa? | Múltipla escolha | No mesmo dia; No dia seguinte; Na mesma semana; Mais de uma semana depois; Não sei | não | Origem e prazo das imagens (C01, Q6) |

**Depois desta seção:** Seção 9.

##### Seção 9 — Para terminar

| # | Pergunta | Tipo | Opções | Obrigatória | Dado da A02 |
|---|---|---|---|:-:|---|
| 9.1 | Há algo sobre a análise dos resultados de segmentação que não perguntamos e que você considera importante? | Parágrafo | — | não | Lacunas não previstas |

**Depois desta seção:** Enviar formulário.

**Mensagem de confirmação:** Obrigado por participar! Suas respostas foram registradas sem nome nem e-mail. Quando a análise estiver pronta, a síntese anonimizada será compartilhada com a equipe.

**O que as perguntas evitam de propósito:** nenhuma pergunta pergunta se a pessoa quer um painel, um histórico ou um relatório. A pergunta 4.4 lista recursos que a pessoa já usa em outras ferramentas, e as perguntas 7.3 e 7.4 investigam se ela volta a análises antigas, sem propor a solução. As opções fechadas sempre incluem "Outro", "Não sei" ou "Nenhum desses".

#### Como os dados serão analisados

1. **Separação dos grupos:** as respostas de quem analisa (seções 3 a 7) e de quem acompanha os testes (seção 8) são analisadas separadamente.
2. **Perguntas fechadas:** contagem de respostas por opção. Com 3 a 6 pessoas, os resultados são relatados como contagens ("4 de 5"), sem porcentagens nem médias de escala.
3. **Programação × interpretação (H02):** a 3.1 e a 3.3 (programação e execução) são cruzadas com a 6.1 e a 5.7 (leitura das métricas e da máscara). O objetivo é ver se quem programa também interpreta bem os resultados, ou o contrário, como pediu o feedback da Entrega 1.
4. **Termos (6.1 e 6.3):** os termos que mais aparecem como "conheço o nome, mas não sei explicar" ou citados como dúvida são candidatos a explicação no ponto de uso (RC01) e a troca de rótulo na legenda.
5. **Perguntas abertas:** codificação temática simples, com a mesma lógica do I01: códigos iniciais a partir das linhas da A02 e temas novos quando aparecerem.
6. **Veredito por hipótese:** H02, H05, H09, H10, H11 e H03 recebem "sustentada", "refutada", "refinada" ou "sem evidência", com as contagens e os trechos que justificam. A H08 recebe só uma contribuição (7.3 e 7.4), a ser somada à I03.
7. **Consequência para o design:** cada veredito é ligado à decisão que afeta (persona P01, tarefas T01 a T03, decisões de design 1 a 5 da P01) e registrado na seção 5 do `RASTREABILIDADE.md`.
8. **Limitações:** respostas autodeclaradas e amostra pequena. Os resultados são cruzados com a I01 (o que quem decide diz sobre como os resultados chegam) e com a I03 (como as configurações chegam a quem analisa). Combinações de curso, tempo de equipe e atividade não são publicadas juntas, para ninguém ser identificado.

### Instrumento I03 — Investigação contextual

**Autor(a):** Mateus Marana Assuena — 22.123.026-1  
**Técnica:** investigação contextual (Barbosa e Silva, 2010): estudo de campo no ambiente da pessoa, com observação e entrevista, no modelo mestre-aprendiz. A pessoa faz o próprio trabalho e ensina enquanto faz (mestre); quem conduz observa e pergunta para aprender (aprendiz). Segue os quatro princípios da técnica: **contexto** (o trabalho real, no lugar onde acontece), **parceria** (a pessoa conduz, o aprendiz acompanha), **interpretação** (o entendimento é conferido com a pessoa) e **foco** (os dados da A03)  
**Objetivo:** entender, vendo o trabalho acontecer, como quem configura e treina modelos define uma configuração, acompanha o treino, reage a falhas, analisa e compara os experimentos e registra o que fez, para sustentar, refutar ou refinar a H08 e as lacunas da T08 e da P02 (Parte A, A03)  
**Público:** pessoas que definem configurações e treinam modelos ligados à Baja FEI (perfil P02, 1 a 3 pessoas `[H]`), excluídos os autores deste projeto e do TCC  
**Duração prevista:** duas sessões de cerca de 40 minutos, porque um treino pode levar mais tempo do que uma visita: a **sessão 1** acompanha a definição da configuração e o início do treino; a **sessão 2**, depois que o treino termina, acompanha a análise e a comparação dos resultados. Se a pessoa preferir, as duas partes acontecem no mesmo dia, com um intervalo

#### Procedimento padronizado de aplicação

1. **Preparação**
   - Confirmar com a equipe quem treina os modelos (hipóteses `[H]` da A03) e convidar cada pessoa individualmente, com o texto de convite abaixo.
   - Agendar as sessões no local e no horário em que a pessoa já faria um experimento, para observar trabalho real, e não uma demonstração montada.
   - Treinar o aprendiz: um autor deste projeto demonstra o próprio fluxo de treino enquanto o aprendiz aplica o roteiro e preenche a ficha. Esse ensaio serve para treinar quem conduz e não entra na análise.
   - Levar o termo, o roteiro de foco e fichas de registro sem campo de nome. Definir dois papéis: o aprendiz, que conversa com a pessoa, e o anotador, que preenche a ficha.
2. **Apresentação e consentimento**
   - Ler o texto de abertura, que explica o modelo mestre-aprendiz.
   - Entregar o termo, esperar a leitura, tirar dúvidas e registrar o aceite, incluindo as escolhas sobre gravação de áudio, gravação de tela e citação de trechos.
3. **Aplicação**
   - **Conversa inicial** (5 minutos): perguntas da fase 1 do roteiro.
   - **Observação com perguntas** (30 minutos por sessão): a pessoa trabalha normalmente e explica o que faz. O aprendiz observa os pontos do roteiro e pergunta só em pausas naturais, sem interromper uma ação em andamento.
   - **Interpretação compartilhada** (5 a 10 minutos, ao fim da sessão 2): o aprendiz resume o que entendeu e a pessoa confirma ou corrige.
   - O aprendiz não sugere outro jeito de fazer, não opina sobre o trabalho e não mostra telas ou protótipos do projeto.
4. **Encerramento**
   - Fazer a pergunta aberta final, lembrar o direito de desistir e de pedir a exclusão dos registros, explicar a devolutiva e agradecer.
5. **Armazenamento e anonimização**
   - No mesmo dia, completar a ficha de registro com o código da pessoa (PQ1, PQ2…) e guardar ficha, áudio e gravação de tela, se autorizados, na pasta privada da equipe, fora do repositório.
   - Apagar áudio e gravação de tela logo depois de completar a ficha; nada é fotografado.
   - Retirar das fichas nomes de pessoas, números de resultados e nomes de arquivos de pesquisa não publicados.

#### Instrumento

##### Texto do convite

> Olá, [nome]. Somos Henrique, Mateus e Tiago, da disciplina de Interação Humano-Computador da FEI. Estamos estudando como são feitos os experimentos com os modelos de segmentação da Baja (configurar, treinar, analisar e comparar) para projetar uma interface que apoie esse trabalho. Gostaríamos de acompanhar você enquanto faz um experimento que já faria de qualquer forma, em duas conversas de cerca de 40 minutos, no local e horário que preferir. Não vamos avaliar o seu trabalho nem copiar resultados. A participação é voluntária e pode ser recusada sem nenhuma consequência. Podemos combinar?

##### Termo de consentimento

> **Projeto:** Interface para análise de segmentação semântica de vias off-road — disciplina de Interação Humano-Computador, FEI.  
> **Atividade:** investigação contextual (acompanhamento de um experimento, com conversa).  
> **Responsáveis:** Henrique Finatti Silveira Belo Trebbi, Mateus Marana Assuena e Tiago Fagundes dos Santos.
>
> **Convite e objetivo.** Você está sendo convidado(a) a mostrar como faz um experimento com os modelos de segmentação, explicando enquanto trabalha. **Estamos estudando o processo, não a sua capacidade nem os resultados da sua pesquisa.**
>
> **O que será solicitado.** Fazer um experimento que você já faria, no seu local de trabalho, em duas sessões de cerca de 40 minutos, respondendo a perguntas quando houver uma pausa.
>
> **Registros.** Faremos anotações. Com a sua autorização, também gravaremos o áudio e, com as outras janelas fechadas, a tela, apenas para completar as anotações; essas gravações são apagadas logo depois. Nada será fotografado, e resultados, imagens e arquivos da sua pesquisa não serão copiados. Apenas os três responsáveis terão acesso aos registros, que ficam fora do repositório do projeto e são apagados ao fim do semestre letivo.
>
> **Privacidade.** Seu nome não aparece em nenhum documento: você recebe um código. Como há poucas pessoas que treinam modelos na equipe, seu papel pode ser reconhecido; por isso, você escolhe se trechos da conversa podem ser citados e pode revisar as citações antes do uso.
>
> **Voluntariedade.** A participação é voluntária. Você pode interromper a qualquer momento, pular perguntas e pedir, mesmo depois, que os registros sejam excluídos, sem justificar.
>
> **Devolutiva.** Você receberá a síntese anonimizada e poderá apontar interpretações erradas antes do uso.
>
> **Consentimento.** Declaro que recebi informações suficientes e concordo em participar.  
> ( ) Autorizo a gravação de áudio. ( ) Não autorizo.  
> ( ) Autorizo a gravação de tela, com as outras janelas fechadas. ( ) Não autorizo.  
> ( ) Autorizo a citação de trechos, depois de revisá-los. ( ) Não autorizo.  
> Código do participante: ______ Data: ___/___/______ Aceite: ______________________

##### Texto de abertura (ler para o participante)

> "Obrigado por nos receber. Hoje você é quem ensina: faça o seu experimento como faria normalmente e vá contando o que está fazendo e por quê. Nós vamos observar e, quando houver uma pausa, perguntar o que não entendermos. Não existe jeito certo ou errado, e não estamos avaliando você nem a sua pesquisa. Se quiser parar ou não mostrar alguma coisa, é só dizer."

##### Roteiro de foco

A coluna "Dado da A03" liga cada ponto à tabela "Que dados coletar" da Parte A. As perguntas servem de apoio: o aprendiz só as usa quando o que está observando não responde por si.

**Fase 1 — Conversa inicial** (no começo da sessão 1)

| # | Pergunta | Dado da A03 |
|---|---|---|
| 1.1 | Qual é o seu papel na equipe Baja ou na pesquisa ligada a ela? Quanto tempo por semana você consegue dedicar a experimentos? | Papel e tempo disponível (perfil da P02; H07) |
| 1.2 | Que experimento você vai fazer hoje e o que quer descobrir com ele? | Critérios para escolher o que testar (C03, Q18 e Q28) |
| 1.3 | Onde e quando você costuma fazer esse trabalho? Hoje é um dia típico? | Onde e em que janelas de tempo trabalha (ambiente da P02) |

**Fase 2 — Sessão 1: definir a configuração e iniciar o treino**

| # | O que observar | Perguntas de apoio (só em pausas) | Dado da A03 |
|---|---|---|---|
| 2.1 | O que a pessoa consulta antes de definir a configuração (anotações, resultados anteriores, colegas) | "De onde veio a ideia de testar isso?" | Critérios para escolher o que testar (Q18); registro de experimentos (H08) |
| 2.2 | Quais parâmetros ela altera e quais deixa no padrão (épocas, early stopping e paciência, datasets de treino, batch size, gráficos) | "Por que esse valor?" "Tem algum que você nunca muda?" | Parâmetros ajustados de fato (T08) |
| 2.3 | O que ela confere antes de iniciar o treino e como o inicia | "O que poderia dar errado neste ponto?" | Como treina hoje (H05; Q26) |
| 2.4 | O que ela olha enquanto o treino avança, se fica esperando ou sai e volta depois | "Como você sabe se está indo bem?" "O que costuma fazer enquanto espera?" | Acompanhamento do treino; janelas de tempo |
| 2.5 | Se o treino parar ou der erro: como ela percebe, o que faz e quanto trabalho perde | Se não houver falha: "Já aconteceu de um treino parar no meio? O que você fez?" | Falhas no treino (Q26 e Q27) |
| 2.6 | Interrupções, equipamento usado e outras atividades que disputam a atenção | — | Ambiente da P02 |

**Fase 2 — Sessão 2: analisar e comparar os resultados**

| # | O que observar | Perguntas de apoio (só em pausas) | Dado da A03 |
|---|---|---|---|
| 3.1 | O que a pessoa abre primeiro quando o treino termina (métricas, curvas de treino, matriz de confusão, imagens, tempo de inferência) | "O que isso te diz?" | Métricas e gráficos usados (H04; Q20) |
| 3.2 | Como examina as imagens segmentadas e o que considera um resultado insatisfatório | "O que faria agora com esse resultado?" | Resultado insatisfatório e próximo experimento (Q22) |
| 3.3 | Como coloca dois experimentos lado a lado e o que precisa ver ao mesmo tempo | "Como você sabe qual resultado veio de qual configuração?" | Como compara e o que vê junto (Q19 e Q24) |
| 3.4 | Que entradas usa (imagens, vídeos) e de onde vêm | "Essas imagens são sempre as mesmas?" | Tipos de entrada (Q21) |
| 3.5 | Onde e como registra o experimento; se volta de fato a um experimento antigo durante o trabalho | Só se a pessoa quiser mostrar: "Como você encontraria um experimento do mês passado?" | Registro e recuperação de experimentos (H08; Q23) |
| 3.6 | Para quem a conclusão vai e em que formato | "Quem usa essa conclusão? Como ela chega à escolha da configuração dos testes?" | Uso das conclusões (H07; Q25 e Q28) |

**Fase 3 — Interpretação compartilhada** (ao fim da sessão 2)

| # | Pergunta | Dado da A03 |
|---|---|---|
| 4.1 | O aprendiz resume em três a cinco frases o que entendeu ("Pelo que vi, você primeiro…, depois…, e o mais demorado é…") e pergunta: "Entendi certo? O que corrigiria?" | Confirmação das observações (princípio da interpretação) |
| 4.2 | Que partes desse trabalho você gostaria que tomassem menos tempo? E quais você faz questão de continuar fazendo do seu jeito, nos seus próprios scripts? | Interface × scripts próprios (H12; decisão 6 da P02) |
| 4.3 | Que informações técnicas você precisa ter sempre à vista para confiar em um resultado? | Informações técnicas que não podem ficar escondidas (decisão 6 da P02) |

**Fase 4 — Encerramento**

| # | Pergunta | Dado da A03 |
|---|---|---|
| 5.1 | Tem alguma parte do seu trabalho com os modelos que não vimos hoje e que você acha importante? | Lacunas não previstas |

**O que o roteiro evita de propósito:** a pergunta 3.5 observa se a pessoa volta de fato a experimentos antigos, em vez de perguntar se ela quer um histórico. Atende ao alerta do professor de que perguntar sobre registros não basta para concluir que a funcionalidade é necessária. Nenhuma pergunta propõe telas ou funcionalidades.

##### Ficha de registro (uma por sessão)

| Campo | Registro |
|---|---|
| Código e sessão | PQ__ · sessão 1 ou 2 |
| Data, local e duração | |
| Equipamento e ferramentas usados | |
| Interrupções (quantas e de que tipo) | |
| Artefatos consultados (anotações, planilhas, resultados anteriores) | Descrever o tipo e o uso, sem copiar o conteúdo |
| Rupturas e contornos | O que deu errado ou travou e o que a pessoa fez |
| Citações da pessoa | Sem nomes; marcar se a citação foi autorizada |
| Dúvidas para a interpretação compartilhada | |

**Sequência de passos** (preenchida durante a observação):

| Horário | Passo observado | Ferramenta | O que a pessoa disse (intenção) | Observação do aprendiz |
|---|---|---|---|---|
| | | | | |

#### Como os dados serão analisados

1. **Sessão de interpretação da equipe:** em até dois dias, aprendiz e anotador leem as fichas para os outros autores, e cada observação relevante vira uma nota curta (um fato ou uma fala por nota), identificada pelo código.
2. **Modelo de sequência:** para cada pessoa, a sequência de passos, intenções e rupturas de um experimento completo (configurar, treinar, acompanhar, analisar, comparar, registrar). As sequências são comparadas entre as pessoas e servem de base para modelar a T08 (HTA, GOMS e CTT), pendente desde a Entrega 5.
3. **Diagrama de afinidade:** as notas são agrupadas por semelhança e os grupos recebem um título. Os grupos são comparados com os dados da A03 e com as lacunas não previstas.
4. **Veredito por hipótese e lacuna:** H08 e as lacunas da T08 e da P02 (parâmetros ajustados, acompanhamento do treino, falhas, papel único ou separado, interface × scripts) recebem "sustentada", "refutada", "refinada" ou "sem evidência", com as notas que justificam. Com 1 a 3 pessoas, os resultados são relatos de caso, sem generalização.
5. **Consequência para o design:** cada veredito é ligado à decisão que afeta (escopo e parâmetros da T08, acompanhamento do treino, histórico na decisão 5 da P02, divisão da persona P02) e registrado na seção 5 do `RASTREABILIDADE.md`.
6. **Limitações:** ser observado muda o comportamento, e uma ou duas sessões podem não mostrar uma falha real. Por isso as falhas também são perguntadas (2.5), e os resultados são cruzados com a I01 (como as conclusões chegam a quem decide) e com a I02 (como as configurações chegam a quem analisa).

## Síntese

O usuário e a interface deste projeto foram propostos pela equipe a partir do TCC, e as três personas são proto-personas. Por isso, a coleta tem duas funções: verificar se o **cenário de uso faz sentido** (se cada perfil existe na Baja FEI e faz a atividade imaginada) e testar as hipóteses que sustentam as decisões de design já tomadas.

### Lacunas que o conjunto de técnicas pretende reduzir

| Lacuna | Instrumento | Por que essa técnica cobre a lacuna |
|---|---|---|
| Quem escolhe as configurações, quem recomenda e quem decide; como a decisão acontece e com que critério | I01 (blocos 2 a 5) e informantes secundários | Processo de poucas pessoas, que pede relato de uma ocorrência concreta e aprofundamento |
| Se quem analisa os resultados sabe programar, se sabe interpretar, quais ferramentas e termos conhece e em que contexto trabalha | I02 (seções 3 a 6) | Público maior e dados comparáveis entre pessoas |
| Como uma configuração é definida, treinada, acompanhada, analisada e registrada | I03 (sessões 1 e 2) | Conhecimento tácito, que a pessoa não descreve bem fora do trabalho |
| Se existe necessidade de histórico (H08) | I02 (7.3 e 7.4), I01 (5.3) e I03 (3.5) | Três fontes, porque perguntar sobre registros não basta: a I03 observa se a pessoa volta de fato a experimentos antigos |
| Se o piloto e quem acompanha os testes se beneficiam sem usar a interface (H03) | I02 (seção 8) | Perguntas curtas para um público que não é usuário |

**Plausibilidade das personas:**

- **P01 (Rafael):** a I02 confirma se existe quem analisa resultados de segmentação na equipe.
- **P03 (Larissa):** a I01 confirma se existe quem prepara a decisão sem executar os modelos e se essa pessoa usaria a interface ou só receberia um material.
- **P02 (Andreia):** a I03 confirma se quem treina os modelos é a coordenação, outro pesquisador ou ninguém fora dos autores.

Se um perfil não existir, a persona correspondente será revista antes da Entrega 8.

### O que deve ficar sustentado, refutado ou refinado

| Hipótese | Instrumentos | Fica **sustentada** se… | Fica **refutada** se… | Pode ser **refinada** se… |
|---|---|---|---|---|
| H01 — decisão com números dispersos e sem critério explícito | I01 (2.1, 3.1, 4.4); I02 (7.5, 7.6) | os relatos mostram resultados chegando por canais separados e escolha sem critério declarado | a equipe já usa um critério explícito e os resultados chegam reunidos | existe critério, mas só uma pessoa o conhece ou ele não é aplicado sempre |
| H02 — analista conhece o domínio, mas pode não dominar programação | I02 (2.2, 3.1–3.3, 6.1) | quem analisa programa pouco ou depende de ajuda para executar | quem analisa programa com frequência e resolve erros sozinho | programar e interpretar aparecem separados (programa bem, mas interpreta com dificuldade, ou o contrário) |
| H03 — piloto beneficiado sem usar a interface | I02 (seção 8) | quem acompanha os testes não consulta os resultados, mas o que faz muda por causa deles | os resultados não mudam nada no trabalho de quem acompanha os testes | parte dessas pessoas consulta os resultados e seria usuária ocasional |
| H04 — conhecimento técnico e familiaridade com métricas influenciam a interação | I01 (4.1–4.3); I02 (6.1–6.3); I03 (3.1) | o conhecimento de métricas e termos varia entre os perfis e muda o que cada um olha | todos os perfis leem as mesmas métricas do mesmo jeito | só alguns termos geram dúvida, o que define a lista de explicações no ponto de uso (RC01) |
| H05 — atividades feitas hoje por scripts que exigem conhecimento técnico | I02 (3.2–3.4); I03 (2.3) | executar depende de scripts e os erros exigem ajuda técnica | a execução já é simples e raramente falha | a dificuldade está em passos específicos (preparar arquivos, interpretar erros) e não na execução como um todo |
| H06 — dificuldade de interpretar resultados sem orientação | I01 (4.4); I02 (5.6–5.8) | quem decide não sabe julgar diferenças e quem analisa não separa falha do modelo de falha da imagem | ambos têm critério claro e o aplicam | a dificuldade aparece só em casos específicos (diferenças pequenas, sombra, poeira) |
| H07 — papéis e colaboração influenciam a interface | I01 (1.1, 2.2, S2.1); I03 (1.1, 3.6) | há papéis distintos de propor, recomendar e decidir | uma só pessoa faz tudo | os papéis existem, mas mudam conforme o ciclo de testes |
| H08 — necessidade de histórico | I01 (5.3); I02 (7.3, 7.4); I03 (3.5) | as pessoas voltam com frequência a análises ou experimentos antigos e têm dificuldade para encontrá-los | ninguém volta a resultados antigos, ou encontra sem esforço | a necessidade existe só para um perfil (por exemplo, quem treina) ou só para um tipo de informação |
| H09 — interfaces conhecidas (editor de código, terminal, GitHub, telemetria) | I02 (4.1) | a maioria usa essas ferramentas com frequência | quase ninguém as usa | o conjunto de ferramentas difere por curso ou papel |
| H10 — ferramentas como CVAT e Roboflow são complexas para o perfil | I02 (4.2, 4.3) | quem já usou relata dificuldade | quem já usou relata facilidade | a dificuldade depende da ferramenta, ou ninguém as conhece (hipótese irrelevante para o público) |
| H11 — padrões familiares (seleção de arquivo, progresso, lado a lado) | I02 (4.4) | esses recursos aparecem entre os que as pessoas já usam | não aparecem | só parte deles é familiar |
| H12 — benefício esperado: dispensar código, apresentar resultados com clareza, comparar | I01 (5.1, 6.1–6.3); I02 (7.8); I03 (4.2, 4.3) | as dificuldades relatadas coincidem com esses três benefícios | as dificuldades estão em outro lugar | os benefícios valem para um perfil e não para outro (por exemplo, quem treina prefere manter os scripts) |

### Depois da coleta

- Cada veredito é registrado na seção 2 (estado da hipótese) e na seção 5 (mudanças) do [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md), com o instrumento e os trechos que o justificam.
- Uma hipótese só muda de estado com evidência dos instrumentos. Respostas dos autores, do piloto e de participantes proxy são registradas à parte e não bastam sozinhas.
- Decisões de design que dependem das hipóteses (personas, tarefas T01–T08, decisões das personas e histórico) são revistas na Entrega 8, a partir desses vereditos.

## Checklist

- [X] Hipóteses/lacunas prioritárias da Entrega 1 foram revisitadas.
- [X] Se o escopo de IHC foi derivado de TCC técnico, a coleta investiga a plausibilidade do usuário, tarefa e contexto adotados.
- [X] Perguntas não pressupõem que dashboard, CRUD, filtros ou relatórios sejam necessários; investigam a necessidade.
- [X] Cada dado a coletar responde uma dúvida concreta do projeto ou justifica outra necessidade de informação.
- [X] Parte A identifica dados e perfis de coleta de forma específica.
- [X] Aspectos éticos são contextualizados para o projeto.
- [X] Há uma técnica completa por integrante e técnicas distintas.
- [X] Questionário está incluído entre as técnicas.
- [X] Cada instrumento possui objetivo, público, procedimento e conteúdo integral.
- [X] Perguntas evitam indução e coletam apenas dados necessários.
- [X] Está claro como os dados serão analisados e usados no design.
