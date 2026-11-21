# Entrega 11 — Protótipo (interface implementada)

**Data:** 16/11/2026 (início) · 16/11/2026 (primeira versão completa) · 20/11/2026 (revisão após feedback)  
**Status:** 🟦 revisada após feedback  
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
**Versão avaliada:** commit `16a5bc195ba7d0f34cc80c386d1c8413e4f1518a` (20/11/2026), a versão única das Entregas 13 e 14. O rodapé de cada tela mostra o commit em uso ("Versão 16a5bc1") e avisa quando há alterações não registradas no git.  
**Última verificação de acesso:** 20/11/2026 (repositório público)

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

O endereço só funciona no próprio computador. Treino, avaliação no conjunto de teste e segmentação rodam enquanto o programa estiver aberto: fechá-lo os interrompe, e a interface mostra o treino ou a avaliação como interrompidos. Para os testes das Entregas 12 a 14, a interface deve rodar sobre uma cópia dos dados, indicada por `SEG_ROOT=<pasta da cópia> python -m app.main`, para não alterar os dados do TCC.

### Evidência no repositório

As 59 capturas das telas e dos estados ficam em `assets/11_figma/`, uma subpasta por tela (TL01 a TL11), e foram feitas na interface do commit `16a5bc1` em 20/11/2026 `[F]`; o rodapé de cada captura mostra a versão. Em cada subpasta, as capturas são numeradas na ordem em que a pessoa percorre o fluxo (por exemplo, `TL02_estado_do_treino/01_na_fila.png` a `05_treino_ou_avaliacao_interrompidos.png`). No texto, uma captura é citada pela tela e pelo número, como TL02/05.

Nas capturas, os valores das métricas são **ilustrativos** e não são resultados do TCC: elas usaram uma cópia reduzida dos dados, com 5 imagens de treino e 6 de teste por dataset (conjunto de teste com 12 imagens) e treinos curtos. As imagens IMG_0401 a IMG_0404 e o vídeo `percurso_trilha.mp4` fazem o papel de imagens de campo, mas vêm do Freiburg Forest com outro nome.

## Cobertura MoLIC → telas

O protótipo implementa os três MoLIC da Entrega 10, revistos em 20/11/2026. Cada tela, de TL01 a TL11, corresponde a cenas dos MoLIC; a TL11 (Datasets) é a conversa "preparar os dados de treino e de teste" (O11) do M03. As cenas reusadas entre diagramas (O03.1, O03.2, O05.2, O06.2, O06.3, O07.2, O08.1 e O08.2) são uma única tela, usada por mais de uma persona. A explicação de um termo (O07.1), que nos MoLIC é um diálogo das cenas com termos técnicos, abre junto do próprio termo em todas as telas (TL10).

| MoLIC | Objetivo | Fluxo/telas | Estados de erro/recuperação | Responsável |
|---|---|---|---|---|
| M01 | O03 | TL03 → TL04 | TL03/01 (PA: entradas e configurações obrigatórias); TL03/03 (AL: formato não aceito); TL04/02 (RA e CE: falha numa imagem e numa configuração inteira) | Tiago Fagundes dos Santos |
| M01 | O04 | TL04 → TL05 | TL05/02 (PP: sem métricas, avaliação visual); TL05/01 (vazio: sem sessão) | Tiago Fagundes dos Santos |
| M01 | O05 | TL05 → TL06 → TL04 → TL06 | TL06/01 (PA: configuração obrigatória); os da TL04 (a execução reusa a O03.2) | Tiago Fagundes dos Santos |
| M01 | O08 | TL05 → TL08 | TL08/02 (AL: imagens sem avaliação); "Corrigir" na conferência (TL08/03) | Tiago Fagundes dos Santos |
| M02 | O06 | TL07 | TL07/01 (PA: configurações obrigatórias); TL07/02 (CE: sem avaliação no conjunto de teste, com acesso à TL11); TL07/03 (AL: conjuntos de teste diferentes); TL07/04 (CE: execução faltante no ciclo); TL07/05 (sem valor de referência) | Henrique Finatti Silveira Belo Trebbi |
| M02 | O07 | TL07 (O07.2) e TL10 (O07.1) | — | Henrique Finatti Silveira Belo Trebbi |
| M02 | O08 | TL07 → TL08 | TL08/07 (PA: configuração indicada obrigatória); "Corrigir" na conferência (TL08/10) | Henrique Finatti Silveira Belo Trebbi |
| M02 | O09 | TL09 | TL09/01 (vazio: sem recomendação) | Henrique Finatti Silveira Belo Trebbi |
| M02 | O10 | TL09 | TL09/04 (PA: condição obrigatória) | Henrique Finatti Silveira Belo Trebbi |
| M03 | O01 | TL01 | TL01/02 (PA: sem dataset de treino); TL01/04 (RA: nome repetido) | Mateus Marana Assuena |
| M03 | O02 | TL02 e indicador do treino no topo | TL02/01 a TL02/03 (PP: o treino continua só com o programa aberto; métricas só depois da avaliação); TL02/05 (RA: treino ou avaliação interrompidos) | Mateus Marana Assuena |
| M03 | O11 | TL11 (item "Datasets" do menu) | TL11/02 (AL: confirmar a remontagem); TL11/05 (PA: configuração obrigatória); TL11/06 (RA e CE: falha na avaliação) | Mateus Marana Assuena |
| M03 | O03, O05 | TL02 → TL03 → TL04 → TL06 | Os da TL03 e da TL04 | Mateus Marana Assuena |
| M03 | O06, O07 | TL06 → TL07 | TL07/02 (CE: sem avaliação no conjunto de teste); TL07/03 (AL: conjuntos de teste diferentes) | Mateus Marana Assuena |
| M03 | O08 | TL07 → TL08 | TL08/04 (PA: conclusão obrigatória); "Corrigir" na conferência (TL08/06) | Mateus Marana Assuena |

