"""Anotações da revisão do protótipo em papel (Entrega 6).

Gera, a partir das fotos da versão simulada (assets/06_prototipos/*.jfif), uma imagem anotada
por tela em assets/06_prototipos/anotacoes/. Cada imagem tem:
  - a foto original, sem alteração, com marcadores numerados;
  - à direita, as notas de cada marcador, com o estado da alteração;
  - embaixo, os estados da tela desenhados em baixa fidelidade (quando há).

Requer Python 3 e Pillow (pip install pillow). Rode a partir desta pasta:
    python3 anotacoes.py
"""
from pathlib import Path
from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "assets/06_prototipos"
OUT = SRC / "anotacoes"

PHOTO_W = 1100          # largura da foto na imagem anotada
PANEL_W = 760           # largura da coluna de notas
M = 30                  # margem
INK = (34, 34, 34)
RED = (200, 30, 30)
GRAY = (110, 110, 110)
PAPER = (250, 250, 247)

TAG = {
    "A": ("APLICADA NA ANOTAÇÃO", (24, 110, 60)),
    "F": ("FORA DO RECORTE", (150, 90, 0)),
    "R": ("RETIRADA", (120, 120, 120)),
}


def font(size, bold=False):
    names = (["DejaVuSans-Bold.ttf", "Arial Bold.ttf", "arialbd.ttf"] if bold
             else ["DejaVuSans.ttf", "Arial.ttf", "arial.ttf"])
    dirs = ["/usr/share/fonts/truetype/dejavu", "/Library/Fonts", "/System/Library/Fonts/Supplemental",
            "C:/Windows/Fonts", ""]
    for d in dirs:
        for n in names:
            try:
                return ImageFont.truetype(str(Path(d) / n) if d else n, size)
            except OSError:
                continue
    return ImageFont.load_default(size)


F_TITLE, F_SUB, F_NOTE, F_TAG, F_NUM = font(30, True), font(18), font(17), font(13, True), font(20, True)
F_BOX, F_BOXB = font(15), font(15, True)


def text_block(d, x, y, text, f, width_chars, fill=INK, gap=4):
    for line in wrap(text, width_chars):
        d.text((x, y), line, font=f, fill=fill)
        y += f.size + gap
    return y


def marker(d, x, y, n):
    r = 19
    d.ellipse([x - r, y - r, x + r, y + r], fill=RED, outline="white", width=3)
    d.text((x, y), str(n), font=F_NUM, fill="white", anchor="mm")


def state_box(d, x, y, w, title, lines):
    """Estado desenhado em baixa fidelidade: caixa com título e linhas de conteúdo."""
    h = 44 + 24 * len(lines)
    d.rounded_rectangle([x, y, x + w, y + h], radius=8, outline=INK, width=2, fill="white")
    d.text((x + 14, y + 12), title, font=F_BOXB, fill=INK)
    d.line([x + 10, y + 36, x + w - 10, y + 36], fill=GRAY, width=1)
    yy = y + 44
    for ln in lines:
        if ln.startswith("[") and ln.endswith("]"):          # botões
            bx = x + 14
            for b in ln[1:-1].split("] ["):
                tw = d.textlength(b, font=F_BOX) + 20
                d.rounded_rectangle([bx, yy - 2, bx + tw, yy + 20], radius=5, outline=INK, width=2)
                d.text((bx + 10, yy), b, font=F_BOX, fill=INK)
                bx += tw + 10
        else:
            d.text((x + 14, yy), ln, font=F_BOX, fill=INK)
        yy += 24
    return y + h


