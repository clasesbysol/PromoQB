# Genera tres "videos" paso a paso (replicación, transcripción, traducción)
# y los inserta en t_n.html (idempotente, entre marcadores).
import math, re

# ---------------------------------------------------------------- helpers
def st(d=0, dx=0, dy=0, t=None):
    s = f"--d:{d}s;--dx:{dx}px;--dy:{dy}px"
    if t: s += f";--t:{t}s"
    return s

def N(body, d=0, dx=0, dy=0, t=None):          # entra
    return f"<g class='new' style='{st(d,dx,dy,t)}'>{body}</g>"

def O(body, d=0, dx=0, dy=0, t=None):          # sale
    return f"<g class='out' style='{st(d,dx,dy,t)}'>{body}</g>"

def P(body, d=0):                               # parpadea (resaltado)
    return f"<g class='pulse' style='--d:{d}s'>{body}</g>"

def T(x, y, s, cls="lab", a="middle"):
    return f"<text x='{x}' y='{y}' text-anchor='{a}' class='{cls}'>{s}</text>"

def L(x1, y1, x2, y2, cls):
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' class='{cls}'/>"

def path(d, cls, grow=False, d0=0, t=None):
    if grow:
        return f"<path d='{d}' class='{cls} grow' pathLength='1' style='{st(d0, t=t)}'/>"
    return f"<path d='{d}' class='{cls}'/>"

def seg(x1, x2, y, cls, grow=False, d0=0, t=None):
    return path(f"M{x1} {y} L{x2} {y}", cls, grow, d0, t)

def ticks(x1, x2, y1, y2, step=14):
    if x2 < x1: x1, x2 = x2, x1
    return "".join(L(x, y1, x, y2, "bp") for x in range(int(x1) + 6, int(x2) - 3, step))

def arrow(x1, y1, x2, y2, cls="arr", h=9):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - h * math.cos(a - .45), y2 - h * math.sin(a - .45))
    p2 = (x2 - h * math.cos(a + .45), y2 - h * math.sin(a + .45))
    return (L(x1, y1, x2, y2, cls) +
            f"<polygon points='{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}' class='{cls}h'/>")

def E(x, y, w, h, c, label, shape="rect", sub=None, fs=None):
    """Enzima / proteína: forma coloreada + nombre adentro."""
    if shape == "ell":
        sh = f"<ellipse cx='{x}' cy='{y}' rx='{w/2}' ry='{h/2}'/>"
    elif shape == "hex":
        r = w / 2
        pts = " ".join(f"{x+r*math.cos(math.pi/3*k):.1f},{y+r*0.82*math.sin(math.pi/3*k):.1f}" for k in range(6))
        sh = f"<polygon points='{pts}'/>"
    else:
        sh = f"<rect x='{x-w/2}' y='{y-h/2}' width='{w}' height='{h}' rx='{min(w,h)/2.6:.0f}'/>"
    lines = label.split("|")
    y0 = y - (len(lines) - 1) * 8 + 5 - (6 if sub else 0)
    tx = "".join(T(x, y0 + 16 * i, s, "ez-t") for i, s in enumerate(lines))
    if sub: tx += T(x, y0 + 16 * len(lines) - 1, sub, "ez-s")
    return f"<g class='ez {c}'>{sh}{tx}</g>"

def svg(body, label):
    return f"<svg class='fr' viewBox='0 0 800 400' role='img' aria-label='{label}'>{body}</svg>"

def bib(s="Solo bibliografía"):
    return f" <span class='bib'>{s}</span>"

# ================================================================ REPLICACIÓN
# Horquilla (zoom): molde de arriba 5'→3' (molde de la retrasada),
# molde de abajo 3'→5' (molde de la adelantada). La horquilla avanza →.
TOPY, BOTY, NTOP, NBOT = 100, 290, 124, 266
FX = 560

def fork(twist=False):
    o = []
    o.append(path(f"M30 {TOPY} L470 {TOPY} C515 {TOPY} 520 175 {FX} 175 L790 175", "s-old"))
    o.append(path(f"M30 {BOTY} L470 {BOTY} C515 {BOTY} 520 205 {FX} 205 L790 205", "s-old"))
    if not twist:
        o.append(ticks(FX + 4, 790, 178, 202))
    o.append(T(18, TOPY + 5, "5′", "pol"))
    o.append(T(18, BOTY + 5, "3′", "pol"))
    o.append(T(788, 166, "3′", "pol", "end"))
    o.append(T(788, 226, "5′", "pol", "end"))
    return "".join(o)

def helicase(new=False):
    g = E(FX + 2, 190, 64, 64, "c1", "Helicasa", "hex")
    return N(g, 0, -60, 0, 1.1) if new else g

def topo(new=False):
    g = E(710, 190, 92, 50, "c2", "Topo-|isomerasa", "ell")
    return N(g, .1, 0, -40) if new else g

def ssb_top(xs):
    return "".join(f"<circle cx='{x}' cy='{TOPY}' r='9' class='ssb'/>" for x in xs)

def leading(full=True, grow=False):
    o = [seg(50, 90, NBOT, "s-rna")]
    if full:
        o.append(seg(90, 470, NBOT, "s-new", grow, .25, 1.8))
        tk = ticks(90, 470, NBOT + 3, BOTY - 3)
        o.append(N(tk, 1.6) if grow else tk)
    o.append(T(40, NBOT + 5, "5′", "pol", "end"))
    return "".join(o)

def pol3_lead(new=False):
    g = E(440, NBOT, 70, 40, "c3", "Pol III")
    return N(g, .25, -350, 0, 1.8) if new else g

def lag_old():
    """Fragmentos previos ya unidos (60–270) + cebador del fragmento anterior (270–300)."""
    return (seg(60, 270, NTOP, "s-new") + ticks(60, 300, TOPY + 3, NTOP - 3) +
            seg(270, 300, NTOP, "s-rna") + T(52, NTOP + 5, "3′", "pol", "end"))

