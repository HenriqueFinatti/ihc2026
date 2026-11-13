"""Gera as telas revisadas da Entrega 6 (protótipo de baixa fidelidade, versão 2) em SVG.

Uso:  cd scripts/prototipos && python3 wireframes.py
Saída: assets/06_prototipos/v2/*.svg

Cada tela tem, à direita, notas numeradas (círculos pretos) que explicam o que mudou em
relação à versão em papel e de onde veio a mudança (simulação, Entrega 5, pendência).
Os nomes das configurações e as classes são ilustrativos: confirmar com o TCC.
"""
from pathlib import Path
from xml.sax.saxutils import escape
import textwrap

OUT = Path(__file__).resolve().parents[2] / "assets/06_prototipos/v2"
FONT = "DejaVu Sans, Arial, sans-serif"
W, H = 1640, 900
SX, SY, SW, SH = 20, 70, 1200, 800          # moldura da tela
NX = 1250                                   # coluna de notas

CFG = ["DeepLabv3+ · ResNet152", "DeepLabv3+ · ResNet101", "FCN · ResNet50"]
ARQ = "trilha_teste_04.jpg"


class WF:
    def __init__(self, sid, title, desc):
        self.sid, self.title, self.desc = sid, title, desc
        self.o = []
        self.n = 0

    # ---------------------------------------------------------------- primitivas
    def t(self, x, y, s, size=15, w=400, a="start", fill="#222"):
        self.o.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" text-anchor="{a}" '
                      f'fill="{fill}">{escape(s)}</text>')

    def r(self, x, y, w, h, fill="white", stroke="#333", sw=1.4, dash=None, rx=4, tag=False):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        c = ' class="frame"' if tag else ""
        self.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
                      f'stroke="{stroke}" stroke-width="{sw}"{d}{c}/>')

    def p(self, d, sw=1.4, fill="none", stroke="#333", dash=None):
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        self.o.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{ds}/>')

    def group(self, fn):
        self.n += 1
        self.o.append(f'<g data-box="{self.sid}-{self.n}">')
        fn()
        self.o.append("</g>")

    # ---------------------------------------------------------------- componentes
    def button(self, x, y, w, label, kind="primary"):
        def f():
            if kind == "primary":
                self.r(x, y, w, 40, fill="#333", tag=True)
                self.t(x + w / 2, y + 26, label, w=700, a="middle", fill="white")
            elif kind == "secondary":
                self.r(x, y, w, 40, tag=True)
                self.t(x + w / 2, y + 26, label, a="middle")
            else:  # desabilitado
                self.r(x, y, w, 40, fill="#eeeeee", stroke="#999", dash="5 4", tag=True)
                self.t(x + w / 2, y + 26, label, a="middle", fill="#888")
        self.group(f)

    def box(self, x, y, w, h, lines, size=15, fill="white", dash=None, bold_first=False, center=False):
        def f():
            self.r(x, y, w, h, fill=fill, dash=dash, tag=True)
            for i, s in enumerate(lines):
                if not s:
                    continue
                if center:
                    self.t(x + w / 2, y + 26 + 22 * i, s, size, 700 if (bold_first and i == 0) else 400, "middle")
                else:
                    self.t(x + 14, y + 26 + 22 * i, s, size, 700 if (bold_first and i == 0) else 400)
        self.group(f)

    def image(self, x, y, w, h, label="Imagem original"):
        self.r(x, y, w, h, fill="#f4f4f4")
        self.p(f"M{x} {y} L{x + w} {y + h} M{x + w} {y} L{x} {y + h}", sw=0.8, stroke="#aaa")
        bw = min(160, w - 12)
        self.r(x + w / 2 - bw / 2, y + h / 2 - 16, bw, 30, fill="#f4f4f4", stroke="none")
        self.t(x + w / 2, y + h / 2 + 5, label, 14, a="middle", fill="#444")

    def mask(self, x, y, w, h, overlay=False, low_conf=False):
        """Máscara esquemática: céu (cinza claro), vegetação (pontos), transitável (hachura)."""
        self.r(x, y, w, h, fill="#f4f4f4" if overlay else "white")
        if overlay:
            self.p(f"M{x} {y} L{x + w} {y + h} M{x + w} {y} L{x} {y + h}", sw=0.6, stroke="#ccc")
        op = ' opacity="0.65"' if overlay else ""
        sky = y + h * 0.3
        self.o.append(f'<path d="M{x} {y} H{x + w} V{sky} H{x} Z" fill="url(#ceu)"{op}/>')
        self.o.append(f'<path d="M{x} {sky} H{x + w} V{y + h} H{x} Z" fill="url(#veg)"{op}/>')
        self.o.append(f'<path d="M{x + w * 0.42} {sky} L{x + w * 0.58} {sky} L{x + w * 0.9} {y + h} '
                      f'L{x + w * 0.1} {y + h} Z" fill="url(#trans)"{op}/>')
        self.r(x, y, w, h, fill="none")
        if low_conf:
            self.r(x + w * 0.62, y + h * 0.45, w * 0.22, h * 0.3, fill="white", stroke="#333", dash="4 3", rx=8)
            self.t(x + w * 0.73, y + h * 0.62, "baixa", 12, a="middle")
            self.t(x + w * 0.73, y + h * 0.62 + 14, "confiança", 12, a="middle")

    def legend(self, x, y):
        self.t(x, y, "Classes", 14, 700)
        for i, (pat, s) in enumerate([("trans", "Transitável"), ("veg", "Vegetação"), ("ceu", "Céu")]):
            yy = y + 14 + 26 * i
            self.o.append(f'<rect x="{x}" y="{yy}" width="22" height="18" fill="url(#{pat})" stroke="#333"/>')
            self.t(x + 30, yy + 14, s, 14)

    def check(self, x, y, on, label, size=15):
        self.r(x, y - 14, 18, 18, rx=2)
        if on:
            self.p(f"M{x + 3} {y - 5} L{x + 8} {y} L{x + 15} {y - 11}", sw=2)
        self.t(x + 28, y, label, size)

    def radio(self, x, y, on, label, size=15):
        self.o.append(f'<circle cx="{x + 9}" cy="{y - 5}" r="9" fill="white" stroke="#333" stroke-width="1.4"/>')
        if on:
            self.o.append(f'<circle cx="{x + 9}" cy="{y - 5}" r="4.5" fill="#333"/>')
        self.t(x + 28, y, label, size)

    def toggle(self, x, y, opts, cur, wseg=150):
        for i, s in enumerate(opts):
            self.box(x + i * wseg, y, wseg, 34, [s], 14, fill="#d9d9d9" if i == cur else "white", center=True)

    def progress(self, x, y, w, pct):
        self.r(x, y, w, 14, fill="white", rx=7)
        if pct:
            self.r(x, y, w * pct / 100, 14, fill="#555", stroke="#555", rx=7)

    def slider(self, x, y, w, pct, label):
        self.t(x, y, label, 14)
        self.p(f"M{x} {y + 18} H{x + w}", sw=3, stroke="#999")
        self.p(f"M{x} {y + 18} H{x + w * pct / 100}", sw=3)
        self.o.append(f'<circle cx="{x + w * pct / 100}" cy="{y + 18}" r="8" fill="white" stroke="#333" stroke-width="1.6"/>')

    def info(self, x, y):
        self.o.append(f'<circle cx="{x}" cy="{y - 5}" r="8" fill="white" stroke="#333" stroke-width="1.2"/>')
        self.t(x, y - 1, "i", 12, 700, "middle")

    def alert(self, x, y, w, lines, kind="warn"):
        h = 18 + 22 * len(lines) + 6
        def f():
            self.r(x, y, w, h, fill="#f2f2f2" if kind == "warn" else "white", sw=1.8 if kind == "warn" else 1.2,
                   dash=None if kind == "warn" else "6 4", tag=True)
            self.t(x + 22, y + 27, "!" if kind == "warn" else "i", 18, 700, "middle")
            for i, s in enumerate(lines):
                self.t(x + 44, y + 26 + 22 * i, s, 14, 700 if i == 0 else 400)
        self.group(f)
        return y + h

    def table(self, x, y, cols, rows, head=True, rh=32, size=14, bold_rows=()):
        total = sum(c for c, _ in cols)
        def f():
            self.r(x, y, total, rh * (len(rows) + (1 if head else 0)), tag=True, rx=2)
            yy = y
            if head:
                self.r(x, y, total, rh, fill="#e6e6e6", rx=2)
                cx = x
                for wc, s in cols:
                    self.t(cx + 10, y + 21, s, size, 700)
                    cx += wc
                yy += rh
            for ri, row in enumerate(rows):
                self.p(f"M{x} {yy} H{x + total}", sw=0.8, stroke="#999")
                cx = x
                for (wc, _), s in zip(cols, row):
                    if s:
                        self.t(cx + 10, yy + 21, s, size, 700 if ri in bold_rows else 400)
                    cx += wc
                yy += rh
        self.group(f)
        return y + rh * (len(rows) + (1 if head else 0))

    def bars(self, x, y, h, groups, series, maxv=100, bw=26, gap=60):
        """Gráfico de barras esquemático. groups=[rótulo]; series=[(padrão, [valores])]."""
        self.p(f"M{x} {y} V{y + h} H{x + len(groups) * (len(series) * bw + gap) + 10}", sw=1.2)
        for gi, g in enumerate(groups):
            gx = x + 20 + gi * (len(series) * bw + gap)
            for si, (fill, vals) in enumerate(series):
                v = vals[gi]
                bh = h * v / maxv
                self.o.append(f'<rect x="{gx + si * bw}" y="{y + h - bh}" width="{bw - 4}" height="{bh}" '
                              f'fill="{fill}" stroke="#333" stroke-width="1"/>')
                self.t(gx + si * bw + (bw - 4) / 2, y + h - bh - 6, f"{v}", 11, a="middle")
            self.t(gx + len(series) * bw / 2, y + h + 18, g, 13, a="middle")

    def badge(self, n, x, y):
        self.o.append(f'<circle cx="{x}" cy="{y}" r="12" fill="#111"/>')
        self.t(x, y + 5, str(n), 13, 700, "middle", "white")

    # ---------------------------------------------------------------- estrutura
    def chrome(self, nav_cur, step=None):
        self.t(20, 40, self.title, 24, 700)
        self.r(SX, SY, SW, SH, sw=2, rx=8)
        # barra superior
        self.r(SX, SY, SW, 56, fill="#e6e6e6", sw=2, rx=8)
        self.p(f"M{SX} {SY + 56} H{SX + SW}", sw=2)
        self.t(SX + 20, SY + 35, "Baja FEI · Segmentação off-road", 17, 700)
        for i, s in enumerate(["Início", "Nova análise", "Desempenho dos modelos"]):
            x = SX + 505 + i * 230
            cur = i == nav_cur
            self.o.append(f'<g data-box="{self.sid}-nav{i}">')
            self.r(x, SY + 11, 220, 34, fill="#333" if cur else "white", tag=True)
            self.t(x + 110, SY + 33, s, 14, 700 if cur else 400, "middle", "white" if cur else "#222")
            self.o.append("</g>")
        if step is not None:
            steps = ["1 Entrada", "2 Processamento", "3 Resultado", "4 Comparação"]
            y = SY + 86
            for i, s in enumerate(steps):
                x = SX + 40 + i * 285
                done = i < step
                self.o.append(f'<circle cx="{x + 12}" cy="{y}" r="12" fill="{"#333" if i <= step else "white"}" '
                              f'stroke="#333" stroke-width="1.4"/>')
                self.t(x + 12, y + 5, "✓" if done else str(i + 1), 13, 700, "middle", "white" if i <= step else "#333")
                self.t(x + 32, y + 5, s[2:], 15, 700 if i == step else 400)
                if i < 3:
                    self.p(f"M{x + 175} {y} H{x + 270}", sw=1.2, dash=None if done else "4 4")
        self.t(SX + 14, SY + SH - 12, self.sid, 16, 700)

    def notes(self, items):
        self.t(NX, 96, "O que mudou e por quê", 17, 700)
        y = 130
        for n, txt in items:
            self.badge(n, NX + 12, y - 5)
            for i, ln in enumerate(textwrap.wrap(txt, 40)):
                self.t(NX + 32, y + 20 * i, ln, 13.5)
            y += 20 * len(textwrap.wrap(txt, 40)) + 16

    def save(self):
        defs = ('<defs>'
                '<pattern id="trans" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
                '<rect width="10" height="10" fill="white"/><path d="M0 0 V10" stroke="#333" stroke-width="2.5"/></pattern>'
                '<pattern id="veg" width="12" height="12" patternUnits="userSpaceOnUse">'
                '<rect width="12" height="12" fill="white"/><circle cx="6" cy="6" r="2.2" fill="#333"/></pattern>'
                '<pattern id="ceu" width="8" height="8" patternUnits="userSpaceOnUse">'
                '<rect width="8" height="8" fill="#dcdcdc"/></pattern>'
                '</defs>')
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
               f'role="img" aria-labelledby="title desc">\n<title id="title">{escape(self.title)}</title>\n'
               f'<desc id="desc">{escape(self.desc)}</desc>\n{defs}\n<rect width="{W}" height="{H}" fill="white"/>\n'
               f'<g font-family="{FONT}">\n' + "\n".join(self.o) + "\n</g></svg>\n")
        OUT.mkdir(parents=True, exist_ok=True)
        name = OUT / f"{self.sid}.svg"
        name.write_text(svg, encoding="utf-8")
        print(name.name)


