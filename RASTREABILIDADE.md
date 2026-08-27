# Matriz de rastreabilidade de IHC

A matriz deve ser atualizada ao longo do semestre. Ela ajuda a demonstrar que a interface não surgiu arbitrariamente e registra **como o conhecimento da equipe evoluiu**.

Para projetos cujo TCC não previa interface, esta matriz é especialmente importante: deve ficar visível a passagem da **contribuição técnica do TCC** para um **cenário de uso plausível**, e desse cenário para as decisões de interação.

## 1. Derivação do escopo de IHC a partir do TCC

| Elemento | Registro da equipe | Evidência/justificativa | Estado |
|---|---|---|---|
| Tema do TCC | {{...}} | {{documento/TCC}} | definido |
| Resultado técnico esperado | {{algoritmo, análise, sistema, modelo, API...}} | {{...}} | definido |
| O TCC previa interface? | sim / não / parcialmente | {{...}} | definido |
| Capacidade/contribuição central | {{o que a tecnologia permite}} | {{...}} | definido |
| Possíveis beneficiários/stakeholders | {{...}} | {{fonte ou hipótese}} | F / H / ? |
| Usuário escolhido para IHC | {{...}} | {{por que esse perfil}} | F / H / ? |
| Objetivo principal do usuário | {{...}} | {{...}} | F / H / ? |
| Contexto de uso adotado | {{...}} | {{...}} | F / H / ? |
| Interface/recorte de IHC | {{...}} | {{como deriva dos itens acima}} | proposta / revisada |
| Relação com o TCC | parte prevista / extensão conceitual / protótipo demonstrativo / outra | {{...}} | definido |

> Se o escopo de IHC mudar ao longo do semestre, preserve a decisão anterior no histórico e registre **qual evidência motivou a mudança**.

## 2. Registro de hipóteses e lacunas da Entrega 1

Use esta tabela para itens importantes marcados como `[H]` ou `[?]`. Preserve o histórico: não apague uma hipótese refutada.

| ID | Afirmação / dúvida inicial | Tipo | Por que importa | Como/onde investigar | Evidência obtida | Estado atual | Impacto no projeto |
|---|---|---|---|---|---|---|---|
| H00 (EXEMPLO)| {{...}} | H / ? | {{...}} | Entrega 2 / 3 / 7 / outra | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H01 | O que se espera que esteja diferente **para pessoas, organizações ou processos** se essa contribuição for bem-sucedida? | Principal motivo de uso da nossa aplicação | Entrega 4 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H02 | Perfil de usuário (Analista) | Precisamos definir quem poderá usar a interface | Entrega 3 | Que características desses perfis podem influenciar a interação? {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H03 | Perfil de usuário (Piloto Baja FEI) | Precisamos definir quem será afetado pela interface sem usá-la interface | Entrega 3 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H04 | Que características desses perfis podem influenciar a interação? | Precisamos definir as características dos perfis de usuários que influenciam na interface | Entrega 3 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H05 | Como essas atividades são realizadas hoje, antes da interface imaginada na disciplina? | Não sabemos como é realizado as atividades | Entrega 2 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H06 | O que é difícil, demorado, confuso, repetitivo, arriscado ou pouco transparente? | Não sabemos cos problemas existentes | Entrega 4 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H07 | Existem fatores sociais ou organizacionais? | Pesquisar melhor os fatores sociais e organizacionais | Entrega 7 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H08 | Existe necessidade de histórico, rastreabilidade ou auditoria? | Não sabemos se existe a necessidade | Entrega 8 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H09 | Quais interfaces profissionais esse público já conhece? | Não temos certeza de quais ferramentas ele já conhecem | Entrega 7 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H10 | O que parecem fazer mal, dificultar ou não atender? | Não temos certeza de quais ferramentas ele já conhecem | Entrega 7 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H10 | Que padrões de interface ou vocabulário parecem familiares a esse público? | Não conhecemos os familiares desse público | Entrega 7 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H11 | Que padrões de interface ou vocabulário parecem familiares a esse público? | Não conhecemos os familiares desse público | Entrega 7 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |
| H12 | Qual benefício concreto o projeto de IHC pretende oferecer? | Não sabemos quais os benefícios o projeto pode oferecer| Entrega 13 | {{link/fonte ou PENDENTE}} | aberta / sustentada / refutada / refinada | {{...}} |

## 3. Rastreabilidade entre contribuição técnica, necessidades e artefatos

| ID | Capacidade do TCC utilizada | Necessidade/problema | Persona | Cenário problema | Objetivo/tarefa | HTA/GOMS/CTT | Cenário de interação / signos | MoLIC | Tela(s) Figma | Heurística / problema | Tarefa no teste | Decisão/melhoria |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | {{ex.: recomendação de otimização}} | {{...}} | {{P01}} | {{C01}} | {{T01}} | {{links}} | {{...}} | {{M01}} | {{F01...}} | {{V01 ou —}} | {{UT01}} | {{...}} |
| R02 |  |  |  |  |  |  |  |  |  |  |  |  |

## 4. Rastreabilidade de padrões de interface

Use esta tabela quando o projeto incorporar padrões como dashboard, relatório, histórico, filtros ou administração. O objetivo é **justificar o padrão**, não apenas listar telas.

| ID da tela/fluxo | Padrão de interface | Objetivo/tarefa que justifica | Informação/ação principal | Evidência de necessidade | Artefatos relacionados |
|---|---|---|---|---|---|
| F01 | dashboard | {{T01}} | {{...}} | {{H01/evidência...}} | {{C01/M01}} |
| F02 | histórico com filtros | {{T02}} | {{...}} | {{...}} | {{...}} |
| F03 | administração/CRUD | {{T03}} | {{...}} | {{...}} | {{...}} |

## 5. Registro de mudanças de escopo

| Data | O que mudou | Evidência/feedback que motivou | Artefatos afetados | Responsável |
|---|---|---|---|---|
| {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

## Como usar

- Use identificadores estáveis (`H01`, `P01`, `C01`, `T01`, `M01`, `F01`, `UT01`).
- Quando uma necessidade/problema tiver origem em hipótese da Entrega 1, cite o ID correspondente.
- Em TCC sem interface original, pelo menos uma linha deve mostrar claramente **como uma capacidade técnica chega até uma tarefa de usuário e uma tela/fluxo**.
- Uma linha pode se desdobrar quando um objetivo possui múltiplos caminhos.
- Não force relação inexistente: se algo ainda não foi modelado, marque `PENDENTE`.
- Ao remover uma funcionalidade, registre a decisão em vez de apagar silenciosamente o histórico.
- Dashboard, CRUD, filtros e relatórios só devem aparecer quando houver objetivo/tarefa que os justifique.
