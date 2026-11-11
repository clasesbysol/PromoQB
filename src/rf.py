# Repaso de falladas (errores del 11/11/2026). Genera t_rf.html.
from anim import T, L, path, arrow
from metab import blob, small, enzyme, note, pur_char, pyr_char, face

def fig(body, h, label):
    return f"<figure class='anim n2fig'><svg viewBox='0 0 800 {h}' role='img' aria-label='{label}'>{body}</svg></figure>"

def figs(*ids, cls="figs"):
    return f'<div class="{cls}">' + "".join(f'<figure data-mol="{i}"></figure>' for i in ids) + "</div>"

def miss(q, mine, ok):
    m = f'<span class="bad">✗ Elegiste: {mine}</span>' if mine else ""
    return f'<div class="rf-q"><span class="rf-tag">Fallaste</span>{q}</div><div class="rf-ans">{m}<span class="ok">✓ Correcta: {ok}</span></div>'

def block(title, misses, body):
    return f'<div class="rf"><h3>{title}</h3>' + "".join(miss(*m) for m in misses) + f'<div class="rf-body">{body}</div></div>'

def truco(t): return f'<div class="box why"><b>Para no volver a errarla.</b> {t}</div>'
def ojo(t): return f'<div class="box trap"><b>Ojo</b> {t}</div>'
def practice(topics, label):
    return f'<p><button class="go" type="button" data-practice="{topics}" data-mode="wrong">{label}</button></p>'

NS = "No lo sé"

# ---------------------------------------------------------------- figuras propias
def fig_hershey():
    def phage(x, y, cap, dna):
        return (f"<polygon points='{x},{y-34} {x+24},{y-20} {x+24},{y+8} {x},{y+22} {x-24},{y+8} {x-24},{y-20}' class='{cap}'/>"
                f"<path d='M{x-10} {y-8} C{x-2} {y-22} {x+8} {y+4} {x+12} {y-10}' class='{dna}'/>"
                f"<line x1='{x}' y1='{y+22}' x2='{x}' y2='{y+52}' class='ph-tail'/>"
                f"<line x1='{x}' y1='{y+52}' x2='{x-14}' y2='{y+66}' class='ph-tail'/><line x1='{x}' y1='{y+52}' x2='{x+14}' y2='{y+66}' class='ph-tail'/>")
    def tube(x, y, pel, sup):
        return (f"<path d='M{x-34} {y} L{x-34} {y+140} Q{x} {y+176} {x+34} {y+140} L{x+34} {y}' class='tube'/>"
                f"<rect x='{x-33}' y='{y+20}' width='66' height='120' class='{sup}'/>"
                f"<ellipse cx='{x}' cy='{y+148}' rx='22' ry='12' class='{pel}'/>")
    o = [T(190, 30, "Experimento 1: ³⁵S marca la PROTEÍNA", "lab"), T(590, 30, "Experimento 2: ³²P marca el ADN", "lab")]
    o.append(phage(80, 100, "cap-hot", "dna-cold") + T(80, 190, "cápside radiactiva", "lab2"))
    o.append(phage(480, 100, "cap-cold", "dna-hot") + T(480, 190, "ADN radiactivo", "lab2"))
    o.append(arrow(115, 110, 185, 110) + arrow(515, 110, 585, 110) + T(150, 98, "infectar,", "lab2") + T(550, 98, "infectar,", "lab2"))
    o.append(T(150, 132, "licuar y", "lab2") + T(150, 148, "centrifugar", "lab2") + T(550, 132, "licuar y", "lab2") + T(550, 148, "centrifugar", "lab2"))
    o.append(tube(240, 60, "pel-cold", "sup-hot") + tube(640, 60, "pel-hot", "sup-cold"))
    o.append(T(285, 110, "sobrenadante:", "lab2", "start") + T(285, 126, "cápsides vacías", "lab2", "start") + T(285, 142, "→ RADIACTIVO", "stp-t", "start"))
    o.append(T(285, 205, "pellet: bacterias", "lab2", "start") + T(285, 221, "→ casi sin marca", "lab2", "start"))
    o.append(T(685, 110, "sobrenadante:", "lab2", "start") + T(685, 126, "sin marca", "lab2", "start"))
    o.append(T(685, 205, "pellet: bacterias", "lab2", "start") + T(685, 221, "con el ADN", "lab2", "start") + T(685, 237, "→ RADIACTIVO", "stp-t", "start"))
    o.append(T(200, 30, "Experimento 1: ³⁵S marca la PROTEÍNA", "lab") if False else "")
    o.append(T(400, 290, "Lo que entra a la bacteria (y queda en el pellet) es el ADN: el ADN es el material genético.", "lab"))
    return fig("".join(o), 305, "Hershey y Chase")

def fig_shapes():
    def lip(x, y, tails=2, head=11, up=True):
        s = 1 if up else -1
        o = f"<circle cx='{x}' cy='{y}' r='{head}' class='lhead'/>"
        xs = [x - 4, x + 4] if tails == 2 else [x]
        for tx in xs:
            o += f"<path d='M{tx} {y+s*head} q4 {s*8} 0 {s*16} q-4 {s*8} 0 {s*16}' class='ltail'/>"
        return o
    o = []
    cols = [(130, "PC: cilindro", "cabeza ≈ colas", "→ BICAPA", 2, 10), (400, "PE: cono", "cabeza chica", "→ curva la membrana", 2, 6), (670, "lisofosfolípido o detergente", "cabeza grande, 1 cola", "→ MICELA", 1, 13)]
    for x, t1, t2, t3, tails, head in cols:
        o.append(T(x, 30, t1, "lab") + T(x, 48, t2, "lab2"))
        o.append(lip(x, 90, tails, head))
        if tails == 2 and head == 10:
            o.append(f"<rect x='{x-14}' y='{78}' width='28' height='48' class='shape'/>")
        elif tails == 2:
            o.append(f"<polygon points='{x-8},78 {x+8},78 {x+18},126 {x-18},126' class='shape'/>")
        else:
            o.append(f"<polygon points='{x-18},76 {x+18},76 {x+6},126 {x-6},126' class='shape'/>")
        o.append(T(x, 160, t3, "stp-t" if "MICELA" in t3 else "lab"))
    for i in range(6):
        o.append(lip(70 + i * 24, 200, 2, 9) + lip(70 + i * 24, 270, 2, 9, False))
    import math
    for k in range(12):
        a = 2 * math.pi * k / 12
        x, y = 670 + 52 * math.cos(a), 238 + 52 * math.sin(a)
        dx, dy = -math.cos(a), -math.sin(a)
        o.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='9' class='lhead'/><line x1='{x+dx*9:.1f}' y1='{y+dy*9:.1f}' x2='{x+dx*36:.1f}' y2='{y+dy*36:.1f}' class='ltail2'/>")
    o.append(T(670, 312, "adentro: solo colas (hidrofóbico)", "lab2"))
    o.append(T(400, 240, "el agua queda afuera de las colas", "lab2"))
    return fig("".join(o), 325, "Formas de los lípidos")

