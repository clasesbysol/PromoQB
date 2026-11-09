# Se ejecuta dentro de mols.py (usa MOL, PYR, svgwrap). Unidades repetitivas en Haworth y esquemas de cadenas.

def hr(out, subs, dx, dy, skip=()):
    """Anillo de piranosa en (dx, dy) con sustituyentes {C: (arriba, abajo)}."""
    P = {k: (x + dx, y + dy) for k, (x, y) in PYR.items()}
    order = ['O', 1, 2, 3, 4, 5]
    out.append("<polygon points='" + " ".join(f"{P[k][0]},{P[k][1]}" for k in order) + "' class='ring'/>")
    out.append(f"<line x1='{P[2][0]}' y1='{P[2][1]}' x2='{P[3][0]}' y2='{P[3][1]}' class='front'/>")
    ox, oy = P['O']
    out.append(f"<rect x='{ox-9}' y='{oy-10}' width='18' height='18' class='bgfill'/><text x='{ox}' y='{oy+5}' text-anchor='middle' class='o'>O</text>")
    for c in (1, 2, 3, 4, 5):
        up, dn = subs.get(c, (None, None))
        if c == 4 and subs.get(5, (None, None))[1]:
            up = None
        x, y = P[c]
        for lab, d in ((up, -1), (dn, 1)):
            if not lab or (c, d) in skip:
                continue
            L = 26
            y2 = y + d * L
            cls = 'h' if lab == 'H' else ('s' if 'SO' in lab else 'o')
            if c == 5 and d == 1:
                out.append(f"<line x1='{x}' y1='{y}' x2='{x-22}' y2='{y+16}' class='b'/>")
                out.append(f"<text x='{x-24}' y='{y+22}' text-anchor='end' class='{cls}'>{lab}</text>")
                continue
            out.append(f"<line x1='{x}' y1='{y}' x2='{x}' y2='{y2}' class='b'/>")
            ty = y2 - 4 if d < 0 else y2 + 14
            out.append(f"<text x='{x}' y='{ty}' text-anchor='middle' class='{cls}'>{lab}</text>")
    return P

def bond(out, pts, olab=None):
    out.append("<polyline points='" + " ".join(f"{x},{y}" for x, y in pts) + "' class='link'/>")
    if olab:
        x, y = olab
        out.append(f"<rect x='{x-9}' y='{y-11}' width='18' height='18' class='bgfill'/><text x='{x}' y='{y+5}' text-anchor='middle' class='o'>O</text>")

def tag(out, x, y, t):
    out.append(f"<text x='{x}' y='{y}' text-anchor='middle' class='lab'>{t}</text>")

OHs = {2: ('H', 'OH'), 3: ('OH', 'H'), 4: ('H', 'OH')}

def unit14(id_, name, s1, s2, beta1, beta2=None, n=True, lab=None):
    """Residuo1 (1→4) Residuo2. beta1: enlace entre ellos. Extremos abiertos para indicar polímero."""
    out = []
    dy = 30
    s1 = dict(s1); s2 = dict(s2)
    s1[1] = ((None, 'H') if beta1 else ('H', None))
    s1[4] = ('H', 'O…') if n else s1.get(4)
    s2[4] = ('H', None)
    if beta2 is not None:
        s2[1] = ('O…', 'H') if beta2 else ('H', 'O…')
    P1 = hr(out, s1, 30, dy)
    P2 = hr(out, s2, 265, dy)
    x1, y1 = P1[1]; x4, y4 = P2[4]
    if beta1:
        bond(out, [(x1, y1), (x1 + 25, y1 - 30), (x4 - 25, y1 - 30), (x4, y4)], ((x1 + x4) / 2, y1 - 30))
    else:
        bond(out, [(x1, y1), (x1 + 20, y1 + 32), (x4 - 20, y4 + 32), (x4, y4)], ((x1 + x4) / 2, y1 + 32))
    tag(out, (x1 + x4) / 2, (y1 - 42) if beta1 else (y1 + 58), lab or ("β(1→4)" if beta1 else "α(1→4)"))
    MOL[id_] = {"name": name, "svg": svgwrap(520, 200, out)}

