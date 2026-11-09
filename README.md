# PromoQB

Repaso para el promocional de **Química Biológica**: glúcidos, lípidos y ácidos nucleicos.

**Abrilo acá:** https://clasesbysol.github.io/PromoQB/

## Qué tiene

- **Teoría** de los seis módulos del temario (Glúcidos I y II, Lípidos I y II, Ácidos nucleicos I y II), con estructuras dibujadas y esquemas de las vías.
  - Lo que aparece solo en capítulos de libros y no en los Powers está en un recuadro gris plegado («Solo bibliografía»).
  - El metabolismo que está en el temario y en parciales viejos, pero no en los Powers, está marcado «¿entra?».
- **Multiple choice** que se corrige al tocar una opción y explica por qué cada opción está bien o mal. Todas las preguntas tienen una opción «No lo sé».
- **Mi progreso**: aciertos por tema, las preguntas que más te cuestan y un botón para repasar solo las erradas.

El progreso se guarda en tu navegador, así que cada uno tiene el suyo. Si cambiás de dispositivo o de navegador, empezás de cero.

## Para quien lo mantiene

`index.html` es la página completa, un solo archivo. Se genera desde `src/`:

```
cd src
python3 mols.py      # dibuja las moléculas (necesita rdkit) → mols.js
python3 build2.py    # arma promocional-qb.html y site/index.html
cp site/index.html ../index.html
```

- `bank.js`: preguntas. Se arma concatenando `b_g1.js`, `b_g2.js`, `b_l.js` y `b_n.js`. La primera opción de cada pregunta es la correcta; la página mezcla el orden al mostrarla.
- `t_g.html`, `t_l.html`, `t_n.html`: teoría.
- `app_head.html`, `app_body.html`: estilos, estructura y lógica de la página.
