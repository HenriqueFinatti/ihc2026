# Entrega 2 — Análise C03: Supervisely

**Autor(a):** Mateus Marana Assuena — 22.123.026-1

**Produto analisado:** Supervisely

**Módulo/versão analisada:** plataforma web Supervisely; módulo de **configuração de treinamento** (seleção de modelo, barras de progresso, gráficos de treino e validação) e **aba de análise** do projeto (filtros, estatísticas de dataset, tabelas e visualizações por classe). Há uma edição Community gratuita, um plano Pro pago e uma edição Enterprise em nuvem privada, on-premise ou offline (página de preços, 08/11/2026).

**Link oficial:** https://supervisely.com/

**Data de acesso:** 03/09/2026 (navegação e gravação de tela); 28/09/2026 (fontes públicas de opinião)

## Entrada obrigatória da Entrega 1

| Item citado na Entrega 1 | Tipo | Por que foi citado | Status inicial | Decisão nesta entrega |
|---|---|---|---|---|
| Supervisely | Análogo | É uma ferramenta de segmentação e visão computacional em imagens e vídeos; permite segmentação manual ou com modelos de IA selecionados pelo usuário | F | Manter como análogo de referência — cobre o ciclo completo de visão computacional; o nosso recorte é a etapa de *segmentação e interpretação do resultado* |

## 1. Público-alvo desta análise

O público-alvo da Supervisely são empresas e pesquisadores que precisam desenvolver modelos de segmentação próprios, usando as suas bases de dados ou as bases existentes na plataforma.

Perfil típico: equipes de visão computacional, empresas de manufatura e inspeção visual, e grupos de pesquisa. A plataforma é usada tanto por quem executa o treinamento quanto por quem opera a interface.

**Relação com o nosso público-alvo:** o nosso público prioritário é o *analista de segmentação da equipe Baja FEI* (ver [`../01_conhecendo_o_problema.md`](../01_conhecendo_o_problema.md), seção 7.2). Diferentemente do Roboflow, a Supervisely é apontada publicamente como uma plataforma de **curva de aprendizado íngreme e grande quantidade de funcionalidades**, o que a torna um contraponto útil: mostra o que acontece quando o produto oferece tudo e o usuário não tem perfil técnico.

> `[?]` Não temos evidência de que integrantes do Baja FEI conhecem ou utilizam a Supervisely. A familiaridade permanece como hipótese (**H09**).

## 2. Concorrentes diretos/indiretos

### Análise C03 — Supervisely

**Classificação:** análogo indireto. Posiciona-se como plataforma completa de desenvolvimento de visão computacional, reunindo coleta, organização, anotação, controle de qualidade, treinamento, avaliação e aplicação.

#### Contexto e proposta

A Supervisely surgiu no contexto do crescimento das aplicações de Computer Vision, em que empresas e pesquisadores precisam lidar com grandes volumes de imagens e vídeos para desenvolver modelos de IA.

O problema que a plataforma busca resolver é que desenvolver um modelo de visão computacional envolve várias etapas diferentes: coleta e organização dos dados, anotação, controle de qualidade, treinamento, avaliação e aplicação. A Supervisely foi criada para reunir esse processo em um único ambiente.

A proposta vai além de ser uma ferramenta de anotação: posiciona-se como uma plataforma completa, quase um "sistema operacional para Computer Vision", reunindo diferentes ferramentas em um ecossistema.