A ruptura de treino interrompido por falta de memória, com a sugestão de um batch size menor, está implementada, mas não foi capturada: ela não pode ser provocada no computador usado nas capturas. A TL02/05 mostra a mesma cena de alerta com outra causa (programa fechado).

### Diferenças em relação aos MoLIC

| Diferença | Onde | Motivo |
|---|---|---|
| **Ciclo de testes** informado pela pessoa ao enviar as entradas | TL03 | A Entrega 9 não definia como as execuções são agrupadas em ciclos (`RASTREABILIDADE.md`, §5, 16/11/2026) |
| Da O03.2 para a O04.1 ou para a O05.2 por botão, e não automaticamente | TL04/03 | A pessoa não perde o contexto se estava lendo outra informação da tela |
| A O05.1 não executa de novo uma configuração já executada nas imagens escolhidas | TL06/02 | Evita repetir o mesmo processamento |
| A captura de erro "sem avaliação no conjunto de teste" oferece "Abrir Datasets" além de "Entendi" | TL07/02 | No MoLIC, a conversa termina e a pessoa abre a O11 pelo acesso ubíquo "Datasets"; o botão leva ao mesmo ponto sem passar pelo menu |
| Além da explicação junto de cada termo, o botão "Glossário de termos" do topo abre a lista de todos os termos | TL10/02 | Complementa a O07.1 para quem quer consultar um termo que não está na tela |
| Configurações treinadas antes da interface aparecem sem o histórico das épocas | TL02, TL03 | Esse treino não passou pela interface |

As decisões desta tabela estão registradas no `RASTREABILIDADE.md`, §5 (16/11/2026 e 20/11/2026). As diferenças da primeira versão que os MoLIC passaram a modelar na revisão de 20/11/2026 (tela Datasets, estado "na fila", treino que continua só com o programa aberto, O04.2 sempre sem métricas, falha de uma configuração inteira e confirmação da remontagem) saíram desta tabela.

## Catálogo de telas/estados

Cada tela traz o responsável, o objetivo do usuário, os signos principais (Entrega 9, §4), a origem no MoLIC e as capturas dos estados implementados, na ordem do fluxo. As capturas são da interface do commit `16a5bc1`; os valores das métricas são ilustrativos (ver "Acesso ao protótipo"). Em todas as telas, um campo obrigatório tem o mesmo comportamento: o botão fica desabilitado, a mensagem "Falta:" aparece junto do campo e "Para continuar:" junto do botão.

### TL01 — Configuração de treino

**Responsável:** Mateus Marana Assuena — 22.123.026-1 (fluxo do M03)  
**Objetivo do usuário:** Definir o modelo e os parâmetros de treino de uma nova configuração, dar um nome a ela e iniciar o treino.  
**Signos principais:** Modelo; parâmetros de treino (épocas, early stopping, paciência, datasets de treino, batch size, geração de gráficos); valor padrão; dataset montado; nome da configuração.  
**Origem no MoLIC:** M03 — O01.1 Escolher o modelo e os parâmetros; O01.2 Nomear a configuração.

![TL01/01 — Escolher o modelo e os parâmetros](../assets/11_figma/TL01_configuracao_de_treino/01_escolher_modelo_e_parametros.png)

*TL01/01 — Escolher o modelo e os parâmetros (O01.1): valores padrão do TCC já preenchidos, ajuda em cada parâmetro e aviso de que os parâmetros internos do treino são fixos. Só os datasets montados podem ser escolhidos; o CaSSeD aparece desabilitado, com o caminho para montá-lo na tela Datasets.*

![TL01/02 — Sem dataset de treino](../assets/11_figma/TL01_configuracao_de_treino/02_campo_obrigatorio_sem_dataset.png)

*TL01/02 — Sem dataset de treino (PA): "Continuar" fica desabilitado, e a interface diz o que falta junto do campo e do botão.*

![TL01/03 — Nomear a configuração](../assets/11_figma/TL01_configuracao_de_treino/03_nomear_configuracao.png)

*TL01/03 — Nomear a configuração (O01.2): resumo dos parâmetros e nome sugerido a partir do modelo e das épocas, que nunca repete um nome existente.*

![TL01/04 — Nome repetido](../assets/11_figma/TL01_configuracao_de_treino/04_nome_repetido.png)

*TL01/04 — Nome editado repetido (RA): a interface marca o campo e pede outro nome.*

### TL02 — Estado do treino

**Responsável:** Mateus Marana Assuena — 22.123.026-1 (fluxo do M03)  
**Objetivo do usuário:** Acompanhar o treino sem ficar presa à tela e, quando ele termina, entender por que terminou e como a configuração se saiu no conjunto de teste.  
**Signos principais:** Estado do treino (na fila, treinando, concluído, falhou); progresso (época atual e total); gráficos de treino e validação; avaliação no conjunto de teste e seu estado; motivo do término do treino; causa da falha; IoU (médio e da classe Trilha); acurácia; tempo de inferência; matriz de confusão; conjunto de teste.  
**Origem no MoLIC:** M03 — O02.1 Acompanhar o treino; O02.2 Conferir o resultado do treino; acesso ubíquo "Em que ponto está o treino?" (indicador no topo de todas as telas); encerramento temporário (a pessoa pode sair da tela).

![TL02/01 — Treino na fila](../assets/11_figma/TL02_estado_do_treino/01_na_fila.png)

*TL02/01 — Treino na fila (O02.1): o treino começa quando o processamento anterior terminar. O aviso de que o treino continua só enquanto o programa estiver aberto (PP) e a mensagem "Métricas disponíveis após a avaliação no conjunto de teste" aparecem desde o início.*

