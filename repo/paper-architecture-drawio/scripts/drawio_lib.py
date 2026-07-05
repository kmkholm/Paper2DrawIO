"""
drawio_lib.py — helper library for generating professional draw.io (mxGraph) XML
architecture figures programmatically. Import from a short composition script;
never hand-write raw mxCell elements.

Typical usage:
    from drawio_lib import Diagram
    d = Diagram(page_w=1100, page_h=1600)
    c = d.container(30, 105, 470, 740, "Deep Path", "#1c56b8")
    b1 = d.block(42, 155, 446, 130, "A1", "SincConv-1D + abs()",
                 sub="64 filters, kernel 251, stride 8",
                 color="#1c56b8", badge_color="#123f8f")
    d.dim_pill(242, 253, "(B, 64, 4000)")
    d.arrow(b1, b2)
    d.save("/mnt/user-data/outputs/figure.drawio", name="Architecture")
"""
from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET

FONT = "fontFamily=Helvetica;"

ARROW = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;"
         "strokeWidth=2;endArrow=block;endFill=1;" + FONT)
ARROW_STRAIGHT = ("edgeStyle=none;rounded=0;html=1;strokeColor=#000000;"
                  "strokeWidth=2;endArrow=block;endFill=1;" + FONT)
ARROW_DASHED = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;"
                "strokeWidth=1.5;dashed=1;endArrow=block;endFill=1;" + FONT)


