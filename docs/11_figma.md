# Entrega 11 — Protótipo (interface implementada)

**Data:** 16/11/2026 (início) · 16/11/2026 (primeira versão completa)  
**Status:** 🟩 concluída  
**Responsabilidade:** 1 protótipo integrado por equipe cobrindo os fluxos MoLIC. Se a turma exigir divisão individual, identifique o responsável por cada fluxo/tela.

## Objetivo da atividade

Materializar o modelo de interação em um protótipo navegável, preservando a lógica dos objetivos, tópicos, signos, feedbacks, alternativas e recuperações definidos anteriormente.

## Biblioteca de possibilidades para projetos técnicos

O protótipo deve materializar os fluxos definidos nas entregas anteriores. Dependendo do escopo, podem fazer sentido:

1. **Dashboard:** indicadores, alertas, estado, tendências e atalhos para tarefas frequentes.
2. **Configuração/parametrização:** escolhas, presets, validação e explicação de opções técnicas.
3. **Entrada de dados:** upload, conexão, seleção, pré-visualização e validação.
4. **Processamento:** fila, status, progresso, cancelamento, falha e reexecução.
5. **Relatório/resultados:** síntese, métricas, gráficos, explicação, exportação e compartilhamento.
6. **Histórico:** busca, filtros, ordenação, paginação, detalhes e repetição de execução.
7. **Comparação:** antes/depois, modelo A/B, execução A/B, baseline ou períodos.
8. **Explicabilidade:** confiança, fatores, evidências, limitações e correção/contestação.
9. **Administração:** usuários, grupos, perfis, permissões, integrações e políticas.
10. **CRUDs de domínio:** somente quando criar/consultar/editar/excluir representa tarefa real.
11. **Auditoria/logs:** histórico de alterações e eventos em linguagem adequada.
12. **Alertas/ocorrências:** severidade, impacto, ação, responsável e resolução.
13. **Ajuda/documentação:** apoio contextual a tarefas complexas.

### Estados que não podem ser esquecidos

Quando aplicável, considere: vazio/sem dados; carregamento/processamento; sucesso; erro de entrada; erro de processamento; filtro sem resultados; permissão insuficiente; confirmação de ação destrutiva; cancelamento/desfazer/recuperação; dados desatualizados/conflito.

> Esta lista é repertório de design, **não uma exigência de quantidade de telas**. A rastreabilidade deve explicar por que cada tela existe.

## Acesso ao protótipo

**Formato:** em vez de um protótipo no Figma, a equipe implementou as telas na própria interface do TCC, com autorização do professor `[F]`. O protótipo é de alta fidelidade e funcional: treino, segmentação, avaliação no conjunto de teste e registros usam o código do TCC, e nenhuma parte da interface é simulada. A interface é feita em HTML e JavaScript, servida pelo código Python do TCC e aberta no navegador do próprio computador, sem internet (Entrega 8, §1).

**Repositório:** https://github.com/HenriqueFinatti/Segmentacao-Semantica-Off-Road, ramo `interface`  
**Versão avaliada:** commit `d11c155f3a8834cd665cc9f86bfd8c6be60093e8`  
**Última verificação de acesso:** 16/11/2026 (repositório público)

> Teste o link em janela anônima. O avaliador deve conseguir abrir o repositório sem solicitar permissão.

### Como executar

1. Instale as dependências, na raiz do repositório do TCC:

   ```bash
   pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu118
   ```

2. Abra a interface:

   ```bash
   python -m app.main
   ```

3. A interface abre no navegador em `http://127.0.0.1:8000/`. As opções `--porta 8080` e `--sem-navegador` mudam a porta e evitam abrir o navegador automaticamente.

O endereço só funciona no próprio computador. Treino e segmentação rodam enquanto o programa estiver aberto: fechá-lo os interrompe, e a interface mostra o treino ou a execução como interrompidos. Para os testes das Entregas 12 a 14, a interface deve rodar sobre uma cópia dos dados, indicada por `SEG_ROOT=<pasta da cópia> python -m app.main`, para não alterar os dados do TCC.

### Evidência no repositório

As capturas das telas e dos estados ficam em `assets/11_figma/`, uma subpasta por tela (TL01 a TL11), e foram feitas na interface implementada em 16/11/2026 `[F]`. Nelas, os valores das métricas são **ilustrativos** e não são resultados do TCC: as capturas usaram uma cópia reduzida dos dados (conjunto de teste com 12 imagens e treinos de 1 ou 2 épocas). As imagens IMG_0401 a IMG_0404 fazem o papel de imagens de campo, mas são imagens de treino do Freiburg Forest com outro nome.

## Cobertura MoLIC → telas