![TL02/02 — Treinando](../assets/11_figma/TL02_estado_do_treino/02_treinando.png)

*TL02/02 — Treinando (O02.1): época atual de N, barra de progresso e gráficos de treino e validação, com a tabela das épocas.*

![TL02/03 — Avaliação no conjunto de teste](../assets/11_figma/TL02_estado_do_treino/03_avaliando_no_conjunto_de_teste.png)

*TL02/03 — Treino concluído e avaliação no conjunto de teste na fila: o sistema avalia a configuração automaticamente, e as métricas ainda não aparecem.*

![TL02/04 — Resultado do treino](../assets/11_figma/TL02_estado_do_treino/04_metricas_apos_avaliacao.png)

*TL02/04 — Resultado do treino (O02.2), depois da avaliação: motivo do término, métricas e matriz de confusão no conjunto de teste e as saídas "Comparar com outra configuração no vídeo" e "Concluir por agora".*

![TL02/05 — Treino ou avaliação interrompidos](../assets/11_figma/TL02_estado_do_treino/05_treino_ou_avaliacao_interrompidos.png)

*TL02/05 — Treino ou avaliação interrompidos (RA): causa, etapa, configuração mantida, ajuste sugerido e "Reiniciar com o ajuste", com o batch size editável.*

### TL03 — Entradas e configurações

**Responsável:** Tiago Fagundes dos Santos — 22.123.017-0 (fluxo do M01, também usado no M03)  
**Objetivo do usuário:** Enviar as imagens ou os vídeos do teste e escolher com quais configurações segmentá-los.  
**Signos principais:** Ciclo de testes; imagem; vídeo; formato aceito; configuração; descrição da configuração; situação da configuração (em uso, disponível); métricas no conjunto de teste.  
**Origem no MoLIC:** M01 e M03 — O03.1 Enviar as entradas e escolher as configurações.

![TL03/01 — Campos obrigatórios](../assets/11_figma/TL03_entradas_e_configuracoes/01_campo_obrigatorio.png)

*TL03/01 — Sem entradas e sem configuração (PA): "Executar" fica desabilitado. O seletor de arquivos tem textos em português e informa os formatos aceitos.*

![TL03/02 — Enviar as entradas e escolher as configurações](../assets/11_figma/TL03_entradas_e_configuracoes/02_enviar_entradas_e_escolher_configuracoes.png)

*TL03/02 — Enviar as entradas e escolher as configurações (O03.1): ciclo de testes, arquivos escolhidos (com "Retirar") e configurações com descrição, situação e métricas no conjunto de teste.*

![TL03/03 — Arquivos fora do formato aceito](../assets/11_figma/TL03_entradas_e_configuracoes/03_arquivos_fora_do_formato.png)

*TL03/03 — Arquivos fora do formato aceito (AL): quais arquivos são, os formatos aceitos e as opções "Trocar os arquivos" ou "Seguir sem eles"; os outros arquivos entram na fila.*

### TL04 — Processamento

**Responsável:** Tiago Fagundes dos Santos — 22.123.017-0 (fluxo do M01, também usado no M03)  
**Objetivo do usuário:** Saber em que ponto está a segmentação de cada configuração e o que fazer quando algo falha.  
**Signos principais:** Estado (na fila, processando, concluído, falhou); progresso; causa da falha; sessão; ciclo de testes.  
**Origem no MoLIC:** M01 e M03 — O03.2 Acompanhar o processamento (cena reusada na execução inicial e na comparação).

![TL04/01 — Na fila e processando](../assets/11_figma/TL04_processamento/01_na_fila_e_processando.png)

*TL04/01 — Acompanhar o processamento (O03.2): uma configuração processando, com progresso, e outra na fila; aviso de que a execução continua enquanto o programa estiver aberto.*

![TL04/02 — Falha na execução](../assets/11_figma/TL04_processamento/02_falha_na_imagem_e_na_configuracao.png)

*TL04/02 — Falha na execução: falha numa imagem, com a causa, "Tentar de novo" ou "Deixar de fora" (RA), e falha numa configuração inteira, com o que fazer fora do sistema (CE).*

![TL04/03 — Concluído](../assets/11_figma/TL04_processamento/03_concluido.png)

*TL04/03 — Concluído: resumo da execução e o caminho para a próxima cena; com mais de uma configuração (precondição "comparação"), "Comparar na mesma imagem e região".*

### TL05 — Resultado e avaliação da imagem

**Responsável:** Tiago Fagundes dos Santos — 22.123.017-0 (fluxo do M01)  
**Objetivo do usuário:** Conferir, imagem a imagem, se a segmentação está certa e registrar a avaliação de cada uma.  
**Signos principais:** Imagem original; máscara; legenda (Trilha, Fora da trilha); sobreposição; transparência; região ampliada; anotação de referência; avaliação da imagem (correta, duvidosa); origem do problema; vídeo com a sobreposição.  
**Origem no MoLIC:** M01 — O04.1 Ver o resultado sobre a imagem; O04.2 Conferir se há métricas; O04.3 Registrar a avaliação da imagem.

![TL05/01 — Sem sessão](../assets/11_figma/TL05_resultado_e_avaliacao/01_sem_sessao.png)

*TL05/01 — Estado vazio: ainda não há sessão, com o caminho para enviar as imagens.*

![TL05/02 — Sobreposição e sem métricas](../assets/11_figma/TL05_resultado_e_avaliacao/02_sobreposicao_e_sem_metricas.png)

*TL05/02 — Ver o resultado sobre a imagem (O04.1) e conferir se há métricas (O04.2): sobreposição com transparência e legenda binária; "Sem métricas: avaliação visual" (PP), com o caminho para o desempenho consolidado.*

