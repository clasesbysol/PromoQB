# Videos "con diálogo" para AN II simple §5. Se insertan en t_n2s.html (correr después de n2s.py).
import math, re
from anim import N, O, P, T, L, path, arrow, player
from metab import (blob, small, enzyme, atom, ribose, rib_pts, rib_under, pur_pos, pyr_pos, PYR_B,
                   ring_atoms, pur_char, pyr_char, stop, note, subst, badge, face, battery, swap)

# ------------------------------------------------------------------ globitos
def say(x, y, text, to, d=0.4, cls="bub"):
    """globito con esquina sup-izq (x,y); 'to' = punto de quien habla"""
    lines = text.split("|")
    w = max(len(l) for l in lines) * 7.5 + 26
    h = len(lines) * 18 + 16
    tx, ty = to
    cx = min(max(tx, x + 18), x + w - 18)
    if ty > y + h:      bx, by, sx, sy = cx, y + h, 9, 0
    elif ty < y:        bx, by, sx, sy = cx, y, 9, 0
    elif tx < x:        bx, by, sx, sy = x, y + h / 2, 0, 8
    else:               bx, by, sx, sy = x + w, y + h / 2, 0, 8
    tail = f"<polygon points='{bx-sx:.1f},{by-sy:.1f} {bx+sx:.1f},{by+sy:.1f} {tx:.1f},{ty:.1f}' class='{cls}-t'/>"
    body = (f"<rect x='{x}' y='{y}' width='{w:.0f}' height='{h}' rx='14' class='{cls}'/>" + tail +
            f"<line x1='{bx-sx*0.8:.1f}' y1='{by-sy*0.8:.1f}' x2='{bx+sx*0.8:.1f}' y2='{by+sy*0.8:.1f}' class='{cls}-c'/>" +
            "".join(T(round(x + w / 2, 1), y + 22 + 18 * i, l, "bub-x") for i, l in enumerate(lines)))
    return N(body, d, 0, 8, .45)

def frame(body, label, title, desc, nb):
    dur = int((0.6 + 1.9 * nb + 3.6) * 1000)
    return (f"<svg class='fr' data-dur='{dur}' viewBox='0 0 800 400' role='img' aria-label='{label}'>{body}</svg>", title, desc)

def D(i): return round(0.5 + 1.9 * i, 2)

def sign(x, y, t1, t2, k="sg1"):
    w = max(len(t1), len(t2)) * 7.6 + 30
    return (f"<rect x='{x-w/2:.0f}' y='{y-24}' width='{w:.0f}' height='52' rx='12' class='{k}'/>" +
            T(x, y - 3, t1, "sg-t") + T(x, y + 17, t2, "lab2"))

def helix(x, y, w=150, lab="ADN"):
    a = f"M{x} {y} " + " ".join(f"Q{x+i*25+12.5} {y-18 if i%2==0 else y+18} {x+(i+1)*25} {y}" for i in range(int(w/25)))
    b = f"M{x} {y} " + " ".join(f"Q{x+i*25+12.5} {y+18 if i%2==0 else y-18} {x+(i+1)*25} {y}" for i in range(int(w/25)))
    return path(a, "s-old") + path(b, "s-new") + T(x + w / 2, y + 42, lab, "lab")

def scissors(x, y):
    return (f"<g class='sci'><circle cx='{x-10}' cy='{y+18}' r='11'/><circle cx='{x+10}' cy='{y+18}' r='11'/>"
            f"<line x1='{x-10}' y1='{y+7}' x2='{x+22}' y2='{y-38}'/><line x1='{x+10}' y1='{y+7}' x2='{x-22}' y2='{y-38}'/></g>" + face(x, y - 12, .7))

def kidney(x, y):
    return (f"<path d='M{x-20} {y-60} C{x+50} {y-70} {x+60} {y+60} {x-10} {y+60} C{x-60} {y+60} {x-40} {y+15} {x-20} {y+5} "
            f"C{x-5} {y-5} {x-5} {y-25} {x-30} {y-30} C{x-60} {y-40} {x-50} {y-58} {x-20} {y-60}Z' class='kid'/>" + face(x + 15, y, .9))

def toe(x, y):
    return (f"<path d='M{x} {y+60} C{x} {y} {x+45} {y-28} {x+105} {y-20} C{x+170} {y-12} {x+205} {y+10} {x+230} {y+24} "
            f"C{x+256} {y+40} {x+254} {y+77} {x+230} {y+82} L{x+18} {y+82} C{x+4} {y+82} {x} {y+74} {x} {y+60}Z' class='toe'/>" +
            f"<circle cx='{x+190}' cy='{y+32}' r='30' class='joint'/>" + face(x + 80, y + 30, .9, "sad"))