def fig_periodato():
    o = [T(400, 28, "Celulosa = Glc β(1→4) Glc β(1→4) … (el periodato corta entre dos C con OH vecinos)", "lab")]
    bx = [(60, "extremo NO reductor", "OH libres en C2, C3, C4", "→ 1 HCOOH", "hot"), (250, "residuo interno", "OH libres solo en C2 y C3", "→ 0 HCOOH", "cold"),
          (440, "residuo interno", "(todos iguales)", "→ 0 HCOOH", "cold"), (630, "extremo reductor", "C1, C2, C3 libres", "→ 2 HCOOH", "hot")]
    for x, t1, t2, t3, k in bx:
        o.append(f"<rect x='{x}' y='60' width='150' height='70' rx='12' class='pbox {k}'/>" + T(x + 75, 90, "Glc", "sg-t") + T(x + 75, 112, t1, "lab2"))
        o.append(T(x + 75, 155, t2, "lab2") + T(x + 75, 178, t3, "stp-t" if k == "hot" else "lab"))
    for x in (210, 400, 590):
        o.append(L(x, 95, x + 40, 95, "bond"))
    o.append(T(400, 220, "Total por molécula: 1 + 2 = 3 mol de ácido fórmico, sea la cadena larga o corta.", "lab"))
    o.append(T(400, 244, "Los residuos internos no dan fórmico: solo se rompen entre C2 y C3 (dos aldehídos).", "lab2"))
    return fig("".join(o), 260, "Periodato y celulosa")