![TL05/03 — Imagem original e máscara](../assets/11_figma/TL05_resultado_e_avaliacao/03_imagem_original_e_mascara.png)

*TL05/03 — Imagem original e máscara lado a lado, com a legenda Trilha × Fora da trilha.*

![TL05/04 — Região ampliada](../assets/11_figma/TL05_resultado_e_avaliacao/04_regiao_ampliada.png)

*TL05/04 — Região ampliada, controlada por botões, mouse ou teclado.*

![TL05/05 — Avaliação registrada](../assets/11_figma/TL05_resultado_e_avaliacao/05_avaliacao_registrada.png)

*TL05/05 — Registrar a avaliação da imagem (O04.3): imagem duvidosa por problema no modelo; a lista de imagens mostra a avaliação, e "Comparar as duvidosas" fica disponível.*

![TL05/06 — Quadro de vídeo](../assets/11_figma/TL05_resultado_e_avaliacao/06_quadro_de_video.png)

*TL05/06 — Quadro de um vídeo: navegação entre quadros e download do vídeo com a sobreposição em MP4.*

### TL06 — Comparação na mesma imagem

**Responsável:** Tiago Fagundes dos Santos — 22.123.017-0 (fluxo do M01, também usado no M03)  
**Objetivo do usuário:** Ver duas ou mais configurações sobre a mesma imagem, na mesma região, para decidir qual delimita melhor a trilha.  
**Signos principais:** Configuração; imagens duvidosas; sobreposição; máscara; região ampliada; avaliação da imagem.  
**Origem no MoLIC:** M01 e M03 — O05.1 Escolher as configurações a comparar; O05.2 Comparar na mesma imagem e região.

![TL06/01 — Configuração obrigatória](../assets/11_figma/TL06_comparacao_na_mesma_imagem/01_campo_obrigatorio.png)

*TL06/01 — Escolher as configurações a comparar (O05.1) sem nenhuma configuração escolhida (PA): imagens duvidosas pré-selecionadas e "Executar nas imagens escolhidas" desabilitado.*

![TL06/02 — Escolher as configurações a comparar](../assets/11_figma/TL06_comparacao_na_mesma_imagem/02_escolher_configuracoes_a_comparar.png)

*TL06/02 — Escolher as configurações a comparar (O05.1): a marca "Já executada nestas imagens" evita repetir uma execução.*

![TL06/03 — Comparar na mesma região](../assets/11_figma/TL06_comparacao_na_mesma_imagem/03_comparar_na_mesma_regiao.png)

*TL06/03 — Comparar na mesma imagem e região (O05.2): imagem original e sobreposição de cada configuração na mesma região ampliada, com a avaliação registrada.*

![TL06/04 — Comparar as máscaras](../assets/11_figma/TL06_comparacao_na_mesma_imagem/04_comparar_mascaras.png)

*TL06/04 — A mesma comparação com as máscaras; "Comparar as métricas no conjunto de teste" leva à TL07 (caminho do M03).*

### TL07 — Desempenho consolidado

**Responsável:** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3 (fluxo do M02, também usado no M03)  
**Objetivo do usuário:** Comparar o desempenho das configurações no conjunto de teste e entender se a diferença entre elas importa, sem que o sistema decida por ela.  
**Signos principais:** Ciclo de testes; conjunto de teste; avaliação no conjunto de teste; IoU (médio, da classe Trilha e da classe Fora da trilha); acurácia; tempo de inferência; valor de referência e sua origem (configuração em uso, a última executada); maior valor; diferença entre configurações; matriz de confusão; situação da configuração (disponível, em uso).  
**Origem no MoLIC:** M02 e M03 — O06.1 Escolher as configurações; O06.2 Conferir se a comparação é válida; O06.3 Ler o desempenho de cada configuração; O06.4 Consultar a matriz de confusão; O07.2 Julgar a diferença entre configurações.

![TL07/01 — Configurações obrigatórias](../assets/11_figma/TL07_desempenho_consolidado/01_escolher_configuracoes_campo_obrigatorio.png)

*TL07/01 — Escolher as configurações (O06.1) sem nenhuma escolhida (PA): "Comparar as selecionadas" desabilitado.*

![TL07/02 — Configuração sem avaliação no conjunto de teste](../assets/11_figma/TL07_desempenho_consolidado/02_sem_avaliacao_no_teste.png)

*TL07/02 — Configuração sem avaliação no conjunto de teste (CE): quais configurações são e que a avaliação é feita na tela Datasets; "Abrir Datasets" leva à TL11.*

![TL07/03 — Conjuntos de teste diferentes](../assets/11_figma/TL07_desempenho_consolidado/03_conjuntos_de_teste_diferentes.png)

*TL07/03 — Conjuntos de teste diferentes (AL, O06.2): o conjunto de cada configuração e as opções "Escolher outras configurações" ou "Comparar mesmo assim". Vindo da TL06, a primeira opção é "Voltar aos quadros".*

![TL07/04 — Execução faltante no ciclo](../assets/11_figma/TL07_desempenho_consolidado/04_execucao_faltante_no_ciclo.png)

*TL07/04 — Configuração sem execução no ciclo (CE): qual configuração falta e que a execução deve ser pedida fora do sistema.*

![TL07/05 — Sem valor de referência](../assets/11_figma/TL07_desempenho_consolidado/05_sem_valor_de_referencia.png)

*TL07/05 — Sem valor de referência: nenhuma configuração foi executada, e a coluna fica vazia, com a explicação.*

![TL07/06 — Valor de referência e maior valor](../assets/11_figma/TL07_desempenho_consolidado/06_referencia_e_maior_valor.png)

*TL07/06 — Ler o desempenho de cada configuração (O06.3): conferência do conjunto de teste (O06.2), tabela com o valor de referência e sua origem e o destaque "maior valor · não é recomendação".*

