# Metabolismo de nucleótidos en "dibujitos" paso a paso.
# Reusa el reproductor de anim.py. Inserta 5 videos en t_n.html (idempotente).
import math, re
from anim import N, O, P, T, L, path, arrow, svg, bib, player, st

PU = "#1d1720"

# ------------------------------------------------------------ kit de personajes
def face(x, y, s=1.0, mood="smile", look=0):
    o = []
    for dx in (-7, 7):
        o.append(f"<ellipse cx='{x+dx*s:.1f}' cy='{y:.1f}' rx='{5*s:.1f}' ry='{6*s:.1f}' fill='#fff' stroke='{PU}' stroke-width='1'/>"
                 f"<circle cx='{x+dx*s+look*1.6*s:.1f}' cy='{y+1*s:.1f}' r='{2.7*s:.1f}' fill='{PU}'/>")
    if mood == "smile":
        o.append(f"<path d='M{x-5*s:.1f} {y+9*s:.1f} Q{x:.1f} {y+15*s:.1f} {x+5*s:.1f} {y+9*s:.1f}' stroke='{PU}' stroke-width='1.8' fill='none' stroke-linecap='round'/>")
    elif mood == "o":
        o.append(f"<ellipse cx='{x:.1f}' cy='{y+11*s:.1f}' rx='{3*s:.1f}' ry='{3.6*s:.1f}' fill='{PU}'/>")
    elif mood == "sad":
        o.append(f"<path d='M{x-5*s:.1f} {y+13*s:.1f} Q{x:.1f} {y+8*s:.1f} {x+5*s:.1f} {y+13*s:.1f}' stroke='{PU}' stroke-width='1.8' fill='none' stroke-linecap='round'/>")
    else:
        o.append(f"<line x1='{x-4*s:.1f}' y1='{y+11*s:.1f}' x2='{x+4*s:.1f}' y2='{y+11*s:.1f}' stroke='{PU}' stroke-width='1.8' stroke-linecap='round'/>")
    return "".join(o)

def names(x, y, name=None, sub=None, cls="lab"):
    o = ""
    if name:
        for i, ln in enumerate(name.split("|")):
            o += T(x, y + 16 * i, ln, cls)
        y += 16 * (len(name.split("|")) - 1)
    if sub:
        for i, ln in enumerate(sub.split("|")):
            o += T(x, y + 17 + 15 * i, ln, "lab2")
    return o

def blob(x, y, k, name=None, sub=None, r=26, mood="smile", look=0, carry=""):
    return (f"<g class='ch {k}'><circle cx='{x}' cy='{y}' r='{r}'/></g>" + face(x, y - 2, r / 24, mood, look) +
            carry + names(x, y + r + 17, name, sub))

def enzyme(x, y, name, sub=None, k="k-enz", mood="smile", look=0, w=54, h=46):
    return (f"<g class='ch {k}'><rect x='{x-w/2}' y='{y-h/2}' width='{w}' height='{h}' rx='12'/></g>" +
            face(x, y - 3, 1.05, mood, look) + names(x, y + h / 2 + 17, name, sub, "enz-n"))

def atom(x, y, lab, q, r=15):
    return f"<g class='at {q}'><circle cx='{x:.1f}' cy='{y:.1f}' r='{r}'/>{T(round(x,1), round(y+4.5,1), lab, 'at-t')}</g>"

def battery(x, y, lab="ATP", full=True):
    lv = 26 if full else 7
    c = "lv" if full else "lv lo"
    return (f"<g class='bat'><rect x='{x-17}' y='{y-10}' width='34' height='20' rx='4'/><rect x='{x+17}' y='{y-4}' width='4' height='8' rx='1'/>"
            f"<rect x='{x-14}' y='{y-7}' width='{lv}' height='14' rx='2' class='{c}'/></g>" + T(x, y + 26, lab, "lab2"))

def spend(x, y, lab="ATP", to="ADP", d=1.0):
    """pila llena que se gasta"""
    return O(battery(x, y, lab), d, 0, 0, .4) + N(battery(x, y, to, False), d, 0, 0, .4)

def badge(text, x=14, y=12):
    w = 34 + len(text) * 7.3
    return (f"<g class='loc'><rect x='{x}' y='{y}' width='{w:.0f}' height='28' rx='14'/>"
            f"<path d='M{x+18} {y+21} C{x+11} {y+13} {x+11} {y+7} {x+18} {y+7} C{x+25} {y+7} {x+25} {y+13} {x+18} {y+21}Z' class='pin'/>"
            f"<circle cx='{x+18}' cy='{y+12.5}' r='2.4' class='pinh'/></g>" + T(x + 30, y + 19, text, "loc-t", "start"))

def stop(x, y, text, a="start"):
    return (f"<g class='stp'><circle cx='{x}' cy='{y}' r='11'/><line x1='{x-5}' y1='{y}' x2='{x+5}' y2='{y}'/></g>" +
            "".join(T(x + (16 if a == "start" else -16), y + 5 + 16 * i, ln, "stp-t", a) for i, ln in enumerate(text.split("|"))))

def note(x, y, text, cls="lab2", a="middle"):
    return "".join(T(x, y + 16 * i, ln, cls, a) for i, ln in enumerate(text.split("|")))

def small(x, y, lab, k="k-sm", r=17):
    return f"<g class='chs {k}'><circle cx='{x}' cy='{y}' r='{r}'/></g>" + T(x, y + 4.5, lab, "at-t")

def pchain(x, y, n, step=-24, d=0):
    """n fosfatos en fila (hacia la izquierda por defecto)"""
    o = ""
    for i in range(n):
        px = x + step * i
        if i: o += L(px - step + (10 if step < 0 else -10), y, px + (10 if step < 0 else -10), y, "bond")
        o += f"<g class='ph'><circle cx='{px}' cy='{y}' r='10'/>{T(px, y + 4, 'P', 'ph-t')}</g>"
    return o

# ---------------------------------------------------------------- ribosa
def rib_pts(cx, cy, r=24):
    a = {"O": -90, "C1": -18, "C2": 54, "C3": 126, "C4": 198}
    return {k: (cx + r * math.cos(math.radians(v)), cy + r * math.sin(math.radians(v))) for k, v in a.items()}

def ribose(cx, cy, p5=0, pp1=False, deoxy=False, two=None, r=24, lab="ribosa", hl2=False):
    if two is None: two = deoxy or hl2
    v = rib_pts(cx, cy, r)
    pts = " ".join(f"{v[k][0]:.1f},{v[k][1]:.1f}" for k in ("O", "C1", "C2", "C3", "C4"))
    o = f"<polygon points='{pts}' class='rib'/>" + T(cx, cy + 4, lab, "rib-t")
    if p5:
        c4 = v["C4"]
        o += L(c4[0], c4[1], c4[0] - 12, c4[1] + 12, "bond") + pchain(c4[0] - 20, c4[1] + 18, p5)
    if pp1:
        c1 = v["C1"]
        o += L(c1[0], c1[1], c1[0] + 14, c1[1] - 4, "bond") + pchain(c1[0] + 24, c1[1] - 4, 2, 24)
    if two:
        c2 = v["C2"]
        cls = "de-t" if deoxy else "oh-t"
        o += L(c2[0], c2[1], c2[0] + 6, c2[1] + 12, "bond") + T(c2[0] + 10, c2[1] + 26, "H" if deoxy else "OH", cls)
        if hl2:
            o += P(f"<circle cx='{c2[0]+10:.1f}' cy='{c2[1]+21:.1f}' r='15' class='hlc'/>")
    return o

def rib_under(ax, ay, r=24, gap=30):
    """centro de ribosa para que su C1' quede debajo de (ax,ay)"""
    return ax - 0.951 * r, ay + gap + 0.309 * r

# ---------------------------------------------------------------- anillos
def pur_pos(hx, hy, R=38):
    def hp(a): return (hx + R * math.cos(math.radians(a)), hy + R * math.sin(math.radians(a)))
    p = {"C5": hp(-30), "C6": hp(-90), "N1": hp(-150), "C2": hp(150), "N3": hp(90), "C4": hp(30)}
    pc = (hx + 0.866 * R + 0.688 * R, hy); rp = 0.851 * R
    def pp(a): return (pc[0] + rp * math.cos(math.radians(a)), pc[1] + rp * math.sin(math.radians(a)))
    p.update({"N7": pp(-72), "C8": pp(0), "N9": pp(72)})
    p["_h"] = (hx, hy); p["_p"] = pc
    return p

PUR_B = [("C6", "N1"), ("N1", "C2"), ("C2", "N3"), ("N3", "C4"), ("C4", "C5"), ("C5", "C6"),
         ("C5", "N7"), ("N7", "C8"), ("C8", "N9"), ("N9", "C4")]