O protótipo implementa os três MoLIC da Entrega 10. As telas TL01 a TL10 correspondem às cenas; a TL11 é uma tela de apoio, fora dos MoLIC. As cenas reusadas entre diagramas (O03.1, O03.2, O05.2, O06.3, O07.2, O08.1 e O08.2) são uma única tela, usada por mais de uma persona. Nos nomes das capturas, **E** indica ruptura com recuperação (AL, RA ou CE), **P** indica prevenção (PA ou PP) e **V** indica estado vazio.

| MoLIC | Objetivo | Fluxo/telas | Estados de erro/recuperação | Responsável |
|---|---|---|---|---|
| M01 | O03 | TL03 → TL04 | TL03 E1 (AL: formato não aceito); TL04 E1 (RA e CE: falha na execução) | Tiago Fagundes dos Santos |
| M01 | O04 | TL04 → TL05 | TL05 P1 (PP: sem métricas, avaliação visual); TL05 V1 (sem sessão) | Tiago Fagundes dos Santos |
| M01 | O05 | TL05 → TL06 → TL04 → TL06 | Os da TL04 (a execução reusa a O03.2) | Tiago Fagundes dos Santos |
| M01 | O08 | TL05 → TL08 | TL08 E1 (AL: imagens sem avaliação); "Corrigir" na conferência | Tiago Fagundes dos Santos |
| M02 | O06 | TL07 | TL07 E1 (CE: sem avaliação no conjunto de teste); TL07 E2 (AL: conjuntos de teste diferentes); TL07 E3 (CE: execução faltante no ciclo); TL07 V2 (sem valor de referência) | Henrique Finatti Silveira Belo Trebbi |
| M02 | O07 | TL07 (O07.2) e TL10 (O07.1) | — | Henrique Finatti Silveira Belo Trebbi |
| M02 | O08 | TL07 → TL08 | "Corrigir" na conferência | Henrique Finatti Silveira Belo Trebbi |
| M02 | O09 | TL09 | TL09 V1 (sem recomendação) | Henrique Finatti Silveira Belo Trebbi |
| M02 | O10 | TL09 | TL09 P1 (PA: condição obrigatória) | Henrique Finatti Silveira Belo Trebbi |
| M03 | O01 | TL01 | TL01 E1 (PA: sem dataset de treino); TL01 E2 (RA: nome repetido) | Mateus Marana Assuena |
| M03 | O02 | TL02 e indicador do treino no topo | TL02 E1 (RA: treino interrompido) | Mateus Marana Assuena |
| M03 | O03, O05 | TL02 → TL03 → TL04 → TL06 | Os da TL03 e da TL04 | Mateus Marana Assuena |
| M03 | O06, O07 | TL06 → TL07 | TL07 E2 (AL: conjuntos de teste diferentes) | Mateus Marana Assuena |
| M03 | O08 | TL07 → TL08 | "Corrigir" na conferência | Mateus Marana Assuena |

A ruptura de treino interrompido por falta de memória, com a sugestão de um batch size menor, está implementada, mas não foi capturada: ela não pode ser provocada no computador usado nas capturas.

### Diferenças em relação aos MoLIC

| Diferença | Onde | Motivo |
|---|---|---|
| Tela de apoio **Datasets**, que não está em nenhum MoLIC; ela também cria a ruptura "configuração sem avaliação no conjunto de teste" (CE) | TL11; TL07 E1 | Sem ela não há dados para treinar nem para calcular as métricas no conjunto de teste |
| Estado **"na fila"**, que vem da Entrega 6 e não está entre os signos da Entrega 9 | TL04 | Treino e execução rodam um de cada vez, porque usam o mesmo processador gráfico |
| "Sair, o treino continua" só vale enquanto o programa estiver aberto; se ele for fechado, o treino aparece como interrompido, com "Reiniciar" | TL02 | Plataforma local (Entrega 8, §1) |
| **Valor de referência** = métricas da configuração em uso, que é a última executada; a decisão da coordenação (O10) não muda a situação "em uso" | TL07 | A origem do valor de referência era `[?]` na Entrega 9; a equipe definiu a regra na implementação |
| **Ciclo de testes** informado pela pessoa ao enviar as entradas | TL03 | A Entrega 9 não definia como as execuções são agrupadas em ciclos |
| A O04.2 sempre mostra "sem métricas, avaliação visual" | TL05 P1 | Só imagens de campo, sem anotação de referência, são enviadas para segmentar; as métricas ficam no desempenho consolidado (TL07) |
| Falha de uma configuração inteira, com "Tentar de novo" e "Deixar esta configuração de fora" (o MoLIC só desenha a falha por imagem) | TL04 E1 | A causa (por exemplo, pesos ausentes) afeta todas as imagens daquela configuração |
| Da O03.2 para a O04.1 ou para a O05.2 por botão, e não automaticamente | TL04 | A pessoa não perde o contexto se estava lendo outra informação da tela |
| A O05.1 não executa de novo uma configuração já executada nas imagens escolhidas | TL06 | Evita repetir o mesmo processamento |
| Confirmação antes de "Remontar o dataset" | TL11 | A remontagem substitui o dataset e pode mudar o conjunto de teste |
| Configurações treinadas antes da interface aparecem sem o histórico das épocas | TL02, TL03 | Esse treino não passou pela interface |