![TL07/07 — Gráfico](../assets/11_figma/TL07_desempenho_consolidado/07_grafico.png)

*TL07/07 — As mesmas métricas em gráfico de barras, abaixo da tabela.*

![TL07/08 — A diferença importa?](../assets/11_figma/TL07_desempenho_consolidado/08_a_diferenca_importa.png)

*TL07/08 — A diferença importa? (O07.2): diferença entre duas configurações numa métrica e o que a métrica não mostra, sem julgar se a diferença é relevante.*

![TL07/09 — Matriz de confusão](../assets/11_figma/TL07_desempenho_consolidado/09_matriz_de_confusao.png)

*TL07/09 — Consultar a matriz de confusão (O06.4) de cada configuração.*

### TL08 — Conclusão

**Responsável:** Equipe (cena compartilhada pelos três MoLIC)  
**Objetivo do usuário:** Registrar a conclusão junto da análise que a sustenta e conferir o que foi registrado.  
**Signos principais:** Conclusão; tipo de conclusão (validação, experimento, recomendação); configuração mais adequada, candidata ou indicada; imagem inconclusiva; origem do problema; ressalva; próximo experimento; ciclo de testes.  
**Origem no MoLIC:** M01, M02 e M03 — O08.1 Informar a conclusão; O08.2 Conferir a conclusão. Uma única conversa: o tipo de conclusão define os campos (Entrega 10, consolidação).

![TL08/01 — Conclusão de validação](../assets/11_figma/TL08_conclusao/01_informar_conclusao_validacao.png)

*TL08/01 — Conclusão de validação (O08.1, M01): configuração mais adequada, imagens inconclusivas e imagens com problema de captura; a contagem de imagens é a da sessão.*

![TL08/02 — Imagens sem avaliação](../assets/11_figma/TL08_conclusao/02_imagens_sem_avaliacao.png)

*TL08/02 — Imagens sem avaliação (AL), só na validação: "Avaliá-las antes" ou "Concluir assim mesmo".*

![TL08/03 — Conferir a conclusão de validação](../assets/11_figma/TL08_conclusao/03_conferir_conclusao_validacao.png)

*TL08/03 — Conferir a conclusão (O08.2): o que foi registrado, com "Confirmar" ou "Corrigir".*

![TL08/04 — Conclusão do experimento obrigatória](../assets/11_figma/TL08_conclusao/04_experimento_campo_obrigatorio.png)

*TL08/04 — Conclusão do experimento (O08.1, M03) sem o texto da conclusão (PA): "Registrar" desabilitado; a comparação que sustenta a conclusão fica acima do formulário.*

![TL08/05 — Conclusão do experimento](../assets/11_figma/TL08_conclusao/05_informar_conclusao_experimento.png)

*TL08/05 — Conclusão do experimento preenchida: conclusão, configuração candidata, ressalva e próximo experimento.*

![TL08/06 — Conferir a conclusão do experimento](../assets/11_figma/TL08_conclusao/06_conferir_conclusao_experimento.png)

*TL08/06 — Conferir a conclusão do experimento (O08.2), registrada junto da comparação.*

![TL08/07 — Recomendação obrigatória](../assets/11_figma/TL08_conclusao/07_recomendacao_campo_obrigatorio.png)

*TL08/07 — Recomendação (O08.1, M02) sem a configuração indicada (PA): "Registrar" desabilitado.*

![TL08/08 — Recomendação](../assets/11_figma/TL08_conclusao/08_informar_recomendacao.png)

*TL08/08 — Recomendação preenchida: ciclo de testes, configuração recomendada e ressalva, ao lado da comparação.*

![TL08/09 — Conferir a recomendação](../assets/11_figma/TL08_conclusao/09_conferir_recomendacao.png)

*TL08/09 — Conferir a recomendação (O08.2), com "Confirmar" ou "Corrigir".*

![TL08/10 — Corrigir a recomendação](../assets/11_figma/TL08_conclusao/10_corrigir_recomendacao.png)

*TL08/10 — Corrigir: o formulário volta preenchido com o que já foi informado, com "Registrar a correção".*

### TL09 — Apresentação e decisão

**Responsável:** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3 (fluxo do M02)  
**Objetivo do usuário:** Retomar a análise na reunião, responder às dúvidas da coordenação e registrar a decisão.  
**Signos principais:** Recomendação; ressalva; diferença entre configurações; decisão da coordenação (aceita, aceita com condição, adiada); condição.  
**Origem no MoLIC:** M02 — O09.1 Retomar a análise; O09.2 Responder a uma dúvida (usa a O07.2); O10 Registrar a decisão da coordenação; acesso ubíquo "Apresentar a recomendação" (item do menu).

![TL09/01 — Sem recomendação](../assets/11_figma/TL09_apresentacao_e_decisao/01_sem_recomendacao.png)

*TL09/01 — Estado vazio: ainda não há recomendação registrada, com o caminho para registrá-la.*

![TL09/02 — Retomar a análise](../assets/11_figma/TL09_apresentacao_e_decisao/02_retomar_analise.png)

*TL09/02 — Retomar a análise (O09.1): recomendação do ciclo e comparação das configurações.*

![TL09/03 — Responder a uma dúvida](../assets/11_figma/TL09_apresentacao_e_decisao/03_responder_duvida.png)

*TL09/03 — Responder a uma dúvida (O09.2), com a mesma explicação da O07.2.*

![TL09/04 — Condição obrigatória](../assets/11_figma/TL09_apresentacao_e_decisao/04_condicao_obrigatoria.png)

*TL09/04 — Decisão "aceita com condição" sem a condição (PA): "Registrar" desabilitado, com o mesmo comportamento das outras telas.*