# ====================================================================== telas
def p00():
    s = WF("P00_inicio", "P00 · Início", "Tela inicial com os dois objetivos de uso.")
    s.chrome(0)
    s.t(SX + 60, SY + 130, "O que você quer fazer?", 26, 700)
    s.t(SX + 60, SY + 162, "Escolha pelo seu objetivo. Você pode trocar a qualquer momento pela barra acima.", 15)
    s.box(SX + 60, SY + 200, 520, 300, ["Analisar uma imagem ou vídeo", "",
          "Executar a segmentação com uma ou mais", "configurações, conferir o resultado e",
          "comparar as configurações na mesma imagem."], 16, bold_first=True)
    s.button(SX + 80, SY + 430, 260, "Começar análise  →")
    s.box(SX + 620, SY + 200, 520, 300, ["Comparar o desempenho dos modelos", "",
          "Ver as métricas consolidadas de um conjunto", "de imagens anotadas e preparar a",
          "recomendação para a reunião."], 16, bold_first=True)
    s.button(SX + 640, SY + 430, 260, "Ver desempenho  →")
    s.badge(1, SX + 40, SY + 100)
    s.badge(2, SX + 488, SY + 28)
    s.notes([
        (1, "Tela nova. Dois pontos de entrada, um por objetivo: analisar (T01, T02, T03) e comparar "
            "o desempenho consolidado (T04, T05). Resposta à simulação: \"não entendi como as telas se conectam\"."),
        (2, "Barra de navegação fixa em todas as telas, com a tela atual destacada (mesma observação)."),
        (3, "Sem login, cadastro ou histórico: sistema local e de uso da equipe (E1 §8; H08 não sustentada)."),
    ])
    s.save()


