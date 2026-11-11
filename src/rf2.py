# Repaso de falladas v2: teoría filtrada (solo temas fallados), con dibujos y videos. Genera t_rf.html.
import json, math, re
from anim import N, O, P, T, L, path, arrow, player
from metab import blob, small, enzyme, note, pur_char, pyr_char, face, battery, stop, ribose
from story import say as _say, frame, D, helix, scissors
def say(x, y, text, to, d=0.4, cls="bub"):
    w = max(len(l) for l in text.split("|")) * 7.5 + 26
    x = max(8, min(x, 792 - w))
    return _say(x, y, text, to, d, cls)
from rf import fig, figs, fig_shapes, fig_periodato

MOLS = json.load(open("mol.json"))

def mol(i, x, y, w):
    s = MOLS[i]["svg"]
    head, rest = s.split(">", 1)
    vb = re.search(r"viewBox='([^']*)'", head).group(1)
    _, _, vw, vh = map(float, vb.split())
    h = w * vh / vw
    head = re.sub(r"\s(width|height)='[^']*'", "", head)
    head = head.replace("<svg", f"<svg x='{x}' y='{y}' width='{w}' height='{h:.0f}'", 1)
    return head + ">" + rest

def hl(x, y, r=16): return P(f"<circle cx='{x}' cy='{y}' r='{r}' class='hlc'/>")
def lab(x, y, t, c="lab", a="middle"): return T(x, y, t, c, a)
def truco(t): return f'<div class="box why"><b>Para recordar.</b> {t}</div>'
def ojo(t): return f'<div class="box trap"><b>Ojo</b> {t}</div>'
def practice(topics, label): return f'<p><button class="go" type="button" data-practice="{topics}" data-mode="wrong">{label}</button></p>'
def vid(key, title, frames): return player(key, title, frames)

# ================================================================ dibujos estáticos
CH = {"L": (0, 20), "LL": (40, 35), "LR": (90, 25), "R": (130, 8), "UR": (90, -7), "UL": (40, 3)}
UP = {"R": 1, "UR": -1, "UL": 1, "L": -1, "LL": 1, "LR": -1}   # 1 = átomo arriba (axial hacia arriba)

def chair(x0, y0, subs, title, s=1.6):
    """subs: {pos: (label, 'eq'|'ax', cls)}"""
    P_ = {k: (x0 + v[0] * s, y0 + v[1] * s) for k, v in CH.items()}
    order = ["L", "LL", "LR", "R", "UR", "UL"]
    o = "".join(L(*P_[order[i]], *P_[order[(i + 1) % 6]], "rbond") for i in range(6))
    o += T(P_["UR"][0] + 2, P_["UR"][1] - 8, "O", "lab")
    cx = sum(p[0] for p in P_.values()) / 6; cy = sum(p[1] for p in P_.values()) / 6
    for k, (t, kind, cls) in subs.items():
        x, y = P_[k]
        if kind == "ax":
            ex, ey = x, y - 34 * UP[k]
        else:
            dx, dy = x - cx, y - cy; n = math.hypot(dx, dy)
            ex, ey = x + dx / n * 32, y + dy / n * 32 + 8 * UP[k]
        o += L(x, y, ex, ey, "bond") + T(round(ex + (8 if ex > x + 3 else -8 if ex < x - 3 else 0)), round(ey + (12 if ey > y else -4)), t, cls, "start" if ex > x + 3 else "end" if ex < x - 3 else "middle")
    o += T(x0 + 65 * s, y0 + 128, title, "lab")
    return o

def fig_chairs():
    glc = {"R": ("OH", "eq", "eqt"), "LR": ("OH", "eq", "eqt"), "LL": ("OH", "eq", "eqt"), "L": ("OH", "eq", "eqt"), "UL": ("CH₂OH", "eq", "eqt")}
    man = dict(glc); man["LR"] = ("OH", "ax", "axt")
    o = chair(70, 90, glc, "β-D-glucosa: TODO ecuatorial") + chair(470, 90, man, "β-D-manosa: OH del C2 axial")
    o += T(400, 30, "silla: ecuatorial = hacia afuera (cómodo) · axial = vertical (choca)", "lab2")
    o += T(574, 245, "(ese OH axial choca con los H axiales del mismo lado)", "stp-t")
    return fig(o, 260, "Sillas")

def fig_brush():
    o = [L(80, 150, 720, 150, "core")]
    for i, x in enumerate(range(110, 700, 60)):
        h = 70 + (i % 3) * 12
        o.append(path(f"M{x} 150 L{x-10} {150-h}", "gag") + path(f"M{x+20} 150 L{x+30} {150+h-20}", "gag2" if i % 2 else "gag"))
    o.append(T(400, 245, "↑ proteína central (core): el palo", "lab") + T(400, 30, "cadenas de GAG unidas covalentemente (condroitín y queratán sulfato)", "lab2"))
    o.append(T(400, 280, "Proteoglicano = «cepillo»: la proteína es el palo y los GAG son las cerdas. Es más azúcar que proteína.", "lab"))
    return fig("".join(o), 300, "Proteoglicano")

def fig_gag_tree():
    def box(x, y, t, cls="nd"):
        w = 18 + len(t) * 7.6
        return f"<rect x='{x-w/2:.0f}' y='{y-17}' width='{w:.0f}' height='34' rx='10' class='{cls}'/>" + T(x, y + 5, t, "lab")
    o = [box(400, 30, "¿Qué ácido urónico tiene?"),
         arrow(330, 48, 140, 98) + arrow(400, 48, 400, 98) + arrow(470, 48, 660, 98),
         T(215, 68, "ninguno", "lab2") + T(415, 78, "GlcA", "lab2", "start") + T(585, 68, "IdoA", "lab2"),
         box(140, 120, "QUERATÁN sulfato", "nd hot") + T(140, 155, "(tiene Gal + GlcNAc)", "lab2"),
         box(400, 120, "¿Qué aminoazúcar?"), arrow(360, 138, 290, 190) + arrow(440, 138, 510, 190),
         T(300, 165, "GlcNAc", "lab2", "end") + T(500, 165, "GalNAc", "lab2", "start"),
         box(270, 210, "HIALURONANO", "nd hot") + T(270, 245, "sin sulfato · sin core", "lab2"),
         box(530, 210, "CONDROITÍN sulfato", "nd hot"),
         box(660, 120, "DERMATÁN sulfato", "nd hot") + T(660, 155, "(IdoA + GalNAc)", "lab2"),
         T(400, 290, "(La heparina también tiene IdoA, pero con GlcNS y muchísimo sulfato.)", "lab2")]
    return fig("".join(o), 305, "Árbol para reconocer GAG")

def fig_rna_alk():
    o = [T(400, 26, "Por qué el ARN se rompe en álcali y el ADN no", "lab")]
    o.append(f"<polygon points='150,90 185,115 172,155 128,155 115,115' class='rib'/>" + T(150, 130, "ribosa", "rib-t"))
    o.append(L(172, 155, 190, 185, "bond") + T(198, 198, "2′-OH", "stp-t", "start"))
    o.append(L(128, 155, 115, 190, "bond") + T(110, 205, "3′-O", "lab2", "end") + L(115, 205, 150, 240, "bond"))
    o.append("<g class='ph'><circle cx='165' cy='250' r='14'/></g>" + T(165, 255, "P", "ph-t"))
    o.append(path("M205 205 C230 230 210 250 182 250", "arr") + "<polygon points='182,250 194,243 193,256' class='arrh'/>")
    o.append(T(250, 225, "el 2′-OH (en álcali, O⁻) ataca", "lab2", "start") + T(250, 241, "al fósforo vecino → se corta la cadena", "lab2", "start") + T(250, 257, "(queda un fosfato cíclico 2′,3′)", "lab2", "start"))
    o.append(f"<polygon points='620,90 655,115 642,155 598,155 585,115' class='rib'/>" + T(620, 130, "desoxirribosa", "rib-t"))
    o.append(L(642, 155, 660, 185, "bond") + T(668, 198, "2′-H", "lab", "start") + T(620, 230, "sin OH en el 2′:", "lab") + T(620, 248, "nadie ataca → el ADN resiste", "lab2"))
    return fig("".join(o), 275, "ARN y álcali")