![TL09/05 — Decisão registrada](../assets/11_figma/TL09_apresentacao_e_decisao/05_decisao_registrada.png)

*TL09/05 — Decisão registrada (O10) junto da recomendação, com a condição.*

### TL10 — Explicação dos termos

**Responsável:** Equipe (diálogo O07.1 dos três MoLIC)  
**Objetivo do usuário:** Entender o que um termo técnico indica e o que ele não indica, sem sair da tela em que está.  
**Signos principais:** Todos os termos do esquema de signos que aparecem na interface, cada um com "o que indica" e "o que não indica".  
**Origem no MoLIC:** M01, M02 e M03 — diálogo `d+u: o que é este termo? (O07.1)` nas cenas com termos técnicos.

![TL10/01 — Explicação no próprio termo](../assets/11_figma/TL10_explicacao_dos_termos/01_explicacao_no_proprio_termo.png)

*TL10/01 — Explicação no próprio termo (O07.1): o botão "?" abre, junto do termo, o que ele indica e o que não indica; "Fechar" (ou Esc) devolve a pessoa ao mesmo ponto da tela.*

![TL10/02 — Glossário de termos](../assets/11_figma/TL10_explicacao_dos_termos/02_glossario_complementar.png)

*TL10/02 — Glossário de termos, aberto pelo botão do topo: lista de todos os termos, complementar à explicação no ponto de uso.*

### TL11 — Datasets

**Responsável:** Mateus Marana Assuena — 22.123.026-1 (fluxo do M03)  
**Objetivo do usuário:** Preparar os dados de treino e de teste e avaliar no conjunto de teste as configurações que ainda não foram avaliadas.  
**Signos principais:** Dataset; arquivos brutos; imagens de treino e de teste; conjunto de teste atual; dataset montado; avaliação no conjunto de teste (sem avaliação no conjunto de teste); estado (na fila, processando, concluída, falhou); causa da falha.  
**Origem no MoLIC:** M03, conversa "preparar os dados de treino e de teste" — acesso ubíquo "Datasets" (item do menu); O11.1 Conferir os datasets; alerta "Confirmar a remontagem"; O11.2 Montar o dataset; O11.3 Avaliar as configurações no conjunto de teste.

![TL11/01 — Conferir os datasets](../assets/11_figma/TL11_datasets/01_conferir_datasets.png)

*TL11/01 — Conferir os datasets (O11.1): arquivos brutos, imagens de treino e de teste de cada dataset, conjunto de teste atual e configurações sem avaliação no conjunto de teste.*

![TL11/02 — Confirmar a remontagem](../assets/11_figma/TL11_datasets/02_confirmar_remontagem.png)

*TL11/02 — Confirmar a remontagem (AL): o conjunto de teste pode mudar, e as configurações avaliadas terão de ser avaliadas de novo; "Cancelar" ou "Confirmar".*

![TL11/03 — Montagem na fila](../assets/11_figma/TL11_datasets/03_montagem_na_fila.png)

*TL11/03 — Montar o dataset (O11.2): a montagem fica na fila enquanto outra avaliação é processada.*

![TL11/04 — Dataset montado](../assets/11_figma/TL11_datasets/04_dataset_montado.png)

*TL11/04 — "Dataset montado", com a data e os datasets da última montagem; a conversa volta à conferência dos datasets.*

![TL11/05 — Avaliar as selecionadas](../assets/11_figma/TL11_datasets/05_avaliar_selecionadas.png)

*TL11/05 — Avaliar as configurações no conjunto de teste (O11.3): a pessoa escolhe entre as configurações sem avaliação. Sem nenhuma escolhida, "Avaliar as selecionadas" fica desabilitado (PA), como na TL11/04.*

![TL11/06 — Falha na avaliação](../assets/11_figma/TL11_datasets/06_falha_avaliacao.png)

*TL11/06 — Falha na avaliação no conjunto de teste (RA e CE): a causa, o que fazer fora do sistema e "Tentar de novo".*

![TL11/07 — Avaliando](../assets/11_figma/TL11_datasets/07_avaliando.png)

*TL11/07 — Avaliação processando, depois de "Tentar de novo".*

![TL11/08 — Avaliação concluída](../assets/11_figma/TL11_datasets/08_avaliacao_concluida.png)

*TL11/08 — "Avaliação concluída": as configurações avaliadas podem entrar na comparação de desempenho (TL07).*

> Documente também estados que muitas equipes esquecem: carregamento, vazio, confirmação, sucesso, erro, permissão negada, cancelamento, desfazer/voltar quando aplicável.

Estados considerados e não implementados: permissão negada (não há perfis nem login; Entrega 1, §8), filtro sem resultados (não há filtros) e cancelamento de execução, de treino ou de avaliação, que não foi modelado nos MoLIC (Entrega 10, "Preparação para o Figma"). A confirmação de ação destrutiva é a da remontagem do dataset (TL11/02).

## Sistema visual e consistência

