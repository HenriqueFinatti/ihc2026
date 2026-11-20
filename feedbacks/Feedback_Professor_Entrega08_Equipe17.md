# Feedback do Professor > Entrega 08 > Equipe 17

A equipe construiu uma entrega extensa e, em vários pontos, bem conectada ao projeto. As características da plataforma apresentam capacidades e restrições com consequências para a interface. As metas qualitativas e quantitativas estão ligadas às personas, tarefas e formas de verificação. Também houve uma boa tentativa de separar a avaliação da interação do desempenho técnico dos modelos de segmentação.

Entretanto, três partes centrais não seguiram a estrutura trabalhada na disciplina. Os princípios gerais não foram separados entre princípios de negócio e princípios de interface; a priorização não utiliza as cinco metas de Nielsen; e a seção sobre iteração não descreve o Ciclo de Vida de Engenharia de Usabilidade. Além disso, decisões tomadas nas Entregas 9, 11 e 12 deixaram alguns trechos da Entrega 8 desatualizados. A equipe já registrou parte dessas divergências em `PENDENCIAS.md`, mas ainda precisa corrigi-las no documento avaliado.

## Pontos positivos

- A delimitação distingue contribuição técnica do TCC, camada de interação e elementos utilizados no protótipo. Essa separação ajuda a não confundir IoU, acurácia ou tempo de inferência com qualidade de uso da interface.
- A seção de plataforma apresenta capacidades concretas, como selecionar entradas, executar a segmentação, visualizar máscaras, consultar métricas, comparar configurações e acompanhar o treino. Também apresenta restrições relevantes, como processamento local, ausência de métricas para imagens de campo, dependência dos recursos do computador e impossibilidade de concluir que um trajeto é seguro.
- As consequências para IHC são descritas com boa especificidade: estados de processamento, mensagens de erro compreensíveis, indicação da configuração e da entrada, legenda consistente e retomada após interrupções.
- As metas qualitativas MQ01 a MQ07 se relacionam com tarefas e comportamentos observáveis. A equipe não se limita a escrever “a interface deve ser fácil”; descreve o que o participante deveria compreender, fazer ou explicar.
- As metas quantitativas apresentam métrica, tarefa, limite e forma de medição. MU01 a MU11 cobrem eficácia, eficiência, erros, compreensão e satisfação. Os tempos são corretamente tratados como hipóteses a recalibrar no piloto.
- A equipe reconhece que as personas ainda dependem de evidências e que algumas decisões devem ser revistas após a coleta. Essa postura é coerente com um projeto iterativo.

## Correções prioritárias

### 1. Refazer a priorização com as cinco metas de Nielsen

A seção 3.3 distribui pesos entre MU01 a MU11. Essa organização prioriza indicadores particulares do teste, mas não atende ao que foi solicitado na aula e na videoaula. A priorização deveria conter somente as cinco metas de Nielsen: facilidade de aprendizado, facilidade de memorização, eficiência, baixa taxa de erros e satisfação positiva do usuário.

A equipe precisa distribuir a prioridade entre essas cinco metas e justificar cada peso com base no projeto. Depois, as metas MQ e MU podem ser relacionadas a elas. Por exemplo, pedidos de ajuda e conclusão na primeira tentativa podem contribuir para facilidade de aprendizado; erros críticos e recuperação podem contribuir para baixa taxa de erros. Os indicadores continuam úteis, mas não substituem as categorias que deveriam ser priorizadas.

A estrutura atual indica que a orientação específica da videoaula não foi aplicada. Não assistir às videoaulas, ou não retomar seu conteúdo ao preencher o modelo, não é uma prática recomendada, especialmente quando a atividade depende de uma classificação apresentada em aula.

### 2. Separar os princípios de negócio dos princípios de interface

A seção 2 reúne ISO 9241-11, LGPD, WCAG, consistência terminológica e diretrizes para interação humano-IA em uma única lista. O conteúdo possui bons elementos, mas os dois grupos obrigatórios não aparecem.

A equipe deve criar uma parte para princípios direcionados ao negócio e outra para princípios direcionados à interface. No primeiro grupo, expliquem as regras que condicionam o uso e o tratamento dos dados no contexto do projeto, como limites da finalidade da segmentação, responsabilidade humana pela escolha e proteção das imagens dos testes. No segundo, coloquem as orientações que guiam a construção da interação, como WCAG, consistência de termos, feedback dos estados, padrões de apresentação e diretrizes de interação humano-IA.

Essa separação não deve ser apenas visual. Cada princípio precisa mostrar qual decisão concreta produz e por que pertence ao respectivo grupo. A ISO 9241-11 pode fundamentar as metas de usabilidade, mas não substitui a explicitação das regras do negócio nem das diretrizes da interface.

