# Entrega 7 — Coleta de dados, necessidades e aspectos éticos

**Data:** 11/11/2026 (início)  
**Status:** 🟨 em andamento

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

> Linhas preenchidas por Henrique (hipóteses ligadas à P03 e ao C02). Tiago e Mateus acrescentam as hipóteses das suas partes.

| ID | Hipótese/lacuna | Evidência atual | Decisão que depende da resposta | Prioridade |
|---|---|---|---|---|
| H07 | Existem fatores sociais ou organizacionais como papéis, permissões e colaboração na equipe. **Para a P03:** quem escolhe as configurações candidatas, quem recomenda e quem decide. | Nenhuma. O C02 descreve, como hipótese, que a gestora reúne e recomenda e que a palavra final é discutida com a coordenação. | Se a T05 (decidir e justificar) acontece na interface ou fora dela; se a P03 continua como persona própria ou se funde a outro papel; se é preciso registrar quem fez a recomendação. | alta |
| H01 | A decisão sobre qual modelo usar é tomada com base em números dispersos e sem critério explícito. | Só o cenário C02, construído pela equipe. Nenhum relato de quem decide. | Se o painel consolidado (decisão 1 da P03) e a referência de comparação (decisão 2) são necessários, ou se a equipe já tem um critério que só precisa ser apresentado. | alta |
| H04 | Conhecimento técnico, experiência com ferramentas e familiaridade com métricas influenciam a interação. **Para a P03:** quais métricas e termos quem decide entende. | As personas variam nesse eixo, mas são construção da equipe. A RC01 (termos) tem sustentação média. | Se a explicação dos termos no ponto de uso (decisão 3 da P03) vira requisito, e com qual vocabulário. | alta |
| H06 | Dificuldades principais: configurar parâmetros, selecionar arquivos, interpretar resultados sem orientação. **Para a P03:** julgar se uma diferença entre configurações é relevante. | Dores escritas pela equipe nas personas e no C02; nenhuma relatada por usuários. | De onde vem o valor de referência (decisão 2 da P03) e qual é o critério de resultado "inconclusivo" (decisão 5). | média |
| H12 | Benefício esperado: eliminar necessidade de código, apresentar resultados claramente, permitir comparação entre modelos. **Para a P03:** chegar à reunião com uma escolha que consiga sustentar. | Expectativa registrada na E1 §9.1, sem evidência. | O que conta como sucesso nas metas de usabilidade (Entrega 8) para a tarefa de decisão; se o resumo exportável (decisão 4 da P03) é o que de fato se leva à reunião. | média |

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

> Repita A02, A03...

## Parte B — ferramentas de coleta

> Cada integrante deve preparar uma técnica/instrumento completo. As técnicas devem ser diferentes entre si e **questionário deve estar entre as técnicas escolhidas**, conforme o enunciado da disciplina.

### Instrumento I01 — {{nome da técnica}}

**Autor(a):** {{nome — matrícula}}  
**Técnica:** questionário / entrevista semiestruturada / observação / grupo focal / outra autorizada  
**Objetivo:** {{...}}  
**Público:** {{...}}

#### Procedimento padronizado de aplicação

1. {{preparação}}
2. {{apresentação/consentimento}}
3. {{aplicação}}
4. {{encerramento}}
5. {{armazenamento/anonimização}}

#### Instrumento

Cole aqui o questionário/roteiro completo ou forneça link **mais uma cópia textual no repositório**.

#### Como os dados serão analisados

{{ex.: distribuição de respostas, codificação temática, agrupamento de problemas}}

## Síntese

Explique quais lacunas de conhecimento sobre usuários o conjunto de técnicas pretende reduzir. Indique explicitamente quais hipóteses da Entrega 1 deverão ficar **sustentadas, refutadas ou refinadas** após a análise dos dados. Quando os dados forem coletados/analisados, atualize o histórico em `RASTREABILIDADE.md`.

## Checklist

- [ ] Hipóteses/lacunas prioritárias da Entrega 1 foram revisitadas.
- [ ] Se o escopo de IHC foi derivado de TCC técnico, a coleta investiga a plausibilidade do usuário, tarefa e contexto adotados.
- [ ] Perguntas não pressupõem que dashboard, CRUD, filtros ou relatórios sejam necessários; investigam a necessidade.
- [ ] Cada dado a coletar responde uma dúvida concreta do projeto ou justifica outra necessidade de informação.
- [ ] Parte A identifica dados e perfis de coleta de forma específica.
- [ ] Aspectos éticos são contextualizados para o projeto.
- [ ] Há uma técnica completa por integrante e técnicas distintas.
- [ ] Questionário está incluído entre as técnicas.
- [ ] Cada instrumento possui objetivo, público, procedimento e conteúdo integral.
- [ ] Perguntas evitam indução e coletam apenas dados necessários.
- [ ] Está claro como os dados serão analisados e usados no design.
