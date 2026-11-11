# Pendências e inconsistências — Entregas 01 a 06

**Levantamento inicial:** 30/10/2026
**Escopo revisado:** `README.md`, `RASTREABILIDADE.md`, `docs/01` a `docs/04`, análises individuais em `docs/entrega_2/` e assets citados nessas entregas.

## Como usar este arquivo

- Cada pendência tem um ID estável (`INC-xx`). **Não apague itens resolvidos**: mude o status no painel e preencha a coluna "Resolução" (o que foi feito, por quem e em qual commit).
- O **painel** é a fonte de verdade do status. As seções detalhadas descrevem o problema e uma sugestão de correção.
- Se a correção mudar uma hipótese, um perfil, o escopo ou uma recomendação, registre também em [`RASTREABILIDADE.md`](RASTREABILIDADE.md), seção 5.
- Os números de linha são do dia do levantamento e podem ter mudado. Use a seção do documento como referência principal.
- **Os documentos descrevem o TCC previsto (ideal), não o estado atual da implementação** (decisão de 08/11/2026). Limitações momentâneas do código do TCC não viram pendência nem texto nas entregas.

**Severidade**

- 🔴 **Alta**: afeta a sustentação de uma evidência ou recomendação, ou é item obrigatório da entrega.
- 🟠 **Média**: contradição entre documentos que um avaliador pode apontar.
- ⚪ **Baixa**: forma, redação ou padronização.

**Status:** ⬜ aberta · 🟨 em andamento · 🟩 resolvida · ➖ descartada (com justificativa)

---

## Decisões que a equipe precisa tomar antes de corrigir

Alguns itens não são correção de texto: dependem de uma decisão do grupo. Vale resolver estes primeiro, porque destravam vários outros.

| Decisão | Itens afetados |
|---|---|
| ~~Qual é a lista real de classes do modelo do TCC e como serão nomeadas na interface?~~ **Decidido em 08/11/2026 (D1):** segmentação binária, *Trilha* × *Fora da trilha* (classe `Trail` dos datasets do TCC). | INC-11, INC-12 |
| ~~Adicionar ou gerenciar modelos está dentro ou fora do recorte de IHC?~~ **Decidido em 08/11/2026 (D2, corrigido no mesmo dia):** configurar e treinar estão **dentro**. "Configuração" = modelo + parâmetros de treino expostos ao usuário (épocas, early stopping e paciência, datasets de treino, batch size, gráficos). Novas arquiteturas e parâmetros internos ficam fora. | INC-14, INC-31, INC-32, INC-61 |
| ~~Qual perfil a P02 (Andreia) representa: desenvolvedora de modelos ou coordenadora? Ela é primária ou secundária?~~ **Decidido em 08/11/2026 (D3):** pesquisadora/coordenadora que configura, treina e compara os modelos; secundária; é a "coordenação" do C02. | INC-31, INC-34, INC-49 |
| O mapa de empatia da Andreia entra na E3 (corrigido) ou sai do repositório? | INC-33 |
| ~~T03 e T04 são a mesma tarefa ou tarefas diferentes?~~ **Decidido em 30/10/2026:** são tarefas diferentes (T03 = uma imagem entre configurações; T04 = desempenho consolidado entre modelos). | INC-05, INC-47 |
| ~~RC03 será sustentada com uma nova captura ou rebaixada para "média"?~~ **Decidido em 08/11/2026 (D7):** rebaixada para "média". | INC-22 |
| **Decididos também em 08/11/2026:** H01 reescrita como afirmação (D4); métricas só no conjunto de teste anotado (D5); histórico fora do recorte até a E7 (D6); T03 e T07 separadas, IDs do C03 alinhados à E5 e T02 renomeada (D8). Registro completo em `RASTREABILIDADE.md` §5. | INC-05, INC-15, INC-16, INC-39, INC-52, INC-56, INC-58 |

---

## Painel