def p01(error=False):
    sid = "P01E_entrada_erro" if error else "P01_nova_analise"
    s = WF(sid, "P01-E · Nova análise: arquivo inválido" if error else "P01 · Nova análise",
           "Entrada de dados e escolha das configurações.")
    s.chrome(1, step=0)
    y0 = SY + 130
    s.t(SX + 40, y0, "1. Imagem ou vídeo", 18, 700)
    if error:
        s.box(SX + 40, y0 + 20, 520, 170, ["Arraste um arquivo aqui ou clique", "para selecionar",
              "", "JPG, PNG ou MP4 · até 2 GB"], 15, dash="8 6", center=True)
        s.alert(SX + 40, y0 + 205, 520, ["Formato não suportado: trilha_04.heic",
                                         "Converta para JPG, PNG ou MP4 e selecione de novo."])
    else:
        s.r(SX + 40, y0 + 20, 520, 110)
        s.image(SX + 54, y0 + 32, 120, 86, "prévia")
        s.t(SX + 192, y0 + 66, f"{ARQ}  ✓", 15, 700)
        s.t(SX + 192, y0 + 92, "3,2 MB · imagem · 1920 × 1080", 14)
        s.button(SX + 400, y0 + 140, 160, "Trocar arquivo", "secondary")
    ya = y0 + 300
    s.t(SX + 40, ya, "Anotação de referência (opcional)", 16, 700)
    s.info(SX + 368, ya)
    s.box(SX + 40, ya + 14, 520, 92, ["Com a máscara anotada, calculamos IoU e acurácia.",
          "Sem ela, a avaliação é visual, com apoio da confiança", "do modelo."], 14, fill="#f7f7f7")
    s.button(SX + 40, ya + 120, 260, "Adicionar anotação", "secondary")

    x2 = SX + 620
    s.t(x2, y0, "2. Configurações a executar", 18, 700)
    s.t(x2, y0 + 28, "Uma para analisar; duas ou mais para comparar.", 14)
    for i, (on, name, d) in enumerate([(True, CFG[0], "Configuração principal do TCC"),
                                       (True, CFG[1], "Backbone menor, mais rápida"),
                                       (False, CFG[2], "Arquitetura alternativa")]):
        yy = y0 + 80 + i * 70
        s.check(x2 + 10, yy, on, name, 16)
        s.info(x2 + 290, yy)
        s.t(x2 + 38, yy + 22, d, 13.5, fill="#555")
    s.box(x2, y0 + 300, 520, 70, ["Os parâmetros de cada configuração vêm do TCC", "e não são alterados aqui."],
          14, fill="#f7f7f7")
    s.button(SX + 40, SY + SH - 80, 160, "Voltar", "secondary")
    if error:
        s.button(SX + SW - 360, SY + SH - 80, 320, "Executar segmentação  ▷", "disabled")
    else:
        s.button(SX + SW - 360, SY + SH - 80, 320, "Executar segmentação  ▷")
    s.badge(1, SX + 30, y0 + 70)
    s.badge(2, SX + 30, ya + 60)
    s.badge(3, x2 - 12, y0 + 150)
    s.badge(4, SX + SW - 30, SY + SH - 100)
    s.badge(5, SX + 1090, SY + 86)
    notes = [
        (1, "Formatos corrigidos (\"JPNG\" → JPG, PNG ou MP4). Prévia do arquivo para confirmar que é o certo "
            "(T03, 1.1)." if not error else
            "Estado de erro: diz o que houve e o que fazer, sem código (T03, 2.3.2). O arquivo inválido "
            "não avança."),
        (2, "\"Calcular métricas\" virou \"Anotação de referência\": sem máscara anotada não existe IoU "
            "(INC-52)."),
        (3, "Lista explícita com nomes reais e descrição curta (F01; simulação: \"modelo A e modelo B\")."
            " Removidos \"Configurações avançadas\" (fora da E1) e \"Salvar no histórico\" (H08)."),
        (4, "Executar só habilita com arquivo válido e ao menos uma configuração." if not error else
            "Executar desabilitado enquanto o arquivo for inválido."),
        (5, "Indicador de etapas: mostra onde a pessoa está no fluxo (simulação: telas sem conexão)."),
    ]
    s.notes(notes)
    s.save()


