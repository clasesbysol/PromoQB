"""Reemplaza el párrafo del ciclo de Lands en t_l.html por una subsección con esquema."""

def tail(x, y, kind, L=110):
    """Cola hacia abajo desde (x, y). kind: 'sat', 'mono', 'poly'."""
    if kind == 'sat':
        return f"<line x1='{x}' y1='{y}' x2='{x}' y2='{y+L}' class='tl sat'/>"
    if kind == 'mono':
        pts = [(x, y), (x, y + 50), (x + 14, y + 66), (x + 14, y + L)]
        cls = 'mono'
    else:
        pts = [(x, y)]
        yy = y
        dx = 0
        for i in range(5):
            yy += 20
            dx = 12 if i % 2 == 0 else 0
            pts.append((x + dx, yy))
        pts.append((x + dx, y + L))
        cls = 'poly'
    return "<polyline points='" + " ".join(f"{a},{b}" for a, b in pts) + f"' class='tl {cls}'/>"

def lipid(cx, top, head, sn1, sn2, label, sub):
    o = []
    o.append(f"<circle cx='{cx}' cy='{top+18}' r='18' class='hd'/><text x='{cx}' y='{top+22}' text-anchor='middle' class='hdt'>{head}</text>")
    o.append(f"<line x1='{cx}' y1='{top+36}' x2='{cx}' y2='{top+48}' class='tl sat'/>")
    o.append(f"<rect x='{cx-26}' y='{top+48}' width='52' height='16' rx='4' class='gly'/>")
    o.append(f"<text x='{cx-40}' y='{top+60}' text-anchor='end' class='sn'>sn-1</text>")
    o.append(f"<text x='{cx+40}' y='{top+60}' text-anchor='start' class='sn'>sn-2</text>")
    if sn1:
        o.append(tail(cx - 13, top + 64, sn1))
    if sn2:
        o.append(tail(cx + 13, top + 64, sn2))
    else:
        o.append(f"<text x='{cx+16}' y='{top+100}' class='hole'>OH</text>")
    o.append(f"<text x='{cx}' y='{top+200}' text-anchor='middle' class='nm'>{label}</text>")
    o.append(f"<text x='{cx}' y='{top+218}' text-anchor='middle' class='sb'>{sub}</text>")
    return "".join(o)

W, H = 760, 365
o = [f"<svg viewBox='0 0 {W} {H}' class='lands' role='img' aria-label='Ciclo de Lands: la fosfolipasa A2 saca la cadena de sn-2 y una aciltransferasa pone otra'>",
     "<defs><marker id='lah' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='7' markerHeight='7' orient='auto-start-reverse'><path d='M0,0 L10,5 L0,10 z' class='arh'/></marker></defs>"]
o.append(lipid(100, 30, "PC", 'sat', 'mono', "Fosfatidilcolina", "16:0 en sn-1 · 18:1 en sn-2"))
o.append(lipid(380, 30, "PC", 'sat', None, "Liso-PC", "le falta la cadena de sn-2"))
o.append(lipid(660, 30, "PC", 'sat', 'poly', "PC remodelada", "16:0 en sn-1 · 20:4 en sn-2"))
o.append("<line x1='172' y1='110' x2='308' y2='110' class='ar' marker-end='url(#lah)'/>")
o.append("<text x='240' y='98' text-anchor='middle' class='en'>1 · Fosfolipasa A₂</text>")
o.append("<text x='240' y='130' text-anchor='middle' class='sb'>+ H₂O</text>")
o.append("<line x1='240' y1='138' x2='240' y2='166' class='ar' marker-end='url(#lah)'/>")
o.append("<polyline points='232,172 232,190 246,202 246,226' class='tl mono'/>")
o.append("<text x='258' y='206' class='sb'>18:1 libre</text>")
o.append("<line x1='452' y1='110' x2='588' y2='110' class='ar' marker-end='url(#lah)'/>")
o.append("<text x='520' y='98' text-anchor='middle' class='en'>2 · Aciltransferasa</text>")
o.append("<text x='520' y='130' text-anchor='middle' class='sb'>(LPCAT para la PC)</text>")
o.append("<line x1='520' y1='176' x2='520' y2='142' class='ar' marker-end='url(#lah)'/>")
o.append("<text x='520' y='196' text-anchor='middle' class='sb'>entra 20:4-CoA</text>")
o.append("<text x='520' y='213' text-anchor='middle' class='sb'>sale CoA-SH</text>")
o.append("<path d='M660,262 Q660,322 380,322 Q100,322 100,262' class='ar dsh' marker-end='url(#lah)'/>")
o.append("<text x='380' y='352' text-anchor='middle' class='sb'>se puede repetir con otra cadena: la sn-1 y la cabeza no cambian</text>")
o.append("</svg>")
SVG = "".join(o)

