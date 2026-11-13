# Gerador das telas da Entrega 6 (versão 2)

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