class Diagram:
    def __init__(self, page_w=1100, page_h=1600, name="Architecture"):
        self.cells = []
        self._id = 1
        self.page_w, self.page_h = page_w, page_h
        self.name = name

    # ---------------- core primitives ----------------
    def _nid(self):
        self._id += 1
        return f"n{self._id}"

    def vertex(self, value, style, x, y, w, h):
        i = self._nid()
        v = escape(value, {'"': "&quot;"})
        self.cells.append(
            f'<mxCell id="{i}" value="{v}" style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
        return i

    def edge(self, src, dst, style=ARROW, points=None, exit_xy=None, entry_xy=None):
        s = style
        if exit_xy:
            s += f"exitX={exit_xy[0]};exitY={exit_xy[1]};"
        if entry_xy:
            s += f"entryX={entry_xy[0]};entryY={entry_xy[1]};"
        i = self._nid()
        pts = ""
        if points:
            arr = "".join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in points)
            pts = f'<Array as="points">{arr}</Array>'
        self.cells.append(
            f'<mxCell id="{i}" style="{s}" edge="1" parent="1" source="{src}" target="{dst}">'
            f'<mxGeometry relative="1" as="geometry">{pts}</mxGeometry></mxCell>')
        return i

    def free_edge(self, points, style=ARROW_STRAIGHT):
        """Edge defined purely by coordinates (first=source, last=target)."""
        i = self._nid()
        (x1, y1), (x2, y2) = points[0], points[-1]
        mid = ""
        if len(points) > 2:
            arr = "".join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in points[1:-1])
            mid = f'<Array as="points">{arr}</Array>'
        self.cells.append(
            f'<mxCell id="{i}" style="{style}" edge="1" parent="1">'
            f'<mxGeometry relative="1" as="geometry">'
            f'<mxPoint x="{x1}" y="{y1}" as="sourcePoint"/>'
            f'<mxPoint x="{x2}" y="{y2}" as="targetPoint"/>{mid}</mxGeometry></mxCell>')
        return i

    def text(self, value, x, y, w, h, size=13, bold=False, align="center",
             color=None, extra=""):
        s = f"text;html=1;align={align};verticalAlign=middle;fontSize={size};" + FONT + extra
        if bold:
            s += "fontStyle=1;"
        if color:
            s += f"fontColor={color};"
        return self.vertex(value, s, x, y, w, h)

    # ---------------- design-system components ----------------
    def container(self, x, y, w, h, title, color, banner_h=40, title_size=19):
        c = self.vertex("", f"rounded=1;arcSize=6;whiteSpace=wrap;html=1;"
                            f"fillColor=#ffffff;strokeColor={color};strokeWidth=2;" + FONT,
                        x, y, w, h)
        self.vertex(title, f"rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor={color};"
                           f"strokeColor=none;fontColor=#ffffff;fontStyle=1;fontSize={title_size};" + FONT,
                    x, y, w, banner_h)
        return c

    def ribbon(self, cx, y, title, color, w=170, h=26):
        """Small centered banner overlapping a container's top border."""
        return self.vertex(title, f"rounded=1;arcSize=30;whiteSpace=wrap;html=1;fillColor={color};"
                                  f"strokeColor=none;fontColor=#ffffff;fontStyle=1;fontSize=15;" + FONT,
                           cx - w / 2, y - h / 2, w, h)

    def block(self, x, y, w, h, bid, title, sub=None, color="#1c56b8",
              badge_color=None, fill="#ffffff", title_size=15, sub_size=12):
        b = self.vertex("", f"rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor={fill};"
                            f"strokeColor={color};strokeWidth=1.5;" + FONT, x, y, w, h)
        if bid:
            self.vertex(bid, f"rounded=1;arcSize=25;whiteSpace=wrap;html=1;"
                             f"fillColor={badge_color or color};strokeColor=none;fontColor=#ffffff;"
                             f"fontStyle=1;fontSize=15;" + FONT, x + 8, y + 8, 44, 30)
        tx = x + (62 if bid else 12)
        self.text(title, tx, y + 10, w - (70 if bid else 24), 22,
                  size=title_size, bold=True, align="left")
        if sub:
            self.text(sub, tx, y + 32, w - (70 if bid else 24), 36,
                      size=sub_size, align="left")
        return b

    def dim_pill(self, cx, y, label, w=120, h=22):
        return self.vertex(label, "rounded=1;arcSize=50;whiteSpace=wrap;html=1;"
                                  "fillColor=#f5f5f5;strokeColor=#666666;fontSize=11;fontStyle=1;" + FONT,
                           cx - w / 2, y, w, h)

    def note(self, x, y, w, h, label, color="#d81b60", fill="#fff0f5"):
        """Dashed side note (parameter counts, complexity, loss)."""
        return self.vertex(label, f"rounded=1;arcSize=15;whiteSpace=wrap;html=1;fillColor={fill};"
                                  f"strokeColor={color};dashed=1;fontColor={color};"
                                  f"fontStyle=1;fontSize=12;" + FONT, x, y, w, h)

    # ---------------- decorative glyphs ----------------
    def strip(self, x, y, n, fill, stroke, cw=17, ch=15, gap=0):
        for k in range(n):
            self.vertex("", f"rounded=0;whiteSpace=wrap;html=1;fillColor={fill};"
                            f"strokeColor={stroke};" + FONT, x + k * (cw + gap), y, cw, ch)
        return x + n * (cw + gap)

    def strip_dots(self, x, y, n1, n2, fill, stroke, cw=17, ch=15):
        """n1 cells, '...', n2 cells. Returns end x."""
        dx = self.strip(x, y, n1, fill, stroke, cw, ch)
        self.text("...", dx + 4, y - 2, 30, ch + 4, size=15, bold=True)
        return self.strip(dx + 38, y, n2, fill, stroke, cw, ch)

    def stacked_maps(self, x, y, n, w, h, fill_from, fill_to, stroke, off=10):
        for k in range(n):
            self.vertex("", f"rounded=0;whiteSpace=wrap;html=1;fillColor={fill_from};"
                            f"gradientColor={fill_to};gradientDirection=south;"
                            f"strokeColor={stroke};" + FONT,
                        x + k * off, y - k * off * 0.55, w, h)

    def neuron_col(self, x, y, n, fill, stroke, r=11, gap=4, dots=False):
        for k in range(n):
            self.vertex("", f"ellipse;whiteSpace=wrap;html=1;fillColor={fill};"
                            f"strokeColor={stroke};" + FONT, x, y + k * (r + gap), r, r)
        if dots:
            self.text("&#8942;", x - 4, y + n * (r + gap), r + 8, 16, size=14, bold=True)

    def plus_circle(self, cx, cy, r=13):
        return self.vertex("+", "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;"
                                "strokeColor=#000000;fontSize=15;fontStyle=1;" + FONT,
                           cx - r, cy - r, 2 * r, 2 * r)

    def sigma_circle(self, cx, cy, label="&#931;", r=16, color="#123f8f"):
        return self.vertex(label, f"ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;"
                                  f"strokeColor={color};fontColor={color};fontSize=15;fontStyle=1;" + FONT,
                           cx - r, cy - r, 2 * r, 2 * r)

    def cylinder(self, x, y, w, h, label, color="#555555", fill="#f5f5f5"):
        return self.vertex(label, f"shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;"
                                  f"backgroundOutline=1;size=8;fillColor={fill};"
                                  f"strokeColor={color};fontSize=11;" + FONT, x, y, w, h)

    def cloud(self, x, y, w, h, label, color="#1c56b8", fill="#e3f2fd"):
        return self.vertex(label, f"shape=cloud;whiteSpace=wrap;html=1;fillColor={fill};"
                                  f"strokeColor={color};fontSize=12;fontStyle=1;" + FONT, x, y, w, h)

    def curve_panel(self, x, y, w, h, curve_color="#c2185b", dot_color="#d81b60",
                    label=None):
        """Mini activation/spline plot: box + curved polyline + knot dots."""
        self.vertex("", "rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#ffffff;"
                        "strokeColor=#888888;" + FONT, x, y, w, h)
        self.free_edge([(x + 6, y + h - 12), (x + w * .25, y + 8), (x + w * .5, y + h - 14),
                        (x + w * .75, y + 10), (x + w - 6, y + h - 16)],
                       style=f"html=1;strokeColor={curve_color};strokeWidth=2;endArrow=none;curved=1;" + FONT)
        for fx in (0.12, 0.32, 0.52, 0.72, 0.9):
            self.vertex("", f"ellipse;whiteSpace=wrap;html=1;fillColor={dot_color};"
                            f"strokeColor=#8e0e3d;" + FONT, x + w * fx - 3, y + h * .45 - 3, 7, 7)
        if label:
            self.text(label, x - 10, y + h + 2, w + 20, 14, size=10)

    def waveform(self, x, y, w, h, color="#000000", n=10):
        import math
        pts = [(x, y + h / 2)]
        for k in range(1, n):
            pts.append((x + w * k / n, y + (h * 0.1 if k % 2 else h * 0.9)))
        pts.append((x + w, y + h / 2))
        self.free_edge(pts, style=f"html=1;strokeColor={color};strokeWidth=2;endArrow=none;" + FONT)
        self.free_edge([(x - 8, y + h / 2), (x + w + 8, y + h / 2)],
                       style="html=1;strokeColor=#000000;strokeWidth=1;endArrow=block;endFill=1;"
                             "startArrow=block;startFill=1;" + FONT)

    def repeat_bracket(self, x, y1, y2, label="&#215; N"):
        self.free_edge([(x, y1), (x + 10, y1), (x + 10, y2), (x, y2)],
                       style="html=1;strokeColor=#555555;strokeWidth=1.5;endArrow=none;rounded=1;" + FONT)
        self.text(label, x + 14, (y1 + y2) / 2 - 10, 46, 20, size=16, bold=True)

    def class_dots(self, x, y, n, fill="#66bb6a", stroke="#2e7d32", r=16, gap=12):
        for k in range(n):
            self.vertex("", f"ellipse;whiteSpace=wrap;html=1;fillColor={fill};"
                            f"strokeColor={stroke};" + FONT, x + k * (r + gap), y, r, r)

    def bar_chart(self, x, y, labels_values, bar_fill="#8e24aa", bar_grad="#d81b60",
                  label_w=70, max_w=90, row_h=18):
        vmax = max(v for _, v in labels_values) or 1
        for i, (lab, v) in enumerate(labels_values):
            yy = y + i * row_h
            self.text(lab, x, yy, label_w, 14, size=9, align="right")
            self.vertex("", f"rounded=0;whiteSpace=wrap;html=1;fillColor={bar_fill};"
                            f"gradientColor={bar_grad};strokeColor=none;" + FONT,
                        x + label_w + 4, yy + 2, max_w * v / vmax, 11)

    # ---------------- output ----------------
    def to_xml(self):
        inner = "\n        ".join(self.cells)
        return f'''<mxfile host="app.diagrams.net" agent="Claude" version="24.0.0" type="device">
  <diagram id="arch" name="{escape(self.name)}">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{self.page_w}" pageHeight="{self.page_h}" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        {inner}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

    def save(self, path, name=None):
        if name:
            self.name = name
        xml = self.to_xml()
        ET.fromstring(xml)  # validate — raises on malformed XML
        with open(path, "w", encoding="utf-8") as f:
            f.write(xml)
        print(f"saved {path}: {len(self.cells)} cells, {len(xml)} bytes, XML valid")
        return path