def rep_frames():
    F = []
    # 1 origen
    b = (path("M40 185 L760 185", "s-old") + path("M40 215 L760 215", "s-old") + ticks(40, 760, 188, 212) +
         T(30, 190, "5′", "pol", "end") + T(30, 220, "3′", "pol", "end") + T(770, 190, "3′", "pol", "start") + T(770, 220, "5′", "pol", "start") +
         P("<rect x='350' y='170' width='100' height='60' rx='10' class='hlbox'/>") +
         T(400, 258, "origen (ori)", "lab") +
         N(E(372, 152, 40, 34, "c6", "") + E(428, 152, 40, 34, "c6", ""), .2, 0, -50) +
         N(T(400, 120, "proteínas iniciadoras", "lab2"), .9))
    F.append((svg(b, "Origen de replicación"), "Todo empieza en el origen",
              "La replicación arranca en un sitio fijo del ADN, el <b>origen</b>. Proteínas iniciadoras lo reconocen y abren la doble hélice."))
    # 2 burbuja
    b = (path("M40 185 L300 185 C340 185 340 130 380 130 L420 130 C460 130 460 185 500 185 L760 185", "s-old") +
         path("M40 215 L300 215 C340 215 340 270 380 270 L420 270 C460 270 460 215 500 215 L760 215", "s-old") +
         ticks(40, 300, 188, 212) + ticks(500, 760, 188, 212) +
         N(seg(370, 430, 152, "s-new") + seg(370, 430, 248, "s-new"), .5) +
         N(arrow(300, 330, 230, 330) + arrow(500, 330, 570, 330) + T(220, 335, "horquilla", "lab", "end") + T(580, 335, "horquilla", "lab", "start"), .2) +
         N("<rect x='470' y='110' width='160' height='180' rx='14' class='zoom'/>" + T(550, 100, "vamos a acercarnos acá", "lab2"), 1.2))
    F.append((svg(b, "Burbuja con dos horquillas"), "Burbuja y dos horquillas",
              "Se forma una <b>burbuja</b> con dos horquillas que avanzan en sentidos opuestos: la replicación es <b>bidireccional</b>. Ahora seguimos una sola horquilla."))
    # 3 helicasa
    b = fork() + helicase(True) + N(arrow(600, 250, 680, 250) + T(640, 272, "avance de la horquilla", "lab2"), .9) + N(T(FX + 2, 140, "usa ATP", "lab2"), 1.1)
    F.append((svg(b, "Helicasa"), "Helicasa: separa las cadenas",
              "La <b>helicasa</b> rompe los puentes de hidrógeno entre las bases y separa las dos cadenas, gastando ATP. Avanza hacia el ADN que todavía está cerrado."))
    # 4 topoisomerasa
    tw = "".join(path(f"M{x} 175 C{x+15} 175 {x+15} 205 {x+30} 205 C{x+45} 205 {x+45} 175 {x+60} 175", "s-old tw") for x in range(600, 780, 60))
    b = (path(f"M30 {TOPY} L470 {TOPY} C515 {TOPY} 520 175 {FX} 175 L600 175", "s-old") +
         path(f"M30 {BOTY} L470 {BOTY} C515 {BOTY} 520 205 {FX} 205 L600 205", "s-old") +
         T(18, TOPY + 5, "5′", "pol") + T(18, BOTY + 5, "3′", "pol") +
         O(tw + T(690, 150, "tensión (superenrollamiento)", "lab2"), .9) +
         N(seg(600, 790, 175, "s-old") + seg(600, 790, 205, "s-old") + ticks(604, 790, 178, 202), 1.1) +
         helicase() + topo(True))
    F.append((svg(b, "Topoisomerasa"), "Topoisomerasa (girasa): alivia la tensión",
              "Al abrir la hélice, por delante se acumula tensión (superenrollamiento). Las <b>topoisomerasas</b> (en bacterias, la <b>girasa</b>) cortan, dejan girar y vuelven a unir el ADN."))
    # 5 SSB
    xs = list(range(70, 460, 34))
    ssb = "".join(N(f"<circle cx='{x}' cy='{TOPY}' r='9' class='ssb'/><circle cx='{x}' cy='{BOTY}' r='9' class='ssb'/>", .08 * i, 0, -16) for i, x in enumerate(xs))
    b = fork() + helicase() + topo() + ssb + N(T(250, 70, "proteínas SSB", "lab"), .6)
    F.append((svg(b, "SSB"), "Proteínas SSB: cuidan la cadena simple",
              "Las <b>SSB</b> se pegan a las cadenas ya separadas para que no se vuelvan a aparear ni formen horquillas internas."))
    # 6 primasa (adelantada)
    b = (fork() + helicase() + topo() + ssb_top(xs) + "".join(f"<circle cx='{x}' cy='{BOTY}' r='9' class='ssb'/>" for x in xs if x > 130) +
         N(E(80, NBOT - 34, 74, 38, "c4", "Primasa"), 0, 0, -40) + N(seg(50, 90, NBOT, "s-rna", True, .6), 0) +
         N(T(70, NBOT + 46, "cebador de ARN", "lab2") + T(40, NBOT + 5, "5′", "pol", "end") + T(98, NBOT + 5, "3′-OH", "pol", "start"), 1.1))
    F.append((svg(b, "Primasa"), "Primasa: pone el cebador",
              "La ADN polimerasa no puede empezar de cero: necesita un extremo 3′-OH. La <b>primasa</b>, que es una ARN polimerasa, arma un <b>cebador</b> corto de ARN."))
    # 7 Pol III adelantada
    b = (fork() + helicase() + topo() + ssb_top(xs) + leading(True, True) + pol3_lead(True) +
         N(T(280, NBOT - 18, "hebra adelantada: continua, 5′→3′", "lab") + arrow(390, NBOT - 34, 450, NBOT - 34), 1.9))
    F.append((svg(b, "ADN polimerasa III en la hebra adelantada"), "ADN pol III: hebra adelantada",
              "La <b>ADN polimerasa III</b> alarga el cebador leyendo el molde 3′→5′ y sintetiza 5′→3′, en el mismo sentido en que avanza la horquilla: una sola pieza continua."))
    # 8 primasa (retrasada)
    b = (fork() + helicase() + topo() + leading() + pol3_lead() + lag_old() + ssb_top([350, 380, 452]) +
         N(E(415, NTOP + 34, 74, 38, "c4", "Primasa"), 0, 0, 40) + N(seg(400, 430, NTOP, "s-rna", True, .6), 0) +
         N(T(250, NTOP + 70, "hebra retrasada", "lab") + T(165, NTOP + 30, "fragmentos anteriores, ya unidos", "lab2"), 1))
    F.append((svg(b, "Primasa en la hebra retrasada"), "Hebra retrasada: un cebador nuevo",
              "El molde de arriba corre al revés: la síntesis 5′→3′ va <b>alejándose</b> de la horquilla. Por eso la primasa pone un cebador nuevo cada vez que se abre un tramo."))
    # 9 Pol III retrasada (Okazaki)
    b = (fork() + helicase() + topo() + leading() + pol3_lead() + lag_old() + ssb_top([452]) +
         seg(400, 430, NTOP, "s-rna") +
         O(f"<circle cx='350' cy='{TOPY}' r='9' class='ssb'/><circle cx='380' cy='{TOPY}' r='9' class='ssb'/>", .3, 0, -14) +
         path(f"M400 {NTOP} L302 {NTOP}", "s-new grow", False) .replace("class='s-new grow'", f"class='s-new grow' pathLength='1' style='{st(.3, t=1.6)}'") +
         N(ticks(300, 400, TOPY + 3, NTOP - 3), 1.6) +
         N(E(330, NTOP + 30, 74, 38, "c3", "Pol III"), .3, 90, 0, 1.6) +
         N(arrow(380, NTOP + 62, 310, NTOP + 62) + T(345, NTOP + 82, "fragmento de Okazaki", "lab"), 1.6))
    F.append((svg(b, "Fragmento de Okazaki"), "ADN pol III: fragmento de Okazaki",
              "Otra ADN polimerasa III alarga ese cebador hacia atrás hasta chocar con el fragmento anterior. Cada pedazo es un <b>fragmento de Okazaki</b>."))
    # 10 Pol I
    b = (fork() + helicase() + topo() + leading() + pol3_lead() + ssb_top([452]) +
         seg(60, 268, NTOP, "s-new") + ticks(60, 430, TOPY + 3, NTOP - 3) + T(52, NTOP + 5, "3′", "pol", "end") +
         seg(302, 400, NTOP, "s-new") + seg(400, 430, NTOP, "s-rna") +
         O(seg(270, 300, NTOP, "s-rna"), .5) +
         path(f"M302 {NTOP} L272 {NTOP}", "s-new").replace("class='s-new'", f"class='s-new grow' pathLength='1' style='{st(.7, t=1)}'") +
         N(E(286, NTOP + 34, 74, 38, "c5", "Pol I"), 0, 40, 0) +
         N(T(286, NTOP + 72, "saca el ARN y pone ADN", "lab2"), .9))
    F.append((svg(b, "ADN polimerasa I"), "ADN pol I: cambia ARN por ADN",
              "La <b>ADN polimerasa I</b> saca el cebador con su actividad <b>exonucleasa 5′→3′</b> y rellena el hueco con ADN. Queda una <b>mella</b>: falta un solo enlace."))
    # 11 ligasa
    b = (fork() + helicase() + topo() + leading() + pol3_lead() + ssb_top([452]) +
         seg(60, 267, NTOP, "s-new") + seg(273, 400, NTOP, "s-new") + seg(400, 430, NTOP, "s-rna") +
         ticks(60, 430, TOPY + 3, NTOP - 3) + T(52, NTOP + 5, "3′", "pol", "end") +
         P(f"<circle cx='270' cy='{NTOP}' r='13' class='hlbox'/>") +
         N(seg(265, 275, NTOP, "s-new"), 1.1) +
         N(E(270, NTOP + 36, 74, 38, "c6", "Ligasa"), .2, 0, 40) +
         N(T(270, NTOP + 76, "enlace fosfodiéster", "lab2"), 1.1))
    F.append((svg(b, "ADN ligasa"), "ADN ligasa: sella la mella",
              "La <b>ADN ligasa</b> forma el último <b>enlace fosfodiéster</b> entre los fragmentos y la hebra retrasada queda continua."))
    # 12 resultado
    def dup(y, new_top):
        a, c = ("s-new", "s-old") if new_top else ("s-old", "s-new")
        return seg(80, 720, y, a) + seg(80, 720, y + 30, c) + ticks(80, 720, y + 3, y + 27)
    b = (N(dup(110, False), 0, 0, 30) + N(dup(250, True), .2, 0, -30) +
         T(400, 92, "molécula hija 1", "lab") + T(400, 330, "molécula hija 2", "lab") +
         N(f"<line x1='250' y1='365' x2='280' y2='365' class='s-old'/>" + T(288, 370, "cadena vieja (molde)", "lab2", "start") +
           f"<line x1='470' y1='365' x2='500' y2='365' class='s-new'/>" + T(508, 370, "cadena nueva", "lab2", "start"), .8))
    F.append((svg(b, "Resultado semiconservativo"), "Resultado: replicación semiconservativa",
              "Cada molécula hija tiene una cadena vieja (el molde) y una nueva. Resumen del orden: helicasa → topoisomerasa → SSB → primasa → pol III → pol I → ligasa."))
    return F