HEXA = ["C6", "N1", "C2", "N3", "C4", "C5"]; PENTA = ["C5", "N7", "C8", "N9", "C4"]

def pyr_pos(hx, hy, R=40):
    def hp(a): return (hx + R * math.cos(math.radians(a)), hy + R * math.sin(math.radians(a)))
    p = {"N1": hp(90), "C2": hp(150), "N3": hp(-150), "C4": hp(-90), "C5": hp(-30), "C6": hp(30)}
    p["_h"] = (hx, hy)
    return p

PYR_B = [("N1", "C2"), ("C2", "N3"), ("N3", "C4"), ("C4", "C5"), ("C5", "C6"), ("C6", "N1")]

def outward(p, a, L_=26):
    c = p["_p"] if a in ("N7", "C8", "N9") and "_p" in p else p["_h"]
    x, y = p[a]; dx, dy = x - c[0], y - c[1]; n = math.hypot(dx, dy)
    return x + dx / n * L_, y + dy / n * L_

def subst(p, a, lab, cls="sb", L_=28):
    x, y = p[a]; ex, ey = outward(p, a, L_)
    w = 11 if len(lab) <= 2 else 8 + 5.6 * len(lab)
    return (L(x, y, ex, ey, "bond") + f"<g class='{cls}'><ellipse cx='{ex:.1f}' cy='{ey:.1f}' rx='{w:.1f}' ry='11'/>"
            f"{T(round(ex,1), round(ey+4.5,1), lab, 'sb-t')}</g>")

def ring_atoms(p, present, src, newset=(), off=None, d=1.1, bonds=PUR_B, newbonds=(), dbl=(), bd=1.9):
    """dibuja enlaces + átomos; los de newset llegan volando desde off[atom]"""
    o = []
    for a, b in bonds:
        if a in present and b in present:
            ln = L(*p[a], *p[b], "rbond")
            if (a, b) in dbl or (b, a) in dbl:
                (x1, y1), (x2, y2) = p[a], p[b]
                cx_, cy_ = p["_h"]; mx, my = (x1 + x2) / 2 - cx_, (y1 + y2) / 2 - cy_
                n = math.hypot(mx, my); ox, oy = -mx / n * 7, -my / n * 7
                ln += L(x1 + ox * .9 + (x2 - x1) * .18, y1 + oy * .9 + (y2 - y1) * .18, x2 + ox * .9 - (x2 - x1) * .18, y2 + oy * .9 - (y2 - y1) * .18, "rbond")
            if (a, b) in newbonds or (b, a) in newbonds or a in newset or b in newset:
                o.append(N(ln, bd))
            else:
                o.append(ln)
    for a in present:
        g = atom(*p[a], a, src[a])
        if a in newset:
            dx, dy = (off or {}).get(a, (0, -80))
            o.append(N(g, d, round(dx), round(dy), .9))
        else:
            o.append(g)
    return "".join(o)

def silhouette(p, atoms_order, k):
    pts = " ".join(f"{p[a][0]:.1f},{p[a][1]:.1f}" for a in atoms_order)
    return f"<g class='ch {k}'><polygon points='{pts}' stroke-linejoin='round'/></g>"

def pur_char(hx, hy, k, subs=(), R=34, rib=None, name=None, sub=None, mood="smile", look=0):
    """purina como personaje: anillo relleno con cara; subs=[(atom,label)]; rib=dict(p5=..,deoxy=..)"""
    p = pur_pos(hx, hy, R)
    o = [silhouette(p, HEXA, k), silhouette(p, PENTA, k)]
    for a, lab in subs:
        o.append(subst(p, a, lab, L_=24))
    o.append(face(hx, hy - 2, 0.85, mood, look))
    ny = hy + R + 34
    if rib is not None:
        rc = rib_under(*p["N9"], 22, 22)
        o.append(L(*p["N9"], rc[0] + 0.951 * 22, rc[1] - 0.309 * 22, "bond"))
        o.append(ribose(*rc, r=22, **rib))
        ny = rc[1] + 62
    o.append(names(hx + 20, ny, name, sub))
    return "".join(o)

def pyr_char(hx, hy, k, subs=(), R=34, rib=None, name=None, sub=None, mood="smile", look=0):
    p = pyr_pos(hx, hy, R)
    o = [silhouette(p, ["N1", "C2", "N3", "C4", "C5", "C6"], k)]
    for a, lab in subs:
        o.append(subst(p, a, lab, L_=24))
    o.append(face(hx, hy - 2, 0.85, mood, look))
    ny = hy + R + 30
    if rib is not None:
        rc = rib_under(*p["N1"], 22, 20)
        o.append(L(*p["N1"], rc[0] + 0.951 * 22, rc[1] - 0.309 * 22, "bond"))
        o.append(ribose(*rc, r=22, **rib))
        ny = rc[1] + 62
    o.append(names(hx, ny, name, sub))
    return "".join(o)

def swap(before, after, d=2.1, dx=-120, dy=0):
    return O(N(before, 0, dx, dy, .8), d, 0, 0, .4) + (N(after, d, 0, 0, .4) if after else "")

def legend(items, y=382):
    """items: [(q, texto)]"""
    tot = sum(30 + len(t) * 6.6 for _, t in items) + 14 * (len(items) - 1)
    x = 400 - tot / 2; o = ""
    for q, t in items:
        o += f"<g class='at {q}'><circle cx='{x+8:.1f}' cy='{y-4}' r='8'/></g>" + T(round(x + 22, 1), y + 1, t, "lab2", "start")
        x += 30 + len(t) * 6.6 + 14
    return o

LEG_PUR = [("q-asp", "aspartato"), ("q-gln", "glutamina"), ("q-gly", "glicina"), ("q-for", "formilo (THF)"), ("q-co2", "CO₂")]
LEG_PYR = [("q-asp", "aspartato"), ("q-gln", "glutamina"), ("q-co2", "HCO₃⁻ (CO₂)")]

def cell_bg(mito=False):
    o = "<rect x='8' y='8' width='784' height='384' rx='40' class='cell'/>"
    if mito:
        o += ("<ellipse cx='640' cy='290' rx='140' ry='80' class='mito'/>"
              "<ellipse cx='640' cy='290' rx='122' ry='64' class='mito-in'/>" + T(640, 200, "mitocondria", "lab2"))
    return o