def p02(fail=False):
    sid = "P02F_falha_execucao" if fail else "P02_processando"
    s = WF(sid, "P02-F · Processamento: falha em uma configuração" if fail else "P02 · Processando",
           "Acompanhamento do processamento por configuração.")
    s.chrome(1, step=1)
    y0 = SY + 140
    s.t(SX + 40, y0, f"Processando {ARQ}", 20, 700)
    s.t(SX + 40, y0 + 28, "Você pode ver o resultado de uma configuração assim que ela terminar.", 15)
    rows = [(CFG[0], "Concluído", 100), (CFG[1], "Falhou" if fail else "Processando: segmentando a imagem", 0 if fail else 45)]
    for i, (n, st, pct) in enumerate(rows):
        yy = y0 + 70 + i * 110
        s.box(SX + 40, yy, 1120, 92, [n], 16, bold_first=True)
        s.t(SX + 60, yy + 56, st + ("" if pct in (0, 100) else f" · {pct}%"), 15, 700 if st == "Falhou" else 400)
        if not (fail and i == 1):
            s.progress(SX + 470, yy + 46, 440, pct)
        if i == 0:
            s.button(SX + 940, yy + 26, 200, "Ver resultado", "secondary")
    ya = y0 + 300
    if fail:
        ya = s.alert(SX + 40, ya, 1120, [f"Não foi possível processar com {CFG[1]}.",
                                         "Motivo: memória insuficiente neste computador.",
                                         "Você pode tentar de novo ou continuar só com as configurações que terminaram."])
        s.button(SX + 40, ya + 20, 220, "Tentar de novo", "secondary")
        s.button(SX + 280, ya + 20, 320, "Continuar sem esta configuração", "secondary")
    s.button(SX + 40, SY + SH - 80, 160, "Cancelar", "secondary")
    s.button(SX + SW - 360, SY + SH - 80, 320, "Ver resultados  →", "primary" if fail else "disabled")
    s.badge(1, SX + 30, y0 + 120)
    s.badge(2, SX + 1150, y0 + 96)
    if fail:
        s.badge(3, SX + 30, SY + 470)
    notes = [
        (1, "Tela nova. Estado de cada configuração: processando, concluído ou falhou, com progresso. "
            "Resposta à simulação: \"não entendi o progresso de segmentação\" (RC04, F03)."),
        (2, "O resultado de uma configuração pode ser aberto enquanto as outras processam (CTT T03: "
            "S2 |[]| 2.2)."),
    ]
    if fail:
        notes.append((3, "Falha explicada em linguagem de usuário, com as duas saídas do HTA T03 (2.3.2.2): "
                         "repetir ou retirar a configuração."))
    else:
        notes.append((3, "Texto descreve a execução (\"segmentando\"), nunca \"treinando\": Rafael só "
                         "executa modelos prontos."))
    s.notes(notes)
    s.save()