NEW = '''<p>El CDP cumple el mismo papel que el UDP en los azúcares: activa la pieza que se va a transferir.</p>
<h3>Ciclo de Lands: cambiar las cadenas después</h3>
<p>La síntesis «de novo» (desde el glicerol-3-fosfato) deja fosfolípidos con las cadenas que justo había disponibles como acil-CoA en ese momento. La célula no se queda con eso: los <b>retoca después</b>, sin desarmar la molécula. Eso es el ciclo de Lands, o <b>remodelado</b>. Cambia una cadena y deja igual la cabeza polar y la cadena de sn-1.</p>
<div class="fig-wide">''' + SVG + '''</div>
<ol class="flow">
  <li class="m">Fosfolípido con una cadena en sn-2 (por ejemplo PC 16:0/18:1)</li>
  <li class="e"><b>1 · Fosfolipasa A₂ (PLA₂)</b> corta el éster de <b>sn-2</b><small>Se libera ese ácido graso. Es la misma enzima que libera el araquidonato para fabricar eicosanoides.</small></li>
  <li class="m">Lisofosfolípido (una sola cola) + ácido graso libre</li>
  <li class="e"><b>2 · Aciltransferasa</b> específica de la clase: LPCAT para la PC, LPIAT para el PI…<small>Toma la cadena nueva desde un <b>acil-CoA</b>: el ácido graso ya viene activado (esa activación gastó ATP antes).</small></li>
  <li class="m">Mismo fosfolípido, con otra cadena en sn-2 (por ejemplo PC 16:0/20:4)</li>
</ol>
<div class="cards">
  <div class="cd"><h4>¿Qué cambia y qué no?</h4><p>Cambia solo la cadena de <b>sn-2</b>. La cabeza (la clase: PC, PI…) y la cadena de sn-1 quedan iguales. Cambia la <b>especie molecular</b>, no la clase.</p></div>
  <div class="cd"><h4>Las enzimas eligen</h4><p>Cada aciltransferasa prefiere ciertas cadenas (por ejemplo, un PUFA). Repitiendo el ciclo, esa clase de fosfolípido se va <b>enriqueciendo</b> en ese tipo de cadena. Por eso cada clase termina con una «firma» de cadenas propia.</p></div>
  <div class="cd"><h4>Para qué le sirve a la célula</h4><p>Ajusta la composición de sus membranas sin tener que fabricar fosfolípidos nuevos desde cero. Y guarda PUFA como el araquidonato en sn-2, listos para que la PLA₂ los libere cuando llega una señal.</p></div>
  <div class="cd"><h4>Mismo principio en la mitocondria</h4><p>La <b>tafazina</b> remodela las cadenas de la <b>cardiolipina</b>. Si falla, la mitocondria funciona mal: síndrome de Barth.</p></div>
</div>
<div class="tbl"><table>
<tr><th></th><th>Síntesis «de novo» (Kennedy / CDP-DAG)</th><th>Ciclo de Lands (remodelado)</th></tr>
<tr><td>Punto de partida</td><td>Glicerol-3-fosfato</td><td>Un fosfolípido ya armado</td></tr>
<tr><td>Qué hace</td><td>Fabrica la molécula entera: cadenas y cabeza</td><td>Cambia la cadena de sn-2</td></tr>
<tr><td>Enzimas clave</td><td>GPAT, LPAAT, enzimas que unen la cabeza con CDP</td><td>Fosfolipasa A₂ + aciltransferasa (LPCAT, LPIAT…)</td></tr>
<tr><td>Intermediario</td><td>Ácido fosfatídico, DAG o CDP-DAG</td><td>Lisofosfolípido</td></tr>
<tr><td>Las cadenas dependen de</td><td>Los acil-CoA disponibles en ese momento</td><td>La preferencia de la aciltransferasa</td></tr>
</table></div>
<details class="biblio"><summary><span class="bib">Solo bibliografía</span> Ejemplos de «firmas» de cadenas</summary><p>El PI está muy enriquecido en la combinación 18:0 en sn-1 y 20:4 (araquidonato) en sn-2, y algunas rutas de PC seleccionan especies con DHA.</p></details>
<div class="box trap"><b>Ojo</b> La fosfolipasa A₂ corta en <b>sn-2</b>, no en sn-1. Y lo que queda después del corte es un <b>lisofosfolípido</b>, no ácido fosfatídico ni DAG (esos son intermediarios de la síntesis de novo).</div>'''

t = open('t_l.html').read()
old = '''<p>El CDP cumple el mismo papel que el UDP en los azúcares: activa la pieza que se va a transferir. En el <b>ciclo de Lands</b>, la PLA₂ saca la cadena de <b>sn-2</b> (queda un lisofosfolípido) y una aciltransferasa (por ejemplo LPCAT) pone otra. Así la célula ajusta la composición sin fabricar la molécula de nuevo.</p>'''
assert t.count(old) == 1
t = t.replace(old, NEW)
open('t_l.html', 'w').write(t)
print("ok")