# ================================================================ 1. MAPA E INGREDIENTES
def map_frames():
    F = []
    # 1 célula
    b = (cell_bg() + T(400, 34, "una célula (los nucleótidos se fabrican sobre todo en el hígado)", "lab2") +
         N("<circle cx='640' cy='190' r='92' class='nuc'/>" + note(640, 175, "núcleo|acá se USAN:|ADN y ARN", "lab"), .1) +
         N("<ellipse cx='170' cy='300' rx='110' ry='52' class='mito'/><ellipse cx='170' cy='300' rx='96' ry='40' class='mito-in'/>" +
           note(170, 296, "mitocondria|1 solo paso (pirimidinas)", "lab2"), .4) +
         N(note(330, 120, "CITOSOL|acá se FABRICAN|purinas y pirimidinas", "lab"), .7) +
         N(enzyme(250, 205, None, mood="smile") + enzyme(320, 215, None, k="k-enz2", look=1) + enzyme(390, 205, None, k="k-enz3", look=-1), 1) +
         N(arrow(450, 210, 540, 200) + note(495, 235, "nucleótidos|listos", "lab2"), 1.4))
    F.append((svg(b, "Dónde pasa"), "¿Dónde pasa todo esto?",
              "Los nucleótidos se fabrican en el <b>citosol</b>, sobre todo en el hígado, y se usan en el <b>núcleo</b> para el ADN y el ARN. Solo un paso de las pirimidinas pasa en la <b>mitocondria</b>."))
    # 2 ribosa-5-P
    hexg = "<polygon points='150,150 176,165 176,195 150,210 124,195 124,165' class='glc'/>" + face(150, 178, .9)
    b = (badge("Citosol") + N(hexg + names(150, 232, "glucosa", "el azúcar de siempre"), 0, -60) +
         N(arrow(200, 180, 430, 180) + note(315, 160, "vía de las pentosas", "enz-n") + note(315, 205, "(también da NADPH,|que se usa más adelante)", "lab2"), .5) +
         N(ribose(520, 182, p5=1, lab="ribosa") + names(520, 232, "ribosa-5-P", "azúcar de 5 C|con un fosfato en el C5′"), 1.2, 40))
    F.append((svg(b, "Ribosa-5-P"), "El azúcar: ribosa-5-P",
              "La <b>ribosa-5-P</b> sale de la glucosa por la <b>vía de las pentosas</b>, en el citosol. Es el azúcar de todos los nucleótidos."))
    # 3 PRPP
    b = (badge("Citosol") + ribose(160, 182, p5=1) + names(160, 232, "ribosa-5-P") +
         N(battery(160, 90), .1, 0, -30) +
         N(enzyme(330, 120, "PRPP sintetasa"), .3, 0, -40) +
         N(arrow(240, 182, 430, 182), .6) +
         N(ribose(540, 182, p5=1, pp1=True) + names(550, 232, "PRPP", "ribosa «activada»: lleva|un pirofosfato (PP) en el C1′"), 1, 30) +
         N(small(330, 290, "AMP", "k-sm") + T(330, 325, "sale AMP", "lab2"), 1.3, 0, 30) +
         N(note(560, 90, "el PP del C1′ es el «enchufe»|donde después se pega la base", "lab"), 1.8))
    F.append((svg(b, "PRPP"), "PRPP: la plataforma",
              "La <b>PRPP sintetasa</b> le pasa un pirofosfato del ATP a la ribosa-5-P y forma el <b>PRPP</b>. Es la ribosa lista para recibir una base: la usan <b>todos</b> los nucleótidos."))
    # 4 glutamina
    carry = atom(205, 160, "N", "q-gln", 13)
    b = (badge("En todas las células") +
         blob(110, 180, "k-glu", "glutamato", "aminoácido") + N(small(110, 90, "NH₄⁺", "k-sm"), .1, 0, -30) + N(battery(110, 290), .1) +
         N(enzyme(290, 120, "glutamina sintetasa"), .3, 0, -40) + N(arrow(160, 180, 400, 180), .6) +
         N(blob(470, 180, "k-gln", "glutamina", "glutamato + 1 N extra", carry=atom(500, 160, "N", "q-gln", 13)), 1, 40) +
         N(note(640, 120, "viaja por la sangre|y está en todas las células:|es el «camión» de N", "lab"), 1.5) +
         N(path("M470 255 C440 340 150 340 115 262", "arr") + f"<polygon points='115,262 110,276 122,272' class='arrh'/>" + note(290, 350, "da su N y vuelve a ser glutamato", "lab2"), 2))
    F.append((svg(b, "Glutamina"), "¿De dónde sale la glutamina?",
              "La glutamina es el glutamato con un nitrógeno (N) extra que le agrega la <b>glutamina sintetasa</b>. Es el gran transportador de N: lo regala en los nucleótidos y vuelve a ser glutamato." + bib("Para entender")))
    # 5 aspartato
    b = (badge("Mitocondria → citosol") +
         "<circle cx='130' cy='180' r='62' class='krebs'/>" + T(130, 176, "ciclo de", "lab2") + T(130, 194, "Krebs", "lab") +
         path("M130 118 A62 62 0 1 1 72 160", "arr") +
         N(small(250, 180, "OAA", "k-sm", 22) + T(250, 222, "oxalacetato", "lab2"), .2, -40) +
         N(arrow(280, 180, 450, 180) + note(370, 160, "transaminación", "enz-n") + note(375, 245, "le pasa un N|(desde el glutamato)", "lab2"), .6) +
         N(blob(510, 180, "k-asp", "aspartato", "aminoácido con N", carry=atom(540, 160, "N", "q-asp", 13)), 1.2, 40) +
         N(note(660, 110, "en purinas: da solo su N", "lab", "middle") + note(660, 140, "en pirimidinas: entra casi entero", "lab"), 1.8))
    F.append((svg(b, "Aspartato"), "¿De dónde sale el aspartato?",
              "El <b>aspartato</b> se forma a partir del oxalacetato (del ciclo de Krebs) cuando recibe un N por transaminación." + bib("Para entender")))
    # 6 glicina y THF
    b = (badge("Citosol") +
         blob(110, 170, "k-ser", "serina", "aminoácido") +
         N(arrow(150, 170, 290, 120) + arrow(150, 175, 290, 245), .3) +
         N(blob(350, 110, "k-gly", "glicina", "el aminoácido más chico"), .6, -40) +
         N(blob(350, 250, "k-thf", "THF", "viene del ácido fólico|(vitamina B9, de la dieta)"), .6, -40) +
         N(atom(380, 230, "C", "q-for", 13) + note(470, 238, "la serina le pasa|1 carbono al THF", "lab2", "start"), 1.2, -200, -60) +
         N(note(560, 100, "THF = una «grúa» de 1 carbono.", "lab", "start") +
           note(560, 124, "Lo carga como formilo (–CHO)|o como metileno (–CH₂–)|y lo entrega donde haga falta.", "lab2", "start"), 1.7) +
         N(note(560, 300, "Nosotros NO fabricamos folato:|lo comemos (verduras de hoja).", "lab", "start"), 2.1))
    F.append((svg(b, "Glicina y THF"), "Glicina y THF",
              "La <b>glicina</b> sale de la serina. En ese paso, la serina le pasa un carbono al <b>THF</b> (tetrahidrofolato, de la vitamina B9). El THF es una «grúa» que lleva carbonos sueltos."))
    # 7 CO2 y ATP
    b = (badge("En todas las células") +
         N(small(170, 170, "CO₂", "k-co2", 30) + note(170, 225, "de la respiración|(el Krebs lo libera)", "lab2"), 0, 0, 30) +
         N(arrow(210, 170, 330, 170), .4) +
         N(small(390, 170, "HCO₃⁻", "k-co2", 34) + note(390, 228, "bicarbonato:|el CO₂ disuelto", "lab2"), .7, -30) +
         N(battery(600, 140) + battery(660, 140) + battery(630, 200), 1.1) +
         N(note(630, 250, "ATP: la «pila» de cada paso.|Armar un anillo cuesta varias.", "lab"), 1.5))
    F.append((svg(b, "CO2 y ATP"), "CO₂ y ATP",
              "El <b>CO₂</b> (como bicarbonato, HCO₃⁻) aporta un carbono. El <b>ATP</b> es la energía: casi cada paso de armado gasta uno."))
    # 8 resumen ingredientes
    rows = [("k-gln", "glutamina", "da N", "N3 y N9", "N3 (vía carbamoil-P)|y el NH₂ del CTP"),
            ("k-asp", "aspartato", "da N (o casi todo)", "N1", "N1, C4, C5 y C6"),
            ("k-gly", "glicina", "entra entera", "C4, C5 y N7", "—"),
            ("k-thf", "THF", "da 1 C", "C2 y C8", "(el CH₃ de la T)"),
            ("k-co2", "CO₂", "da 1 C", "C6", "C2")]
    b = T(150, 40, "ingrediente", "lab") + T(470, 40, "en purinas", "lab") + T(660, 40, "en pirimidinas", "lab")
    for i, (k, nm, what, pu, py) in enumerate(rows):
        y = 85 + i * 64
        b += N(f"<g class='ch {k}'><circle cx='70' cy='{y}' r='22'/></g>" + face(70, y - 2, .9) +
               T(105, y - 2, nm, "lab", "start") + T(105, y + 16, what, "lab2", "start") +
               note(470, y + 2, pu, "lab") + note(660, y - 4 if "|" in py else y + 2, py, "lab2"), .25 * i, -30)
    F.append((svg(b, "Resumen de ingredientes"), "Resumen: quién da qué",
              "Tabla para tener a mano: qué átomos de cada anillo aporta cada ingrediente. En los próximos videos los vas a ver llegar uno por uno."))
    return F

# ================================================================ 2. PURINAS DE NOVO
PH, PHY, PR = 400, 150, 38
PP = pur_pos(PH, PHY, PR)
PSRC = {"N9": "q-gln", "C4": "q-gly", "C5": "q-gly", "N7": "q-gly", "C8": "q-for", "N3": "q-gln",
        "C6": "q-co2", "N1": "q-asp", "C2": "q-for"}
RC = rib_under(*PP["N9"], 24, 30)

def pur_base(present):
    """ribosa con P en 5' + enlace a N9 si está"""
    o = ribose(*RC, p5=1, pp1=("N9" not in present))
    if "N9" in present:
        c1 = rib_pts(*RC)["C1"]
        o = L(*PP["N9"], *c1, "bond") + o
    return o

def ghost():
    return "".join(f"<circle cx='{PP[a][0]:.1f}' cy='{PP[a][1]:.1f}' r='15' class='ghost'/>" for a in PSRC)

def pur_step(present, new, carrier, after=None, enz=None, extra="", cx=150, cy=170, d=1.1):
    """carrier: (k, nombre, sub). Los átomos nuevos salen del personaje."""
    k, nm, sb = carrier
    carry = "".join(atom(cx + 34 + 0 * i, cy - 26 + 30 * i, a, PSRC[a], 13) for i, a in enumerate(new))
    off = {a: (cx + 34 - PP[a][0], cy - 26 + 30 * i - PP[a][1]) for i, a in enumerate(new)}
    o = [badge("Citosol (sobre todo hígado)"), ghost(), pur_base(present | set(new)) if "N9" in new else pur_base(present),
         ring_atoms(PP, present | set(new), PSRC, set(new), off, d)]
    o.append(O(N(carry, 0, -120, 0, .8), d, 0, 0, .25))
    o.append(swap(blob(cx, cy, k, nm, sb), blob(cx, cy, k, after[0], after[1]) if after else None))
    if enz: o.append(N(enz, .2, 0, -30))
    o.append(extra)
    o.append(legend(LEG_PUR))
    return "".join(o)

