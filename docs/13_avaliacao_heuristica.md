# Entrega 13 — Avaliação de IHC por inspeção heurística

**Data:** 20/11/2026 (início)  
**Status:** 🟨 em andamento  
**Responsabilidade:** 1 avaliação completa por integrante, sobre todas as telas/estados relevantes do projeto.

## Objetivo da atividade

Encontrar problemas de usabilidade por inspeção sistemática da interface com as **10 heurísticas de Nielsen**. Cada avaliador trabalha individualmente primeiro; depois a equipe consolida problemas duplicados e prioridades.

> **Parte de violações:** registre somente problemas reais. Não invente uma violação para “preencher” cada heurística. Para provar que todas foram exercitadas, use a **matriz de cobertura H1–H10**. Para heurísticas sem violação, a disciplina solicita um exemplo didático de boa prática.

## 1. Heurísticas adotadas

1. Visibilidade do status do sistema
2. Compatibilidade entre o sistema e o mundo real
3. Controle e liberdade do usuário
4. Consistência e padrões
5. Prevenção de erros
6. Reconhecimento em vez de memorização
7. Flexibilidade e eficiência de uso
8. Estética e design minimalista
9. Ajudar usuários a reconhecer, diagnosticar e recuperar-se de erros
10. Ajuda e documentação

## Cobertura especial para interfaces administrativas e analíticas

Quando existirem, não limite a avaliação às “telas principais”. Inspecione também:

- dashboard em estados normal, vazio e erro;
- filtros sem resultado e filtros combinados;
- relatórios e exportação;
- histórico/listas longas;
- formulários CRUD (criação, edição, exclusão, validação);
- alteração de perfil/permissão;
- confirmações de ações destrutivas;
- processamento/loading/progresso;
- falha e recuperação;
- comparação de resultados;
- mensagens de termos técnicos, métricas e recomendações;
- ajuda/documentação contextual.

Em TCCs técnicos, observe especialmente se a interface comunica o estado do processamento e traduz informações técnicas para o vocabulário do usuário escolhido.

## 2. Escopo da inspeção

| Item | Definição |
|---|---|
| Versão avaliada | Interface implementada na Entrega 11: https://github.com/HenriqueFinatti/Segmentacao-Semantica-Off-Road, ramo `interface`, commit `16a5bc1` (20/11/2026), identificado no rodapé de cada tela; é a versão única das Entregas 13 e 14 (Entrega 11, "Acesso ao protótipo") |
| Telas/estados | TL01 Configuração de treino: escolher o modelo e os parâmetros; sem dataset de treino (PA); nomear a configuração; nome repetido (RA).<br>TL02 Estado do treino: na fila; treinando; avaliação no conjunto de teste; resultado do treino; treino ou avaliação interrompidos (RA); falta de memória, com sugestão de batch size menor (RA).<br>TL03 Entradas e configurações: entradas e configurações obrigatórias (PA); envio de imagens ou vídeos e escolha das configurações; arquivos fora do formato aceito (AL).<br>TL04 Processamento: na fila; processando; falha numa imagem e numa configuração inteira (RA e CE); concluído.<br>TL05 Resultado e avaliação da imagem: sem sessão (vazio); sobreposição e sem métricas (PP); imagem original e máscara; região ampliada; avaliação registrada; quadro de vídeo e download do MP4.<br>TL06 Comparação na mesma imagem: configuração obrigatória (PA); escolher as configurações a comparar; comparar na mesma região, com sobreposição e com máscara.<br>TL07 Desempenho consolidado: configurações obrigatórias (PA); sem avaliação no conjunto de teste (CE); conjuntos de teste diferentes (AL); execução faltante no ciclo (CE); sem valor de referência (vazio); valor de referência e maior valor; gráfico; a diferença importa?; matriz de confusão.<br>TL08 Conclusão: validação, experimento e recomendação, cada uma com campo obrigatório (PA), conferência e correção; imagens sem avaliação (AL).<br>TL09 Apresentação e decisão: sem recomendação (vazio); retomar a análise; responder a uma dúvida; condição obrigatória (PA); decisão registrada.<br>TL10 Explicação dos termos: explicação junto do termo, aberta pelo botão "?"; glossário de termos, aberto pelo botão do topo.<br>TL11 Datasets: conferir os datasets; confirmar a remontagem (AL); montagem na fila; dataset montado; avaliar as selecionadas (PA); falha na avaliação (RA e CE); avaliando; avaliação concluída.<br>Elementos de todas as telas: menu, indicador do treino e da avaliação no topo, rodapé com a versão. As capturas de referência são as da Entrega 11 (`assets/11_figma/`) |
| Fluxos | M01 (P01, Rafael), M02 (P03, Larissa) e M03 (P02, Andreia), da Entrega 10 revista em 20/11/2026; a TL11 é a conversa "preparar os dados de treino e de teste" (O11) do M03 |
| Percursos de acessibilidade | Os sete percursos completos da Entrega 11 ("Verificação de acessibilidade básica"), feitos só com teclado e com ampliação de 200% do navegador e, quando possível, com leitor de tela `[?]` |
| Dispositivo/viewport | Computador que executa os modelos, com mouse e teclado, e a interface no navegador desse computador, em endereço local e sem internet (Entrega 8, §1; Entrega 12, seção C). Resolução da tela e navegador: `[?]` |
| Avaliadores | AV01 — Henrique Finatti Silveira Belo Trebbi; AV02 — Tiago Fagundes dos Santos; AV03 — Mateus Marana Assuena. Cada um inspeciona sozinho, sem conhecer os achados dos outros, antes da consolidação (seção 7) |