As decisões desta tabela estão registradas no `RASTREABILIDADE.md`, §5 (16/11/2026).

## Catálogo de telas/estados

Cada tela traz o responsável, o objetivo do usuário, os signos principais (Entrega 9, §4), a origem no MoLIC e as capturas dos estados implementados. As capturas são da interface implementada; os valores das métricas são ilustrativos (ver "Acesso ao protótipo").

### TL01 — Configuração de treino

**Responsável:** Mateus Marana Assuena — 22.123.026-1 (fluxo do M03)  
**Objetivo do usuário:** Definir o modelo e os parâmetros de treino de uma nova configuração, dar um nome a ela e iniciar o treino.  
**Signos principais:** Modelo; parâmetros de treino (épocas, early stopping, paciência, datasets de treino, batch size, geração de gráficos); valor padrão; nome da configuração; descrição da configuração.  
**Origem no MoLIC:** M03 — O01.1 Escolher o modelo e os parâmetros; O01.2 Nomear a configuração.

![TL01 — Escolher o modelo e os parâmetros](../assets/11_figma/TL01_configuracao_de_treino/TL01_escolher_modelo_e_parametros.png)

*Escolher o modelo e os parâmetros (O01.1): valores padrão do TCC já preenchidos, ajuda em cada parâmetro e aviso de que os parâmetros internos do treino são fixos.*

![TL01 — Prevenção ativa](../assets/11_figma/TL01_configuracao_de_treino/TL01_E1_sem_dataset_de_treino.png)

*Prevenção ativa (PA): sem dataset de treino, a interface pede pelo menos um para continuar. Na captura, o botão "Continuar" aparece ativo, diferente da TL09, que desabilita o botão (`PENDENCIAS.md`, INC-70).*

![TL01 — Nomear a configuração](../assets/11_figma/TL01_configuracao_de_treino/TL01_nomear_configuracao.png)

*Nomear a configuração (O01.2): resumo dos parâmetros e nome sugerido a partir do modelo e das épocas.*

![TL01 — Nome repetido](../assets/11_figma/TL01_configuracao_de_treino/TL01_E2_nome_repetido.png)

*Nome repetido (RA): a interface aponta o nome que já existe e oferece outro.*

### TL02 — Estado do treino

**Responsável:** Mateus Marana Assuena — 22.123.026-1 (fluxo do M03)  
**Objetivo do usuário:** Acompanhar o treino sem ficar presa à tela e, quando ele termina, entender por que terminou e como a configuração se saiu no conjunto de teste.  
**Signos principais:** Estado do treino (treinando, concluído, falhou); progresso (época atual e total); gráficos de treino e validação; motivo do término do treino; causa da falha; IoU (médio e da classe Trilha); acurácia; tempo de inferência; matriz de confusão; conjunto de teste.  
**Origem no MoLIC:** M03 — O02.1 Acompanhar o treino; O02.2 Conferir o resultado do treino; acesso ubíquo "Em que ponto está o treino?" (indicador no topo de todas as telas).

![TL02 — Acompanhar o treino](../assets/11_figma/TL02_estado_do_treino/TL02_acompanhar_o_treino.png)

*Acompanhar o treino (O02.1): época atual de N, barra de progresso, gráficos de treino e validação e aviso de que é possível sair. Na captura, o eixo do gráfico de IoU médio repete valores; isso foi corrigido na interface depois da captura.*

![TL02 — Resultado do treino](../assets/11_figma/TL02_estado_do_treino/TL02_resultado_do_treino.png)

*Resultado do treino (O02.2): motivo do término, métricas e matriz de confusão no conjunto de teste e caminhos para comparar a configuração.*

![TL02 — Treino interrompido](../assets/11_figma/TL02_estado_do_treino/TL02_E1_treino_interrompido.png)

*Treino interrompido (RA): causa, configuração mantida e reinício com o batch size ajustável.*

### TL03 — Entradas e configurações

**Responsável:** Tiago Fagundes dos Santos — 22.123.017-0 (fluxo do M01, também usado no M03)  
**Objetivo do usuário:** Enviar as imagens ou os vídeos do teste e escolher com quais configurações segmentá-los.  
**Signos principais:** Ciclo de testes; imagem; vídeo; formato aceito; configuração; descrição da configuração; situação da configuração (em uso, disponível); métricas no conjunto de teste.  
**Origem no MoLIC:** M01 e M03 — O03.1 Enviar as entradas e escolher as configurações.