| ID | Sev. | Entrega | Pendência | Responsável sugerido | Status | Resolução |
|---|:-:|---|---|---|:-:|---|
| INC-01 | 🟠 | Todas | Status 🟩 em entregas já revisadas; falta "Histórico de revisões" | Equipe | 🟩 | 08/11: **decisão da equipe:** o status 🟦 só é usado quando há feedback direto do professor a aplicar; as entregas revisadas internamente continuam 🟩 concluída. Seção "Histórico de revisões" criada na E1, E3, E4 e E6 (a E2 já tinha). |
| INC-02 | ⚪ | E3, E4 | Autoria sem nome completo | Cada autor | 🟩 | 30/10 (Henrique): nome completo na P03 (E3) e no C02 (E4), e na RAST §5. 30/10: nome completo também na P01 e no C01 (Tiago Fagundes dos Santos) e na P02 (Mateus Marana Assuena), com o separador "—" padronizado. |
| INC-03 | 🟠 | E1, E3, E4 | Falta seção de Referências | Equipe | ➖ | 08/11 (Fase 2): seção de Referências criada na E1. **Falta:** E3 e E4. 09/11: a equipe retirou a seção de Referências da E1. 09/11: **descartado por decisão da equipe:** seção de Referências não se aplica às entregas (mesmo critério da E1 e da E5). |
| INC-04 | 🟠 | E4 | "Entrevista com Rafael/Larissa": personas fictícias como fonte | Tiago, Henrique | 🟩 | 30/10 (Henrique): no C02, "Entrevista com Larissa" → "Entrevista com integrante de gestão (perfil P03)" (7 ocorrências). **Falta:** C01 (Q1, Q8 — Tiago). 08/11 (triagem): o C03 também usa "Entrevista com Andreia" (4 ocorrências); C01 ainda com "Entrevista com Rafael" (6). 10/11 (Fase 2): C01 e C03 deixam de citar personas como entrevistados ("integrante que faz a análise de segmentação (perfil P01)" e "pesquisador(a) ou coordenador(a) da equipe (perfil P02)"). |
| INC-05 | ⚪ | E3, E4, RAST | Mesmo ID de tarefa com nomes diferentes | Equipe | 🟩 | 08/11 (Fase 1): T02 = "Executar a segmentação com uma ou mais configurações disponíveis" em E3 (contexto de uso), E4 (C01 e C03), E5, E6 (PF01) e RAST R02. |
| INC-06 | ⚪ | Várias | Erros de grafia | Equipe | 🟩 | 08/11 (Fase 2): corrigidos "pra" (E1 §1.2), "Comprender" e "percusos" (README); os erros da E1 §5.5 saíram com a reescrita da seção. **Falta:** E2 (RC01) e 02_Henrique. 08/11 (Fase 2, E2): "adoptabilidade" saiu com a reescrita e "Pre-roteulagem" → "Pré-rotulagem" (02_Henrique). **Falta:** conferir E3 a E6. 10/11 (Fase 2): conferidas E1 a E6, as análises individuais da E2, README e RAST. Corrigidos "nas pista", "videos" e "se faz necessário" (E1 §5.1 e §5.3); "do ter que", "Pc's" e "Devido a sua" (E3, P01 e P02); "Exeperimentação" (E4 e E5) e "Equipe Baja Fei" (E4); "incial", "comparacao", "nao", "métrica comparativas", "Trocarmos" e "não fica tão claro de qual" (E6). As falas dos participantes da simulação da E6 foram mantidas como ditas. |
| INC-07 | 🟠 | README | Usuário principal ainda "Estudantes do projeto Baja" | Equipe | 🟩 | 08/11 (Fase 2): README usa "Analista de segmentação da equipe Baja FEI (P01)" na tabela e no resumo. |
| INC-08 | ⚪ | README | Campo "recorte" preenchido com o tema | Equipe | 🟩 | 08/11 (Fase 2): campo do recorte no README descreve o fluxo da E1 §11. |
| INC-09 | ⚪ | README, E1 | Restos do template e coluna de responsabilidade vazia | Equipe | ➖ | 08/11 (Fase 2): aviso de template removido do README; coluna "Responsabilidade principal" preenchida no README e na E1 §0.1 com a persona, o cenário e os modelos da E5 de cada integrante. 09/11: **descartado por decisão da equipe:** o aviso do template no README e a coluna "Responsabilidade principal" (README e E1 §0.1) ficam como estavam. |
| INC-10 | 🟠 | E1 | IDs A01–A05 duplicados com significados diferentes | Equipe | 🟩 | 08/11 (Fase 2): ações da E1 §9.2 renomeadas para AC01–AC06; atividades da §3.2 continuam A01–A04; referência da E3 ajustada. |
| INC-11 | 🟠 | E1 | §5.1 fala em "identificar regiões transitáveis" [F], contra §4.3/§5.6 | Equipe | 🟩 | 08/11 (Fase 1): E1 §5.1 separa fato (locais dos testes) de hipótese; §5.2 e §6.4 com [F]/[H] corrigidos; "transitável × não transitável" removido de P01, P03, mapa de empatia, jornada e cenários. |
| INC-12 | 🟠 | E1–E4 | Nomes das classes da segmentação variam entre documentos | Equipe | 🟩 | 08/11 (Fase 1, D1): classes do TCC = segmentação binária *Trilha* × *Fora da trilha* (documento e repositório do TCC). Atualizado em README, E1 §0.4, E2 (RC01, 02_Tiago), E3, E4, E5 (premissa 5). Rascunhos da E6 não alterados (ver INC-59). |
| INC-13 | 🟠 | E1 | §7.1 descreve um recorte menor que §7.3/§7.4/§11 | Equipe | 🟩 | 08/11 (Fase 2): E1 §7.1 descreve configuração e treino, execução, visualização com legenda, métricas e comparação. |
| INC-14 | 🟠 | E1 | Gestão/adição de modelos: dentro ou fora do recorte? | Equipe | 🟩 | 08/11 (Fase 1, D2): "configuração" = modelo + parâmetros de treino expostos ao usuário; configurar e treinar dentro do recorte; novas arquiteturas e parâmetros internos fora. E1 §2.2, §7.1, §8, §9.2 (A06), §9.3 e Delimitação; RAST §1 e R04. A tarefa nova segue no INC-61. |
| INC-15 | 🟠 | E1 | §5.5 afirma necessidade de histórico; §8 e RAST dizem "talvez"/aberta | Equipe | 🟩 | 08/11 (Fase 1, D6): E1 §5.5 reescrita como hipótese H08; histórico fora do recorte até a E7 (E1 §8 e Delimitação, RAST H08). |
| INC-16 | ⚪ | E1, RAST | H01 é uma pergunta e se sobrepõe à H12 | Equipe | 🟩 | 08/11 (Fase 1, D4): H01 = "A decisão sobre qual modelo usar é tomada com base em números dispersos e sem critério explícito" (E1 §10 e RAST §2, texto original preservado). |
| INC-17 | ⚪ | E1, RAST | "Onde investigar" de H05/H08 diverge | Equipe | 🟩 | 08/11 (Fase 2): E1 §10 alinhada à RAST (H05: Entrega 2 e Entrega 7; H08: Entrega 7 e Entrega 8). |
| INC-18 | ⚪ | E1 | §11 ("será implementada: Sim") contradiz a declaração da §7.5 | Equipe | 🟩 | 08/11: interface prevista no TCC; a E1 §7.5 explica que a declaração da disciplina vale para o design produzido nela. |
| INC-19 | ⚪ | E1 | §1.2 e §2.1 marcados [F] sem origem | Equipe | 🟩 | 08/11 (Fase 2): §1.2 e §2.1 com origem "documento do TCC"; §2.1 deixa de usar "Estudantes do projeto Baja". |
| INC-20 | 🔴 | E2, RAST | Links de E5/E6 apontam para `.webm`/`.mp4` inexistentes | Mateus | 🟩 | 08/11 (Fase 2): E5 e E6 apontam para `treinamento-supervisely.png` e `analise-metricas-supervisely.png` (E2 §3 e RAST §7), com tipo "Print"; tempos de vídeo retirados de E2, RAST e 02_Mateus. |
| INC-21 | 🔴 | E2, RAST | Capturas estáticas existem, mas a pendência continua aberta nos docs | Mateus | 🟩 | 08/11 (Fase 2): pendência fechada na E2 §3, no checklist e na RAST §7; legendas do 02_Mateus descrevem capturas estáticas extraídas da gravação. |
| INC-22 | 🔴 | E2, E3, RAST | E6 mostra estatística de dataset, não métricas de modelo (RC03 "alta") | Mateus + Equipe | 🟩 | 08/11 (Fase 1, D7, opção b): RC03 rebaixada para "média" e texto do que a E6 comprova reescrito em E2 (§3.1, RC03, histórico), 02_Mateus, E3 (P01-3, P02-3, mapa de empatia, jornada etapa 6) e RAST (F02, RC03, E6). |
| INC-23 | 🔴 | E2, E3 | E5 não mostra seleção de modelo, mas é citado para isso | Mateus | 🟩 | 08/11 (Fase 1): seleção de modelo da Supervisely marcada como não comprovada em E2 §3.1, 02_Mateus (linha e legenda da E5), P02 decisão 2 e RAST §7. |
| INC-24 | 🟠 | E2 (Mateus) | "Confirma H10" contradiz a consolidação; comentários meta no texto | Mateus | 🟩 | 08/11 (Fase 2): 02_Mateus diz "reforça a H10, que permanece refinada"; CVAT citado como também tendo indicador de progresso; comentário meta removido; tabela descrita como estatística do dataset; afirmação "local e gratuito" virou [H]. |
| INC-25 | 🟠 | E2 (Tiago) | Indicador de progresso atribuído a E2 em vez de E1 | Tiago | 🟩 | 08/11 (Fase 2): lição do 02_Tiago dividida: indicador de progresso com a Figura E1 e painel de eventos com a Figura E2. |
| INC-26 | 🟠 | E2 (Tiago) | "Roda sem instalação" como diferencial, sem evidência | Tiago | 🟩 | 08/11 (Fase 2): "roda sem instalação" (02_Tiago) e "local, gratuito" (02_Henrique, 02_Mateus) reescritos como [H]. |
| INC-27 | 🟠 | E2 | Fontes secundárias e preços ainda não confirmados | Todos | 🟩 | 08/11 (Fase 2): preços de CVAT, Roboflow e Supervisely conferidos nos sites oficiais e atualizados (a Roboflow informa workspaces privados em todos os planos; a Supervisely não tem mais Community auto-hospedada como descrito). Frase do "pre-seed" removida. **Falta:** o G2 respondeu 403 ao navegador; as citações do G2 precisam ser conferidas manualmente. 09/11: citações confirmadas pela equipe nas páginas de origem; registrado na E2 §7 e nos três arquivos individuais. |
| INC-28 | 🟠 | E2 (Henrique) | Print do Roboflow (341 × 192 px) não foi ampliado | Henrique | ➖ | 09/11: **descartado por decisão da equipe:** a captura fica como está. A limitação (recorte parcial, 341 × 192 px) continua registrada na E2 §3, no 02_Henrique e na RAST §7, e o fluxo completo não é citado como evidência. |
| INC-29 | ⚪ | E2 | Status 🟩 com checklist incompleto; nota repetida na §1 | Equipe | 🟩 | 08/11 (Fase 2): nota repetida da §1 unificada; checklist da captura do Supervisely marcado. **Falta:** item de prints legíveis, que depende do INC-28. 09/11: checklist de prints legíveis marcado, com a ressalva do recorte parcial da E3 do Roboflow. |
| INC-30 | ⚪ | E2 (Henrique) | Referência a uma "seção 2.1" que não existe; origem da RC02 divergente | Henrique | 🟩 | 08/11 (Fase 2): referência interna trocada por RAST §5; origem da RC02 unificada como "G2, via SearchTools.ai" (E2, 02_Henrique e RAST); limite de escopo atualizado para o treino dentro do recorte. |
| INC-31 | 🟠 | E1, E3, RAST | Papel da P02: "desenvolvedor de modelos" × "professora coordenadora" | Mateus | 🟩 | 08/11 (Fase 1, D3): P02 = pesquisadora/coordenadora que configura, treina e compara os modelos. E1 §2.2 ("Pesquisador(a) de modelos"), E3 (entrada e ficha da P02), E4 (C03). |
| INC-32 | 🟠 | E3 | Necessidades da P02 fora do recorte (tempo real, treinar modelos) | Mateus | 🟩 | 08/11 (Fase 1): campo Necessidades da P02 inclui configurar e treinar (dentro do recorte) e sinaliza tempo real como fora. **Falta:** mapa de empatia da Andreia (depende do INC-33). 09/11: fechado junto com o INC-33. |
| INC-33 | 🟠 | E3 | Mapa de empatia da Andreia não citado e com contradições | Mateus | 🟩 | 09/11: decisão da equipe: remover `assets/03_personas/mapa_empatia_Andreia.jpeg` (nenhuma entrega o cita; a E3 usa o mapa do Rafael). Arquivo removido pelo Henrique em 10/11. |
| INC-34 | 🟠 | E3 | As três personas estão como "primária" | Equipe | 🟩 | 08/11 (Fase 1, D3): P01 primária; P02 e P03 secundárias (fichas e síntese da E3). |
| INC-35 | 🟠 | E1, E3, E4 | Perfil do Rafael não bate com H02/E1 §2.4 nem com o C01 | Tiago | 🟩 | 08/11 (Fase 2): RAST H02 registra que a P01 refina a hipótese (programa, mas não atua como desenvolvedor e prefere a análise sem código; interpreta métricas, mas sem referência). A Entrega 7 verifica. |
| INC-36 | 🟠 | E3 | Atalhos de teclado na P01 contrariam a lição da E2 | Tiago | 🟩 | 09/11: preferência por atalhos movida para "Comportamentos relevantes" da P01, como `[H]`; "Restrições/acessibilidade" passou a "nenhuma restrição identificada". A decisão 5 foi mantida pela equipe. |
| INC-37 | 🟠 | E3 | P01 diz que a E2 observou comparação de resultados; a jornada diz que não | Tiago | 🟩 | 09/11: base da decisão 1 da P01 diz que a E2 não observou lado a lado e que a transferência é hipótese. |
| INC-38 | 🟠 | E3 | P03 cita RC03/F02 para "valor de referência"; decisões que "sustentam" hipóteses | Henrique | 🟩 | 08/11 (Fase 1): P03 decisão 2 deixa de atribuir o valor de referência à RC03/F02; decisões 1, 2 e 5 "ligam-se" a hipóteses abertas em vez de "sustentá-las". |
| INC-39 | 🟠 | E3 | Histórico nas decisões da P01/P02 × "não construir histórico agora" | Tiago, Mateus | 🟩 | 08/11 (Fase 1, D6): P01 decisão 4 e P02 decisão 5 marcadas como condicionadas à H08 (fora do recorte até a E7). |
| INC-40 | ⚪ | E3 | Decisões 1 e 6 da P02 sem linha "Base:" | Mateus | 🟩 | 09/11: linhas "Base:" acrescentadas às decisões 1 e 6 da P02. |
| INC-41 | 🟠 | E3 | Contexto de uso desatualizado (T01–T03) e com nota de rascunho | Henrique | 🟩 | 09/11: contexto de uso lista T01–T08 por persona; nota de pendência removida. |
| INC-42 | ⚪ | E3 | Data, [F] da jornada e síntese inconsistentes | Equipe | 🟩 | 09/11: data "23/09/2026 (primeira versão) · 16/10/2026 (revisão)"; síntese cita métricas em tabela e em gráfico; o [F] da etapa 6 já tinha sido corrigido em 08/11. |
| INC-43 | 🔴 | E4 | Falta o cenário C03 (P02 / Mateus) | Mateus | 🟩 | 08/11 (triagem): C03 escrito pelo Mateus na E4. |
| INC-44 | 🔴 | E4 | Cabeçalho do C01 com placeholders `{{...}}?` | Tiago | 🟩 | 10/11 (Fase 2): cabeçalho do C01 preenchido (P01; R01, R02 e R03; E1 §4.5; H02, H04, H05, H06). |
| INC-45 | 🔴 | E4 | Refinamento do C01 não acrescenta informação | Tiago | 🟩 | 10/11 (Fase 2): refinamento do C01 reescrito no molde do C02, com respostas hipotéticas em negrito e "Resumo do refinamento". **Rascunho a revisar pelo Tiago.** |
| INC-46 | 🟠 | E4 | Questões redundantes no C01 (Q4 ⊂ Q6, Q2 ⊂ Q8) | Tiago | 🟩 | 10/11 (Fase 2): Q2 reformulada (consequência da falha para o teste do dia) e Q4 reformulada (o que a equipe faz com o resultado), sem renumerar. |
| INC-47 | 🟠 | E4, RAST | T03 e T04 com o mesmo nome | Tiago, Henrique | 🟩 | 30/10 (Henrique): T03 = "Comparar o resultado de uma imagem entre configurações"; T04 = "Comparar o desempenho consolidado entre modelos". Atualizado em E4 (C01, C02), E3 (síntese das personas e contexto de uso) e RAST §3; mudança registrada na RAST §5. |
| INC-48 | ⚪ | E4 | Marcação "[NOVO: ...]" usada uma vez, em formato de rascunho | Henrique | 🟩 | 30/10 (Henrique): criada a seção "Convenção de marcação do refinamento" no topo da E4 (`[Qn]`, normal = mantido, **negrito** = novo, *itálico* = reescrito + tabela "Resumo do refinamento") e aplicada ao C02. O C01 deve adotar a convenção ao resolver o INC-45. |
| INC-49 | ⚪ | E4, RAST | "Coordenação" no C02 sem ligação com a P02; RAST sem registro da E4 | Henrique | 🟩 | 08/11 (Fase 1, D3): "coordenação" do C02 ligada à P02 (cenário, Ator(es) e contexto de uso da E3); RAST §5 com registro retroativo da E4 (20/10). |
| INC-50 | ⚪ | E4 | Checklist da E4 todo desmarcado | Equipe | 🟩 | 08/11 (triagem): checklist foi marcado (8 de 9), mas três itens marcados ainda não se cumprem: origem rastreável do C01 (INC-44), questões que acrescentam informação (INC-45, INC-51) e refinamento que mostra o que mudou no C01 (INC-45). Desmarcar ou resolver. 10/11 (Fase 2): com os INC-44, 45, 51 e 62 resolvidos, os itens marcados passam a valer; o item de TCC sem interface ficou como "não se aplica". |
| INC-51 | 🟠 | E4 | Q11, Q13 e Q16 do C02 não acrescentam informação | Henrique | 🟩 | 10/11 (Fase 2): Q11, Q13 e Q16 reformuladas (antecedência dos resultados, métricas ignoradas, decisão revista) e respondidas como hipótese no cenário refinado; nota de "sem acréscimo" removida. |
| INC-52 | 🟠 | E1, E3, E4 | Métricas (IoU, acurácia) tratadas como disponíveis para qualquer imagem, mas exigem anotação de referência | Equipe | 🟩 | 02/11: restrição explicitada na E5 (T01/T03 e precondições da T05). **Falta:** ajustar E1 §9.2 (A04), P01 decisão 3 e C01. 08/11 (Fase 1, D5): métricas só no conjunto de teste anotado do TCC. E1 §9.2 (A04) e §9.3, E3 (P01-3, P02-3), E4 (C01, Recursos), E5 (premissa 5, RQ06). |
| INC-53 | 🟠 | E5 (Mateus) | Figura da seção 3.1 não corresponde à tabela do HTA da T07 | Mateus | ⬜ | 08/11 (triagem): **regressão.** A E5 no computador voltou a uma versão anterior e aponta de novo para `hta-task-08.svg`, que não existe mais; ver INC-57. 08/11: link restaurado para `hta-task-06.svg` (o arquivo existe); a figura continua sem corresponder à tabela. |
| INC-54 | 🟠 | E5 (Mateus) | HTA da T07: planos divergentes, falta Feedback na tarefa 0 e falta o passo de comparar | Mateus | ⬜ | |
| INC-55 | ⚪ | E5 (Mateus) | GOMS T06 trata métodos como combináveis; CTT T07 sem motivação externa | Mateus | ⬜ | |
| INC-56 | ⚪ | E4, E5 | IDs das tarefas da P02 divergem entre o C03 (T07–T09) e a E5 (T06–T07) | Mateus | 🟩 | 08/11 (Fase 1, D8): C03 usa T02 (compartilhada), T06 e T07; divergência marcada como resolvida na síntese da E5. |
| INC-57 | 🔴 | E5 | A E5 voltou a uma versão anterior: perdeu Síntese, Rastreabilidade e Checklist e a correção do link do HTA da T07 | Henrique | 🟩 | 08/11: Síntese, Rastreabilidade e Checklist restaurados na E5 e link do HTA da T07 apontando para `hta-task-06.svg`. Tabela de protótipo da síntese passou a citar as telas reais da E6 (P01–P03). |
| INC-58 | 🟠 | E4 (Mateus) | C03: refinamento cita Q1–Q7 (do C01) em vez de Q18–Q26; tarefas T07–T09 com origem "C02" | Mateus | 🟩 | 08/11 (Fase 1): marcações do C03 trocadas para Q19, Q20, Q22, Q24 e Q26; origem das tarefas corrigida para C03. |
| INC-59 | 🟠 | E6 | Rascunhos em papel usam classes ilustrativas e IoU por classe para qualquer arquivo | Equipe | ⬜ | 08/11: registrado no histórico da E6; corrigir no protótipo da E11 (não redesenhar a E6 validada). |
| INC-60 | 🟠 | E1, E5, E6 | Dependências do TCC para a interface: avaliação no teste, confiança e sobreposição não existem hoje | Equipe + TCC | ➖ | 08/11: **descartado.** Os documentos descrevem o TCC previsto, não o estado atual da implementação; as menções foram retiradas da E1, E5 e RAST. |
| INC-61 | 🟠 | E3, E4, E5, RAST | Configurar e treinar entrou no recorte, mas não tem persona, cenário nem modelo de tarefa | Equipe | 🟨 | 08/11: registrado na E1 (A06), na E5 (premissa 5) e na RAST (R04). 09/11: T08 criada no C03 (E4) e citada na E3 (síntese das personas e contexto de uso), na RAST (R04) e na E5 (premissa 5). **Falta:** modelar a T08 (HTA/GOMS/CTT), na E5 ou na E9. |
| INC-62 | 🟠 | E4 (Mateus) | Refinamento do C03 sem respostas e com marcações fora da convenção | Mateus | 🟩 | 10/11 (Fase 2): refinamento do C03 reescrito com respostas hipotéticas em negrito para Q18–Q26 e resumo do que mudou; marcações "[Contexto da P02]", "[Necessidade da P02]" e "[P02]" removidas. **Rascunho a revisar pelo Mateus.** |

