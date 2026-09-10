# Entrega 2 — Respostas 1 e 2 sobre o CVAT.

## Entrada obrigatória da Entrega 1

Retome o mapa inicial de alternativas e produtos citado na Entrega 1. Aqui a equipe deixa de trabalhar apenas com impressão inicial e passa a **investigar sistematicamente** cada solução.

| Item citado na Entrega 1 | Tipo | Por que foi citado | Status inicial | Decisão nesta entrega |
|---|---|---|---|---|
| CVAT | Análogo | Ferramenta capaz de anotar imagens e criar máscaras para treinamento de modelos | F | analisar / descartar com justificativa |

Se uma hipótese da Entrega 1 for confirmada ou refutada durante esta análise, atualize `H01`, `H02`... em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

## 1. Público-alvo desta análise

O público-alvo do CVAT é composto por pesquisadores, desenvolvedores, estudantes e equipes que trabalham com inteligência artificial e visão computacional. A ferramenta atende especialmente usuários que precisam criar, organizar e revisar anotações em imagens e vídeos para o treinamento de modelos computacionais.

## 2. Concorrentes diretos/indiretos

### Análise C01 — CVAT

**Autor(a):** {{Tiago Fagundes — 22.123.017-0 }}  
**Tipo:**  análogo  
**Link oficial:** https://www.cvat.ai/  
**Data de acesso:** 27/08/2026
#### Contexto e proposta
O CVAT está inserido no contexto do desenvolvimento de soluções de inteligência artificial e visão computacional, em que é necessário ensinar modelos a reconhecer objetos e regiões em imagens ou vídeos. Para realizar esse treinamento, são necessários dados anotados, ou seja, imagens acompanhadas das informações corretas sobre o que aparece nelas. A proposta do CVAT é facilitar a criação, organização e revisão dessas anotações. A ferramenta permite marcar objetos com caixas, contornar regiões com polígonos, criar máscaras de segmentação e acompanhar objetos em vídeos. Também oferece recursos automáticos e semiautomáticos para acelerar esse trabalho. No projeto de segmentação semântica de vias off-road, o CVAT pode ser utilizado para marcar regiões como área transitável, vegetação, céu e obstáculos, produzindo as máscaras que servirão como referência para o treinamento e a avaliação do modelo.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print | Observação de IHC |
|---|---|---|---|
| Seleção de Modelos | Através de lista suspensa | `assets/02_concorrencia/cvat_selecao_modelo.png` | Vamos permitir o usuário selecionar entre os modelos que nós montamos através de uma lista suspensa também. |
| Análise de Métricas | Através de dashboads e gráficos contendo informações sobre a análise. | `assets/02_concorrencia/cvat_metricas.png` | Para nossa interface, seria interessante incluir métricas e gráficos que facilitem a avaliação e a comparação do desempenho dos modelos. |

#### Experiência do usuário e opiniões

Use avaliações públicas, relatos, estudos, testes próprios ou outra fonte identificável. Não trate opinião isolada como verdade universal.


#### Padrões e tendências percebidos

É um sistema pago e bem abrangente. Permite muita liberdade ao usuário, montar projetos, selecionar modelos, diferentes formas de entrar dados etc.

#### Pontos positivos, limitações e lições

| Ponto | Evidência | Implicação para nosso projeto |
|---|---|---|
| {{...}} | {{...}} | {{...}} |