# ================================================================ VIDEOS
def v_anillo():
    F = []
    b = (mol("f_dglucosa", 60, 30, 190) + hl(155, 70, 18) + hl(170, 255, 20) +
         lab(155, 30, "C1 (carbonilo)", "lab2") + lab(170, 322, "OH del C5", "lab2") +
         say(330, 60, "Mi OH del C5 ataca al C1 (el carbonilo)…|y me cierro en un anillo de 6.", (190, 250), D(0)) +
         N(arrow(300, 210, 450, 210) + mol("h_bglc", 470, 120, 280), D(1)) +
         say(480, 300, "El C1 queda como carbono ANOMÉRICO:|su OH nuevo puede quedar arriba o abajo.", (690, 200), D(1) + .5))
    F.append(frame(b, "Cierre", "El anillo se cierra", "En agua, la glucosa se cierra sola: el <b>OH del C5</b> ataca al <b>C1</b> (el carbonilo) y se forma un anillo de 6 (piranosa). El C1 pasa a ser el <b>carbono anomérico</b>, con un OH nuevo.", 2))
    b = (mol("h_aglc", 40, 70, 300) + mol("h_bglc", 440, 70, 300) +
         lab(190, 32, "α-D-glucosa", "sg-t") + lab(590, 32, "β-D-glucosa", "sg-t") +
         hl(274, 210, 20) + hl(674, 120, 20) + hl(148, 82, 26) + hl(548, 82, 26) +
         say(40, 300, "α: el OH del C1 queda ABAJO,|del lado opuesto al CH₂OH.", (270, 220), D(0)) +
         say(440, 300, "β: el OH del C1 queda ARRIBA,|del mismo lado que el CH₂OH.", (670, 135), D(1)))
    F.append(frame(b, "Alfa y beta", "α y β en Haworth", "En una D-hexosa el <b>CH₂OH va arriba</b>. <b>α</b>: el OH anomérico queda del lado <b>opuesto</b> (abajo). <b>β</b>: del <b>mismo lado</b> (arriba).", 2))
    glc = {"R": ("OH", "eq", "eqt"), "LR": ("OH", "eq", "eqt"), "LL": ("OH", "eq", "eqt"), "L": ("OH", "eq", "eqt"), "UL": ("CH₂OH", "eq", "eqt")}
    man = dict(glc); man["LR"] = ("OH", "ax", "axt")
    b = (T(400, 30, "Pero el anillo no es plano: es una SILLA", "lab") + chair(70, 110, glc, "β-D-glucosa") + N(chair(470, 110, man, "β-D-manosa"), D(1) - .4) +
         say(60, 300, "Tengo TODO ecuatorial (hacia afuera):|nada choca. Soy la más estable.", (180, 250), D(0)) +
         say(470, 300, "Soy la glucosa con el C2 al revés:|mi OH del C2 queda AXIAL y choca.", (560, 250), D(1)))
    F.append(frame(b, "Silla", "La silla: ecuatorial vs axial", "En la silla, cada sustituyente queda <b>ecuatorial</b> (hacia afuera, cómodo) o <b>axial</b> (vertical, choca). La β-D-glucosa tiene <b>todo ecuatorial</b>. La β-D-manosa es su epímero en C2, así que ese OH queda <b>axial</b>: es menos estable.", 2))
    b = (mol("f_dmanosa", 40, 40, 170) + mol("f_dglucosa", 315, 40, 170) + mol("f_dgalactosa", 590, 40, 170) +
         lab(125, 30, "D-manosa", "sg-t") + lab(400, 30, "D-glucosa", "sg-t") + lab(675, 30, "D-galactosa", "sg-t") +
         N(f"<rect x='45' y='{40+71*170/170-14:.0f}' width='160' height='26' rx='8' class='hlbox'/>" + f"<rect x='320' y='{40+71-14}' width='160' height='26' rx='8' class='hlbox'/>", .4) +
         N(f"<rect x='320' y='{40+151-14}' width='160' height='26' rx='8' class='hlbox2'/>" + f"<rect x='595' y='{40+151-14}' width='160' height='26' rx='8' class='hlbox2'/>", D(1) - .3) +
         say(215, 300, "Manosa: cambia el C2.", (200, 112), D(0)) +
         say(470, 320, "Galactosa: cambia el C4.", (600, 192), D(1)))
    F.append(frame(b, "Epímeros", "Epímeros: buscá el único OH que cambia", "<b>Epímeros</b> = iguales salvo en <b>un</b> carbono. Con la glucosa como referencia: la <b>manosa</b> cambia en el <b>C2</b> y la <b>galactosa</b> en el <b>C4</b>. Manosa y galactosa entre sí no son epímeros, porque difieren en dos carbonos.", 2))
    return F

def v_activado():
    F = []
    hexg = lambda x, y, k="glcx": f"<polygon points='{x},{y-24} {x+21},{y-12} {x+21},{y+12} {x},{y+24} {x-21},{y+12} {x-21},{y-12}' class='{k}'/>"
    udp = lambda x, y: f"<rect x='{x}' y='{y-14}' width='70' height='28' rx='10' class='udp'/>" + T(x + 35, y + 5, "UDP", "lab")
    b = (hexg(120, 200) + face(120, 198, .7) + lab(120, 250, "glucosa-1-P") + blob(330, 200, "k-imp", "UTP", r=24) +
         say(30, 60, "Sola no me puedo unir a nada:|me falta energía.", (120, 175), D(0)) +
         say(290, 80, "Te activo: te pego a un UDP.", (330, 175), D(1)) +
         N(arrow(380, 200, 470, 200) + hexg(530, 200) + face(530, 198, .7) + udp(552, 200) + lab(560, 255, "UDP-glucosa") + small(500, 320, "PPi", "k-sm"), D(2) - .3) +
         say(580, 90, "¡Ahora estoy ACTIVADA!", (520, 175), D(2)))
    F.append(frame(b, "Activación", "Activar un azúcar", "Para unir un azúcar a otra molécula hace falta energía. La célula primero lo <b>activa</b>: glucosa-1-P + UTP → <b>UDP-glucosa</b> + PPi. Un azúcar pegado a un nucleótido es un <b>azúcar nucleotídico</b>.", 3))
    chain = "".join(hexg(470 + 46 * i, 260, "glcx") + (L(491 + 46 * i, 260, 495 + 46 * i, 260, "bond") if i < 4 else "") for i in range(4))
    b = (hexg(130, 140) + face(130, 138, .7) + udp(152, 140) + lab(170, 190, "UDP-glucosa") + chain + lab(560, 310, "cadena que crece (glucógeno)") +
         enzyme(400, 130, "glicosiltransferasa") +
         say(450, 30, "Tomo la glucosa del UDP-glucosa|y se la paso a la cadena.", (420, 110), D(0)) +
         N(hexg(654, 260) + face(654, 258, .55), D(1) - .3, -400, -120, 1) +
         O(hexg(130, 140) + face(130, 138, .7), D(1) - .3, 400, 120, 1) +
         say(60, 230, "Y yo, el UDP, quedo libre.", (180, 150), D(1)))
    F.append(frame(b, "Glicosiltransferasa", "Las glicosiltransferasas usan el azúcar activado", "Las <b>glicosiltransferasas</b> usan el azúcar nucleotídico como <b>dador</b>: pasan el azúcar al aceptor y sueltan el UDP. Así se arma el glucógeno y se agregan los azúcares de las glicoproteínas.", 2))
    b = (hexg(140, 180) + face(140, 178, .7) + lab(140, 230, "glucosa") + blob(420, 190, "k-amp", "hemoglobina", r=34) +
         say(40, 40, "Me pego a la proteína SOLA,|sin ninguna enzima.", (140, 155), D(0)) +
         N(arrow(470, 190, 560, 190) + blob(640, 190, "k-amp", "HbA1c", "glucosa pegada", r=34) + hexg(675, 158) , D(1) - .3) +
         say(470, 300, "Me miden para saber la glucosa|de los últimos 2–3 meses.", (630, 245), D(1)) +
         N(note(400, 385, "En la cocina, la misma química se llama MAILLARD (el dorado del pan).", "lab"), D(2)))
    F.append(frame(b, "Glicación", "Glicación = Maillard: sin enzimas", "El carbonilo de un azúcar reductor reacciona con un grupo amino de una proteína, <b>sin enzimas</b>. En el cuerpo se llama <b>glicación</b> (así se forma la <b>HbA1c</b>); en la cocina, <b>reacción de Maillard</b>. Es la misma química.", 2))
    return F

def v_reconocer():
    F = []
    def leuk(x, y):
        o = f"<circle cx='{x}' cy='{y}' r='42' class='leuk'/>" + face(x, y - 4, 1.1)
        for a in range(0, 360, 45):
            r = math.radians(a); px, py = x + 42 * math.cos(r), y + 42 * math.sin(r)
            o += f"<line x1='{px:.1f}' y1='{py:.1f}' x2='{px+8*math.cos(r):.1f}' y2='{py+8*math.sin(r):.1f}' class='slx'/><circle cx='{px+11*math.cos(r):.1f}' cy='{py+11*math.sin(r):.1f}' r='4' class='slxd'/>"
        return o
    endo = "<rect x='20' y='300' width='760' height='40' rx='8' class='endo'/>" + "".join(f"<path d='M{x} 300 l0 -16 m-6 0 l12 0' class='sel'/>" for x in range(60, 760, 50)) + T(400, 362, "endotelio (pared del vaso) con SELECTINAS", "lab")
    b = (endo + N(leuk(140, 240), 0, -100, 0, 1.2) + N(leuk(400, 240), 1.6, -150, 0, 1.4) +
         say(480, 40, "¡Te agarro el sialyl-Lewis X!|…y te suelto. Y te vuelvo a agarrar.", (420, 285), D(0) + .4) +
         say(40, 40, "Me frenás, me suelto…|voy RODANDO.", (140, 200), D(1) + .6))
    F.append(frame(b, "Rolling", "Selectinas: los leucocitos ruedan", "En la inflamación, el endotelio expone <b>selectinas</b>, proteínas que reconocen azúcares (lectinas). Agarran el glicano <b>sialyl-Lewis X</b> de los leucocitos con uniones débiles que se arman y se sueltan: el leucocito <b>rueda</b>, frena y después sale del vaso.", 2))
    def virus(x, y):
        o = f"<circle cx='{x}' cy='{y}' r='30' class='vir'/>" + face(x, y - 2, .9)
        for a in range(0, 360, 40):
            r = math.radians(a)
            o += f"<line x1='{x+30*math.cos(r):.1f}' y1='{y+30*math.sin(r):.1f}' x2='{x+42*math.cos(r):.1f}' y2='{y+42*math.sin(r):.1f}' class='{'ha' if a % 80 == 0 else 'na'}'/>"
        return o
    cellm = "<rect x='20' y='310' width='760' height='70' rx='10' class='cellm'/>" + "".join(f"<path d='M{x} 310 l0 -14' class='sia'/><circle cx='{x}' cy='292' r='5' class='siad'/>" for x in range(50, 770, 40)) + T(400, 360, "célula con ÁCIDO SIÁLICO en su superficie", "lab")
    b = (cellm + N(virus(250, 240), 0, 0, -120, 1) +
         say(330, 60, "Mi HEMAGLUTININA se engancha|al ácido siálico: así entro.", (270, 215), D(0)))
    F.append(frame(b, "Entrar", "Influenza (1): la hemaglutinina engancha", "El virus de la influenza tiene dos proteínas en su superficie. La <b>hemaglutinina</b> se une al <b>ácido siálico</b> de la célula y así el virus entra.", 1))
    b = (cellm + virus(200, 250) + virus(420, 250) + virus(640, 250) +
         say(40, 40, "Salimos de la célula… ¡pero quedamos|pegados al ácido siálico!", (200, 215), D(0)) +
         N(scissors(560, 140), D(1) - .3) + say(600, 40, "Soy la NEURAMINIDASA:|corto el ácido siálico.", (575, 110), D(1)) +
         O(virus(200, 250) + virus(420, 250) + virus(640, 250), D(2), 0, -160, 1.4) +
         N(stop(250, 150, "oseltamivir (Tamiflu)|bloquea la neuraminidasa", "start"), D(2) + .8))
    F.append(frame(b, "Salir", "Influenza (2): la neuraminidasa libera", "Los virus nuevos quedarían pegados al ácido siálico de la célula. La <b>neuraminidasa</b> lo corta y <b>libera</b> los virus. El oseltamivir (Tamiflu) la bloquea.", 2))
    ecoli = "<rect x='60' y='120' width='220' height='110' rx='55' class='bact'/>" + face(170, 170, 1.1) + "".join(f"<path d='M{x} 120 l0 -18' class='lps'/>" for x in range(90, 260, 20)) + T(170, 260, "E. coli (gram negativa)", "lab") + T(170, 90, "LPS en la membrana externa", "lab2")
    b = (ecoli + N(arrow(300, 175, 420, 175) + "<path d='M450 110 L450 240 Q480 270 510 240 L510 110' class='tube'/>" + T(480, 280, "proteína purificada", "lab"), .3) +
         say(530, 50, "Me purificaste, pero vengo|con LPS pegado…", (500, 150), D(0) + .5) +
         N(blob(660, 230, "k-amp", "paciente", r=26, mood="sad"), D(1) - .3) +
         say(330, 300, "¡Fiebre e inflamación!|(el LPS es una endotoxina)", (640, 240), D(1) + .2))
    F.append(frame(b, "LPS", "LPS: la endotoxina de E. coli", "El <b>LPS</b> (lipopolisacárido) está en la membrana externa de las bacterias gram negativas, como <i>E. coli</i>. Si queda pegado a una proteína producida en ella, al inyectarla causa <b>fiebre e inflamación</b>: hay que sacarlo.", 2))
    return F