### 3. Descrever o Ciclo de Vida de Engenharia de Usabilidade

A seção 4 afirma que o projeto segue design centrado no ser humano e lista quais artefatos podem mudar depois de cada entrega. Isso demonstra intenção de iterar, mas não descreve um dos modelos apresentados no material teórico, nem explica como o Ciclo de Vida de Engenharia de Usabilidade organiza o trabalho.

A equipe deve adotar e descrever esse ciclo, conforme a recomendação da videoaula. É necessário relacionar o projeto às etapas de análise de requisitos, definição de metas de usabilidade, projeto essencial, padrões de telas e diálogos, prototipação, testes e refinamento. A explicação precisa mostrar como os resultados de uma avaliação retornam às decisões anteriores e como cada grupo de funcionalidades percorre novamente o ciclo.

A lista atual de entregas pode ser preservada como aplicação prática do ciclo, desde que primeiro fique claro qual modelo está sendo usado e como suas etapas se conectam aos artefatos do projeto.

### 4. Atualizar a Entrega 8 depois das decisões das Entregas 9, 11 e 12

A seção de delimitação afirma que IoU, acurácia, tempo de inferência e processamento são simulados. A Entrega 12, porém, registra que a avaliação utiliza a interface implementada e uma cópia completa dos dados do TCC, sem simulação. A própria equipe registrou essa divergência como INC-71. O documento precisa refletir o estado atual do projeto.

MQ04 e MU05 incluem uma falha simulada, mas o plano da Entrega 12 informa que essa falha não será provocada no teste com usuários e ficará restrita à inspeção. Atualizem o método de verificação e retirem qualquer promessa de medição que não será executada.

MQ03 e a linha “Consistência de termos e referências” ainda mencionam aviso de diferença pequena ou resultado inconclusivo. A rastreabilidade informa que esse aviso automático foi retirado em 14/11 e que a pessoa continuará responsável por julgar a relevância da diferença. A meta deve avaliar se o usuário interpreta os valores e justifica sua conclusão, sem depender de um aviso que não faz mais parte da interface.

Há também uma inconsistência de enquadramento: a captura por câmera do veículo aparece entre integrações ou dispositivos, embora a integração com o hardware do veículo esteja declarada fora do recorte. Expliquem que a câmera produz os arquivos usados posteriormente, sem sugerir captura direta pela interface.

### 5. Rever a composição da amostra e a leitura dos resultados

As metas MU01 a MU03 e MU11 adotam “2 de 3 participantes”, mas as tarefas são associadas a personas diferentes. A equipe precisa esclarecer se os três participantes executarão todas as tarefas e se cada um realmente representa o perfil necessário. Um participante que apenas acompanha testes não deve ser contado como evidência equivalente para uma tarefa de configuração de treino.

Com três participantes, a mediana de uma escala ou de tempo pode ser calculada, mas deve ser interpretada como resultado desses casos, sem pretensão de generalização. Para cada meta, indiquem qual perfil poderá produzir evidência válida e como será tratada uma amostra que não contenha três representantes do mesmo perfil.

## Recomendações de melhoria

- Revisem a delimitação para explicar com precisão o que é interface, dado real, processamento real e elemento preparado para o teste. “Métricas simuladas” e “limite do protótipo por memória da GPU” são questões diferentes.
- Substituam referências desatualizadas como “conjunto de teste anotado” quando a terminologia consolidada do projeto passou a utilizar “conjunto de teste”, explicando em linguagem acessível que ele possui referência.
- Incluam a fonte do valor de referência do SUS e tratem o limite de 68 como critério adotado pela equipe, evitando apresentá-lo como uma fronteira universal entre interface boa e ruim.
- Na facilidade de memorização de Nielsen, definam como ela poderá ser avaliada. Uma tarefa executada apenas uma vez mede mais diretamente aprendizado inicial do que memorização após um intervalo.
- Corrijam pequenos problemas de redação e grafia, como “segementação”, “quantitaivas”, “véiculo” e “disponiveis”.

## Pontos que devem alimentar as próximas entregas

- A Entrega 12 deve usar apenas metas que possuam método, tarefa e participante compatíveis. O que for avaliado somente por inspeção precisa estar identificado dessa forma.
- A avaliação heurística deve verificar as decisões de acessibilidade, consistência, feedback, prevenção de erros e controle humano descritas nos princípios de interface.
- A observação com usuários deve comparar os resultados com metas revisadas, respeitando os perfis das personas e os limites da amostra.
- As mudanças decorrentes dos testes devem retornar ao modelo conceitual, ao MoLIC e às telas quando o problema tiver origem nesses artefatos, seguindo o ciclo escolhido.
- A rastreabilidade deve registrar a correção da INC-71 e a retirada das referências ao aviso automático de resultado inconclusivo.

