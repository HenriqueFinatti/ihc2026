# Entrega 2 — Análise C02: Roboflow

**Autor(a):** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3
**Produto analisado:** Roboflow
**Módulo/versão analisada:** plataforma web Roboflow; módulo **"Test Your Model"** (fluxo de teste de modelo por upload de imagem ou webcam) e o recurso de **seleção de modelo por assistente conversacional** (Roboflow Universe). O módulo conversacional é um recorte específico da plataforma e **não deve ser confundido** com o restante do produto.
**Link oficial:** https://roboflow.com/
**Data de acesso:** 27/08/2026 (navegação e captura de tela); 28/09/2026 (fontes públicas de opinião)

## Entrada obrigatória da Entrega 1

| Item citado na Entrega 1 | Tipo | Por que foi citado | Status inicial | Decisão nesta entrega |
|---|---|---|---|---|
| Roboflow | Análogo | É uma ferramenta que permite enviar imagens e selecionar modelos | F | Manter como análogo de referência — **não é concorrente direto**, pois cobre o ciclo completo (anotação, treinamento e implantação), enquanto o nosso recorte é a etapa de *segmentação e interpretação do resultado* |

## 1. Público-alvo desta análise

O público-alvo do Roboflow são equipes de visão computacional, desenvolvedores de IA e pesquisadores de aprendizado de máquina que precisam levar imagens do estado bruto até um modelo implantado, sem construir a infraestrutura do zero.

Perfil típico: equipes pequenas e médias sem MLOps dedicado, desenvolvedores que querem iterar rápido e empresas de setores como varejo, manufatura, segurança e saúde.

**Relação com o nosso público-alvo:** o nosso público prioritário é o *analista de segmentação da equipe Baja FEI* (ver [`../01_conhecendo_o_problema.md`](../01_conhecendo_o_problema.md), seção 7.2). O Roboflow é avaliado publicamente como acessível a quem não é especialista, o que o torna um **análogo mais próximo** do nosso perfil do que o CVAT. Ainda assim, não temos evidência de que integrantes do Baja FEI utilizem esta plataforma.

> `[?]` A familiaridade do nosso público com o Roboflow permanece como hipótese (**H09**).

## 2. Concorrentes diretos/indiretos

### Análise C02 — Roboflow

**Classificação:** análogo indireto. Cobre o ciclo completo de visão computacional; a etapa de **segmentação e interpretação do resultado** aparece diluída em um fluxo maior de treinamento e implantação.

#### Contexto e proposta

O Roboflow funciona como um ecossistema completo para projetos de visão computacional, cobrindo o ciclo de vida de um modelo de IA desde a imagem bruta até a aplicação final. A proposta central é ser *low code*, permitindo que empresas criem soluções de IA rapidamente sem construir toda a infraestrutura do zero.

No contexto do nosso TCC, o Roboflow é relevante porque o nosso usuário **precisa executar a segmentação e confiar ou desconfiar do resultado**. O módulo "Test Your Model" é o ponto de contato mais próximo com essa atividade — é a tela de envio de imagem e webcam, o que coincide com a nossa ação de entrada de dados.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência | O que a evidência sustenta (e o que não sustenta) | Observação de IHC |
|---|---|---|---|---|
| Entrada de imagens para teste de modelo | Botão de upload posicionado no canto superior esquerdo, ao lado de uma prévia do resultado | [`roboflow_input_imagens.png`](../../assets/02_concorrencia/roboflow_input_imagens.png) | Sustenta: existe um **ponto de entrada de imagens com ícone de upload** e a possibilidade de usar webcam, em um contexto de projeto de trilha off-road. **Não** sustenta: o recorte tem 341 × 192 px e mostra apenas parte da tela — **não permite avaliar o fluxo completo nem o resultado do processamento**. | O upload como **ação primária e visível** é um bom padrão para o nosso usuário, que não tem familiaridade com linha de comando. |
| Seleção de modelo por assistente conversacional | Resposta em formato de conversa, com opções de modelos e justificativas resumidas para trilhas | [`roboflow_selecionar_modelos.png`](../../assets/02_concorrencia/roboflow_selecionar_modelos.png) | Sustenta: o produto **apresenta sugestões de modelo em formato conversacional**, com justificativas. **Não** sustenta: a troca do modelo foi executada, o treinamento foi concluído, o desempenho foi obtido, nem que é difícil desfazer alterações. | Oferece acesso rápido à escolha de modelo, mas depende de o usuário **descobrir** que existe um chat. Para o nosso perfil, uma lista explícita é mais previsível. |