def xtals(x, y):
    return "".join(f"<line x1='{x+dx}' y1='{y+dy}' x2='{x+dx+10}' y2='{y+dy-8}' class='xtal'/>" for dx, dy in ((0, 0), (12, 5), (5, 15), (17, 17), (-6, 12)))

def nuc(x, y, k="k-imp", subs=(("C6", "O"),), rib=None, name=None, mood="smile", R=28, look=0):
    return pur_char(x, y, k, list(subs), R=R, rib=rib, name=name, mood=mood, look=look)

# ================================================================== VIDEO 1: de novo y rescate
def v_rescate():
    F = []
    b = (enzyme(400, 270, "ADN polimerasa") + say(255, 120, "¡Necesito nucleótidos para|copiar el ADN y hacer ARN!", (400, 245), D(0)) +
         N(sign(150, 70, "DE NOVO", "fabricarlos desde cero") + sign(650, 70, "RECUPERACIÓN", "reciclar lo que ya hay", "sg2"), D(1)) +
         say(480, 250, "Hay dos caminos.", (432, 262), D(1) + .6))
    F.append(frame(b, "Dos caminos", "La célula necesita nucleótidos", "Para copiar el ADN y fabricar ARN hacen falta nucleótidos. Hay dos maneras de conseguirlos: <b>de novo</b> (fabricarlos desde cero) o por <b>recuperación</b> (reciclar bases que ya existen).", 2))
    ing = [(100, "k-gln", "glutamina", "Yo traigo N", 150), (250, "k-asp", "aspartato", "Yo también, N", 205),
           (400, "k-gly", "glicina", "¡Yo entro entera!", 150), (550, "k-thf", "THF", "Yo, carbonos|sueltos", 205), (700, "k-co2", "CO₂", "Yo pongo|un C", 150)]
    b = badge("De novo: desde cero")
    for i, (x, k, n, t, by) in enumerate(ing):
        b += blob(x, 320, k, n, r=24)
        w = max(len(l) for l in t.split("|")) * 7.5 + 26
        b += say(round(x - w / 2), by - (18 if "|" in t else 0), t, (x, 294), D(i) * .55 + .3)
    b += N(T(400, 60, "Con ingredientes simples se arma la base del nucleótido.", "lab"), 3.4)
    F.append(frame(b, "De novo", "De novo: los ingredientes", "En la vía <b>de novo</b> el nucleótido se fabrica desde cero con moléculas simples: aminoácidos (glutamina, aspartato, glicina), THF (tetrahidrofolato, de la vitamina B9) y CO₂.", 3))
    b = (badge("Citosol") + ribose(400, 270, p5=1, pp1=True, r=40) + face(400, 262, .9) + T(400, 335, "PRPP", "lab") +
         say(150, 70, "Soy el PRPP: una ribosa-5-P|con un pirofosfato (PP).", (385, 230), D(0)) +
         say(420, 120, "Le doy la ribosa-fosfato a TODOS|los nucleótidos: de novo y reciclados.", (420, 228), D(1)))
    F.append(frame(b, "PRPP", "El dador de ribosa", "El <b>PRPP</b> (5-fosforribosil-1-pirofosfato) es una ribosa-5-fosfato «activada». Es el que <b>da la ribosa-fosfato a todos los nucleótidos</b>, en las dos vías.", 2))
    plate = ("<ellipse cx='120' cy='300' rx='85' ry='26' class='plate'/>" + blob(95, 280, "k-enz3", r=18) + blob(140, 284, "k-xan", r=16) + T(120, 352, "comida", "lab"))
    b = (badge("Intestino") + plate + scissors(400, 230) + T(400, 285, "nucleasas", "enz-n") +
         say(250, 80, "Corto los ácidos nucleicos|de la comida.", (395, 190), D(0)) +
         N(nuc(620, 250, R=22) + nuc(700, 300, "k-amp", (("C6", "NH₂"),), R=20), D(1) - .3, -80) +
         say(540, 110, "¡Nos soltaron!|Somos bases libres.", (630, 220), D(1)) +
         N(T(400, 385, "Esta es la ruta principal de importación de bases.", "lab"), D(2)))
    F.append(frame(b, "Dieta", "Recuperación (1): de la dieta", "Al digerir la comida se rompen sus ácidos nucleicos y quedan <b>bases libres</b>. Esa digestión (hidrólisis extracelular) es la <b>ruta principal de importación</b> de bases y nucleótidos.", 2))
    rna = path("M90 260 C120 230 150 290 180 260 C210 230 240 290 270 260", "s-rna") + face(180, 240, .8, "sad")
    b = (badge("Dentro de la célula") + rna + T(180, 320, "un ARN viejo", "lab") +
         say(70, 110, "Ya cumplí mi función…|me van a desarmar.", (180, 235), D(0)) +
         N(arrow(300, 260, 420, 260), D(1) - .4) +
         N(nuc(500, 250, R=22) + nuc(600, 290, "k-ump", (("C6", "O"),), R=20) + pyr_char(690, 240, "k-ump", [("C2", "O"), ("C4", "O")], R=20), D(1) - .3, -60) +
         say(470, 100, "Y nosotras quedamos libres|para que nos reciclen.", (560, 220), D(1)))
    F.append(frame(b, "Recambio", "Recuperación (2): de adentro", "Las bases también salen de la <b>degradación de los ácidos nucleicos de la propia célula</b>, por ejemplo de ARN que ya cumplieron su función.", 2))
    b = (badge("Citosol") + nuc(130, 170, R=26) + T(140, 240, "base libre", "lab") +
         ribose(660, 175, p5=1, pp1=True) + face(660, 172, .6) + T(660, 222, "PRPP", "lab") +
         enzyme(400, 90, "HGPRT") +
         say(40, 40, "Sola no sirvo: me falta|la ribosa-fosfato.", (130, 135), D(0)) +
         say(560, 40, "¡Te la doy yo!", (650, 150), D(1)) +
         say(450, 150, "Yo los junto.", (420, 105), D(2)) +
         N(nuc(400, 260, R=24, rib={"p5": 1}), D(3) - .4, 0, -30) +
         say(470, 300, "¡Reciclado! Mucho más barato|que fabricarme de cero.", (430, 270), D(3)))
    F.append(frame(b, "Rescate", "Recuperación (3): se recicla", "En el rescate, a la base libre se le pega la ribosa-fosfato del <b>PRPP</b>. Para la hipoxantina y la guanina lo hace la enzima <b>HGPRT</b>. Sale un nucleótido nuevo, mucho más barato que fabricarlo de cero.", 4))
    b = (N(nuc(200, 110, R=24), 0) + N(arrow(200, 165, 200, 215), .3) +
         N(blob(200, 275, "k-uri", "ácido úrico", r=24, mood="flat"), D(1) - .4) +
         say(20, 20, "Si nadie me recicla…", (180, 85), D(0)) +
         say(250, 250, "Las purinas terminamos|como ácido úrico.", (225, 270), D(1)) +
         N(pyr_char(600, 110, "k-ump", [("C2", "O"), ("C4", "O")], R=24) + arrow(600, 160, 600, 215), D(2) - .4) +
         N(blob(600, 275, "k-xmp", "β-ureidopropionato", r=24, mood="flat"), D(2) - .2) +
         say(560, 210, "Y las pirimidinas,|como β-ureidopropionato.", (622, 262), D(2)))
    F.append(frame(b, "Degradación", "Si no se reciclan, se degradan", "Las bases que no se reutilizan se degradan: las <b>purinas</b> terminan en <b>ácido úrico</b> y las <b>pirimidinas</b> en <b>β-ureidopropionato</b>.", 3))
    return F

