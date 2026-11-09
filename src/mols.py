"""Genera mols.js: un diccionario MOL{id: {svg, name}} con estructuras en SVG que usan currentColor."""
import json, re
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

rdDepictor.SetPreferCoordGen(True)
MOL = {}

def rd(id_, name, smi, w=300, h=220):
    m = Chem.MolFromSmiles(smi)
    assert m is not None, id_
    rdDepictor.Compute2DCoords(m)
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    o = d.drawOptions()
    o.clearBackground = False
    o.bondLineWidth = 2
    o.minFontSize = 14
    o.maxFontSize = 18
    o.padding = 0.08
    o.updateAtomPalette({6: (0, 0, 0), 1: (0, 0, 0), 7: (0.25, 0.48, 0.95), 8: (0.92, 0.27, 0.32),
                         15: (0.93, 0.55, 0.1), 16: (0.85, 0.66, 0.1), 9: (0.15, 0.7, 0.45)})
    d.DrawMolecule(m)
    d.FinishDrawing()
    s = d.GetDrawingText()
    s = re.sub(r"<\?xml[^>]*\?>\s*", "", s)
    s = re.sub(r"<!-- .*? -->\s*", "", s, flags=re.S)
    s = s.replace("#000000", "currentColor")
    s = re.sub(r"<rect[^>]*style='opacity:1.0;fill:#FFFFFF[^>]*>\s*</rect>", "", s)
    s = re.sub(r" width='\d+px' height='\d+px'", "", s)
    s = s.replace("xmlns:rdkit='http://www.rdkit.org/xml' xmlns:xlink='http://www.w3.org/1999/xlink' ", "")
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"(\d+\.\d)\d+", r"\1", s)
    MOL[id_] = {"name": name, "svg": s}

# ---------- Fischer ----------
def fischer(id_, name, rows):
    """rows: ('c', texto central) o ('x', izquierda, derecha)."""
    W, top, step = 170, 26, 40
    H = top + step * (len(rows) - 1) + 26
    out = [f"<svg viewBox='0 0 {W} {H}' xmlns='http://www.w3.org/2000/svg' class='fz'>"]
    cx = W / 2
    ys = [top + i * step for i in range(len(rows))]
    for i in range(len(rows) - 1):
        y1 = ys[i] + (9 if rows[i][0] == 'c' else 0)
        y2 = ys[i + 1] - (11 if rows[i + 1][0] == 'c' else 0)
        out.append(f"<line x1='{cx}' y1='{y1}' x2='{cx}' y2='{y2}' class='b'/>")
    for r, y in zip(rows, ys):
        if r[0] == 'c':
            out.append(f"<text x='{cx}' y='{y+5}' text-anchor='middle' class='t'>{r[1]}</text>")
        else:
            l, rr = r[1], r[2]
            out.append(f"<line x1='{cx-34}' y1='{y}' x2='{cx+34}' y2='{y}' class='b'/>")
            out.append(f"<text x='{cx-38}' y='{y+5}' text-anchor='end' class='{ 'o' if 'O' in l or 'N' in l else 'h'}'>{l}</text>")
            out.append(f"<text x='{cx+38}' y='{y+5}' text-anchor='start' class='{ 'o' if 'O' in rr or 'N' in rr else 'h'}'>{rr}</text>")
    out.append("</svg>")
    MOL[id_] = {"name": name, "svg": "".join(out)}

