# Entrega 8 — Ciclo de vida e engenharia de usabilidade

**Data:** 11/11/2026 (início) 
**Status:** 🟨 em andamento

**Responsabilidade:** 1 solução por equipe

## Objetivo da atividade

Transformar o conhecimento acumulado sobre usuários, tarefas, plataforma e contexto em princípios e **metas de usabilidade verificáveis**, mantendo o caráter iterativo do projeto.

## Delimitação do sistema interativo

Antes das características da plataforma, separe:

| Camada | O que pertence ao projeto | O que será avaliado em IHC |
|---|---|---|
| contribuição técnica do TCC | Modelo de IA que utiliza visão computacional para realizar a segementação em vias off-road. | Compreensão do resultado segmentado. Informar com métricas quantitaivas a precisão dos nossos modelos de segmentação. |
| camada de interação da disciplina | upload de imagens/vídeos, utilizar configurações disponíveis, executar a segmentação, visualização e análise do resultado e comparação de modelos | Compreensão, eficiência, satisfação, erros e acessibilidade da interação nessas tarefas |
| integrações/dados simulados | Os dados simulados são as métricas de resultados IoU, acurácia e tempo de inferência. Além disso, temos a captura das imagens/vídeos pela câmera integrada ao véiculo. | O limite do protótipo está relacionada a capacidade de memória e processamento da GPU, quanto maior o volume de dados, há mais consumo de recursos computacionais, podendo gerar erros no processamento. |

Em um protótipo de disciplina, é aceitável simular processamento ou resultados quando a implementação técnica não estiver integrada, desde que isso seja declarado e a simulação seja suficiente para avaliar a interação.

## 1. Características da plataforma

Marcação: `[F]` fato, com a origem indicada; `[H]` hipótese; `[?]` lacuna. A coleta da Entrega 7 foi planejada, mas seus dados ainda não foram analisados, e o que depende dela continua `[H]` ou `[?]`.