# ================================================================== VIDEO 2: purinas vs pirimidinas, hipoxantina, regulación
def v_estrategias():
    F = []
    pp = pur_pos(410, 170, 32)
    src = {"N9": "q-gln", "C4": "q-gly", "C5": "q-gly", "N7": "q-gly", "C8": "q-for", "N3": "q-gln", "C6": "q-co2", "N1": "q-asp", "C2": "q-for"}
    rc = rib_under(*pp["N9"], 24, 26); c1 = rib_pts(*rc)["C1"]
    order = ["N9", "C4", "C5", "N7", "C8", "N3", "C6", "N1", "C2"]
    atoms = "".join(N(atom(*pp[a], a, src[a], 13), .8 + .25 * i, 0, -40, .5) for i, a in enumerate(order))
    bonds = N("".join(L(*pp[a], *pp[b], "rbond") for a, b in [("C6", "N1"), ("N1", "C2"), ("C2", "N3"), ("N3", "C4"), ("C4", "C5"), ("C5", "C6"), ("C5", "N7"), ("N7", "C8"), ("C8", "N9"), ("N9", "C4")]), 3.2)
    b = (badge("Purinas (A y G)") + L(*pp["N9"], *c1, "bond") + ribose(*rc, p5=1) + bonds + atoms +
         say(40, 260, "En las purinas yo estoy desde|el principio: ¡armen el anillo|encima mío!", (rc[0] - 10, rc[1] + 8), D(0) + 3) +
         say(560, 80, "Cada uno pone|sus átomos.", (470, 150), D(1) + 3))
    F.append(frame(b, "Purinas", "Purinas: el anillo se arma encima", "En las <b>purinas</b>, la ribosa-fosfato del PRPP está <b>desde el principio</b> y el anillo se arma encima, átomo por átomo. Los colores son de quien trae cada átomo: aminoácidos, THF y CO₂.", 2))
    b = (nuc(400, 150, R=34, rib={"p5": 1}) +
         say(470, 40, "¡Nací! Soy el IMP (inosinato).|Mi base se llama HIPOXANTINA.", (430, 110), D(0)) +
         N(nuc(130, 230, "k-amp", (("C6", "NH₂"),), R=24, rib={"p5": 1}, name="AMP") + nuc(680, 230, "k-gua", (("C6", "O"), ("C2", "NH₂")), R=24, rib={"p5": 1}, name="GMP"), D(1) - .3) +
         N(arrow(340, 200, 200, 230) + arrow(470, 200, 610, 230), D(1) - .3) +
         say(250, 320, "De mí salen el AMP y el GMP.", (390, 290), D(1)))
    F.append(frame(b, "IMP", "Nace el IMP: su base es la hipoxantina", "El primer nucleótido de purina que se forma es el <b>IMP</b> (inosinato). Su base se llama <b>hipoxantina</b>. Del IMP salen el AMP y el GMP.", 2))
    yp = pyr_pos(400, 190, 40)
    ysrc = {"C2": "q-co2", "N3": "q-gln", "N1": "q-asp", "C6": "q-asp", "C5": "q-asp", "C4": "q-asp"}
    b = (badge("Pirimidinas (C, U y T)") + blob(110, 260, "k-co2", "carbamoil fosfato", r=24) + blob(110, 130, "k-asp", "aspartato", r=24) +
         say(150, 215, "Armamos el anillo|solos, sin ribosa.", (132, 255), D(0)) +
         say(150, 30, "¡Dale! Yo pongo|casi todo.", (125, 110), D(1)) +
         N(ring_atoms(yp, set(ysrc), ysrc, bonds=PYR_B), D(1) + .6) +
         N(ribose(680, 260, p5=1, pp1=True) + face(680, 257, .6) + T(680, 308, "PRPP", "lab"), D(2) - .3, 80) +
         say(560, 120, "¿Ahora sí me necesitan?", (670, 230), D(2)) +
         say(470, 330, "¡Sí! Ahora dame la ribosa-fosfato.", (440, 230), D(3)))
    F.append(frame(b, "Pirimidinas", "Pirimidinas: anillo primero, ribosa después", "En las <b>pirimidinas</b> el anillo se arma <b>por separado</b>, con carbamoil fosfato y aspartato (es más simple). Recién después toma la ribosa-fosfato del <b>PRPP</b>.", 4))
    b = (f"<rect x='14' y='14' width='378' height='372' rx='18' class='pan'/><rect x='408' y='14' width='378' height='372' rx='18' class='pan'/>" +
         T(203, 48, "PURINAS", "ttl-a") + T(597, 48, "PIRIMIDINAS", "ttl-b") +
         ribose(150, 290, p5=1) + face(150, 288, .55) + N(nuc(240, 170, R=26), .6, 0, -40) + T(150, 340, "1° ribosa", "lab") + T(260, 260, "2° anillo encima", "lab") +
         pyr_char(530, 160, "k-ump", [("C2", "O"), ("C4", "O")], R=28) + T(530, 230, "1° anillo", "lab") +
         N(ribose(690, 290, p5=1) + face(690, 288, .55) + T(690, 340, "2° ribosa", "lab"), 1, 60) +
         say(40, 70, "Yo llego al principio.", (140, 268), D(1)) +
         say(560, 70, "Yo llego al final.", (680, 268), D(2)))
    F.append(frame(b, "Comparación", "Para no confundirse", "<b>Purinas</b>: primero la ribosa y el anillo se arma encima. <b>Pirimidinas</b>: primero el anillo y la ribosa se pega al final.", 2))
    b = (enzyme(170, 250, "enzima del|1.er paso") +
         nuc(450, 110, R=22, name=None) + T(450, 160, "IMP", "lab") +
         nuc(560, 220, "k-amp", (("C6", "NH₂"),), R=22) + T(560, 270, "AMP", "lab") +
         nuc(680, 120, "k-gua", (("C6", "O"), ("C2", "NH₂")), R=22) + T(680, 170, "GMP", "lab") +
         say(605, 240, "¡Ya somos un montón!", (585, 222), D(0)) +
         say(560, 20, "¡Frená!", (660, 95), D(1)) +
         say(40, 70, "Ok, freno.|(retroinhibición)", (170, 225), D(2)) +
         N(stop(125, 340, "producto final frena el 1.er paso", "start"), D(2) + .6))
    F.append(frame(b, "Regulación", "Cómo se regula: retroinhibición", "Cuando hay suficiente IMP, AMP y GMP, ellos mismos <b>frenan la enzima del primer paso</b> de su síntesis. Eso es la <b>retroinhibición</b>.", 3))
    b = (nuc(200, 180, "k-amp", (("C6", "NH₂"),), R=30, rib={"p5": 1}, name="AMP") + nuc(600, 180, "k-gua", (("C6", "O"), ("C2", "NH₂")), R=30, rib={"p5": 1}, name="GMP") +
         say(40, 20, "Para hacerme a mí|se gasta GTP.", (190, 140), D(0)) + say(500, 20, "Y para mí, ATP.", (590, 140), D(1)) +
         N(battery(320, 300, "GTP") + battery(480, 300, "ATP"), D(1)) +
         N(note(400, 365, "si sobra G se fabrica más A, y al revés: quedan equilibrados", "lab"), D(2)))
    F.append(frame(b, "Equilibrio", "Cada uno gasta la moneda del otro", "Para hacer AMP se gasta <b>GTP</b> y para hacer GMP se gasta <b>ATP</b>. Así, si sobra uno se fabrica más del otro, y A y G quedan equilibrados.", 2))
    return F

