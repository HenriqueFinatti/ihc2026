# Feedback do Professor > Entrega 11 > Grupo 17

A equipe apresentou uma interface implementada de alta fidelidade, alternativa válida ao Figma, com boa cobertura das tarefas centrais do projeto de segmentação semântica *off-road*. A entrega demonstra maturidade: há 44 capturas organizadas em 11 grupos de telas, documentação do fluxo, estados normais e excepcionais, vocabulário coerente e uma relação explícita entre os MoLIC M01, M02 e M03 e as telas TL01 a TL10.

O material permite compreender como o usuário configura e acompanha um treino, envia imagens e vídeos, acompanha o processamento, inspeciona resultados, compara configurações, registra conclusões e apresenta uma recomendação. A interface também comunica limites importantes, como a ausência de métricas para imagens de campo sem anotação de referência. Isso evita que a aplicação sugira uma precisão que não pode calcular.

Os principais pontos de revisão estão na coerência entre a modelagem e a solução implementada. A TL11 - Datasets oferece atividades necessárias ao funcionamento do produto, mas foi criada fora dos MoLIC. Além disso, a própria documentação reconhece capturas desatualizadas e diferenças de comportamento entre componentes equivalentes. Essas diferenças não anulam a entrega, porém precisam ser corrigidas antes das avaliações, pois uma evidência visual deve representar exatamente a versão que será inspecionada e testada.

## Pontos positivos

- A equipe escolheu adequadamente o caminho de apresentar uma interface implementada e documentou a versão exata do código, as instruções de execução e as limitações do ambiente local.
- As 44 capturas estão preservadas no projeto e organizadas por tela, de TL01 a TL11. Elas incluem estados de vazio, processamento, conclusão, falha, confirmação, prevenção e recuperação.
- A seção “Cobertura MoLIC → telas” é clara e útil. Ela relaciona objetivos, telas, rupturas e responsáveis, permitindo verificar a passagem do modelo de interação para a interface.
- As telas empregam signos definidos anteriormente, como configuração, ciclo de testes, conjunto de teste, IoU, acurácia, tempo de inferência, valor de referência, avaliação e recomendação.
- A TL05 comunica corretamente que imagens de campo sem anotação de referência exigem avaliação visual e não produzem IoU ou acurácia.
- A interface distingue o maior valor numérico de uma recomendação. A decisão continua com a pessoa, o que é consistente com o recorte do projeto e evita automatizar um julgamento que depende do contexto.
- A TL10 oferece explicações no ponto de uso e informa tanto o que um termo indica quanto o que ele não indica. Essa solução é especialmente adequada para métricas técnicas.
- O sistema visual é consistente entre as telas: navegação fixa, hierarquia clara, estados combinando cor, ícone e texto, diálogos de recuperação e ações com rótulos objetivos.
- A entrega explica decisões novas e diferenças em relação aos modelos anteriores, e essas decisões foram registradas no `RASTREABILIDADE.md`.
- A documentação de acessibilidade apresenta verificações concretas de contraste, foco, teclado, tamanho de alvo e alternativas textuais. A confirmação prática com usuários e tecnologias assistivas foi corretamente reservada para as avaliações posteriores.

## Correções prioritárias

### 1. A atividade da TL11 precisa entrar na modelagem de interação

A TL11 - Datasets não é apenas uma tela técnica de apoio. Nela, uma pessoa verifica dados, monta ou remonta o conjunto, escolhe configurações e inicia a avaliação no conjunto de teste. Essas ações possuem objetivo, decisões, consequências e uma confirmação antes de substituir dados. A própria entrega afirma que, sem essa tela, não é possível treinar nem calcular as métricas.

Por isso, não é suficiente declarar que a TL11 está “fora dos MoLIC”. Se a interação é necessária e faz parte do produto apresentado, ela deve ter origem em um objetivo e em uma conversa de interação. A equipe precisa revisar o mapa de objetivos, o cenário correspondente, o Design Centrado na Comunicação e o MoLIC responsável por preparar os dados e avaliar as configurações. Depois, deve atualizar a cobertura da Entrega 11. Caso alguma parte seja realmente uma tarefa administrativa fora do recorte, a equipe deve delimitar quem a executa e por que ela não pertence às tarefas avaliadas.

### 2. As capturas devem representar a versão atual da interface

A equipe registrou que algumas capturas não correspondem ao estado atual: o eixo repetido no gráfico da TL02, a quantidade de imagens na TL06 e o enquadramento da TL07 E3. O documento também informa diferenças que ainda permanecem na interface ou nas evidências, como o seletor de arquivos em inglês e uma contagem de imagens que não corresponde à sessão mostrada.