| Elemento | Regra adotada | Justificativa |
|---|---|---|
| Tipografia | Fonte padrão do sistema operacional, corpo de 16 px; títulos de tela de 24 px e de seção de 19 px; textos de apoio de 14 px em cinza-escuro | Leitura em tela de notebook (Entrega 8, §1), sem depender de fontes externas, já que a interface roda sem internet |
| Cores | Cores das classes fixas em todas as telas: *Trilha* em amarelo (`#ffb000`) e *Fora da trilha* em azul-escuro (`#2b3a55`), a mesma cor do topo. Uma cor de ação (azul, `#1d4ed8`). Estados com cores próprias: verde para concluído, vermelho para falhou, âmbar para alerta e para o que falta num campo obrigatório, azul para processando ou treinando e cinza para na fila. Foco em laranja (`#b45309`) | Cores fixas evitam reinterpretar a legenda a cada tela (RQ04). O par amarelo × azul-escuro tem contraste de 6,2:1 e não depende da distinção entre vermelho e verde. As cores dos estados nunca aparecem sozinhas (ver acessibilidade) |
| Componentes | Botão principal para a ação esperada da cena e botão secundário para as alternativas; cartões para agrupar cada subtópico; selo de estado com ícone e texto; diálogo para todo alerta (AL) e captura de erro (CE), com botões que repetem as saídas do MoLIC ("Trocar os arquivos", "Seguir sem eles", "Comparar mesmo assim", "Confirmar" e "Cancelar" na remontagem); quadro junto do termo para a explicação (O07.1) e painel lateral para o glossário; visualizador único para original, máscara e sobreposição, com transparência e região ampliada; tabela de métricas com o gráfico abaixo | O mesmo tipo de fala do MoLIC vira sempre o mesmo componente: cenas viram telas ou cartões, rupturas viram diálogos, diálogos de uma cena ficam na própria tela e acessos ubíquos viram elementos fixos no topo e no menu |
| Prevenção (PA) | Em todo campo obrigatório, o botão da ação fica desabilitado; "Falta: …" aparece junto do campo e "Para continuar: …" junto do botão, desde que a tela abre (TL01, TL03, TL06, TL07, TL08, TL09 e TL11) | O mesmo comportamento para componentes equivalentes; a pessoa vê o que falta antes de tentar continuar (parecer da Entrega 11, correção 3) |
| Feedback | Estados "na fila", "processando" ou "treinando", "concluído" e "falhou", com ícone, texto e barra de progresso; mensagens de falha com a causa em linguagem de usuário e o que fazer; indicador do treino e da avaliação no topo de todas as telas; aviso de que o treino e a execução continuam só com o programa aberto; confirmação de cada registro ("Avaliação registrada", "Conclusão registrada", "Decisão registrada", "Dataset montado", "Avaliação concluída"); rodapé fixo com o que o sistema faz e não faz e com a versão (commit) | Estado visível do treino, da avaliação e da execução (RC04; RQ01). O rodapé atende à diretriz de deixar claro o que o sistema faz e quão bem faz (Entrega 8, §2, interação humano-IA), e a versão liga capturas, documentação e avaliação ao mesmo commit |
| Navegação | Menu fixo com seis itens: Segmentar imagens, Sessão atual, Treinar uma configuração, Comparar o desempenho, Apresentar a recomendação e Datasets; item atual sublinhado em amarelo; botão "Glossário de termos" no topo; link "←" para a cena anterior no topo de cada tela | Os itens do menu são os pontos de entrada das conversas dos MoLIC (aberturas e acessos ubíquos) |
| Linguagem | Termos do esquema de signos da Entrega 9, com o botão "?" ao lado de cada termo técnico | Um único vocabulário entre as personas (Entrega 8, §2, consistência de termos; RC01) |

## Verificação de acessibilidade básica

Para produto Web, considere critérios pertinentes da WCAG vigente (por exemplo, contraste, foco, tamanho de alvo, texto alternativo e navegação por teclado quando aplicáveis). Para outras plataformas, use as recomendações adequadas ao contexto.

A referência é o nível AA da WCAG 2.2, com os cinco pontos prioritários da Entrega 8 (§2). A verificação foi feita sobre o código da interface (folha de estilos e componentes) e as capturas; os contrastes foram calculados pela fórmula da WCAG a partir das cores da folha de estilos. Os elementos novos do commit `16a5bc1` (explicação junto do termo, mensagens de campo obrigatório e versão no rodapé) usam as mesmas cores e foram conferidos no código.

| Critério (WCAG 2.2) | Como a interface atende | Situação |
|---|---|---|
| 1.4.1 Uso de cor | A legenda sempre traz o nome da classe; a área de *Trilha* tem contorno branco na sobreposição; os estados combinam cor, ícone e texto; o maior valor é marcado com "▲ maior valor"; o que falta num campo vem escrito ("Falta: …") | Atendido `[F]` |
| 1.4.3 Contraste do texto | Texto principal 15,1:1; texto de apoio 7,2:1; texto dos botões 6,7:1; estados e mensagens "Falta:" entre 5,6:1 e 6,8:1; menu 11,1:1 (mínimo exigido: 4,5:1). O botão desabilitado (2,5:1) é uma exceção prevista na WCAG, e o motivo vem escrito ao lado dele | Atendido `[F]` |
| 1.4.11 Contraste não textual | Borda dos campos 4,8:1; contorno de foco entre 4,6:1 e 5,0:1; *Trilha* × *Fora da trilha* 6,2:1; amostras da legenda com contorno escuro (mínimo exigido: 3:1) | Atendido `[F]` |
| 2.1.1 Teclado e 2.4.7 Foco visível | Todos os controles são elementos nativos (botões, links, campos e diálogos); o visualizador recebe foco e responde a "+", "−", "0" e às setas; a explicação de um termo recebe o foco ao abrir e fecha com Esc; há link "Pular para o conteúdo"; o foco aparece com contorno de 3 px | Atendido no código `[F]`; percursos completos a conferir na Entrega 13 (tabela abaixo) `[?]` |
| 3.3.1 e 3.3.2 Identificação de erros, rótulos e instruções | Campo obrigatório descrito pela mensagem "Falta: …", ligada ao campo para leitores de tela; resumo "Para continuar: …" ligado ao botão desabilitado e anunciado quando muda | Atendido no código `[F]` |
| Gráficos com tabela (RC03) | Os gráficos de treino vêm com a "Tabela das épocas"; o gráfico de desempenho fica abaixo da tabela de métricas; a descrição de cada gráfico para leitores de tela aponta a tabela | Atendido `[F]` |
| 2.5.8 Tamanho do alvo | Botões com pelo menos 36 px de altura; o botão "?" dos termos tem 26 px (mínimo exigido: 24 px) | Atendido `[F]` |
| Outros | Idioma da página declarado em português (3.1.1); mensagens de estado anunciadas a leitores de tela (4.1.3); animações desligadas quando o sistema pede movimento reduzido | Atendido no código `[F]`; uso com leitor de tela e com ampliação de 200% a conferir na Entrega 13 `[?]` |