![TL03 — Enviar as entradas e escolher as configurações](../assets/11_figma/TL03_entradas_e_configuracoes/TL03_enviar_entradas_e_escolher_configuracoes.png)

*Enviar as entradas e escolher as configurações (O03.1): ciclo de testes, imagens ou vídeos e configurações com descrição, situação e métricas no conjunto de teste. O seletor de arquivos mostra um texto em inglês, do próprio navegador (`PENDENCIAS.md`, INC-70).*

![TL03 — Formato não aceito](../assets/11_figma/TL03_entradas_e_configuracoes/TL03_E1_formato_nao_aceito.png)

*Formato não aceito (AL): o arquivo fora do formato, os formatos aceitos e as opções "Trocar os arquivos" ou "Seguir sem elas".*

### TL04 — Processamento

**Responsável:** Tiago Fagundes dos Santos — 22.123.017-0 (fluxo do M01, também usado no M03)  
**Objetivo do usuário:** Saber em que ponto está a segmentação de cada configuração e o que fazer quando algo falha.  
**Signos principais:** Estado (na fila, processando, concluído, falhou); progresso; causa da falha; sessão; ciclo de testes.  
**Origem no MoLIC:** M01 e M03 — O03.2 Acompanhar o processamento (cena reusada na execução inicial e na comparação).

![TL04 — Acompanhar o processamento](../assets/11_figma/TL04_processamento/TL04_acompanhar_o_processamento.png)

*Acompanhar o processamento (O03.2): uma configuração processando, com progresso, e outra na fila.*

![TL04 — Concluído](../assets/11_figma/TL04_processamento/TL04_concluido.png)

*Concluído: resumo da execução e acesso à comparação na mesma imagem e região.*

![TL04 — Falha na execução](../assets/11_figma/TL04_processamento/TL04_E1_falha_na_execucao.png)

*Falha na execução (RA e CE): falha numa imagem, com "Tentar de novo" ou "Deixar de fora", e falha numa configuração inteira, com o que fazer fora do sistema.*

### TL05 — Resultado e avaliação da imagem

**Responsável:** Tiago Fagundes dos Santos — 22.123.017-0 (fluxo do M01)  
**Objetivo do usuário:** Conferir, imagem a imagem, se a segmentação está certa e registrar a avaliação de cada uma.  
**Signos principais:** Imagem original; máscara; legenda (Trilha, Fora da trilha); sobreposição; transparência; região ampliada; anotação de referência; avaliação da imagem (correta, duvidosa); origem do problema; vídeo com a sobreposição.  
**Origem no MoLIC:** M01 — O04.1 Ver o resultado sobre a imagem; O04.2 Conferir se há métricas; O04.3 Registrar a avaliação da imagem.

![TL05 — Ver o resultado sobre a imagem](../assets/11_figma/TL05_resultado_e_avaliacao/TL05_ver_resultado_sobreposicao.png)

*Ver o resultado sobre a imagem (O04.1): sobreposição com transparência e legenda binária; avaliação registrada (O04.3) e lista das imagens com a avaliação de cada uma.*

![TL05 — Imagem original e máscara lado a lado, com a legenda Trilha × Fora da trilha.](../assets/11_figma/TL05_resultado_e_avaliacao/TL05_imagem_original_e_mascara.png)

*Imagem original e máscara lado a lado, com a legenda Trilha × Fora da trilha.*

![TL05 — Região ampliada](../assets/11_figma/TL05_resultado_e_avaliacao/TL05_regiao_ampliada.png)

*Região ampliada (2,3×), controlada por botões, mouse ou teclado.*

![TL05 — Conferir se há métricas](../assets/11_figma/TL05_resultado_e_avaliacao/TL05_P1_sem_metricas_avaliacao_visual.png)

*Conferir se há métricas (O04.2), com prevenção passiva (PP): sem anotação de referência, não há IoU nem acurácia, e a avaliação é visual.*

![TL05 — Quadro de um vídeo](../assets/11_figma/TL05_resultado_e_avaliacao/TL05_quadro_de_video.png)

*Quadro de um vídeo: navegação entre quadros e download do vídeo com a sobreposição em MP4.*

![TL05 — Estado vazio](../assets/11_figma/TL05_resultado_e_avaliacao/TL05_V1_sem_sessao.png)

*Estado vazio: ainda não há sessão, com o caminho para enviar as imagens.*

### TL06 — Comparação na mesma imagem