def pur_frames():
    F = []
    # 1 PRPP + fantasma
    b = (badge("Citosol (sobre todo hígado)") + N(ghost(), .5) + ribose(*RC, p5=1, pp1=True) +
         names(RC[0], RC[1] + 44, "PRPP") +
         N(note(PH + 30, 70, "acá se va a armar el anillo,|átomo por átomo", "lab"), .9) +
         N(note(640, 170, "Las purinas (A y G)|se construyen ENCIMA|de la ribosa", "lab"), 1.3) +
         legend(LEG_PUR))
    F.append((svg(b, "Arranque"), "Se arma encima del PRPP",
              "En las purinas, la ribosa (como <b>PRPP</b>) está desde el principio y el anillo se arma encima, átomo por átomo. Cada átomo tiene el color de quien lo trajo."))
    # 2 amidotransferasa N9
    enz = enzyme(650, 75, "Glutamina-PRPP|amidotransferasa", None, "k-enz")
    ex = (N(T(650, 30, "PASO COMPROMETIDO", "tagc"), .4) +
          N(stop(570, 170, "la frenan IMP,|AMP y GMP|(retroinhibición)") , 1.6) +
          O(pchain(RC[0] + 0.951 * 24 + 24, RC[1] - 0.309 * 24 - 4, 2, 24), 1.0, 60, 30) +
          N(small(560, 290, "PPi", "k-sm") , 1.2, -60, -30))
    b = pur_step(set(), ["N9"], ("k-gln", "glutamina", "trae N"), ("glutamato", "ya sin su N"), enz, ex)
    F.append((svg(b, "N9"), "1. Entra el primer N (de la glutamina)",
              "La <b>glutamina-PRPP amidotransferasa</b> cambia el PP del PRPP por el N de la glutamina: ese será el <b>N9</b>. Es el <b>paso comprometido</b>, y los productos finales (IMP, AMP y GMP) lo frenan."))
    # 3 glicina
    ex = spend(640, 220, d=1.2) + N(note(640, 120, "la glicina entra ENTERA:|aporta C4, C5 y N7", "lab"), 1.5)
    b = pur_step({"N9"}, ["C4", "C5", "N7"], ("k-gly", "glicina", "aminoácido chiquito"), None, None, ex)
    F.append((svg(b, "Glicina"), "2. Entra la glicina entera",
              "Se suma una <b>glicina</b> completa, gastando ATP. Aporta 3 átomos de un saque: <b>C4, C5 y N7</b>."))
    # 4 formilo C8
    ex = N(note(640, 120, "el THF trae un formilo (1 C)|y lo deja como C8", "lab"), 1.5)
    b = pur_step({"N9", "C4", "C5", "N7"}, ["C8"], ("k-thf", "N¹⁰-formil-THF", "lleva 1 C"), ("THF", "vacío, vuelve a cargar"), None, ex)
    F.append((svg(b, "C8"), "3. El THF trae un carbono (C8)",
              "El <b>N¹⁰-formil-THF</b> (la «grúa» de 1 carbono) entrega un formilo que será el <b>C8</b>."))
    # 5 glutamina N3
    ex = spend(640, 220, d=1.2) + N(note(640, 120, "otra glutamina regala|su N: será el N3", "lab"), 1.5)
    b = pur_step({"N9", "C4", "C5", "N7", "C8"}, ["N3"], ("k-gln", "glutamina", "trae N"), ("glutamato", ""), None, ex)
    F.append((svg(b, "N3"), "4. Otra glutamina (N3)",
              "Una segunda <b>glutamina</b> da su N, que será el <b>N3</b>. También gasta ATP."))
    # 6 cierra el anillo chico + CO2
    pres = {"N9", "C4", "C5", "N7", "C8", "N3"}
    b = (badge("Citosol (sobre todo hígado)") + ghost() + pur_base(pres) +
         ring_atoms(PP, pres | {"C6"}, PSRC, {"C6"}, {"C6": (150 - PP["C6"][0], 170 - PP["C6"][1])}, 1.5, newbonds=[("C8", "N9")], bd=.4) +
         N(P(f"<circle cx='{(PP['C8'][0]+PP['N9'][0])/2:.1f}' cy='{(PP['C8'][1]+PP['N9'][1])/2:.1f}' r='14' class='hlc'/>"), .3) +
         N(small(150, 170, "CO₂", "k-co2", 26), .8, -120, 0, .7) + O(small(150, 170, "CO₂", "k-co2", 26), 1.5, 0, 0, .3) +
         spend(640, 220, d=.4) + N(note(640, 110, "se cierra el anillo de 5|y el CO₂ aporta el C6", "lab"), 1.8) + legend(LEG_PUR))
    F.append((svg(b, "Anillo chico y C6"), "5. Se cierra el anillo chico y entra el CO₂",
              "Se cierra el anillo de 5 (con gasto de ATP). Después un <b>CO₂</b> se pega y será el <b>C6</b>."))
    # 7 aspartato N1
    ex = spend(640, 220, d=1.2) + N(note(640, 100, "el aspartato deja SOLO su N|y se va como fumarato", "lab"), 1.6)
    b = pur_step(pres | {"C6"}, ["N1"], ("k-asp", "aspartato", "trae N"), ("fumarato", "lo que sobra"), None, ex)
    F.append((svg(b, "N1"), "6. El aspartato da el N1",
              "El <b>aspartato</b> se pega, deja su N (será el <b>N1</b>) y el resto se suelta como <b>fumarato</b>. Gasta ATP."))
    # 8 formilo C2 -> IMP
    pres2 = pres | {"C6", "N1"}
    ex = (N(subst(PP, "C6", "O", L_=26), 2.4) +
          N(note(640, 90, "se cierra el anillo de 6:|¡nació el IMP!", "lab") + note(640, 140, "su base es la hipoxantina", "lab2"), 2.5) +
          N(face(PH, PHY - 2, .8), 2.8))
    b = pur_step(pres2, ["C2"], ("k-thf", "N¹⁰-formil-THF", "lleva 1 C"), ("THF", ""), None, ex)
    b = b.replace(ring_atoms(PP, pres2 | {"C2"}, PSRC, {"C2"}, {"C2": (150 + 34 - PP["C2"][0], 170 - 26 - PP["C2"][1])}, 1.1),
                  ring_atoms(PP, pres2 | {"C2"}, PSRC, {"C2"}, {"C2": (150 + 34 - PP["C2"][0], 170 - 26 - PP["C2"][1])}, 1.1, bd=1.9))
    F.append((svg(b, "C2 e IMP"), "7. Segundo formilo (C2): IMP",
              "Otro <b>N¹⁰-formil-THF</b> trae el <b>C2</b> y se cierra el anillo de 6. Sale el <b>IMP</b> (inosina monofosfato), cuya base es la <b>hipoxantina</b>. Es el primer nucleótido de purina."))
    # 9 resumen colores
    allp = set(PSRC)
    b = (pur_base(allp) + ring_atoms(PP, allp, PSRC) + subst(PP, "C6", "O", L_=26) +
         N(note(150, 70, "Para memorizar (9 átomos):", "lab", "start"), .1) +
         N(note(560, 110, "glicina → 3 (C4, C5, N7)|glutamina → 2 (N3, N9)|formilo del THF → 2 (C2, C8)|aspartato → 1 (N1)|CO₂ → 1 (C6)", "lab", "start"), .4) +
         N(note(560, 230, "~5 ATP en total", "lab2", "start"), .8) + legend(LEG_PUR))
    F.append((svg(b, "Resumen del anillo"), "Resumen: de dónde viene cada átomo",
              "Glicina: 3 átomos. Glutamina: 2. Formilo (THF): 2. Aspartato: 1. CO₂: 1. Total: 9 átomos."))
    # 10 IMP -> AMP / GMP
    b = (badge("Citosol") +
         pur_char(370, 120, "k-imp", [("C6", "O")], R=30, rib={"p5": 1}, name="IMP", sub="base: hipoxantina") +
         N(arrow(320, 130, 210, 130) + note(262, 92, "+ aspartato", "lab2") + note(262, 160, "gasta GTP", "lab"), .3) +
         N(pur_char(100, 120, "k-amp", [("C6", "NH₂")], R=30, rib={"p5": 1}, name="AMP", sub="base: adenina"), .7, 40) +
         N(arrow(460, 120, 540, 90) + note(505, 70, "NAD⁺", "lab2"), 1.1) +
         N(pur_char(585, 80, "k-xmp", [("C6", "O"), ("C2", "O")], R=22) + T(640, 50, "XMP", "lab", "start"), 1.4, -30) +
         N(arrow(640, 120, 650, 175) + note(668, 145, "+ glutamina (N)", "lab2", "start") + note(668, 162, "gasta ATP", "lab", "start"), 1.8) +
         N(pur_char(640, 225, "k-gua", [("C6", "O"), ("C2", "NH₂")], R=26, rib={"p5": 1}, name="GMP", sub="base: guanina"), 2.1, 0, -20) +
         N(stop(40, 300, "el AMP frena su rama") + stop(300, 345, "el GMP frena su rama"), 2.4) + N(note(160, 375, "cruzado: AMP gasta GTP · GMP gasta ATP", "lab2", "start"), 2.6))
    F.append((svg(b, "AMP y GMP"), "8. Del IMP salen AMP y GMP",
              "<b>IMP → AMP</b>: se suma aspartato y se gasta <b>GTP</b>. <b>IMP → XMP → GMP</b>: se usa NAD⁺, glutamina y <b>ATP</b>. Cada producto frena su propia rama."))
    return F