R, L = ('x', 'H', 'OH'), ('x', 'HO', 'H')
fischer("f_dgliceraldehido", "D-gliceraldehído", [('c', 'CHO'), R, ('c', 'CH₂OH')])
fischer("f_lgliceraldehido", "L-gliceraldehído", [('c', 'CHO'), L, ('c', 'CH₂OH')])
fischer("f_dihidroxiacetona", "Dihidroxiacetona", [('c', 'CH₂OH'), ('c', 'C=O'), ('c', 'CH₂OH')])
fischer("f_dglucosa", "D-glucosa", [('c', 'CHO'), R, L, R, R, ('c', 'CH₂OH')])
fischer("f_lglucosa", "L-glucosa", [('c', 'CHO'), L, R, L, L, ('c', 'CH₂OH')])
fischer("f_dmanosa", "D-manosa", [('c', 'CHO'), L, L, R, R, ('c', 'CH₂OH')])
fischer("f_dgalactosa", "D-galactosa", [('c', 'CHO'), R, L, L, R, ('c', 'CH₂OH')])
fischer("f_dfructosa", "D-fructosa", [('c', 'CH₂OH'), ('c', 'C=O'), L, R, R, ('c', 'CH₂OH')])
fischer("f_dribosa", "D-ribosa", [('c', 'CHO'), R, R, R, ('c', 'CH₂OH')])
fischer("f_glucitol", "D-glucitol (sorbitol)", [('c', 'CH₂OH'), R, L, R, R, ('c', 'CH₂OH')])
fischer("f_gluconico", "Ácido D-glucónico", [('c', 'COOH'), R, L, R, R, ('c', 'CH₂OH')])
fischer("f_glucuronico", "Ácido D-glucurónico", [('c', 'CHO'), R, L, R, R, ('c', 'COOH')])
fischer("f_glucarico", "Ácido D-glucárico", [('c', 'COOH'), R, L, R, R, ('c', 'COOH')])

# ---------- Haworth ----------
PYR = {'O': (150, 40), 1: (195, 75), 2: (160, 112), 3: (90, 112), 4: (55, 75), 5: (90, 40)}
FUR = {'O': (122, 36), 1: (180, 74), 2: (152, 114), 3: (92, 114), 4: (64, 74)}

def sub(x, y, up, dn, out, L=30, side=0):
    for lab, dy in ((up, -1), (dn, 1)):
        if not lab:
            continue
        y2 = y + dy * L
        x2 = x + side
        out.append(f"<line x1='{x}' y1='{y}' x2='{x2}' y2='{y2}' class='b'/>")
        x = x2 if False else x
        cls = 'h' if lab == 'H' else 'o'
        ty = y2 - 4 if dy < 0 else y2 + 14
        anchor = 'middle'
        out.append(f"<text x='{x+side}' y='{ty}' text-anchor='{anchor}' class='{cls}'>{lab}</text>")

def ring(verts, order, dx=0, dy=0, out=None):
    pts = [verts[k] for k in order]
    p = " ".join(f"{x+dx},{y+dy}" for x, y in pts)
    out.append(f"<polygon points='{p}' class='ring'/>")
    # borde frontal grueso
    return pts

def haworth_pyr(subs, dx=0, out=None, skip=()):
    order = ['O', 1, 2, 3, 4, 5]
    ring(PYR, order, dx, 0, out)
    a, b = PYR[2], PYR[3]
    out.append(f"<line x1='{a[0]+dx}' y1='{a[1]}' x2='{b[0]+dx}' y2='{b[1]}' class='front'/>")
    ox, oy = PYR['O']
    out.append(f"<rect x='{ox+dx-9}' y='{oy-10}' width='18' height='18' class='bgfill'/><text x='{ox+dx}' y='{oy+5}' text-anchor='middle' class='o'>O</text>")
    for c in (1, 2, 3, 4, 5):
        if c in skip:
            continue
        up, dn = subs.get(c, (None, None))
        x, y = PYR[c]
        sub(x + dx, y, up, dn, out, L=(28 if c != 5 else 26))

def svgwrap(W, H, body):
    return f"<svg viewBox='0 0 {W} {H}' xmlns='http://www.w3.org/2000/svg' class='hw'>" + "".join(body) + "</svg>"

def pyranose(id_, name, subs):
    out = []
    haworth_pyr(subs, 0, out)
    MOL[id_] = {"name": name, "svg": svgwrap(250, 170, out)}