**Prioridade sugerida:** resolver os 🔴 antes de fechar a E4 e começar a E5. O INC-22 é o mais sensível, porque a RC03 sustenta decisões nas três personas.

---

## Detalhamento

### Transversais

#### INC-01 🟠 Status de entregas revisadas e histórico de revisões
- **Onde:** cabeçalho de `01`, `02` e `03`.
- **Problema:** a E1 foi revisada em 26/09 e 28/09, a E2 em 28/09 e 15/10, e a E3 em 16/10 (segundo a RAST §5). As três continuam como 🟩 "concluída". O `GUIA_DE_USO.md` §10 pede 🟦 "revisada após feedback" e uma seção **Histórico de revisões**. Só a E2 tem essa seção.
- **Sugestão:** trocar para 🟦 e criar o histórico na E1 e na E3, reaproveitando as entradas da RAST §5.

#### INC-02 ⚪ Formato de autoria
- **Onde:** E3 (P01 "Tiago — …", P02 "Mateus Marana - …", P03 "Henrique — …"); E4 (C01 "Tiago - …", C02 "Henrique — …").
- **Problema:** o GUIA §2 pede `**Autor(a):** Nome completo — matrícula`. Os arquivos individuais da E2 já seguem esse formato.

#### INC-03 🟠 Falta seção de Referências
- **Onde:** E1, E3, E4.
- **Problema:** o GUIA §1 (item 8) pede referências em cada entrega. A E3 (personas, mapa de empatia, jornada) e a E4 (cenários, taxonomia de questões) usam métodos que deveriam citar a bibliografia (ex.: Barbosa & Silva; Rogers, Sharp & Preece).

