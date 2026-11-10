"""Foto 51: esquema del patrón de difracción, hélice con medidas, subsección de teoría y figuras para preguntas."""
import math, json

C = (180, 205)          # centro del patrón
S = 17                  # separación entre líneas de capa (px)
AX = lambda l: 8 + 11 * l  # distancia de la mancha al eje en la línea l

def photo(on=None, callouts=True, layers=True, cls=""):
    cx, cy = C
    o = [f"<svg viewBox='0 0 360 410' class='f51p {cls}'" + (f" data-on='{on}'" if on else "") +
         " role='img' aria-label='Esquema de la Foto 51: patrón de difracción en forma de X'>"]
    o.append("<rect x='30' y='10' width='300' height='390' rx='14' class='film'/>")
    # rombos (debajo de todo)
    for d in (-1, 1):
        o.append(f"<polygon points='{cx},{cy+d*14} {cx-AX(9)},{cy+d*9*S} {cx},{cy+d*10*S} {cx+AX(9)},{cy+d*9*S}' class='hl hl6 dia'/>")
    # manchas
    for d in (-1, 1):
        for l in range(1, 10):
            if l == 4:
                continue
            r = max(1.8, 5.2 - 0.38 * l)
            op = max(0.35, 1 - 0.07 * l)
            y = cy + d * l * S
            for sx in (-1, 1):
                o.append(f"<ellipse cx='{cx+sx*AX(l)}' cy='{y}' rx='{r+1.5:.1f}' ry='{r:.1f}' class='spot' opacity='{op:.2f}'/>")
        y = cy + d * 10 * S
        o.append(f"<ellipse cx='{cx}' cy='{y}' rx='34' ry='6' class='spot mer'/>")
    o.append(f"<circle cx='{cx}' cy='{cy}' r='11' class='stop'/>")
    # resaltados
    o.append(f"<g class='hl hl1'><line x1='{cx-AX(9)-8}' y1='{cy-9*S-6}' x2='{cx+AX(9)+8}' y2='{cy+9*S+6}' class='hlline'/><line x1='{cx+AX(9)+8}' y1='{cy-9*S-6}' x2='{cx-AX(9)-8}' y2='{cy+9*S+6}' class='hlline'/></g>")
    x2 = cx + AX(3) + 22
    o.append(f"<g class='hl hl2'>" + "".join(f"<line x1='40' y1='{cy-l*S}' x2='320' y2='{cy-l*S}' class='hlthin'/>" for l in (1, 2, 3)) +
             f"<line x1='{x2}' y1='{cy-S}' x2='{x2}' y2='{cy-2*S}' class='hlbr'/><text x='{x2+6}' y='{cy-1.5*S+4}' class='hlt'>1 vuelta (34 Å)</text></g>")
    o.append(f"<g class='hl hl3'><ellipse cx='{cx}' cy='{cy-10*S}' rx='46' ry='13' class='hlring'/><ellipse cx='{cx}' cy='{cy+10*S}' rx='46' ry='13' class='hlring'/><text x='{cx+52}' y='{cy-10*S+5}' class='hlt'>3,4 Å</text></g>")
    o.append(f"<g class='hl hl4'><rect x='40' y='{cy-4*S-7}' width='280' height='14' rx='7' class='hlband'/><rect x='40' y='{cy+4*S-7}' width='280' height='14' rx='7' class='hlband'/><text x='{cx}' y='{cy-4*S+4}' text-anchor='middle' class='hlt'>acá no hay nada</text></g>")
    o.append(f"<g class='hl hl5'><line x1='{cx}' y1='{cy-S}' x2='{cx+AX(1)}' y2='{cy-S}' class='hlbr'/><line x1='{cx}' y1='{cy-2*S}' x2='{cx+AX(2)}' y2='{cy-2*S}' class='hlbr'/><text x='{cx+AX(2)+10}' y='{cy-2*S+4}' class='hlt'>ancho → 20 Å</text></g>")
    # números de línea de capa
    if layers:
        for l in range(1, 11):
            y = cy - l * S + 4
            k = " miss" if l == 4 else ""
            o.append(f"<text x='46' y='{y}' text-anchor='middle' class='ln{k}'>{l}</text>")
        o.append(f"<text x='46' y='{cy+4}' text-anchor='middle' class='ln'>0</text>")
    if callouts:
        pts = {1: (cx + AX(7) + 16, cy - 7 * S - 10), 2: (300, cy + 2 * S), 3: (cx - 52, cy - 10 * S + 2),
               4: (300, cy - 4 * S), 5: (cx + AX(1) + 14, cy - S + 14), 6: (cx, cy - 6 * S)}
        for k, (x, y) in pts.items():
            o.append(f"<g class='co' data-k='{k}'><circle cx='{x}' cy='{y}' r='11'/><text x='{x}' y='{y+4.5}' text-anchor='middle'>{k}</text></g>")
    o.append("</svg>")
    return "".join(o)