**Responsável:** Tiago Fagundes dos Santos — 22.123.017-0 (fluxo do M01, também usado no M03)  
**Objetivo do usuário:** Ver duas ou mais configurações sobre a mesma imagem, na mesma região, para decidir qual delimita melhor a trilha.  
**Signos principais:** Configuração; imagens duvidosas; sobreposição; máscara; região ampliada; avaliação da imagem.  
**Origem no MoLIC:** M01 e M03 — O05.1 Escolher as configurações a comparar; O05.2 Comparar na mesma imagem e região.

![TL06 — Escolher as configurações a comparar](../assets/11_figma/TL06_comparacao_na_mesma_imagem/TL06_escolher_configuracoes_a_comparar.png)

*Escolher as configurações a comparar (O05.1): imagens duvidosas pré-selecionadas e a marca "já executada nestas imagens". A captura mostra "Outras imagens (3)"; na versão atual, a imagem deixada de fora na execução não aparece mais nessa lista.*

![TL06 — Comparar na mesma imagem e região](../assets/11_figma/TL06_comparacao_na_mesma_imagem/TL06_comparar_mesma_imagem_e_regiao.png)

*Comparar na mesma imagem e região (O05.2): imagem original e configurações lado a lado na mesma região ampliada, com a avaliação registrada.*

### TL07 — Desempenho consolidado

**Responsável:** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3 (fluxo do M02, também usado no M03)  
**Objetivo do usuário:** Comparar o desempenho das configurações no conjunto de teste e entender se a diferença entre elas importa, sem que o sistema decida por ela.  
**Signos principais:** Ciclo de testes; conjunto de teste; IoU (médio, da classe Trilha e da classe Fora da trilha); acurácia; tempo de inferência; valor de referência e sua origem; maior valor; diferença entre configurações; matriz de confusão; situação da configuração (candidata, em uso).  
**Origem no MoLIC:** M02 e M03 — O06.1 Escolher as configurações; O06.2 Conferir se a comparação é válida; O06.3 Ler o desempenho de cada configuração; O06.4 Consultar a matriz de confusão; O07.2 Julgar a diferença entre configurações.

![TL07 — Escolher as configurações](../assets/11_figma/TL07_desempenho_consolidado/TL07_escolher_configuracoes_do_ciclo.png)

*Escolher as configurações (O06.1): filtro por ciclo de testes, situação de cada configuração e execução concluída no ciclo.*

![TL07 — Ler o desempenho de cada configuração](../assets/11_figma/TL07_desempenho_consolidado/TL07_ler_desempenho.png)

*Ler o desempenho de cada configuração (O06.3): conferência do conjunto de teste (O06.2), tabela com o valor de referência e sua origem e destaque do maior valor, que não é recomendação.*

![TL07 — As mesmas métricas em gráfico de barras, sempre abaixo da tabela.](../assets/11_figma/TL07_desempenho_consolidado/TL07_ler_desempenho_grafico.png)

*As mesmas métricas em gráfico de barras, sempre abaixo da tabela.*

![TL07 — A diferença importa?](../assets/11_figma/TL07_desempenho_consolidado/TL07_julgar_diferenca.png)

*A diferença importa? (O07.2): diferença entre duas configurações numa métrica e o que a métrica não mostra, sem julgar se a diferença é relevante.*

![TL07 — Consultar a matriz de confusão](../assets/11_figma/TL07_desempenho_consolidado/TL07_matriz_de_confusao.png)

*Consultar a matriz de confusão (O06.4) de cada configuração.*

![TL07 — Configuração sem avaliação no conjunto de teste](../assets/11_figma/TL07_desempenho_consolidado/TL07_E1_sem_avaliacao_no_teste.png)

*Configuração sem avaliação no conjunto de teste (CE): a avaliação deve ser pedida a quem prepara os datasets (tela TL11).*

![TL07 — Conjuntos de teste diferentes](../assets/11_figma/TL07_desempenho_consolidado/TL07_E2_conjuntos_de_teste_diferentes.png)

*Conjuntos de teste diferentes (AL): o conjunto de cada configuração e as opções "Escolher outras configurações" ou "Comparar mesmo assim".*

![TL07 — Execução faltante no ciclo](../assets/11_figma/TL07_desempenho_consolidado/TL07_E3_execucao_faltante_no_ciclo.png)

*Execução faltante no ciclo (CE): qual configuração falta e o que fazer fora do sistema. A captura está deslocada e corta o topo da tela.*

![TL07 — Sem valor de referência](../assets/11_figma/TL07_desempenho_consolidado/TL07_V2_sem_valor_de_referencia.png)

*Sem valor de referência: nenhuma configuração está em uso, e a coluna fica vazia, com a explicação.*

### TL08 — Conclusão

