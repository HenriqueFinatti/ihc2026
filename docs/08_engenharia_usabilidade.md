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

| Característica | Descrição | Consequência para IHC |
|---|---|---|
| Software | | O usuário não precisa de conta nem de permissões, e o fluxo principal é único. A interface precisa transformar a execução do código em estados e mensagens compreensíveis, sem expor parâmetros internos. (Entregas 1, §7.1; 2, RC04; 5) |
| Hardware/dispositivos | Computadores e notebooks capazes de executar os modelos e processar imagens e vídeos, no laboratório da FEI ou em computadores pessoais; as câmeras do veículo e dispositivos móveis apenas capturam os dados. O ResNet152 aumenta o tempo de processamento e o consumo de memória, sobretudo sem GPU. (Entregas 1, §5.2 e §9.3; 3, contexto) | Projetar primeiro para desktop/notebook; não derivar requisitos de uso móvel. O desempenho depende do equipamento, então a interface deve informar progresso e falhas por recurso, sem prometer tempos. (Entregas 1, §9.3; 3, contexto; 5) |
| Capacidades | Selecionar e enviar imagens/vídeos; escolher uma ou mais configurações já treinadas; executar a segmentação e acompanhar o estado; visualizar a imagem original e a máscara lado a lado ou sobrepostas, com legenda *Trilha* × *Fora da trilha*; consultar IoU e acurácia (só no conjunto de teste anotado) e tempo de inferência; comparar modelos/configurações; definir uma configuração de treino e treinar o modelo (P02). (Entregas 1, §7.1 e §9.2 AC01–AC06; 5, T01–T08) | Apoiar as tarefas T01–T08: executar, interpretar e comparar sem scripts. A comparação deve reunir as configurações na mesma visão e deixar claro o conjunto de imagens usado. (Entregas 3 e 5, §1.5 e §2.5) |
| Restrições | Segmentação binária; IoU e acurácia só existem para imagens com anotação de referência; imagens novas de campo são avaliadas visualmente; vídeos são segmentados quadro a quadro; novas arquiteturas e parâmetros internos do treino ficam fora; histórico fora do recorte até a H08; processamento em tempo real e integração com o hardware do veículo ficam fora; o resultado não indica segurança ou transitabilidade do trajeto. (Entregas 1, §4.3, §7.1, §8 e §9.3; 5, premissa 5) | Não prometer IoU para toda imagem: prever o estado "sem métricas" para imagens de campo. Explicar o que cada métrica indica e não indica e não sugerir que a segmentação autoriza concluir que o trajeto é seguro. (Entregas 1, §4.3 e §9.2 AC04; 3, P01-2 e P03-3; 5, 3.3) |
| Conectividade/latência | Não há requisito de conexão definido para a análise; o processamento é local, no computador que executa os modelos. O contexto prioritário é o laboratório da FEI, e a conexão disponível e a necessidade de modo offline são hipóteses a investigar na Entrega 7. (Entregas 1, §5.1; 3, contexto e P01-5; 7) | A interface não deve exigir conexão para analisar. Se o modo offline se confirmar, prever operação local e retomada após interrupção. A latência percebida é o tempo de processamento local, não a rede. (Entregas 1, §5.3; 3, contexto; 5) |
| Segurança/privacidade | Sistema local, de uso restrito à equipe, sem login, cadastro ou perfis; não guarda dados pessoais dos usuários da interface. As imagens e vídeos dos testes podem mostrar pilotos, integrantes e instalações da FEI. (Entregas 1, §8; 3; 7, A01 e A02) | Sem necessidade de autenticação, perfis ou administração. Cuidado ao exibir ou exportar imagens com pessoas; não copiar nem compartilhar fora da equipe sem autorização. (Entregas 1, §8; 7, A02) |
| Volume de dados/histórico | Imagens e vídeos dos testes; o C01 registra algumas dezenas de imagens por sessão e o C03, cerca de 40 quadros extraídos de trechos de sombra. Vídeos são segmentados quadro a quadro. O histórico é hipótese (H08) e está fora do recorte até a Entrega 7. (Entregas 1, §9.3; 3; 4, C01 Q9 e C03 Q21) | Não construir busca, filtros ou paginação agora. Organizar a sessão atual (imagem, configurações e resultados da mesma comparação) e só incluir histórico se a Entrega 7 confirmar a H08 e definir o que recuperar. (Entregas 3, contexto; 5, §1.5; 7) |
| Tempo de processamento | O processamento pode levar tempo por causa do ResNet152, sobretudo sem GPU; vídeos são segmentados quadro a quadro; o treino pode ser longo e falhar no meio por falta de memória. Não há tempos medidos, e os valores dos protótipos são ilustrativos. (Entregas 1, §9.3; 4, C03 Q26; 5, premissa 5) | Prever estados processando/concluído/falhou, progresso por modelo e por época no treino, aviso quando o resultado estiver pronto e mensagem de erro em linguagem de usuário, com opção de repetir. Cancelamento não foi definido nos artefatos anteriores. (Entregas 2, RC04; 5, 2.2, 2.3 e T08) |
| Papéis/permissões | Três perfis no mesmo fluxo, sem login: P01, analista (prioritária), executa e avalia; P02, pesquisadora/coordenadora, configura, treina e compara; P03, gestora, compara o consolidado e prepara a decisão. A decisão é tomada na reunião com a coordenação. (Entregas 1, §2.2; 3, personas e contexto) | Sem telas de administração, perfis ou permissões. Como não há login, a interface deve deixar explícitos o modelo/configuração e o conjunto de imagens de cada resultado, para que a recomendação possa ser conferida; evitar comparar execuções de conjuntos diferentes. (Entregas 1, §8; 3, contexto; 5, 1.1) |

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