def render(photo, sid, title, subtitle, notes, states, out_name):
    im = Image.open(SRC / photo).convert("RGB")
    k = PHOTO_W / im.width
    ph = im.resize((PHOTO_W, round(im.height * k)))

    # altura da coluna de notas
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    ny = 0
    for _, tag, txt in notes:
        ny += 30 + (len(wrap(txt, 62)) * (F_NOTE.size + 4)) + 18
    states_h = 0
    if states:
        states_h = 60 + max(44 + 24 * len(l) for _, l in states) + 20
    H = max(110 + ph.height + states_h + M, 110 + 70 + ny + M)
    W = M + PHOTO_W + M + PANEL_W + M

    canvas = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(canvas)
    d.text((M, 22), f"{sid} — {title}", font=F_TITLE, fill=INK)
    d.text((M, 64), subtitle, font=F_SUB, fill=GRAY)

    py = 110
    canvas.paste(ph, (M, py))
    d.rectangle([M, py, M + PHOTO_W, py + ph.height], outline=GRAY, width=1)
    for n, ((x, y), _, _) in enumerate(notes, 1):
        marker(d, M + x * k, py + y * k, n)

    # coluna de notas
    x0 = M + PHOTO_W + M
    d.text((x0, py), "Anotações da revisão (15/11/2026)", font=font(20, True), fill=INK)
    y = py + 40
    for n, (_, tag, txt) in enumerate(notes, 1):
        marker(d, x0 + 19, y + 12, n)
        label, color = TAG[tag]
        tw = d.textlength(label, font=F_TAG) + 16
        d.rounded_rectangle([x0 + 48, y + 2, x0 + 48 + tw, y + 22], radius=4, fill=color)
        d.text((x0 + 56, y + 5), label, font=F_TAG, fill="white")
        y = text_block(d, x0 + 48, y + 30, txt, F_NOTE, 62) + 14

    # estados
    if states:
        sy = py + ph.height + 30
        d.text((M, sy), "Estados desta tela, desenhados na anotação (baixa fidelidade)", font=font(20, True), fill=INK)
        n = len(states)
        bw = (PHOTO_W - 20 * (n - 1)) / n
        for i, (t, lines) in enumerate(states):
            state_box(d, M + i * (bw + 20), sy + 40, bw, t, lines)

    OUT.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT / out_name, optimize=True)
    print(out_name, canvas.size)


# ------------------------------------------------------------------ P01
render("input_config.jfif", "P01", "Nova análise (versão simulada, com anotações)",
       "Fluxo PF01 · T02 · Foto original preservada; as alterações aparecem só nas anotações.",
       [((865, 555), "A", "Configuração: a lista de escolha única vira seleção múltipla, com o nome real e uma "
                           "descrição curta de cada configuração (ex.: \"DeepLabV3+ – 50 épocas\"). Origem: "
                           "simulação (pedido de rodar mais de um modelo) e F01."),
        ((840, 762), "R", "\"Calcular métricas\" e \"Gerar máscara\" saem: a máscara é sempre gerada, e IoU e "
                           "acurácia não são calculadas para o arquivo enviado. Elas vêm do conjunto de teste de "
                           "cada configuração; imagem de campo é avaliada visualmente (D5, INC-59)."),
        ((840, 808), "F", "\"Salvar resultados no histórico\" é uma alternativa exploratória: histórico depende "
                           "da H08 e está fora do recorte."),
        ((815, 905), "F", "\"Configurações avançadas\": parâmetros de treino não são definidos nesta tela. "
                           "Definir e treinar uma configuração é a T08, fora deste protótipo."),
        ((200, 560), "A", "O arquivo é validado ao ser selecionado. Se o formato não for aceito, a tela mostra o "
                          "estado P01-E e \"Executar\" fica desabilitado até a pessoa escolher outro arquivo."),
        ((860, 1065), "A", "\"Executar segmentação\" leva ao estado P01-P: as configurações escolhidas entram "
                            "em fila e rodam uma de cada vez, cada uma com o seu estado. A falha de uma não "
                            "interrompe as outras. Com todas tratadas, segue para P02.")],
       [("P01-E · Arquivo inválido", ["⚠ trilha_03.gif: formato não aceito.", "Aceitos: JPG, PNG e MP4.",
                                      "[Escolher outro arquivo]"]),
        ("P01-P · Processando (fila)", ["✓ DeepLabV3+ – 50 épocas: concluída", "▶ FCN – 30 épocas: processando 45%",
                                        "✗ Falhou: arquivo corrompido", "[Repetir] [Retirar] [Voltar e alterar]"])],
       "P01_nova_analise_anotada.png")