def p03(no_metrics=False):
    sid = "P03S_resultado_sem_metricas" if no_metrics else "P03_resultado"
    s = WF(sid, "P03-S · Resultado sem anotação (sobreposição)" if no_metrics else "P03 · Resultado",
           "Avaliação da segmentação de uma imagem.")
    s.chrome(1, step=2)
    y0 = SY + 126
    s.t(SX + 40, y0, f"Resultado · {ARQ}", 19, 700)
    s.toggle(SX + 40, y0 + 14, [CFG[0], CFG[1]], 0, wseg=260)
    s.toggle(SX + 600, y0 + 14, ["Lado a lado", "Sobreposição"], 1 if no_metrics else 0, wseg=140)
    vy = y0 + 64
    if no_metrics:
        s.mask(SX + 40, vy, 680, 330, overlay=True, low_conf=True)
        s.slider(SX + 40, vy + 356, 260, 60, "Opacidade da máscara: 60%")
    else:
        s.image(SX + 40, vy, 335, 330)
        s.mask(SX + 385, vy, 335, 330)
        s.t(SX + 40, vy + 352, "Imagem original", 14)
        s.t(SX + 385, vy + 352, "Segmentação", 14)
    s.box(SX + 580, vy + 340, 140, 34, ["−  100%  +"], 14, center=True)
    s.legend(SX + 40, vy + 412)

    x2 = SX + 760
    s.t(x2, y0 + 70, "Métricas desta imagem", 16, 700)
    s.info(x2 + 232, y0 + 70)
    if no_metrics:
        ya = s.alert(x2, y0 + 86, 400, ["Métricas indisponíveis", "Esta imagem não tem anotação",
                                        "de referência. Avalie pela imagem", "e pela confiança do modelo."], "info")
    else:
        ya = s.table(x2, y0 + 86, [(220, "Medida"), (180, "Valor")],
                     [["IoU médio", "75%"], ["  Transitável", "80%"], ["  Vegetação", "50%"],
                      ["  Céu", "95%"], ["Acurácia", "91%"]], bold_rows=(0,), rh=30)
    s.check(x2, ya + 34, no_metrics, "Mostrar confiança do modelo [H]", 14)
    yb = ya + 66
    s.t(x2, yb, "Sua avaliação", 16, 700)
    for i, (on, lab) in enumerate([(False, "Adequada"), (not no_metrics, "Inadequada"), (no_metrics, "Inconclusiva")]):
        s.radio(x2 + i * 130, yb + 30, on, lab, 14)
    s.t(x2, yb + 62, "Se inadequada, o problema parece estar:", 14)
    s.radio(x2, yb + 88, True, "na imagem", 14)
    s.radio(x2 + 140, yb + 88, False, "no modelo", 14)
    s.box(x2, yb + 102, 400, 44, ["Observação (opcional)"], 14, fill="#f7f7f7")
    s.button(SX + 40, SY + SH - 80, 200, "Nova análise", "secondary")
    s.button(SX + SW - 360, SY + SH - 80, 320, "Comparar configurações  →")
    s.badge(1, SX + 30, y0 + 30)
    s.badge(2, SX + 870, y0 + 10)
    s.badge(3, SX + 30, vy + 425)
    s.badge(4, x2 - 14, y0 + 66)
    s.badge(5, x2 - 14, yb - 4)
    s.badge(6, SX + SW - 30, SY + SH - 100)
    s.notes([
        (1, "Seletor de configuração com nomes reais, no lugar do menu \"Modelo\" que parecia executar "
            "de novo (simulação: \"modelo A e modelo B\")."),
        (2, "Dois modos: lado a lado ou sobreposição com opacidade, e zoom (T01, métodos 1.A e 1.B; P01, "
            "decisão 1)."),
        (3, "Mesma legenda e mesmos padrões na máscara, nos gráficos e em todas as telas (P01, decisão 2). "
            "Classes a confirmar com o TCC (INC-12)."),
        (4, "Métricas coerentes (IoU médio = média das classes) e só quando há anotação; sem ela, "
            "mensagem e confiança do modelo (INC-52; T01 3.B)." if not no_metrics else
            "Sem anotação: métricas indisponíveis e confiança ligada, com região de baixa confiança "
            "destacada (T01, 3.B) [H]."),
        (5, "Registro da avaliação, separando problema da imagem e do modelo: ruptura central do C01 "
            "(T01, 3.A)."),
        (6, "Removidos \"Exportar PDF\" e \"Salvar relatório\" desta tela: fora do recorte da E1."),
    ])
    s.save()