Uma legenda explicando que a tela já mudou não substitui a evidência atualizada. Isso prejudica a inspeção e pode produzir resultados diferentes nas Entregas 13 e 14. A equipe deve refazer as capturas afetadas depois de consolidar a versão que será avaliada, mantendo no repositório somente evidências que correspondam a essa versão.

### 3. Componentes equivalentes precisam adotar o mesmo comportamento preventivo

Na TL01, a prevenção informa que é obrigatório selecionar ao menos um dataset, mas o botão “Continuar” permanece ativo. Na TL09, uma condição obrigatória desabilita a ação. A entrega reconhece essa diferença e registra que a equipe decidiu mantê-la.

Essa decisão enfraquece a consistência da interface. Se a condição impede legitimamente a continuidade, o sistema deve aplicar a mesma lógica preventiva e deixar claro o que precisa ser resolvido. A equipe deve unificar o comportamento ou justificar uma diferença baseada na tarefa do usuário, e não apenas registrar que os componentes se comportam de maneiras distintas.

### 4. A acessibilidade declarada precisa ser confirmada por percursos completos

A análise de contraste e a inspeção do código são boas evidências iniciais, mas ainda não demonstram que uma pessoa consegue concluir os fluxos somente com teclado, ampliação ou leitor de tela. Esse limite está corretamente reconhecido no documento.

Nas próximas avaliações, a equipe deve percorrer as tarefas críticas completas: configurar e iniciar um treino, enviar entradas, recuperar-se de um formato inválido, comparar configurações, registrar uma conclusão e apresentar uma recomendação. O foco precisa permanecer visível e seguir ordem lógica; mensagens e diálogos devem ser anunciados; gráficos e comparações devem continuar compreensíveis sem depender apenas de cor ou posição visual.

## Recomendações de melhoria

- Remover o arquivo `f01.svg`, pois ele contém apenas um marcador de artefato e não contribui para a evidência desta entrega.
- Corrigir a tradução do seletor de arquivos ou empregar um controle visual em português que preserve a operação acessível do campo nativo.
- Acrescentar, para cada fluxo crítico, uma sequência curta de capturas numeradas. O catálogo atual é completo, mas a ordem de navegação poderia ficar mais evidente para quem não conhece os MoLIC.
- Manter nas capturas uma identificação discreta da versão ou do commit. Isso facilita comprovar que documentação, interface e avaliação usam a mesma versão.
- Rever a afirmação de que todos os fluxos críticos estão prontos “sem links mortos” depois da atualização das telas e antes do início dos testes com participantes.
- Preservar a explicação de que os valores das métricas nas capturas são ilustrativos. Essa observação evita confundir evidência da interface com resultado técnico do TCC.

## Pontos que devem alimentar as próximas entregas

- Na avaliação heurística, verificar especialmente a consistência das ações preventivas, a localização do usuário no fluxo, a recuperação após falha e a clareza das diferenças entre “em uso”, “candidata”, “avaliada” e “sem avaliação”.
- No teste com usuários, observar se os perfis compreendem a diferença entre desempenho no conjunto de teste e avaliação visual de imagens de campo.
- Verificar se “valor de referência” entendido como resultado da última configuração executada corresponde à expectativa dos usuários. A regra foi definida na implementação e ainda precisa de evidência de uso.
- Avaliar se a tela Datasets será operada pelo mesmo perfil que treina os modelos. Essa decisão deve orientar a revisão do cenário e do MoLIC.
- Testar se os usuários percebem que o destaque “maior valor” não equivale a uma recomendação automática.
- Conferir com teclado, leitor de tela e ampliação os diálogos, o painel de termos, o visualizador de imagens e os gráficos acompanhados de tabelas.

## Síntese das ações recomendadas

1. Incorporar a preparação dos datasets e a avaliação no conjunto de teste ao modelo de objetivos, ao cenário, ao Design Centrado na Comunicação e ao MoLIC pertinente.
2. Corrigir as inconsistências registradas e refazer todas as capturas que não representam a versão atual.
3. Uniformizar o comportamento das prevenções obrigatórias, especialmente entre TL01 e TL09.
4. Consolidar uma versão única da interface para as Entregas 13 e 14 e identificá-la por commit.
5. Validar os fluxos completos com teclado e, quando possível, com leitor de tela e ampliação.

## Parecer geral sobre a entrega

De forma geral, a Entrega 11 está bem desenvolvida e demonstra uma evolução consistente das modelagens anteriores para uma interface funcional, extensa e cuidadosamente documentada. A equipe não se limitou a apresentar telas principais: trabalhou estados de erro, recuperação, vazio, comparação, explicação e confirmação, o que fortalece bastante a qualidade do protótipo. Para consolidar esse bom resultado, é necessário incorporar a atividade da TL11 à modelagem e substituir evidências desatualizadas pela versão efetivamente avaliada. Com essas correções, o projeto estará em condições muito melhores para produzir resultados confiáveis nas avaliações seguintes.