#### INC-04 🟠 Persona fictícia citada como fonte de entrevista
- **Onde:** E4 C01 (Q1, Q8: "Entrevista com Rafael"); C02 (Q10–Q17: "Entrevista com Larissa").
- **Problema:** P01 e P03 são proto-personas e não podem ser entrevistadas.
- **Sugestão:** "entrevista com um integrante que faz a análise de segmentação (perfil P01)" e "integrante com papel de gestão (perfil P03)". Isso já prepara o recrutamento da E7.

#### INC-05 ⚪ IDs de tarefa com nomes diferentes
- **Onde:** T02 aparece como "Executar a segmentação de imagens com uma configuração disponível" (E4 C01) e como "enviar imagem e iniciar a execução" (RAST R02; E3 §3).
- **Sugestão:** fixar um nome por ID antes da E5, que vai modelar essas tarefas. Ver também INC-47.

#### INC-06 ⚪ Grafia
- "adoptá-la" (E2 RC01), "adoptabilidade" e "Pre-roteulagem" (02_Henrique), "Comprender" e "percusos" (README), "images", "segementação" e "possivel" (E1 §5.5), "pra" (E1 §1.2).

### README

#### INC-07 🟠 Usuário principal desatualizado
- **Onde:** README, tabela "Relação entre TCC e projeto de IHC" (linha ~43) e "Resumo do projeto" (linha ~52).
- **Problema:** ainda usa "Estudantes do projeto Baja". A RAST §5 (28/09) registra que o termo foi padronizado como "analista de segmentação da equipe Baja FEI", e o checklist da E2 marca a correção como feita.