def furanose(id_, name, subs, labels=None):
    out = []
    ring(FUR, ['O', 1, 2, 3, 4], 0, 0, out)
    a, b = FUR[2], FUR[3]
    out.append(f"<line x1='{a[0]}' y1='{a[1]}' x2='{b[0]}' y2='{b[1]}' class='front'/>")
    ox, oy = FUR['O']
    out.append(f"<rect x='{ox-9}' y='{oy-10}' width='18' height='18' class='bgfill'/><text x='{ox}' y='{oy+5}' text-anchor='middle' class='o'>O</text>")
    for c in (1, 2, 3, 4):
        up, dn = subs.get(c, (None, None))
        x, y = FUR[c]
        sub(x, y, up, dn, out, side=(16 if c == 1 else (-12 if c == 4 else 0)))
    MOL[id_] = {"name": name, "svg": svgwrap(250, 170, out)}

GLC = {2: ('H', 'OH'), 3: ('OH', 'H'), 4: ('H', 'OH'), 5: ('CH₂OH', None)}
pyranose("h_aglc", "α-D-glucopiranosa", {**GLC, 1: ('H', 'OH')})
pyranose("h_bglc", "β-D-glucopiranosa", {**GLC, 1: ('OH', 'H')})
pyranose("h_bgal", "β-D-galactopiranosa", {**GLC, 1: ('OH', 'H'), 4: ('OH', 'H')})
pyranose("h_agal", "α-D-galactopiranosa", {**GLC, 1: ('H', 'OH'), 4: ('OH', 'H')})
pyranose("h_bman", "β-D-manopiranosa", {**GLC, 1: ('OH', 'H'), 2: ('OH', 'H')})
pyranose("h_bglcnac", "β-N-acetilglucosamina (GlcNAc)", {**GLC, 1: ('OH', 'H'), 2: ('H', 'NHAc')})
pyranose("h_bglca", "β-D-glucuronato", {**GLC, 1: ('OH', 'H'), 5: ('COO⁻', None)})
pyranose("h_g6p", "α-D-glucosa-6-fosfato", {**GLC, 1: ('H', 'OH'), 5: ('CH₂OPO₃²⁻', None)})
furanose("h_brib", "β-D-ribofuranosa (ARN)", {1: ('OH', 'H'), 2: ('H', 'OH'), 3: ('H', 'OH'), 4: ('HOCH₂', None)})
furanose("h_bdrib", "β-D-2-desoxirribofuranosa (ADN)", {1: ('OH', 'H'), 2: ('H', 'H'), 3: ('H', 'OH'), 4: ('HOCH₂', None)})
furanose("h_bfru", "β-D-fructofuranosa", {1: ('OH', 'CH₂OH'), 2: ('OH', 'H'), 3: ('H', 'OH'), 4: ('HOCH₂', None)})

def disac(id_, name, s1, s2, beta, note):
    out = []
    haworth_pyr(s1, 0, out, skip=(1,))
    haworth_pyr(s2, 235, out, skip=(4,))
    # sustituyente del C1 del primer residuo
    x1, y1 = PYR[1]
    x4, y4 = PYR[4][0] + 235, PYR[4][1]
    if beta:
        out.append(f"<line x1='{x1}' y1='{y1}' x2='{x1}' y2='{y1+28}' class='b'/><text x='{x1}' y='{y1+42}' text-anchor='middle' class='h'>H</text>")
        oy = 44
    else:
        out.append(f"<line x1='{x1}' y1='{y1}' x2='{x1}' y2='{y1-28}' class='b'/><text x='{x1}' y='{y1-32}' text-anchor='middle' class='h'>H</text>")
        oy = 108
    ox = (x1 + x4) / 2
    out.append(f"<polyline points='{x1},{y1} {ox-8},{oy} ' class='link'/><polyline points='{ox+8},{oy} {x4},{y4}' class='link'/>")
    out.append(f"<text x='{ox}' y='{oy+5}' text-anchor='middle' class='o'>O</text>")
    out.append(f"<line x1='{x4}' y1='{y4}' x2='{x4}' y2='{y4-28}' class='b'/><text x='{x4}' y='{y4-32}' text-anchor='middle' class='h'>H</text>")
    MOL[id_] = {"name": name, "svg": svgwrap(485, 172, out)}