# ================================================================ 3. PIRIMIDINAS
YH, YHY, YR = 400, 160, 48
YP = pyr_pos(YH, YHY, YR)
YSRC = {"C2": "q-co2", "N3": "q-gln", "N1": "q-asp", "C6": "q-asp", "C5": "q-asp", "C4": "q-asp"}

def pyr_frames():
    F = []
    LEG = legend(LEG_PYR)
    cpP = lambda: L(*YP["C2"], YP["C2"][0] - 34, YP["C2"][1] - 4, "bond") + pchain(YP["C2"][0] - 44, YP["C2"][1] - 4, 1)
    O2 = lambda: subst(YP, "C2", "O", L_=28)
    O4 = lambda: subst(YP, "C4", "O", L_=28)
    COO = lambda: subst(YP, "C6", "COO⁻", L_=34)
    # 1 CPS II
    b = (badge("Citosol") +
         N(small(120, 110, "HCO₃⁻", "k-co2", 30), 0, -80) + N(blob(120, 250, "k-gln", "glutamina", "trae N", carry=atom(150, 230, "N", "q-gln", 13)), .1, -80) +
         N(battery(250, 60) + battery(300, 60), .2) +
         N(enzyme(650, 80, "carbamoil fosfato|sintetasa II (CPS II)"), .3, 0, -30) +
         ring_atoms(YP, {"C2", "N3"}, YSRC, {"C2", "N3"}, {"C2": (120 - YP["C2"][0], 110 - YP["C2"][1]), "N3": (150 - YP["N3"][0], 230 - YP["N3"][1])}, 1, bonds=PYR_B) +
         N(O2() + cpP(), 1.6) + N(note(YH - 10, 300, "carbamoil fosfato", "lab"), 1.8) +
         N(note(650, 170, "¡ojo! la CPS I es otra:|está en la mitocondria,|usa NH₄⁺ y sirve para la urea", "lab2"), 2.2) + LEG)
    F.append((svg(b, "CPS II"), "1. Carbamoil fosfato",
              "En el citosol, la <b>carbamoil fosfato sintetasa II</b> junta bicarbonato (HCO₃⁻), el N de la glutamina y 2 ATP: sale el <b>carbamoil fosfato</b>. Aporta el <b>C2</b> y el <b>N3</b>."))
    # 2 ATCasa
    asp_at = {a: (150 + 34, 130 + 26 * i) for i, a in enumerate(["N1", "C6", "C5", "C4"])}
    off = {a: (asp_at[a][0] - YP[a][0], asp_at[a][1] - YP[a][1]) for a in asp_at}
    pres = {"C2", "N3", "N1", "C6", "C5", "C4"}
    b = (badge("Citosol") +
         ring_atoms(YP, pres, YSRC, {"N1", "C6", "C5", "C4"}, off, 1.1,
                    bonds=[("N1", "C2"), ("C2", "N3"), ("C4", "C5"), ("C5", "C6"), ("C6", "N1")]) + O2() +
         O(cpP(), 1.0, -40, 30) + N(small(250, 330, "Pi", "k-sm"), 1.2, 40, -40) +

         O(N("".join(atom(*asp_at[a], a, "q-asp", 13) for a in asp_at), 0, -100, 0, .8), 1.1, 0, 0, .25) +
         swap(blob(150, 180, "k-asp", "aspartato", "entra casi entero"), None, 2.0, -100) +
         N(O4() + COO(), 2.0) +
         N(enzyme(650, 80, "ATCasa", "aspartato|transcarbamilasa"), .2, 0, -30) +
         N(T(650, 30, "PASO COMPROMETIDO", "tagc"), .4) +
         N(stop(560, 200, "CTP la frena") + note(575, 236, "⊕ ATP la activa", "lab2", "start"), 1.6) +
         N(note(YH, 300, "carbamoil aspartato (todavía abierto)", "lab"), 2.2) + LEG)
    F.append((svg(b, "ATCasa"), "2. ATCasa: entra el aspartato",
              "La <b>ATCasa</b> (aspartato transcarbamilasa) une el <b>aspartato</b>, que trae N1, C6, C5 y C4, al carbamoil fosfato. Sale Pi. Es el <b>paso comprometido</b>: el CTP la frena y el ATP la activa." + bib("En animales se regula sobre todo la CPS II")))
    # 3 dihidroorotasa
    b = (badge("Citosol") + ring_atoms(YP, pres, YSRC, bonds=PYR_B, newbonds=[("N3", "C4")], bd=.5) + O2() + O4() + COO() +
         N(P(f"<circle cx='{(YP['N3'][0]+YP['C4'][0])/2:.1f}' cy='{(YP['N3'][1]+YP['C4'][1])/2:.1f}' r='14' class='hlc'/>"), .3) +
         N(enzyme(650, 80, "dihidroorotasa"), 0, 0, -30) + N(small(560, 260, "H₂O", "k-sm"), 1, -60, -40) +
         N(note(YH, 300, "dihidroorotato: ¡ya es un anillo!", "lab"), 1.2) + LEG)
    F.append((svg(b, "Dihidroorotasa"), "3. Se cierra el anillo",
              "La <b>dihidroorotasa</b> une el N3 con el C4 y se cierra el anillo de 6 (sale agua). Queda el <b>dihidroorotato</b>."))
    # 4 DHODH en la mitocondria
    b = (cell_bg(mito=True) + badge("Membrana interna de la mitocondria") +
         ring_atoms(YP, pres, YSRC, bonds=PYR_B, dbl=[("C5", "C6")], newbonds=[("C5", "C6")], bd=1) + O2() + O4() + COO() +
         N(enzyme(590, 275, "dihidroorotato|deshidrogenasa"), 0, 0, 40) +
         N(small(490, 110, "2 H", "k-sm") , 1, -60, 30) + N(path("M510 110 C640 110 700 180 700 250", "arr"), 1.3) +
         N(small(700, 272, "Q", "k-sm") + note(720, 316, "→ QH₂", "lab2", "start"), 1.5) +
         N(note(YH - 40, 300, "orotato (ganó|un doble enlace)", "lab"), 1.6) + LEG)
    F.append((svg(b, "DHODH"), "4. El único paso en la mitocondria",
              "La <b>dihidroorotato deshidrogenasa</b>, pegada a la membrana interna de la mitocondria, saca 2 H y se los da a la <b>ubiquinona</b> (Q). Queda el <b>orotato</b>." + bib("Detalle de bibliografía")))
    # 5 OPRT: + PRPP
    rc = rib_under(*YP["N1"], 24, 30)
    c1 = rib_pts(*rc)["C1"]
    b = (badge("Citosol") + ring_atoms(YP, pres, YSRC, bonds=PYR_B, dbl=[("C5", "C6")]) + O2() + O4() + COO() +
         N(ribose(*rc, p5=1, pp1=True), 0, -200, 40, 1) + O(pchain(c1[0] + 24, c1[1] - 4, 2, 24), 1.3, 60, 40) +
         N(L(*YP["N1"], *c1, "bond"), 1.4) + N(small(620, 330, "PPi", "k-sm"), 1.4, -60, -20) +
         N(enzyme(650, 80, "orotato fosforribosil|transferasa"), .2, 0, -30) +
         N(note(150, 90, "¡recién ahora|llega la ribosa!", "lab"), 1.6) + N(note(650, 250, "OMP", "lab"), 1.8) + LEG)
    F.append((svg(b, "OMP"), "5. Llega el PRPP: OMP",
              "Recién ahora se pega la ribosa: el orotato toma la ribosa-5-P del <b>PRPP</b> (sale PPi) y queda el <b>OMP</b> (orotidina monofosfato). Es al revés que en las purinas."))
    # 6 descarboxilación -> UMP
    rib5 = L(*YP["N1"], *c1, "bond") + ribose(*rc, p5=1)
    b = (badge("Citosol") + ring_atoms(YP, pres, YSRC, bonds=PYR_B, dbl=[("C5", "C6")]) + O2() + O4() + rib5 +
         O(COO(), .8, 120, -40) + N(small(560, 110, "CO₂", "k-co2", 22), 1.2, -60, 20) +
         N(enzyme(650, 250, "OMP|descarboxilasa"), 0, 0, 30) +
         N(face(YH, YHY - 2, .8), 1.6) + N(note(170, 120, "UMP|(base: uracilo)", "lab"), 1.6) + LEG)
    F.append((svg(b, "UMP"), "6. Sale un CO₂: UMP",
              "La <b>OMP descarboxilasa</b> le saca el carboxilo (sale CO₂). Queda el <b>UMP</b>, cuya base es el uracilo: el primer nucleótido de pirimidina."))
    # 7 UMP -> UDP -> UTP
    b = (badge("Citosol") +
         pyr_char(140, 150, "k-ump", [("C2", "O"), ("C4", "O")], rib={"p5": 1}, name="UMP") +
         N(arrow(205, 160, 300, 160) + battery(252, 120), .3) +
         N(pyr_char(390, 150, "k-ump", [("C2", "O"), ("C4", "O")], rib={"p5": 2}, name="UDP"), .7, -30) +
         N(arrow(455, 160, 550, 160) + battery(502, 120), 1.1) +
         N(pyr_char(650, 150, "k-ump", [("C2", "O"), ("C4", "O")], rib={"p5": 3}, name="UTP"), 1.5, -30) +
         N(note(400, 360, "quinasas: cada una le pasa un fosfato del ATP", "lab2"), 1.8))
    F.append((svg(b, "UTP"), "7. UMP → UDP → UTP",
              "Unas <b>quinasas</b> le van sumando fosfatos que sacan del ATP: UMP → UDP → UTP."))
    # 8 CTP sintetasa
    up = pyr_pos(430, 150, 34)
    b = (badge("Citosol") +
         O(pyr_char(430, 150, "k-ump", [("C2", "O"), ("C4", "O")], rib={"p5": 3}, name="UTP"), 1.4, 0, 0, .4) +
         N(pyr_char(430, 150, "k-ctp", [("C2", "O"), ("C4", "NH₂")], rib={"p5": 3}, name="CTP", sub="base: citosina"), 1.4, 0, 0, .4) +

         O(N(atom(200, 130, "N", "q-gln", 13), 0, -100, 0, .8), 1.0, up["C4"][0] - 200, up["C4"][1] - 150, .5) +
         swap(blob(170, 150, "k-gln", "glutamina", "trae N"), blob(170, 150, "k-gln", "glutamato", "ya sin su N"), 1.9, -100) +
         N(battery(300, 280), .3) + N(enzyme(660, 90, "CTP sintetasa"), .2, 0, -30) +
         N(note(660, 200, "cambia el O del C4|por un NH₂", "lab"), 1.8))
    F.append((svg(b, "CTP"), "8. UTP → CTP",
              "La <b>CTP sintetasa</b> cambia el O del C4 por un NH₂ que trae la <b>glutamina</b> (gasta ATP). El uracilo pasa a ser citosina: sale el <b>CTP</b>."))
    # 9 resumen
    b = (ring_atoms(YP, pres, YSRC, bonds=PYR_B, dbl=[("C5", "C6")]) + O2() + O4() +
         L(*YP["N1"], *c1, "bond") + ribose(*rc, p5=1) +
         N(note(560, 90, "aspartato → 4 (N1, C4, C5, C6)|carbamoil fosfato → 2:|   C2 (del HCO₃⁻)|   N3 (de la glutamina)", "lab", "start"), .3) +
         N(note(560, 210, "Purinas: ribosa primero,|anillo encima.", "lab2", "start") +
           note(560, 260, "Pirimidinas: anillo primero,|ribosa después.", "lab2", "start"), .8) + LEG)
    F.append((svg(b, "Resumen pirimidinas"), "Resumen: anillo de pirimidina",
              "El <b>aspartato</b> da 4 átomos y el <b>carbamoil fosfato</b> da 2 (el C2 del bicarbonato y el N3 de la glutamina). Primero se arma el anillo y después se pega el PRPP."))
    return F

