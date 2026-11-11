# Entrega 2 — Análise C01: CVAT

**Autor(a):** Tiago Fagundes dos Santos — 22.123.017-0
**Produto analisado:** CVAT (Computer Vision Annotation Tool)
**Módulo/versão analisada:** CVAT Online (nuvem) e documentação da edição Community (open-source). Versão community citada na documentação: v2.74.0.
**Link oficial:** https://www.cvat.ai/
**Data de acesso:** 27/08/2026 (navegação e coleta das imagens de divulgação do site); 28/09/2026 (fontes públicas de opinião)

## Entrada obrigatória da Entrega 1

| Item citado na Entrega 1 | Tipo | Por que foi citado | Status inicial | Decisão nesta entrega |
|---|---|---|---|---|
| CVAT | Análogo | Ferramenta capaz de anotar imagens e criar máscaras para treinamento de modelos | F | Manter como análogo de referência — **não é concorrente direto**, pois atua na etapa de *anotação*, e o recorte de IHC do projeto é a etapa de *segmentação e interpretação do resultado* |

> Observação de escopo: o CVAT é mantido como referência de **padrões de interface** (seleção de modelo, indicadores de progresso), não como alternativa funcional ao nosso recorte. Ver `../02_analise_concorrencia.md`, seção 3.1.

## 1. Público-alvo desta análise

O público-alvo do CVAT é composto por equipes de visão computacional e IA que precisam **criar e revisar dados anotados** (imagens, vídeos e nuvens de pontos 3D) para treinar ou avaliar modelos.

Perfil típico: engenheiros de ML, pesquisadores, equipes de anotação e empresas de manufatura e inspeção visual. A documentação e os fóruns públicos do produto concentram-se em usuários técnicos, e não em usuários de negócio.

**Relação com o nosso público-alvo:** o nosso público prioritário é o *analista de segmentação da equipe Baja FEI* (ver [`../01_conhecendo_o_problema.md`](../01_conhecendo_o_problema.md), seção 7.2). Esse perfil **não tem a mesma formação** do usuário típico do CVAT: conhece o domínio off-road, mas pode não dominar auto-hospedagem, Docker ou o sistema de atalhos. Portanto, o CVAT é útil como referência de *padrões*, mas **não podemos assumir que o nosso usuário já conhece ou opera esta ferramenta**.

> `[?]` Não temos evidência de que integrantes do Baja FEI utilizam ou conhecem o CVAT. A familiaridade permanece como hipótese (**H09**).

## 2. Concorrentes diretos/indiretos

### Análise C01 — CVAT

**Classificação:** análogo indireto. Atua em **anotação de dados** (criação de ground truth), enquanto o recorte do nosso projeto é **executar a segmentação e interpretar seu resultado**. Não há sobreposição direta de tarefa.

#### Contexto e proposta

O CVAT surgiu dentro da Intel como ferramenta de anotação para o projeto OpenVINO e foi disponibilizado como código aberto em 2018; hoje é mantido pela empresa CVAT.ai. A proposta é permitir marcar objetos com caixas, contornar regiões com polígonos, criar máscaras de segmentação e acompanhar objetos em vídeos, com recursos automáticos e semiautomáticos (Segment Anything, YOLO, interpolação) para acelerar o trabalho.

No contexto do nosso TCC, o CVAT poderia ser usado para produzir as máscaras de referência — por exemplo, marcando a região de *trilha* (no TCC, a segmentação é binária: *Trilha* × *Fora da trilha*) — que servem de ground truth para treinar e avaliar os modelos do TCC (FCN e DeepLabV3+).

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência | O que a evidência sustenta (e o que não sustenta) | Observação de IHC |
|---|---|---|---|---|
| Seleção de modelo para anotação automática | Lista de modelos disponíveis, com opção de correspondência de rótulos e indicação de progresso | [`cvat_selecao_modelo.png`](../../assets/02_concorrencia/cvat_selecao_modelo.png) | Sustenta: o produto **apresenta os modelos em uma lista explícita** e mostra estado do processamento. **Não** sustenta: afirmações sobre eficiência de atalhos ou experiência em modo escuro, pois o recorte não mostra esses elementos, nem o comportamento do produto em uso real, pois é uma imagem de divulgação. | O padrão de **lista explícita de modelos** é mais adequado ao nosso perfil do que descoberta conversacional. Adotar lista, não chat. |
| Indicadores de trabalho de anotação | Painel com contagem de objetos e imagens, tempo de trabalho, velocidade de anotação, tabela de eventos e filtros | [`cvat_metricas.png`](../../assets/02_concorrencia/cvat_metricas.png) | Sustenta: o produto exibe **indicadores de progresso e eventos** do trabalho. **Não** sustenta: acurácia de modelo nem comparação de desempenho entre modelos de segmentação — são métricas de *produtividade de anotação*, objeto diferente do nosso. | Indicadores de progresso são úteis, mas devem ser apresentados como **estado da execução**, nunca como "quão bom é o modelo". |