| Característica | Descrição | Consequência para IHC |
|---|---|---|
| Software | Aplicação de desktop local, com interface gráfica, executada no computador que roda os modelos e integrada ao código Python do TCC, que treina e executa FCN e DeepLabV3+ `[F]` (Entrega 1, §0.5 e §9.3). A interface gráfica também em Python `[H]`. | Sem conta, cadastro nem permissões dentro do sistema (Entrega 1, §8; F06 e F07). A interface transforma a execução do código em estados (processando, concluído, falhou) e mensagens em linguagem de usuário, sem expor mensagens técnicas do código (RQ01, RC04). |
| Hardware/dispositivos | Computadores e notebooks capazes de executar os modelos e processar imagens/vídeos `[H]`; ter ou não GPU muda o tempo e a memória disponíveis `[F]` (Entrega 1, §5.2 e §9.3; 3, §3.1). E as câmeras do veículo para captação de dados. (Entrega 3, §3). | Projetar para desktop/notebook, com mouse e teclado; uso de celulares/tablets fica fora do recorte (Entrega 3, §3). O layout deve funcionar em tela de notebook, sem exigir monitor grande. Se a projeção se confirmar, legenda, números e rótulos precisam ser legíveis a distância (Entrega 7, A01). O desempenho depende do equipamento, então a interface informa progresso e falhas por recurso, sem prometer tempos. (Entregas 1, §9.3; 3, contexto; 5) |
| Capacidades | As ações AC01–AC06 (Entrega 1, §9.2) e as tarefas T01–T08 (Entrega 5; T08 no C03 da Entrega 4): selecionar e enviar imagens ou vídeos; escolher uma ou mais configurações já treinadas e executar a segmentação, acompanhando o estado; ver a imagem original e a máscara lado a lado ou sobrepostas, com legendas disponiveis; consultar as métricas de cada configuração no conjunto de teste anotado; comparar configurações e modelos; para a P02, definir uma configuração de treino (épocas, early stopping e paciência, datasets de treino, batch size e gráficos) e treinar, acompanhando loss, acurácia e mIoU a cada época `[F]` (Entrega 1, §7.1 e §9.3). | Apoiar T01–T08 sem scripts. A comparação reúne as configurações na mesma visão, sobre a mesma entrada ou o mesmo conjunto anotado, e mostra qual foi usado (RQ02, RQ03). Legenda e paleta fixas em todas as visualizações (RQ04). O treino expõe só os parâmetros do usuário, com valores padrão (Entrega 1, §9.3). Quais métricas aparecem por padrão e quais ficam sob demanda (por exemplo, a matriz de confusão para a P02) é decisão das Entregas 9–11 `[?]`. (Entregas 3 e 5, §1.5, §2.5 e síntese) |
| Restrições | Segmentação binária; imagens novas de campo são avaliadas visualmente; vídeos são segmentados quadro a quadro; novas arquiteturas e parâmetros internos do treino ficam fora; histórico fora do recorte até a H08; processamento em tempo real e integração com o hardware do veículo ficam fora; o resultado não indica segurança ou transitabilidade do trajeto. (Entregas 1, §4.3, §7.1, §8, §9.3 e Delimitação; 5, premissa 5) | Não prometer métricas para toda imagem: prever o estado "sem métricas" para imagens de campo (RQ06). Explicar o que cada métrica indica e não indica (RQ07) e não sugerir que a segmentação autoriza concluir que o trajeto é seguro. A interface exibe e calcula, mas a escolha da configuração continua com as pessoas (RQ08). (Entregas 1, §4.3 e §9.2 AC04; 3, P01-2 e P03-3; 5, 3.3 e síntese) |
| Conectividade/latência | O processamento é local, no computador que executa os modelos (Entrega 1, §8); a análise não depende de rede. O contexto prioritário é o laboratório da FEI (Entrega 1, §5.1). Se há internet nos outros locais de uso, como a beira da pista ou reuniões fora do laboratório, é lacuna `[?]` investigada pela Entrega 7 (I02 5.5; I01 3.3). (Entregas 1, §5.1; 3, §3.1) | Nenhuma função do recorte deve depender de internet. A latência percebida é o tempo de processamento local, não a rede. Como a análise sofre interrupções `[H]`, a interface deve permitir retomar de onde a pessoa parou (Entrega 3, §3). (Entregas 1, §5.3; 3, contexto; 7, A02) |
| Segurança/privacidade | Sistema local, de uso restrito à equipe, sem login, cadastro ou perfis; não guarda dados pessoais de quem usa a interface (Entrega 1, §8). As imagens e vídeos dos testes podem mostrar pilotos, integrantes e instalações da FEI (Entrega 7, aspectos éticos da A02). (Entregas 1, §8; 3; 7, A01 e A02) | Sem autenticação, perfis ou administração. Cuidado ao exibir imagens com pessoas; não copiar nem compartilhar fora da equipe sem autorização. A exportação de resultados ainda não está decidida (`PENDENCIAS.md`, INC-63); se entrar no recorte, deve seguir o mesmo cuidado. (Entregas 1, §8; 7, A02) |
| Volume de dados/histórico | Imagens e vídeos dos testes: o C01 registra algumas dezenas de imagens por sessão, e o C03, cerca de 40 quadros extraídos de trechos de sombra, de vídeos com resoluções diferentes conforme a câmera `[H]`. Vídeos são segmentados quadro a quadro. O histórico é hipótese (H08) e está fora do recorte até a Entrega 7. (Entregas 1, §9.3; 3; 4, C01 Q9 e C03 Q21) | Aceitar imagens e vídeos de resoluções diferentes sem preparação manual. Não construir busca, filtros ou paginação agora. Organizar a sessão atual (entrada, configurações e resultados da mesma comparação) e manter os resultados já executados acessíveis sem recarregar a entrada (RQ03). Só incluir histórico se a Entrega 7 confirmar a H08 e definir o que recuperar. (Entregas 3, contexto; 5, §1.5 e síntese; 7) |
| Tempo de processamento | O processamento pode levar tempo por causa do ResNet152, sobretudo sem GPU; vídeos são segmentados quadro a quadro; o treino pode ser longo e falhar no meio por falta de memória. A P02 inicia o treino e se afasta, e, quando ele falha, reduz o batch size e recomeça `[H]` (Entrega 4, C03 Q26). Não há tempos medidos, e os valores dos protótipos são ilustrativos. (Entregas 1, §9.3; 4, C03 Q26; 5, premissa 5) | Prever estados processando/concluído/falhou, progresso por modelo e, no treino, por época, aviso quando o resultado estiver pronto e estado visível para quem volta depois. A mensagem de erro diz, em linguagem de usuário, o que ocorreu e o que fazer (por exemplo, falta de memória → reduzir o batch size) e oferece repetir. Cancelamento não foi definido nos artefatos anteriores `[?]`. (Entregas 2, RC04; 5, 2.2, 2.3 e T08) |
| Papéis/permissões | Três perfis no mesmo fluxo, sem login: P01 (Rafael), analista e persona prioritária, executa e avalia; P02 (Andreia), pesquisadora/coordenadora, configura, treina e compara; P03 (Larissa), gestora, compara o consolidado e prepara a decisão. A decisão é tomada na reunião com a coordenação. Se essas funções são formais é a H07, ainda aberta `[H]`. (Entregas 1, §2.2 e §5.4; 3, personas e contexto) | Sem telas de administração, perfis ou permissões. Como não há login, a interface deve deixar explícitos a configuração e o conjunto de imagens de cada resultado, para que a recomendação possa ser conferida, e evitar comparar execuções de conjuntos diferentes (RQ02). (Entregas 1, §8; 3, contexto; 5, 1.1 e síntese) |