#### INC-08 ⚪ Campo "recorte" com o tema
- **Onde:** README, "Interface/recorte explorado na disciplina: Segmentação Semântica".
- **Sugestão:** usar o recorte da E1 §11: upload → execução → visualização lado a lado → métricas → comparação entre modelos.

#### INC-09 ⚪ Restos do template
- **Onde:** README linhas 3–4 ("Template acadêmico… Substitua todo texto entre `{{...}}`"); coluna "Responsabilidade principal" vazia no README e na E1 §0.1.

### Entrega 1

#### INC-10 🟠 IDs de atividade duplicados
- **Onde:** E1 §3.2 e §9.2.
- **Problema:** na §3.2, A03 = analisar/interpretar e A04 = comparar. Na §9.2, A03 = ver lado a lado, A04 = ver métricas e A05 = comparar. A E3 cita "A01–A05 (01 §3.2, §9.2)" como se fossem a mesma lista.
- **Sugestão:** unificar em uma lista ou renomear a da §9.2 (ex.: AC01–AC05).

#### INC-11 🟠 Transitabilidade afirmada como fato
- **Onde:** E1 §5.1 ("identifiquem regiões transitáveis e não transitáveis", marcado [F]).
- **Problema:** a §4.3 e a §5.6 dizem que o resultado da segmentação **não** autoriza conclusões sobre transitabilidade ou segurança do trajeto. Além disso, a §5.1 marca como [F] algo hipotético ("poderia ocorrer"). O mesmo acontece na §5.2 ("ocorreria" [F]) e na §6.4 ("podem facilitar" [F]).
- **Observação:** o rótulo "transitável × não transitável" reaparece na P01 (decisão 2), na jornada (etapa 5), na P03 e nos cenários. Decidir junto com o INC-12.

#### INC-12 🟠 Classes da segmentação sem nomenclatura única
- **Onde:** E1 §0.4 ("pista, vegetação, obstáculos"); README ("pista e vegetação"); 02_Tiago ("área transitável, vegetação, céu, obstáculo"); E2 RC01 ("pista, vegetação, intransitável"); E3 ("transitável × não transitável").
- **Sugestão:** registrar a lista real de classes do modelo do TCC. Ela define a legenda, a RC01 e os signos da E9.

#### INC-13 🟠 Recorte descrito de formas diferentes
- **Onde:** E1 §7.1 (Caminho A).
- **Problema:** a §7.1 fala apenas em enviar → processar → ver lado a lado com legenda. Métricas e comparação entre modelos, presentes na §7.3, §7.4, §9.2 e §11, não aparecem.

#### INC-14 🟠 Gestão de modelos: dentro ou fora?
- **Onde:** E1 §2.2, §7.1, §8 e Delimitação.
- **Problema:** a §7.1 exclui "inserir novos modelos" e a Delimitação exclui "configuração avançada". Porém, a §2.2 atribui ao desenvolvedor "adicionar novos modelos ao sistema" e a §8 marca "Administração — gerenciar modelos disponíveis" e "Configuração/parametrização" como "talvez".

#### INC-15 🟠 Histórico afirmado como necessidade
- **Onde:** E1 §5.5 ("Existe a necessidade de manter o histórico…").
- **Problema:** a §8 diz "talvez", e a RAST mantém a H08 aberta, a RC02 como pendente e o F05 como "NÃO sustentado".
- **Sugestão:** reescrever como hipótese, apontando para a H08.

#### INC-16 ⚪ H01 não é uma hipótese
- **Onde:** E1 §10 e RAST §2.
- **Problema:** a H01 copia o título da §1.4 ("O que se espera que esteja diferente…?"), que é uma pergunta e não uma afirmação verificável. Além disso, ela se sobrepõe à H12 (benefício esperado).
- **Sugestão:** reescrever como afirmação testável ou fundir com a H12, preservando o histórico.

#### INC-17 ⚪ "Onde investigar" divergente
- H05: E1 §10 diz "Entrega 2"; RAST diz "Entrega 7".
- H08: E1 §10 diz "Entrega 8"; RAST diz "Entrega 7 e 8".

#### INC-18 ⚪ Implementação no TCC
- **Onde:** E1 §11 ("Interface da disciplina será implementada no TCC? Sim") × declaração da §7.5 ("somente ocorrerá se… decidido").
- **Sugestão:** como o TCC já prevê a interface, explicar que a declaração é texto-padrão da disciplina ou ajustá-la.
- **Resolução (08/11/2026):** a interface está prevista no TCC. A §7.5 explica que a declaração da disciplina vale para o design produzido nela. Os documentos descrevem o TCC previsto, não o estado atual da implementação.
#### INC-19 ⚪ [F] sem origem
- **Onde:** E1 §1.2 e §2.1.
- **Problema:** o GUIA §5.1 pede que todo [F] indique a fonte. A §2.1 também usa "Estudantes do projeto Baja" (ver INC-07).

### Entrega 2

#### INC-20 🔴 Links quebrados de E5 e E6
- **Onde:** `02_analise_concorrencia.md` §3 (linhas ~66–67) e RAST §7.
- **Problema:** os dois apontam para `treinamento.webm` e `analise-metricas.mp4`, que não existem em `assets/02_concorrencia/`. Lá estão `treinamento-supervisely.png` e `analise-metricas-supervisely.png`, já usados no `02_Mateus.md`.
- **Sugestão:** atualizar os links e trocar o tipo de "Vídeo" para "Print".

#### INC-21 🔴 Pendência das capturas estáticas aberta só no papel
- **Onde:** E2 §3 (nota "Pendência material", linha ~69) e checklist (linhas ~188–189); RAST §7 (nota final); 02_Mateus (última linha da tabela de lições).
- **Problema:** os PNGs já existem, mas os documentos continuam pedindo para "extrair os frames". As legendas do 02_Mateus ainda falam em "instantes ~12–18 s" e "gravação de tela" para uma imagem estática.
- **Sugestão:** confirmar quais quadros foram extraídos, ajustar as legendas e fechar a pendência (ou registrar o que ainda falta).

#### INC-22 🔴 E6 não mostra métricas do modelo
- **Onde:** `assets/02_concorrencia/analise-metricas-supervisely.png`.
- **Problema:** a imagem mostra a matriz **Class Co-Occurrence**, uma estatística do **dataset** (quantas vezes duas classes aparecem juntas). Não é desempenho do modelo. Mesmo assim, ela sustenta:
  - RC03 com "sustentação **alta**" (E2 §5; RAST §6);
  - F02 (RAST §4);
  - a linha "Análise de métricas do modelo" do 02_Mateus;
  - as decisões P01-3, P02-3 e P03-2 da E3;
  - a etapa 6 da jornada, marcada como [F].
