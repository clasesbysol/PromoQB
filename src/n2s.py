# Ácidos nucleicos II · versión simplificada (sección n2s)
import math
from anim import T, L, path, arrow, player, phased, all_rep, all_tr, tl_frames, E
from metab import (blob, small, enzyme, atom, ribose, rib_pts, rib_under, pur_pos, pyr_pos, PUR_B, PYR_B,
                   ring_atoms, pur_char, pyr_char, legend, stop, note, subst, badge)

def fig(body, h, label, cap=""):
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f"<figure class='anim n2fig'><svg viewBox='0 0 800 {h}' role='img' aria-label='{label}'>{body}</svg>{c}</figure>"

def pan(x, y, w, h, cls="pan"):
    return f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='18' class='{cls}'/>"

# ---------------------------------------------------------------- figura 1: dos caminos
def fig_caminos():
    o = [pan(10, 10, 384, 320), pan(406, 10, 384, 320)]
    o.append(T(202, 42, "DE NOVO", "ttl-a") + T(202, 62, "se fabrica desde cero, con moléculas simples", "lab2"))
    for x, k, n in ((58, "k-gln", "glutamina"), (130, "k-asp", "aspartato"), (202, "k-gly", "glicina"), (274, "k-thf", "THF"), (346, "k-co2", "CO₂")):
        o.append(blob(x, 105, k, r=18) + T(x, 140, n, "lab2"))
    o.append(arrow(202, 152, 202, 180))
    o.append(pur_char(186, 222, "k-imp", [("C6", "O")], R=24, rib={"p5": 1}))
    o.append(note(300, 230, "+ PRPP|(pone la|ribosa-5-P)", "lab2", "middle"))
    o.append(T(202, 318, "→ nucleótido nuevo", "lab"))
    o.append(T(598, 42, "RECUPERACIÓN (rescate)", "ttl-b") + T(598, 62, "se reciclan bases que ya existen", "lab2"))
    o.append(note(505, 92, "DIETA|digestión de los ácidos|nucleicos que comemos|(ruta principal de|importación de bases)", "lab2"))
    o.append(note(695, 92, "DENTRO DE LA CÉLULA|degradación de su propio|ADN y ARN (recambio)", "lab2"))
    o.append(arrow(505, 178, 560, 210) + arrow(695, 148, 590, 210))
    o.append(pur_char(560, 240, "k-imp", [("C6", "O")], R=22, name=None))
    o.append(T(560, 296, "base libre", "lab2"))
    o.append(T(660, 245, "+ PRPP", "lab") + arrow(700, 240, 745, 240))
    o.append(T(598, 318, "→ nucleótido otra vez útil", "lab"))
    o.append(pan(10, 342, 780, 78, "pan2"))
    o.append(arrow(752, 240, 752, 350, "arrb"))
    o.append(T(400, 372, "¿Y si no se reutilizan? Se degradan:", "lab"))
    o.append(T(400, 400, "purinas → ácido úrico     ·     pirimidinas → β-ureidopropionato", "lab"))
    return fig("".join(o), 430, "De novo y recuperación")

# ---------------------------------------------------------------- figura 2: dos estrategias
PSRC = {"N9": "q-gln", "C4": "q-gly", "C5": "q-gly", "N7": "q-gly", "C8": "q-for", "N3": "q-gln", "C6": "q-co2", "N1": "q-asp", "C2": "q-for"}
YSRC = {"C2": "q-co2", "N3": "q-gln", "N1": "q-asp", "C6": "q-asp", "C5": "q-asp", "C4": "q-asp"}