RED = {**GLC, 1: ('OH', 'H')}
disac("d_maltosa", "Maltosa · Glcα(1→4)Glc", {**GLC}, RED, False, "α(1→4)")
disac("d_celobiosa", "Celobiosa · Glcβ(1→4)Glc", {**GLC}, RED, True, "β(1→4)")
disac("d_lactosa", "Lactosa · Galβ(1→4)Glc", {**GLC, 4: ('OH', 'H')}, RED, True, "β(1→4)")

# ---------- RDKit ----------
S = {
 "adenina": ("Adenina (purina)", "Nc1ncnc2[nH]cnc12"),
 "guanina": ("Guanina (purina)", "Nc1nc2[nH]cnc2c(=O)[nH]1"),
 "citosina": ("Citosina (pirimidina)", "Nc1cc[nH]c(=O)n1"),
 "timina": ("Timina (pirimidina)", "Cc1c[nH]c(=O)[nH]c1=O"),
 "uracilo": ("Uracilo (pirimidina)", "O=c1cc[nH]c(=O)[nH]1"),
 "purina": ("Purina", "c1ncc2[nH]cnc2n1"),
 "pirimidina": ("Pirimidina", "c1cncnc1"),
 "hipoxantina": ("Hipoxantina", "O=c1[nH]cnc2[nH]cnc12"),
 "xantina": ("Xantina", "O=c1[nH]c(=O)c2[nH]cnc2[nH]1"),
 "urico": ("Ácido úrico", "O=c1[nH]c(=O)c2[nH]c(=O)[nH]c2[nH]1"),
 "alopurinol": ("Alopurinol", "O=c1[nH]cnc2[nH]ncc12"),
 "cafeina": ("Cafeína (1,3,7-trimetilxantina)", "Cn1cnc2c1c(=O)n(C)c(=O)n2C"),
 "fu": ("5-fluorouracilo", "O=c1[nH]cc(F)c(=O)[nH]1"),
 "adenosina": ("Adenosina (nucleósido)", "Nc1ncnc2c1ncn2[C@@H]1O[C@H](CO)[C@@H](O)[C@H]1O"),
 "dadenosina": ("Desoxiadenosina (nucleósido)", "Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](CO)O1"),
 "amp": ("AMP (adenilato)", "Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)([O-])[O-])[C@@H](O)[C@H]1O"),
 "damp": ("dAMP (desoxiadenilato)", "Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](COP(=O)([O-])[O-])O1"),
 "atp": ("ATP (adenosín trifosfato)", "Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)([O-])OP(=O)([O-])OP(=O)([O-])[O-])[C@@H](O)[C@H]1O"),
 "camp": ("AMP cíclico (AMPc)", "Nc1ncnc2c1ncn2[C@@H]1O[C@@H]2COP(=O)([O-])O[C@H]2[C@H]1O"),
 "uridina": ("Uridina (nucleósido)", "O=c1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1"),
 "palmitico": ("Ácido palmítico 16:0", "CCCCCCCCCCCCCCCC(=O)O"),
 "estearico": ("Ácido esteárico 18:0", "CCCCCCCCCCCCCCCCCC(=O)O"),
 "oleico": ("Ácido oleico 18:1 cis-Δ9 (ω-9)", "CCCCCCCC/C=C\\CCCCCCCC(=O)O"),
 "elaidico": ("Ácido elaídico 18:1 trans-Δ9", "CCCCCCCC/C=C/CCCCCCCC(=O)O"),
 "linoleico": ("Ácido linoleico 18:2 Δ9,12 (ω-6)", "CCCCC/C=C\\C/C=C\\CCCCCCCC(=O)O"),
 "linolenico": ("Ácido α-linolénico 18:3 Δ9,12,15 (ω-3)", "CC/C=C\\C/C=C\\C/C=C\\CCCCCCCC(=O)O"),
 "araquidonico": ("Ácido araquidónico 20:4 (ω-6)", "CCCCC/C=C\\C/C=C\\C/C=C\\C/C=C\\CCCC(=O)O"),
 "glicerol": ("Glicerol", "OCC(O)CO"),
 "tag": ("Triacilglicérido (colas acortadas)", "CCCCCCCC(=O)OCC(OC(=O)CCCCCCC)COC(=O)CCCCCCC"),
 "pa": ("Ácido fosfatídico (colas acortadas)", "O=P([O-])([O-])OCC(COC(=O)CCCCCCC)OC(=O)CCCCCCC"),
 "pc": ("Fosfatidilcolina (colas acortadas)", "C[N+](C)(C)CCOP(=O)([O-])OCC(COC(=O)CCCCCCC)OC(=O)CCCCCCC"),
 "pe": ("Fosfatidiletanolamina (colas acortadas)", "[NH3+]CCOP(=O)([O-])OCC(COC(=O)CCCCCCC)OC(=O)CCCCCCC"),
 "ps": ("Fosfatidilserina (colas acortadas)", "[NH3+][C@@H](COP(=O)([O-])OCC(COC(=O)CCCCCCC)OC(=O)CCCCCCC)C(=O)[O-]"),
 "esfingosina": ("Esfingosina", "CCCCCCCCCCCCC/C=C/[C@@H](O)[C@@H](N)CO"),
 "ceramida": ("Ceramida (acilo acortado)", "CCCCCCCCCCCCC/C=C/[C@@H](O)[C@H](CO)NC(=O)CCCCCCC"),
 "esfingomielina": ("Esfingomielina (acilo acortado)", "CCCCCCCCCCCCC/C=C/[C@@H](O)[C@H](COP(=O)([O-])OCC[N+](C)(C)C)NC(=O)CCCCCCC"),
 "colesterol": ("Colesterol", "CC(C)CCC[C@@H](C)[C@H]1CC[C@H]2[C@@H]3CC=C4C[C@@H](O)CC[C@]4(C)[C@H]3CC[C@]12C"),
 "ergosterol": ("Ergosterol (hongos)", "CC(C)[C@@H](C)/C=C/[C@@H](C)[C@H]1CC[C@H]2C3=CC=C4C[C@@H](O)CC[C@]4(C)[C@H]3CC[C@]12C"),
 "acetoacetato": ("Acetoacetato", "CC(=O)CC(=O)[O-]"),
 "bhb": ("D-β-hidroxibutirato", "C[C@@H](O)CC(=O)[O-]"),
 "acetona": ("Acetona", "CC(C)=O"),
 "piruvato": ("Piruvato", "CC(=O)C(=O)[O-]"),
 "lactato": ("Lactato", "C[C@H](O)C(=O)[O-]"),
 "pep": ("Fosfoenolpiruvato (PEP)", "C=C(OP(=O)([O-])[O-])C(=O)[O-]"),
 "bpg": ("1,3-bisfosfoglicerato", "O=C(OP(=O)([O-])[O-])[C@H](O)COP(=O)([O-])[O-]"),
 "carnitina": ("Carnitina", "C[N+](C)(C)C[C@@H](O)CC(=O)[O-]"),
 "hmgcoa": ("HMG (parte acilo de la HMG-CoA)", "CC(O)(CC(=O)[O-])CC(=O)S*"),
 "malonil": ("Malonilo (parte acilo del malonil-CoA)", "[O-]C(=O)CC(=O)S*"),
 "citrato": ("Citrato", "OC(CC(=O)[O-])(CC(=O)[O-])C(=O)[O-]"),
 "oxalacetato": ("Oxalacetato", "O=C(CC(=O)[O-])C(=O)[O-]"),
}
for k, (n, smi) in S.items():
    w, h = (360, 200) if len(smi) > 60 else (300, 210)
    rd(k, n, smi, w, h)

exec(open("polys.py").read())
open("mols.js", "w").write("const MOL=" + json.dumps(MOL, ensure_ascii=False) + ";\n")
print(len(MOL), sum(len(v["svg"]) for v in MOL.values()))