**Legendas das imagens**

- **Figura E3 — `roboflow_input_imagens.png`.** Recorte do módulo "Test Your Model", com as opções de envio de arquivo e uso de webcam, no contexto do projeto "Off-Road Trail Segmentation". *Fonte: captura de tela da equipe, em projeto de demonstração do produto, 27/08/2026. Recorte parcial (341 × 192 px) — registrado aqui como limitação da evidência, não como falha do produto.*
- **Figura E4 — `roboflow_selecionar_modelos.png`.** Resposta do assistente conversacional apresentando opções de modelos com justificativas resumidas para uso em trilhas. *Fonte: captura de tela da equipe, 27/08/2026.*

#### Experiência do usuário e opiniões

As afirmações abaixo são **opiniões de terceiros**, com fonte registrada.

| Opinião | Fonte | O que sugere para o nosso projeto |
|---|---|---|
| O Roboflow é bem avaliado quanto a facilidade de uso e é descrito como acessível a usuários não especialistas; nota agregada ~4,7–4,8/5 em 146–161 avaliações | G2 — https://www.g2.com/products/roboflow/reviews (acesso 28/09/2026; números republicados por Oryndex, Toolradar e SearchTools) | É o **análogo mais próximo do nosso perfil de usuário** entre os três produtos. Apoia a plausibilidade de que uma interface sem código é compreensível para o analista do Baja. |
| Usuários elogiam a **versionação de datasets**, que permite reverter a um conjunto de anotações anterior | SearchTools.ai — https://searchtools.ai/t/roboflow (acesso 28/09/2026), reunindo avaliações do G2 | Dá origem observável a parte de **RC02 (histórico/versionamento)** no Roboflow, e não no Supervisely. |
| Pre-roteulagem assistida por IA é apontada como o principal diferencial | G2 — alguns usuários relatam que a rotulagem pré-anotada por modelos reduzem bastante o trabalho manual | Confirma que o usuário **não precisa executar** a tarefa manualmente — princípio alinhado ao nosso objetivo de remover o script do fluxo. |
| Há relatos de **lentidão no carregamento de imagens** e de instabilidade da interface de anotação com conjuntos grandes (acima de alguns milhares de imagens) | SearchTools.ai (reunindo avaliações do G2); AppCritica — https://www.appcritica.com/review/roboflow/ | Alerta de desempenho. Se o nosso usuário carregar vídeos longos ou lotes grandes, o feedback de espera precisa ser bem desenhado. |
| Abstrações pesadas "podem esconder os fundamentos" para quem está aprendendo | AppCritica | Alerta: uma interface que esconde o modelo pode tanto ajudar (usuário técnico) quanto atrapalhar (quem precisa entender o resultado). Relevante para a escolha de nível de transparência. |
| Política de dados públicos por padrão no plano gratuito e cobrança baseada em créditos são queixas recorrentes | Oryndex — https://oryndex.co/tools/roboflow | Questão de **modelo de negócio**, não de tela. Para o nosso recorte, o produto é gratuito e local, o que evita esse custo de entrada. |

> **Ressalva de verificação:** assim como na análise do CVAT, as citações vêm do G2 e de fontes secundárias. A equipe deve confirmar a formulação exata na página primária antes da entrega.

#### Padrões e tendências percebidos

- **Plataforma integrada de ponta a ponta:** dataset → anotação → treinamento → avaliação → implantação, em um só ambiente.
- **Baixo código como proposta central:** a messaging é "não construa a infraestrutura do zero".
- **Versionamento de datasets** como recurso de primeira classe, permitindo reverter anotações.
- **Monetização por créditos de treinamento**, com salto de preço entre o plano gratuito e os pagos — o que torna o custo um ponto sensível para equipes pequenas.
- Para o nosso perfil, o padrão relevante é a **previsibilidade**: o usuário deve ver, sem esforço, o que será enviado, o que está sendo processado e o que será devolvido.