def fig_estrategias():
    o = [pan(10, 10, 384, 350), pan(406, 10, 384, 350)]
    o.append(T(202, 40, "PURINAS (A, G)", "ttl-a") + T(202, 62, "el anillo se arma ENCIMA de la ribosa-fosfato", "lab"))
    pp = pur_pos(160, 150, 38)
    rc = rib_under(*pp["N9"], 24, 28); c1 = rib_pts(*rc)["C1"]
    o.append(L(*pp["N9"], *c1, "bond") + ribose(*rc, p5=1) + ring_atoms(pp, set(PSRC), PSRC))
    o.append(note(318, 205, "el PRPP está|desde el|principio", "lab2"))
    o.append(note(202, 312, "con aminoácidos (glicina, glutamina,|aspartato) + THF + CO₂", "lab2"))
    o.append(T(598, 40, "PIRIMIDINAS (C, U, T)", "ttl-b") + T(598, 62, "el anillo se arma SOLO y después se une", "lab"))
    yp = pyr_pos(500, 150, 44)
    o.append(ring_atoms(yp, set(YSRC), YSRC, bonds=PYR_B))
    o.append(T(500, 228, "1° anillo suelto", "lab2"))
    o.append(arrow(560, 150, 610, 150) + T(585, 140, "+ PRPP", "lab2"))
    yp2 = pyr_pos(690, 140, 36)
    rc2 = rib_under(*yp2["N1"], 22, 22); c12 = rib_pts(*rc2, 22)["C1"]
    o.append(ring_atoms(yp2, set(YSRC), YSRC, bonds=PYR_B) + L(*yp2["N1"], *c12, "bond") + ribose(*rc2, p5=1, r=22))
    o.append(T(690, 262, "2° recién ahí la ribosa", "lab2"))
    o.append(note(598, 300, "más simple: carbamoil fosfato|+ aspartato", "lab2"))
    o.append(legend([("q-asp", "aspartato"), ("q-gln", "glutamina"), ("q-gly", "glicina"), ("q-for", "THF"), ("q-co2", "CO₂")], 388))
    return fig("".join(o), 400, "Dos estrategias")

# ---------------------------------------------------------------- figura 3: hipoxantina
def fig_hipox():
    o = []
    o.append(pur_char(130, 120, "k-imp", [("C6", "O")], R=28, rib={"p5": 1}, name="IMP (inosinato)", sub="1.er producto de la|síntesis de purinas"))
    o.append(pur_char(420, 150, "k-imp", [("C6", "O")], R=40, name="HIPOXANTINA", sub="la base del IMP"))
    o.append(path("M190 110 C260 70 330 80 380 105", "arr") + T(285, 70, "su base es…", "lab2"))
    o.append(arrow(175, 30, 300, 30) + T(310, 35, "del IMP salen AMP y GMP", "lab", "start"))
    o.append(arrow(520, 150, 610, 150) + note(565, 128, "xantina oxidasa", "enz-n") + note(700, 135, "xantina →|ácido úrico", "lab"))
    o.append(T(700, 180, "(degradación)", "lab2"))
    o.append(path("M400 260 C380 330 200 340 150 260", "arr") + f"<polygon points='150,260 146,274 158,270' class='arrh'/>")
    o.append(note(275, 350, "+ PRPP → IMP (rescate, por la HGPRT)", "lab"))
    o.append(pur_char(640, 270, "k-alo", [("C6", "O")], R=26, name="alopurinol", sub="se parece a la hipoxantina", look=-1))
    return fig("".join(o), 380, "Hipoxantina")

# ---------------------------------------------------------------- figura 4: regulación
def node(x, y, t, w=None, cls="nd"):
    w = w or 20 + len(t) * 9
    return f"<rect x='{x-w/2}' y='{y-17}' width='{w}' height='34' rx='10' class='{cls}'/>" + T(x, y + 5, t, "lab")

def fig_reg():
    o = [node(70, 150, "PRPP"), arrow(105, 150, 165, 150),
         f"<rect x='170' y='122' width='120' height='56' rx='12' class='nd hot'/>" + T(230, 145, "1.er paso", "lab") + T(230, 164, "(comprometido)", "lab2"),
         arrow(292, 150, 340, 150) + T(370, 155, "· · ·", "lab") + arrow(395, 150, 440, 150),
         node(480, 150, "IMP"),
         arrow(515, 140, 600, 80) + node(640, 70, "AMP") + T(560, 92, "usa GTP", "lab2", "end"),
         arrow(515, 160, 600, 220) + node(640, 230, "GMP") + T(560, 222, "usa ATP", "lab2", "end"),
         path("M480 130 C460 70 300 60 250 118", "inh"), path("M640 52 C600 0 300 10 236 118", "inh"), path("M640 248 C600 330 300 320 236 182", "inh"),
         stop(250, 108, "", "start"), stop(40, 50, "frenan el 1.er paso:|IMP, AMP y GMP", "start"),
         path("M675 70 C715 70 715 112 650 112", "inh") + T(720, 100, "AMP frena", "stp-t", "start") + T(720, 116, "su rama", "stp-t", "start"),
         path("M675 230 C715 230 715 188 650 188", "inh") + T(720, 196, "GMP frena", "stp-t", "start") + T(720, 212, "su rama", "stp-t", "start"),
         T(400, 345, "Retroinhibición: los productos finales frenan su propia síntesis.", "lab")]
    return fig("".join(o), 365, "Regulación de purinas")