def helix(on=None):
    W, H = 320, 410
    ax, r, P, y0 = 150, 95, 340, 40
    def xs(y, ph):
        return ax + r * math.sin(2 * math.pi * (y - y0) / P - ph)
    o = [f"<svg viewBox='0 0 {W} {H}' class='f51h'" + (f" data-on='{on}'" if on else "") + " role='img' aria-label='Doble hélice B con sus medidas'>"]
    # bases (10 por vuelta)
    for k in range(10):
        y = y0 + 17 + 34 * k
        o.append(f"<line x1='{xs(y,0):.1f}' y1='{y}' x2='{xs(y,2*math.pi*3/8):.1f}' y2='{y}' class='rung'/>")
    for ph, cl in ((0, 's1'), (2 * math.pi * 3 / 8, 's2')):
        pts = " ".join(f"{xs(y,ph):.1f},{y}" for y in range(y0, y0 + P + 1, 4))
        o.append(f"<polyline points='{pts}' class='strand {cl}'/>")
    # 1: inclinación de los tramos
    o.append(f"<g class='hl hl1'><line x1='{xs(y0+60,0)-30:.0f}' y1='{y0+60-38}' x2='{xs(y0+60,0)+30:.0f}' y2='{y0+60+38}' class='hlline'/><line x1='{xs(y0+230,0)+30:.0f}' y1='{y0+230-38}' x2='{xs(y0+230,0)-30:.0f}' y2='{y0+230+38}' class='hlline'/><text x='{W-10}' y='{y0+150}' text-anchor='end' class='hlt'>tramos inclinados</text><text x='{W-10}' y='{y0+166}' text-anchor='end' class='hlt'>hacia los 2 lados</text></g>")
    # 2: paso 34 Å
    o.append(f"<g class='hl hl2'><line x1='{W-24}' y1='{y0}' x2='{W-24}' y2='{y0+P}' class='hlbr'/><line x1='{W-32}' y1='{y0}' x2='{W-16}' y2='{y0}' class='hlbr'/><line x1='{W-32}' y1='{y0+P}' x2='{W-16}' y2='{y0+P}' class='hlbr'/><text x='{W-30}' y='{y0+P/2}' text-anchor='end' class='hlt'>1 vuelta = 34 Å</text></g>")
    # 3: 3,4 Å entre bases
    ya, yb = y0 + 17 + 34 * 4, y0 + 17 + 34 * 5
    o.append(f"<g class='hl hl3'><line x1='{ax}' y1='{ya}' x2='{ax}' y2='{yb}' class='hlbr'/><text x='{ax+8}' y='{(ya+yb)/2+4}' class='hlt'>3,4 Å</text><line x1='{xs(ya,0):.1f}' y1='{ya}' x2='{xs(ya,2*math.pi*3/8):.1f}' y2='{ya}' class='hlline'/><line x1='{xs(yb,0):.1f}' y1='{yb}' x2='{xs(yb,2*math.pi*3/8):.1f}' y2='{yb}' class='hlline'/></g>")
    # 4: surcos (desfase 3/8)
    yA = y0 + P / 2  # cruce de s1 por el eje (bajando)
    ys1 = [y0 + P * f for f in (0, 0.5, 1)]
    ys2 = [y0 + P * (f + 3 / 8) for f in (0, 0.5) if y0 + P * (f + 3 / 8) <= y0 + P]
    o.append(f"<g class='hl hl4'><line x1='{ax-50}' y1='{y0+P*0.5}' x2='{ax-50}' y2='{y0+P*0.875}' class='hlbr'/><text x='{ax-56}' y='{y0+P*0.69}' text-anchor='end' class='hlt'>surco</text><text x='{ax-56}' y='{y0+P*0.69+15}' text-anchor='end' class='hlt'>menor (3/8)</text>"
             f"<line x1='{ax-50}' y1='{y0+P*0.875}' x2='{ax-50}' y2='{y0+P*1.0}' class='hlbr2'/><line x1='{ax-50}' y1='{y0}' x2='{ax-50}' y2='{y0+P*0.375}' class='hlbr2'/>"
             f"<text x='{ax-56}' y='{y0+P*0.2}' text-anchor='end' class='hlt'>surco</text><text x='{ax-56}' y='{y0+P*0.2+15}' text-anchor='end' class='hlt'>mayor</text></g>")
    # 5: diámetro
    o.append(f"<g class='hl hl5'><line x1='{ax-r}' y1='{y0-18}' x2='{ax+r}' y2='{y0-18}' class='hlbr'/><text x='{ax}' y='{y0-24}' text-anchor='middle' class='hlt'>diámetro ≈ 20 Å</text></g>")
    # 6: esqueleto afuera
    o.append(f"<g class='hl hl6'><text x='{ax+r+6}' y='{y0+P*0.25+4}' class='hlt'>fosfatos</text><text x='{ax+r+6}' y='{y0+P*0.25+19}' class='hlt'>afuera</text><text x='{ax}' y='{y0+P*0.62}' text-anchor='middle' class='hlt bgt'>bases adentro</text></g>")
    o.append("</svg>")
    return "".join(o)