## Síntese das ações recomendadas

1. Substituir a priorização das onze MU pela priorização das cinco metas de Nielsen.
2. Organizar os princípios em negócio e interface, com decisões decorrentes de cada grupo.
3. Descrever e aplicar o Ciclo de Vida de Engenharia de Usabilidade.
4. Atualizar simulação, falha, aviso de resultado inconclusivo e integração com câmera conforme as decisões atuais.
5. Ajustar participantes e critérios de cada meta ao perfil que realmente executa a tarefa.

**Parecer geral:** A Entrega 8 demonstra esforço de integração e apresenta uma base consistente de plataforma e metas verificáveis. A equipe compreendeu que usabilidade precisa ser observada em tarefas e contextos concretos, o que é um avanço importante. Entretanto, a priorização, a organização dos princípios e a escolha do ciclo são componentes centrais da atividade e precisam ser refeitos conforme a teoria trabalhada. Depois dessas correções e da atualização das inconsistências já reconhecidas pela própria equipe, o documento poderá orientar com mais segurança as avaliações e as próximas revisões da interface.

## Tratamento dos comentários

*Registro da equipe, 20/11/2026. Cada item foi conferido contra o estado atual de `docs/08_engenharia_usabilidade.md` e das Entregas 9, 11 e 12 antes de qualquer alteração. A E8 não tinha mudado desde 16/11/2026, e todos os pontos do parecer continuavam válidos; os itens 4 e 5 já estavam registrados como INC-71 e INC-72. A estrutura das §2 a §4 segue as aulas de Processos de Projeto de IHC e de Qualidade de Uso (Barbosa e Silva, 2010).*

| Item do parecer | Situação em 20/11/2026 | O que foi feito |
|---|---|---|
| 1. Priorização com as cinco metas de Nielsen | Não atendido | §3.3 refeita: pesos para facilidade de aprendizado (30%), baixa taxa de erros (30%), facilidade de memorização (15%), satisfação (15%) e eficiência (10%), justificados pelo uso esporádico, pelo custo de um erro de leitura e pela duração dominada pelo processamento. Uma segunda tabela liga as metas MQ e MU a cada meta de Nielsen e diz como cada uma é verificada |
| 2. Princípios de negócio × interface | Não atendido | §2 dividida em 2.1 (negócio: finalidade da segmentação, responsabilidade humana pela escolha, proteção das imagens, uso interno e local, validade das métricas) e 2.2 (interface: WCAG 2.2 AA, consistência de termos, visibilidade do estado, padrões de apresentação, interação humano-IA), com a decisão que cada um produz e por que pertence ao grupo. A ISO 9241-11 passa a fundamentar as metas, fora dos dois grupos |
| 3. Ciclo de Vida de Engenharia de Usabilidade | Não atendido | §4 descreve o ciclo de Mayhew (análise de requisitos; níveis 1 a 3 de projeto, avaliação e desenvolvimento; instalação) e liga cada etapa a uma entrega. Grupos de funcionalidades G1 (P01), G2 (P03) e G3 (P02) percorrem de novo os níveis; os resultados das Entregas 13 e 14 voltam à etapa de origem. A tabela anterior foi mantida como aplicação prática, atualizada |
| 4. Atualizar depois das Entregas 9, 11 e 12 | Não atendido (registrado como INC-71) | Delimitação reescrita: nada é simulado, com dado real, processamento real e estado preparado para o teste separados; a câmera produz os arquivos e não se conecta à interface; o limite de memória passa a restrição da plataforma. MQ04 e MU05: falha só na inspeção (QA09). MQ03 e consistência de termos sem o aviso automático de resultado inconclusivo. §1 atualizada com as decisões da E10 e da E11 |
| 5. Composição da amostra | Não atendido (registrado como INC-72) | Cada meta diz o perfil e o participante que a verificam (U01 = P01, U02 = P02, U03 = P03), com critério por participante, leitura caso a caso, sem medianas, e participante aproximado como limitação. MU11 com a UT04, sem a falta de memória. MU06, MU07, MU09 e MU10 retiradas, como decidido na E12 |
| Recomendações | Atendido, exceto o SUS | Delimitação precisa (interface, dado real, processamento real, preparado para o teste); "conjunto de teste anotado" passa a "conjunto de teste", explicado; forma de avaliar a memorização descrita (segunda sessão após um intervalo), sem verificação nesta disciplina; grafia corrigida (segmentação, quantitativas, veículo, disponíveis). A recomendação sobre o SUS deixou de se aplicar: a MU10 foi retirada por decisão da equipe na E12 |