# ================================================================== VIDEO 3: desoxi, dTMP, 5-FU, T y U
def v_desoxi():
    F = []
    hx = helix(560, 120, 175, "ADN")
    b = (nuc(140, 190, "k-gen", (), R=30, rib={"p5": 2, "hl2": True}, name="ADP (ribo)") + hx +
         N(T(648, 200, "solo entran desoxi", "stp-t"), .2) +
         say(270, 200, "Así como estoy no puedo entrar|al ADN: tengo un OH en el 2′.", (200, 270), D(0)) +
         say(270, 300, "Alguien me tiene que sacar el OH.", (205, 290), D(1)))
    F.append(frame(b, "No entra", "«Así no puedo entrar al ADN»", "Los nucleótidos se fabrican con <b>ribosa</b>, que tiene un OH en el carbono 2′. El ADN solo acepta <b>desoxirribosa</b> (sin ese OH).", 2))
    b = (swap(nuc(140, 150, "k-gen", (), R=30, rib={"p5": 2, "hl2": True}, name="ADP"), nuc(140, 150, "k-gen", (), R=30, rib={"p5": 2, "deoxy": True, "hl2": True}, name="dADP"), D(2) - .3, 0) +
         enzyme(420, 110, "ribonucleótido|reductasa") + blob(420, 300, "k-nadph", "NADPH", r=24) +
         say(490, 40, "¡Yo te lo saco! Te reduzco:|de ribo a desoxi.", (445, 95), D(0)) +
         say(480, 260, "Los electrones|los pongo yo.", (445, 290), D(1)) +
         say(230, 330, "¡Ahora soy desoxi!", (200, 310), D(2)))
    F.append(frame(b, "Reductasa", "La ribonucleótido reductasa", "La <b>ribonucleótido reductasa</b> le saca el OH del 2′ (lo <b>reduce</b>, con electrones del NADPH). Así se pasa de ribo a desoxirribonucleótido.", 3))
    b = (swap(pyr_char(140, 150, "k-ump", [("C2", "O"), ("C4", "O")], R=30, rib={"p5": 3, "deoxy": True}, name="dUTP", mood="o"),
              pyr_char(140, 150, "k-ump", [("C2", "O"), ("C4", "O")], R=30, rib={"p5": 1, "deoxy": True}, name="dUMP"), D(2) - .3, 0) +
         enzyme(470, 120, "dUTPasa") + helix(560, 300, 175, "ADN") +
         say(230, 40, "¡Yo también quiero|entrar al ADN!", (175, 115), D(0)) +
         say(510, 160, "¡No! El ADN no lleva U.|Te corto a dUMP.", (490, 140), D(1)) +
         say(220, 300, "Bueno… así sirvo|para hacer timina.", (170, 280), D(2)))
    F.append(frame(b, "dUTPasa", "La dUTPasa no deja pasar al dUTP", "La <b>dUTPasa</b> rompe el dUTP y deja <b>dUMP</b>. Así el dUTP queda casi en cero (no entra U al ADN) y el dUMP sirve para fabricar timina.", 3))
    b = (swap(pyr_char(140, 150, "k-ump", [("C2", "O"), ("C4", "O")], R=30, rib={"p5": 1, "deoxy": True}, name="dUMP"),
              pyr_char(140, 150, "k-dtmp", [("C2", "O"), ("C4", "O"), ("C5", "CH₃")], R=30, rib={"p5": 1, "deoxy": True}, name="dTMP (timina)"), D(2) - .3, 0) +
         enzyme(450, 110, "timidilato sintasa") + blob(450, 300, "k-thf", "metilen-THF", r=24) +
         say(510, 30, "Te pongo un metilo (CH₃)|en el carbono 5.", (475, 95), D(0)) +
         say(510, 250, "El CH₃ lo traigo yo.", (475, 290), D(1)) +
         say(240, 320, "¡Soy timina! Ahora sí entro al ADN.", (190, 300), D(2)))
    F.append(frame(b, "Timidilato sintasa", "La timidilato sintasa hace la timina", "La <b>timidilato sintasa</b> le pone un metilo al dUMP (el carbono lo trae el metilen-THF) y forma <b>dTMP</b>, la timina del ADN.", 3))
    cell = "<circle cx='640' cy='280' r='62' class='bad-cell'/>" + face(640, 275, 1.4, "sad")
    b = (pyr_char(140, 150, "k-alo", [("C2", "O"), ("C4", "O"), ("C5", "F")], R=30, rib={"p5": 1, "deoxy": True}, name="5-fluorouracilo", look=1) +
         enzyme(420, 120, "timidilato sintasa", mood="o") + cell + T(640, 370, "célula de cáncer", "lab") +
         say(210, 20, "Me hago pasar por dUMP…", (165, 110), D(0)) +
         say(470, 30, "¡Me trabé! No puedo|hacer más dTMP.", (440, 95), D(1)) +
         say(250, 300, "Sin dTMP no copio mi ADN|y no me puedo dividir.", (585, 285), D(2)))
    F.append(frame(b, "5-FU", "El 5-fluorouracilo", "El <b>5-fluorouracilo</b> bloquea la timidilato sintasa. Sin dTMP no se puede copiar el ADN, así que frena a las células que se dividen mucho, como las del cáncer.", 3))
    g = nuc(150, 140, "k-gua", (("C6", "O"), ("C2", "NH₂")), R=26)
    b = (g + T(160, 210, "G", "sg-t") + L(225, 140, 290, 140, "bp") +
         swap(pyr_char(360, 140, "k-ctp", [("C2", "O"), ("C4", "NH₂")], R=30, name="citosina"),
              pyr_char(360, 140, "k-ump", [("C2", "O"), ("C4", "O")], R=30, name="uracilo", mood="o"), D(1) + .3, 0) +
         say(450, 40, "Estoy feliz con mi G.", (390, 105), D(0)) +
         say(450, 150, "¡Ay! Se me fue el NH₂…|(desaminación espontánea)", (395, 150), D(1)) +
         say(380, 290, "Ahora soy un uracilo…|y me pego con A.", (370, 220), D(2)) +
         N(T(400, 385, "Esto le pasa a miles de citosinas por día en cada célula.", "lab2"), D(2)))
    F.append(frame(b, "Desaminación", "¿Por qué T y no U? (1)", "La <b>citosina se desamina sola</b> (pierde su NH₂) y se convierte en uracilo. Pasa todo el tiempo, en miles de bases por día.", 3))
    b = (enzyme(400, 120, "reparadora", mood="o") +
         pyr_char(150, 140, "k-ump", [("C2", "O"), ("C4", "O")], R=26) + T(150, 205, "¿U original?", "lab") +
         pyr_char(650, 140, "k-ump", [("C2", "O"), ("C4", "O")], R=26) + T(650, 205, "¿o era una C?", "lab") +
         say(250, 20, "Si el ADN usara U siempre…|¿cuál es original y cuál era C?", (400, 95), D(0)) +
         N(note(400, 280, "si no se corrige: U se aparea con A →|en la replicación, G-C pasa a A-T", "lab"), D(1)) +
         say(290, 330, "¡Mutación!", (400, 310), D(1) + 1))
    F.append(frame(b, "Sin T", "¿Por qué T y no U? (2)", "Si el ADN usara U normalmente, la célula <b>no podría distinguir</b> una U legítima de una C dañada. Sin corregirla, en la siguiente replicación el par <b>G-C pasaría a A-T</b>: una mutación.", 2))
    b = (pyr_char(130, 140, "k-dtmp", [("C2", "O"), ("C4", "O"), ("C5", "CH₃")], R=30, name="timina") +
         O(pyr_char(420, 300, "k-ump", [("C2", "O"), ("C4", "O")], R=24, mood="o"), D(1) + .8, 120, 60) +
         enzyme(420, 120, "uracilo-ADN|glicosilasa") + enzyme(680, 270, "reparación", k="k-enz2") +
         say(200, 10, "Yo soy uracilo + CH₃:|mi metilo es la etiqueta de original.", (155, 100), D(0)) +
         say(525, 30, "Entonces toda U en el ADN|es un error. ¡Afuera!", (445, 95), D(1)) +
         say(420, 250, "Y yo vuelvo a poner la C.", (652, 265), D(2)))
    F.append(frame(b, "Con T", "¿Por qué T y no U? (3)", "Como el ADN usa <b>timina</b> (uracilo con un metilo en el C5), <b>toda U que aparece es un error</b>. La <b>uracilo-ADN glicosilasa</b> la saca y la reparación por escisión de bases repone la C.", 3))
    rna = path("M120 220 C160 190 200 250 240 220 C280 190 320 250 360 220", "s-rna") + face(240, 200, .9)
    b = (rna + T(240, 280, "ARN", "lab") +
         say(400, 60, "Yo duro poco y hay muchas copias|de mí: un error no se hereda.", (300, 205), D(0)) +
         say(400, 170, "Y fabricar U es más barato|que fabricar T.", (330, 215), D(1)) +
         N(note(400, 340, "en el ADN, que guarda la información para siempre, vale la pena pagar la T", "lab2"), D(2)))
    F.append(frame(b, "ARN", "¿Por qué el ARN sí usa U?", "El <b>ARN</b> dura poco y se hacen muchas copias: un error no se hereda ni es grave. Además, la U es más barata (la T necesita el paso extra de la timidilato sintasa).", 2))
    return F