#### Modelo de negócio

- **Freemium com cobrança por consumo.** Plano gratuito limitado, com datasets e modelos públicos por padrão; planos pagos para uso privado, cobrança baseada em créditos de treinamento e limites de API na inferência hospedada.
- Receptor típico: equipes de desenvolvedores e pequenas empresas que precisam chegar rápido a um modelo implantado.
- **Implicação para o nosso projeto:** o nosso recorte é local, gratuito e de escopo restrito (executar modelos já disponíveis). Não há dependência de créditos, e isso é um diferencial de adoptabilidade frente ao Roboflow.

> `[?]` As faixas de preço divergem entre as fontes consultadas (Starter em torno de US$ 79/mês ou US$ 249/mês, dependendo da fonte e do plano). Os valores **não foram confirmados** e devem ser verificados em https://roboflow.com/pricing antes da entrega. Registramos a divergência em vez de escolher um valor.

#### Pontos positivos, limitações e lições

| Ponto | Tipo | Evidência | Implicação para o nosso projeto |
|---|---|---|---|
| Upload como ação primária, com ícone visível | Padrão observado (positivo) | [Figura E3](../../assets/02_concorrencia/roboflow_input_imagens.png) | O nosso usuário precisa de uma entrada de dados óbvia e em linguagem simples. |
| Seleção de modelo acessível, com justificativas por trilha | Padrão observado (positivo, com ressalva) | [Figura E4](../../assets/02_concorrencia/roboflow_selecionar_modelos.png) | **Oferecer a escolha de modelo com justificativa**, mas em lista explícita, e não apenas por descoberta conversacional. |
| Versionamento de datasets e capacidade de reverter anotações | Padrão observado (positivo, com fonte pública) | SearchTools.ai / G2 | É a origem mais clara para **RC02**. Aplicável apenas se o nosso recorte incluir recuperação de análises anteriores. |
| Acerto de métricas de desempenho do modelo com filtros e visualizações | Relato de usuário | G2 — "the evaluation graphs show how well the model is performing" | Requisito confirmado: o nosso usuário precisa de métricas do modelo, e não apenas do trabalho de anotação. |
| Seleção de modelo depende de o usuário descobrir o chat | Limitação (auto-observação da equipe) | [Figura E4](../../assets/02_concorrencia/roboflow_selecionar_modelos.png) | Uma **lista explícita** reduz dependência de descoberta. Decisão de projeto: adotar lista, não chat. |
| Evidência visual é insuficiente para avaliar o fluxo completo | Limite de interpretação | [Figura E3](../../assets/02_concorrencia/roboflow_input_imagens.png) | A equipe deve ampliar esta captura (sem recorte) antes de citar o fluxo. |
| Lentidão em conjuntos grandes | Limitação (com fonte pública) | SearchTools.ai; AppCritica | Feedback de progresso e tolerância a espera precisam ser tratados como requisito. |
| Versionamento só se aplica se o recorte incluir histórico | Limite de escopo | seção 2.1 — rastreabilidade | Não assumir treinamento nem versionamento de modelos: nosso recorte é **executar** modelos disponíveis, não treiná-los. |

## Referências desta análise

- Roboflow (site oficial). https://roboflow.com/ — acesso 27/08/2026.
- G2 — Roboflow Reviews. https://www.g2.com/products/roboflow/reviews — acesso 28/09/2026.
- Oryndex — Roboflow. https://oryndex.co/tools/roboflow — acesso 28/09/2026. Fonte secundária.
- SearchTools.ai — Roboflow AI App. https://searchtools.ai/t/roboflow — acesso 28/09/2026. Fonte secundária.
- AppCritica — Roboflow Reviews 2026. https://www.appcritica.com/review/roboflow/ — acesso 28/09/2026. Fonte secundária.

---

**Rastreabilidade:** as observações desta análise alimentam as hipóteses **H09** (interfaces conhecidas), **H10** (complexidade das ferramentas) e **H11** (padrões familiares) em [`../../RASTREABILIDADE.md`](../../RASTREABILIDADE.md). O padrão "seleção de modelo com justificativa" alimenta a recomendação **RC01** verificada em [`../02_analise_concorrencia.md`](../02_analise_concorrencia.md).