def tube(x, y, w=70, h=170, liquid="liq"):
    return (f"<path d='M{x} {y} L{x} {y+h} Q{x+w/2} {y+h+30} {x+w} {y+h} L{x+w} {y}' class='tube'/>"
            f"<path d='M{x+1} {y+30} L{x+1} {y+h} Q{x+w/2} {y+h+29} {x+w-1} {y+h} L{x+w-1} {y+30}Z' class='{liquid}'/>")
def prot(x, y): return f"<circle cx='{x}' cy='{y}' r='7' class='protd'/>"
def poly(x, y): return path(f"M{x} {y} q6 -8 12 0 q6 8 12 0 q6 -8 12 0", "polyd")
def salt(x, y): return f"<circle cx='{x}' cy='{y}' r='2.6' class='saltd'/>"

def v_aislar():
    F = []
    mix = "".join(prot(x, y) for x, y in ((120, 120), (150, 160), (110, 200), (140, 230))) + "".join(poly(x, y) for x, y in ((105, 140), (120, 185), (110, 250))) + "".join(salt(x, y) for x, y in ((160, 130), (100, 170), (160, 200), (130, 215), (150, 255), (115, 105)))
    leg = (prot(560, 120) + lab(575, 125, "proteínas", "lab2", "start") + poly(552, 150) + lab(595, 155, "polisacáridos", "lab2", "start") + salt(560, 180) + lab(575, 185, "sales y azúcares chicos", "lab2", "start"))
    b = (tube(95, 80) + mix + leg + lab(130, 300, "extracto vegetal") +
         say(250, 60, "Estamos todos mezclados.|Hay que ir sacando de a uno.", (175, 150), D(0)))
    F.append(frame(b, "Extracto", "El punto de partida", "Un extracto tiene <b>proteínas</b>, <b>polisacáridos</b> y <b>sales</b> mezclados. La idea es sacar lo que molesta de a una cosa por vez.", 1))
    b = (tube(95, 80) + "".join(poly(x, y) for x, y in ((105, 140), (120, 185), (110, 230))) + "".join(salt(x, y) for x, y in ((160, 130), (100, 170), (160, 200), (130, 215))) +
         N("".join(prot(x, 262 + (i % 2) * 6) for i, x in enumerate(range(112, 160, 12))), .6, 0, -120, 1.2) +
         small(300, 110, "TCA", "k-sm", 26) + say(340, 40, "Soy el TCA (ácido tricloroacético):|¡las proteínas al fondo!", (310, 90), D(0)) +
         say(320, 250, "Centrifugo y me quedo con el líquido:|ahí siguen los polisacáridos.", (165, 200), D(1)) + leg)
    F.append(frame(b, "TCA", "1) TCA: chau proteínas", "El <b>TCA</b> precipita las proteínas. Se centrifuga, se <b>descarta el precipitado</b> y se sigue con el sobrenadante.", 2))
    b = (tube(95, 80) + "".join(salt(x, y) for x, y in ((160, 130), (100, 170), (160, 200), (130, 215))) +
         N("".join(poly(x, 262 + (i % 2) * 5) for i, x in enumerate((100, 122, 138))), .6, 0, -110, 1.2) +
         small(300, 110, "etanol", "k-sm", 26) + say(340, 40, "Con etanol al 80 % los polisacáridos|precipitan; lo chico queda disuelto.", (322, 95), D(0)) +
         say(320, 250, "Ahora me quedo con el PRECIPITADO.", (165, 262), D(1)) + leg)
    F.append(frame(b, "Etanol", "2) Etanol 80 %: precipitan los polisacáridos", "Con <b>etanol al 80 %</b> los polisacáridos (grandes) precipitan y los azúcares chicos quedan disueltos. Ahora sí se guarda el <b>precipitado</b>.", 2))
    bag = "<rect x='90' y='110' width='90' height='150' rx='40' class='bag'/>" + "<rect x='40' y='70' width='190' height='240' rx='20' class='bath'/>"
    b = (bag + "".join(poly(x, y) for x, y in ((105, 160), (110, 200), (105, 235))) +
         N("".join(salt(x, y) for x, y in ((205, 140), (60, 180), (210, 230), (55, 260), (200, 290))), .5) + O("".join(salt(x, y) for x, y in ((150, 140), (120, 180), (150, 230))), .5, 60, 0, 1.2) +
         say(300, 60, "Soy la membrana de DIÁLISIS: tengo poros.|Las sales salen; los polisacáridos no pasan.", (180, 150), D(0)) +
         N(lab(135, 340, "polisacáridos limpios"), D(1)) + leg)
    F.append(frame(b, "Diálisis", "3) Diálisis: chau sales", "En la <b>diálisis</b> la muestra queda dentro de una membrana con poros: las sales y moléculas chicas salen y los polisacáridos quedan adentro. Orden: <b>TCA → etanol 80 % → diálisis</b>.", 1))
    col = "<rect x='80' y='40' width='80' height='250' rx='10' class='col'/>" + "".join(T(95 + (i % 3) * 25, 70 + (i // 3) * 30, "+", "plus") for i in range(21))
    peaks = path("M450 330 L470 330 Q490 330 500 260 Q510 330 530 330 L560 330 Q580 330 590 230 Q600 330 620 330 L650 330 Q670 330 680 190 Q690 330 710 330 L760 330", "peak")
    b = (col + lab(120, 320, "resina con cargas +") +
         say(200, 30, "Soy de INTERCAMBIO ANIÓNICO:|atrapo lo NEGATIVO.", (160, 70), D(0)) +
         N(peaks + L(440, 330, 770, 330, "bond") + lab(500, 355, "0 M") + lab(590, 355, "0,3 M") + lab(680, 355, "0,6 M") + lab(605, 380, "NaCl (sal) creciente", "lab2"), D(1) - .3) +
         say(330, 110, "Neutros: salen sin sal. Cuanto más NEGATIVO,|más fuerte me pego y más sal hace falta.", (680, 200), D(1)) +
         N(T(680, 225, "↑ el más negativo", "stp-t"), D(2)))
    F.append(frame(b, "Intercambio aniónico", "4) Separar por carga", "La resina tiene cargas <b>positivas</b> y retiene lo <b>negativo</b>. La sal compite por la resina: lo neutro sale con 0 M y lo <b>más negativo</b> (más carga por tamaño) necesita <b>más sal</b> para despegarse. Algo positivo ni se pegaría.", 2))
    def lane(x, ys, t):
        return f"<rect x='{x-30}' y='70' width='60' height='250' rx='6' class='gel'/>" + "".join(f"<rect x='{x-24}' y='{y}' width='48' height='7' rx='3' class='band'/>" for y in ys) + lab(x, 345, t)
    b = (lane(250, (100, 140, 170, 215, 260), "pico 1") + N(lane(450, (190,), "pico 3"), .5) +
         say(500, 40, "FACE: cada polisacárido DISTINTO|corre a su altura y da UNA banda.", (290, 120), D(0)) +
         say(500, 230, "5 bandas = 5 polisacáridos.|1 banda = puro.", (470, 195), D(1)))
    F.append(frame(b, "FACE", "5) FACE: ¿está puro?", "En <b>FACE</b> (electroforesis con un fluoróforo) cada especie da <b>una banda</b>. Una fracción con 5 polisacáridos da 5 bandas; una pura, 1.", 2))
    return F

def gp(x, y, glyc_on="Asn"):
    """cadena de proteína con un glicano en árbol"""
    o = path(f"M{x} {y} q30 -20 60 0 q30 20 60 0 q30 -20 60 0 q30 20 60 0", "protchain")
    return o

def tree(x, y, s=1.0, cls="treeg"):
    pts = [(x, y), (x, y - 20 * s), (x - 14 * s, y - 38 * s), (x + 14 * s, y - 38 * s), (x - 22 * s, y - 56 * s), (x + 22 * s, y - 56 * s)]
    o = "".join(L(*pts[a], *pts[b], "bond") for a, b in ((0, 1), (1, 2), (1, 3), (2, 4), (3, 5)))
    o += "".join(f"<rect x='{px-6*s:.1f}' y='{py-6*s:.1f}' width='{12*s:.1f}' height='{12*s:.1f}' class='{cls}'/>" if i < 2 else f"<circle cx='{px:.1f}' cy='{py:.1f}' r='{6*s:.1f}' class='mang'/>" for i, (px, py) in enumerate(pts[1:]))
    return o

def v_glicanos():
    F = []
    b = (gp(120, 260) + T(180, 300, "Asn", "sg-t") + N(tree(180, 255), 0) +
         scissors(300, 180) + lab(300, 238, "PNGasa F", "enz-n") +
         say(360, 40, "Corto el N-glicano entero, justo en la unión|con la Asn… y me llevo el N de su amida.", (320, 150), D(0)) +
         O(tree(180, 255), D(1) - .3, 300, -40, 1.2) +
         N(T(180, 330, "Asn → Asp", "stp-t"), D(1)) + say(380, 300, "Quedé convertida en ácido aspártico.", (210, 300), D(1) + .3))
    F.append(frame(b, "PNGasa F", "Liberar N-glicanos: PNGasa F", "La <b>PNGasa F</b> corta el N-glicano entero en su unión con la <b>asparagina (Asn)</b>. Al hacerlo, la Asn pierde el N de su amida y queda como <b>ácido aspártico (Asp)</b>.", 2))
    b = (gp(80, 220) + T(140, 275, "Ser / Thr", "sg-t") + T(320, 255, "Asn", "sg-t") +
         N(tree(140, 215, .9, "treeo"), 0) + tree(320, 215) +
         "<rect x='640' y='60' width='26' height='220' rx='13' class='thermo'/><circle cx='653' cy='290' r='22' class='thermob'/>" + T(700, 160, "60 °C", "sg-t", "start") +
         small(520, 110, "hidracina", "k-sm", 34) +
         say(360, 20, "No elijo aminoácidos: lo que cambia|es qué unión aguanta el calor.", (520, 85), D(0)) +
         O(tree(140, 215, .9, "treeo"), D(1), -60, -90, 1.2) +
         say(30, 300, "A 60 °C se suelta el O-glicano (Ser/Thr):|su unión es más LÁBIL. El N-glicano necesita más calor.", (215, 175), D(1) + .3))
    F.append(frame(b, "Hidracinólisis", "Hidracinólisis: O vs N", "La <b>hidracinólisis</b> libera glicanos sin enzimas. La unión de los <b>O-glicanos</b> a Ser/Thr es más <b>lábil</b> y se rompe a 60 °C; la de los N-glicanos a Asn es más firme y necesita más temperatura.", 2))
    pac = lambda x, y: f"<path d='M{x} {y} L{x+22} {y-14} A26 26 0 1 0 {x+22} {y+14}Z' class='lectin'/>" + face(x - 8, y - 6, .6)
    b = ("<rect x='60' y='50' width='120' height='260' rx='12' class='col'/>" + pac(130, 140) + pac(130, 230) + lab(120, 335, "columna de Con A") +
         "".join(f"<circle cx='{x}' cy='{y}' r='6' class='mang'/>" for x, y in ((152, 140), (152, 230))) +
         small(330, 110, "NaCl", "k-sm", 26) + say(380, 40, "Yo no la despego: la unión|NO es por cargas.", (350, 90), D(0)) +
         small(330, 270, "", "k-sm", 44) + note(330, 266, "α-metil-|manósido", "at-t") + say(390, 220, "Yo me parezco a la manosa: ocupo el lugar|de la lectina y la glicoproteína se suelta.", (360, 255), D(1)))
    F.append(frame(b, "Con A", "Lectinas: se despegan con un azúcar", "La <b>Con A</b> es una <b>lectina</b> que reconoce <b>manosa</b>. La glicoproteína queda pegada por sus manosas, así que no se despega con sal: se eluye por <b>competencia</b> con un azúcar libre parecido, el <b>α-metilmanósido</b>.", 2))
    b = ("<rect x='90' y='60' width='100' height='200' rx='12' class='pgc'/>" + lab(140, 285, "cartucho PGC") + lab(140, 50, "carbono grafitizado", "lab2") +
         "".join(tree(115 + 25 * i, 200 - 30 * (i % 2), .6) for i in range(3)) +
         N("".join(salt(x, y) for x, y in ((250, 140), (270, 170), (300, 150))) + "".join(f"<polygon points='{x},{y-8} {x+7},{y-4} {x+7},{y+4} {x},{y+8} {x-7},{y+4} {x-7},{y-4}' class='glcx'/>" for x, y in ((260, 210), (300, 230))), .4, -120, 0, 1.2) +
         say(350, 40, "Con AGUA salen las sales y los monosacáridos:|son muy chicos para quedarse.", (300, 160), D(0)) +
         say(350, 250, "Los glicanos (oligosacáridos) quedan retenidos|y salen recién con acetonitrilo.", (190, 180), D(1)))
    F.append(frame(b, "PGC", "Limpiar glicanos con carbono grafitizado", "El <b>PGC</b> retiene los <b>oligosacáridos</b>. El lavado con <b>agua</b> se lleva las <b>sales y los monosacáridos</b>; después los glicanos se eluyen con acetonitrilo.", 2))
    lad = "".join(f"<line x1='{80+60*i}' y1='300' x2='{80+60*i}' y2='{300-12-i*3}' class='ladder'/>" + T(80 + 60 * i, 322, str(i + 1), "lab2") for i in range(11))
    b = (lad + L(60, 300, 760, 300, "bond") + lab(410, 350, "unidades de glucosa (GU): escalera de referencia") +
         path("M440 300 Q450 300 455 210 Q460 300 470 300", "peak") + lab(455, 195, "7,0 GU") +
         N(scissors(540, 120) + lab(540, 178, "exoglicosidasa", "enz-n"), .4) +
         N(path("M380 300 Q390 300 395 210 Q400 300 410 300", "peak2") + lab(390, 195, "≈ 6 GU", "stp-t"), D(1) - .3) +
         say(560, 30, "Le saco el azúcar de la punta.", (560, 95), D(0)) +
         say(60, 40, "Quedé más chico → salgo en MENOS GU.|Cuánto bajé dice qué azúcar perdí.", (402, 228), D(1)))
    F.append(frame(b, "GU", "Medir tamaño en GU", "En el Biogel P-4 el tamaño se mide en <b>unidades de glucosa (GU)</b>, comparando con una escalera. Si una <b>exoglicosidasa</b> saca un residuo, el glicano queda <b>más chico → menos GU</b>.", 2))
    return F

def galf(x, y, labels, ring=True, link=True, alditol=False):
    """galactofuranosa: anillo de 5 (C1-C4 + O), C5-C6 afuera. labels: {C: 'OH'|'OMe'|'OAc'|'—R'}"""
    o = ""
    if not alditol:
        pts = {"C1": (x + 70, y + 10), "C2": (x + 50, y + 60), "C3": (x - 10, y + 60), "C4": (x - 30, y + 10), "O": (x + 20, y - 22)}
        for a, b in (("C1", "C2"), ("C2", "C3"), ("C3", "C4"), ("C4", "O"), ("O", "C1")):
            o += L(*pts[a], *pts[b], "rbond")
        o += T(pts["O"][0], pts["O"][1] - 6, "O", "lab") + P(f"<circle cx='{pts['O'][0]}' cy='{pts['O'][1]-10}' r='14' class='hlc2'/>")
        pts["C5"] = (x - 70, y - 20); pts["C6"] = (x - 110, y - 50)
        o += L(*pts["C4"], *pts["C5"], "rbond") + L(*pts["C5"], *pts["C6"], "rbond")
        off = {"C1": (34, 0), "C2": (18, 30), "C3": (-18, 30), "C4": (0, 32), "C5": (-10, 30), "C6": (-36, -10)}
    else:
        pts = {f"C{i}": (x - 120 + 50 * (i - 1), y + 20) for i in range(1, 7)}
        for i in range(1, 6):
            o += L(*pts[f"C{i}"], *pts[f"C{i+1}"], "rbond")
        off = {f"C{i}": (0, 34 if i % 2 else -30) for i in range(1, 7)}
    for c, (px, py) in pts.items():
        if c == "O": continue
        o += f"<circle cx='{px}' cy='{py}' r='4' class='cdot'/>" + T(px + (8 if not alditol else 0), py - 8 if not alditol else py + (16 if c in ('C2','C4','C6') else -8), c, "lab2", "start" if not alditol else "middle")
        if c in labels:
            t = labels[c]; dx, dy = off[c]
            cls = {"OH": "tg-oh", "OMe": "tg-me", "OAc": "tg-ac"}.get(t, "tg-r")
            o += L(px, py, px + dx * .6, py + dy * .6, "bond") + f"<rect x='{px+dx-22}' y='{py+dy-12}' width='44' height='22' rx='8' class='{cls}'/>" + T(px + dx, py + dy + 4, t, "tg-t")
    return o

def v_metil():
    F = []
    base = {"C2": "OH", "C3": "OH", "C5": "OH", "C6": "OH", "C1": "—R"}
    b = (galf(420, 170, base) + lab(400, 30, "Galactofuranosa TERMINAL: unida a la cadena solo por el C1", "lab") +
         lab(400, 330, "anillo de 5 (furanosa): el oxígeno del anillo une el C1 con el C4", "lab2") +
         say(560, 210, "R = el resto de la cadena.|Mis OH libres: C2, C3, C5 y C6.", (500, 185), D(0)))
    F.append(frame(b, "Punto de partida", "El ejemplo", "Seguimos una <b>galactofuranosa terminal</b>: anillo de 5 (el O del anillo une C1 y C4), unida a la cadena solo por el C1. Sus OH libres son C2, C3, C5 y C6.", 1))
    b = (galf(420, 170, {"C2": "OMe", "C3": "OMe", "C5": "OMe", "C6": "OMe", "C1": "—R"}) + lab(400, 30, "Paso 1: PERMETILACIÓN", "lab") +
         say(520, 230, "Todo OH LIBRE se marca con un metilo.|Lo que está ocupado (C1, el anillo) no.", (480, 200), D(0)))
    F.append(frame(b, "Permetilación", "1) Permetilar: marcar lo libre", "Se metilan <b>todos los OH libres</b>. Los que están ocupados (unidos a otro azúcar o formando el anillo) no se pueden metilar.", 1))
    b = (galf(420, 170, {"C2": "OMe", "C3": "OMe", "C5": "OMe", "C6": "OMe", "C1": "OH"}) + lab(400, 30, "Paso 2: HIDRÓLISIS", "lab") +
         say(520, 230, "Se cortan los enlaces glicosídicos:|el C1 queda con OH (sin metilo).", (500, 180), D(0)))
    F.append(frame(b, "Hidrólisis", "2) Hidrolizar: soltar cada azúcar", "Se rompen los enlaces glicosídicos: cada azúcar queda suelto. Los carbonos que estaban unidos ahora tienen OH, <b>sin metilo</b>.", 1))
    b = (galf(400, 140, {"C1": "OH", "C2": "OMe", "C3": "OMe", "C4": "OH", "C5": "OMe", "C6": "OMe"}, alditol=True) + lab(400, 30, "Paso 3: REDUCCIÓN → el anillo se abre (alditol)", "lab") +
         say(250, 280, "Al abrirse el anillo, el C4 (que tenía el O del anillo)|también queda con OH sin metilo.", (400, 125), D(0)))
    F.append(frame(b, "Reducción", "3) Reducir: se abre el anillo", "Se reduce a <b>alditol</b>: el anillo se abre. El carbono que cerraba el anillo (acá el <b>C4</b>) también queda con OH sin metilo.", 1))
    b = (galf(400, 140, {"C1": "OAc", "C2": "OMe", "C3": "OMe", "C4": "OAc", "C5": "OMe", "C6": "OMe"}, alditol=True) + lab(400, 30, "Paso 4: ACETILACIÓN → 1,4-di-O-acetil-2,3,5,6-tetra-O-metil-galactitol", "lab") +
         say(150, 270, "Los OH que quedaban se acetilan.|Ac = estaba OCUPADO (enlace o anillo)|Me = estaba LIBRE", (300, 175), D(0)) +
         N(note(620, 300, "sin metilo en C1 y C4:|C1 = enlace · C4 = anillo|→ anillo de 5: FURANOSA|→ un solo enlace: TERMINAL", "lab"), D(1)))
    F.append(frame(b, "Acetilación", "4) Acetilar y leer el resultado", "Se acetilan los OH que quedaban. Regla: <b>metilo = estaba libre</b>; <b>acetilo = estaba ocupado</b>. Acá C1 (el enlace) y C4 (el anillo) → anillo de 5 = <b>furanosa</b>, un solo enlace = <b>terminal</b>. Si el anillo cerrara en el C5, sería piranosa (2,3,4,6-tetra-O-metil).", 2))
    gc = path("M80 300 L200 300 Q215 300 222 180 Q229 300 245 300 L340 300 Q355 300 362 150 Q369 300 385 300 L480 300 Q495 300 502 200 Q509 300 525 300 L720 300", "peak")
    b = (gc + L(60, 300, 740, 300, "bond") + lab(222, 170, "Glc") + lab(362, 140, "Man") + lab(502, 190, "Gal") + lab(400, 335, "tiempo de retención en el GC →", "lab2") +
         say(80, 30, "Glc, Man y Gal con los mismos sustituyentes|se rompen IGUAL en el espectrómetro de masas.", (300, 160), D(0)) +
         say(380, 220, "Pero salen a distinto TIEMPO del cromatógrafo:|así se distinguen (con estándares).", (500, 215), D(1)))
    F.append(frame(b, "GC-MS", "5) GC-MS: ¿cuál azúcar era?", "Los derivados de Glc, Man y Gal son estereoisómeros y dan el <b>mismo espectro de masas</b>. Se distinguen por el <b>tiempo de retención</b> en el cromatógrafo de gases, comparando con estándares.", 2))
    return F

def chainz(x0, y, n, dbl=None, cis=True, numbering=None, color_from=None):
    pts = [(x0 + i * 36, y + (0 if i % 2 == 0 else -22)) for i in range(n)]
    o = ""
    for i in range(n - 1):
        o += L(*pts[i], *pts[i + 1], "rbond")
        if dbl and i + 1 == dbl:
            (x1, y1), (x2, y2) = pts[i], pts[i + 1]
            o += L(x1 + 4, y1 + 7, x2 - 4, y2 + 7, "rbond dbl")
    return o, pts

def v_omega():
    F = []
    n = 18
    o, pts = chainz(80, 200, n)
    def nums(rev=False, cls="nmb"):
        s = ""
        for i, (x, y) in enumerate(pts):
            k = (n - i) if rev else (i + 1)
            s += T(x, y + (22 if i % 2 == 0 else -10), str(k), cls)
        return s
    dbl = L(pts[8][0] + 4, pts[8][1] + 7, pts[9][0] - 4, pts[9][1] + 7, "rbond dbl")
    cooh = T(pts[0][0] - 16, pts[0][1] + 5, "HOOC", "lab", "end"); ch3 = T(pts[-1][0] + 14, pts[-1][1] + 5, "CH₃", "lab", "start")
    b = (o + dbl + cooh + ch3 + N(nums(), .3) + hl(pts[8][0] + 18, pts[8][1] - 6, 22) +
         say(80, 40, "Δ se cuenta desde el COOH (C1).|El doble enlace arranca en el C9 → Δ9.", (pts[0][0], 180), D(0)) +
         N(lab(400, 300, "ácido oleico: 18 carbonos, 1 doble enlace → 18:1 Δ9", "lab"), D(1)))
    F.append(frame(b, "Delta", "Contar Δ: desde el COOH", "<b>18:1</b> = 18 carbonos, 1 doble enlace. <b>Δ9</b> = el doble enlace empieza en el C9, contando desde el <b>carboxilo</b> (C1).", 1))
    b = (o + dbl + cooh + ch3 + N(nums(True, "nmb2"), .3) + hl(pts[9][0] - 18, pts[9][1] - 6, 22) +
         say(430, 40, "ω se cuenta desde el CH₃ del final:|el doble enlace está a 9 → ω-9.", (pts[-1][0], 180), D(0)) +
         N(lab(400, 300, "ω = 18 − 9 = 9 · los naturales son CIS (codo)", "lab"), D(1)))
    F.append(frame(b, "Omega", "Contar ω: desde el CH₃", "<b>ω-9</b> = el último doble enlace está a 9 carbonos del <b>metilo del final</b>. Cuenta rápida: ω = 18 − 9 = 9. El oleico natural es <b>cis</b> (el elaídico es su versión trans).", 1))
    o2, pts2 = chainz(80 - 72, 200, n + 2)
    newc = "".join(f"<circle cx='{pts2[i][0]}' cy='{pts2[i][1]}' r='9' class='newc'/>" for i in (0, 1))
    b = (o2 + L(pts2[10][0] + 4, pts2[10][1] + 7, pts2[11][0] - 4, pts2[11][1] + 7, "rbond dbl") + T(pts2[-1][0] + 14, pts2[-1][1] + 5, "CH₃", "lab", "start") +
         N(newc, .3) + enzyme(130, 80, "elongasa") +
         say(220, 20, "Agrego 2 carbonos del lado del COOH.", (150, 70), D(0)) +
         say(430, 280, "El CH₃ no se tocó: sigo siendo ω-9.|Solo los Δ suben en 2 (ahora Δ11).", (pts2[-1][0], 210), D(1)))
    F.append(frame(b, "Elongación", "Alargar no cambia el ω", "Las elongasas agregan carbonos <b>del lado del COOH</b>. El extremo CH₃ no cambia, así que el <b>ω se mantiene</b> (un ω-6 sigue siendo ω-6). Lo que cambia es la numeración Δ.", 2))
    def stack(x, kinked):
        s = ""
        for j in range(5):
            if kinked:
                s += path(f"M{x+j*26} 120 l0 70 l26 40 l0 50", "satc" if False else "kink")
            else:
                s += path(f"M{x+j*16} 120 l0 160", "satc")
        return s
    b = (stack(80, False) + lab(115, 310, "18:0 (esteárico)") + lab(115, 330, "~69 °C", "lab2") +
         stack(300, False).replace("l0 160", "l0 140") + lab(335, 310, "16:0 (palmítico)") + lab(335, 330, "~63 °C", "lab2") +
         stack(520, True) + lab(590, 330, "18:1 cis (oleico) · ~13 °C", "lab") +
         say(40, 20, "Rectas y largas: me apilo bien → fundo ALTO.", (115, 110), D(0)) +
         say(470, 20, "Mi codo cis no deja apilar →|fundo BAJO (líquido).", (600, 110), D(1)) +
         N(lab(400, 380, "18:0 > 16:0 > 18:1 cis", "sg-t"), D(2)))
    F.append(frame(b, "Fusión", "Punto de fusión", "Dos reglas: cadena <b>más larga</b> → funde más alto; doble enlace <b>cis</b> → el codo impide empaquetar → funde mucho más bajo. Por eso 18:0 &gt; 16:0 &gt; 18:1 cis.", 2))
    return F

def bilayer(y0, ps_out=False, ps_in=True, n=13, x0=90):
    o = ""
    for i in range(n):
        x = x0 + i * 48
        out_ps = ps_out and i % 4 == 1; in_ps = ps_in and i % 4 == 1 and not ps_out
        o += f"<circle cx='{x}' cy='{y0}' r='10' class='{'pshead' if out_ps else 'lhead'}'/>" + path(f"M{x-3} {y0+10} l0 40 M{x+3} {y0+10} l0 40", "ltail")
        o += f"<circle cx='{x}' cy='{y0+110}' r='10' class='{'pshead' if in_ps else 'lhead'}'/>" + path(f"M{x-3} {y0+100} l0 -40 M{x+3} {y0+100} l0 -40", "ltail")
    return o + T(30, y0 + 5, "afuera", "lab2", "start") + T(30, y0 + 125, "adentro", "lab2", "start")

def v_asim():
    F = []
    b = (bilayer(150) + N(enzyme(400, 70, "flipasa"), 0, 0, -30) + battery(500, 70) +
         say(520, 10, "Llevo la PS (fosfatidilserina)|a la cara INTERNA, gastando ATP.", (420, 55), D(0)) +
         N(lab(400, 330, "célula sana: la PS (rojo) está solo adentro", "lab"), D(1)))
    F.append(frame(b, "Flipasa", "Célula sana: la flipasa ordena", "La membrana es <b>asimétrica</b>: la PS está solo en la cara interna. La <b>flipasa</b> la mantiene ahí, gastando <b>ATP</b>.", 1))
    b = (N(bilayer(150, ps_out=True), D(1) - .3) + O(bilayer(150), D(1) - .3) + enzyme(400, 70, "scramblasa") +
         say(480, 10, "Apoptosis: yo MEZCLO las dos caras,|en las dos direcciones y SIN ATP.", (420, 55), D(0)) +
         say(100, 320, "¡Ahora la PS quedó afuera!", (186, 160), D(1)))
    F.append(frame(b, "Scramblasa", "Apoptosis: la scramblasa mezcla", "En la apoptosis se apaga la flipasa y se activa la <b>scramblasa</b>, que mezcla los lípidos de las dos caras <b>sin gastar ATP</b>: la PS aparece afuera.", 2))
    b = (bilayer(150, ps_out=True) + blob(660, 70, "k-xan", "macrófago", r=36) +
         say(300, 20, "PS afuera = señal de «comeme».", (630, 60), D(0)))
    F.append(frame(b, "Macrófago", "La PS afuera es una señal", "La PS en la cara externa es una señal de <b>«comeme»</b>: los macrófagos reconocen y eliminan la célula apoptótica.", 1))
    return F

def lipid(x, y, head, cls="lhead", chains=("ltail", "ltail"), lab_=None):
    o = f"<circle cx='{x}' cy='{y}' r='14' class='{cls}'/>" + T(x, y + 4, head, "at-t")
    o += f"<rect x='{x-20}' y='{y+14}' width='40' height='14' rx='4' class='glyb'/>"
    for k, c in enumerate(chains):
        if c: o += path(f"M{x-8+16*k} {y+28} q4 10 0 20 q-4 10 0 20 q4 10 0 20", c)
    if lab_: o += T(x, y + 112, lab_, "lab")
    return o

def v_kennedy():
    F = []
    b = (blob(80, 120, "k-gln", "colina", r=22) + N(arrow(110, 120, 190, 120) + battery(150, 80), .3) + N(blob(240, 120, "k-gln", "fosfocolina", r=22), .6) +
         N(arrow(270, 120, 350, 120) + T(310, 105, "+ CTP", "lab2"), D(1) - .6) + N(blob(410, 120, "k-gln", "CDP-colina", r=24), D(1) - .3) +
         say(330, 210, "¡Me activé pegándome a CTP!", (410, 145), D(1)) +
         N(lipid(560, 70, "", "lhead", ("ltail", "ltail")) + lab(560, 200, "DAG") + arrow(440, 120, 520, 100), D(2) - .4) +
         N(lipid(700, 70, "C", "lhead", ("ltail", "ltail")) + lab(700, 200, "fosfatidilcolina") + arrow(600, 110, 660, 110), D(2)) +
         say(480, 290, "Kennedy FABRICA la PC desde cero:|DAG + CDP-colina (sale CMP).", (690, 200), D(2) + .3))
    F.append(frame(b, "Kennedy", "Vía de Kennedy: fabricar PC", "La colina se fosforila y se <b>activa con CTP</b> (CDP-colina). Después se le pasa la fosfocolina a un <b>diacilglicerol (DAG)</b> y sale la <b>fosfatidilcolina</b>. Así se fabrica PC (y PE) desde cero.", 3))
    b = (lipid(150, 60, "PI", "lhead", ("ltail", "ltail"), "fosfolípido") + scissors(300, 120) + lab(300, 70, "fosfolipasa A₂", "enz-n") +
         say(190, 215, "Corto la cadena de la posición sn-2|(la del medio del glicerol).", (320, 150), D(0)) +
         N(arrow(200, 120, 260, 120) + lipid(450, 60, "PI", "lhead", ("ltail", None), "lisofosfolípido"), D(1) - .3) +
         N(enzyme(620, 120, "LPIAT") + lipid(720, 60, "PI", "lhead", ("ltail", "arach"), "PI con araquidónico"), D(2) - .4) +
         say(330, 300, "Soy la aciltransferasa del PI: siempre elijo|el araquidónico para el sn-2.", (620, 165), D(2)))
    F.append(frame(b, "Lands", "Ciclo de Lands: retocar el sn-2", "<b>Lands</b> no fabrica: <b>remodela</b>. La <b>fosfolipasa A₂</b> saca la cadena del <b>sn-2</b> (queda un lisofosfolípido) y una <b>aciltransferasa</b> pone otra desde un acil-CoA. Cada clase tiene la suya (LPCAT para PC, LPIAT para PI).", 3))
    b = ("".join(lipid(180 + 120 * i, 60, "PI", "lhead", ("ltail", "arach")) for i in range(4)) +
         say(150, 240, "Vuelta tras vuelta, como mi aciltransferasa PREFIERE|el araquidónico, el PI termina muy enriquecido en él.", (400, 170), D(0)))
    F.append(frame(b, "Enriquecido", "Por qué un fosfolípido se enriquece", "Si la aciltransferasa de una clase <b>prefiere</b> un tipo de cadena, cada vuelta del ciclo de Lands la va acumulando: así el PI termina muy enriquecido en araquidónico en el sn-2.", 1))
    return F

def phage(x, y, cap, dna, s=1.0):
    return (f"<polygon points='{x},{y-34*s} {x+24*s},{y-20*s} {x+24*s},{y+8*s} {x},{y+22*s} {x-24*s},{y+8*s} {x-24*s},{y-20*s}' class='{cap}'/>"
            f"<path d='M{x-10*s} {y-8*s} C{x-2*s} {y-22*s} {x+8*s} {y+4*s} {x+12*s} {y-10*s}' class='{dna}'/>"
            f"<line x1='{x}' y1='{y+22*s}' x2='{x}' y2='{y+52*s}' class='ph-tail'/>"
            f"<line x1='{x}' y1='{y+52*s}' x2='{x-14*s}' y2='{y+66*s}' class='ph-tail'/><line x1='{x}' y1='{y+52*s}' x2='{x+14*s}' y2='{y+66*s}' class='ph-tail'/>")

def v_hershey():
    F = []
    b = (T(200, 40, "Experimento 1", "sg-t") + T(600, 40, "Experimento 2", "sg-t") + L(400, 30, 400, 380, "bond") +
         phage(200, 150, "cap-hot", "dna-cold") + phage(600, 150, "cap-cold", "dna-hot") +
         say(40, 260, "Crecí con ³⁵S: el azufre está en las|PROTEÍNAS → mi cápside brilla.", (200, 175), D(0)) +
         say(440, 260, "Crecí con ³²P: el fósforo está en el|ADN → mi ADN brilla.", (600, 160), D(1)))
    F.append(frame(b, "Marcar", "1) Marcar: proteína o ADN", "Se crían fagos con <b>³⁵S</b> (marca las <b>proteínas</b>: cisteína y metionina tienen S) o con <b>³²P</b> (marca el <b>ADN</b>: los fosfatos). Cada experimento sigue una sola cosa.", 2))
    bact = lambda x, y: f"<rect x='{x-70}' y='{y}' width='140' height='70' rx='35' class='bact'/>"
    b = (bact(200, 230) + bact(600, 230) + phage(200, 160, "cap-hot", "dna-cold", .8) + phage(600, 160, "cap-cold", "dna-hot", .8) +
         N(path("M190 240 C200 260 215 250 220 270", "dna-cold") + path("M590 240 C600 260 615 250 620 270", "dna-hot"), .5) +
         say(250, 40, "Me pego a la bacteria e INYECTO mi ADN.|La cápside se queda afuera.", (215, 140), D(0)))
    F.append(frame(b, "Infectar", "2) Infectar", "El fago se pega a la bacteria e <b>inyecta su ADN</b>. La cápside (proteína) queda <b>afuera</b>, pegada a la superficie.", 1))
    b = (bact(200, 230) + bact(600, 230) + path("M190 240 C200 260 215 250 220 270", "dna-cold") + path("M590 240 C600 260 615 250 620 270", "dna-hot") +
         O(phage(200, 160, "cap-hot", "dna-cold", .8), .6, 60, -120, 1) + O(phage(600, 160, "cap-cold", "dna-hot", .8), .6, 60, -120, 1) +
         N(phage(280, 70, "cap-hot", "dna-cold", .6) + phage(680, 70, "cap-cold", "dna-hot", .6), 1.2) +
         say(260, 300, "LICUADORA: despega las cápsides vacías de las bacterias.", (300, 110), D(0) + 1))
    F.append(frame(b, "Licuar", "3) Licuar", "La <b>licuadora</b> despega las cápsides vacías que quedaron afuera de las bacterias.", 1))
    def tb(x, pel, sup):
        return (f"<path d='M{x-40} 60 L{x-40} 240 Q{x} 284 {x+40} 240 L{x+40} 60' class='tube'/><rect x='{x-39}' y='80' width='78' height='160' class='{sup}'/>"
                f"<ellipse cx='{x}' cy='252' rx='26' ry='14' class='{pel}'/>")
    b = (tb(200, "pel-cold", "sup-hot") + tb(600, "pel-hot", "sup-cold") +
         T(255, 120, "sobrenadante:", "lab2", "start") + T(255, 136, "cápsides", "lab2", "start") + N(T(255, 155, "³⁵S ✓", "stp-t", "start"), .6) +
         T(255, 250, "pellet:", "lab2", "start") + T(255, 266, "bacterias", "lab2", "start") +
         T(655, 120, "sobrenadante", "lab2", "start") + T(655, 250, "pellet:", "lab2", "start") + T(655, 266, "bacterias", "lab2", "start") + N(T(655, 285, "³²P ✓", "stp-t", "start"), .6) +
         say(230, 320, "El ³²P (ADN) quedó en el PELLET, con las bacterias:|lo que entró fue el ADN → es el material genético.", (600, 260), D(0) + .6))
    F.append(frame(b, "Centrifugar", "4) Centrifugar y medir", "Al centrifugar, las bacterias (pesadas) van al <b>pellet</b> y las cápsides quedan en el sobrenadante. El <b>³⁵S</b> sale en el <b>sobrenadante</b> y el <b>³²P</b> en el <b>pellet</b>: lo que entró a la bacteria es el ADN.", 1))
    return F

def v_uracilo():
    F = []
    b = (pyr_char(130, 120, "k-ump", [("C2", "O"), ("C4", "O")], R=26, rib={"p5": 3, "deoxy": True}, name="dUTP", mood="o") + enzyme(400, 120, "dUTPasa") + helix(560, 300, 175, "ADN") +
         say(470, 20, "Soy el PORTERO: rompo el dUTP libre|ANTES de que entre al ADN.", (420, 105), D(0)) +
         N(lab(400, 230, "prevención: actúa sobre el nucleótido suelto", "lab2"), D(1)))
    F.append(frame(b, "dUTPasa", "Prevenir: dUTPasa", "La <b>dUTPasa</b> actúa <b>antes</b>: rompe el dUTP libre (dUTP → dUMP) para que no entre U al ADN.", 1))
    b = (helix(80, 280, 250, "ADN con una U") + N(pyr_char(205, 160, "k-ump", [("C2", "O"), ("C4", "O")], R=22, mood="o", name="uracilo"), 0) +
         enzyme(470, 120, "uracilo-ADN|glicosilasa") +
         say(420, 20, "Soy la LIMPIEZA: encuentro la U que ya|quedó en el ADN y la saco.", (490, 100), D(0)) +
         O(pyr_char(205, 160, "k-ump", [("C2", "O"), ("C4", "O")], R=22, mood="o", name="uracilo"), D(1), 200, -60, 1) +
         N(enzyme(650, 260, "reparación", k="k-enz2"), D(1)) + say(400, 250, "Y yo pongo la C correcta.", (625, 265), D(2)))
    F.append(frame(b, "Glicosilasa", "Reparar: uracilo-ADN glicosilasa", "La <b>uracilo-ADN glicosilasa</b> actúa <b>después</b>: saca la U que ya quedó en el ADN, y la reparación por escisión de bases repone la C.", 3))
    return F

# ================================================================ TEXTO
def build():
    H = ['<section class="mod" id="rf" data-topics="G1,G2,GC,L,N,NM">\n<p class="kicker">Repaso personal · hecho con tus errores del 11/11</p>\n<h1>Repaso de falladas</h1>\n'
         '<p class="lead">Es la teoría <b>filtrada</b>: solo los temas donde fallaste, explicados de nuevo, con dibujos y videos en lo que tiene varios pasos. Leelo entero y después practicá tus falladas con el botón del final de cada parte.</p>\n']
    # ---------------- GLÚCIDOS
    H.append('<h2>1. Glúcidos</h2>')
    H.append('<h3>Monosacáridos: epímeros y forma cíclica</h3>'
             '<p>Dos azúcares son <b>epímeros</b> cuando son iguales salvo en <b>un solo</b> carbono quiral. Tomando la glucosa como referencia: la <b>manosa</b> es su epímero en <b>C2</b> y la <b>galactosa</b>, en <b>C4</b>.</p>'
             '<p>En agua, las hexosas se cierran en un anillo: el OH del C5 ataca al carbonilo (C1) y forma un anillo de 6 (piranosa). El C1 queda como <b>carbono anomérico</b>, con un OH nuevo que puede quedar de dos maneras:</p>'
             '<ul><li><b>α</b>: el OH anomérico, del lado <b>opuesto</b> al CH₂OH (abajo en una D-hexosa).</li><li><b>β</b>: del <b>mismo lado</b> que el CH₂OH (arriba).</li></ul>'
             '<p>El anillo real no es plano: es una <b>silla</b>. Cada sustituyente queda <b>ecuatorial</b> (hacia afuera, sin choques) o <b>axial</b> (vertical, choca con los vecinos). La <b>β-D-glucosa</b> tiene <b>todo ecuatorial</b> y por eso es la hexosa más estable. Cualquier epímero tiene algo axial: la β-D-manosa tiene el OH del C2 axial.</p>'
             + vid("rfa", "Del azúcar abierto a la silla", v_anillo()) + fig_chairs()
             + '<div class="box why"><b>Para recordar.</b> «<b>Ma</b>nosa = C2, <b>Ga</b>lactosa = C4». En D: <b>β = arriba = mismo lado</b> que el CH₂OH. La β-glucosa es la única con todo ecuatorial.</div>')
    H.append('<h3>Derivados: alditoles, azúcares activados y glicación</h3>'
             '<div class="tbl"><table><tr><th>Derivado</th><th>Qué le pasó al azúcar</th><th>Ejemplos</th></tr>'
             '<tr><td><b>Alditol</b> (termina en «-itol»)</td><td>El C=O se <b>redujo</b> a CH₂OH: un polialcohol, sin anillo</td><td>Sorbitol (de la glucosa), <b>ribitol</b> (de la ribosa, en la riboflavina → <b>FMN y FAD</b>)</td></tr>'
             '<tr><td><b>Desoxiazúcar</b></td><td>Le falta un OH</td><td>2-desoxirribosa (ADN)</td></tr>'
             '<tr><td><b>Ácido urónico</b></td><td>El C6 se oxidó a COOH</td><td>Glucurónico, idurónico (en los GAG)</td></tr>'
             '<tr><td><b>Azúcar nucleotídico</b></td><td>Pegado a un nucleótido: <b>activado</b></td><td>UDP-glucosa, UDP-galactosa</td></tr></table></div>'
             + figs("f_dribosa", "f_glucitol") +
             '<p>Los <b>azúcares nucleotídicos</b> son la forma <b>activada</b> de los azúcares. Las <b>glicosiltransferasas</b> los usan como dadores para armar glucógeno, glicoproteínas y glicolípidos.</p>'
             '<p>La <b>glicación</b> (en el cuerpo) y la <b>reacción de Maillard</b> (en la cocina) son la <b>misma química no enzimática</b>: el carbonilo de un azúcar reductor reacciona con un grupo amino de una proteína. La <b>HbA1c</b> es hemoglobina glicada: mide la glucosa promedio de los últimos 2–3 meses.</p>'
             + vid("rfb", "Azúcares activados y glicación", v_activado()))
    H.append('<h3>Polisacáridos: glucógeno, quitina y peptidoglicano</h3>'
             + figs("s_amilopectina", "s_glucogeno", cls="figs pf") +
             '<div class="tbl"><table><tr><th></th><th>Unidad y enlace</th><th>Lo que lo distingue</th></tr>'
             '<tr><td>Amilopectina (plantas)</td><td>Glc α(1→4) + ramas α(1→6)</td><td>Una rama cada <b>24–30</b> residuos</td></tr>'
             '<tr><td><b>Glucógeno</b> (animales)</td><td>Glc α(1→4) + ramas α(1→6)</td><td>Una rama cada <b>8–12</b>: más ramificado, compacto y con muchos extremos para liberar glucosa rápido</td></tr>'
             '<tr><td>Celulosa</td><td>Glc β(1→4)</td><td>Cadenas rectas → fibras</td></tr>'
             '<tr><td><b>Quitina</b></td><td><b>GlcNAc β(1→4)</b></td><td>Como la celulosa con NHAc en el C2 (artrópodos, hongos)</td></tr>'
             '<tr><td><b>Peptidoglicano</b></td><td>GlcNAc y MurNAc <b>alternados</b>, β(1→4)</td><td>Con péptidos que unen las cadenas (pared bacteriana)</td></tr></table></div>'
             + figs("s_quitina", "p_peptidoglicano", cls="figs pf"))
    H.append('<h3>GAG y proteoglicanos</h3>'
             '<p>Los GAG son cadenas largas, sin ramificar, de un <b>disacárido que se repite</b>: casi siempre <b>ácido urónico + aminoazúcar</b>. Para reconocerlos, mirá qué ácido urónico tienen y qué aminoazúcar:</p>'
             + fig_gag_tree() + figs("c_hialuronano", "c_condroitin", "c_dermatan", "c_queratan", cls="figs pf") +
             '<p>El <b>ácido L-idurónico (IdoA)</b> es el <b>epímero en C5</b> del ácido D-glucurónico (GlcA): el COO⁻ queda del otro lado del anillo. El <b>queratán sulfato</b> es la excepción: no tiene ácido urónico, sino <b>galactosa</b>.</p>' + figs("m_glca", "m_idoa") +
             '<p>Un <b>proteoglicano</b> es una <b>proteína central (core)</b> con muchas cadenas de GAG unidas covalentemente. Es más azúcar que proteína. En el cartílago, el <b>agrecano</b> lleva condroitín y queratán sulfato; muchos agrecanos se enganchan a una cadena de hialuronano y forman un agregado enorme que retiene agua y amortigua.</p>' + fig_brush())
    H.append('<h3>Glicanos que se reconocen: selectinas, influenza y LPS</h3>'
             '<p>Muchas funciones de los glicanos dependen de que una proteína los <b>reconozca</b>. Las proteínas que reconocen azúcares se llaman <b>lectinas</b>.</p>'
             + vid("rfc", "Glicanos que se reconocen", v_reconocer()))
    H.append('<h3>Análisis de glicanos: obtener, separar y medir</h3>'
             '<p>Para estudiar polisacáridos y glicanos hay una secuencia lógica: primero <b>aislar</b>, después <b>separar</b>, comprobar si está <b>puro</b>, <b>liberar</b> los glicanos de la proteína, <b>limpiarlos</b>, medir su <b>tamaño</b> y averiguar sus <b>enlaces</b>.</p>'
             + vid("rfd", "Del extracto al polisacárido puro", v_aislar())
             + vid("rfe", "Liberar, purificar y medir glicanos", v_glicanos()) +
             '<p><b>¿Por qué secuenciar glicanos es tan difícil?</b> Una proteína es una cadena lineal copiada de un molde (el ARNm). Un glicano se <b>ramifica</b>, sus azúcares se unen por distintos carbonos y como α o β, y <b>no se copia de ningún molde</b>: su estructura depende de qué enzimas actuaron. No se puede «leer» como una secuencia.</p>')
    H.append('<h3>Análisis de metilación: qué enlace tenía cada azúcar</h3>'
             '<p>El análisis de metilación responde «¿por qué carbonos estaba unido cada azúcar?». La lógica es <b>marcar lo libre antes de desarmar</b>: lo que quede sin marca estaba ocupado.</p>'
             + vid("rff", "Análisis de metilación", v_metil()) + truco('«<b>Metilo = estaba libre; acetilo = estaba ocupado</b>». Hay un acetilo extra por el anillo: si cae en el C4 es furanosa y si cae en el C5, piranosa.'))
    H.append('<h3>Periodato</h3>' + fig_periodato() +
             '<p>El periodato corta entre carbonos vecinos que tienen OH; si hay tres OH seguidos, el del medio sale como <b>ácido fórmico</b>. En la celulosa solo los <b>extremos</b> dan fórmico (1 el no reductor y 2 el reductor), así que da <b>3 mol por mol</b> sin importar el largo de la cadena.</p>')
    H.append(practice("G1,G2,GC", "Ya leí: practicar mis falladas de glúcidos"))
    # ---------------- LÍPIDOS
    H.append('<h2>2. Lípidos</h2>')
    H.append('<h3>Ácidos grasos: nombres, ω y punto de fusión</h3>'
             + vid("rfg", "Contar Δ y ω", v_omega()) + figs("oleico", "elaidico", "linoleico") +
             '<p><b>Oleico</b> = 18:1 cis-Δ9, ω-9 (un doble enlace). <b>Linoleico</b> = 18:2 Δ9,12, ω-6 (dos). <b>Elaídico</b> = el oleico en trans.</p>')
    H.append('<h3>TAG: por qué rinden tanto</h3><p>Los triacilglicéridos (glicerol + 3 ácidos grasos; <b>no</b> tienen fosfato) son la mejor reserva porque sus carbonos están <b>muy reducidos</b> (casi todo CH₂: mucho para oxidar, ~9 kcal/g contra ~4 de los glúcidos) y se guardan <b>sin agua</b> (el glucógeno arrastra unos 2 g de agua por gramo).</p>')
    H.append('<h3>Fosfolípidos, esfingolípidos y arqueas</h3>'
             '<div class="tbl"><table><tr><th>Lípido</th><th>Esqueleto</th><th>Cabeza</th><th>Carga a pH 7</th></tr>'
             '<tr><td>Fosfatidilcolina (PC)</td><td>glicerol</td><td>fosfato − · colina +</td><td>0</td></tr><tr><td>Fosfatidiletanolamina (PE)</td><td>glicerol</td><td>fosfato − · amino +</td><td>0</td></tr>'
             '<tr><td><b>Fosfatidilserina (PS)</b></td><td>glicerol</td><td>fosfato − · <b>carboxilo −</b> · amino +</td><td><b>−1</b></td></tr><tr><td>Fosfatidilinositol (PI)</td><td>glicerol</td><td>fosfato − · inositol</td><td>−1</td></tr>'
             '<tr><td><b>Esfingomielina</b></td><td><b>esfingosina</b> (ceramida)</td><td>fosfocolina</td><td>0</td></tr></table></div>'
             + figs("pc", "ps", "esfingomielina") +
             '<p>La <b>esfingomielina</b> no tiene glicerol: es <b>ceramida</b> (esfingosina + un ácido graso por amida) con <b>fosfocolina</b>. Tiene la misma cabeza que la PC con otro esqueleto: es un <b>esfingolípido</b>, no un glicerofosfolípido.</p>'
             '<p>Las <b>arqueas</b> no usan colesterol para resistir. Sus lípidos tienen <b>enlaces éter</b> (C–O–C, mucho más resistentes que los éster) y <b>cadenas isoprenoides ramificadas</b>; algunas atraviesan toda la membrana. Eso aguanta calor, ácido y sal.</p>')
    H.append('<h3>Cómo se comporta la membrana</h3>'
             '<p><b>Esteroles</b> (colesterol en animales, ergosterol en hongos): abundan sobre todo en la <b>membrana plasmática</b> y escasean en las internas. Ordenan la membrana y amortiguan los cambios de fluidez.</p>'
             '<p><b>DHA</b> (22:6, ω-3): con 6 dobles enlaces cis, sus cadenas son muy flexibles. Hace la membrana <b>más fluida y deformable</b> (lo contrario del colesterol), lo que facilita la fusión de vesículas en la sinapsis y los cambios de forma en la retina.</p>'
             + fig_shapes() +
             '<p>La <b>forma</b> de cada lípido decide qué arma: los cilindros (PC) arman <b>bicapas</b>; los conos (PE, cabeza chica) curvan la membrana; los de <b>una sola cola</b> y cabeza grande (lisofosfolípidos, detergentes) arman <b>micelas</b>. Los <b>detergentes</b> no rompen enlaces: desarman la bicapa en micelas mixtas que se llevan lípidos y proteínas. Las <b>nanopartículas de las vacunas</b> encierran el ARN dentro de una estructura lipídica cerrada, porque el centro de una micela es pura cola hidrofóbica y el ARN, polar y cargado, no puede estar ahí.</p>'
             + vid("rfh", "Asimetría de la membrana", v_asim()))
    H.append('<h3>Fabricar y remodelar fosfolípidos</h3>' + vid("rfi", "Kennedy y Lands", v_kennedy()) +
             '<div class="box why"><b>Para recordar.</b> Kennedy = <b>fabricar</b> (DAG + CDP-colina). Lands = <b>retocar el sn-2</b> (la PLA₂ saca y la aciltransferasa pone).</div>')
    H.append('<h3>Extraer lípidos: Folch</h3><p><b>Folch</b> usa cloroformo : metanol <b>2:1</b>. El metanol separa los lípidos de las proteínas y el cloroformo los disuelve. Al agregar agua se forman dos fases, y los lípidos quedan en la de <b>abajo</b> (cloroformo).</p>')
    H.append(practice("L", "Ya leí: practicar mis falladas de lípidos"))
    # ---------------- AN I
    H.append('<h2>3. Ácidos nucleicos I</h2>')
    H.append('<h3>Nucleósidos, nucleótidos y azúcares</h3>'
             '<div class="tbl"><table><tr><th>Partes</th><th>Nombre</th><th>Ejemplo</th></tr><tr><td>base</td><td>base</td><td>adenina</td></tr><tr><td>base + azúcar</td><td><b>nucleósido</b></td><td>adenosina</td></tr><tr><td>base + azúcar + fosfato(s)</td><td><b>nucleótido</b></td><td>AMP, ADP, ATP</td></tr></table></div>'
             + figs("adenina", "adenosina", "amp") +
             '<p>El azúcar del ADN es la <b>2-desoxirribosa</b> (una pentosa en anillo de 5, sin OH en el 2′); el del ARN es la ribosa. Ese OH del 2′ explica por qué el ARN es frágil en medio alcalino:</p>' + figs("h_brib", "h_bdrib") + fig_rna_alk())
    H.append('<h3>Cómo se descubrió que el ADN es el material genético</h3>'
             '<ol class="flow"><li class="m">Miescher (1869): aísla la «nucleína»</li><li class="m">Kossel: describe sus componentes y sus 5 bases</li><li class="m">Levene: hipótesis del tetranucleótido</li><li class="m">Griffith (1928): principio transformante</li><li class="m">Avery, MacLeod y McCarty (1944): es ADN</li><li class="m">Chargaff (1950): A = T, G = C y la composición varía entre especies</li><li class="m">Hershey y Chase (1952)</li><li class="m">Foto 51 → Watson y Crick (1953)</li></ol>'
             '<p>La <b>hipótesis del tetranucleótido</b> decía que el ADN era una misma unidad de 4 nucleótidos (A, T, G, C en igual cantidad) repetida una y otra vez. Una secuencia así de <b>monótona y repetitiva</b> no podría guardar información, y por eso se creía que el material genético eran las proteínas. Chargaff la refutó.</p>'
             + vid("rfj", "Hershey y Chase", v_hershey()))
    H.append('<h3>Chargaff y los cálculos con bases</h3>'
             '<p>En un ADN bicatenario <b>A = T</b> y <b>G = C</b>. Con eso se resuelve todo, siguiendo un método:</p>'
             '<ol><li><b>Pasar pares de bases a bases:</b> 1 pb = 2 bases (1000 pb = 2000 bases).</li><li><b>Usar los pares:</b> si G = 22 %, entonces C = 22 % y G + C = 44 %.</li><li><b>Lo que falta es A + T</b> (56 %), y se reparte en partes iguales → A = 28 %.</li></ol>'
             '<p><b>Ejemplo.</b> 1000 pb con 58 % G+C → 2000 bases → G + C = 1160 → G = C = 580; A + T = 840 → A = T = 420.</p>'
             '<p><b>Complementaria en 5′→3′:</b> primero se escribe la complementaria antiparalela (5′-ATGCCA-3′ → 3′-TACGGT-5′) y después se da vuelta para leerla 5′→3′ (<b>5′-TGGCAT-3′</b>). En el ADN nunca va U.</p>'
             '<p><b>Unidades:</b> 1 pg = 10⁻¹² g. Entonces 6 pg × 2 × 10¹² células = 12 × 10¹² pg = <b>12 g</b>.</p>')
    H.append('<h3>Foto 51 y la forma B</h3>' + figs("f51_2", "f51_3", "f51_4", cls="figs pf") +
             '<p>En la foto, las distancias van al revés: lo <b>grande</b> en la molécula aparece <b>cerca del centro</b> y lo <b>chico</b>, lejos.</p>'
             '<ul><li>La <b>separación entre las filas</b> de manchas → <b>34 Å</b>: lo que mide una vuelta.</li><li>Las <b>manchas fuertes de arriba y abajo</b> → <b>3,4 Å</b>: la distancia entre pares de bases. Caen en la fila 10 → <b>10 pb por vuelta</b>.</li><li>La <b>4.ª fila falta</b> → hay <b>dos cadenas</b> corridas 3/8 de vuelta, y eso arma el surco mayor y el menor.</li></ul>'
             '<p>El esquema interactivo completo está en Ác. nucleicos I → «La Foto 51, detalle por detalle».</p>')
    H.append(practice("N", "Ya leí: practicar mis falladas de ácidos nucleicos I"))
    # ---------------- AN II
    H.append('<h2>4. Ácidos nucleicos II</h2>')
    H.append('<h3>Replicación: cebador y horquillas</h3><p>La ADN polimerasa reconoce el molde sin problema, pero <b>no puede empezar de cero</b>: solo agrega nucleótidos a un <b>3′-OH que ya existe</b>. El cebador de ARN (hecho por la primasa) le da ese primer 3′-OH.</p>'
             '<p><b>Bidireccional</b> se refiere a las <b>horquillas</b>: desde el origen salen dos horquillas en sentidos opuestos. La síntesis es <b>siempre 5′→3′</b>; ninguna polimerasa sintetiza 3′→5′.</p>')
    H.append('<h3>Terminar la transcripción e iniciar la traducción</h3>'
             '<ul><li><b>Independiente de Rho</b> = sin Rho: el ARN forma una <b>horquilla</b> rica en G-C seguida de varias <b>U</b>, que suelta a la polimerasa. La que usa la proteína Rho es la <b>dependiente</b> de Rho.</li>'
             '<li>El <b>ARNt iniciador</b> es el único que entra directo al sitio <b>P</b>; todos los demás entran por el A.</li>'
             '<li>El ribosoma es una <b>ribozima</b>: el enlace peptídico lo cataliza su <b>ARNr</b>, no sus proteínas.</li></ul>'
             '<p>Los videos con fases están en Ác. nucleicos II · simple (transcripción, pasos 8–9; traducción, pasos 4–6).</p>')
    H.append('<h3>Nucleótidos: de dónde vienen y cómo se cuida el ADN</h3>'
             '<p>La <b>ruta principal de importación</b> de bases y nucleótidos es la <b>digestión de los ácidos nucleicos de la dieta</b>.</p>'
             '<p>Con alopurinol se acumulan hipoxantina y xantina, que no hacen daño porque son <b>más solubles</b> que el ácido úrico: se eliminan sin formar cristales.</p>'
             + vid("rfk", "U en el ADN: prevenir y reparar", v_uracilo()))
    H.append(practice("NM", "Ya leí: practicar mis falladas de ácidos nucleicos II"))
    H.append('</section>\n')
    return "".join(H)

if __name__ == "__main__":
    open("t_rf.html", "w").write(build())
    print("ok")