# ================================================================ TRANSCRIPCIÓN
CY, MY = 175, 205   # codificante arriba, molde abajo

def gene(bubble=None, prom=True):
    """bubble=(x1,x2): zona abierta."""
    o = []
    if bubble:
        a, b_ = bubble
        o.append(path(f"M40 {CY} L{a} {CY} C{a+20} {CY} {a+20} 140 {a+40} 140 L{b_-40} 140 C{b_-20} 140 {b_-20} {CY} {b_} {CY} L760 {CY}", "s-old"))
        o.append(path(f"M40 {MY} L{a} {MY} C{a+20} {MY} {a+20} 240 {a+40} 240 L{b_-40} 240 C{b_-20} 240 {b_-20} {MY} {b_} {MY} L760 {MY}", "s-mold"))
        o.append(ticks(40, a, CY + 3, MY - 3) + ticks(b_, 760, CY + 3, MY - 3))
    else:
        o.append(seg(40, 760, CY, "s-old") + seg(40, 760, MY, "s-mold") + ticks(40, 760, CY + 3, MY - 3))
    o.append(T(30, CY + 5, "5′", "pol", "end") + T(30, MY + 5, "3′", "pol", "end") +
             T(770, CY + 5, "3′", "pol", "start") + T(770, MY + 5, "5′", "pol", "start"))
    if prom:
        o.append(f"<rect x='110' y='{CY-10}' width='100' height='{MY-CY+20}' rx='8' class='box1'/>")
        o.append(f"<rect x='610' y='{CY-10}' width='90' height='{MY-CY+20}' rx='8' class='box2'/>")
    return "".join(o)

