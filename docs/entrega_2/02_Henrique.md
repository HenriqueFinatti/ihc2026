# Entrega 2 — Respostas 1 e 2 sobre o Roboflow

## Entrada obrigatória da Entrega 1

| Item citado na Entrega 1 | Tipo | Por que foi citado | Status inicial | Decisão nesta entrega |
|---|---|---|---|---|
| Roboflow | análogo | É uma ferramenta que serve para classificar imagens, permitindo ao usuário enviar imagens e selecionar modelos | F | analisar |

## 1. Público-alvo desta análise

Empresas que precisam de modelos para reconhecimento de objetos em imagens para diferentes casos de uso como reconhecer falhas em peças automotivas, doenças em plantas, análise de raio x etc.

## 2. Concorrentes diretos/indiretos

### Análise Roboflow

**Autor(a):** Henrique Finatti Silveira Belo Trebbi  
**Tipo:** análogo  
**Link oficial:** https://roboflow.com/  
**Data de acesso:** 27/08/2026

#### Contexto e proposta

O Roboflow funciona como um ecossistema completo para projetos de visão computacional, cobrindo todo o ciclo de vida de um modelo de IA desde a imagem bruta até o aplicativo final.
A grande vantagem da ferramenta é ser low code, permitindo que e empresas criem soluções de IA de forma rápida, sem a necessidade de construir toda a infraestrutura do zero.

#### Funcionalidades relevantes

| Funcionalidade | Como é realizada | Evidência/print | Observação de IHC |
|---|---|---|---|
| Upload de imagens | Através de um botão ao lado de um resultado prévio | `assets/02_concorrencia/roboflow_input_imagens.png` | O botão na parte superior esquerda da tela, usando o ícone de upload de imagem deixa bem claro pro usuário como usar e para que serve |
Seleção de modelos | Através de prompt | `assets/02_concorrencia/roboflow_selecionar_modelos.png` | A seleção de diferentes modelos através do chat é bem limitada e pouco intuitiva, usuários que não sabem dessa característica não conseguirão entender essa funcionalidade |


#### Experiência do usuário e opiniões

Use avaliações públicas, relatos, estudos, testes próprios ou outra fonte identificável. Não trate opinião isolada como verdade universal.

#### Padrões e tendências percebidos

É um sistema pago e bem abrangente. Permite muita liberdade ao usuário, montar projetos, selecionar modelos, diferentes formas de entrar dados etc.

#### Pontos positivos, limitações e lições

| Ponto | Evidência | Implicação para nosso projeto |
|---|---|---|
| O input de imagens | `assets/02_concorrencia/roboflow_input_imagens.png` | No nosso projeto iremos precisar permitir ao usuário carregar imagens/vídeos a serem segmentados |
| Seleção de modelos | `assets/02_concorrencia/roboflow_selecionar_modelos.png` | Nosso projeto irá permitir a seleção de diferentes modelos, porém usando algum tipo de lista, considerando que o chat é pouco intuitivo |
