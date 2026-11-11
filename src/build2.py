head=open('app_head.html').read(); body=open('app_body.html').read()
theory=open('t_g.html').read()+open('t_l.html').read()+open('t_n.html').read()+open('t_n2s.html').read()
data=open('mols.js').read()+open('f51.js').read()+open('abbr.js').read()+open('bank.js').read()
page=(head+body).replace('/*__THEORY__*/',theory).replace('/*__DATA__*/',data)
open('promocional-qb.html','w').write(page)
# versión independiente para GitHub Pages
i=page.index('<nav class="nav">')
headpart,bodypart=page[:i],page[i:]
# los <style> del body se pueden quedar; el título y fuentes van al head
std='<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="description" content="Teoría y multiple choice para el promocional de Química Biológica: glúcidos, lípidos y ácidos nucleicos.">\n'+headpart+'\n<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>\n</head>\n<body>\n'+bodypart+'\n</body>\n</html>\n'
import os
os.makedirs('site',exist_ok=True)
open('site/index.html','w').write(std)
print(len(page))