**Responsável:** Equipe (cena compartilhada pelos três MoLIC)  
**Objetivo do usuário:** Registrar a conclusão junto da análise que a sustenta e conferir o que foi registrado.  
**Signos principais:** Conclusão; tipo de conclusão (validação, experimento, recomendação); configuração mais adequada, candidata ou indicada; imagem inconclusiva; origem do problema; ressalva; próximo experimento; ciclo de testes.  
**Origem no MoLIC:** M01, M02 e M03 — O08.1 Informar a conclusão; O08.2 Conferir a conclusão. Uma única conversa: o tipo de conclusão define os campos (Entrega 10, consolidação).

![TL08 — Conclusão de validação](../assets/11_figma/TL08_conclusao/TL08_informar_conclusao_validacao.png)

*Conclusão de validação (O08.1, M01): configuração mais adequada, imagens inconclusivas e imagens com problema de captura. A contagem de imagens no topo inclui a imagem deixada de fora na execução (`PENDENCIAS.md`, INC-70).*

![TL08 — Imagens sem avaliação](../assets/11_figma/TL08_conclusao/TL08_E1_imagens_sem_avaliacao.png)

*Imagens sem avaliação (AL), só na validação: "Avaliá-las antes" ou "Concluir assim mesmo".*

![TL08 — Conclusão do experimento](../assets/11_figma/TL08_conclusao/TL08_informar_conclusao_experimento.png)

*Conclusão do experimento (O08.1, M03): comparação que a sustenta, conclusão, configuração candidata, ressalva e próximo experimento.*

![TL08 — Recomendação](../assets/11_figma/TL08_conclusao/TL08_informar_recomendacao.png)

*Recomendação (O08.1, M02): configuração recomendada e ressalva, ao lado da comparação.*

![TL08 — Conferir a conclusão](../assets/11_figma/TL08_conclusao/TL08_conferir_recomendacao.png)

*Conferir a conclusão (O08.2): o que foi registrado, com "Confirmar" ou "Corrigir". A mesma tela vale para os três tipos de conclusão.*

![TL08 — Corrigir](../assets/11_figma/TL08_conclusao/TL08_corrigir_recomendacao.png)

*Corrigir: o formulário volta preenchido com o que já foi informado.*

### TL09 — Apresentação e decisão

**Responsável:** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3 (fluxo do M02)  
**Objetivo do usuário:** Retomar a análise na reunião, responder às dúvidas da coordenação e registrar a decisão.  
**Signos principais:** Recomendação; ressalva; diferença entre configurações; decisão da coordenação (aceita, aceita com condição, adiada); condição.  
**Origem no MoLIC:** M02 — O09.1 Retomar a análise; O09.2 Responder a uma dúvida (usa a O07.2); O10 Registrar a decisão da coordenação; acesso ubíquo "Apresentar a recomendação" (item do menu).

![TL09 — Retomar a análise](../assets/11_figma/TL09_apresentacao_e_decisao/TL09_retomar_analise.png)

*Retomar a análise (O09.1): recomendação e comparação do ciclo.*

![TL09 — Responder a uma dúvida](../assets/11_figma/TL09_apresentacao_e_decisao/TL09_responder_duvida.png)

*Responder a uma dúvida (O09.2), com a mesma explicação da O07.2.*

![TL09 — Decisão "aceita com condição" sem a condição](../assets/11_figma/TL09_apresentacao_e_decisao/TL09_P1_condicao_obrigatoria.png)

*Decisão "aceita com condição" sem a condição (PA): o botão "Registrar" fica desabilitado até a condição ser informada.*

![TL09 — Decisão registrada](../assets/11_figma/TL09_apresentacao_e_decisao/TL09_decisao_registrada.png)

*Decisão registrada (O10) junto da recomendação.*

![TL09 — Estado vazio](../assets/11_figma/TL09_apresentacao_e_decisao/TL09_V1_sem_recomendacao.png)

*Estado vazio: ainda não há recomendação registrada, com o caminho para registrá-la.*

### TL10 — Explicação dos termos

**Responsável:** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3 (fluxo do M02, disponível em todas as telas)  
**Objetivo do usuário:** Entender o que um termo técnico indica e o que ele não indica, sem sair da tela em que está.  
**Signos principais:** Todos os termos do esquema de signos que aparecem na interface, cada um com "o que indica" e "o que não indica".  
**Origem no MoLIC:** M02 — O07.1 Entender um termo (acesso ubíquo: botão "?" ao lado de cada termo e botão "O que é este termo?" no topo).

![TL10 — Entender um termo](../assets/11_figma/TL10_explicacao_dos_termos/TL10_entender_um_termo.png)

*Entender um termo (O07.1): painel lateral com o que o termo indica e o que não indica e a lista dos outros termos; "Voltar à cena anterior" fecha o painel.*

### TL11 — Datasets