**Identificadores desta entrega:** H1 a H10 são as heurísticas de Nielsen (não confundir com as hipóteses H01 a H12 da Entrega 1); AV01 a AV03 são os avaliadores; cada avaliador numera as próprias violações a partir de V01, e elas são citadas com o avaliador, como "V01 (AV02)"; HC01… são os problemas consolidados da equipe. As capturas de cada avaliador ficam em `assets/13_heuristica/av01/`, `av02/` e `av03/`.

## 3. Procedimento individual

Cada avaliador deve:

1. percorrer os fluxos/telas ao menos uma vez para familiarização;
2. inspecionar novamente aplicando sistematicamente H1–H10;
3. registrar cada problema com evidência e contexto;
4. atribuir severidade **depois de compreender bem o problema**, justificando a decisão;
5. não discutir achados com os demais antes de terminar a inspeção individual, quando o objetivo for preservar independência.

### Escala de severidade (0–4)

| Grau | Interpretação |
|---:|---|
| 0 | não é considerado problema de usabilidade |
| 1 | problema cosmético; corrigir se houver tempo |
| 2 | problema menor; baixa prioridade |
| 3 | problema maior; alta prioridade |
| 4 | catástrofe de usabilidade; correção imperativa antes de disponibilizar |

Ao justificar, considere **frequência, impacto e persistência** do problema no contexto real de uso.

---

## Avaliador AV01 — Henrique Finatti Silveira Belo Trebbi

**Autor(a):** Henrique Finatti Silveira Belo Trebbi — 22.123.030-3  
**Data da inspeção:** {{dd/mm/aaaa}}  
**Versão inspecionada:** commit `16a5bc1`  
**Computador, tela, resolução e navegador:** {{...}}  
**Tempo gasto na inspeção:** {{...}}

### 4. Cobertura das telas, dos estados e das heurísticas

#### Telas e estados examinados

Os estados de cada tela são os da seção 2 ("Telas/estados"). A falta de memória no treino não pode ser provocada no equipamento: é examinada pela mensagem implementada (Entrega 11) e marcada como "examinada sem reproduzir".

| Tela | Estados examinados | Examinado? | Observação (motivo, se não examinado) |
|---|---|---|---|
| TL01 Configuração de treino | {{...}} | sim/não | {{...}} |
| TL02 Estado do treino (inclui treino interrompido e falta de memória) | {{...}} | sim/não | {{...}} |
| TL03 Entradas e configurações | {{...}} | sim/não | {{...}} |
| TL04 Processamento (inclui falha na execução) | {{...}} | sim/não | {{...}} |
| TL05 Resultado e avaliação da imagem | {{...}} | sim/não | {{...}} |
| TL06 Comparação na mesma imagem | {{...}} | sim/não | {{...}} |
| TL07 Desempenho consolidado | {{...}} | sim/não | {{...}} |
| TL08 Conclusão | {{...}} | sim/não | {{...}} |
| TL09 Apresentação e decisão | {{...}} | sim/não | {{...}} |
| TL10 Explicação dos termos | {{...}} | sim/não | {{...}} |
| TL11 Datasets | {{...}} | sim/não | {{...}} |
| Elementos de todas as telas | {{...}} | sim/não | {{...}} |