def unit13(id_, name, s1, s2, beta1, nxt, lab=None):
    """Residuo1 (1→3) Residuo2 (1→4)… ; el residuo 2 queda más arriba para acercar su C3."""
    out = []
    s1 = dict(s1); s2 = dict(s2)
    s1[1] = ((None, 'H') if beta1 else (None, 'H'))
    s1[4] = ('H', 'O…')
    s2[3] = (None, 'H')
    s2[1] = nxt
    P1 = hr(out, s1, 30, 70)
    P2 = hr(out, s2, 255, 20)
    x1, y1 = P1[1]; x3, y3 = P2[3]
    oy = min(y1, y3) - 34
    bond(out, [(x1, y1), (x1 + 18, oy), (x3 - 18, oy), (x3, y3)], ((x1 + x3) / 2, oy))
    tag(out, (x1 + x3) / 2 - 2, oy - 14, lab or (("β" if beta1 else "α") + "(1→3)"))
    MOL[id_] = {"name": name, "svg": svgwrap(500, 230, out)}

GLCs = {**OHs, 5: ('CH₂OH', None)}
GLCNAC = {**GLCs, 2: ('H', 'NHAc')}
GALNAC4S = {**GLCs, 2: ('H', 'NHAc'), 4: ('⁻O₃SO', 'H')}
GLCA = {**OHs, 5: ('COO⁻', None)}
IDOA = {**OHs, 5: ('H', 'COO⁻')}
GAL = {**GLCs, 4: ('OH', 'H')}

unit14("p_amilosa", "Amilosa / almidón: Glcα(1→4)Glc repetido", GLCs, GLCs, False, False)
unit14("p_celulosa", "Celulosa: Glcβ(1→4)Glc repetido", GLCs, GLCs, True, True)
unit14("p_quitina", "Quitina: GlcNAcβ(1→4)GlcNAc repetido", GLCNAC, GLCNAC, True, True)
unit14("p_peptidoglicano", "Peptidoglicano: GlcNAcβ(1→4)MurNAc (+ péptido en el lactilo)",
       GLCNAC, {**GLCNAC, 3: ('O-lactil–péptido', 'H')}, True, True)
unit14("g_queratan", "Queratán sulfato: Galβ(1→4)GlcNAc-6-sulfato (sin ácido urónico)",
       GAL, {**GLCNAC, 5: ('CH₂OSO₃⁻', None)}, True, None)
unit14("g_heparina", "Heparina: IdoA-2-sulfato α(1→4) GlcNS-6-sulfato",
       {**IDOA, 2: ('H', 'OSO₃⁻')}, {**GLCs, 2: ('H', 'NHSO₃⁻'), 5: ('CH₂OSO₃⁻', None)}, True, False, lab="α-L(1→4)")
def mono(id_, name, subs):
    out = []
    hr(out, subs, 20, 30)
    MOL[id_] = {"name": name, "svg": svgwrap(250, 190, out)}
mono("m_glca", "β-D-glucuronato (GlcA)", {**GLCA, 1: ('OH', 'H')})
mono("m_idoa", "α-L-iduronato (IdoA): epímero en C5 del GlcA", {**IDOA, 1: ('OH', 'H')})
mono("m_glcnac", "β-N-acetilglucosamina (GlcNAc)", {**GLCNAC, 1: ('OH', 'H')})
mono("m_galnac4s", "N-acetilgalactosamina-4-sulfato (GalNAc4S)", {**GALNAC4S, 1: ('OH', 'H')})
mono("m_glcns6s", "Glucosamina N-sulfato 6-sulfato (GlcNS6S)", {**GLCs, 2: ('H', 'NHSO₃⁻'), 5: ('CH₂OSO₃⁻', None), 1: ('OH', 'H')})