def gene_labels():
    return (T(160, 228, "promotor", "lab2") + T(655, 228, "terminador", "lab2") +
            path("M230 214 L230 252 L262 252", "arr") + f"<polygon points='262,247 270,252 262,257' class='arrh'/>" + T(222, 272, "+1", "lab2"))

def rnap(x, w=170, sigma=False):
    o = [f"<g class='ez c3'><rect x='{x-w/2}' y='110' width='{w}' height='160' rx='60'/></g>",
         T(x, 105, "ARN polimerasa", "lab")]
    if sigma:
        o.append(f"<g class='ez c4'><ellipse cx='{x-w/2+10}' cy='252' rx='30' ry='22'/>{T(x-w/2+10, 258, 'σ', 'ez-t big')}</g>")
    return "".join(o)

def tr_frames():
    F = []
    lab_strands = T(400, 150, "cadena codificante", "lab2") + T(400, 236, "cadena molde", "lab2")
    # 1 gen
    b = gene() + gene_labels() + N(lab_strands, .2) + N(path("M230 120 L610 120", "s-dim") + T(420, 112, "zona que se va a transcribir", "lab2"), .6)
    F.append((svg(b, "Un gen"), "El gen",
              "Antes del gen está el <b>promotor</b> y al final el <b>terminador</b>. Solo una cadena se usa de <b>molde</b>; la otra se llama <b>codificante</b>."))
    # 2 holoenzima
    b = gene() + gene_labels() + N(rnap(185, sigma=True), 0, 0, -70, 1)
    F.append((svg(b, "Holoenzima en el promotor"), "La ARN polimerasa reconoce el promotor",
              "En bacterias hay una sola <b>ARN polimerasa</b>. Su subunidad <b>σ (sigma)</b> reconoce el promotor. En eucariotas eso lo hacen los <b>factores de transcripción</b>."))
    # 3 apertura
    b = (gene((190, 300)) + gene_labels() + rnap(245, sigma=True) +
         N(T(245, 300, "burbuja de transcripción", "lab2"), .5))
    F.append((svg(b, "Apertura"), "Se abre una burbuja",
              "La misma polimerasa separa unas pocas bases y deja expuesta la cadena molde. No necesita helicasa." + bib()))
    # 4 inicio sin cebador
    b = (gene((190, 300)) + gene_labels() + rnap(245, sigma=True) +
         N(seg(230, 262, 222, "s-rna", True, .2), 0) + N(T(222, 227, "5′", "pol", "end"), .8) +
         N("".join(T(x, 300, "NTP", "lab2") for x in (280, 320)) + arrow(320, 290, 285, 262, "arr"), .4) +
         N(T(245, 330, "sin cebador", "lab"), 1))
    F.append((svg(b, "Inicio"), "Arranca sin cebador",
              "Une los primeros ribonucleótidos (NTP) frente al +1. A diferencia de la ADN polimerasa, la ARN polimerasa <b>no necesita cebador</b>."))
    # 5 sigma se suelta
    b = (gene((190, 300)) + gene_labels() + rnap(245) + seg(230, 278, 222, "s-rna") +
         O(f"<g class='ez c4'><ellipse cx='170' cy='252' rx='30' ry='22'/>{T(170, 258, 'σ', 'ez-t big')}</g>", .3, -40, 80) +
         N(T(245, 330, "σ se va; sigue la enzima central", "lab2"), .8))
    F.append((svg(b, "Se suelta sigma"), "Se suelta σ",
              "Tras unir los primeros nucleótidos, <b>σ (sigma)</b> se suelta y la enzima central sigue sola." + bib("Detalle de bibliografía")))
    # 6 elongación
    rna6 = path("M500 222 L440 222 C410 222 400 160 360 90 L330 60", "s-rna")
    b = (gene((420, 530)) + gene_labels() + N(rnap(475), 0, -230, 0, 1.3) +
         N(rna6, .9) + N(T(322, 54, "5′", "pol", "end"), 1.2) +
         N(T(475, 300, "híbrido ARN-ADN", "lab2") + arrow(560, 330, 640, 330) + T(600, 352, "avanza", "lab2"), 1.2) +
         N(T(250, 300, "el ADN de atrás se vuelve a cerrar", "lab2"), 1.4))
    F.append((svg(b, "Elongación"), "Elongación",
              "La polimerasa lee el molde <b>3′→5′</b> y arma el ARN <b>5′→3′</b>, con U en lugar de T. Detrás de ella, el ADN se vuelve a cerrar."))
    # 7 terminación independiente de Rho
    hp = ("M600 222 L560 222 C530 222 525 180 520 160 L520 120 C520 98 548 98 548 120 L548 160 "
          "C548 175 560 175 560 160")
    rna7 = path("M600 222 L560 222 C520 222 500 170 470 120 L420 50", "s-rna")
    hp7 = path("M520 158 L520 120 C520 98 548 98 548 120 L548 160", "s-rna")
    b = (O(gene((590, 700)), 2.2, 0, 0, .5) + N(gene(), 2.2, 0, 0, .5) + gene_labels() +
         f"<g class='mv' style='{st(1.9, 30, -40, 1)}'>" + rnap(645) + rna7 + N(hp7, .2) + N(T(440, 150, "horquilla (rica en G-C) →", "lab2", "end"), .4) +
           N(T(560, 250, "U U U U", "seq sm rna"), .7) + "</g>" +
         N(T(400, 340, "la polimerasa y el ARN se sueltan", "lab2"), 2.4))
    F.append((svg(b, "Terminación independiente de Rho"), "Fin (1): independiente de Rho",
              "En el terminador, el ARN se pliega sobre sí mismo formando una <b>horquilla</b>. Eso traba a la polimerasa y el ARN se suelta."))
    # 8 terminación dependiente de Rho
    b = (gene((590, 700)) + gene_labels() + rnap(645) +
         path("M600 222 C520 222 500 170 470 120 L400 40", "s-rna") +
         N(E(460, 105, 62, 62, "c1", "Rho", "hex"), .1, -60, -60, 1.4) +
         N(arrow(420, 140, 500, 190), 1.3) +
         N(T(400, 60, "Rho corre por el ARN", "lab2", "end"), 1.4))
    F.append((svg(b, "Terminación dependiente de Rho"), "Fin (2): dependiente de Rho",
              "La proteína <b>Rho</b> se engancha al ARN, avanza hasta alcanzar a la polimerasa y la separa del molde."))
    # 9 producto (secuencias)
    def row(y, lab, s, cls):
        return T(160, y, lab, "lab", "end") + T(180, y, s, f"seq {cls}", "start")
    b = (row(130, "codificante", "5′- ATG GCT TGG TAA -3′", "") +
         row(180, "molde", "3′- TAC CGA ACC ATT -5′", "") +
         N(row(250, "ARNm", "5′- AUG GCU UGG UAA -3′", "rna"), .3) +
         N(T(400, 310, "el ARN es igual a la codificante, con U en lugar de T", "lab2"), .9) +
         N(arrow(350, 195, 350, 228), .2))
    F.append((svg(b, "Producto"), "El ARN copia a la cadena codificante",
              "El ARN es complementario al molde, así que queda <b>igual a la codificante</b>, solo que con U en lugar de T."))
    # 10 eucariotas: factores
    b = (gene(prom=False) + f"<rect x='150' y='{CY-10}' width='60' height='{MY-CY+20}' rx='8' class='box1'/>" + T(180, 158, "caja TATA", "lab2") +
         N(E(165, 252, 60, 40, "c6", "TF") + E(232, 252, 60, 40, "c6", "TF"), 0, 0, 50) +
         N(rnap(280, 150), .6, 0, -70) + N(T(400, 330, "factores de transcripción + ARN polimerasa II", "lab2"), 1.1))
    F.append((svg(b, "Eucariotas"), "En eucariotas",
              "Los <b>factores de transcripción</b> reconocen el promotor y reclutan a la ARN polimerasa (para ARNm, la II). El producto es un <b>pre-ARNm</b>." + bib("Pol II y caja TATA: bibliografía")))
    # 11-15 procesamiento
    exons = [(140, 250, "exón 1"), (330, 450, "exón 2"), (540, 660, "exón 3")]
    introns = [(250, 330), (450, 540)]
    def pre(cap=False, tail=False, introns_out=False):
        o = [seg(100, 700, 200, "s-rna thin")]
        for a, c, s in exons:
            o.append(f"<rect x='{a}' y='185' width='{c-a}' height='30' rx='6' class='exon'/>" + T((a + c) / 2, 205, s, "ez-t"))
        if not introns_out:
            for a, c in introns:
                o.append(f"<rect x='{a}' y='190' width='{c-a}' height='20' rx='5' class='intron'/>" + T((a + c) / 2, 240, "intrón", "lab2"))
        o.append(T(90, 205, "5′", "pol", "end") + T(710, 205, "3′", "pol", "start"))
        if cap: o.append(cap_g())
        if tail: o.append(tail_g())
        return "".join(o)
    def cap_g():
        return f"<g class='ez c4'><circle cx='82' cy='200' r='20'/>{T(82, 205, 'm⁷G', 'ez-t')}</g>"
    def tail_g():
        return T(712, 205, "AAAAAA…", "seq rna", "start")
    b = pre() + N(T(400, 140, "pre-ARNm = exones + intrones", "lab"), .3)
    F.append((svg(b, "pre-ARNm"), "Pre-ARNm", "El ARN recién hecho en eucariotas tiene <b>exones</b> (se quedan) e <b>intrones</b> (se van)."))
    b = pre().replace(T(90, 205, "5′", "pol", "end"), "") + N(cap_g(), 0, -40, -40) + N(T(82, 160, "cap 5′", "lab"), .7)
    F.append((svg(b, "Cap"), "Cap en el extremo 5′",
              "Al extremo 5′ se le agrega un <b>cap</b> de <b>7-metilguanosina</b>. Lo protege y sirve para que el ribosoma lo reconozca."))
    b = pre(cap=True).replace(T(710, 205, "3′", "pol", "start"), "") + N(tail_g(), .1, 40, 0) + N(T(760, 160, "cola de poli(A)", "lab", "end"), .7)
    F.append((svg(b, "Poli A"), "Cola de poli(A) en el 3′",
              "En el extremo 3′ se agrega una <b>cola de poli(A)</b>: muchas A seguidas, que estabilizan el ARNm."))
    loops = "".join(path(f"M{a} 200 C{a} 120 {c} 120 {c} 200", "s-rna loop") for a, c in introns)
    b = (pre(cap=True, tail=True).replace(T(710, 205, "3′", "pol", "start"), "") +
         N("<ellipse cx='290' cy='160' rx='70' ry='34' class='spl'/><ellipse cx='495' cy='160' rx='70' ry='34' class='spl'/>" +
           T(290, 166, "espliceosoma", "ez-t") + T(495, 166, "espliceosoma", "ez-t"), .1, 0, -40) +
         N(T(400, 290, "corta los intrones y une los exones", "lab2"), .8))
    F.append((svg(b, "Splicing"), "Splicing",
              "El <b>espliceosoma</b> (proteínas + ARNsn) corta los intrones y empalma los exones."))
    ex2 = [(160, 270, "exón 1"), (270, 390, "exón 2"), (390, 510, "exón 3")]
    b = (seg(110, 650, 200, "s-rna thin") + cap_g().replace("cx='82'", "cx='92'").replace("x='82'", "x='92'") +
         "".join(N(f"<rect x='{a}' y='185' width='{c-a}' height='30' rx='6' class='exon'/>" + T((a + c) / 2, 205, s, "ez-t"), .15 * i, 0, 0) for i, (a, c, s) in enumerate(ex2)) +
         T(652, 205, "AAAAAA…", "seq rna", "start") +
         T(135, 240, "5′UTR", "lab2") + T(580, 240, "3′UTR", "lab2") +
         N(T(400, 140, "ARNm maduro: listo para salir al citoplasma", "lab"), .6) +
         N(T(400, 300, "con splicing alternativo, un pre-ARNm da varias proteínas (isoformas)", "lab2"), 1))
    F.append((svg(b, "ARNm maduro"), "ARNm maduro",
              "Queda cap + exones + poli(A). Con <b>splicing alternativo</b>, un mismo pre-ARNm da distintos ARNm y distintas proteínas (isoformas)."))
    return F

