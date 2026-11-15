# Geradores da Entrega 6

## `anotacoes.py` — anotações da revisão (incorporado à entrega)

Gera, a partir das fotos da versão simulada (`assets/06_prototipos/*.jfif`), uma imagem anotada por tela em `assets/06_prototipos/anotacoes/`: a foto original com marcadores numerados, as notas de cada marcador (aplicada na anotação, retirada ou fora do recorte) e os estados da tela desenhados em baixa fidelidade. É a revisão usada na Entrega 6 (seções 3 e 5).

```bash
cd scripts/prototipos
python3 anotacoes.py
```

Requer Python 3 e Pillow (`pip install pillow`).

| Arquivo | Tela | Estados anotados |
|---|---|---|
| `P01_nova_analise_anotada.png` | P01 — Nova análise | P01-E (arquivo inválido), P01-P (processando em fila) |
| `P02_resultado_anotado.png` | P02 — Resultado | P02-S (imagem de campo, sem métricas) |
| `P03_comparacao_anotada.png` | P03 — Comparação | P03-I (mesma imagem), P03-C (conjunto de teste), P03-F (sem resultado) |

## `wireframes.py` — versão 2 (não incorporada)

> **Não faz parte da Entrega 6.** É um rascunho de trabalho da equipe e está desatualizado: usa três classes (*Transitável*, *Vegetação*, *Céu*), configurações com ResNet101 e ResNet50 e a confiança do modelo, todos retirados do projeto. As notas que citam a "simulação" ("não entendi como as telas se conectam", "não entendi o progresso", "gostaria de ver as imagens segmentadas") são **propostas da equipe**, e não falas registradas na sessão (Entrega 6, seção 4). Pode servir de ponto de partida para o protótipo da Entrega 11, depois de alinhado ao recorte.


`wireframes.py` gera as telas revisadas do protótipo de baixa fidelidade em `assets/06_prototipos/v2/`. Cada tela traz, à direita, notas numeradas com o que mudou em relação à versão em papel e de onde veio a mudança (simulação, Entrega 5 ou pendência).

```bash
cd scripts/prototipos
python3 wireframes.py
```

Requer só Python 3. Para conferir a legibilidade, use o verificador da Entrega 5:

```bash
node ../diagramas/verificar.js ../../assets/06_prototipos/v2/*.svg
```

| Arquivo | Tela | Tarefas |
|---|---|---|
| `P00_inicio.svg` | Início: escolha do objetivo | — |
| `P01_nova_analise.svg` | Nova análise: arquivo, anotação opcional e configurações | T02, T03 |
| `P01E_entrada_erro.svg` | Estado: arquivo inválido | T02 |
| `P02_processando.svg` | Processamento por configuração | T02, T03 |
| `P02F_falha_execucao.svg` | Estado: falha em uma configuração | T03 (2.3.2) |
| `P03_resultado.svg` | Resultado com métricas (lado a lado) | T01 |
| `P03S_resultado_sem_metricas.svg` | Estado: sem anotação (sobreposição e confiança) | T01 |
| `P04_comparar_configuracoes.svg` | Comparar configurações na mesma imagem | T03 |
| `P05_desempenho_consolidado.svg` | Desempenho consolidado e recomendação | T04, T05 |
| `P05F_execucao_faltante.svg` | Estado: execução faltante | T05 (1.2) |
| `mapa_navegacao.svg` | Mapa de navegação entre telas e estados | — |

Os nomes das configurações (`CFG`) e das classes são ilustrativos. Confirme com o TCC e altere no topo do script.
