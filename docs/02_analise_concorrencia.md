# Entrega 2 — Público-alvo e análise de concorrência

**Data:** {{27/08/2026}}  
**Status:** 🟨 Em andamento  
**Responsabilidade mínima:** cada integrante analisa pelo menos 1 concorrente/interface representativa; a equipe produz síntese comparativa.

## Objetivo da atividade

Compreender soluções do mesmo domínio **e também interfaces familiares ao público-alvo**. O objetivo não é copiar telas, mas identificar convenções, padrões, affordances percebidas, problemas recorrentes, expectativas e oportunidades de design.

> **Concorrente não precisa ser idêntico ao produto.** Pode atuar na mesma área, resolver objetivo semelhante ou disputar a mesma necessidade. Quando não houver concorrente direto, use produtos análogos e softwares que o público já utiliza.

### Para TCCs que não previam interface

Não procure apenas um “concorrente do algoritmo”. Investigue **interfaces profissionais que materializam atividades semelhantes** às que o usuário escolhido precisaria realizar.

Exemplos:

- TCC de banco de dados → consoles de administração, ferramentas para DBA, monitoramento e análise de consultas;
- TCC de LLM/ML → painéis de experimentos, gestão de modelos/datasets, comparação de métricas, revisão de resultados;
- TCC de análise de dados → dashboards, ferramentas de BI, filtros, relatórios e exploração;
- TCC de infraestrutura/API → portais administrativos, observabilidade, logs, gestão de credenciais e uso;
- TCC de cibersegurança → consoles de alertas, triagem, histórico e auditoria.

A pergunta é: **“que convenções esse perfil já conhece para executar tarefas equivalentes?”**

## Entrada obrigatória da Entrega 1

| Item citado na Entrega 1 | Resposta no arquivo                     |
|--------------------------|-----------------------------------------|
| CVAT                     |[2_Tiago.md](entrega_2/02_Tiago.md)      |
| Roboflow                 |[2_Henrique.md](entrega_2/02_Henrique.md)|
| Supervisely              |[2_Mateus.md](entrega_2/02_Mateus.md)    |


## 1. Público-alvo desta análise

| Item citado na Entrega 1 | Resposta no arquivo                     |
|--------------------------|-----------------------------------------|
| CVAT                     |[2_Tiago.md](entrega_2/02_Tiago.md)      |
| Roboflow                 |[2_Henrique.md](entrega_2/02_Henrique.md)|
| Supervisely              |[2_Mateus.md](entrega_2/02_Mateus.md)    |


## 2. Concorrentes diretos/indiretos

| Concorrente Analisado    | Resposta no arquivo                     |
|--------------------------|-----------------------------------------|
| CVAT                     |[2_Tiago.md](entrega_2/02_Tiago.md)      |
| Roboflow                 |[2_Henrique.md](entrega_2/02_Henrique.md)|
| Supervisely              |[2_Mateus.md](entrega_2/02_Mateus.md)    |


## 3. Softwares que o público-alvo usa no cotidiano

Analise interfaces que moldam a expectativa do público, mesmo que não sejam concorrentes.

| Software | Por que o público usa | Padrões relevantes | Prints | O que aprender |
|---|---|---|---|---|
| CVAT | Utilizado para anotação de imagens e vídeos, incluindo segmentação e ferramentas de anotação automática com modelos de IA. | Seleção de modelos, automação da anotação, configuração de parâmetros, feedback de progresso, filtros e visualização de métricas. | `assets/02_concorrencia/` |Apresentar os modelos disponíveis de forma clara e permitir que o usuário escolha o modelo utilizado. Utilizar gráficos e indicadores para facilitar a interpretação e comparação dos resultados. |
| Roboflow | Utilizado para criação e gerenciamento de datasets, anotação, treinamento, avaliação e implantação de modelos de visão computacional. | Interface integrada de dataset → anotação → treinamento → avaliação; ferramentas de anotação assistida por IA; gráficos e métricas; comparação entre versões dos modelos | `assets/02_concorrencia/` |A comparação entre versões/modelos é especialmente relevante para permitir que o usuário identifique qual modelo apresenta melhor desempenho. |
| Supervisely | Utilizado para anotação, gerenciamento de datasets, treinamento, avaliação e implantação de modelos de visão computacional. | Auto Labeling, assistência por IA, workflows personalizados, métricas de qualidade e comparação de desempenho entre modelos/checkpoints. | `assets/02_concorrencia/` |Facilitar a utilização de modelos de IA para usuários que não precisam interagir diretamente com código, além de apresentar a comparação de desempenho de diferentes modelos de maneira visual e objetiva. |