# ================================================================ TRADUCCIÓN
X0, CW, MRY = 230, 70, 303
COD = ["AUG", "GCU", "UGG", "UAA"]

def cx(i): return X0 + CW * i + CW / 2

def mrna(hl=None):
    o = [seg(40, 760, MRY, "s-rna")]
    o.append(f"<rect x='95' y='{MRY-22}' width='80' height='20' rx='5' class='sd'/>" + T(135, MRY - 7, "AGGAGG", "seq sm"))
    for i, c in enumerate(COD):
        for j, ch in enumerate(c):
            o.append(T(cx(i) - 20 + 20 * j, MRY - 6, ch, "seq"))
        o.append(L(X0 + CW * i, MRY + 4, X0 + CW * i, MRY + 12, "cb"))
    o.append(L(X0 + CW * 4, MRY + 4, X0 + CW * 4, MRY + 12, "cb"))
    o.append(T(30, MRY + 5, "5′", "pol", "end") + T(770, MRY + 5, "3′", "pol", "start"))
    return "".join(o)

def small(Rx):
    return f"<g class='ez c2'><rect x='{Rx-125}' y='{MRY+8}' width='250' height='48' rx='22'/></g>"

def large(Rx, sites=True, ly=386):
    o = [f"<g class='ez c1'><rect x='{Rx-140}' y='70' width='280' height='210' rx='60'/></g>"]
    if sites:
        for k, s in zip((-1, 0, 1), "EPA"):
            x = Rx + CW * k
            o.append(f"<rect x='{x-31}' y='112' width='62' height='166' rx='12' class='slot'/>" + T(x, ly, s, "site"))
    return "".join(o)