No contexto do nosso TCC, a Supervisely é relevante por dois motivos: mostra **barras de progresso de treinamento por época e lote** (o CVAT também tem indicador de progresso, na seleção de modelo — Figura E1 da análise C01), e a sua aba de análise apresenta **tabelas além de gráficos**.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência | O que a evidência sustenta (e o que não sustenta) | Observação de IHC |
|---|---|---|---|---|
| Configuração de treinamento | Tela de acompanhamento do treinamento, com barras de progresso e gráficos (a seleção de modelo **não** aparece na captura estática) | [`treinamento-supervisely.png`](../../assets/02_concorrencia/treinamento-supervisely.png) — barras de progresso de épocas e lotes e gráficos de treino/validação | Sustenta: o produto oferece **acompanhamento visual da execução**, com barras de progresso e gráficos. **Não** sustenta: recuperação efetiva por checkpoint ou histórico de execuções — esses elementos não aparecem nos trechos inspecionados. | É a origem mais clara de **RC04**. O estado acompanhado é o *treinamento*, que também faz parte do nosso recorte (configurar e treinar modelos); para a execução da segmentação, os textos do progresso devem ser adaptados. |
| Análise do projeto (estatísticas do dataset) | Aba de análise do projeto, com filtros, estatísticas de dataset, **tabelas** e visualizações por classe. A tabela capturada é a matriz *Class Co-Occurrence*, estatística do dataset, e não métrica de desempenho do modelo | [`analise-metricas-supervisely.png`](../../assets/02_concorrencia/analise-metricas-supervisely.png) — tabela de coocorrência de classes e menu de estatísticas por classe | Sustenta: o produto apresenta **tabelas, filtros e estatísticas**, além de gráficos. **Não** sustenta: a crítica de "dependência de gráficos" aplicada ao produto como um todo — as tabelas existem e contrariam uma leitura simplista. | Corrige a recomendação **RC03**: a tabela não é apenas algo a acrescentar, é um padrão que o produto **já oferece** ao lado de gráficos. Como a tabela capturada é de estatística do dataset, a sustentação da RC03 é **média**. |

**Legendas das evidências**

- **Figura E5 — `treinamento-supervisely.png`.** Tela de acompanhamento do treinamento: barras de progresso de épocas e lotes e gráficos de treino e validação (as métricas dos gráficos são de detecção de objetos, não de segmentação). *Fonte: captura estática extraída da gravação de tela da equipe durante navegação no produto (uso próprio), 03/09/2026, por volta de 12–18 s.*
- **Figura E6 — `analise-metricas-supervisely.png`.** Aba de análise: tabela *Class Co-Occurrence* (estatística do dataset) e menu de estatísticas por classe. *Fonte: captura estática extraída da gravação de tela da equipe, 03/09/2026, por volta de 8 s.*

#### Experiência do usuário e opiniões

| Opinião | Fonte | O que sugere para o nosso projeto |
|---|---|---|
| Avaliações são predominantemente positivas, destacando a qualidade das ferramentas de anotação, a variedade de recursos e a capacidade de integrar as etapas do desenvolvimento | G2 — https://www.g2.com/sellers/supervisely (acesso 03/09/2026 e 28/09/2026) | A plataforma integra o fluxo de ponta a ponta, o que reduz troca de contexto — um princípio aplicável ao nosso recorte. |
| Usuários apontam como pontos negativos a **curva de aprendizado**, a **complexidade decorrente da grande quantidade de funcionalidades**, relatos de lentidão e limitações dos recursos gratuitos | G2 — https://www.g2.com/sellers/supervisely (acesso em 28/09/2026) | **Reforça a hipótese H10, que permanece refinada** (opinião de terceiros não confirma hipótese sobre o nosso público): é o caso mais claro de excesso de opções entre os três produtos. Apoia a escolha de uma interface contida. |
| A plataforma é considerada adequada a projetos de pesquisa e aplicações profissionais, mas com custo escalonado | G2 | `[H]` Custo de entrada pode pesar para uma equipe estudantil; a forma de distribuição da nossa interface ainda não foi definida. |

> **Ressalva de verificação:** a fonte é pública e identificável, mas a equipe deve registrar a data exata de acesso e, se possível, o recorte analisado. Opinião agregada de terceiros não deve ser tratada como medição do nosso público.

#### Padrões e tendências percebidos

- Transformar a anotação em **uma etapa de um ecossistema completo**, com uso crescente de IA para automatizar a rotulagem.
- Suporte a **múltiplas modalidades de dados** e integração de modelos e ferramentas de treinamento e implantação.
- Interface **densa e orientada a projeto/workspace**, com muitos módulos especializados.
- A densidade é, simultaneamente, o diferencial do produto e o risco para o nosso perfil.