## 3.1 Padrões de interface relevantes ao escopo de IHC

Registre somente padrões encontrados nas soluções analisadas e que possam ter relação com objetivos reais da equipe.

| Padrão observado | Produto(s) | Para qual tarefa serve | Vantagem percebida | Risco/limitação | Aplicável ao nosso escopo? |
|---|---|---|---|---|---|
| dashboard | CVAT, Roboflow e Supervisely | Visualizar métricas e informações do modelo | Facilita a compreensão dos resultados.  | Excesso de informações pode dificultar a interpretação. | sim |
| relatório | CVAT, Roboflow e Supervisely | Consultar resultados e desempenho dos modelos. | Centraliza informações importantes para análise. | Relatórios muito técnicos podem dificultar o entendimento por usuários não especialistas. | sim |
| histórico + filtros | CVAT, Roboflow e Supervisely | Localizar tarefas, imagens, modelos ou resultados anteriores. | Facilita a organização e recuperação de informações. | Muitos filtros ou opções podem aumentar a complexidade da interface. | sim |
| administração/CRUD | CVAT, Roboflow, Supervisely | Gerenciar projetos, datasets, tarefas e modelos. | Permite organizar e manter os dados utilizados pela equipe. | Pode adicionar funcionalidades desnecessárias ao escopo inicial. | Talvez |
| comparação de resultados | CVAT, Roboflow e Supervisely | Comparar desempenho e resultados de diferentes modelos. | Facilita identificar qual modelo apresenta melhor desempenho. | Comparações com muitas métricas podem dificultar a interpretação. | sim |

> O objetivo não é concluir “todo concorrente tem dashboard, então teremos um”. O padrão só será adotado se apoiar uma tarefa rastreável.

## 4. Síntese comparativa da equipe

| Critério | C01 | C02 | C03 | Oportunidade para o projeto |
|---|---|---|---|---|
| Navegação |  |  |  |  |
| Feedback/estado |  |  |  |  |
| Prevenção/recuperação de erro |  |  |  |  |
| Terminologia |  |  |  |  |
| Acessibilidade |  |  |  |  |
| Eficiência |  |  |  |  |

## 5. Recomendações derivadas

Liste recomendações com origem explícita.

- **RC01:** {{recomendação}} — derivada de {{C01/C02/evidência}}.
- **RC02:** {{...}}

## Referências

{{fontes dos produtos, avaliações e literatura}}

## Checklist

- [ ] O mapa inicial de alternativas da Entrega 1 foi revisitado e aprofundado.
- [ ] Hipóteses relevantes sobre mercado/padrões foram atualizadas na rastreabilidade quando surgiram evidências.
- [ ] Há pelo menos uma análise completa por integrante.
- [ ] Cada análise contém prints legíveis da interface.
- [ ] Prints mostram telas/estados relevantes, não apenas logos/homepage.
- [ ] Foram analisados concorrentes e/ou interfaces representativas ao público.
- [ ] Em TCC sem interface original, foram investigadas ferramentas profissionais análogas às atividades do usuário escolhido.
- [ ] Padrões como dashboard, relatório, filtros e CRUD foram analisados como soluções para tarefas, não como requisitos automáticos.
- [ ] Opiniões de UX têm fonte.
- [ ] A síntese compara critérios comuns e produz recomendações.
- [ ] Não há “copiar porque o concorrente faz”; há justificativa de adequação ao público/contexto.