def ribo(Rx):
    return small(Rx) + large(Rx)

AACOL = {"Met": "a1", "fMet": "a1", "Ala": "a2", "Trp": "a3"}

def trna(x, anti, aa=None, chain=()):
    o = [L(x, 156, x, 186, "tr-st"),
         f"<rect x='{x-24}' y='186' width='48' height='58' rx='16' class='tr'/>",
         f"<rect x='{x-29}' y='246' width='58' height='24' rx='6' class='tr'/>"]
    for j, ch in enumerate(anti):
        o.append(T(x - 18 + 18 * j, 264, ch, "seq sm"))
    o.append("".join(L(x - 18 + 18 * j, 272, x - 18 + 18 * j, 281, "bp") for j in range(3)))
    if aa:
        pts = [(x, 140)]
        for k in range(1, len(chain) + 1):
            pts.append((x, 140 - 36 * k))
        names = [aa] + list(reversed(chain))
        for k in range(len(pts) - 1):
            o.append(L(*pts[k], *pts[k + 1], "pep"))
        for (px, py), nm in zip(pts, names):
            o.append(f"<circle cx='{px}' cy='{py}' r='17' class='aa {AACOL.get(nm, 'a2')}'/>" + T(px, py + 4, nm, "aa-t"))
    return "".join(o)