**Legendas das imagens**

- **Figura E1 — `cvat_selecao_modelo.png`.** Tela de seleção de modelo para anotação automática, com lista de modelos, controle de correspondência de rótulos e indicação de progresso. *Fonte: imagem de divulgação do site oficial do CVAT (https://www.cvat.ai/), acesso 27/08/2026. A composição e as legendas das ferramentas são do próprio site, e os dados (tarefa "Runner") são de exemplo: a imagem mostra o que o produto divulga, não um uso real.*
- **Figura E2 — `cvat_metricas.png`.** Painel de métricas de trabalho de anotação: contagem de objetos e imagens, tempo de trabalho, velocidade de anotação, tabela de eventos e filtros. *Fonte: imagem de divulgação do site oficial do CVAT (https://www.cvat.ai/), acesso 27/08/2026. Os dados da tarefa são de exemplo.*

#### Experiência do usuário e opiniões

As afirmações abaixo são **opiniões de terceiros**, não observações próprias da equipe. A fonte é registrada para que cada opinião seja rastreável.

| Opinião | Fonte | O que sugere para o nosso projeto |
|---|---|---|
| Usuários avaliam o CVAT positivamente quanto à profundidade de anotação e ao controle granular | G2 — https://www.g2.com/products/cvat/reviews (acesso 28/09/2026) | O CVAT é percebido como **poderoso e completo**. Isso é referência para investigar a quantidade de terminologia e configuração adequada ao nosso perfil; não confirma a necessidade de simplificação para o Baja. |
| "Interface densa em funcionalidades" e "curva de aprendizado íngreme" são queixas recorrentes | Oryndex — https://oryndex.co/tools/cvat (acesso 28/09/2026), sintetizando avaliações do G2 | Apoia a hipótese **H10** (ferramentas genéricas são complexas para o perfil priorizado). |
| O **sistema de atalhos é descrito como complexo** e demanda tempo para ser dominado por novos anotadores | Oryndex (sintetizando o G2) | **Corrige uma suposição da equipe:** a equipe havia atribuído "excelente suporte a atalhos" como oportunidade. A evidência pública sugere o contrário para usuários novos. Não devemos prometer atalhos como diferencial. |
| Relatos de lentidão da interface com vídeos muito grandes ou anotações densas | Francis Okafor — https://www.francisokafor.com/tools/cvat (acesso 28/09/2026) | Alerta de desempenho para conteúdos grandes — relevante se o nosso usuário carregar vídeos longos. |
| A instalação auto-hospedada via Docker é apontada como sobrecarga para equipes pequenas | Oryndex; Francis Okafor | `[H]` Sugere que a instalação pesa para equipes pequenas; para o nosso público, isso precisa ser investigado (Entrega 7). |

> **Ressalva de verificação:** as citações acima vieram do G2 e de fontes secundárias que o reproduzem. A formulação foi confirmada pela equipe nas páginas de origem em 09/11/2026 (ver [`../02_analise_concorrencia.md`](../02_analise_concorrencia.md), seção 7).

#### Padrões e tendências percebidos

- **Código aberto (MIT) na edição Community e versão gerenciada em nuvem (CVAT Online):** modelo *open-core*.
- Predomínio de **densidade funcional:** a plataforma cobre imagens, vídeo e 3D com vários tipos de anotação — maximalismo de opções.
- Crescente **assistência por IA** (Segment Anything, YOLO, rastreamento) para reduzir trabalho manual.
- Exportação em **múltiplos formatos padrão** (COCO, YOLO, Pascal VOC, KITTI), evitando dependência de fornecedor.
- Para o nosso perfil, o relevante não é a completude, e sim a **densidade** — exatamente o risco apontado em **H10**.

#### Modelo de negócio

- **Open-core / freemium.** Community Edition sob licença MIT (gratuita e auto-hospedada); CVAT Online em nuvem: Free (US$ 0, limitado), Solo (US$ 33 por mês, ou US$ 23 no plano anual) e Team (US$ 33 por usuário por mês, mínimo de 2 usuários); CVAT Enterprise on-premise ou em nuvem privada, sob consulta.
- A empresa **CVAT.ai** mantém o produto.
- **Implicação para o nosso projeto:** o CVAT compete no *ecossistema*, não apenas na tela. O nosso foco é a etapa de **segmentação e interpretação do resultado**, que ele não cobre.

> Valores conferidos em https://www.cvat.ai/pricing em 08/11/2026. As informações comerciais são de consulta pública e podem mudar.

#### Pontos positivos, limitações e lições

| Ponto | Tipo | Evidência | Implicação para o nosso projeto |
|---|---|---|---|
| Lista explícita de modelos para anotação automática | Padrão observado (positivo) | [Figura E1](../../assets/02_concorrencia/cvat_selecao_modelo.png) | O nosso usuário deve **escolher o modelo por lista ou menu suspenso**, com descrição curta de cada — replicar este padrão. |
| Indicador de progresso na execução de um modelo | Padrão observado (positivo) | [Figura E1](../../assets/02_concorrencia/cvat_selecao_modelo.png) | Adotar indicador de estado da execução, distinguindo "processando", "concluído" e "falhou". |
| Painel de eventos e indicadores do trabalho | Padrão observado (positivo) | [Figura E2](../../assets/02_concorrencia/cvat_metricas.png) | Referência para registrar o que aconteceu em cada execução, sem confundir produtividade com qualidade do modelo. |
| Ícones de ajuda ("?") ao lado de termos técnicos e de cada indicador | Padrão observado (positivo) | [Figura E1](../../assets/02_concorrencia/cvat_selecao_modelo.png); [Figura E2](../../assets/02_concorrencia/cvat_metricas.png) | Referência para a explicação contextual da **RC01**. O conteúdo das ajudas não aparece nas imagens. |
| Densidade de funcionalidades e terminologia | Limitação (com fonte pública) | Oryndex / G2 — ver "Experiência do usuário e opiniões" | A interface deve ser **contida no recorte**: apenas o necessário para enviar imagem, ver o resultado e comparar. |
| Curva de aprendizado e sistema de atalhos complexo | Limitação (com fonte pública) | Oryndex / G2 | **Não prometer atalhos como diferencial**; se incluídos, devem ser documentados. Corrige suposição anterior da equipe. |
| Instalação auto-hospedada exige Docker | Limitação (com fonte pública) | Oryndex; Francis Okafor | `[H]` Reduzir a barreira de instalação pode ser relevante para o nosso público; a forma de instalação da nossa interface ainda não foi definida. |
| As métricas do produto são de produtividade, não de qualidade do modelo | Limite de interpretação | [Figura E2](../../assets/02_concorrencia/cvat_metricas.png) | Nunca apresentar "quantidade de objetos anotados" como "acerto da segmentação". São grandezas diferentes. |

## Referências desta análise

- CVAT (site oficial). https://www.cvat.ai/ — acesso 27/08/2026.
- CVAT — preços. https://www.cvat.ai/pricing — acesso 08/11/2026.
- G2 — CVAT Reviews. https://www.g2.com/products/cvat/reviews — acesso 28/09/2026.
- Oryndex — CVAT. https://oryndex.co/tools/cvat — acesso 28/09/2026. Fonte secundária; usar como pista e confirmar no G2.
- Francis Okafor — CVAT Review. https://www.francisokafor.com/tools/cvat — acesso 28/09/2026. Fonte secundária.

---

**Rastreabilidade:** as observações desta análise alimentam as hipóteses **H09** (interfaces conhecidas), **H10** (complexidade das ferramentas) e **H11** (padrões familiares) em [`../../RASTREABILIDADE.md`](../../RASTREABILIDADE.md). O padrão de seleção de modelo por lista explícita sustenta o fluxo **F01**; a recomendação **RC01** trata separadamente da explicação contextual de termos.