# ================================================================ 4. DESOXI Y TIMIDILATO
def dx_frames():
    F = []
    # 1 RNR
    b = (badge("Citosol") +
         pur_char(150, 120, "k-gen", rib={"p5": 2, "hl2": True}, name="NDP", sub="ADP, GDP, CDP o UDP|(ribosa con OH en el 2′)") +
         N(enzyme(400, 90, "ribonucleótido|reductasa"), .2, 0, -30) + N(arrow(270, 180, 520, 180), .5) +
         N(blob(400, 290, "k-nadph", "NADPH", "da los electrones"), .6, 0, 40) +
         N(pur_char(620, 120, "k-gen", rib={"p5": 2, "deoxy": True, "hl2": True}, name="dNDP", sub="desoxirribosa:|H en el 2′"), 1.2, 30) +
         N(small(530, 300, "H₂O", "k-sm"), 1.4, -60, -40))
    F.append((svg(b, "Ribonucleótido reductasa"), "1. De ribo a desoxi",
              "La <b>ribonucleótido reductasa</b> le saca el OH del carbono 2′ a la ribosa de un <b>difosfato</b> (ADP, GDP, CDP, UDP). Los electrones vienen del <b>NADPH</b>. Siempre va de ribo a desoxi, nunca al revés."))
    # 2 dNDP -> dNTP
    b = (badge("Citosol") +
         pur_char(170, 130, "k-gen", rib={"p5": 2, "deoxy": True}, name="dNDP") +
         N(arrow(250, 170, 450, 170) + battery(350, 130) + note(350, 205, "quinasa", "enz-n"), .3) +
         N(pur_char(560, 130, "k-gen", rib={"p5": 3, "deoxy": True}, name="dNTP", sub="dATP, dGTP, dCTP…"), .9, -30) +
         N(note(400, 340, "los dNTP son los ladrillos que usa la ADN polimerasa", "lab"), 1.4))
    F.append((svg(b, "dNTP"), "2. dNDP → dNTP",
              "Una quinasa le suma el tercer fosfato y queda el <b>dNTP</b>: el ladrillo que usa la ADN polimerasa."))
    # 3 dUMP y dUTPasa
    b = (badge("Citosol") +
         pyr_char(150, 130, "k-ump", [("C2", "O"), ("C4", "O")], rib={"p5": 3, "deoxy": True}, name="dUTP", mood="o") +
         N(enzyme(370, 90, "dUTPasa"), .2, 0, -30) + N(arrow(240, 170, 480, 170), .5) +
         N(pyr_char(590, 130, "k-ump", [("C2", "O"), ("C4", "O")], rib={"p5": 1, "deoxy": True}, name="dUMP"), 1, -30) +
         N(small(370, 270, "PPi", "k-sm"), 1.2, 0, -40) +
         N(note(400, 345, "así el dUTP queda casi en cero y no se mete U en el ADN", "lab"), 1.5))
    F.append((svg(b, "dUMP"), "3. ¿Y la timina? Primero, dUMP",
              "El ADN no lleva U. La <b>dUTPasa</b> rompe el dUTP y deja <b>dUMP</b>: así no se cuela U en el ADN y se tiene la materia prima para la T."))
    # 4 timidilato sintasa
    ump = pyr_pos(170, 150, 34)
    b = (badge("Citosol") +
         O(pyr_char(170, 150, "k-ump", [("C2", "O"), ("C4", "O")], rib={"p5": 1, "deoxy": True}, name="dUMP"), 1.5, 0, 0, .4) +
         N(pyr_char(170, 150, "k-dtmp", [("C2", "O"), ("C4", "O"), ("C5", "CH₃")], rib={"p5": 1, "deoxy": True}, name="dTMP", sub="base: timina"), 1.5, 0, 0, .4) +

         O(N(atom(590, 128, "C", "q-for", 13), 0, 80, 0, .8), 1.0, ump["C5"][0] + 20 - 590, ump["C5"][1] - 20 - 128, .6) +
         swap(blob(560, 150, "k-thf", "N⁵,N¹⁰-metilen-THF", "trae 1 C"), blob(560, 150, "k-dhf", "DHF", "THF «gastado»", mood="flat"), 1.9, 80) +
         N(enzyme(370, 70, "timidilato sintasa"), .2, 0, -30) +
         N(stop(330, 290, "5-fluorouracilo (como FdUMP)|la bloquea: inhibidor suicida"), 2.3))
    F.append((svg(b, "Timidilato sintasa"), "4. Timidilato sintasa: U → T",
              "La <b>timidilato sintasa</b> le pone un CH₃ al C5 del uracilo: <b>dUMP → dTMP</b> (timina). El carbono lo da el <b>metilen-THF</b>, que queda como <b>DHF</b>. El 5-fluorouracilo la bloquea."))
    # 5 DHFR
    b = (badge("Citosol") +
         blob(150, 170, "k-dhf", "DHF", "dihidrofolato", mood="flat") +
         N(enzyme(390, 90, "DHFR", "dihidrofolato reductasa"), .2, 0, -30) +
         N(blob(390, 300, "k-nadph", "NADPH"), .4, 0, 40) +
         N(arrow(200, 170, 560, 170), .6) +
         N(blob(640, 170, "k-thf", "THF", "listo para cargar"), 1.1, -40) +
         N(stop(290, 220, "metotrexato y aminopterina|la bloquean"), 1.8))
    F.append((svg(b, "DHFR"), "5. DHFR recupera el THF",
              "La <b>DHFR</b> (dihidrofolato reductasa) usa NADPH para volver de DHF a <b>THF</b>. El <b>metotrexato</b> y la aminopterina la bloquean."))
    # 6 ciclo
    cxx, cyy, rr = 400, 200, 120
    def at(a): return cxx + rr * math.cos(math.radians(a)), cyy + rr * math.sin(math.radians(a))
    p1, p2, p3 = at(-90), at(30), at(150)
    b = ("<circle cx='400' cy='200' r='120' class='cyc'/>" +
         N(blob(*p1, "k-thf", None, r=22) + T(p1[0], p1[1] - 32, "metilen-THF", "lab"), 0) +
         N(blob(*p2, "k-dhf", None, r=22, mood="flat") + T(p2[0] + 30, p2[1] + 5, "DHF", "lab", "start"), .3) +
         N(blob(*p3, "k-thf", None, r=22) + T(p3[0] - 30, p3[1] + 5, "THF", "lab", "end"), .6) +
         N(note(560, 92, "timidilato sintasa", "enz-n", "start") + note(560, 110, "dUMP → dTMP", "lab2", "start") +
           stop(560, 135, "5-FU"), .9) +
         N(note(400, 345, "DHFR (+ NADPH)", "enz-n") + stop(330, 368, "metotrexato"), 1.2) +
         N(note(240, 92, "serina → glicina", "enz-n", "end") + note(240, 110, "recarga el carbono", "lab2", "end"), 1.5) +
         N(note(400, 196, "sin dTMP|no hay ADN nuevo", "lab"), 1.9))
    F.append((svg(b, "Ciclo"), "6. El ciclo completo (y por qué sirve contra el cáncer)",
              "Metilen-THF → DHF → THF → metilen-THF. Las células que se dividen rápido necesitan mucho dTMP: frenar la timidilato sintasa (5-FU) o la DHFR (metotrexato) frena la división."))
    # 7 sulfonamidas
    b = (N(T(200, 50, "BACTERIA", "lab") + "<rect x='60' y='70' width='280' height='230' rx='70' class='bact'/>" +
           small(130, 150, "PABA", "k-sm", 26) + N(arrow(160, 150, 240, 150), .2) + blob(285, 150, "k-thf", "folato", None, r=22) +
           note(200, 240, "la bacteria FABRICA|su folato desde PABA", "lab2"), 0) +
         N(stop(180, 105, "sulfonamidas:", "start") + note(198, 122, "compiten con PABA", "lab2", "start"), .8) +
         N(T(600, 50, "NOSOTROS", "lab") + "<rect x='460' y='70' width='280' height='230' rx='40' class='cell'/>" +
           note(600, 120, "no fabricamos folato:", "lab") + note(600, 150, "lo comemos (vitamina B9)", "lab2") +
           blob(600, 220, "k-thf", None, r=24), 1.2) +
         N(note(400, 345, "por eso las sulfonamidas frenan a la bacteria y no a nosotros", "lab"), 1.8))
    F.append((svg(b, "Sulfonamidas"), "7. Sulfonamidas: ¿por qué solo a las bacterias?",
              "Las bacterias fabrican su folato a partir de PABA y las <b>sulfonamidas</b> compiten con el PABA. Nosotros comemos el folato, así que no nos afectan."))
    return F