# ---------------------------------------------------------------- figura 5: dTMP
def fig_dtmp():
    o = [T(400, 22, "ribonucleótido reductasa: NDP → dNDP (de ribo a desoxi)", "lab2")]
    xs = [115, 300, 485, 670]
    o.append(pyr_char(xs[0], 110, "k-ump", [("C2", "O"), ("C4", "O")], R=26, rib={"p5": 2, "deoxy": True}, name="dUDP"))
    o.append(pyr_char(xs[1], 110, "k-ump", [("C2", "O"), ("C4", "O")], R=26, rib={"p5": 3, "deoxy": True}, name="dUTP", mood="o"))
    o.append(pyr_char(xs[2], 110, "k-ump", [("C2", "O"), ("C4", "O")], R=26, rib={"p5": 1, "deoxy": True}, name="dUMP"))
    o.append(pyr_char(xs[3], 110, "k-dtmp", [("C2", "O"), ("C4", "O"), ("C5", "CH₃")], R=26, rib={"p5": 1, "deoxy": True}, name="dTMP", sub="(timina)"))
    for a, b_, t1 in ((0, 1, "+ P (ATP)"), (1, 2, "dUTPasa"), (2, 3, "timidilato sintasa")):
        o.append(arrow(xs[a] + 60, 70, xs[b_] - 50, 70) + T((xs[a] + xs[b_]) / 2 + 5, 58, t1, "enz-n" if a else "lab2"))
    o.append(T(578, 42, "+ metilen-THF (pone el CH₃)", "lab2"))
    o.append(note(390, 290, "la dUTPasa deja el dUTP casi en cero:|así NO entra U al ADN y queda dUMP", "lab"))
    o.append(stop(560, 300, "5-fluorouracilo bloquea la|timidilato sintasa: sin dTMP|no hay ADN nuevo → frena|células que se dividen mucho", "start"))
    return fig("".join(o), 370, "dTMP")

# ---------------------------------------------------------------- figura 6: C, U, T
def fig_tu():
    o = []
    o.append(pyr_char(120, 110, "k-ctp", [("C2", "O"), ("C4", "NH₂")], R=34, name="citosina"))
    o.append(arrow(185, 110, 300, 110) + note(242, 88, "se desamina|sola", "lab2") + T(242, 140, "(pierde NH₂)", "lab2"))
    o.append(pyr_char(380, 110, "k-ump", [("C2", "O"), ("C4", "O")], R=34, name="uracilo", sub="¿legítimo o C dañada?", mood="o"))
    o.append(pyr_char(660, 110, "k-dtmp", [("C2", "O"), ("C4", "O"), ("C5", "CH₃")], R=34, name="timina", sub="= uracilo + CH₃ en el C5"))
    o.append(T(728, 30, "«etiqueta» de base original", "lab2", "end"))
    o.append(f"<rect x='20' y='230' width='370' height='120' rx='14' class='pan2'/>" +
             note(205, 258, "Si el ADN usara U:|no podría distinguir una U legítima|de una C dañada → en la replicación|G-C pasa a A-T (mutación)", "lab"))
    o.append(f"<rect x='410' y='230' width='370' height='120' rx='14' class='pan3'/>" +
             note(595, 258, "Como el ADN usa T:|toda U en el ADN es un error →|la uracilo-ADN glicosilasa la saca|y la reparación repone la C", "lab"))
    return fig("".join(o), 365, "Timina y uracilo")