# ------------------------------------------------------------------ P02
render("resultado_segmentacao.jfif", "P02", "Resultado da segmentação (versão simulada, com anotações)",
       "Fluxo PF02 · T01 · Foto original preservada; as alterações aparecem só nas anotações.",
       [((965, 215), "A", "Legenda binária e fixa: Trilha × Fora da trilha (D1). As classes Transitável, "
                           "Vegetação e Céu do rascunho eram ilustrativas."),
        ((160, 470), "A", "Métricas só quando a imagem tem anotação de referência (conjunto de teste). Para "
                          "imagem de campo, a tela mostra o estado P02-S, e a avaliação é visual (D5, INC-59)."),
        ((1080, 450), "R", "\"Distribuição das classes\" sai: não corresponde a nenhuma decisão das tarefas da "
                           "Entrega 5."),
        ((485, 712), "F", "\"Exportar PDF\" e \"Salvar relatório\" são alternativas exploratórias: exportação "
                          "depende da H12 e histórico da H08."),
        ((170, 718), "A", "\"Comparar modelo\" abre P03-I com a mesma imagem. Um comando \"Voltar para nova "
                          "análise\" permite trocar o arquivo ou as configurações."),
        ((290, 125), "A", "O seletor alterna entre as configurações executadas no mesmo pedido. Novo controle "
                          "anotado: a pessoa registra a avaliação (adequada, inadequada ou inconclusiva), "
                          "guardada só na sessão (T01; T03, 4.2.4).")],
       [("P02-S · Imagem de campo, sem métricas", ["Sem anotação de referência:", "não há IoU nem acurácia.",
                                                    "Avalie pela imagem e pela sobreposição.",
                                                    "[Sobrepor máscara] [Registrar avaliação]"])],
       "P02_resultado_anotado.png")

# ------------------------------------------------------------------ P03
render("comparacao_modelo.jfif", "P03", "Comparação (versão simulada, com anotações)",
       "Fluxo PF03 · T04 (e T03/T07) · Foto original preservada; as alterações aparecem só nas anotações.",
       [((430, 262), "A", "\"Modelo A\" e \"Modelo B\" saem em todos os pontos da tela (cabeçalhos, tabela e "
                          "gráfico): ficam só os nomes reais das configurações. Origem: simulação."),
        ((720, 150), "A", "A tela em papel mistura duas tarefas. Ela passa a ter duas visões, cada uma com a "
                          "origem dos dados à vista: P03-I compara configurações na mesma imagem (T03, T07); "
                          "P03-C compara o desempenho no conjunto de teste (T04)."),
        ((1365, 182), "A", "\"Atualizar\" sai. Trocar a seleção só atualiza a visualização dos resultados que já "
                           "existem. Se uma configuração ainda não tem resultado para a imagem, aparece o "
                           "estado P03-F, com o comando explícito \"Executar\"."),
        ((85, 520), "A", "Na visão consolidada, a tabela mostra IoU, acurácia e tempo no conjunto de teste e a "
                          "diferença entre as configurações. O sistema não diz se a diferença é relevante (RQ07)."),
        ((1160, 470), "R", "Classes passam a Trilha × Fora da trilha (D1); \"Distribuição das classes\" sai, como "
                           "na P02."),
        ((90, 790), "A", "\"Conclusão\" vira um campo preenchido pela pessoa (melhor, nenhuma ou "
                          "inconclusiva, com o motivo), e não um texto do sistema (RQ08). O exemplo do rascunho "
                          "contradizia a tabela, que favorecia o FCN em IoU e acurácia."),
        ((1170, 760), "F", "\"Exportar relatório\" e \"Salvar comparação\" são alternativas exploratórias "
                           "(H12 e H08).")],
       [("P03-I · Mesma imagem (T03, T07)", ["Imagem: trilha_03.jpg (sem métricas)",
                                             "Original | DeepLabV3+ | FCN",
                                             "[Mesma região] [Registrar conclusão]"]),
        ("P03-C · Conjunto de teste (T04)", ["Conjunto de teste (valores ilustr.)",
                                             "IoU: 0,78 × 0,76 · diferença: 0,02",
                                             "[Ver explicação] [Registrar conclusão]"]),
        ("P03-F · Sem resultado", ["FCN – 30 ép. ainda não foi executada", "para esta imagem.",
                                   "[Executar] [Voltar]"])],
       "P03_comparacao_anotada.png")