# ================================================================ 5. DEGRADACIÓN, GOTA Y RESCATE
def dg_frames():
    F = []
    # 1 origen
    b = (badge("Intestino y todas las células") +
         N(T(130, 70, "dieta", "lab") + note(130, 92, "carnes rojas, vísceras,|mariscos: muchas purinas", "lab2"), 0) +
         N(T(130, 200, "recambio", "lab") + note(130, 222, "células que mueren|y ARN que se rompe", "lab2"), .3) +
         N(path("M260 120 C330 120 330 170 380 170", "arr") + path("M260 220 C330 220 330 180 380 180", "arr"), .6) +
         N(path("M400 175 C420 150 440 200 460 175 C480 150 500 200 520 175", "s-dna-t"), .8) +
         N("<g class='sci'><circle cx='470' cy='120' r='12'/><circle cx='490' cy='120' r='12'/>"
           "<line x1='470' y1='108' x2='510' y2='60'/><line x1='490' y1='108' x2='450' y2='60'/></g>" + note(480, 50, "nucleasas", "enz-n"), 1) +
         N(arrow(540, 175, 620, 175), 1.3) +
         N(pur_char(690, 140, "k-amp", [("C6", "NH₂")], R=24, rib={"p5": 1}, name="nucleótidos", sub="por ej. AMP"), 1.5, -30))
    F.append((svg(b, "Origen"), "1. ¿De dónde vienen las purinas que se rompen?",
              "De la <b>dieta</b> (carnes rojas, vísceras, mariscos) y del <b>recambio</b> de nuestras propias células. Las nucleasas cortan el ADN y el ARN en nucleótidos."))
    # 2 nucleotidasa
    b = (badge("Citosol") + O(pur_char(170, 140, "k-amp", [("C6", "NH₂")], rib={"p5": 1}, name="AMP"), 1.4, 0, 0, .4) +
         N(pur_char(170, 140, "k-amp", [("C6", "NH₂")], rib={}, name="adenosina", sub="nucleósido (sin P)"), 1.4, 0, 0, .4) +
         N(enzyme(450, 110, "nucleotidasa"), .2, 0, -30) +
         O(f"<g class='ph'><circle cx='{rib_pts(*rib_under(*pur_pos(170,140,34)['N9'],22,22),22)['C4'][0]-24:.1f}' cy='{rib_pts(*rib_under(*pur_pos(170,140,34)['N9'],22,22),22)['C4'][1]-10:.1f}' r='10'/></g>", 1.2, 0, 0, .2) +
         N(small(450, 250, "Pi", "k-sm"), 1.2, -250, 40) + N(note(620, 250, "le saca el fosfato", "lab"), 1.6))
    F.append((svg(b, "Nucleotidasa"), "2. Nucleotidasa: chau fosfato",
              "La <b>nucleotidasa</b> le saca el fosfato al AMP (sale Pi) y queda la <b>adenosina</b>, que es un nucleósido."))
    # 3 adenosina desaminasa
    b = (badge("Citosol") + O(pur_char(170, 140, "k-amp", [("C6", "NH₂")], rib={}, name="adenosina"), 1.4, 0, 0, .4) +
         N(pur_char(170, 140, "k-imp", [("C6", "O")], rib={}, name="inosina", sub="base: hipoxantina"), 1.4, 0, 0, .4) +
         N(enzyme(450, 110, "adenosina|desaminasa"), .2, 0, -30) + N(small(450, 260, "NH₃", "k-sm"), 1.2, -260, -100) +
         N(note(620, 250, "le saca el grupo amino|(NH₂ → O)", "lab"), 1.6))
    F.append((svg(b, "ADA"), "3. Adenosina desaminasa",
              "La <b>adenosina desaminasa</b> le saca el grupo amino (sale NH₃): la adenosina pasa a <b>inosina</b>, con hipoxantina como base."))
    # 4 nucleósido fosforilasa
    b = (badge("Citosol") + O(pur_char(170, 140, "k-imp", [("C6", "O")], rib={}, name="inosina"), 1.2, 0, 0, .4) +
         N(pur_char(170, 140, "k-imp", [("C6", "O")], name="hipoxantina", sub="base libre"), 1.2, 0, 0, .4) +
         N(ribose(450, 290) + note(450, 335, "ribosa-1-P (se recicla)", "lab2"), 1.4, -260, -60) +
         N(enzyme(450, 100, "nucleósido|fosforilasa"), .2, 0, -30) + N(small(330, 50, "Pi", "k-sm"), .4, 0, -30) +
         N(note(640, 210, "separa la base|del azúcar", "lab"), 1.6))
    F.append((svg(b, "Fosforilasa"), "4. Se separa la base",
              "La <b>nucleósido fosforilasa</b> usa un fosfato para separar la base del azúcar: queda la <b>hipoxantina</b> libre y una ribosa-1-P."))
    # 5 xantina oxidasa (1)
    b = (badge("Sobre todo en el hígado") +
         pur_char(130, 150, "k-imp", [("C6", "O")], R=30, name="hipoxantina") +
         N(enzyme(320, 90, "xantina oxidasa"), .2, 0, -30) + N(arrow(200, 160, 440, 160), .5) +
         N(pur_char(530, 150, "k-xan", [("C6", "O"), ("C2", "O")], R=30, name="xantina", sub="ganó otro O"), 1, -30) +
         N(pur_char(300, 300, "k-gua", [("C6", "O"), ("C2", "NH₂")], R=24, name=None) + T(230, 350, "guanina", "lab", "end") +
           path("M340 300 C420 300 470 260 500 215", "arr") + note(440, 330, "guanina desaminasa", "enz-n", "start"), 1.6))
    F.append((svg(b, "Xantina"), "5. Xantina oxidasa (1): hipoxantina → xantina",
              "La <b>xantina oxidasa</b> le agrega un O a la hipoxantina y queda <b>xantina</b>. La guanina también llega a xantina, por la <b>guanina desaminasa</b>."))
    # 6 xantina oxidasa (2)
    b = (badge("Sobre todo en el hígado") +
         pur_char(150, 150, "k-xan", [("C6", "O"), ("C2", "O")], R=30, name="xantina") +
         N(enzyme(360, 90, "xantina oxidasa"), .2, 0, -30) + N(arrow(230, 160, 470, 160), .5) +
         N(pur_char(560, 150, "k-uri", [("C6", "O"), ("C2", "O"), ("C8", "O")], R=30, name="ácido úrico", sub="3 oxígenos: poco soluble", mood="flat"), 1, -30) +
         N(note(400, 340, "la base fue ganando oxígenos: 1 → 2 → 3", "lab"), 1.5))
    F.append((svg(b, "Ácido úrico"), "6. Xantina oxidasa (2): xantina → ácido úrico",
              "La misma <b>xantina oxidasa</b> agrega otro O y sale el <b>ácido úrico</b> (urato). Es poco soluble en agua."))
    # 7 fin del camino
    b = (pur_char(140, 140, "k-uri", [("C6", "O"), ("C2", "O"), ("C8", "O")], R=28, name="urato", mood="flat") +
         N(enzyme(400, 90, "urato oxidasa", None, "k-off", mood="sad") + "<line x1='370' y1='64' x2='430' y2='116' class='nox'/><line x1='430' y1='64' x2='370' y2='116' class='nox'/>" +
           note(400, 165, "los humanos NO la tenemos", "lab"), .3) +
         N(note(640, 90, "otros mamíferos:|urato → alantoína (soluble)", "lab2"), .8) +
         N(path("M150 230 C150 300 300 320 380 320", "arr") + note(470, 300, "sangre → riñón → orina", "lab"), 1.3))
    F.append((svg(b, "Fin"), "7. En humanos, el camino termina en el urato",
              "Los humanos no tenemos <b>urato oxidasa</b>, la enzima que en otros mamíferos lo pasa a alantoína, que es soluble. El urato viaja por la sangre y se elimina por el <b>riñón</b>."))
    # 8 gota
    toe = ("<path d='M240 300 C240 220 300 180 380 190 C470 200 520 230 560 250 C600 270 600 320 560 330 L260 330 C245 330 240 320 240 300Z' class='toe'/>"
           "<circle cx='510' cy='270' r='40' class='joint'/>")
    xt = "".join(f"<line x1='{490+dx}' y1='{255+dy}' x2='{502+dx}' y2='{245+dy}' class='xtal'/>" for dx, dy in ((0, 0), (14, 6), (6, 18), (22, 20), (-4, 26), (16, 32)))
    b = (badge("Articulaciones (típico: dedo gordo del pie)") + toe +
         N(xt + note(510, 345, "cristales en la articulación", "lab2"), .5) + N(P("<circle cx='510' cy='270' r='48' class='hlc'/>"), 1) +
         N(note(560, 90, "si hay demasiado urato|precipita como cristales|de urato monosódico", "lab", "start"), .8) +
         N(note(130, 110, "causa más frecuente:|el riñón elimina poco", "lab2"), 1.3) +
         N(note(130, 160, "Carlos V tenía gota", "lab2"), 1.6))
    F.append((svg(b, "Gota"), "8. Gota",
              "Si se acumula urato (lo más común es que el riñón elimine poco), precipita como <b>cristales de urato monosódico</b> en las articulaciones y las inflama: es la <b>gota</b>."))
    # 9 alopurinol
    b = (badge("Hígado") +
         N(pur_char(130, 140, "k-alo", [("C6", "O")], R=28, name="alopurinol", sub="se parece a la hipoxantina", look=1), 0, -40) +
         N(enzyme(380, 120, "xantina oxidasa", None, "k-enz", mood="o"), .3) +
         N(arrow(200, 140, 330, 130), .6) + N(stop(380, 200, "queda bloqueada", "start"), 1.2) +
         N(note(600, 90, "inhibidor suicida", "lab"), 1.4) +
         N(note(600, 170, "se forma menos urato y se|acumulan hipoxantina y xantina,|que son más solubles", "lab2"), 1.8))
    F.append((svg(b, "Alopurinol"), "9. Alopurinol",
              "El <b>alopurinol</b> se parece a la hipoxantina. La xantina oxidasa lo agarra y queda bloqueada (<b>inhibidor suicida</b>). Se forma menos urato y salen hipoxantina y xantina, que son más solubles."))
    # 10 rescate
    b = (badge("Citosol") +
         pur_char(110, 120, "k-imp", [("C6", "O")], R=26, name="hipoxantina|o guanina") +
         N(ribose(280, 120, p5=1, pp1=True) + T(280, 165, "PRPP", "lab"), .2, 0, -30) +
         N(enzyme(420, 70, "HGPRT"), .4, 0, -30) + N(arrow(330, 130, 520, 130), .6) +
         N(pur_char(600, 92, "k-imp", [("C6", "O")], R=24, rib={}) + T(690, 120, "IMP o GMP", "lab", "start"), 1, -30) +
         N(pur_char(110, 280, "k-amp", [("C6", "NH₂")], R=24, name="adenina") + ribose(280, 290, p5=1, pp1=True) +
           enzyme(420, 270, "APRT") + arrow(330, 290, 540, 290) + pur_char(600, 262, "k-amp", [("C6", "NH₂")], R=22, rib={"p5": 1}) + T(690, 300, "AMP", "lab", "start"), 1.5) +
         N(note(400, 380, "reciclar es mucho más barato que fabricar de cero", "lab"), 2))
    F.append((svg(b, "Rescate"), "10. Rescate: reciclar bases",
              "En vez de romper la base, se le vuelve a pegar un PRPP. <b>HGPRT</b>: hipoxantina → IMP y guanina → GMP. <b>APRT</b>: adenina → AMP. Sale mucho más barato que fabricarla de cero."))
    return F

