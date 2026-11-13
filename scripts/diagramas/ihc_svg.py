"""Biblioteca para gerar diagramas HTA e CTT (Entrega 5) e mapas de objetivos (Entrega 9) em SVG.

Usa apenas a biblioteca padrão do Python 3. Cada diagrama é descrito em um
arquivo próprio (ex.: hta_t05.py) que importa este módulo.

Notação seguida (Barbosa e Silva, 2010):
- HTA: retângulo = objetivo; operação (folha) = retângulo com traço duplo
  abaixo; plano dentro do objetivo decomposto (1 > 2, 1 / 2, 1 + 2).
- CTT: nuvem = abstrata; pessoa = usuário; pessoa + computador = interação;
  computador = sistema; operadores temporais entre tarefas irmãs.
"""
from xml.sax.saxutils import escape

W = 1440
FONT = "DejaVu Sans, Arial, sans-serif"
CLOUD = ("M17 46 C2 46 0 31 10 25 C4 12 16 3 27 9 C32 0 46 -1 51 8 C61 0 76 5 76 16 "
         "C90 16 93 33 81 38 C84 51 68 57 59 49 C50 59 34 58 30 50 C25 54 19 52 17 46 Z")


class Svg:
    def __init__(self, title, desc):
        self.title, self.desc = title, desc
        self.out = []
        self.panels = []  # (titulo, y) dos painéis de CTT, para recortes
        self._bid = 0

    # ------------------------------------------------------------ primitivas
    def text(self, x, y, s, size=16, weight=400, anchor="middle", cls=None):
        c = f' class="{cls}"' if cls else ""
        self.out.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" '
                        f'font-weight="{weight}"{c}>{escape(s)}</text>')

    def path(self, d, w=1.6, arrow=False, fill="none"):
        m = ' marker-end="url(#arrow)"' if arrow else ""
        self.out.append(f'<path d="{d}" fill="{fill}" stroke="#333" stroke-width="{w}"{m}/>')

    def header(self, title, subtitle):
        self.text(40, 40, title, size=25, weight=700, anchor="start")
        self.text(40, 73, subtitle, anchor="start")
        return 100

    def section(self, y, title):
        self.path(f"M40 {y} H1400")
        self.text(40, y + 30, title, size=18, weight=700, anchor="start")
        return y + 52

    def note(self, y, lines, size=14):
        for i, s in enumerate(lines):
            self.text(40, y + 20 * i, s, size=size, anchor="start")
        return y + 20 * len(lines)

    # ------------------------------------------------------------ HTA
    def box(self, cx, y, w, h, lines, plan=None, op=False, dashed=False):
        self._bid += 1
        x = cx - w / 2
        dash = ' stroke-dasharray="8 5"' if dashed else ""
        self.out.append(f'<g data-box="b{self._bid}">')
        self.out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" fill="white" '
                        f'stroke="#333" stroke-width="1.6"{dash} class="frame"/>')
        for i, s in enumerate(lines):
            self.text(cx, y + 26 + 23 * i, s)
        if plan:
            self.text(cx, y + h - 15, plan, size=14, weight=700)
        self.out.append("</g>")
        if op:
            self.path(f"M{x:.1f} {y + h + 5} H{x + w:.1f}")
            self.path(f"M{x:.1f} {y + h + 9} H{x + w:.1f}")

    @staticmethod
    def _height(nodes):
        nl = max(len(n["lines"]) for n in nodes)
        hasplan = any(n.get("plan") for n in nodes)
        return 18 + 23 * nl + (34 if hasplan else 12)

    def tree(self, parent, children, y, x0=40, x1=1400, gap=30, pw=520):
        """Pai centrado em [x0, x1] e filhos distribuídos. Retorna o y final."""
        cx = (x0 + x1) / 2
        ph = self._height([parent])
        self.box(cx, y, pw, ph, parent["lines"], parent.get("plan"), parent.get("op", False),
                 parent.get("dashed", False))
        n = len(children)
        cw = (x1 - x0 - gap * (n - 1)) / n
        ch = self._height(children)
        cy, bar = y + ph + 70, y + ph + 31
        centers = [x0 + cw / 2 + i * (cw + gap) for i in range(n)]
        self.path(f"M{cx} {y + ph} V{bar}")
        self.path(f"M{centers[0]:.1f} {bar} H{centers[-1]:.1f}")
        for c, node in zip(centers, children):
            self.path(f"M{c:.1f} {bar} V{cy}", arrow=True)
            self.box(c, cy, cw, ch, node["lines"], node.get("plan"), node.get("op", False),
                     node.get("dashed", False))
        return cy + ch + 14

    def hta_legend(self, y):
        y = self.section(y, "Legenda (Barbosa e Silva, 2010)")
        self.box(140, y, 180, 50, ["objetivo"])
        self.box(360, y, 180, 50, ["operação"], op=True)
        self.text(480, y + 22, "Planos: 1 > 2 sequencial · 1 / 2 seleção (depende das circunstâncias) · "
                  "1 + 2 paralelo (não usado).", size=14, anchor="start")
        self.text(480, y + 44, "Operações (folhas) têm traço duplo abaixo. [H]: modelo hipotético a "
                  "validar na Entrega 7.", size=14, anchor="start")
        return y + 90

    # ------------------------------------------------------------ CTT
    def _person(self, cx, top):
        self.out.append(f'<circle cx="{cx}" cy="{top + 12}" r="10" fill="white" stroke="#333" stroke-width="1.8"/>')
        self.path(f"M{cx - 19} {top + 58} V{top + 35} Q{cx - 19} {top + 25} {cx} {top + 25} "
                  f"Q{cx + 19} {top + 25} {cx + 19} {top + 35} V{top + 58} Z "
                  f"M{cx - 9} {top + 41} V{top + 58} M{cx + 9} {top + 41} V{top + 58}")

    def _monitor(self, cx, top):
        self.out.append(f'<rect x="{cx - 24}" y="{top + 8}" width="48" height="34" rx="3" fill="white" '
                        f'stroke="#333" stroke-width="1.8"/>')
        self.out.append(f'<rect x="{cx - 18}" y="{top + 14}" width="36" height="22" fill="none" '
                        f'stroke="#333" stroke-width="1.2"/>')
        self.path(f"M{cx} {top + 42} V{top + 50} M{cx - 14} {top + 54} H{cx + 14} M{cx - 8} {top + 50} H{cx + 8}")

    def icon(self, kind, cx, top):
        if kind == "A":
            self.out.append(f'<path transform="translate({cx - 46},{top})" d="{CLOUD}" fill="white" '
                            f'stroke="#333" stroke-width="1.8"/>')
        elif kind == "U":
            self._person(cx, top)
        elif kind == "S":
            self._monitor(cx, top)
        elif kind == "I":
            self._monitor(cx - 30, top)
            self._person(cx + 32, top)
            y = top + 30
            self.out.append(f'<path d="M{cx - 4} {y} H{cx + 8}" stroke="#333" stroke-width="5" fill="none"/>')
            self.out.append(f'<path d="M{cx - 6} {y - 6} L{cx - 12} {y} L{cx - 6} {y + 6} Z '
                            f'M{cx + 10} {y - 6} L{cx + 16} {y} L{cx + 10} {y + 6} Z" fill="#333"/>')
        else:
            raise ValueError(kind)

    def node(self, cx, top, kind, lines):
        self.icon(kind, cx, top)
        for i, s in enumerate(lines):
            self.text(cx, top + 80 + 21 * i, s)
        return top + 80 + 21 * (len(lines) - 1)

    def operator(self, xa, xb, y, op):
        self.path(f"M{xa} {y} H{xb}")
        mid = (xa + xb) / 2
        wbox = 14 * len(op) + 18
        self.out.append(f'<rect x="{mid - wbox / 2}" y="{y - 17}" width="{wbox}" height="32" fill="white"/>')
        self.text(mid, y + 6, op, size=18, weight=700)

    def panel(self, y, title, parent, children, ops, x0=40, x1=1400, note=None):
        """parent = (tipo, linhas); children = [(tipo, linhas)]; ops entre irmãs.
        tipo: A abstrata, U usuário, I interação, S sistema."""
        self.panels.append((title, y))
        if title:
            y = self.section(y, title) + 2
        cx = (x0 + x1) / 2
        pb = self.node(cx, y, *parent)
        ytop = pb + 40
        n = len(children)
        slot = (x1 - x0) / n
        centers = [x0 + slot * (i + 0.5) for i in range(n)]
        for c in centers:
            self.path(f"M{cx} {pb + 14} L{c} {ytop}")
        bottoms = [self.node(c, ytop, k, lines) for c, (k, lines) in zip(centers, children)]
        half = 62 if n <= 2 else 58
        for i, op in enumerate(ops):
            self.operator(centers[i] + half, centers[i + 1] - half, ytop + 30, op)
        yb = max(bottoms) + 22
        if note:
            yb = self.note(yb + 14, note)
        return yb + 18

    def divider(self, x, y0, y1):
        self.path(f"M{x} {y0} V{y1}", w=0.8)

    def ctt_legend(self, y, ops, letters):
        self.legend_y = y
        y = self.section(y, "Legenda (Barbosa e Silva, 2010; Paternò, 1999)") + 2
        for i, (k, s) in enumerate([("A", "Abstrata"), ("U", "Usuário"), ("I", "Interação"), ("S", "Sistema")]):
            cx = 120 + i * 200
            self.icon(k, cx, y)
            self.text(cx, y + 80, s)
        for i, s in enumerate(ops):
            self.text(880, y + 10 + 24 * i, s, size=15, anchor="start")
        yy = y + 10 + 24 * len(ops)
        for i, s in enumerate(letters):
            self.text(880, yy + 20 * i, s, size=14, anchor="start")
        return max(y + 140, yy + 20 * len(letters) + 20)

    # ------------------------------------------------------------ saída
    def render(self, height, viewbox_y=0, view_h=None, label=None):
        vh = view_h or height
        aria = f'aria-label="{escape(label)}"' if label else 'aria-labelledby="title desc"'
        return "\n".join([
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{vh}" '
            f'viewBox="0 {viewbox_y} {W} {vh}" role="img" {aria}>',
            f'<title id="title">{escape(self.title)}</title>',
            f'<desc id="desc">{escape(self.desc)}</desc>',
            '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" '
            'markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#333"/></marker></defs>',
            f'<rect width="{W}" height="{height}" fill="white"/>',
            f'<g font-family="{FONT}" fill="#222">',
            *self.out,
            "</g></svg>",
        ]) + "\n"

    def save(self, path, height):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.render(height))

    def save_crops(self, base_path, height, crops):
        """crops = [(sufixo, índice do painel inicial, índice do painel final ou None, rótulo)].
        Índices referem-se aos painéis com título, na ordem em que foram desenhados;
        None no fim significa até o final do diagrama."""
        starts = [y for t, y in self.panels if t is not None]
        for suf, i0, i1, label in crops:
            y0 = 0 if i0 == 0 else starts[i0]
            y1 = height if i1 is None else starts[i1]
            with open(base_path.replace(".svg", f"_{suf}.svg"), "w", encoding="utf-8") as f:
                f.write(self.render(height, viewbox_y=y0, view_h=y1 - y0, label=label))


def N(lines, plan=None, op=False, dashed=False):
    """Nó de HTA: lines = linhas do rótulo; plan = plano abreviado; op = operação (folha).
    dashed = contorno tracejado (usado no mapa de objetivos da Entrega 9 para objetivos
    alcançados fora do sistema)."""
    return {"lines": lines, "plan": plan, "op": op, "dashed": dashed}