# ---------------------------------------------------------------- figura 7: gota
def fig_gota():
    o = []
    Y = 140
    o.append(pur_char(90, Y, "k-imp", [("C6", "O")], R=26, name="hipoxantina"))
    o.append(arrow(150, Y, 240, Y) + T(195, Y - 15, "xantina oxidasa", "enz-n"))
    o.append(pur_char(300, Y, "k-xan", [("C6", "O"), ("C2", "O")], R=26, name="xantina"))
    o.append(arrow(360, Y, 450, Y) + T(405, Y - 15, "xantina oxidasa", "enz-n"))
    o.append(pur_char(510, Y, "k-uri", [("C6", "O"), ("C2", "O"), ("C8", "O")], R=26, name="ácido úrico", mood="flat"))
    o.append(arrow(592, Y, 650, Y) + note(720, Y - 8, "sangre → riñón|→ orina", "lab"))
    o.append(stop(150, 26, "alopurinol (análogo de la hipoxantina) inhibe la xantina oxidasa:", "start"))
    o.append(T(166, 48, "quedan hipoxantina y xantina, que son más solubles", "lab2", "start"))
    toe = ("<path d='M470 330 C470 268 515 240 575 248 C640 256 675 278 700 292 C726 308 724 345 700 350 L488 350 C474 350 470 342 470 330Z' class='toe'/>"
           "<circle cx='660' cy='300' r='30' class='joint'/>")
    xt = "".join(f"<line x1='{646+dx}' y1='{290+dy}' x2='{656+dx}' y2='{282+dy}' class='xtal'/>" for dx, dy in ((0, 0), (12, 5), (5, 15), (17, 17)))
    o.append(arrow(520, 205, 560, 252))
    o.append(toe + xt + note(700, 208, "mucho urato →|cristales en las|articulaciones: GOTA", "lab"))
    o.append(path("M80 205 C80 270 110 292 160 296", "arr") + f"<polygon points='166,296 154,290 154,302' class='arrh'/>")
    o.append(T(176, 301, "rescate: + PRPP → IMP (HGPRT)", "lab", "start"))
    o.append(T(40, 330, "si funciona: se recicla y se forma menos urato", "lab2", "start"))
    o.append(T(40, 348, "si falla: más degradación → más urato → gota", "lab2", "start"))
    return fig("".join(o), 365, "Gota")