- **Sugestão:** (a) recapturar uma tela de avaliação de modelo da Supervisely que mostre métricas em tabela; ou (b) rebaixar a RC03 para "média" e reescrever o que a E6 de fato comprova ("o produto apresenta estatísticas em tabela").

#### INC-23 🔴 E5 não mostra seleção de modelo
- **Onde:** `assets/02_concorrencia/treinamento-supervisely.png`.
- **Problema:** a imagem mostra barras de época e lote e gráficos de treino (box/cls/dfl loss, precision & recall). Isso sustenta a RC04 (progresso), mas **não mostra a seleção de modelo**. Mesmo assim, a E2 §3.1 marca "Seleção de modelo em lista explícita — Supervisely: Sim (E5)", o 02_Mateus descreve "seleção de modelo" nessa evidência e a P02 (decisão 2) cita "E1/E5".
- **Observação:** as métricas do gráfico são de **detecção de objetos**, não de segmentação. Evitar usar o print como referência de métricas de segmentação.

#### INC-24 🟠 Texto do 02_Mateus diverge da consolidação
- **Onde:** 02_Mateus, tabela de opiniões ("**Confirma a hipótese H10**") e "Contexto e proposta".
- **Problema:** a consolidação (§6) e a RAST tratam a H10 como **refinada** e afirmam que opinião de terceiros não confirma hipótese. O texto também traz comentários meta ("padrão que o professor apontou… e que a equipe havia ignorado") e diz que a Supervisely é "a única das três" com barra de progresso, embora o CVAT tenha indicador (E1).

#### INC-25 🟠 Evidência trocada no 02_Tiago
- **Onde:** 02_Tiago, lição "Indicadores de progresso e eventos".
- **Problema:** a lição usa E2 (`cvat_metricas.png`), que a consolidação classifica como métricas de produtividade de anotação. O indicador de progresso da consolidação vem da E1.

#### INC-26 🟠 "Roda sem instalação" sem evidência
- **Onde:** 02_Tiago, lição sobre a instalação via Docker.
- **Problema:** o texto afirma que rodar sem instalação "é um diferencial do nosso recorte", mas a E1 §9.3 descreve execução local em Python com DeepLabv3+/ResNet152 (possível dependência de GPU).
- **Sugestão:** reescrever ou marcar como [H].

#### INC-27 🟠 Fontes não confirmadas
- **Onde:** E2 §7 (nota sobre fontes secundárias); ressalvas nos três arquivos individuais; preços de CVAT e Supervisely marcados `[?]`.
- **Problema:** as citações ainda não foram conferidas no G2. A frase "captou aporte externo em rodada pre-seed em 2026" (02_Tiago) não tem fonte.

#### INC-28 🟠 Print do Roboflow pequeno demais
- **Onde:** E3 da E2, `roboflow_input_imagens.png` (341 × 192 px). O 02_Henrique pede para ampliar a captura e o checklist "prints legíveis" está desmarcado.

#### INC-29 ⚪ Status × checklist e nota repetida
- **Onde:** E2.
- **Problema:** a entrega está 🟩 com dois itens do checklist desmarcados. Na §1, a mesma nota sobre "Estudante FEI" aparece duas vezes (linhas ~30 e ~32).

#### INC-30 ⚪ Referências internas do 02_Henrique
- **Problema:** o texto cita "seção 2.1 — rastreabilidade", que não existe. A origem da RC02 aparece como "G2" na consolidação e como "SearchTools.ai (reunindo G2)" no individual.

### Entrega 3

#### INC-31 🟠 Papel da P02
- **Onde:** E3, tabela de entrada (linha ~32: "desenvolvedor de modelos… representado por P02"); ficha da P02 ("Professora Coordenadora"); síntese ("pesquisadora / coordenadora"); RAST R03 ("experimentar").
- **Problema:** o perfil "desenvolvedor de modelos" da E1 §2.2 inclui "adicionar novos modelos", o que está fora do recorte (INC-14).

#### INC-32 🟠 Necessidades da P02 fora do recorte
- **Onde:** P02, campos "Necessidades" e "Dores", e o mapa de empatia da Andreia.
- **Problema:** segmentação em tempo real e desenvolver ou treinar os próprios modelos estão fora do recorte. A decisão 4 já reconhece isso para a câmera, mas o campo "Necessidades" continua tratando como necessidade.

#### INC-33 🟠 Mapa de empatia da Andreia
- **Onde:** `assets/03_personas/mapa_empatia_Andreia.jpeg`, que não é citado em nenhuma entrega (a E3 diz que o mapa foi feito só para a P01).
- **Problemas no conteúdo:**
  - os selos "Evidência: H01; H02…" tratam hipóteses como evidência;
  - "Evita depender de código" contradiz a persona (experiência avançada em Python);
  - "Não tem modelos pré-treinados" contradiz o objetivo "Utilizar os modelos pré-treinados";
  - vários itens repetem o mapa do Rafael literalmente.
- **Sugestão:** decidir entre incorporar o mapa corrigido ou removê-lo do repositório.

#### INC-34 🟠 Três personas "primárias"
- **Problema:** P01, P02 e P03 estão como "Tipo: primária", mas a síntese define a P01 como prioritária e as outras duas como "apoiadas na análise produzida por P01".
- **Sugestão:** classificar P02 e P03 como secundárias ou justificar as três primárias.

#### INC-35 🟠 Rafael × perfil prioritário
- **Problema:** a E1 §2.4 e a H02 descrevem um perfil que "pode não dominar programação" e "precisa de orientação para interpretar métricas". O Rafael cursa Ciência da Computação, programa em Python e tem "familiaridade… na interpretação de métricas". Já o C01 diz "mesmo não sendo desenvolvedor".
- **Sugestão:** ajustar a persona ou registrar na RAST que a P01 refina a H02.

#### INC-36 🟠 Atalhos de teclado
- **Problema:** a P01 "prefere atalhos de teclado" e a decisão 5 inclui atalhos e presets, mas a E2 conclui "não prometer atalhos como diferencial". Além disso, uma preferência não é restrição de acessibilidade.
- **Sugestão:** mover o item para "Comportamentos relevantes" e alinhar a decisão 5 com a lição da E2.

#### INC-37 🟠 Comparação lado a lado e a E2
- **Problema:** a decisão 1 da P01 diz que "a comparação de resultado é um padrão presente na E2". A jornada (etapa 4) diz que "a E2 **não** observou 'lado a lado'", e a E2 §3.1 de fato não registra esse padrão.
- **Sugestão:** corrigir a decisão 1 da P01.

#### INC-38 🟠 Bases das decisões da P03
- **Problema:** a decisão 2 (valor de referência para as métricas) cita "RC03 / F02 (sustentação alta)", mas RC03 e F02 tratam de tabela + gráfico, não de valor de referência. Nenhuma recomendação da E2 cobre esse ponto. A decisão 1 diz que o painel "sustenta H01/H06": uma decisão de design não sustenta hipótese.
- **Sugestão:** marcar a decisão 2 como [H] derivada da persona e trocar "sustenta" por "responde a".

#### INC-39 🟠 Histórico nas decisões de design
- **Problema:** a P01 (decisão 4: "lista de execuções anteriores") e a P02 (decisão 5: histórico de execuções) mantêm o histórico entre as decisões. O contexto de uso diz "Não construir busca nem filtros agora", e o F05 está "NÃO sustentado".
- **Sugestão:** marcar essas decisões explicitamente como condicionadas à H08.

#### INC-40 ⚪ Decisões da P02 sem base
- **Problema:** as decisões 1 e 6 da P02 não têm a linha "Base:", que as demais decisões têm.