**Responsável:** Equipe (tela de apoio, fora dos MoLIC)  
**Objetivo do usuário:** Preparar os dados de treino e de teste e avaliar no conjunto de teste as configurações que ainda não foram avaliadas.  
**Signos principais:** Datasets de treino; conjunto de teste; situação da configuração (sem avaliação no conjunto de teste).  
**Origem no MoLIC:** Nenhuma cena. A tela existe porque sem ela não há dados para treinar nem para calcular as métricas (ver "Diferenças em relação aos MoLIC").

![TL11 — Estado de cada dataset, montagem do dataset e avaliação no conjunto de teste.](../assets/11_figma/TL11_datasets/TL11_datasets.png)

*Estado de cada dataset, montagem do dataset e avaliação no conjunto de teste.*

![TL11 — Configurações a avaliar no conjunto de teste atual.](../assets/11_figma/TL11_datasets/TL11_datasets_configuracoes_a_avaliar.png)

*Configurações a avaliar no conjunto de teste atual.*

![TL11 — Confirmação antes de remontar o dataset, porque o conjunto de teste pode mudar.](../assets/11_figma/TL11_datasets/TL11_confirmar_remontagem.png)

*Confirmação antes de remontar o dataset, porque o conjunto de teste pode mudar.*

> Documente também estados que muitas equipes esquecem: carregamento, vazio, confirmação, sucesso, erro, permissão negada, cancelamento, desfazer/voltar quando aplicável.

Estados considerados e não implementados: permissão negada (não há perfis nem login; Entrega 1, §8), filtro sem resultados (não há filtros) e cancelamento de execução ou de treino, que não foi modelado nos MoLIC (Entrega 10, "Preparação para o Figma").

## Sistema visual e consistência

| Elemento | Regra adotada | Justificativa |
|---|---|---|
| Tipografia | Fonte padrão do sistema operacional, corpo de 16 px; títulos de tela de 24 px e de seção de 19 px; textos de apoio de 14 px em cinza-escuro | Leitura em tela de notebook (Entrega 8, §1), sem depender de fontes externas, já que a interface roda sem internet |
| Cores | Cores das classes fixas em todas as telas: *Trilha* em amarelo (`#ffb000`) e *Fora da trilha* em azul-escuro (`#2b3a55`), a mesma cor do topo. Uma cor de ação (azul, `#1d4ed8`). Estados com cores próprias: verde para concluído, vermelho para falhou, âmbar para alerta, azul para processando ou treinando e cinza para na fila. Foco em laranja (`#b45309`) | Cores fixas evitam reinterpretar a legenda a cada tela (RQ04). O par amarelo × azul-escuro tem contraste de 6,2:1 e não depende da distinção entre vermelho e verde. As cores dos estados nunca aparecem sozinhas (ver acessibilidade) |
| Componentes | Botão principal para a ação esperada da cena e botão secundário para as alternativas; cartões para agrupar cada subtópico; selo de estado com ícone e texto; diálogo para todo alerta (AL) e captura de erro (CE), com botões que repetem as saídas do MoLIC ("Trocar os arquivos", "Seguir sem elas", "Comparar mesmo assim"); painel lateral para a explicação dos termos; visualizador único para original, máscara e sobreposição, com transparência e região ampliada; tabela de métricas com o gráfico abaixo | O mesmo tipo de fala do MoLIC vira sempre o mesmo componente: cenas viram telas ou cartões, rupturas viram diálogos, acessos ubíquos viram elementos fixos no topo e no menu |
| Feedback | Estados "na fila", "processando" ou "treinando", "concluído" e "falhou", com ícone, texto e barra de progresso; mensagens de falha com a causa em linguagem de usuário e o que fazer; indicador do treino no topo de todas as telas; confirmação de cada registro ("Avaliação registrada", "Conclusão registrada", "Decisão registrada"); rodapé fixo com o que o sistema faz e não faz | Estado visível da execução e do treino (RC04; RQ01). O rodapé atende à diretriz de deixar claro o que o sistema faz e quão bem faz (Entrega 8, §2, interação humano-IA) |
| Navegação | Menu fixo com seis itens: Segmentar imagens, Sessão atual, Treinar uma configuração, Comparar o desempenho, Apresentar a recomendação e Datasets; item atual sublinhado em amarelo; link "←" para a cena anterior no topo de cada tela | Os itens do menu são os pontos de entrada das conversas dos MoLIC (aberturas e acessos ubíquos) |
| Linguagem | Termos do esquema de signos da Entrega 9, com o botão "?" ao lado de cada termo técnico | Um único vocabulário entre as personas (Entrega 8, §2, consistência de termos; RC01) |

## Verificação de acessibilidade básica

Para produto Web, considere critérios pertinentes da WCAG vigente (por exemplo, contraste, foco, tamanho de alvo, texto alternativo e navegação por teclado quando aplicáveis). Para outras plataformas, use as recomendações adequadas ao contexto.