FEAT = [
    (1, "La cruz en X", "La molécula es una <b>hélice</b>.",
     "Vista de costado, una hélice se ve como un zigzag: tramos que suben inclinados hacia un lado y tramos inclinados hacia el otro. Cada dirección de tramo dispersa los rayos X formando una fila de manchas perpendicular a ese tramo. Dos direcciones dan dos filas cruzadas: la X.",
     "Qué tan abiertos están los brazos de la X indica cuánto se inclinan las cadenas: eso depende de la relación entre lo que mide la vuelta y el radio."),
    (2, "Líneas horizontales de manchas (líneas de capa)", "Cada vuelta de la hélice mide <b>34 Å</b>.",
     "Las manchas no están sueltas: se acomodan en filas horizontales, a la misma distancia una de otra. Esa separación corresponde a lo que tarda la hélice en repetirse, o sea una vuelta completa. Como la relación es inversa, filas muy juntas significan una repetición larga: 34 Å.",
     None),
    (3, "Manchas fuertes arriba y abajo, en el eje (el meridiano)", "Las bases están apiladas cada <b>3,4 Å</b>, y hay <b>10 por vuelta</b>.",
     "Son las manchas más lejanas del centro, así que corresponden a la distancia más chica que se repite: 3,4 Å, la separación entre pares de bases apilados como monedas. Caen justo en la línea de capa número 10: 34 Å ÷ 3,4 Å = 10 pares de bases por vuelta.",
     None),
    (4, "Falta la 4.ª línea", "Hay <b>dos cadenas</b>: es una doble hélice.",
     "Contá las filas desde el centro hacia arriba: 1, 2, 3… y la cuarta no está (después siguen la 5, la 6…). Con una sola cadena estarían todas. Con dos cadenas desplazadas una respecto de la otra, lo que dispersa cada cadena se suma en algunas filas y se anula en otras. Justo en la cuarta se anula del todo: esa ausencia delata la segunda cadena.",
     "Para que se anule la 4.ª línea, la segunda cadena tiene que estar corrida 3/8 de vuelta (no media vuelta). Por eso las dos cadenas no quedan equidistantes y aparecen un <b>surco menor</b> (3/8 de vuelta) y un <b>surco mayor</b> (5/8)."),
    (5, "Qué tan lejos del eje vertical están las primeras manchas", "El <b>diámetro</b> de la hélice es de unos <b>20 Å</b>.",
     "La distancia horizontal entre el eje y las manchas de las primeras filas depende del radio de la hélice. De ahí sale un diámetro de unos 20 Å, el mismo que da un par purina–pirimidina entre los dos esqueletos.",
     None),
    (6, "Los rombos vacíos", "Los <b>fosfatos están afuera</b> y las bases adentro.",
     None,
     "Arriba y abajo del centro, entre los brazos de la X, queda una zona sin manchas con forma de rombo. Ese hueco aparece cuando la mayor parte de los electrones (los fosfatos, con átomos de P) está en el radio externo de la hélice. Es otra evidencia de que el esqueleto azúcar-fosfato va por fuera."),
]