#### Matriz das 10 heurísticas

| Heurística | Telas/fluxos examinados | Houve violação? | IDs dos achados | Exemplo de boa prática se não violada |
|---|---|---|---|---|
| H1 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H2 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H3 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H4 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H5 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H6 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H7 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H8 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H9 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H10 | {{...}} | sim/não | {{V01...}} | {{...}} |

### 5. Declaração de violações

| ID | Heurística | Tela/estado | Ação ou condição | Problema observado | Consequência para quem usa | Evidência | Severidade | Justificativa da severidade | Recomendação |
|---|---|---|---|---|---|---|---:|---|---|
| V01 | {{H...}} | {{TL...}} | {{em que ação ou condição}} | {{o que ocorre}} | {{o que isso causa a quem usa}} | ![V01 (AV01)](../assets/13_heuristica/av01/v01.png) | {{0–4}} | {{frequência/impacto/persistência}} | {{correção específica}} |

**Qualidade do relato:** o problema deve ser observável e localizado. Evite “interface confusa” sem dizer **o que**, **onde**, **quando** e **para quem**.

#### Percursos de acessibilidade

Os sete percursos da Entrega 11 ("Percursos completos a confirmar"), feitos de ponta a ponta. Cada problema encontrado também entra na declaração de violações.

| Percurso | Só com teclado: concluído? Onde parou? | Foco visível e na ordem da tela? | Ampliação de 200%: legível, sem rolagem horizontal? | Leitor de tela: anuncia estados e mensagens? | IDs das violações |
|---|---|---|---|---|---|
| Configurar e iniciar um treino (TL01 → TL02) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Enviar entradas e recuperar-se de um formato inválido (TL03 → TL04) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Avaliar as imagens (TL05) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Comparar configurações (TL06 → TL07) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Registrar uma conclusão (TL08) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Apresentar uma recomendação (TL09) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Preparar os dados e avaliar as configurações (TL11) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

### 6. Boas práticas — heurísticas não violadas (atividade didática)

| Heurística sem violação | Exemplo no sistema | Evidência | Por que atende |
|---|---|---|---|
| {{H...}} | {{...}} | {{print}} | {{...}} |

---

## Avaliador AV02 — Tiago Fagundes dos Santos

**Autor(a):** Tiago Fagundes dos Santos — 22.123.017-0  
**Data da inspeção:** {{dd/mm/aaaa}}  
**Versão inspecionada:** commit `16a5bc1`  
**Computador, tela, resolução e navegador:** {{...}}  
**Tempo gasto na inspeção:** {{...}}

### 4. Cobertura das telas, dos estados e das heurísticas

#### Telas e estados examinados

Os estados de cada tela são os da seção 2 ("Telas/estados"). A falta de memória no treino não pode ser provocada no equipamento: é examinada pela mensagem implementada (Entrega 11) e marcada como "examinada sem reproduzir".

| Tela | Estados examinados | Examinado? | Observação (motivo, se não examinado) |
|---|---|---|---|
| TL01 Configuração de treino | {{...}} | sim/não | {{...}} |
| TL02 Estado do treino (inclui treino interrompido e falta de memória) | {{...}} | sim/não | {{...}} |
| TL03 Entradas e configurações | {{...}} | sim/não | {{...}} |
| TL04 Processamento (inclui falha na execução) | {{...}} | sim/não | {{...}} |
| TL05 Resultado e avaliação da imagem | {{...}} | sim/não | {{...}} |
| TL06 Comparação na mesma imagem | {{...}} | sim/não | {{...}} |
| TL07 Desempenho consolidado | {{...}} | sim/não | {{...}} |
| TL08 Conclusão | {{...}} | sim/não | {{...}} |
| TL09 Apresentação e decisão | {{...}} | sim/não | {{...}} |
| TL10 Explicação dos termos | {{...}} | sim/não | {{...}} |
| TL11 Datasets | {{...}} | sim/não | {{...}} |
| Elementos de todas as telas | {{...}} | sim/não | {{...}} |