A referência é o nível AA da WCAG 2.2, com os cinco pontos prioritários da Entrega 8 (§2). A verificação foi feita sobre o código da interface (folha de estilos e componentes) e as capturas; os contrastes foram calculados pela fórmula da WCAG a partir das cores da folha de estilos.

| Critério (WCAG 2.2) | Como a interface atende | Situação |
|---|---|---|
| 1.4.1 Uso de cor | A legenda sempre traz o nome da classe; a área de *Trilha* tem contorno branco na sobreposição; os estados combinam cor, ícone e texto; o maior valor é marcado com "▲ maior valor" | Atendido `[F]` |
| 1.4.3 Contraste do texto | Texto principal 15,1:1; texto de apoio 7,2:1; texto dos botões 6,7:1; estados entre 5,6:1 e 6,8:1; menu 11,1:1 (mínimo exigido: 4,5:1). O botão desabilitado (2,5:1) é uma exceção prevista na WCAG | Atendido `[F]` |
| 1.4.11 Contraste não textual | Borda dos campos 4,8:1; contorno de foco entre 4,6:1 e 5,0:1; *Trilha* × *Fora da trilha* 6,2:1; amostras da legenda com contorno escuro (mínimo exigido: 3:1) | Atendido `[F]` |
| 2.1.1 Teclado e 2.4.7 Foco visível | Todos os controles são elementos nativos (botões, links, campos e diálogos); o visualizador recebe foco e responde a "+", "−", "0" e às setas; há link "Pular para o conteúdo"; o foco aparece com contorno de 3 px | Atendido no código `[F]`; percurso completo de cada tarefa só com teclado a conferir na Entrega 13 `[?]` |
| Gráficos com tabela (RC03) | Os gráficos de treino vêm com a "Tabela das épocas"; o gráfico de desempenho fica abaixo da tabela de métricas; a descrição de cada gráfico para leitores de tela aponta a tabela | Atendido `[F]` |
| 2.5.8 Tamanho do alvo | Botões com pelo menos 36 px de altura; o botão "?" dos termos tem 26 px (mínimo exigido: 24 px) | Atendido `[F]` |
| Outros | Idioma da página declarado em português (3.1.1); mensagens de estado anunciadas a leitores de tela (4.1.3); campos inválidos marcados e descritos (3.3.1); animações desligadas quando o sistema pede movimento reduzido | Atendido no código `[F]`; uso com leitor de tela e com ampliação de 200% a conferir na Entrega 13 `[?]` |

## Checklist

- [x] Link do Figma está acessível. *(Não há Figma: o protótipo é a interface implementada, no repositório público do TCC, commit `d11c155`; ver "Acesso ao protótipo".)*
- [x] Há screenshots representativos no repositório. *(44 capturas em `assets/11_figma/`, uma subpasta por tela.)*
- [x] Todos os MoLIC relevantes estão cobertos. *(M01, M02 e M03; ver "Cobertura MoLIC → telas".)*
- [x] Estados de erro, feedback e recuperação foram prototipados. *(Todas as rupturas da Síntese da Entrega 9; a falta de memória no treino está implementada, mas não foi capturada.)*
- [x] Terminologia/signos são consistentes com Entrega 9. *(O único signo novo, o estado "na fila", está em "Diferenças em relação aos MoLIC".)*
- [x] Componentes equivalentes se comportam de forma consistente. *(Exceção conhecida: a prevenção ativa desabilita o botão na TL09, mas não na TL01; a equipe decidiu não alterar, `PENDENCIAS.md`, INC-70.)*
- [x] Fluxos críticos são clicáveis do início ao fim. *(A interface é funcional; os fluxos dos três MoLIC foram percorridos nas capturas.)*
- [x] O protótipo está pronto para inspeção e testes, sem “links mortos” nas tarefas avaliadas. *(Para os testes, a interface roda sobre uma cópia dos dados.)*
- [x] Dashboards, relatórios, históricos, filtros, administração e CRUDs presentes possuem justificativa rastreável. *(Não há dashboard, histórico, filtros, administração nem CRUD. A tela de apoio TL11 e o download do vídeo com a sobreposição estão justificados no `RASTREABILIDADE.md`, §5.)*
- [x] Estados de vazio, processamento, erro e recuperação foram considerados quando pertinentes.
- [x] Resultados técnicos são apresentados de forma interpretável para o perfil de usuário. *(Explicação de cada termo, estado "sem métricas", destaque do maior valor que não é recomendação e diferença entre configurações sem julgamento.)*
- [x] A equipe distingue no protótipo o que é interação simulada e o que é funcionalidade técnica realmente integrada, quando necessário. *(Nada é simulado; os valores das capturas são ilustrativos.)*