#### Modelo de negócio

- **Modelo comercial em três edições:** Community gratuita (até 2 membros, 5 GB e 10.000 arquivos), Pro a partir de €199 por mês (3 membros incluídos, €85 por membro extra) e Enterprise sob consulta, em nuvem privada, on-premise ou offline (https://supervisely.com/pricing, acesso 08/11/2026).
- A cobrança está ligada a recursos, armazenamento e uso da plataforma, e não apenas a assentos.
- **Implicação para o nosso projeto:** o nosso recorte é um sistema local de uso restrito à equipe, sem cobrança e sem gestão de workspace compartilhado. Portanto, não há necessidade de ativação de usuários ou planos — o que já foi decidido na Entrega 1 (padrões "usuários/permissões" e "administração" marcados como **não** aplicáveis).

> Planos e preços conferidos em https://supervisely.com/pricing em 08/11/2026 (a página informa atualização em 27/10/2026). Os valores podem mudar.

#### Pontos positivos, limitações e lições

| Ponto | Tipo | Evidência | Implicação para o nosso projeto |
|---|---|---|---|
| Tabelas de estatísticas do dataset existem no produto, junto com gráficos | Padrão observado (positivo) | [Figura E6](../../assets/02_concorrencia/analise-metricas-supervisely.png) | **Corrige RC03.** A tabela deve ser adotada como alternativa ao gráfico desde o início, e não como correção de um problema que não existe. A captura não mostra tabela de métricas do modelo (sustentação média). |
| Barras de progresso de época e lote durante o treinamento | Padrão observado (positivo) | [Figura E5](../../assets/02_concorrencia/treinamento-supervisely.png) | Origem mais clara de **RC04**. Aplica-se ao treino de uma configuração e, com textos adaptados, à execução da segmentação. |
| Filtros e estatísticas de dataset na aba de análise | Padrão observado (positivo) | [Figura E6](../../assets/02_concorrencia/analise-metricas-supervisely.png) | Apoia a utilidade de filtros, mas **apenas se** o nosso recorte mantiver histórico — ver H08. |
| Integração de todas as etapas em um só ambiente | Ponto positivo com fonte | G2 | Reduz troca de contexto. No nosso recorte, o caminho inteiro (enviar → executar → comparar) deve estar em uma única interface. |
| Curva de aprendizado e excesso de funcionalidades | Limitação (com fonte) | G2 — ver "Experiência do usuário e opiniões" | Justifica uma interface contida, voltada a **um** fluxo principal. |
| Lentidão relatada | Limitação (com fonte) | G2 | Reforça a necessidade de feedback de estado e de espera tolerada. |
| As métricas do modelo só aparecem diluídos em um fluxo maior | Limite de interpretação | Figuras E5 e E6 | A etapa que o nosso usuário precisa (segmentar e interpretar) **não é o centro** dessas plataformas. Isso é um argumento a favor do nosso recorte: tratar a interpretação como objetivo principal. |
| Cada evidência tem uma única captura estática | Limite de evidência | Figuras E5 e E6 | As capturas foram extraídas das gravações; o que aparece só no vídeo (outros quadros, a seleção de modelo) não é citado como evidência. |

## Referências desta análise

- Supervisely (site oficial). https://supervisely.com/ — acesso 03/09/2026.
- Supervisely — preços. https://supervisely.com/pricing — acesso 08/11/2026.
- G2 — Supervisely. https://www.g2.com/sellers/supervisely — acesso 03/09/2026 e 28/09/2026.

---

**Rastreabilidade:** as observações desta análise alimentam as hipóteses **H08** (necessidade de histórico), **H10** (complexidade das ferramentas) e **H11** (padrões familiares) em [`../../RASTREABILIDADE.md`](../../RASTREABILIDADE.md). O padrão de tabelas altera a recomendação **RC03** e o padrão de barras de progresso sustenta **RC04**, ambos verificados em [`../02_analise_concorrencia.md`](../02_analise_concorrencia.md).