#### Matriz das 10 heurísticas

| Heurística | Telas/fluxos examinados | Houve violação? | IDs dos achados | Exemplo de boa prática se não violada |
|---|---|---|---|---|
| H1 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H2 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H3 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H4 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H5 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H6 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H7 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H8 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H9 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H10 | {{...}} | sim/não | {{V01...}} | {{...}} |

### 5. Declaração de violações

| ID | Heurística | Tela/estado | Ação ou condição | Problema observado | Consequência para quem usa | Evidência | Severidade | Justificativa da severidade | Recomendação |
|---|---|---|---|---|---|---|---:|---|---|
| V01 | {{H...}} | {{TL...}} | {{em que ação ou condição}} | {{o que ocorre}} | {{o que isso causa a quem usa}} | ![V01 (AV02)](../assets/13_heuristica/av02/v01.png) | {{0–4}} | {{frequência/impacto/persistência}} | {{correção específica}} |

**Qualidade do relato:** o problema deve ser observável e localizado. Evite “interface confusa” sem dizer **o que**, **onde**, **quando** e **para quem**.

#### Percursos de acessibilidade

Os sete percursos da Entrega 11 ("Percursos completos a confirmar"), feitos de ponta a ponta. Cada problema encontrado também entra na declaração de violações.

| Percurso | Só com teclado: concluído? Onde parou? | Foco visível e na ordem da tela? | Ampliação de 200%: legível, sem rolagem horizontal? | Leitor de tela: anuncia estados e mensagens? | IDs das violações |
|---|---|---|---|---|---|
| Configurar e iniciar um treino (TL01 → TL02) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Enviar entradas e recuperar-se de um formato inválido (TL03 → TL04) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Avaliar as imagens (TL05) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Comparar configurações (TL06 → TL07) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Registrar uma conclusão (TL08) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Apresentar uma recomendação (TL09) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Preparar os dados e avaliar as configurações (TL11) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

### 6. Boas práticas — heurísticas não violadas (atividade didática)

| Heurística sem violação | Exemplo no sistema | Evidência | Por que atende |
|---|---|---|---|
| {{H...}} | {{...}} | {{print}} | {{...}} |

---

## Avaliador AV03 — Mateus Marana Assuena

**Autor(a):** Mateus Marana Assuena — 22.123.026-1  
**Data da inspeção:** {{dd/mm/aaaa}}  
**Versão inspecionada:** commit `16a5bc1`  
**Computador, tela, resolução e navegador:** {{...}}  
**Tempo gasto na inspeção:** {{...}}

### 4. Cobertura das telas, dos estados e das heurísticas

#### Telas e estados examinados

Os estados de cada tela são os da seção 2 ("Telas/estados"). A falta de memória no treino não pode ser provocada no equipamento: é examinada pela mensagem implementada (Entrega 11) e marcada como "examinada sem reproduzir".

| Tela | Estados examinados | Examinado? | Observação (motivo, se não examinado) |
|---|---|---|---|
| TL01 Configuração de treino | {{...}} | sim/não | {{...}} |
| TL02 Estado do treino (inclui treino interrompido e falta de memória) | {{...}} | sim/não | {{...}} |
| TL03 Entradas e configurações | {{...}} | sim/não | {{...}} |
| TL04 Processamento (inclui falha na execução) | {{...}} | sim/não | {{...}} |
| TL05 Resultado e avaliação da imagem | {{...}} | sim/não | {{...}} |
| TL06 Comparação na mesma imagem | {{...}} | sim/não | {{...}} |
| TL07 Desempenho consolidado | {{...}} | sim/não | {{...}} |
| TL08 Conclusão | {{...}} | sim/não | {{...}} |
| TL09 Apresentação e decisão | {{...}} | sim/não | {{...}} |
| TL10 Explicação dos termos | {{...}} | sim/não | {{...}} |
| TL11 Datasets | {{...}} | sim/não | {{...}} |
| Elementos de todas as telas | {{...}} | sim/não | {{...}} |

#### Matriz das 10 heurísticas