def p04():
    s = WF("P04_comparar_configuracoes", "P04 · Comparar configurações na mesma imagem",
           "Imagens segmentadas lado a lado e conclusão registrada pelo usuário.")
    s.chrome(1, step=3)
    y0 = SY + 126
    s.t(SX + 40, y0, f"Comparar configurações · {ARQ}", 19, 700)
    s.check(SX + 820, y0, True, "Zoom sincronizado", 14)
    cw, ch, gy = 360, 230, y0 + 22
    cols = [("Imagem original", None), (CFG[0], "IoU médio 75% · avaliada: inadequada"),
            (CFG[1], "IoU médio 71% · avaliada: inadequada")]
    for i, (name, sub) in enumerate(cols):
        x = SX + 40 + i * (cw + 20)
        s.t(x, gy + 18, name, 15, 700)
        if sub is None:
            s.image(x, gy + 30, cw, ch)
        else:
            s.mask(x, gy + 30, cw, ch)
            s.t(x, gy + ch + 52, sub, 13.5)
    s.legend(SX + 40, gy + ch + 82)
    ty = gy + ch + 70
    s.t(SX + 240, ty + 12, "Métricas por classe (imagem com anotação)", 15, 700)
    s.table(SX + 240, ty + 24, [(140, "Classe"), (230, CFG[0]), (230, CFG[1])],
            [["Transitável", "80%", "74%"], ["Vegetação", "50%", "48%"], ["Céu", "95%", "91%"],
             ["IoU médio", "75%", "71%"]], rh=28, bold_rows=(3,))
    x2 = SX + 870
    s.t(x2, ty + 12, "Sua conclusão", 16, 700)
    s.radio(x2, ty + 44, True, "Indicar a mais adequada:", 14)
    s.box(x2 + 28, ty + 54, 270, 32, [f"{CFG[0]} ▾"], 13.5)
    s.radio(x2, ty + 112, False, "Nenhuma é adequada", 14)
    s.radio(x2, ty + 140, False, "Inconclusiva", 14)
    s.box(x2, ty + 154, 300, 40, ["Motivo"], 14, fill="#f7f7f7")
    s.button(SX + 40, SY + SH - 80, 240, "Voltar ao resultado", "secondary")
    s.button(SX + SW - 360, SY + SH - 80, 320, "Registrar conclusão")
    s.badge(1, SX + 30, gy + 60)
    s.badge(2, SX + 1150, gy + 20)
    s.badge(3, x2 - 14, ty + 8)
    s.badge(4, SX + 230, ty + 8)
    s.notes([
        (1, "Tela nova. Imagens segmentadas de cada configuração lado a lado, junto da original. Resposta à "
            "simulação: \"gostaria de ver as imagens segmentadas\" (T03, 4.1; C03)."),
        (2, "Zoom sincronizado: ao ampliar uma região, todas acompanham (\"mesma região\", T03 4.1)."),
        (3, "A conclusão é da pessoa, não do sistema. Remove a conclusão automática da versão em papel, "
            "que contradizia os números (T03, 4.2)."),
        (4, "Nomes reais em vez de \"Modelo A/B\" (simulação). Números coerentes com a P03."),
        (5, "Comunicar à equipe fica fora da interface (T03, 4.3); exportar continua hipótese."),
    ])
    s.save()