### Percursos completos a confirmar

A inspeção do código não demonstra que uma pessoa conclui as tarefas só com teclado, com ampliação ou com leitor de tela. Os percursos abaixo, das tarefas críticas, são feitos de ponta a ponta na Entrega 13, na versão `16a5bc1`, só com teclado e com ampliação de 200% do navegador e, quando possível, com um leitor de tela `[?]`. Em cada um, confere-se: o foco fica visível e segue a ordem lógica da tela; as mensagens de estado e os diálogos são anunciados; o foco volta a um ponto previsível quando um diálogo fecha; gráficos e comparações continuam compreensíveis sem depender só de cor ou de posição.

| Percurso | Telas | Pontos de atenção |
|---|---|---|
| Configurar e iniciar um treino | TL01 → TL02 | Campo obrigatório dos datasets (TL01/02); nome repetido (TL01/04); anúncio dos estados do treino e da avaliação |
| Enviar entradas e recuperar-se de um formato inválido | TL03 → TL04 | Seletor de arquivos; diálogo "Arquivos fora do formato aceito" (TL03/03); estados na fila, processando e falhou (TL04/02) |
| Avaliar as imagens | TL05 | Visualizador e região ampliada pelo teclado; "Sem métricas" (TL05/02); registro da avaliação |
| Comparar configurações | TL06 → TL07 | Comparação lado a lado; tabela com "maior valor"; diálogos de CE e AL (TL07/02, TL07/03); explicação de um termo (TL10/01) |
| Registrar uma conclusão | TL08 | Campos obrigatórios (TL08/04, TL08/07); alerta de imagens sem avaliação (TL08/02); "Corrigir" |
| Apresentar uma recomendação | TL09 | "A diferença importa?" (TL09/03); condição obrigatória (TL09/04) |
| Preparar os dados e avaliar as configurações | TL11 | Confirmação da remontagem (TL11/02); estados da montagem e da avaliação; falha (TL11/06) |

## Checklist

- [x] Link do Figma está acessível. *(Não há Figma: o protótipo é a interface implementada, no repositório público do TCC, commit `16a5bc1`; ver "Acesso ao protótipo".)*
- [x] Há screenshots representativos no repositório. *(59 capturas do commit `16a5bc1` em `assets/11_figma/`, uma subpasta por tela, numeradas na ordem do fluxo e com a versão no rodapé.)*
- [x] Todos os MoLIC relevantes estão cobertos. *(M01, M02 e M03, inclusive a preparação dos dados (O11) na TL11; ver "Cobertura MoLIC → telas".)*
- [x] Estados de erro, feedback e recuperação foram prototipados. *(As rupturas da Síntese da Entrega 9; a falta de memória no treino está implementada, mas não foi capturada.)*
- [x] Terminologia/signos são consistentes com Entrega 9. *(Esquema de signos revisto em 20/11/2026, com "na fila", "avaliação no conjunto de teste" e "dataset montado".)*
- [x] Componentes equivalentes se comportam de forma consistente. *(Todo campo obrigatório desabilita o botão e diz o que falta, da TL01 à TL11.)*
- [x] Fluxos críticos são clicáveis do início ao fim. *(A interface é funcional; os fluxos dos três MoLIC foram percorridos nas capturas de 20/11/2026.)*
- [x] O protótipo está pronto para inspeção e testes, sem “links mortos” nas tarefas avaliadas. *(Conferido nas capturas de 20/11/2026; a conferência é refeita na cópia dos dados preparada para o piloto, antes dos testes da Entrega 14.)*
- [x] Dashboards, relatórios, históricos, filtros, administração e CRUDs presentes possuem justificativa rastreável. *(Não há dashboard, histórico, filtros, administração nem CRUD. A TL11 vem da O11 (Entrega 9), e o download do vídeo com a sobreposição está justificado no `RASTREABILIDADE.md`, §5.)*
- [x] Estados de vazio, processamento, erro e recuperação foram considerados quando pertinentes.
- [x] Resultados técnicos são apresentados de forma interpretável para o perfil de usuário. *(Explicação de cada termo, estado "sem métricas", destaque do maior valor que não é recomendação e diferença entre configurações sem julgamento.)*
- [x] A equipe distingue no protótipo o que é interação simulada e o que é funcionalidade técnica realmente integrada, quando necessário. *(Nada é simulado; os valores das capturas são ilustrativos.)*

## Histórico de revisões

| Data | O que mudou | Motivo |
|---|---|---|
| 20/11/2026 | Versão avaliada passa a ser o commit `16a5bc1`, identificado no rodapé. Interface ajustada à Entrega 10 revista: tela Datasets como conversa O11; métricas do treino só depois da avaliação no conjunto de teste; aviso de que o treino continua só com o programa aberto; explicação do termo junto do próprio termo e glossário à parte; campo obrigatório com o mesmo comportamento em todas as telas; seletor de arquivos em português. As 44 capturas e o `f01.svg` saíram e entraram 59 capturas numeradas por fluxo. Cobertura, diferenças, catálogo, sistema visual, acessibilidade (com os percursos a confirmar na Entrega 13) e checklist reescritos | Parecer do professor sobre a Entrega 11 e revisão da Entrega 10 (`PENDENCIAS.md`, INC-74) |