# ---------------------------------------------------------------- contenido
def build():
    H = ['<section class="mod" id="rf" data-topics="G1,G2,GC,L,N,NM">\n<p class="kicker">Repaso personal · errores del 11/11</p>\n<h1>Repaso de falladas</h1>\n'
         '<p class="lead">Acá está explicado <b>solo lo que te salió mal</b> (68 preguntas distintas), agrupado por concepto. Arriba de cada explicación ves la pregunta, lo que elegiste y la correcta. Al final de cada parte hay un botón para practicar justo esas preguntas.</p>\n'
         '<div class="cards"><div class="cd"><h4>1. Glúcidos</h4><p>29 errores · GAG, Haworth y análisis de glicanos</p></div><div class="cd"><h4>2. Lípidos</h4><p>18 errores · nomenclatura, cargas, formas y vías</p></div>'
         '<div class="cd"><h4>3. Ácidos nucleicos I</h4><p>13 errores · cálculos, Foto 51, experimentos</p></div><div class="cd"><h4>4. Ácidos nucleicos II</h4><p>8 errores · conceptos puntuales</p></div></div>\n']

    # ============================== GLÚCIDOS
    H.append('<h2>1. Glúcidos</h2>')
    H.append(block("Epímeros: ¿en qué carbono se diferencian?",
        [("D-glucosa y D-galactosa son:", "Epímeros en C2", "Epímeros en C4")],
        '<p>Dos azúcares son <b>epímeros</b> cuando son iguales en todo salvo en <b>un solo carbono quiral</b>. Para encontrarlo, poné las Fischer una al lado de la otra y buscá el único OH que cambia de lado.</p>'
        + figs("f_dglucosa", "f_dmanosa", "f_dgalactosa") +
        '<ul><li><b>Glucosa vs manosa</b>: cambia el OH del <b>C2</b> → epímeros en C2.</li><li><b>Glucosa vs galactosa</b>: cambia el OH del <b>C4</b> → epímeros en C4.</li><li>Manosa vs galactosa no son epímeros: difieren en dos carbonos (C2 y C4).</li></ul>'
        + truco('«<b>Ma</b>nosa = <b>2</b> (C2), <b>Ga</b>lactosa = <b>4</b> (C4)». Con respecto a la glucosa: <b>M</b>anosa cambia <b>arriba</b> (C2), <b>G</b>alactosa más <b>abajo</b> (C4).')))
    H.append(block("Haworth: α y β, y por qué la manosa β es menos estable",
        [("En la proyección de Haworth de una D-hexosa, el anómero α tiene:", "El OH anomérico del mismo lado que el CH₂OH", "El OH anomérico en el lado opuesto al CH₂OH"),
         ("¿Por qué la β-D-manopiranosa es menos estable que la β-D-glucopiranosa?", NS, "Su OH del C2 queda axial en la silla")],
        '<p>En una D-hexosa en Haworth, el <b>CH₂OH (C6) va siempre arriba</b>. El carbono anomérico es el C1 (el que era el carbonilo):</p>'
        + figs("h_aglc", "h_bglc", "h_bman") +
        '<ul><li><b>α</b>: el OH del C1 queda del lado <b>opuesto</b> al CH₂OH → <b>abajo</b>.</li><li><b>β</b>: el OH del C1 queda del <b>mismo lado</b> que el CH₂OH → <b>arriba</b>.</li></ul>'
        '<p><b>Estabilidad en la silla.</b> El anillo de 6 no es plano: tiene forma de silla, y cada sustituyente puede quedar <b>ecuatorial</b> (hacia afuera, cómodo) o <b>axial</b> (vertical, choca con los vecinos). La <b>β-D-glucosa</b> es especial: <b>todos</b> sus OH y el CH₂OH quedan ecuatoriales, por eso es la más estable. La <b>manosa</b> es la glucosa con el C2 al revés (epímero en C2), así que en la β-D-manosa el <b>OH del C2 queda axial</b>: más choques, menos estable.</p>'
        + truco('En D: «<b>β = arriba = mismo lado</b> que el CH₂OH; α = abajo». Y «la β-glucosa tiene todo ecuatorial; cualquier epímero tiene algo axial».')))
    H.append(block("Ribitol, azúcares nucleotídicos y glicación",
        [("¿Qué es el ribitol?", "El desoxiazúcar del ADN", "Un alditol que forma parte de FMN y FAD"),
         ("¿Para qué sirven los azúcares nucleotídicos como la UDP-glucosa?", NS, "Son la forma activada que usan las glicosiltransferasas"),
         ("Reacción de Maillard y glicación de la HbA1c:", "Maillard es enzimática y la glicación no", "Son la misma química no enzimática")],
        '<div class="tbl"><table><tr><th>Nombre</th><th>Qué es</th><th>Dónde está</th></tr>'
        '<tr><td>Ribosa</td><td>Aldopentosa</td><td>ARN</td></tr><tr><td>2-desoxirribosa</td><td>Ribosa sin el OH del C2 (desoxiazúcar)</td><td>ADN</td></tr>'
        '<tr><td><b>Ribitol</b></td><td>Ribosa <b>reducida</b>: el C=O del C1 pasa a CH₂OH → es un <b>alditol</b> (un polialcohol, como el sorbitol)</td><td>Riboflavina (vitamina B2) → <b>FMN y FAD</b></td></tr></table></div>'
        '<p>La terminación <b>«-itol»</b> siempre indica alditol (azúcar reducido): glucitol (sorbitol), ribitol, manitol. El «desoxi» indica que falta un OH.</p>'
        '<p><b>UDP-glucosa.</b> Para unir un azúcar a otra molécula hace falta energía. La célula primero «activa» el azúcar pegándolo a un nucleótido (glucosa-1-P + UTP → UDP-glucosa). Las <b>glicosiltransferasas</b> usan esa forma activada como <b>dador</b>: pasan el azúcar al aceptor y sueltan el UDP. Así se arma el glucógeno y se agregan los azúcares de las glicoproteínas.</p>'
        + figs("f_dribosa", "f_glucitol") +
        '<p><b>Maillard y glicación son la misma reacción, y ninguna usa enzimas.</b> El grupo carbonilo de un azúcar reductor reacciona con un grupo amino libre (de una proteína) → base de Schiff → producto de Amadori. En la cocina se llama <b>Maillard</b> (el dorado del pan o de la carne). En el cuerpo se llama <b>glicación</b>: la glucosa de la sangre se pega a la hemoglobina y forma la <b>HbA1c</b>, que refleja cuánta glucosa hubo en los últimos 2–3 meses.</p>'
        + truco('«-itol» = alditol. «Activado» = pegado a un nucleótido. Maillard = glicación = <b>sin enzimas</b>.')))
    H.append(block("Glucógeno, quitina, peptidoglicano y proteoglicanos",
        [("¿Cuál de estas cadenas corresponde al glucógeno?", "Amilopectina", "Glucógeno"),
         ("Sobre quitina y peptidoglicano, ¿qué es correcto?", NS, "La quitina es GlcNAc β(1→4)"),
         ("En un proteoglicano como el agrecano del cartílago:", NS, "Cadenas de GAG se unen a una proteína central")],
        '<p><b>Glucógeno vs amilopectina.</b> Las dos tienen el mismo esqueleto: glucosas α(1→4) con ramas α(1→6). Lo que cambia es <b>cada cuánto</b> hay una rama:</p>'
        + figs("s_amilopectina", "s_glucogeno", cls="figs pf") +
        '<ul><li><b>Amilopectina</b> (almidón de plantas): una rama cada <b>24–30</b> glucosas, con ramas largas y espaciadas.</li><li><b>Glucógeno</b> (animales): una rama cada <b>8–12</b>. Es más ramificado y compacto, y tiene muchos extremos para soltar glucosa rápido.</li></ul>'
        '<p><b>Quitina y peptidoglicano.</b></p>' + figs("s_quitina", "p_peptidoglicano", cls="figs pf") +
        '<ul><li><b>Quitina</b> (exoesqueleto de artrópodos, pared de hongos): <b>GlcNAc β(1→4)</b> repetido. Es como la celulosa, pero con un NHAc en el C2.</li><li><b>Peptidoglicano</b> (pared bacteriana): <b>GlcNAc y MurNAc alternados</b>, β(1→4), con péptidos que unen las cadenas entre sí.</li></ul>'
        '<p><b>Proteoglicano.</b> Es una <b>proteína central (core)</b> a la que se le unen covalentemente <b>muchas cadenas largas de GAG</b>. Es más azúcar que proteína. En el <b>agrecano</b> del cartílago, el core lleva muchas cadenas de condroitín sulfato y queratán sulfato. A su vez, muchos agrecanos se enganchan a una cadena de hialuronano y forman un agregado gigante que atrapa agua y amortigua.</p>'
        + truco('Glucógeno = «más ramificado» (cada 8–12). Quitina = celulosa con NHAc. Proteoglicano = «cepillo»: proteína (el palo) + GAG (las cerdas).')))
    H.append(block("GAG: reconocerlos por sus azúcares",
        [("¿Cuál de estas afirmaciones sobre los GAG es correcta?", NS, "El queratán sulfato no tiene ácido urónico"),
         ("¿Cuál es el ácido L-idurónico (IdoA)?", "GlcA", "IdoA"),
         ("¿Qué GAG tiene esta unidad repetitiva? (hialuronano)", NS, "Hialuronano"),
         ("¿Qué GAG tiene esta unidad repetitiva? (queratán)", "Condroitín sulfato", "Queratán sulfato"),
         ("¿Qué GAG tiene esta unidad repetitiva? (dermatán)", NS, "Dermatán sulfato")],
        '<p>Cada GAG es un disacárido que se repite: <b>[ácido urónico + aminoazúcar]</b>. El truco es mirar <b>dos cosas</b>: qué ácido urónico tiene (GlcA, IdoA o ninguno) y qué aminoazúcar (GlcNAc o GalNAc).</p>'
        '<div class="tbl"><table><tr><th>GAG</th><th>Ácido urónico</th><th>Aminoazúcar</th><th>Sulfato</th><th>Para reconocerlo</th></tr>'
        '<tr><td><b>Hialuronano</b></td><td>GlcA</td><td>GlcNAc</td><td><b>no</b></td><td>El único sin sulfato y sin proteína central</td></tr>'
        '<tr><td><b>Condroitín sulfato</b></td><td>GlcA</td><td><b>GalNAc</b></td><td>sí (4 o 6)</td><td>Como el hialuronano, pero con GalNAc y sulfatos</td></tr>'
        '<tr><td><b>Dermatán sulfato</b></td><td><b>IdoA</b></td><td>GalNAc</td><td>sí</td><td>El condroitín con IdoA en lugar de GlcA</td></tr>'
        '<tr><td><b>Queratán sulfato</b></td><td><b>ninguno</b></td><td>GlcNAc + <b>Gal</b></td><td>sí</td><td>El único <b>sin ácido urónico</b>: tiene galactosa</td></tr>'
        '<tr><td>Heparina / heparán</td><td>IdoA (y GlcA)</td><td>GlcNS</td><td>muchísimo</td><td>El más cargado; N-sulfato</td></tr></table></div>'
        '<p><b>GlcA vs IdoA.</b> El ácido L-idurónico es el <b>epímero en C5</b> del ácido D-glucurónico: el grupo COO⁻ queda del otro lado del anillo. En el dibujo, el IdoA tiene el carboxilo «dado vuelta».</p>'
        + figs("m_glca", "m_idoa") + figs("c_hialuronano", "c_condroitin", "c_dermatan", "c_queratan", cls="figs pf")
        + truco('Buscá primero el urónico. ¿No hay? → <b>queratán</b> (tiene Gal). ¿IdoA + GalNAc? → <b>dermatán</b>. ¿GlcA + GalNAc? → <b>condroitín</b>. ¿GlcA + GlcNAc sin sulfatos? → <b>hialuronano</b>.')))
    H.append('<h3 class="rf-sub">Análisis de glicanos</h3>')
    H.append(block("Aislar y separar polisacáridos",
        [("Partís de un extracto vegetal con proteínas, polisacáridos y sales. ¿Qué secuencia aísla los polisacáridos?", NS, "TCA → etanol 80 % → diálisis"),
         ("Una columna de intercambio aniónico se eluye con 0; 0,3 y 0,6 M de NaCl. El polisacárido del pico de 0,6 M:", "Tiene la mayor carga positiva", "Tiene la mayor densidad de carga negativa"),
         ("El primer pico tiene 5 polisacáridos distintos y el tercero, uno puro. En FACE se espera:", NS, "5 bandas en el primero y 1 en el tercero")],
        '<ol class="flow h"><li class="m">Extracto</li><li class="e">TCA: precipita proteínas (se descartan)</li><li class="m">Sobrenadante</li><li class="e">etanol 80 %: precipita polisacáridos</li><li class="m">Precipitado</li><li class="e">diálisis: salen sales y moléculas chicas</li><li class="m">Polisacáridos</li></ol>'
        '<p>La lógica es ir sacando lo que molesta de a una cosa: primero las <b>proteínas</b> (el TCA las precipita), después se <b>precipitan los polisacáridos</b> con etanol (las cosas chicas quedan disueltas) y al final la <b>diálisis</b> limpia las sales.</p>'
        '<p><b>Intercambio aniónico.</b> La resina tiene cargas <b>positivas</b> y retiene lo <b>negativo</b>. Lo neutro sale enseguida (0 M). La sal compite por la resina: cuanto más negativo es un polisacárido (más carga por unidad de tamaño), más fuerte se pega y <b>más sal hace falta</b> para despegarlo. El pico de 0,6 M es el más negativo. Un polisacárido con carga positiva ni siquiera se pegaría.</p>'
        '<p><b>FACE</b> (electroforesis de carbohidratos con un fluoróforo): cada especie distinta corre a su propia altura y da <b>una banda</b>. Si el pico tiene 5 polisacáridos, se ven 5 bandas; si es puro, 1. Por eso FACE sirve para ver si una fracción está pura.</p>'
        + truco('Intercambio <b>aniónico</b> = atrapa <b>aniones</b>. Más sal para soltarlo = más negativo.')))
    H.append(block("Análisis de metilación (PMAA)",
        [("Aparece 2,3,5,6-tetra-O-metil-galactitol. ¿Qué indica?", NS, "Galactofuranosa terminal"),
         ("Los PMAA de Glc, Man y Gal con iguales sustituyentes dan el mismo espectro de masas. Se distinguen por:", NS, "El tiempo de retención en el GC")],
        '<p>La regla de la metilación: primero se metilan <b>todos los OH libres</b>. Después se hidroliza, se reduce y se acetila. En el producto final:</p>'
        '<ul><li><b>O-metilo</b> = ese carbono tenía el OH <b>libre</b> (no estaba unido a nada).</li><li><b>Acetilo (sin metilo)</b> = ese carbono estaba <b>ocupado</b>: unido a otro azúcar, o formando el anillo.</li></ul>'
        '<div class="tbl"><table><tr><th>Carbono</th><th>C1</th><th>C2</th><th>C3</th><th>C4</th><th>C5</th><th>C6</th></tr>'
        '<tr><td>2,3,5,6-tetra-O-metil-galactitol</td><td>sin metilo</td><td>metilo</td><td>metilo</td><td><b>sin metilo</b></td><td>metilo</td><td>metilo</td></tr>'
        '<tr><td>Interpretación</td><td>enlace glicosídico</td><td>libre</td><td>libre</td><td><b>oxígeno del anillo</b></td><td>libre</td><td>libre</td></tr></table></div>'
        '<p>Solo dos posiciones quedaron sin metilo: el C1 (por donde el azúcar se une a la cadena) y el C4. Si el anillo cierra en el C4, el anillo es de 5 → <b>furanosa</b>. Y como está unida solo por el C1, es <b>terminal</b>. Respuesta: <b>galactofuranosa terminal</b>. Una galactopiranosa terminal daría 2,3,4,6-tetra-O-metil (el anillo cerraría en el C5).</p>'
        '<p><b>¿Por qué no se distinguen por masa?</b> Glc, Man y Gal son estereoisómeros: tienen los mismos átomos y se rompen igual en el espectrómetro. Lo que cambia es cómo interactúan con la columna del <b>cromatógrafo de gases</b>, así que salen a <b>tiempos de retención</b> distintos (se comparan con estándares).</p>'
        + truco('«Metilo = estaba libre; sin metilo = estaba ocupado». Anillo en C4 → furanosa; anillo en C5 → piranosa.')))
    H.append(block("Liberar, purificar y medir glicanos",
        [("Después de la PNGasa F, en el sitio de N-glicosilación queda:", NS, "Ácido aspártico"),
         ("La hidracinólisis a 60 °C libera O-glicanos pero no N-glicanos porque:", "La hidracina solo ataca serinas", "El enlace a Ser/Thr es más lábil"),
         ("Una glicoproteína retenida en una columna de Con A se eluye con:", "NaCl 1 M en el buffer de elución", "α-metilmanósido 100 mM"),
         ("En el cartucho de carbono grafitizado (PGC), ¿qué sale con el lavado de agua?", NS, "Sales y monosacáridos"),
         ("Un glicano en 7,0 GU (Biogel P-4) pierde un residuo con una exoglicosidasa. Ahora sale:", "En el mismo lugar", "En menos GU"),
         ("¿Por qué secuenciar glicanos es más difícil que secuenciar proteínas?", NS, "Se ramifican y no se copian de un molde")],
        '<p><b>PNGasa F.</b> Corta el N-glicano justo en la unión con la asparagina (Asn), y al hacerlo se lleva el N de la amida: la <b>Asn queda convertida en ácido aspártico (Asp)</b>. Ese cambio (+1 de masa) sirve para marcar dónde estaba el glicano.</p>'
        '<p><b>Hidracinólisis.</b> La hidracina no elige aminoácidos: lo que cambia es qué tan fácil se rompe cada unión. La unión O-glicosídica a <b>Ser/Thr es más lábil</b> y se rompe ya a 60 °C. La unión N-glicosídica a Asn es más fuerte y necesita más temperatura. Controlando la temperatura se elige qué liberar.</p>'
        '<p><b>Con A</b> es una lectina que reconoce <b>manosa</b>. La glicoproteína queda pegada por sus manosas, no por cargas: la sal no la despega. Se despega por <b>competencia</b>, con un azúcar libre parecido que ocupa el sitio de la lectina, el <b>α-metilmanósido</b>.</p>'
        '<p><b>PGC</b>: retiene los <b>oligosacáridos</b> (glicanos). Con agua salen las <b>sales y los monosacáridos</b>, que son demasiado chicos para quedarse. Los glicanos se eluyen después con acetonitrilo.</p>'
        '<p><b>GU</b> (unidades de glucosa): en el Biogel P-4 el tamaño se mide comparando con una escalera de glucosas. Si una exoglicosidasa le saca un residuo, el glicano queda <b>más chico → menos GU</b>. Cuánto baja indica qué azúcar se perdió.</p>'
        '<p><b>¿Por qué cuesta secuenciar glicanos?</b> Las proteínas son cadenas lineales copiadas de un molde (el ARNm). Los glicanos se <b>ramifican</b>, sus azúcares se unen por distintos carbonos (1→2, 1→3, 1→4, 1→6, α o β) y <b>no se copian de un molde</b>: dependen de qué enzimas actuaron, por eso hay mucha variedad.</p>'
        + truco('Lectina → se eluye con <b>azúcar</b>. Intercambio iónico → se eluye con <b>sal</b>. PNGasa F: <b>Asn → Asp</b>.')))
    H.append(block("Glicanos en biología: selectinas, influenza y LPS",
        [("Durante la inflamación los leucocitos «ruedan» sobre el endotelio porque:", NS, "Las selectinas reconocen sialyl-Lewis X"),
         ("¿Qué hace la neuraminidasa del virus de la influenza?", NS, "Corta el ácido siálico y libera viriones"),
         ("¿Por qué el LPS es un problema al producir proteínas recombinantes en E. coli?", NS, "Contamina la proteína y causa inflamación")],
        '<ul><li><b>Rolling.</b> En la inflamación, el endotelio expone <b>selectinas</b>, lectinas que reconocen el glicano <b>sialyl-Lewis X</b> de los leucocitos. La unión es débil y se arma y desarma todo el tiempo, así que el leucocito «rueda» frenándose. Después lo detienen las integrinas y sale del vaso.</li>'
        '<li><b>Influenza.</b> La hemaglutinina del virus se pega al <b>ácido siálico</b> de la célula para entrar. Al salir, los virus nuevos quedarían pegados a ese mismo ácido siálico, así que la <b>neuraminidasa lo corta y los libera</b>. El oseltamivir (Tamiflu) bloquea la neuraminidasa.</li>'
        '<li><b>LPS</b> (lipopolisacárido): está en la membrana externa de las bacterias gram negativas como <i>E. coli</i>. Es una <b>endotoxina</b>: si contamina la proteína purificada y se inyecta, causa fiebre e inflamación. Por eso hay que eliminarlo.</li></ul>'
        + truco('Neuraminidasa = «tijera» del ácido siálico para <b>salir</b>. Hemaglutinina = «gancho» para <b>entrar</b>.')))
    H.append(block("Periodato y celulosa",
        [("1 mol de celulosa tratado con periodato produce:", "Depende del largo de la cadena", "3 mol de ácido fórmico")],
        fig_periodato() +
        '<p>El periodato corta entre dos carbonos vecinos que tienen OH. Si hay <b>tres OH seguidos</b>, el del medio sale como <b>ácido fórmico</b>. En la celulosa, los residuos internos (unidos por C1 y C4) solo tienen OH en C2 y C3: se cortan, pero <b>no dan fórmico</b>. Solo los extremos dan fórmico: el no reductor 1 y el reductor 2. Por eso sale siempre <b>3 mol por mol</b>, sin importar el largo.</p>'))
    H.append(practice("G1,G2,GC", "Practicar mis falladas de glúcidos"))

    # ============================== LÍPIDOS
    H.append('<h2>2. Lípidos</h2>')
    H.append(block("Nombrar ácidos grasos: Δ, ω, cis y trans",
        [("El ácido oleico se puede nombrar como:", "18:1 Δ9, ω-6 (trans-9-octadecenoico)", "18:1 Δ9, ω-9 (cis-9-octadecenoico)"),
         ("¿Cuál es el ácido oleico? (imagen)", "Ácido linoleico", "Ácido oleico"),
         ("Si un ácido graso ω-6 se alarga en 2 carbonos:", "Pasa a ser ω-8", "Sigue siendo ω-6"),
         ("Ordená de mayor a menor punto de fusión: 18:1 cis, 18:0, 16:0.", "16:0 > 18:1 cis > 18:0", "18:0 > 16:0 > 18:1 cis")],
        '<ul><li><b>18:1</b> = 18 carbonos, 1 doble enlace.</li><li><b>Δ9</b> = el doble enlace empieza en el C9, <b>contando desde el COOH</b> (C1).</li><li><b>ω-9</b> = el último doble enlace está a 9 carbonos <b>contando desde el CH₃ del final</b>. Cuenta: ω = 18 − 9 = 9.</li><li>Los ácidos grasos naturales tienen dobles enlaces <b>cis</b>; el trans (elaídico) aparece en grasas industriales.</li></ul>'
        + figs("oleico", "elaidico", "linoleico") +
        '<p><b>Oleico vs linoleico:</b> el oleico tiene <b>un</b> doble enlace (18:1, ω-9) y el linoleico <b>dos</b> (18:2 Δ9,12, ω-6). En el dibujo, contá los dobles enlaces.</p>'
        '<p><b>Alargar no cambia el ω.</b> Las elongasas agregan carbonos <b>del lado del COOH</b>. El extremo CH₃ no se toca, así que la distancia desde el CH₃ al doble enlace sigue igual: un ω-6 sigue siendo ω-6 (los números Δ sí suben en 2).</p>'
        '<p><b>Punto de fusión.</b> Dos reglas: cadena <b>más larga</b> → más alto; <b>doble enlace cis</b> → el codo impide empaquetar → mucho más bajo. Entonces: 18:0 (esteárico, ~69 °C) &gt; 16:0 (palmítico, ~63 °C) &gt; 18:1 cis (oleico, ~13 °C, líquido).</p>'
        + truco('Δ se cuenta desde el <b>ácido</b> (COOH), ω desde la <b>cola</b> (CH₃). «ω = total − Δ del último doble enlace». El cis le gana a todo: siempre funde más bajo.')))
    H.append(block("TAG, cargas de los fosfolípidos y esfingomielina",
        [("¿Por qué los TAG son una reserva de energía tan eficiente?", "Porque contienen fosfato", "Carbonos muy reducidos y sin agua"),
         ("¿Cuál tiene carga neta negativa a pH 7?", NS, "Fosfatidilserina"),
         ("Sobre la esfingomielina:", "Es un glicerofosfolípido con colina", "Es ceramida con fosfocolina")],
        '<p><b>TAG.</b> Los triacilglicéridos no tienen fosfato. Rinden mucho por dos razones: sus carbonos están <b>muy reducidos</b> (casi todo CH₂, con mucho para oxidar → ~9 kcal/g contra ~4 de los glúcidos) y se guardan <b>sin agua</b> (el glucógeno arrastra unos 2 g de agua por gramo).</p>'
        '<div class="tbl"><table><tr><th>Fosfolípido</th><th>Cargas de la cabeza a pH 7</th><th>Neta</th></tr>'
        '<tr><td>Fosfatidilcolina (PC)</td><td>fosfato − · colina +</td><td>0</td></tr><tr><td>Fosfatidiletanolamina (PE)</td><td>fosfato − · amino +</td><td>0</td></tr>'
        '<tr><td><b>Fosfatidilserina (PS)</b></td><td>fosfato − · <b>carboxilo −</b> · amino +</td><td><b>−1</b></td></tr><tr><td>Fosfatidilinositol (PI)</td><td>fosfato − · inositol (neutro)</td><td>−1</td></tr></table></div>'
        + figs("pc", "ps", "esfingomielina") +
        '<p>La <b>serina</b> es un aminoácido: aporta un + (amino) y un − (carboxilo), que se cancelan, y queda la carga − del fosfato.</p>'
        '<p><b>Esfingomielina.</b> No tiene glicerol, así que <b>no</b> es un glicerofosfolípido. Es un <b>esfingolípido</b>: esfingosina + un ácido graso unido por amida = <b>ceramida</b>, y a la ceramida se le pega <b>fosfocolina</b>. Tiene la misma cabeza que la PC, pero otro esqueleto.</p>'
        + truco('«Gliceri-» = glicerol; «esfingo-» = esfingosina. PS = la «Serina Suma» un negativo.')))
    H.append(block("Arqueas, esteroles y DHA: la membrana según sus lípidos",
        [("¿Por qué las membranas de las arqueas resisten condiciones extremas?", "Tienen mucho colesterol", "Usan enlaces éter y cadenas isoprenoides"),
         ("Sobre los esteroles, ¿qué es correcto?", NS, "Abundan en la membrana plasmática"),
         ("El DHA abunda en retina y sinapsis porque:", "Hace la membrana más rígida y ordenada, como el colesterol", "Hace la membrana flexible y facilita la fusión")],
        '<ul><li><b>Arqueas.</b> No tienen colesterol. Sus lípidos unen las cadenas al glicerol por <b>enlaces éter</b> (C–O–C), mucho más resistentes a la hidrólisis que los éster. Además, sus cadenas son <b>isoprenoides ramificadas</b>, y algunas atraviesan toda la membrana (monocapa). Eso aguanta calor, ácido y sal.</li>'
        '<li><b>Esteroles</b> (colesterol en animales, ergosterol en hongos): abundan sobre todo en la <b>membrana plasmática</b> (hasta un 30–40 % de sus lípidos) y son escasos en las membranas internas, como la mitocondrial. Regulan la fluidez: amortiguan los cambios con la temperatura.</li>'
        '<li><b>DHA</b> (22:6, ω-3): tiene 6 dobles enlaces cis y sus cadenas son muy flexibles. Hace la membrana <b>más fluida y deformable</b>, lo contrario del colesterol, que ordena. Eso sirve en la retina (la rodopsina cambia de forma) y en las sinapsis (fusión constante de vesículas).</li></ul>'
        + figs("colesterol", "ergosterol")
        + truco('Muchos dobles enlaces = flexible (DHA). Anillos rígidos = ordena (colesterol). Arqueas = <b>éter</b>.')))
    H.append(block("Forma de los lípidos: bicapas, micelas y detergentes",
        [("¿Qué lípido favorece formar micelas?", "Fosfatidiletanolamina (cono)", "Un lisofosfolípido (una sola cola)"),
         ("¿Por qué los detergentes disuelven las membranas?", "Rompen enlaces covalentes de los lípidos", "Forman micelas que se llevan lípidos y proteínas"),
         ("Las nanopartículas lipídicas de las vacunas de ARN funcionan porque:", "El ARN queda en el centro de una micela", "La bicapa se cierra y encierra el ARN")],
        fig_shapes() +
        '<p>La forma de cada lípido decide qué estructura arma:</p><ul><li><b>Cilindro</b> (cabeza y colas del mismo ancho, como la PC) → se apilan planos → <b>bicapa</b>.</li><li><b>Cono</b> (cabeza chica, como la PE) → curva la membrana hacia adentro, pero <b>no</b> forma micelas.</li><li><b>Cono invertido</b> (cabeza grande y <b>una sola cola</b>: lisofosfolípidos, detergentes) → se acomodan en esfera → <b>micela</b>.</li></ul>'
        '<p><b>Detergentes.</b> No rompen enlaces covalentes: son moléculas anfipáticas. Se meten en la bicapa y la desarman en <b>micelas mixtas</b> que se llevan lípidos y proteínas de membrana.</p>'
        '<p><b>Nanopartículas de las vacunas.</b> El centro de una micela son solo colas, totalmente hidrofóbico: ahí <b>no puede ir</b> el ARN, que es muy polar y cargado. El ARN queda encerrado dentro de una partícula lipídica, protegido del medio, como adentro de una bicapa cerrada.</p>'
        + truco('Una cola → micela. Dos colas → bicapa. El centro de una micela no tiene agua: nada polar puede ir ahí.')))
    H.append(block("Asimetría: scramblasa y fosfatidilserina",
        [("En apoptosis aparece fosfatidilserina en la cara externa. ¿Qué la lleva ahí?", NS, "Una scramblasa, sin gastar ATP")],
        '<div class="tbl"><table><tr><th>Proteína</th><th>Qué hace</th><th>¿ATP?</th></tr>'
        '<tr><td>Flipasa</td><td>Lleva lípidos (PS, PE) hacia la cara <b>interna</b></td><td>Sí</td></tr><tr><td>Flopasa</td><td>Lleva lípidos hacia la cara <b>externa</b></td><td>Sí</td></tr>'
        '<tr><td><b>Scramblasa</b></td><td><b>Mezcla</b> en las dos direcciones, a favor del gradiente</td><td><b>No</b></td></tr></table></div>'
        '<p>Normalmente la PS está solo adentro, porque la flipasa la mantiene ahí gastando ATP. En la apoptosis se apaga la flipasa y se activa una <b>scramblasa</b>, que mezcla las dos caras: la PS aparece afuera y funciona como señal de «comeme» para los macrófagos.</p>'
        + truco('<b>Scram</b>blasa = «revuelve» (scramble), y revolver no cuesta energía.')))
    H.append(block("Vía de Kennedy y ciclo de Lands",
        [("En la vía de Kennedy, ¿cómo se forma la fosfatidilcolina?", "Esfingosina + fosfocolina", "DAG + CDP-colina"),
         ("En el ciclo de Lands se cambia:", NS, "La cadena de sn-2"),
         ("¿Por qué el PI de una célula puede terminar muy enriquecido en un tipo de cadena en sn-2?", NS, "Su aciltransferasa prefiere esa cadena")],
        '<ol class="flow h"><li class="m">Colina</li><li class="e">+ ATP</li><li class="m">Fosfocolina</li><li class="e">+ CTP</li><li class="m">CDP-colina</li><li class="e">+ DAG</li><li class="m">Fosfatidilcolina</li></ol>'
        '<p><b>Kennedy</b> fabrica PC (y PE) <b>desde cero</b>: la cabeza se activa pegándose a CTP (CDP-colina) y después se le pasa a un <b>diacilglicerol (DAG)</b>. La esfingosina no participa: es de los esfingolípidos.</p>'
        '<ol class="flow h"><li class="m">Fosfolípido</li><li class="e">fosfolipasa A₂ saca la cadena de sn-2</li><li class="m">Lisofosfolípido</li><li class="e">aciltransferasa pone otra cadena</li><li class="m">Fosfolípido remodelado</li></ol>'
        '<p><b>Lands</b> no fabrica: <b>remodela</b>. Cambia la cadena de la posición <b>sn-2</b> (la del medio del glicerol). Cada clase de fosfolípido tiene su aciltransferasa (LPCAT para PC, LPIAT para PI). Si esa enzima <b>prefiere</b> un tipo de cadena (por ejemplo el araquidónico), cada vuelta del ciclo la va enriqueciendo en esa cadena.</p>'
        + truco('Kennedy = <b>fabricar</b> (DAG + CDP-colina). Lands = <b>retocar</b> el sn-2 (PLA₂ saca, aciltransferasa pone).')))
    H.append(block("Extracción de lípidos: Folch",
        [("¿Qué mezcla de extracción usa el método de Folch?", "Cloroformo : metanol 1:1", "Cloroformo : metanol 2:1")],
        '<p><b>Folch</b>: cloroformo : metanol <b>2:1</b>. El metanol rompe las uniones de los lípidos con las proteínas y el cloroformo los disuelve. Al agregar agua (o una solución salina) se separan dos fases y los lípidos quedan en la de <b>abajo</b> (cloroformo).</p>'
        + truco('Folch: «<b>2</b> de cloro, <b>1</b> de meta» (más cloroformo).')))
    H.append(practice("L", "Practicar mis falladas de lípidos"))

    # ============================== AN I
    H.append('<h2>3. Ácidos nucleicos I</h2>')
    H.append(block("Nombres y azúcares: nucleósido vs nucleótido",
        [("Adenina + ribosa + un fosfato en 5′ se llama:", "Adenosina", "AMP"),
         ("¿Cuál es el azúcar del ADN?", "Fructofuranosa", "2-desoxirribosa"),
         ("¿Por qué el ARN se hidroliza fácil en medio alcalino y el ADN no?", "Porque es de cadena simple", "Su 2′-OH ataca el fosfodiéster vecino")],
        '<div class="tbl"><table><tr><th>Partes</th><th>Se llama</th><th>Ejemplo</th></tr><tr><td>Base sola</td><td>base</td><td>adenina</td></tr>'
        '<tr><td>Base + azúcar</td><td><b>nucleósido</b></td><td>adenosina</td></tr><tr><td>Base + azúcar + fosfato(s)</td><td><b>nucleótido</b></td><td><b>AMP</b> (1 P), ADP (2), ATP (3)</td></tr></table></div>'
        + figs("adenina", "adenosina", "amp") +
        '<p><b>Azúcar del ADN: 2-desoxirribosa</b>, una pentosa en forma de furanosa (anillo de 5) a la que le falta el OH del C2′. La fructofuranosa es una cetohexosa (la de la sacarosa).</p>' + figs("h_brib", "h_bdrib") +
        '<p><b>ARN y álcali.</b> El ARN tiene un <b>OH en el 2′</b>, justo al lado del enlace fosfodiéster. En medio alcalino ese OH ataca al fósforo vecino, se forma un fosfato cíclico 2′,3′ y la cadena se corta. El ADN no tiene ese OH, así que resiste. Que el ARN sea de cadena simple no es la razón: la clave es el 2′-OH.</p>'
        + truco('«Nucleó<b>s</b>ido = <b>s</b>in fosfato; nucleó<b>t</b>ido = <b>t</b>iene fosfato». Termina en «-osina» o «-idina» → nucleósido; «-MP, -DP, -TP» → nucleótido.')))
    H.append(block("Historia: Miescher, tetranucleótido y Hershey-Chase",
        [("Después de que Miescher aisló la «nucleína», el siguiente avance fue:", NS, "Describir sus componentes y sus 5 bases"),
         ("¿Por qué la hipótesis del tetranucleótido hacía ver al ADN incapaz de ser material genético?", "Decía que el ADN no tenía grupos fosfato en su estructura", "Implicaba una secuencia repetitiva y monótona"),
         ("Hershey y Chase: tras infectar, licuar y centrifugar:", "El ³⁵S queda en el pellet con las bacterias", "El ³²P queda en el pellet con las bacterias")],
        '<ol class="flow"><li class="m">Miescher (1869): aísla la «nucleína» de núcleos de pus</li><li class="m">Kossel: describe sus componentes (azúcar, fosfato y 5 bases: A, G, C, T, U)</li><li class="m">Levene: hipótesis del tetranucleótido</li><li class="m">Griffith (1928): «principio transformante»</li><li class="m">Avery, MacLeod y McCarty (1944): ese principio es ADN</li><li class="m">Chargaff (1950): A = T y G = C, y la composición cambia entre especies</li><li class="m">Hershey y Chase (1952)</li><li class="m">Franklin y Wilkins (Foto 51) → Watson y Crick (1953)</li></ol>'
        '<p><b>Tetranucleótido (Levene).</b> Proponía que el ADN era la misma unidad de 4 nucleótidos (uno de cada base) repetida una y otra vez: <b>ATGC-ATGC-ATGC…</b>. Una secuencia así de monótona no puede guardar información, como un libro que repite siempre las mismas 4 letras. Por eso se pensaba que el material genético eran las proteínas. Chargaff la tiró abajo al mostrar que las proporciones de bases cambian entre especies.</p>'
        + fig_hershey() +
        '<p><b>Hershey y Chase.</b> El <b>azufre (³⁵S)</b> está en las proteínas y no en el ADN. El <b>fósforo (³²P)</b> está en el ADN y no en las proteínas. Al licuar, se despegan las cápsides vacías que quedaron afuera. Al centrifugar, las bacterias (pesadas) van al <b>pellet</b> y las cápsides quedan en el sobrenadante. El ³²P termina en el pellet porque el ADN <b>entró</b> a la bacteria.</p>'
        + truco('<b>S</b> → prote<b>í</b>na (cisteína y metionina tienen S) → se queda <b>afuera</b>. <b>P</b> → ADN (fosfatos) → entra → <b>pellet</b>.')))
    H.append(block("Cálculos con bases (Chargaff)",
        [("Bicatenario de 1000 pb con 58 % de G+C. ¿Cuántas bases de cada tipo?", "G = C = 290; A = T = 210", "G = C = 580; A = T = 420"),
         ("Un ADN bicatenario tiene 22 % de G. ¿Cuánto tiene de A?", "56 %", "28 %"),
         ("La complementaria de 5′-ATGCCA-3′, escrita 5′→3′, es:", "5′-UGGCAU-3′", "5′-TGGCAT-3′"),
         ("6 pg de ADN por célula y 2 × 10¹² células. ¿ADN total?", NS, "12 g")],
        '<p><b>1000 pb son 2000 bases</b>: cada par tiene dos. Ese fue el error.</p><ul><li>G + C = 58 % de 2000 = 1160 → G = C = <b>580</b>.</li><li>A + T = 42 % de 2000 = 840 → A = T = <b>420</b>.</li><li>Control: 580 + 580 + 420 + 420 = 2000 ✓</li></ul>'
        '<p><b>22 % de G:</b> por Chargaff, C también es 22 % → G + C = 44 %. Lo que queda (56 %) es A + T, repartido en partes iguales → <b>A = 28 %</b>. El 56 % es A + T junto, no la A sola.</p>'
        '<p><b>Complementaria en 5′→3′</b>, en dos pasos:</p><ol><li>Se escribe la complementaria debajo (antiparalela): 5′-ATGCCA-3′ → <b>3′-TACGGT-5′</b>.</li><li>Se da vuelta para leerla 5′→3′: <b>5′-TGGCAT-3′</b>.</li></ol><p>Es ADN, así que va <b>T</b>, nunca U.</p>'
        '<p><b>6 pg × 2 × 10¹² = 12 × 10¹² pg.</b> Como 1 pg = 10⁻¹² g, eso da <b>12 g</b>.</p>'
        + truco('Siempre: «pb × 2 = bases». A = T y G = C. Complementaria: complemento, dar vuelta, nunca U en el ADN. pico = 10⁻¹².')))
    H.append(block("La Foto 51 y la forma B",
        [("En este esquema de la Foto 51, ¿qué te dice la fila marcada (la 4.ª que falta)?", NS, "Que hay dos cadenas desplazadas"),
         ("La separación entre las filas horizontales de manchas corresponde a:", "La distancia entre bases (3,4 Å)", "Lo que mide una vuelta (34 Å)"),
         ("En el ADN B, una vuelta mide y contiene:", "3,4 Å y 1 pb", "34 Å y unos 10 pb")],
        figs("f51_2", "f51_3", "f51_4", cls="figs pf") +
        '<p>En la foto, una distancia <b>grande</b> en la molécula aparece <b>cerca del centro</b>, y una <b>chica</b>, <b>lejos</b> del centro.</p>'
        '<ul><li><b>Separación entre filas (cerca del centro)</b> → distancia grande → <b>34 Å</b>, lo que mide una vuelta de la hélice.</li><li><b>Manchas fuertes arriba y abajo (lejos del centro)</b> → distancia chica → <b>3,4 Å</b>, la separación entre pares de bases apilados. Caen en la fila 10.</li><li>Entonces, 34 ÷ 3,4 = <b>10 pb por vuelta</b>.</li><li><b>La 4.ª fila falta</b> porque hay <b>dos cadenas</b> corridas 3/8 de vuelta: en esa fila lo que dispersa una cancela a la otra. Ese corrimiento también arma el surco mayor y el menor.</li></ul>'
        + truco('«3,4 Å entre bases, 34 Å por vuelta, 10 pb por vuelta». Fila que falta = dos cadenas.') +
        '<p>La explicación completa, con el esquema interactivo, está en Ác. nucleicos I → «La Foto 51, detalle por detalle».</p>'))
    H.append(practice("N", "Practicar mis falladas de ácidos nucleicos I"))

    # ============================== AN II
    H.append('<h2>4. Ácidos nucleicos II</h2>')
    H.append(block("Replicación: cebador y bidireccionalidad",
        [("¿Por qué la ADN polimerasa necesita un cebador?", "Necesita el cebador para reconocer la cadena molde", "Solo alarga un 3′-OH ya existente"),
         ("Que la replicación sea bidireccional significa que:", "Se sintetiza a la vez en sentido 5′→3′ y 3′→5′", "Del origen salen dos horquillas opuestas")],
        '<p>La ADN polimerasa reconoce el molde sin problema. Lo que <b>no puede</b> es arrancar de cero: solo sabe <b>agregar</b> un nucleótido al <b>3′-OH</b> de una cadena que ya existe. El cebador (de ARN, hecho por la primasa) le da ese primer 3′-OH.</p>'
        '<p><b>Bidireccional</b> habla de las <b>horquillas</b>, no del sentido químico: desde el origen se abre una burbuja y salen <b>dos horquillas</b> en direcciones opuestas. La síntesis es <b>siempre 5′→3′</b>: ninguna polimerasa sintetiza 3′→5′.</p>'
        + truco('«Bi-direccional = dos horquillas». «5′→3′ siempre, sin excepción».')))
    H.append(block("Transcripción y traducción",
        [("En la terminación independiente de Rho, ¿qué suelta a la polimerasa?", "La proteína Rho, que corre por el ARN hasta alcanzarla", "Una horquilla en el ARN y varias U"),
         ("¿A qué sitio del ribosoma entra el ARNt iniciador?", "Al sitio A, como todos", "Al sitio P"),
         ("¿Por qué se dice que el ribosoma es una ribozima?", "Porque sus proteínas catalizan el enlace peptídico", "Su ARNr cataliza el enlace peptídico")],
        '<p><b>Independiente de Rho</b> quiere decir <b>sin</b> Rho. El propio ARN forma una <b>horquilla</b> (una zona rica en G-C que se aparea consigo misma), seguida de varias <b>U</b>. La horquilla traba a la polimerasa y el apareamiento U-A, que es débil, se suelta. La que usa Rho es la <b>dependiente</b> de Rho.</p>'
        '<p><b>ARNt iniciador → sitio P.</b> Es la excepción: todos los demás aminoacil-ARNt entran por el <b>A</b>. El iniciador se ubica directo en el P durante la iniciación, así el sitio A queda libre para el segundo aminoácido.</p>'
        '<p><b>Ribozima</b> = enzima hecha de ARN. En el ribosoma, el enlace peptídico lo cataliza el <b>ARNr</b> de la subunidad mayor (la peptidil transferasa), no sus proteínas.</p>'
        + truco('«Independiente de Rho = horquilla + U». Iniciador = el único que entra por la Puerta P. Ribozima = <b>ribo</b> (ARN) + en<b>zima</b>.') +
        '<p>Para verlo en movimiento: Ác. nucleicos II · simple, videos de transcripción (pasos 8–9) y traducción (pasos 4–6).</p>'))
    H.append(block("Nucleótidos: importación, uracilo en el ADN y alopurinol",
        [("¿Cuál es la ruta principal de importación de bases y nucleótidos?", NS, "Digerir los ácidos nucleicos de la dieta"),
         ("¿Qué enzima saca el uracilo que aparece en el ADN?", "La dUTPasa, antes de que entre", "La uracilo-ADN glicosilasa"),
         ("Con alopurinol se acumulan hipoxantina y xantina. ¿Por qué no es un problema?", "Porque se convierten en pirimidinas", "Son más solubles que el ácido úrico")],
        '<p><b>Importación:</b> la mayoría de las bases y nucleótidos que entran al cuerpo vienen de <b>digerir los ácidos nucleicos de la comida</b> (hidrólisis extracelular en el intestino).</p>'
        '<div class="tbl"><table><tr><th></th><th>dUTPasa</th><th>Uracilo-ADN glicosilasa</th></tr><tr><td>¿Cuándo actúa?</td><td><b>Antes</b>: sobre el dUTP libre</td><td><b>Después</b>: sobre la U ya metida en el ADN</td></tr>'
        '<tr><td>¿Qué hace?</td><td>Rompe dUTP → dUMP, para que no entre U</td><td>Saca la base U del ADN para que la reparación ponga C</td></tr><tr><td>Tipo</td><td>Prevención</td><td>Reparación</td></tr></table></div>'
        '<p><b>Alopurinol.</b> Bloquea la xantina oxidasa, así que se forma menos ácido úrico y se acumulan hipoxantina y xantina. No hay problema porque son <b>más solubles</b> que el ácido úrico: se eliminan por la orina sin formar cristales. Las purinas nunca se convierten en pirimidinas.</p>'
        + truco('dUTPasa = <b>portero</b> (no deja entrar U). Glicosilasa = <b>limpieza</b> (saca la U que ya entró).')))
    H.append(practice("NM", "Practicar mis falladas de ácidos nucleicos II"))
    H.append('</section>\n')
    return "".join(H)

if __name__ == "__main__":
    open("t_rf.html", "w").write(build())
    print("ok")