def p05(missing=False):
    sid = "P05F_execucao_faltante" if missing else "P05_desempenho_consolidado"
    s = WF(sid, "P05-F · Desempenho: execução faltante" if missing else "P05 · Desempenho dos modelos",
           "Comparação consolidada sobre um conjunto anotado e recomendação.")
    s.chrome(2)
    y0 = SY + 120
    s.t(SX + 40, y0, "Conjunto anotado:", 15, 700)
    s.box(SX + 210, y0 - 22, 410, 34, ["Pista FEI · ciclo out/2026 · 120 imagens ▾"], 14)
    s.t(SX + 650, y0, "Execuções: 2 de 3 modelos" if missing else "Execuções: 3 de 3 modelos ✓", 15, 700)
    s.toggle(SX + 940, y0 - 22, ["Tabela", "Gráfico"], 0, wseg=110)
    rows = [[CFG[0], "78%", "91%", "84%", "57%", "93%"],
            [CFG[1], "76%", "90%", "82%", "55%", "91%"],
            [CFG[2], "— sem execução", "", "", "", ""] if missing else [CFG[2], "69%", "86%", "76%", "45%", "86%"]]
    ty = s.table(SX + 40, y0 + 26, [(250, "Modelo"), (170, "IoU médio"), (130, "Acurácia"),
                                    (140, "Transitável"), (140, "Vegetação"), (110, "Céu")], rows, rh=34)
    s.info(SX + 395, y0 + 46)
    s.info(SX + 560, y0 + 46)
    s.t(SX + 40, ty + 24, "Referência: melhor IoU médio do ciclo anterior (set/2026) = 74%", 14)
    ya = ty + 40
    if missing:
        ya = s.alert(SX + 40, ya, 980, [f"{CFG[2]} ainda não foi executado neste conjunto.",
                                         "A comparação mostra só os modelos executados. Peça a execução ao responsável "
                                         "técnico."])
    else:
        ya = s.alert(SX + 40, ya, 980, ["Diferença pequena entre os dois primeiros",
                                        f"{CFG[0]} e {CFG[1]} diferem 2 pontos no IoU médio. A diferença pode não "
                                        "ser relevante."])
        s.box(SX + 40, ya + 12, 980, 52, ["IoU: o quanto a área prevista coincide com a anotada, de 0 a 100%.",
                                          "Não indica se o trajeto é seguro ou transitável."], 13.5, fill="#f7f7f7")
        ya += 64
    ry = ya + 34
    s.t(SX + 40, ry, "Recomendação para a reunião", 16, 700)
    s.radio(SX + 40, ry + 32, not missing, "Recomendar:", 14)
    s.box(SX + 170, ry + 12, 270, 32, [f"{CFG[0]} ▾"], 13.5)
    s.radio(SX + 470, ry + 32, False, "Recomendar com ressalva", 14)
    s.radio(SX + 760, ry + 32, missing, "Adiar e pedir execuções", 14)
    s.box(SX + 40, ry + 52, 980, 40, ["Justificativa (aparece no resumo)"], 14, fill="#f7f7f7")
    s.button(SX + 40, SY + SH - 80, 260, "Ver imagens de exemplo", "secondary")
    s.button(SX + SW - 360, SY + SH - 80, 320, "Exportar resumo [H]")
    s.badge(1, SX + 40, y0 - 40)
    s.badge(2, SX + 1016, y0 + 44)
    s.badge(3, SX + 1036, ty + 60)
    s.badge(4, SX + 30, ry - 6)
    s.badge(5, SX + SW - 30, SY + SH - 100)
    notes = [
        (1, "Tela nova para a T04/T05 (Larissa): métricas consolidadas de um conjunto anotado, não de "
            "uma imagem. A versão em papel comparava uma imagem só."),
        (2, "Valor de referência e explicação dos termos no ponto de uso (T04 2.3; RC01). Tabela ou "
            "gráfico (RC03)."),
        (3, "Aviso de diferença pequena: apoia a recomendação com ressalva (T05, 3.2)." if not missing else
            "Execução faltante: a tela diz o que falta e quem resolve; o pedido é fora da interface "
            "(T05, 1.2)."),
        (4, "As três saídas da T05 (3.1, 3.2, 3.3). A decisão é da gestora; a tela não escolhe."),
        (5, "Exportar resumo só aqui e marcado [H]: fora do recorte da E1 até decisão da equipe "
            "(T05, 4.1.1). \"Ver imagens de exemplo\" abre a P04 com imagens do conjunto."),
    ]
    s.notes(notes)
    s.save()