# ---------------------------------------------------------------- texto
def build():
    H = []
    H.append('<section class="mod" id="n2s" data-topics="NM">\n<p class="kicker">Módulo 6 · versión simplificada</p>\n'
             '<h1>Ácidos nucleicos II · Lo que entra</h1>\n'
             '<p class="lead">Esta versión tiene solo los <b>conceptos que entran</b>, explicados simple. El cuestionario de Ácidos nucleicos II está hecho sobre esta página. La versión completa, con todos los detalles, sigue en la pestaña «Ác. nucleicos II».</p>\n')
    H.append('''<h2>1. Dogma central y tipos de ARN</h2>
<ol class="flow h"><li class="m">ADN</li><li class="e">replicación ↺ · transcripción</li><li class="m">ARN</li><li class="e">traducción</li><li class="m">Proteína</li></ol>
<p>La información va del ADN al ARN y del ARN a la proteína; de una proteína no puede volver a salir. La <b>retrotranscripción</b> (ARN → ADN, en retrovirus) no contradice el dogma.</p>
<div class="cards">
<div class="cd"><h4>ARNm</h4><p>Lleva el mensaje del ADN al ribosoma. Se lee de a 3 bases (codones).</p></div>
<div class="cd"><h4>ARNt</h4><p>Es el adaptador: lleva un aminoácido en su extremo 3′ y reconoce el codón con su <b>anticodón</b>.</p></div>
<div class="cd"><h4>ARNr</h4><p>Es casi el <b>80 %</b> del ARN de la célula. Forma el ribosoma y además cataliza el enlace peptídico: es una <b>ribozima</b>.</p></div>
<div class="cd"><h4>ARNsn</h4><p>Forma parte del espliceosoma, que corta los intrones.</p></div>
</div>
<div class="box why"><b>Dato.</b> Una célula tiene hasta <b>10 veces más ARN que ADN</b> (entre 4 y 10 veces): el ADN es una sola copia guardada y el ARN se fabrica en muchas copias.</div>
''')
    H.append('''<h2>2. Replicación</h2>
<p>Copiar el ADN antes de que la célula se divida. Tres ideas clave:</p>
<div class="cards">
<div class="cd"><h4>Semiconservativa</h4><p>Cada molécula hija tiene una cadena vieja (molde) y una nueva.</p></div>
<div class="cd"><h4>Bidireccional</h4><p>Desde el origen salen dos horquillas en sentidos opuestos.</p></div>
<div class="cd"><h4>Siempre 5′→3′</h4><p>La polimerasa lee el molde 3′→5′, solo alarga y necesita un <b>cebador</b>.</p></div>
</div>
<div class="tbl"><table><tr><th>Proteína</th><th>Qué hace (en una frase)</th></tr>
<tr><td>Helicasa</td><td>Separa las dos cadenas.</td></tr>
<tr><td>Topoisomerasa (girasa)</td><td>Saca la tensión que se acumula adelante de la horquilla.</td></tr>
<tr><td>Proteínas SSB</td><td>Mantienen separadas las cadenas simples.</td></tr>
<tr><td>Primasa</td><td>Pone el cebador de ARN (es una ARN polimerasa).</td></tr>
<tr><td>ADN polimerasa III</td><td>Copia: hebra adelantada continua y retrasada en fragmentos de Okazaki.</td></tr>
<tr><td>ADN polimerasa I</td><td>Saca los cebadores (exonucleasa 5′→3′) y pone ADN en su lugar.</td></tr>
<tr><td>ADN ligasa</td><td>Une los fragmentos (enlace fosfodiéster).</td></tr></table></div>
<div class="box trap"><b>Ojo</b> La hebra <b>adelantada</b> se copia continua porque va en el mismo sentido que la horquilla. La <b>retrasada</b> va al revés, así que se copia de a pedazos (fragmentos de Okazaki), cada uno con su cebador.</div>
''' + player("rep", "Replicación", phased("rep", all_rep())))
    H.append('''<h2>3. Transcripción</h2>
<p>Copiar un gen de ADN a ARN. La <b>ARN polimerasa</b> lee la cadena <b>molde</b> 3′→5′ y arma el ARN 5′→3′, con U en lugar de T. El ARN queda igual a la cadena <b>codificante</b> (cambiando T por U).</p>
<div class="cards">
<div class="cd"><h4>Iniciación</h4><p>La polimerasa reconoce el <b>promotor</b>: en bacterias, con la subunidad <b>σ (sigma)</b>; en eucariotas, con <b>factores de transcripción</b>. <b>No necesita cebador.</b></p></div>
<div class="cd"><h4>Elongación</h4><p>Avanza abriendo una burbuja y sumando NTP al extremo 3′ del ARN.</p></div>
<div class="cd"><h4>Terminación</h4><p>En el <b>terminador</b>: con una horquilla en el ARN (independiente de Rho) o con la proteína <b>Rho</b>.</p></div>
</div>
<ol class="flow h"><li class="m">Pre-ARNm (exones + intrones)</li><li class="e">cap 5′ · poli(A) 3′ · splicing</li><li class="m">ARNm maduro</li></ol>
<p>En eucariotas el ARNm se procesa: se le pone un <b>cap</b> de 7-metilguanosina en el 5′, una <b>cola de poli(A)</b> en el 3′, y el <b>espliceosoma</b> saca los intrones. Con <b>splicing alternativo</b>, un mismo gen da varias proteínas (isoformas).</p>
''' + player("tr", "Transcripción", phased("tr", all_tr())))
    H.append('''<h2>4. Traducción</h2>
<p>Leer el ARNm y armar la proteína en el <b>ribosoma</b>. El código es de <b>tripletes</b>: 64 codones, 61 para aminoácidos y 3 de stop (UAA, UAG, UGA). Es degenerado y casi universal. <b>AUG</b> es el codón de inicio (Met).</p>
<div class="cards">
<div class="cd"><h4>Antes: activación</h4><p>Una aminoacil-ARNt sintetasa carga cada ARNt con su aminoácido (gasta ATP).</p></div>
<div class="cd"><h4>Iniciación</h4><p>La subunidad menor encuentra el AUG (Shine-Dalgarno en bacterias, cap en eucariotas). El ARNt iniciador (fMet o Met) entra al sitio <b>P</b>. Se une la subunidad mayor.</p></div>
<div class="cd"><h4>Elongación</h4><p>Ciclo: entra un aminoacil-ARNt al sitio <b>A</b> → la peptidil transferasa (ARNr) forma el enlace peptídico → el ribosoma avanza un codón (GTP) y el ARNt vacío sale por <b>E</b>.</p></div>
<div class="cd"><h4>Terminación</h4><p>En un codón stop entra un <b>factor de liberación</b> (no hay ARNt para el stop) y se suelta la proteína.</p></div>
</div>
''' + player("tl", "Traducción", phased("tl", tl_frames())))
    H.append('''<h2>5. Nucleótidos: de dónde salen y adónde van</h2>
<p>Esta parte entra solo como <b>concepto</b>: no hace falta saber los pasos uno por uno ni las enzimas intermedias.</p>
<h3>Dos caminos para tener nucleótidos</h3>
''' + fig_caminos() + '''
<div class="cards">
<div class="cd"><h4>De novo</h4><p>Fabricar el nucleótido <b>desde cero</b>, a partir de moléculas simples: aminoácidos, THF (tetrahidrofolato, de la vitamina B9), CO₂ y ribosa.</p></div>
<div class="cd"><h4>Recuperación (rescate)</h4><p><b>Reciclar</b> bases y nucleósidos que ya existen. Vienen de la <b>degradación de ácidos nucleicos</b>: dentro de la célula (recambio) o por la <b>digestión de los ácidos nucleicos de la dieta</b>. Esa hidrólisis extracelular de lo que comemos es la <b>ruta principal de importación</b> de bases y nucleótidos.</p></div>
<div class="cd"><h4>Si no se reutilizan…</h4><p>…se degradan: las <b>purinas</b> terminan en <b>ácido úrico</b> y las <b>pirimidinas</b> en <b>β-ureidopropionato</b>.</p></div>
</div>
<h3>El dador de ribosa</h3>
<p>El <b>PRPP</b> (5-fosforribosil-1-pirofosfato) es una ribosa-5-fosfato «activada» con un pirofosfato en el C1. Es el <b>dador de la ribosa-fosfato de TODOS los nucleótidos</b>, tanto en la vía de novo como en la de recuperación.</p>
<h3>De qué se arman los anillos y las dos estrategias</h3>
''' + fig_estrategias() + '''
<div class="tbl"><table><tr><th></th><th>Purinas (A, G)</th><th>Pirimidinas (C, U, T)</th></tr>
<tr><td>Se arma con</td><td>Aminoácidos (glicina, glutamina, aspartato), THF y CO₂</td><td>Carbamoil fosfato y aspartato (más simple)</td></tr>
<tr><td>Estrategia</td><td>El anillo se arma <b>encima de la ribosa-fosfato</b> (el PRPP está desde el principio)</td><td>El anillo se arma <b>por separado</b> y después toma la ribosa-fosfato del PRPP</td></tr>
<tr><td>Primer producto</td><td><b>IMP</b> (inosinato), cuya base es la <b>hipoxantina</b></td><td>UMP (uracilo)</td></tr></table></div>
<div class="box why"><b>Para recordar.</b> Purinas: primero la ribosa y el anillo encima. Pirimidinas: primero el anillo y la ribosa al final.</div>
<h3>La hipoxantina</h3>
''' + fig_hipox() + '''
<p>La <b>hipoxantina</b> es la base purínica del <b>IMP (inosinato)</b>, el primer nucleótido de purina que se fabrica. Del IMP salen el AMP y el GMP. La hipoxantina aparece en tres lugares:</p>
<div class="cards">
<div class="cd"><h4>Síntesis</h4><p>Es la base del IMP, de donde salen AMP y GMP.</p></div>
<div class="cd"><h4>Degradación</h4><p>La xantina oxidasa la pasa a xantina y después a ácido úrico.</p></div>
<div class="cd"><h4>Rescate</h4><p>Hipoxantina + PRPP → IMP (enzima HGPRT): se recicla en vez de degradarse.</p></div>
</div>
<h3>Cómo se regula la síntesis de purinas</h3>
''' + fig_reg() + '''
<p>Por <b>retroinhibición</b>: los productos finales (IMP, AMP y GMP) frenan el primer paso comprometido. Además, cada rama se frena con su propio producto. Hay un control cruzado: para hacer AMP se gasta <b>GTP</b> y para hacer GMP se gasta <b>ATP</b>, así que si sobra uno se fabrica más del otro y quedan equilibrados.</p>
<h3>Desoxirribonucleótidos y el paso extra de la timina</h3>
''' + fig_dtmp() + '''
<p>La <b>ribonucleótido reductasa</b> pasa los ribonucleótidos a desoxirribonucleótidos. La timina (dTMP) necesita un <b>paso extra</b>: el dUDP pasa a dUTP, y la <b>dUTPasa</b> hidroliza el dUTP a <b>dUMP</b>. Eso sirve para dos cosas: el dUTP queda casi en cero (así el uracilo no entra al ADN) y se obtiene el dUMP que la <b>timidilato sintasa</b> va a metilar para formar dTMP.</p>
<div class="box trap"><b>5-fluorouracilo.</b> Inhibe la timidilato sintasa. Sin dTMP no se puede copiar el ADN, así que frena las células que se dividen mucho, como las del cáncer.</div>
<h3>¿Por qué el ADN tiene timina y el ARN uracilo?</h3>
''' + fig_tu() + '''
<p>La <b>citosina se desamina sola</b> y se convierte en uracilo: le pasa a miles de bases por día en cada célula. Si el ADN usara uracilo normalmente, la célula no podría distinguir un uracilo legítimo de uno que en realidad era una citosina dañada. Sin corregirlo, ese uracilo se aparearía con adenina y en la siguiente replicación quedaría una mutación <b>G-C → A-T</b>.</p>
<p><b>Solución:</b> el ADN usa <b>timina</b>, que es un uracilo con un metilo en el carbono 5. Ese metilo funciona como <b>etiqueta de base original</b>. Cualquier uracilo que aparezca en el ADN es necesariamente un error: la <b>uracilo-ADN glicosilasa</b> lo detecta y lo saca, y la <b>reparación por escisión de bases</b> repone la citosina.</p>
<p>El <b>ARN</b> dura poco y se hacen muchas copias: un error en una molécula no se hereda ni es grave. Además, usar uracilo es más barato, porque fabricar timina requiere un paso extra (la timidilato sintasa, con metilen-THF). En el ADN, que guarda la información a largo plazo, vale la pena pagar ese costo.</p>
<h3>Degradación de purinas y gota</h3>
''' + fig_gota() + '''
<p>Las purinas que no se reciclan se degradan a <b>ácido úrico</b>, que sale por el <b>riñón</b>. El ácido úrico es poco soluble: si se acumula, forma <b>cristales</b> en las articulaciones (típicamente en los pies), que las inflaman y duelen. Eso es la <b>gota</b>.</p>
<div class="cards">
<div class="cd"><h4>Alopurinol</h4><p>Es un <b>análogo de la hipoxantina</b> e inhibe la <b>xantina oxidasa</b>. Se forma menos ácido úrico y quedan hipoxantina y xantina, que son más solubles y se eliminan sin formar cristales.</p></div>
<div class="cd"><h4>El rescate importa</h4><p>Si la enzima de rescate (HGPRT) funciona bien, las bases se reciclan y se forma menos ácido úrico. Si no funciona, se degradan más purinas, sube el ácido úrico y aparece la gota.</p></div>
</div>
</section>
''')
    return "".join(H)

if __name__ == "__main__":
    open("t_n2s.html", "w").write(build())
    print("ok")