## 2. Princípios gerais do projeto

Inclua apenas normas, leis, padrões e princípios realmente relevantes, explicando **como** afetam o projeto. Não transforme esta seção em lista de links.

| Princípio/norma | Aplicabilidade ao contexto | Decisão/requisito decorrente | Fonte |
|---|---|---|---|
| Contexto de uso | {{...}} | {{...}} | Entregas 1/3 |
| LGPD, se aplicável | {{...}} | {{...}} | {{fonte oficial}} |
| Acessibilidade | {{...}} | {{...}} | {{WCAG/norma aplicável}} |
| {{outro}} | {{...}} | {{...}} | {{...}} |

## 3. Metas de usabilidade

Usabilidade deve ser discutida **no contexto de uso**. Metas quantitativas devem dizer o que será medido, em qual tarefa, com qual população e qual limite será considerado aceitável.

### 3.1 Metas qualitativas

| Meta | Para quem/tarefa | Evidência desejada | Justificativa |
|---|---|---|---|
| {{ex.: compreensão clara da diferença entre X e Y}} | {{...}} | {{fala/observação}} | {{...}} |

### 3.2 Metas quantitativas

| ID | Dimensão | Métrica | Tarefa/escopo | Meta | Como medir | Justificativa |
|---|---|---|---|---|---|---|
| MU01 | eficácia | taxa de conclusão sem ajuda | T01 | ≥ {{x}}% | teste observado | {{...}} |
| MU02 | eficiência | tempo mediano | T02 | ≤ {{tempo}} | cronômetro/log | {{...}} |
| MU03 | satisfação | escala pós-tarefa | T01–T03 | ≥ {{valor}} | questionário | {{...}} |

### 3.3 Priorização das metas (se exigida na disciplina)

Se o professor solicitar porcentagens que somem 100%, trate-as como **peso de prioridade**, não como métrica de usabilidade.

| Meta | Peso de prioridade | Justificativa |
|---|---:|---|
| MU01 | {{...}}% | {{...}} |
| **Total** | **100%** | |

## 4. Como o ciclo será iterado

Explique que artefatos serão revisitados após protótipos e avaliações.

## Checklist

- [ ] Capacidades e restrições têm impacto de IHC explicitado.
- [ ] Está claro o limite entre contribuição técnica do TCC e camada interativa da disciplina.
- [ ] Resultados/processamento simulados no protótipo foram explicitados.
- [ ] Metas de usabilidade avaliam a interação, não substituem métricas técnicas do TCC.
- [ ] Normas/princípios estão contextualizados, não apenas copiados.
- [ ] Metas quantitativas são mensuráveis e associadas a tarefas/público.
- [ ] Eficácia, eficiência e satisfação são consideradas quando pertinentes.
- [ ] Metas poderão ser verificadas nas Entregas 12–14.