#### INC-41 🟠 Contexto de uso desatualizado
- **Problema:** o contexto lista só T01–T03 (a E4 criou T04 e T05). A nota "**Pendência:** esta consolidação é proposta de Henrique e precisa ser validada pela equipe" continua no texto, com a entrega marcada como concluída.

#### INC-42 ⚪ Data, [F] e síntese
- **Problemas:**
  - a data da E3 (23/09) não bate com a RAST (concluída em 07/10, revisada em 16/10);
  - a etapa 6 da jornada usa [F] com base na E6 (ver INC-22);
  - a síntese final fala em "comparação de modelos com métricas gráficas" e omite a tabela (RC03).

### Entrega 4

#### INC-43 🔴 Falta o cenário C03
- **Problema:** a entrega pede um cenário completo por integrante. Falta o da P02 (Mateus), e a RAST §3 já registra essa falta.

#### INC-44 🔴 Placeholders no cabeçalho do C01
- **Onde:** C01, linhas ~29–31 ("{{R01}}?", "{{seção 4.4 / H01 / …}}?", "{{H01, H02 ou —}}?").
- **Sugestão:** Necessidade: R01, R02, R03. Situação: E1 §4.5. Hipóteses: H02, H04, H05, H06.

#### INC-45 🔴 Refinamento do C01 sem informação nova
- **Problema:** o cenário refinado é o inicial com as tags [Q] inseridas, sem nenhuma resposta nova. Por exemplo, [Q9] foi colado em uma frase que já existia, e [Q5] está numa frase que não responde "como decide qual modelo comparar". O checklist pede que as questões acrescentem informação e que o refinamento mostre o que mudou.
- **Sugestão:** usar o C02 como referência: respostas hipotéticas marcadas como tais e destaque do que é novo.

#### INC-46 🟠 Questões redundantes no C01
- **Problema:** a Q6 já contém a Q4 (atores e consumidores do resultado), e a Q8 já contém a Q2 (erros na execução).
- **Sugestão:** fundir ou diferenciar.

#### INC-47 🟠 T03 e T04 com o mesmo nome
- **Problema:** as duas se chamam "Comparar resultados entre configurações/modelos".
- **Sugestão:** diferenciar o objeto (ex.: T03 = comparar o resultado de uma imagem entre configurações; T04 = comparar o desempenho consolidado entre modelos) ou unificar em uma tarefa com duas personas. Afeta a E5 e a RAST R03.

#### INC-48 ⚪ Marcação de novidade no C02
- **Problema:** só uma frase usa "**[NOVO: …]**", em formato de rascunho, embora as outras respostas também sejam novas.
- **Sugestão:** escolher um padrão único e aplicá-lo também no C01.

#### INC-49 ⚪ "Coordenação" no C02 e registro na RAST
- **Problema:** o C02 cita "coordenação" como participante da decisão, e a P02 é a Professora Coordenadora. Vale ligar as duas, ou explicar que a coordenação não é a P02. Além disso, a RAST §5 não tem entrada para a criação de C01/C02 e de T04/T05 (20/10).

#### INC-50 ⚪ Checklist da E4
- **Problema:** todos os itens estão desmarcados. Revisar o checklist ao fechar INC-43 a INC-47.

#### INC-51 🟠 Questões do C02 sem acréscimo
- **Onde:** E4, C02, tabela "Resumo do refinamento".
- **Problema:** ao aplicar a convenção de marcação (INC-48), ficou visível que Q11, Q13 e Q16 só repetem o que o cenário inicial já dizia (fluxo de mensagens e planilhas; IoU e acurácia sem referência; modelo inadequado e retrabalho).
- **Sugestão:** reformular essas questões para buscar algo ainda ausente (ex.: Q11 — com que antecedência os resultados chegam antes da reunião?; Q13 — quais métricas por classe ela recebe e quais ignora?; Q16 — já houve uma decisão revista depois do teste?) ou mantê-las para investigação na Entrega 7.

#### INC-52 🟠 Métricas exigem anotação de referência
- **Onde:** E1 §9.2 (A04: "visualizar métricas de desempenho (IoU, acurácia)" de cada segmentação); E3, P01 decisão 3; E4, C01 ("métricas do resultado" de cada execução).
- **Problema:** IoU e acurácia comparam a máscara do modelo com uma máscara de referência anotada à mão. Uma imagem nova capturada em campo normalmente não tem essa anotação, então não há métrica para ela. Os documentos tratam as métricas como se existissem para qualquer execução.
- **Sugestão:** deixar explícito que métricas só existem para imagens do conjunto anotado (avaliação de modelos) e que, para imagens de campo, a avaliação é visual, com apoio da confiança do modelo `[H]`. Conferir com o TCC qual conjunto anotado existe.


#### INC-53 🟠 Figura do HTA da T07
- **Onde:** E5, seção 3.1, imagem `hta-task-08.svg` (texto alternativo "HTA - Tarefa 06").
- **Problema:** a figura mostra outra árvore (1. Segmentar com mais de um modelo, 2. Comparar visualmente, 3. Comparar métricas), enquanto a tabela descreve 1. Selecionar a entrada, 2. Selecionar o modelo, 3. Executar, 4. Visualizar. A árvore da tabela está em `hta-task-06.svg`, que não é usada. Os nomes também fogem do padrão da premissa 4 (`hta_t07_<descricao>.svg`).
- **Sugestão:** decidir qual árvore é a da T07, embutir a figura correta, renomear o arquivo e remover o que sobrar.

#### INC-54 🟠 Estrutura do HTA da T07
- **Onde:** E5, seção 3.1 (tabela e figura).
- **Problemas:**
  - o plano 0 na figura é `1>2`, mas há quatro filhos e a tabela diz `1 > 2 > 3 > 4`;
  - `1.1 + 1.2` e `2.1 + 2.2` indicam paralelo, mas selecionar vem antes de carregar e consultar vem antes de escolher (o próprio CTT usa `[]>>`); pela regra do professor, `+` também exige métodos no GOMS;
  - a tarefa 0 tem Input e Plano, mas não tem **Feedback**;
  - o objetivo é "comparar", mas não há passo de comparação nem repetição por modelo no plano (a seção 3.4 reconhece isso).
- **Sugestão:** usar `>` nos planos 1 e 2; acrescentar ao Plano 0 a repetição `1 > (2 > 3 > 4) > 5`, com um objetivo 5 "Comparar os resultados dos modelos"; incluir o Feedback da tarefa 0.

#### INC-55 ⚪ GOMS T06 e CTT T07
- **Onde:** E5, seções 3.2 e 3.3.
- **Problemas:** a seção "Regras e repetições" diz que os métodos 2.A, 2.B e 2.C "podem ser utilizados em conjunto", mas em GOMS métodos são alternativas escolhidas por regra de seleção (usar em sequência é repetir a meta). O CTT começa direto na interface, sem a motivação externa `M []>> ...` adotada na premissa 3.
- **Sugestão:** reescrever a regra como repetição da meta 2 com outro método; acrescentar ao CTT um nó M (ex.: "decidir comparar modelos para um experimento").

#### INC-56 ⚪ IDs das tarefas da P02
- **Onde:** E4, C03, seção 5 (T07 executar, T08 analisar, T09 comparar) × E5 (T06 analisar, T07 comparar).
- **Sugestão:** alinhar os IDs nos dois documentos e na rastreabilidade.