# ================================================================== VIDEO 4: gota
def v_gota():
    F = []
    b = (swap(nuc(150, 160, R=30, name="hipoxantina"), nuc(150, 160, "k-xan", (("C6", "O"), ("C2", "O")), R=30, name="xantina"), D(2) - .3, 0) +
         enzyme(470, 120, "xantina oxidasa") +
         say(230, 20, "Si nadie me recicla,|me degradan…", (175, 120), D(0)) +
         say(540, 30, "Yo te oxido:|pasás a xantina.", (492, 100), D(1)) +
         N(T(150, 290, "+1 oxígeno", "lab2"), D(2)))
    F.append(frame(b, "Xantina", "Degradación (1): hipoxantina → xantina", "Una purina que no se recicla se degrada. La <b>xantina oxidasa</b> oxida la hipoxantina a <b>xantina</b>.", 2))
    b = (swap(nuc(150, 160, "k-xan", (("C6", "O"), ("C2", "O")), R=30, name="xantina"),
              nuc(150, 160, "k-uri", (("C6", "O"), ("C2", "O"), ("C8", "O")), R=30, name="ácido úrico", mood="flat"), D(1) + .3, 0) +
         enzyme(470, 120, "xantina oxidasa") +
         say(540, 30, "Y a vos también:|ahora sos ácido úrico.", (492, 100), D(0)) +
         say(250, 250, "Soy poco soluble en agua…", (205, 185), D(1) + .6))
    F.append(frame(b, "Ácido úrico", "Degradación (2): xantina → ácido úrico", "La misma <b>xantina oxidasa</b> pasa la xantina a <b>ácido úrico</b>. En humanos el camino termina acá, y el ácido úrico es <b>poco soluble</b>.", 2))
    b = (nuc(150, 170, "k-uri", (("C6", "O"), ("C2", "O"), ("C8", "O")), R=28, name="ácido úrico", mood="flat") + kidney(560, 200) + T(560, 290, "riñón", "lab") +
         N(arrow(230, 170, 480, 190), .3) +
         say(560, 30, "Lo saco por la orina.", (565, 140), D(0)) +
         say(240, 260, "Siempre que no seamos demasiados…", (200, 185), D(1)))
    F.append(frame(b, "Riñón", "El ácido úrico sale por el riñón", "El ácido úrico viaja por la sangre y el <b>riñón</b> lo elimina por la orina.", 2))
    b = (toe(260, 230) + xtals(440, 255) +
         N(P("<circle cx='450' cy='262' r='38' class='hlc'/>"), .3) +
         say(470, 70, "¡Somos tantos que nos|hicimos cristales!", (455, 240), D(0)) +
         say(40, 110, "¡Ay! Me duele|y se me inflama.", (330, 250), D(1)) +
         N(T(400, 370, "GOTA: cristales de urato en las articulaciones (típico en los pies)", "lab"), D(2)))
    F.append(frame(b, "Gota", "Gota", "Si hay demasiado ácido úrico (lo más común es que el riñón elimine poco), <b>precipita como cristales</b> en las articulaciones, que se inflaman y duelen: es la <b>gota</b>.", 2))
    b = (nuc(140, 160, "k-alo", R=30, name="alopurinol", look=1) + enzyme(450, 140, "xantina oxidasa", mood="o") +
         say(200, 20, "Me parezco a la hipoxantina…", (160, 125), D(0)) +
         say(510, 50, "¿Hipoxantina? Vení…|¡Ay, me trabaste!", (475, 120), D(1)) +
         N(nuc(330, 310, R=20) + nuc(440, 310, "k-xan", (("C6", "O"), ("C2", "O")), R=20), D(2) - .3) +
         say(510, 280, "Nosotras somos más solubles:|salimos sin hacer cristales.", (480, 305), D(2)))
    F.append(frame(b, "Alopurinol", "El alopurinol", "El <b>alopurinol</b> es un análogo de la hipoxantina e <b>inhibe la xantina oxidasa</b>. Se forma menos ácido úrico y quedan hipoxantina y xantina, que son más solubles.", 3))
    broken = (enzyme(600, 230, "HGPRT (falla)", k="k-off", mood="sad") +
              "<line x1='575' y1='210' x2='625' y2='252' class='nox'/><line x1='625' y1='210' x2='575' y2='252' class='nox'/>")
    b = (f"<rect x='14' y='14' width='378' height='372' rx='18' class='pan3'/><rect x='408' y='14' width='378' height='372' rx='18' class='pan2'/>" +
         enzyme(200, 230, "HGPRT") +
         say(40, 40, "Si funciono bien, reciclo|la hipoxantina: hay menos|ácido úrico.", (200, 205), D(0)) +
         broken +
         say(440, 40, "Si fallo, todo se degrada:|más ácido úrico → gota.", (600, 205), D(1)))
    F.append(frame(b, "Rescate y gota", "El rescate protege de la gota", "Si la enzima de rescate (<b>HGPRT</b>) funciona, la hipoxantina se recicla y se forma menos ácido úrico. Si <b>falla</b>, se degradan más purinas, sube el ácido úrico y aparece la gota.", 2))
    return F

def run():
    s = open("t_n2s.html").read()
    s = re.sub(r"<!--ANIM:(s\w+)-->.*?<!--/ANIM:\1-->\n?", "", s, flags=re.S)
    ins = [("<h3>Dos caminos para tener nucleótidos</h3>", "s1", "Historia 1 · De novo y rescate", v_rescate()),
           ("<h3>De qué se arman los anillos y las dos estrategias</h3>", "s2", "Historia 2 · Purinas, pirimidinas y la hipoxantina", v_estrategias()),
           ("<h3>Desoxirribonucleótidos y el paso extra de la timina</h3>", "s3", "Historia 3 · Desoxi, timina y por qué T y no U", v_desoxi()),
           ("<h3>Degradación de purinas y gota</h3>", "s4", "Historia 4 · Gota y alopurinol", v_gota())]
    for anchor, key, title, fr in ins:
        assert s.count(anchor) == 1, anchor
        s = s.replace(anchor, anchor + "\n" + player(key, title, fr))
    open("t_n2s.html", "w").write(s)
    print("ok", [len(x[3]) for x in ins])

if __name__ == "__main__":
    run()
