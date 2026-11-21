"""Elementos de diagramas MoLIC em SVG (Entrega 10).

Usa a classe Svg de ihc_svg.py (cabeçalho, seções, texto e saída). Notação seguida
(Barbosa e Silva, 2010; aulas de MoLIC, partes A e B):
- cena: retângulo arredondado com o tópico em cima e os diálogos embaixo;
- cena de alerta ou de confirmação: cena com contorno tracejado;
- processo do sistema: quadrado preto;
- acesso ubíquo: retângulo arredondado cinza, sem texto;
- ponto de abertura: círculo preenchido; ponto de encerramento: círculo duplo;
- fala de transição: seta contínua com a fala (u: usuário; d: preposto do designer);
- fala de recuperação de ruptura: seta tracejada.
"""
from xml.sax.saxutils import escape


class Molic:
    def __init__(self, svg):
        self.s = svg
        self.out = svg.out

    # ------------------------------------------------------------ elementos
    def scene(self, cx, y, w, title, dialogs, dashed=False):
        """Cena: title = linhas do tópico; dialogs = linhas dos diálogos. Retorna a caixa."""
        h = 14 + 21 * len(title) + 10 + 19 * len(dialogs) + 12
        x = cx - w / 2
        dash = ' stroke-dasharray="9 6"' if dashed else ""
        self.s._bid += 1
        self.out.append(f'<g data-box="b{self.s._bid}">')
        self.out.append(f'<rect x="{x:.1f}" y="{y}" width="{w}" height="{h}" rx="14" fill="white" '
                        f'stroke="#333" stroke-width="1.6"{dash} class="frame"/>')
        ty = y + 26
        for line in title:
            self.s.text(cx, ty, line, size=15, weight=700)
            ty += 21
        sep = ty - 8
        self.out.append(f'<path d="M{x:.1f} {sep} H{x + w:.1f}" stroke="#333" stroke-width="1"{dash} fill="none"/>')
        dy = sep + 22
        for line in dialogs:
            stripped = line.lstrip(" ")
            line = "\u00a0" * (len(line) - len(stripped)) + stripped
            self.s.text(x + 14, dy, line, size=13, anchor="start")
            dy += 19
        self.out.append("</g>")
        return {"x": x, "y": y, "w": w, "h": h, "cx": cx, "cy": y + h / 2, "r": x + w, "b": y + h}

    def process(self, cx, cy, size=26):
        self.out.append(f'<rect x="{cx - size / 2}" y="{cy - size / 2}" width="{size}" height="{size}" fill="#222"/>')
        return {"cx": cx, "cy": cy, "x": cx - size / 2, "r": cx + size / 2, "y": cy - size / 2, "b": cy + size / 2}

    def ubiquitous(self, cx, cy, w=150, h=34):
        self.out.append(f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="17" '
                        f'fill="#c8c8c8" stroke="#555" stroke-width="1.4"/>')
        return {"cx": cx, "cy": cy, "x": cx - w / 2, "r": cx + w / 2, "y": cy - h / 2, "b": cy + h / 2}

    def opening(self, cx, cy, r=13):
        self.out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#222"/>')
        return {"cx": cx, "cy": cy, "y": cy - r, "b": cy + r, "x": cx - r, "r": cx + r}

    def closing(self, cx, cy, r=13):
        self.out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="#222" stroke-width="2"/>')
        self.out.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 6}" fill="#222"/>')
        return {"cx": cx, "cy": cy, "y": cy - r, "b": cy + r, "x": cx - r, "r": cx + r}

    def closing_temp(self, cx, cy, r=13):
        """Encerramento temporário: a pessoa sai, mas a atividade do sistema continua (contorno tracejado)."""
        self.out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="#222" stroke-width="2" '
                        f'stroke-dasharray="4 3"/>')
        self.out.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 6}" fill="#222"/>')
        return {"cx": cx, "cy": cy, "y": cy - r, "b": cy + r, "x": cx - r, "r": cx + r}

    # ------------------------------------------------------------ falas
    def arrow(self, points, label=None, at=None, anchor="start", dashed=False, size=13):
        """Fala de transição: points = [(x, y), ...]; label = linhas; at = (x, y) da primeira linha."""
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in points)
        dash = ' stroke-dasharray="7 5"' if dashed else ""
        self.out.append(f'<path d="{d}" fill="none" stroke="#333" stroke-width="1.5"{dash} '
                        f'marker-end="url(#arrow)"/>')
        if label:
            x, y = at
            for i, line in enumerate(label):
                self.s.text(x, y + 17 * i, line, size=size, anchor=anchor)

    # ------------------------------------------------------------ legenda
    def legend(self, y):
        y = self.s.section(y, "Legenda (Barbosa e Silva, 2010; aulas de MoLIC)") + 4
        self.scene(130, y, 170, ["Tópico"], ["d+u: diálogos"])
        self.s.text(130, y + 96, "cena", size=13)
        self.scene(330, y, 170, ["Tópico"], ["d: alerta"], dashed=True)
        self.s.text(330, y + 96, "cena de alerta", size=13)
        self.process(480, y + 32)
        self.s.text(480, y + 72, "processo", size=13)
        self.s.text(480, y + 89, "do sistema", size=13)
        self.ubiquitous(620, y + 32, w=110)
        self.s.text(620, y + 72, "acesso ubíquo", size=13)
        self.opening(740, y + 32)
        self.s.text(740, y + 72, "abertura", size=13)
        self.closing(840, y + 32)
        self.s.text(840, y + 72, "encerramento", size=13)
        self.closing_temp(1020, y + 32)
        self.s.text(1020, y + 72, "encerramento temporário", size=13)
        self.s.text(1020, y + 89, "(a atividade continua)", size=13)
        notes = ["Seta contínua: fala de transição (u: usuário; d: preposto do designer).",
                 "Seta tracejada: fala de recuperação de ruptura.",
                 "gco / gcc: abertura / fechamento de cada conversa sobre um objetivo do usuário (um par por conversa).",
                 "[PP] prevenção passiva · [PA] prevenção ativa · [AL] prevenção apoiada (alerta)",
                 "[RA] recuperação apoiada · [CE] captura de erro (Entrega 9, seção 4)."]
        for i, n in enumerate(notes):
            self.s.text(40, y + 130 + 20 * i, n, size=13, anchor="start")
        return y + 130 + 20 * len(notes) + 10