#### INC-57 🔴 E5 voltou a uma versão anterior
- **Onde:** `docs/05_analise_tarefas.md` no computador do Henrique (gravado em 08/11).
- **Problema:** o arquivo é idêntico à versão anterior a 05/11: as seções Síntese da equipe, Rastreabilidade e Checklist voltaram aos placeholders, e a correção do Mateus no link da seção 3.1 (`hta-task-08` → `hta-task-06`) também se perdeu. Provável efeito de uma operação do git (pull, checkout ou reset).
- **Sugestão:** restaurar as três seções (há cópia da versão de 05/11) e reaplicar a correção do link.

#### INC-58 🟠 Referências internas do C03
- **Onde:** E4, cenário C03.
- **Problemas:** o cenário refinado marca os trechos com `[Q1]`, `[Q2]`, `[Q3]`, `[Q5]` e `[Q7]`, que são questões do C01; as questões do C03 são Q18–Q26. A tabela de tarefas dá origem "C02" para T07–T09, que vêm do C03.
- **Sugestão:** trocar as marcações pelas questões do C03 e corrigir a origem para C03.

### Criados em 08/11/2026 (Fase 1)

#### INC-59 🟠 Rascunhos da E6 divergem das decisões D1 e D5
- **Onde:** `assets/06_prototipos/resultado_segmentacao.jfif` e `comparacao_modelo.jfif`.
- **Problema:** as telas mostram as classes *Transitável*, *Vegetação* e *Céu*, com IoU por classe e distribuição das classes para o arquivo enviado. No TCC, a segmentação é binária (*Trilha* × *Fora da trilha*) e IoU e acurácia só existem para imagens com anotação de referência.
- **Decisão:** a E6 foi validada com o professor e não será redesenhada. A divergência está registrada no histórico da E6 e deve ser corrigida no protótipo da Entrega 11 (legenda binária; métricas só quando a entrada pertence ao conjunto de teste anotado; estado "sem métricas" para imagens de campo).

#### INC-60 ➖ Dependências do TCC para a interface *(descartado)*
- **Era:** registrar nos documentos o que o código atual do TCC ainda não faz (avaliação no teste, confiança, sobreposição, um único arquivo treinado por modelo).
- **Por que foi descartado:** a equipe decidiu que os documentos descrevem o TCC previsto, não o estado atual da implementação; do contrário, cada mudança no código exigiria revisar todas as entregas.

#### INC-61 🟠 Tarefa de configurar e treinar sem cenário nem modelo
- **Origem:** decisão da equipe em 08/11/2026: a configuração reúne o modelo e parâmetros de treino do TCC (épocas, early stopping e paciência, datasets de treino, batch size, gráficos), e o usuário define a configuração e treina pela interface.
- **Problema:** nenhuma persona, cenário (E4) ou modelo de tarefa (E5) cobre essa atividade. A E1 tem a ação A06 e a RAST tem a linha R04, ainda `PENDENTE`.
- **Atenção:** em 28/09/2026 a equipe registrou, após feedback do professor sobre a RC02, que o recorte era só **executar** modelos ("não treinamos modelos"). A decisão de 08/11 revoga esse limite. Vale confirmar com o professor e registrar a justificativa: o TCC prevê que o usuário configure e treine os modelos.
- **Sugestão:** atribuir a tarefa à P02 (a P02 já tem configurar e treinar entre as necessidades), acrescentar uma tarefa ao C03 (ex.: T08 — definir uma configuração e treinar o modelo) e decidir se ela será modelada na E5 ou fica para a E9. Ligar o progresso por época à RC04 e a guarda de configurações treinadas à H08.

#### INC-62 🟠 Refinamento do C03
- **Onde:** E4, cenário C03, seção 3 e "Resumo do refinamento".
- **Problema:** o resumo marcava Q18 e Q20–Q26 como "Novo", mas descrevia só a necessidade de investigar; o cenário refinado não trazia respostas. O texto usava marcações fora da convenção ("[Contexto da P02]", "[Necessidade da P02]", "[P02]").
- **Resolução:** mesmo tratamento do C01 (INC-45): respostas hipotéticas em negrito, nota de proto-persona e resumo do que mudou no texto.

---

## Histórico deste arquivo

| Data | Alteração | Responsável |
|---|---|---|
| 30/10/2026 | Levantamento inicial (INC-01 a INC-50) | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 30/10/2026 | Resolvidos INC-47 e INC-48; INC-02 e INC-04 resolvidos na parte do Henrique; criado INC-51 | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 30/10/2026 | INC-02 resolvido (autoria de Tiago e Mateus) | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 02/11/2026 | Criado INC-52 (métricas exigem anotação de referência) durante a E5 do Tiago | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 05/11/2026 | Criados INC-53 a INC-56 na revisão da seção 3 da E5 (Mateus) | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 08/11/2026 | Triagem: INC-43 resolvido; INC-04, INC-50 e INC-53 atualizados; criados INC-57 e INC-58 | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 08/11/2026 | Fase 1 (decisões transversais D1–D8, conferidas com o repositório do TCC) aplicada nas E1–E6, nas análises individuais da E2 e na RAST. Resolvidos INC-05, 11, 12, 14, 15, 16, 22, 23, 31, 34, 38, 39, 49, 52, 56, 57 e 58; INC-32 em andamento; criados INC-59 e INC-60 | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 08/11/2026 | Correções do Henrique: status das entregas mantido 🟩 (INC-01 resolvido por decisão da equipe); "configuração" = modelo + parâmetros de treino expostos ao usuário, com configurar e treinar dentro do recorte (D2 corrigida); interface prevista no TCC, ainda não implementada (INC-18 resolvido). Criado INC-61 | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 08/11/2026 | Princípio "TCC previsto": retiradas dos documentos as menções ao estado atual da implementação (terminal, edição manual da configuração, tempos em CPU, recursos não implementados). INC-60 descartado; INC-18 com resolução revista | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 08/11/2026 | Fase 2, Entrega 1 e README: resolvidos INC-07, 08, 09, 10, 13, 17, 19 e 35; INC-03 e INC-06 em andamento (partes de outras entregas) | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 08/11/2026 | Fase 2, Entrega 2: resolvidos INC-20, 21, 24, 25, 26 e 30; INC-27 e INC-29 em andamento; INC-28 aguarda nova captura (Henrique) | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 09/11/2026 | Entrega 2 fechada: INC-27 e INC-29 resolvidos (citações confirmadas pela equipe); INC-28 descartado (captura do Roboflow mantida) | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 09/11/2026 | Ajustes do Henrique incorporados: aviso do template e coluna de responsabilidade mantidos (INC-09 descartado); seção de Referências retirada da E1 | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 09/11/2026 | Fase 2, Entrega 3: resolvidos INC-32, 33, 36, 37, 40, 41 e 42; INC-03 descartado; INC-61 em andamento (T08 criada) | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 10/11/2026 | Fase 2, Entrega 4: resolvidos INC-04, 44, 45, 46, 50 e 51; criado e resolvido INC-62 (refinamento do C03). Rascunhos do C01 e do C03 a revisar pelo Tiago e pelo Mateus | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
| 10/11/2026 | INC-06 (grafia) resolvido. Ficam abertos, por decisão da equipe, INC-53 a 55 (E5 do Mateus), INC-59 (protótipo da E11) e INC-61 (modelar a T08) | Henrique Finatti Silveira Belo Trebbi (com apoio do Claude) |