# ---------------------------------------------------------------- inserción
if __name__ == "__main__":
    s = open("t_n.html").read()
    s = re.sub(r"<!--ANIM:(m\w+)-->.*?<!--/ANIM:\1-->\n?", "", s, flags=re.S)
    i = s.index("<h2>5. Metabolismo de nucleótidos</h2>")
    k = s.index("porque los fabricamos.", i); k = s.index("</p>", k) + 4
    s = s[:k] + "\n" + player("mmap", "Dónde pasa y de dónde sale cada ingrediente", map_frames()) + s[k:]
    for anchor, key, title, fn in [("<h3>Desoxirribonucleótidos y timidilato</h3>", "mpur", "Síntesis de purinas", pur_frames),
                                   ("<h3>Desoxirribonucleótidos y timidilato</h3>", "mpyr", "Síntesis de pirimidinas", pyr_frames),
                                   ("<h3>Degradación de purinas y gota</h3>", "mdx", "Desoxirribonucleótidos y timidilato", dx_frames),
                                   ("<h3>Nucleótidos dentro de coenzimas</h3>", "mdg", "Degradación, gota y rescate", dg_frames)]:
        assert s.count(anchor) == 1, anchor
        s = s.replace(anchor, player(key, title, fn()) + anchor)
    open("t_n.html", "w").write(s)
    print("ok", [len(f()) for f in (map_frames, pur_frames, pyr_frames, dx_frames, dg_frames)])