def tl_frames():
    F = []
    # 1 ARNm
    b = (mrna() + N(T(135, MRY - 34, "Shine-Dalgarno", "lab2"), .2) +
         N("".join(f"<rect x='{X0+CW*i+3}' y='{MRY-26}' width='{CW-6}' height='34' rx='8' class='{'hlbox' if i in (0,3) else 'codon'}'/>" for i in range(4)), .3) +
         N(T(cx(0), MRY + 36, "inicio", "lab") + T(cx(3), MRY + 36, "stop", "lab") + T(cx(1.5), MRY + 36, "codones", "lab2"), .6) +
         N(T(400, 160, "se lee de a 3 bases (codones), 5′→3′", "lab"), 1))
    F.append((svg(b, "ARNm"), "El mensaje: codones",
              "El ARNm se lee de a <b>3 bases (codones)</b>, de 5′ a 3′. Empieza en <b>AUG</b> y termina en un <b>stop</b> (UAA, UAG o UGA). Este ejemplo da Met–Ala–Trp."))
    # 2 activación
    b = (N(E(400, 200, 200, 110, "c5", "aminoacil-ARNt|sintetasa"), 0, 0, 0) +
         N(f"<circle cx='190' cy='140' r='18' class='aa a2'/>" + T(190, 144, "Ala", "aa-t") + T(190, 110, "aminoácido", "lab2"), .2, -40) +
         N(T(190, 272, "ATP", "lab") , .4, -40) +
         N(trna(620, "CGA", "Ala").replace("y='186'", "y='186'"), 1.2, 0, 30) +
         N(T(620, 300, "aminoacil-ARNt", "lab") + T(620, 322, "+ AMP + PPi", "lab2"), 1.5) +
         N(arrow(510, 200, 570, 200), 1))
    F.append((svg(b, "Activación"), "Activación del aminoácido",
              "Una <b>aminoacil-ARNt sintetasa</b> por cada aminoácido lo carga en el extremo 3′ de su ARNt, gastando <b>ATP</b>. Cada ARNt lleva un solo aminoácido."))
    # 3 subunidades
    b = (N(large(560, ly=104), 0, 0, -30) + N(small(200).replace(f"y='{MRY+8}'", "y='240'"), .2, 0, 30) +
         N(T(200, 225, "subunidad menor", "lab") + T(200, 312, "30S bacterias · 40S eucariotas", "lab2") +
           T(560, 300, "subunidad mayor", "lab") + T(560, 322, "50S bacterias · 60S eucariotas", "lab2"), .5) +
         N(T(470, 60, "A: entra el aminoacil-ARNt · P: peptidil-ARNt · E: salida", "lab2"), .9))
    F.append((svg(b, "Subunidades"), "El ribosoma y sus sitios",
              "Dos subunidades de ARNr + proteínas. En la mayor hay 3 sitios: <b>A</b> (aminoacil, entra el ARNt cargado), <b>P</b> (peptidil, el que sostiene la cadena) y <b>E</b> (salida)."))
    # 4 iniciación 1
    Rx = cx(0)
    b = (mrna() + N(small(Rx), 0, -60, 40, 1.2) + N(E(Rx + 170, MRY + 32, 60, 30, "c6", "IF"), .6, 0, 30) +
         N(T(135, MRY - 52, "se guía por Shine-Dalgarno", "lab2") + T(135, MRY - 34, "(eucariotas: por el cap)", "lab2"), 1.1))
    F.append((svg(b, "Iniciación 1"), "Iniciación (1): subunidad menor",
              "La <b>subunidad menor</b> se pega al ARNm y se ubica en el AUG: en bacterias, guiada por la secuencia <b>Shine-Dalgarno</b>; en eucariotas, por el <b>cap</b>. La ayudan factores de iniciación (IF)." + bib("Factores IF: bibliografía")))
    # 5 iniciación 2
    b = (mrna() + small(Rx) + f"<rect x='{Rx-31}' y='112' width='62' height='166' rx='12' class='slot dash'/>" + T(Rx, 104, "P", "site") +
         N(trna(Rx, "UAC", "fMet"), .1, 0, -80, 1.1) +
         N(T(Rx + 60, 205, "ARNt iniciador", "lab", "start") + T(Rx + 60, 225, "fMet en bacterias · Met en eucariotas", "lab2", "start") +
           T(Rx + 60, 262, "anticodón UAC ↔ AUG", "lab2", "start"), 1.2))
    F.append((svg(b, "Iniciación 2"), "Iniciación (2): ARNt iniciador en P",
              "El ARNt iniciador, con anticodón <b>UAC</b>, se aparea con <b>AUG</b>. Lleva <b>fMet</b> en bacterias y <b>Met</b> en eucariotas, y es el único que entra directo al sitio <b>P</b>."))
    # 6 iniciación 3
    b = (mrna() + small(Rx) + N(large(Rx), 0, 0, -90, 1.1) + trna(Rx, "UAC", "fMet") +
         N(T(Rx + 175, 180, "ribosoma armado", "lab", "start") + T(Rx + 175, 200, "(gasta GTP)", "lab2", "start"), 1.1))
    F.append((svg(b, "Iniciación 3"), "Iniciación (3): llega la subunidad mayor",
              "Se une la <b>subunidad mayor</b> y queda el ribosoma completo: fMet-ARNt en P, sitio A libre frente al codón GCU."))
    # 7 entrada al A
    b = (mrna() + ribo(Rx) + trna(Rx, "UAC", "fMet") +
         N(trna(Rx + CW, "CGA", "Ala"), .1, 0, -110, 1.1) +
         N(E(Rx + CW + 70, 60, 74, 30, "c6", "EF-Tu"), .1, 0, -110, 1.1) +
         N(T(Rx + CW + 115, 250, "GCU ↔ CGA", "lab2", "start"), 1.2))
    F.append((svg(b, "Entrada al sitio A"), "Elongación (1): entra al sitio A",
              "Entra al sitio <b>A</b> el aminoacil-ARNt cuyo anticodón (CGA) se aparea con el codón (GCU). Lo trae un factor de elongación con GTP." + bib("EF-Tu: bibliografía")))
    # 8 enlace peptídico
    b = (mrna() + ribo(Rx) + trna(Rx, "UAC") + trna(Rx + CW, "CGA") +
         f"<circle cx='{Rx+CW}' cy='140' r='17' class='aa a2'/>" + T(Rx + CW, 144, "Ala", "aa-t") +
         N(L(Rx + CW, 140, Rx + CW, 104, "pep") + f"<circle cx='{Rx+CW}' cy='104' r='17' class='aa a1'/>" + T(Rx + CW, 108, "fMet", "aa-t"), .3, -70, 36, 1.1) +
         N(T(Rx + CW + 60, 60, "peptidil transferasa (ARNr)", "lab", "start") + T(Rx + CW + 60, 80, "enlace peptídico", "lab2", "start"), .9))
    F.append((svg(b, "Enlace peptídico"), "Elongación (2): enlace peptídico",
              "La <b>peptidil transferasa</b> pasa la cadena del ARNt de P al aminoácido de A y forma el <b>enlace peptídico</b>. Es un ARNr de la subunidad mayor (una ribozima)."))
    # 9 translocación
    R2 = Rx + CW
    b = (mrna() + N(ribo(R2), 0, -CW, 0, 1.2) + trna(Rx, "UAC") + trna(R2, "CGA", "Ala", ("fMet",)) +
         N(E(R2 + CW + 70, 60, 74, 30, "c6", "EF-G"), 0, 0, -50) +
         N(arrow(R2 - 40, 40, R2 + 40, 40) + T(R2 - 50, 45, "avanza 1 codón (GTP)", "lab2", "end"), .9))
    F.append((svg(b, "Translocación"), "Elongación (3): translocación",
              "El ribosoma avanza <b>un codón</b> hacia 3′, gastando GTP. El ARNt vacío queda en <b>E</b>, el que lleva la cadena en <b>P</b>, y <b>A</b> queda libre." + bib("EF-G: bibliografía")))
    # 10 sale por E y entra el siguiente
    b = (mrna() + ribo(R2) + O(trna(Rx, "UAC"), .2, 0, -120) + trna(R2, "CGA", "Ala", ("fMet",)) +
         N(trna(R2 + CW, "ACC", "Trp"), 1, 0, -110, 1.1) +
         N(T(Rx - 40, 60, "sale por E", "lab2", "end"), .3))
    F.append((svg(b, "Sale por E"), "Sale el ARNt vacío y entra el siguiente",
              "El ARNt vacío sale por <b>E</b>. Entra Trp-ARNt (anticodón ACC ↔ UGG) al sitio A y el ciclo se repite."))
    # 11 tras otro ciclo
    R3 = R2 + CW
    b = (mrna() + N(ribo(R3), 0, -CW, 0, 1.2) + trna(R2, "CGA") + trna(R3, "ACC", "Trp", ("fMet", "Ala")) +
         N(P(f"<rect x='{R3+CW-31}' y='{MRY-26}' width='62' height='34' rx='8' class='hlbox'/>"), 1.1) +
         N(T(R3 + 152, 200, "UAA = stop", "lab", "start"), 1.2) +
         N(T(R3 - 150, 60, "la cadena crece", "lab2", "end") + T(R3 - 150, 78, "de N- a C-terminal", "lab2", "end"), .8))
    F.append((svg(b, "Otro ciclo"), "Otro ciclo: llega el stop",
              "Tras otro enlace y otra translocación, la cadena fMet–Ala–Trp está en P y el sitio A queda frente a <b>UAA</b>: no hay ningún ARNt para ese codón."))
    # 12 terminación
    rf = (f"<g class='ez c4'><rect x='{R3+CW-24}' y='150' width='48' height='120' rx='16'/>{T(R3+CW, 214, 'RF', 'ez-t')}</g>")
    b = (mrna() + ribo(R3) + trna(R3, "ACC") +
         O(L(R3, 140, R3, 68, "pep") +
           f"<circle cx='{R3}' cy='68' r='17' class='aa a1'/>" + T(R3, 72, "fMet", "aa-t") +
           f"<circle cx='{R3}' cy='104' r='17' class='aa a2'/>" + T(R3, 108, "Ala", "aa-t") +
           f"<circle cx='{R3}' cy='140' r='17' class='aa a3'/>" + T(R3, 144, "Trp", "aa-t"), 1.3, -60, -110, 1.2) +
         N(rf, 0, 0, -100, 1) + N(T(R3 + 152, 200, "factor de liberación", "lab", "start"), .6) +
         N(T(R3 - 160, 40, "la proteína se suelta", "lab2"), 1.6))
    F.append((svg(b, "Terminación"), "Terminación",
              "En el stop entra un <b>factor de liberación</b> (no un ARNt). Se corta la unión entre la cadena y el último ARNt, y la proteína se suelta."))
    # 13 disociación
    b = (mrna() + O(small(R3), .2, 40, 60) + O(large(R3, False), .2, 40, -80) + O(trna(R3, "ACC"), .2, 0, -100) +
         N("".join(f"<circle cx='{x}' cy='{y}' r='17' class='aa {c}'/>" + T(x, y + 4, n, "aa-t") for x, y, n, c in ((300, 140, "fMet", "a1"), (340, 160, "Ala", "a2"), (380, 140, "Trp", "a3"))) +
           L(317, 148, 323, 152, "pep") + L(357, 152, 363, 148, "pep"), 1, 0, 40) +
         N(T(340, 100, "proteína → modificaciones postraduccionales", "lab"), 1.4))
    F.append((svg(b, "Disociación"), "Se separa todo",
              "Las subunidades se separan y se pueden reutilizar. Después vienen las <b>modificaciones postraduccionales</b>, distintas en eucariotas y procariotas."))
    return F