def gagchain(id_, name, units, note):
    """units: [(forma, color, sulfato), 'enlace', (forma,...), 'enlace']; se repite 3 veces."""
    shapes, lines = [], []
    y = 50; x = 34; step = 70
    seq = units * 3
    k = 0
    for u in seq:
        if isinstance(u, str):
            lines.append(f"<line x1='{x}' y1='{y}' x2='{x+step}' y2='{y}' class='bnd'/><text x='{x+step/2}' y='{y-14}' text-anchor='middle' class='lk'>{u}</text>")
            x += step
            continue
        shape, col, lab = u
        if shape == 'sq':
            shapes.append(f"<rect x='{x-12}' y='{y-12}' width='24' height='24' class='sym {col}'/>")
        elif shape == 'ci':
            shapes.append(f"<circle cx='{x}' cy='{y}' r='12' class='sym {col}'/>")
        else:
            shapes.append(f"<polygon points='{x},{y-14} {x+14},{y} {x},{y+14} {x-14},{y}' class='sym {col}'/>")
        if lab:
            shapes.append(f"<text x='{x}' y='{y+32}' text-anchor='middle' class='s'>{lab}</text>")
    W = x + 20
    out = [f"<line x1='6' y1='{y}' x2='34' y2='{y}' class='bnd'/>"] + lines + shapes
    out.append(f"<text x='{W/2}' y='{y+60}' text-anchor='middle' class='lab'>{note}</text>")
    MOL[id_] = {"name": name, "svg": svgwrap(W, 120, out)}

gagchain("c_hialuronano", "Hialuronano: [GlcA β1→3 GlcNAc β1→4]ₙ", [('di', 'glca', ''), 'β1→3', ('sq', 'glcnac', ''), 'β1→4'], "sin sulfato · enorme")
gagchain("c_condroitin", "Condroitín sulfato: [GlcA β1→3 GalNAc β1→4]ₙ", [('di', 'glca', ''), 'β1→3', ('sq', 'galnac', '4S o 6S'), 'β1→4'], "GalNAc sulfatada en 4 o 6")
gagchain("c_dermatan", "Dermatán sulfato: [IdoA α1→3 GalNAc β1→4]ₙ", [('di', 'idoa', ''), 'α1→3', ('sq', 'galnac', '4S'), 'β1→4'], "como condroitín, pero con IdoA")
gagchain("c_queratan", "Queratán sulfato: [Gal β1→4 GlcNAc β1→3]ₙ", [('ci', 'gal', ''), 'β1→4', ('sq', 'glcnac', '6S'), 'β1→3'], "Gal en lugar de ácido urónico")
gagchain("c_heparina", "Heparina / heparán sulfato: [IdoA(2S) α1→4 GlcNS(6S) α1→4]ₙ", [('di', 'idoa', '2S'), 'α1→4', ('sq', 'glcns', 'NS, 6S'), 'α1→4'], "la más sulfatada (heparán: menos)")


# ---- rama α(1→6) ----
out = []
s_top = {**GLCs, 1: (None, 'H'), 4: ('H', 'O…')}
s_bot = {**GLCs, 5: ('CH₂', None), 1: ('H', 'O…'), 4: ('H', 'O…')}
P1 = hr(out, s_top, 10, 30)
P2 = hr(out, s_bot, 200, 175)
x1, y1 = P1[1]
cx, cy = P2[5][0], P2[5][1] - 26 - 18
bond(out, [(x1, y1), (x1, y1 + 34), (cx - 22, cy)], (x1 + 6, y1 + 40))
tag(out, x1 + 95, y1 + 40, "α(1→6)")
tag(out, 100, 220, "rama")
tag(out, 300, 345, "cadena principal α(1→4)")
MOL["p_rama16"] = {"name": "Punto de ramificación α(1→6) (amilopectina y glucógeno)", "svg": svgwrap(440, 355, out)}