| Heurística | Telas/fluxos examinados | Houve violação? | IDs dos achados | Exemplo de boa prática se não violada |
|---|---|---|---|---|
| H1 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H2 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H3 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H4 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H5 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H6 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H7 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H8 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H9 | {{...}} | sim/não | {{V01...}} | {{...}} |
| H10 | {{...}} | sim/não | {{V01...}} | {{...}} |

### 5. Declaração de violações

| ID | Heurística | Tela/estado | Ação ou condição | Problema observado | Consequência para quem usa | Evidência | Severidade | Justificativa da severidade | Recomendação |
|---|---|---|---|---|---|---|---:|---|---|
| V01 | {{H...}} | {{TL...}} | {{em que ação ou condição}} | {{o que ocorre}} | {{o que isso causa a quem usa}} | ![V01 (AV03)](../assets/13_heuristica/av03/v01.png) | {{0–4}} | {{frequência/impacto/persistência}} | {{correção específica}} |

**Qualidade do relato:** o problema deve ser observável e localizado. Evite “interface confusa” sem dizer **o que**, **onde**, **quando** e **para quem**.

#### Percursos de acessibilidade

Os sete percursos da Entrega 11 ("Percursos completos a confirmar"), feitos de ponta a ponta. Cada problema encontrado também entra na declaração de violações.

| Percurso | Só com teclado: concluído? Onde parou? | Foco visível e na ordem da tela? | Ampliação de 200%: legível, sem rolagem horizontal? | Leitor de tela: anuncia estados e mensagens? | IDs das violações |
|---|---|---|---|---|---|
| Configurar e iniciar um treino (TL01 → TL02) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Enviar entradas e recuperar-se de um formato inválido (TL03 → TL04) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Avaliar as imagens (TL05) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Comparar configurações (TL06 → TL07) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Registrar uma conclusão (TL08) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Apresentar uma recomendação (TL09) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| Preparar os dados e avaliar as configurações (TL11) | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

### 6. Boas práticas — heurísticas não violadas (atividade didática)

| Heurística sem violação | Exemplo no sistema | Evidência | Por que atende |
|---|---|---|---|
| {{H...}} | {{...}} | {{print}} | {{...}} |

---

## 7. Consolidação da equipe

Problemas iguais ou muito semelhantes encontrados por avaliadores diferentes devem ser consolidados, preservando quem os encontrou. A consolidação só começa quando os três avaliadores terminam a inspeção individual. A heurística e a severidade que cada avaliador deu ficam registradas antes do consenso; quando não houver acordo, as posições ficam lado a lado na coluna "Divergências" (Entrega 12, E.5).

| ID consolidado | Achados individuais | Heurística e severidade de cada avaliador | Problema | Severidade final | Divergências | Prioridade | Responsável pela correção |
|---|---|---|---|---:|---|---|---|
| HC01 | {{V01 (AV01), V04 (AV02)}} | {{AV01: H.., ..; AV02: H.., ..}} | {{...}} | {{...}} | {{...}} | {{alta/média/baixa}} | {{...}} |

## 8. Síntese e plano de melhoria

- Quantidade de problemas por heurística e severidade.
- Problemas críticos/graves que bloqueiam teste ou release.
- Padrões recorrentes entre telas.
- Correções que serão feitas antes/para a avaliação com usuários.
- Respostas às perguntas QA09 a QA13 da Entrega 12 (E.5).
- A ausência de problemas encontrados não comprova alta usabilidade: indica só que esta inspeção, com esse escopo e esses avaliadores, não revelou outros problemas.

## Checklist

- [ ] Cada integrante fez uma inspeção completa e identificada.
- [ ] Todas as telas/estados relevantes foram examinados.
- [ ] Estados administrativos, filtros, relatórios, históricos, processamento e erros foram incluídos quando existentes.
- [ ] A inspeção avaliou a interface/protótipo, não o mérito técnico do algoritmo/modelo.
- [ ] H1–H10 aparecem na matriz de cobertura de cada avaliador.
- [ ] Cada avaliador fez os sete percursos de acessibilidade (teclado, ampliação de 200% e, quando possível, leitor de tela).
- [ ] Parte de violações contém apenas violações, sem “forçar” exemplos.
- [ ] Todo problema tem print/localização e contexto.
- [ ] Severidade possui justificativa, não apenas número.
- [ ] Recomendação resolve a causa ou reduz o impacto.
- [ ] Achados duplicados foram consolidados ao final.