# ================================================================ player HTML
def player(key, title, frames):
    st_ = "".join(f.replace("class='fr'", "class='fr on'", 1) if i == 0 else f for i, (f, _, _) in enumerate(frames))
    caps = "".join(f"<div class='an-cap{' on' if i == 0 else ''}'><h4><span class='n'>{i+1}</span>{t}</h4><p>{d}</p></div>"
                   for i, (_, t, d) in enumerate(frames))
    bar = "".join(f"<button type='button' data-i='{i}' aria-label='Paso {i+1}'><i></i></button>" for i in range(len(frames)))
    return (f"<!--ANIM:{key}--><div class='anim' data-anim='{key}'>"
            f"<div class='an-top'><span class='an-ttl'>▶ {title}, paso a paso</span><span class='an-ct'>1 / {len(frames)}</span></div>"
            f"<div class='an-stage'>{st_}</div>"
            f"<div class='an-bar'>{bar}</div>"
            f"<div class='an-caps'>{caps}</div>"
            f"<div class='an-ctl'><button type='button' data-a='prev' aria-label='Anterior'>‹</button>"
            f"<button type='button' data-a='play' class='an-play'>▶ Reproducir</button>"
            f"<button type='button' data-a='next' aria-label='Siguiente'>›</button>"
            f"<button type='button' data-a='speed' class='an-sp'>Velocidad: normal</button></div>"
            f"</div><!--/ANIM:{key}-->\n")

if __name__ == "__main__":
    s = open("t_n.html").read()
    s = re.sub(r"<!--ANIM:(\w+)-->.*?<!--/ANIM:\1-->\n?", "", s, flags=re.S)
    blocks = [("<h2>3. Transcripción</h2>", player("rep", "Replicación", rep_frames())),
              ("<h2>4. Traducción</h2>", player("tr", "Transcripción", tr_frames())),
              ("<h2>5. Metabolismo de nucleótidos</h2>", player("tl", "Traducción", tl_frames()))]
    for anchor, html in blocks:
        assert s.count(anchor) == 1, anchor
        s = s.replace(anchor, html + anchor)
    open("t_n.html", "w").write(s)
    print("ok", [len(f()) for f in (rep_frames, tr_frames, tl_frames)])