# ---- esquemas de cadenas (símbolos) ----
def sym(out, x, y, kind):
    if kind == 'glc':
        out.append(f"<circle cx='{x}' cy='{y}' r='9' class='glc'/>")
    elif kind == 'glcnac':
        out.append(f"<rect x='{x-9}' y='{y-9}' width='18' height='18' class='glc'/>")

def chain_svg(id_, name, segs, W, H, extra=""):
    out = []
    for (x1, y1, x2, y2, cls) in segs.get('lines', []):
        out.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' class='{cls}'/>")
    for (x, y, k) in segs['nodes']:
        sym(out, x, y, k)
    out.append(extra)
    MOL[id_] = {"name": name, "svg": svgwrap(W, H, out)}

def linear(y, n, x0=20, dx=26, k='glc', wave=0):
    nodes, lines = [], []
    pts = [(x0 + i * dx, y + (wave * (1 if i % 2 else -1) if wave else 0)) for i in range(n)]
    for i in range(n - 1):
        lines.append((pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], 'bnd'))
    nodes = [(x, yy, k) for x, yy in pts]
    return nodes, lines

n, l = linear(60, 16, wave=8)
chain_svg("s_amilosa", "Amilosa: cadena lineal α(1→4) que se enrolla en hélice", {'nodes': n, 'lines': l}, 440, 110,
          "<text x='220' y='100' text-anchor='middle' class='lab'>lineal · hélice · el yodo entra en la hélice (azul)</text>")

def branched(id_, name, every, depth_rows, W, H, note):
    nodes, lines = [], []
    def grow(x, y, length, level):
        prev = None
        for i in range(length):
            px, py = x + i * 22, y
            nodes.append((px, py, 'glc'))
            if prev: lines.append((prev[0], prev[1], px, py, 'bnd'))
            prev = (px, py)
            if level < depth_rows and i > 0 and i % every == 0 and px + 22 * 4 < W:
                ny = y + 30
                lines.append((px, py, px + 11, ny, 'bnd16'))
                grow(px + 11, ny, max(4, length - i - 2), level + 1)
    grow(20, 24, int((W - 40) / 22), 0)
    extra = f"<text x='{W/2}' y='{H-6}' text-anchor='middle' class='lab'>{note}</text>"
    chain_svg(id_, name, {'nodes': nodes, 'lines': lines}, W, H, extra)

branched("s_amilopectina", "Amilopectina: ramas α(1→6) espaciadas (cada 24–30)", 8, 2, 460, 130, "ramas cada 24–30 residuos (esquema)")
branched("s_glucogeno", "Glucógeno: ramas α(1→6) muy frecuentes (cada 8–12)", 3, 4, 460, 190, "ramas cada 8–12 · muchos extremos no reductores")

nodes, lines, extra = [], [], ""
for r in range(3):
    nn, ll = linear(28 + r * 32, 16, k='glc')
    nodes += nn; lines += ll
for r in range(2):
    for i in range(0, 16, 2):
        x = 20 + i * 26
        lines.append((x, 28 + r * 32 + 9, x, 28 + (r + 1) * 32 - 9, 'hb'))
chain_svg("s_celulosa", "Celulosa: cadenas rectas paralelas unidas por puentes de H (fibras)", {'nodes': nodes, 'lines': lines}, 440, 130,
          "<text x='220' y='124' text-anchor='middle' class='lab'>lineal β(1→4) · puentes de H entre cadenas (punteado)</text>")
nodes, lines = [], []
for r in range(2):
    nn, ll = linear(28 + r * 32, 16, k='glcnac')
    nodes += nn; lines += ll
for i in range(0, 16, 2):
    lines.append((20 + i * 26, 37, 20 + i * 26, 51, 'hb'))
chain_svg("s_quitina", "Quitina: cadenas de GlcNAc β(1→4) (como la celulosa con NHAc en C2)", {'nodes': nodes, 'lines': lines}, 440, 100,
          "<text x='220' y='94' text-anchor='middle' class='lab'>■ = GlcNAc · ● = glucosa</text>")