def mapa():
    s = WF("mapa_navegacao", "Mapa de navegação · versão 2", "Estados e transições do protótipo revisado.")
    s.o.append('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
               'orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#333"/></marker></defs>')
    s.t(20, 40, s.title, 24, 700)
    s.t(20, 68, "Retângulo cheio = tela; tracejado = estado da mesma tela. A barra superior leva a "
                "Início, Nova análise e Desempenho em qualquer tela.", 14)
    nodes = {
        "P00": (90, 400, "P00 · Início", False),
        "P01": (390, 250, "P01 · Nova análise", False),
        "P01E": (390, 110, "P01-E · Arquivo inválido", True),
        "P02": (700, 250, "P02 · Processando", False),
        "P02F": (700, 110, "P02-F · Falha", True),
        "P03": (1010, 250, "P03 · Resultado", False),
        "P03S": (1010, 110, "P03-S · Sem anotação", True),
        "P04": (1320, 250, "P04 · Comparar", False),
        "P05": (390, 600, "P05 · Desempenho", False),
        "P05F": (390, 760, "P05-F · Execução faltante", True),
    }
    bw, bh = 240, 56
    for k, (x, y, lab, st) in nodes.items():
        s.box(x, y, bw, bh, [lab], 15, dash="7 5" if st else None, center=True, fill="#f7f7f7" if st else "white")

    def edge(a, b, label, dy=0, bend=None):
        xa, ya = nodes[a][0], nodes[a][1]
        xb, yb = nodes[b][0], nodes[b][1]
        anchor = "middle"
        if bend == "up":
            d = f"M{xa + bw / 2 - 30} {ya} V{yb + bh}"
            lx, ly, anchor = xa + bw / 2 - 38, (ya + yb + bh) / 2 + 4, "end"
        elif bend == "down":
            d = f"M{xa + bw / 2 + 30} {ya + bh} V{yb}"
            lx, ly, anchor = xb + bw / 2 + 38, (ya + yb + bh) / 2 + 4, "start"
        elif xa < xb and abs(ya - yb) < 5:
            d = f"M{xa + bw} {ya + bh / 2 + dy} H{xb}"
            lx, ly = (xa + bw + xb) / 2, ya - 10
        elif xa > xb and abs(ya - yb) < 5:
            d = f"M{xa} {ya + bh / 2 + dy} H{xb + bw}"
            lx, ly = (xa + xb + bw) / 2, ya + bh / 2 + dy + 18
        else:
            d = f"M{xa + bw} {ya + bh / 2} C{xa + bw + 60} {ya + bh / 2} {xb - 60} {yb + bh / 2} {xb} {yb + bh / 2}"
            lx, ly = (xa + bw + xb) / 2 + 10, (ya + yb) / 2 + bh / 2 - 10
        s.o.append(f'<path d="{d}" fill="none" stroke="#333" stroke-width="1.4" marker-end="url(#ar)"/>')
        if label:
            s.t(lx, ly, label, 12.5, a=anchor)

    edge("P00", "P01", "Começar análise")
    edge("P00", "P05", "Ver desempenho")
    edge("P01", "P01E", "arquivo inválido", bend="up")
    edge("P01E", "P01", "novo arquivo", bend="down")
    edge("P01", "P02", "Executar")
    edge("P02", "P02F", "falha", bend="up")
    edge("P02F", "P02", "Tentar de novo", bend="down")
    edge("P02", "P03", "Ver resultado(s)")
    edge("P03", "P03S", "sem anotação", bend="up")
    edge("P03", "P04", "Comparar (≥ 2)")
    edge("P04", "P03", "Voltar", dy=18)
    edge("P05", "P05F", "falta execução", bend="down")
    s.o.append(f'<path d="M{390 + bw} {600 + bh / 2} C{900} {640} {1300} {560} {1320 + bw / 2} {250 + bh}" '
               f'fill="none" stroke="#333" stroke-width="1.4" stroke-dasharray="6 4" marker-end="url(#ar)"/>')
    s.t(900, 600, "Ver imagens de exemplo (P04 com imagens do conjunto)", 12.5)
    s.o.append(f'<path d="M{700 + bw} {110 + bh / 2} C{975} {110 + bh / 2} {975} {250 + bh / 2 - 12} {1010} {250 + bh / 2 - 12}" '
               f'fill="none" stroke="#333" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#ar)"/>')
    s.t(944, 184, "continuar sem ela", 12.5)
    s.box(1010, 690, 550, 150, ["Tarefas cobertas", "T02 · P01 → P02 (executar)",
          "T01 · P03, P03-S (avaliar uma imagem)", "T03 · P01 → P02 → P03 → P04 (comparar configurações)",
          "T04, T05 · P05, P05-F (comparar o consolidado e decidir)"], 14, bold_first=True)
    s.save()


if __name__ == "__main__":
    p00(); p01(); p01(error=True); p02(); p02(fail=True); p03(); p03(no_metrics=True); p04(); p05(); p05(missing=True)
    mapa()