def section():
    cards = []
    for n, what, means, why, extra in FEAT:
        body = f"<p class='f51m'>{means}</p>"
        if why:
            body += f"<p>{why}</p>"
        if extra:
            body += f"<p class='f51x'><span class='xtag'>Para entender mejor</span> {extra}</p>"
        cards.append(f"<div class='cd f51c' data-n='{n}'><h4><span class='num'>{n}</span>{what}</h4>{body}</div>")
    chips = "".join(f"<button class='chip' type='button' data-f51='{n}' aria-pressed='false'><span class='num'>{n}</span>{FEAT[n-1][1]}</button>" for n in range(1, 7))
    return f'''
<h3>La Foto 51, detalle por detalle</h3>
<p>La Foto 51 no es una foto de la molécula: es la «sombra» que dejan los rayos X después de atravesar fibras de ADN. Cuando algo se repite muchas veces a la misma distancia (las vueltas de una hélice, las bases apiladas), los rayos desviados se suman en ciertas direcciones y dejan una mancha en la película. Mirando <b>dónde</b> caen las manchas se deducen las distancias que se repiten en la molécula.</p>
<div class="box why"><b>La regla de oro: es al revés.</b> Lo que está <b>lejos del centro</b> de la foto corresponde a distancias <b>chicas</b> en la molécula, y lo que está cerca del centro, a distancias grandes. Es la ley de Bragg: nλ = 2d·sen θ. Si d (la distancia que se repite) es chica, el ángulo θ tiene que ser grande.</div>
<p class="note">Tocá un número para ver dónde está cada detalle en la foto y qué le corresponde en la hélice. A la izquierda de la foto están numeradas las filas de manchas desde el centro.</p>
<div class="f51wrap">
  <div class="chips f51chips">{chips}<button class="chip" type="button" data-f51="0">Ver sin marcas</button></div>
  <div class="f51pair">
    <figure class="f51fig"><figcaption>Lo que se ve (esquema de la Foto 51)</figcaption>{photo()}</figure>
    <figure class="f51fig"><figcaption>Lo que significa (forma B del ADN)</figcaption>{helix()}</figure>
  </div>
  <div class="cards f51cards">{"".join(cards)}</div>
</div>
<div class="tbl"><table>
<tr><th>#</th><th>Lo que se ve</th><th>Lo que significa</th></tr>
{"".join(f"<tr><td>{n}</td><td>{w}</td><td>{m}</td></tr>" for n, w, m, _, _ in FEAT)}
</table></div>
<h4 class="sub">Ley de Bragg con los números del ADN</h4>
<p>Con rayos X de cobre (λ ≈ 1,54 Å) y n = 1, se despeja d = λ / (2·sen θ). En la película se mide el ángulo 2θ:</p>
<div class="tbl"><table>
<tr><th>Mancha a 2θ</th><th>θ</th><th>d</th><th>Qué es</th></tr>
<tr><td>26,2° (lejos del centro)</td><td>13,1°</td><td>≈ 3,4 Å</td><td>Separación entre bases apiladas</td></tr>
<tr><td>4,0°</td><td>2,0°</td><td>≈ 22 Å</td><td>Del orden del diámetro</td></tr>
<tr><td>2,6° (cerca del centro)</td><td>1,3°</td><td>≈ 34 Å</td><td>Una vuelta de la hélice</td></tr>
</table></div>
<div class="box trap"><b>Ojo</b> La X dice «hélice», no «doble hélice». Lo que dice que hay <b>dos</b> cadenas es la 4.ª línea que falta. Y las manchas de 3,4 Å son las <b>más lejanas</b> del centro, justamente porque 3,4 Å es la distancia más chica.</div>
'''

if __name__ == "__main__":
    t = open("t_n.html").read()
    if "La Foto 51, detalle por detalle" in t:
        a = t.index("\n<h3>La Foto 51, detalle por detalle</h3>")
        b = t.index("<div class=\"tbl\"><table>\n<tr><th>Rasgo del modelo B</th>")
        t = t[:a] + t[b:]
    anchor = '<div class="tbl"><table>\n<tr><th>Rasgo del modelo B</th>'
    assert t.count(anchor) == 1
    t = t.replace(anchor, section() + "\n" + anchor)
    open("t_n.html", "w").write(t)
    extra = {f"f51_{k}": {"name": "", "svg": photo(on=str(k), callouts=False, layers=(k == 4), cls="q")} for k in range(1, 7)}
    extra["f51_0"] = {"name": "", "svg": photo(callouts=False, layers=True, cls="q")}
    open("f51.js", "w").write("Object.assign(MOL," + json.dumps(extra, ensure_ascii=False) + ");\n")
    print("ok")
