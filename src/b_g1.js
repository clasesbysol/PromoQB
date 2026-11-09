// Banco v4. M(tema, referencia, enunciado, opciones, origen, imagen_enunciado, solo_bibliografía)
// La PRIMERA opción es siempre la correcta; el orden se mezcla al mostrar. Cada opción: [texto, por qué, imagen?]
const Q = [];
const M = (t, r, q, o, s, img, b) => Q.push({ t, r, q, o, c: 0, s, img, b });

/* ======================= GLÚCIDOS I ======================= */
M("G1", "Glúcidos I §1", "¿Qué define que un monosacárido sea de la serie D?", [
  ["El OH del C quiral más alejado del carbonilo, a la derecha en Fischer", "Se compara con el D-gliceraldehído; en una hexosa se mira el C5."],
  ["Que desvía la luz polarizada hacia la derecha, como indica el signo (+)", "D/L no es el signo de rotación: la D-fructosa es levógira."],
  ["El OH del carbono anomérico hacia abajo en Haworth", "Eso define α en un azúcar D, no la serie."],
  ["El OH del C2 a la derecha en la proyección de Fischer", "Se mira el C quiral más alejado del carbonilo, no el C2 (salvo en el gliceraldehído)."]
]);
M("G1", "Glúcidos I §1", "D-glucosa y D-galactosa son:", [
  ["Epímeros en C4", "Difieren solo en el C4."],
  ["Epímeros en C2", "Ese es el par glucosa–manosa."],
  ["Anómeros entre sí", "Los anómeros difieren solo en el C anomérico de la forma cíclica."],
  ["Enantiómeros entre sí", "El enantiómero de la D-glucosa es la L-glucosa."]
]);
M("G1", "Glúcidos I §1", "Una aldohexosa abierta tiene 4 carbonos quirales. ¿Cuántos estereoisómeros puede tener como máximo?", [
  ["16", "2⁴ = 16: 8 de la serie D y 8 de la L."],
  ["8", "2³: corresponde a 3 centros quirales (aldopentosa)."],
  ["4", "Es el número de centros, no de isómeros."],
  ["32", "Sería 2⁵."]
]);
M("G1", "Glúcidos I §2", "En la proyección de Haworth de una D-hexosa, el anómero α tiene:", [
  ["El OH anomérico en el lado opuesto al CH₂OH", "α = trans al CH₂OH de referencia (abajo)."],
  ["El OH anomérico del mismo lado que el CH₂OH", "Eso es β."],
  ["El OH del C4 orientado hacia arriba", "El C4 no define α/β; arriba en C4 sería galactosa."],
  ["Un anillo de cinco átomos (furanosa)", "El tamaño del anillo no define α/β."]
]);
M("G1", "Glúcidos I §2", "Al pasar de Fischer a Haworth (D-hexosa), los grupos que estaban a la derecha quedan:", [
  ["Hacia abajo del anillo", "Derecha → abajo; izquierda → arriba."],
  ["Hacia arriba del anillo", "Es al revés."],
  ["Siempre en posición axial", "Axial/ecuatorial es de la silla, no de esta regla."],
  ["Arriba o abajo según sea α o β", "α/β solo afecta al OH anomérico."]
]);
M("G1", "Glúcidos I §2", "Sobre la mutarrotación de la D-glucosa, ¿qué es correcto?", [
  ["Pasa α ⇄ β a través de la forma abierta", "Requiere un hemiacetal libre; en el equilibrio predomina β (≈ 64 %)."],
  ["En el equilibrio predomina el anómero α", "Predomina β (≈ 63,6 %)."],
  ["También ocurre en la sacarosa disuelta", "La sacarosa tiene los dos C anoméricos en el enlace: no puede abrirse."],
  ["Ocurre porque α y β son enantiómeros", "Son anómeros, no enantiómeros."]
]);
M("G1", "Glúcidos I §2", "¿Qué grupos reaccionan para formar el anillo de la glucopiranosa?", [
  ["Aldehído del C1 con el OH del C5", "Se forma un hemiacetal y un anillo de 6 (5 C + O)."],
  ["Aldehído del C1 con el OH del C4", "Daría un anillo de 5 (furanosa)."],
  ["Cetona del C2 con el OH del C5", "Eso es la fructosa (hemicetal, furanosa)."],
  ["OH del C6 con el OH del C1", "No: reacciona el carbonilo con un OH."]
]);
M("G1", "Glúcidos I §2", "¿Por qué la β-D-glucopiranosa es tan estable y abundante?", [
  ["En su silla todos los grupos voluminosos son ecuatoriales", "Evita las interacciones 1,3-diaxiales."],
  ["Su anillo es plano, como se dibuja en la proyección de Haworth", "Haworth es una representación; el anillo real es una silla."],
  ["Porque su anillo es una furanosa", "Es una piranosa (6)."],
  ["Porque no tiene carbono anomérico libre", "Lo tiene (C1)."]
]);
M("G1", "Glúcidos I §2", "¿Por qué la β-D-manopiranosa es menos estable que la β-D-glucopiranosa?", [
  ["Su OH del C2 queda axial en la silla", "En la β-glucosa todos son ecuatoriales."],
  ["Porque es un azúcar de la serie L", "Es D-manosa."],
  ["Porque su anillo es de cinco átomos", "Ambas son piranosas."],
  ["Porque su C anomérico es un acetal", "Libre es un hemiacetal, igual que en la glucosa."]
]);
M("G1", "Glúcidos I §4", "¿En qué par los dos azúcares son NO reductores?", [
  ["Sacarosa y trehalosa", "Ambas unen anomérico con anomérico."],
  ["Maltosa y lactosa", "Las dos tienen un C anomérico libre."],
  ["Lactosa y sacarosa", "La lactosa es reductora."],
  ["Maltosa y trehalosa", "La maltosa es reductora."]
]);
M("G1", "Glúcidos I §4", "La lactosa es:", [
  ["Galβ(1→4)Glc, reductora", "El C1 de la glucosa queda libre."],
  ["Galβ(1→4)Glc, no reductora", "La estructura es correcta pero sí es reductora."],
  ["Glcα(1→4)Glc, reductora", "Eso es la maltosa."],
  ["Glcα(1↔2)βFru, no reductora", "Eso es la sacarosa."]
]);
M("G1", "Glúcidos I §4", "En la sacarosa, la fructosa está como:", [
  ["β-D-fructofuranosa unida por su C2", "Glcα(1↔2)βFru: los dos anoméricos están en el enlace."],
  ["α-D-fructopiranosa unida por su C1", "Es furanosa y se une por el C2."],
  ["β-D-fructofuranosa unida por su C6", "El enlace compromete el C2 anomérico."],
  ["Fructosa en forma abierta", "Abierta tendría carbonilo libre: sería reductora."]
]);
M("G1", "Glúcidos I §4", "¿Por qué la intolerancia a la lactosa produce diarrea y gases?", [
  ["La lactosa no se absorbe y llega al colon", "Sin lactasa no se hidroliza: retiene agua por ósmosis y las bacterias la fermentan."],
  ["La lactosa es tóxica para el epitelio", "No es tóxica."],
  ["Falta la enzima sacarasa intestinal", "La que falta es la lactasa."],
  ["La lactosa se absorbe entera y altera el epitelio intestinal", "Justamente no puede absorberse entera."]
]);
M("G1", "Glúcidos I §3", "Si se oxida solamente el C6 de la D-glucosa se obtiene:", [
  ["Ácido glucurónico (urónico)", "Urónico = C6 oxidado; está en los GAG."],
  ["Ácido glucónico (aldónico)", "Se obtiene oxidando el C1."],
  ["Ácido glucárico (aldárico)", "Requiere oxidar C1 y C6."],
  ["Glucitol (un alditol)", "Se obtiene reduciendo el carbonilo."]
], "Estilo Maugeri 2023");
M("G1", "Glúcidos I §3", "Sobre el glucitol (sorbitol), ¿qué es correcto?", [
  ["No cicla, no mutarrota y no es reductor", "Es un alditol: no tiene carbonilo."],
  ["Forma anómeros α y β cuando se disuelve en agua", "Sin carbonilo no forma hemiacetal."],
  ["Sigue siendo un azúcar reductor", "No tiene carbonilo que oxidar."],
  ["Es el enantiómero de la D-glucosa", "El enantiómero es la L-glucosa."]
], "Estilo Maugeri 2023");
M("G1", "Glúcidos I §3", "¿Qué es el ribitol?", [
  ["Un alditol que forma parte de FMN y FAD", "Es ribosa reducida unida a la flavina."],
  ["Un ácido urónico que forma parte de los GAG", "No está oxidado."],
  ["El desoxiazúcar del ADN", "Ese es la 2-desoxirribosa."],
  ["Un aminoazúcar de la quitina", "Ese es la GlcNAc."]
]);
M("G1", "Glúcidos I §3", "El ácido siálico (Neu5Ac):", [
  ["Tiene 9 C y carga negativa", "Suele ocupar la punta de los glicanos; se dona como CMP-siálico."],
  ["Es una hexosa neutra", "Tiene 9 C y un carboxilo."],
  ["Es el monómero de la celulosa", "Es la glucosa."],
  ["Solo existe en paredes vegetales", "Es típico de glicoconjugados animales."]
]);
M("G1", "Glúcidos I §3", "¿Para qué sirven los azúcares nucleotídicos como la UDP-glucosa?", [
  ["Son la forma activada que usan las glicosiltransferasas", "El nucleótido es buen grupo saliente: aporta energía al enlace."],
  ["Son la forma en que la célula guarda la glucosa de reserva", "La reserva es el glucógeno."],
  ["Transportan glucosa en el plasma", "No."],
  ["Son productos de la reacción de Maillard", "No."]
]);
M("G1", "Glúcidos I §3", "La HbA1c es un ejemplo de:", [
  ["Glicación no enzimática", "Un azúcar reductor reacciona con grupos amino; refleja la glucemia promedio."],
  ["Glicosilación enzimática en el Golgi", "La glicosilación es enzimática y programada."],
  ["Unión O-glicosídica a serina", "No es una O-glicosilación."],
  ["Reacción de Fehling positiva", "Fehling es un ensayo con cobre."]
]);
M("G1", "Glúcidos I §3", "Reacción de Maillard y glicación de la HbA1c:", [
  ["Son la misma química no enzimática", "Azúcar reductor + grupo amino → base de Schiff → AGE. Una en alimentos, otra en el cuerpo."],
  ["Maillard es enzimática y la glicación no", "Ninguna es enzimática."],
  ["La glicación necesita sacarosa", "La sacarosa no es reductora."],
  ["Maillard es la glicosilación del Golgi", "La glicosilación es enzimática."]
]);
M("G1", "Glúcidos I §5", "Amilopectina y glucógeno se diferencian en:", [
  ["La frecuencia de las ramas α(1→6)", "Glucógeno cada 8–12; amilopectina cada 24–30."],
  ["El tipo de enlace de la cadena principal", "Ambos tienen α(1→4)."],
  ["El monómero que los forma", "Ambos son de glucosa."],
  ["Que la amilopectina no tiene ramas", "Sí tiene; la lineal es la amilosa."]
]);
M("G1", "Glúcidos I §5", "Celulosa (insoluble, fibrosa) y glucógeno (soluble) son polímeros de glucosa. La diferencia física se debe a:", [
  ["El tipo de enlace: β(1→4) vs α(1→4)", "β estira las cadenas (fibras con puentes de H); α las curva en hélices ramificadas e hidratadas."],
  ["Que la celulosa tiene ramas cada 8 residuos", "La celulosa es lineal."],
  ["Que la celulosa tiene N-acetilglucosamina", "Eso es la quitina."],
  ["Que el glucógeno no tiene extremo reductor", "Tiene uno solo."]
], "Final 2008 / 2018 (Maugeri)");
M("G1", "Glúcidos I §5", "Elegí los atributos del SULFATO DE CONDROITINA:", [
  ["Cargado negativamente · extracelular · disacárido repetitivo", "GAG: GlcA + GalNAc sulfatada."],
  ["Neutro · polisacárido intracelular · muy ramificado", "Eso es glucógeno o amilopectina."],
  ["Insoluble en agua · uniones β(1→4) · puentes de H intercatenarios", "Eso es la celulosa."],
  ["Dulce · disacárido · sin extremo reductor", "Eso es la sacarosa."]
], "Parcial 2023 (Maugeri)");
M("G1", "Glúcidos I §5", "Elegí los atributos de la AMILOPECTINA:", [
  ["Ramificado · intracelular · cadenas helicoidales", "Reserva vegetal con ramas α(1→6)."],
  ["Cargado negativamente · extracelular · repetitivo", "Eso es un GAG."],
  ["Insoluble · β(1→4) · forma fibras", "Eso es la celulosa."],
  ["Disacárido · dulce · sin extremo reductor", "Eso es la sacarosa."]
], "Parcial 2023 (Maugeri)");
M("G1", "Glúcidos I §5", "¿Cuál de estas afirmaciones sobre los GAG es correcta?", [
  ["El queratán sulfato no tiene ácido urónico", "Lleva galactosa en su lugar."],
  ["El hialuronano es el GAG más sulfatado de todos", "No está sulfatado; el más sulfatado es la heparina."],
  ["La heparina es neutra a pH fisiológico", "Es muy negativa."],
  ["Los GAG suelen ser muy ramificados", "Son lineales."]
]);
M("G1", "Glúcidos I §5", "¿Por qué los GAG forman geles que resisten la compresión?", [
  ["Sus cargas negativas atraen cationes y agua", "Además se repelen entre sí y mantienen las cadenas extendidas."],
  ["Son muy hidrofóbicos y excluyen el agua de la matriz", "Son muy hidrofílicos."],
  ["Forman puentes disulfuro entre cadenas", "No tienen tioles."],
  ["Son polímeros muy ramificados", "Son lineales."]
]);
M("G1", "Glúcidos I §5", "¿Por qué la célula guarda glucosa como polímero y no libre?", [
  ["Para bajar la cantidad de partículas osmóticas", "Miles de glucosas libres subirían la osmolaridad."],
  ["Porque el polímero rinde más energía por residuo", "La energía por residuo es similar."],
  ["Porque la glucosa libre no se fosforila", "Sí se fosforila."],
  ["Porque el polímero es más dulce", "No tiene relación."]
]);
M("G1", "Glúcidos I §5", "Una molécula de glucógeno con 2000 extremos no reductores tiene:", [
  ["Un solo extremo reductor", "Toda molécula de polisacárido tiene uno."],
  ["2000 extremos reductores", "Esos son los no reductores."],
  ["1999 extremos reductores", "1999 son los puntos de ramificación."],
  ["Ningún extremo reductor", "Tiene uno."]
]);
M("G1", "Glúcidos I §5", "Sobre quitina y peptidoglicano, ¿qué es correcto?", [
  ["La quitina es GlcNAc β(1→4)", "Es como la celulosa con NHAc en C2."],
  ["La lisozima rompe los puentes peptídicos", "Corta el enlace glicosídico GlcNAc–MurNAc."],
  ["El peptidoglicano es un homopolisacárido", "Alterna GlcNAc y MurNAc."],
  ["La quitina es glucosa unida α(1→4)", "Eso es la amilosa."]
]);
M("G1", "Glúcidos I §5", "¿Qué se obtiene al desacetilar la quitina?", [
  ["Quitosano", "Queda con aminos libres que pueden cargarse positivamente."],
  ["Celulosa", "Habría que cambiar el NH₂ por OH."],
  ["Peptidoglicano", "Lleva MurNAc y péptidos."],
  ["Ácido hialurónico", "Es un GAG con GlcA."]
]);
M("G1", "Glúcidos II §1", "La unión N-glicosídica de una glicoproteína se forma con:", [
  ["El N de la amida de asparagina", "En la secuencia Asn–X–Ser/Thr (X ≠ Pro)."],
  ["El OH de serina o treonina", "Esa es la O-glicosídica."],
  ["El N de la lisina", "La lisina participa en la glicación."],
  ["El amino terminal de la proteína", "No."]
]);
M("G1", "Glúcidos II §1", "¿Qué señal dirige enzimas recién sintetizadas al lisosoma?", [
  ["Manosa-6-fosfato", "La reconoce su receptor y desvía la proteína."],
  ["Ácido siálico terminal", "Lo reconoce la hemaglutinina de influenza."],
  ["Sialyl-Lewis X", "Lo reconocen las selectinas."],
  ["Gangliósido GM1", "Es el receptor de la toxina del cólera."]
]);
M("G1", "Glúcidos II §1", "En un proteoglicano como el agrecano del cartílago:", [
  ["Cadenas de GAG se unen a una proteína central", "Muchos se organizan sobre un hialuronano y retienen agua."],
  ["Tiene pocos azúcares, cortos y ramificados, como una glicoproteína", "Eso describe una glicoproteína."],
  ["Los GAG se unen a la proteína por Asn", "Se unen a Ser."],
  ["La estructura es neutra y compacta", "Es muy negativa y extendida."]
]);
M("G1", "Glúcidos II §1", "¿Qué determina el grupo sanguíneo ABO?", [
  ["El azúcar terminal de ciertos glicanos", "GalNAc en A, Gal en B, ninguno extra en O."],
  ["Una proteína distinta en el eritrocito", "Lo que cambia es el glicano."],
  ["La cantidad de ácido siálico", "No."],
  ["El tipo de hemoglobina", "No."]
]);

/* ---- con imágenes (el nombre aparece recién al responder) ---- */
M("G1", "Glúcidos I §2", "¿Cuál es la α-D-glucopiranosa?", [
  ["α-D-glucopiranosa", "C1 con OH abajo (opuesto al CH₂OH); C2 y C4 abajo, C3 arriba.", "h_aglc"],
  ["β-D-glucopiranosa", "OH del C1 arriba: β.", "h_bglc"],
  ["β-D-galactopiranosa", "OH del C4 arriba: galactosa.", "h_bgal"],
  ["β-D-manopiranosa", "OH del C2 arriba: manosa.", "h_bman"]
]);
M("G1", "Glúcidos I §2", "¿Cuál es la β-D-galactopiranosa?", [
  ["β-D-galactopiranosa", "C4 con OH arriba y C1 con OH arriba.", "h_bgal"],
  ["α-D-galactopiranosa", "Es galactosa, pero α (C1 abajo).", "h_agal"],
  ["β-D-glucopiranosa", "C4 con OH abajo: glucosa.", "h_bglc"],
  ["β-D-manopiranosa", "Cambia el C2, no el C4.", "h_bman"]
]);
M("G1", "Glúcidos I §1", "¿Cuál es el epímero en C2 de la D-glucosa?", [
  ["D-manosa", "Solo cambia el C2.", "f_dmanosa"],
  ["D-galactosa", "Cambia el C4.", "f_dgalactosa"],
  ["L-glucosa", "Cambian todos: enantiómero.", "f_lglucosa"],
  ["D-fructosa", "Es una cetosa.", "f_dfructosa"]
]);
M("G1", "Glúcidos I §1", "¿Cuál pertenece a la serie L?", [
  ["L-glucosa", "C5 con OH a la izquierda.", "f_lglucosa"],
  ["D-glucosa", "C5 a la derecha.", "f_dglucosa"],
  ["D-galactosa", "C5 a la derecha (el C4 no decide).", "f_dgalactosa"],
  ["D-manosa", "C5 a la derecha.", "f_dmanosa"]
]);
M("G1", "Glúcidos I §1", "¿Cuál NO tiene carbono quiral?", [
  ["Dihidroxiacetona", "Su C central es C=O con dos CH₂OH iguales.", "f_dihidroxiacetona"],
  ["D-gliceraldehído", "Su C2 es quiral.", "f_dgliceraldehido"],
  ["L-gliceraldehído", "Su C2 es quiral.", "f_lgliceraldehido"],
  ["D-ribosa", "Tiene 3 centros quirales.", "f_dribosa"]
]);
M("G1", "Glúcidos I §3", "¿Cuál es un ácido urónico?", [
  ["Ácido glucurónico", "C1 aldehído y C6 como COOH.", "f_glucuronico"],
  ["Ácido glucónico", "C1 oxidado: aldónico.", "f_gluconico"],
  ["Ácido glucárico", "C1 y C6 oxidados: aldárico.", "f_glucarico"],
  ["Glucitol", "Carbonilo reducido: alditol.", "f_glucitol"]
], "Estilo Maugeri 2023");
M("G1", "Glúcidos I §3", "¿Cuál NO puede ciclar ni mutarrotar?", [
  ["D-glucitol", "No tiene carbonilo.", "f_glucitol"],
  ["D-glucosa", "Forma hemiacetal.", "f_dglucosa"],
  ["D-fructosa", "Forma hemicetal.", "f_dfructosa"],
  ["Ácido D-glucurónico", "Conserva el aldehído.", "f_glucuronico"]
]);
M("G1", "Glúcidos I §4", "¿Qué disacárido es este?", [
  ["Lactosa", "Gal (C4 OH arriba) β(1→4) Glc: reductora.", null],
  ["Maltosa", "Dos glucosas, enlace α.", null],
  ["Celobiosa", "Dos glucosas: el primer C4 tendría el OH abajo.", null],
  ["Sacarosa", "Tiene una fructofuranosa.", null]
], null, "d_lactosa");
M("G1", "Glúcidos I §4", "¿Qué disacárido es este?", [
  ["Maltosa", "Dos glucosas con el enlace saliendo hacia abajo del C1: α(1→4).", null],
  ["Celobiosa", "Sería β: el enlace saldría hacia arriba del C1.", null],
  ["Lactosa", "El primer residuo sería galactosa (C4 arriba).", null],
  ["Trehalosa", "Uniría C1 con C1.", null]
], null, "d_maltosa");
M("G1", "Glúcidos I §4", "¿Cuál tiene un enlace β(1→4) entre dos glucosas?", [
  ["Celobiosa", "Glcβ(1→4)Glc: la unidad de la celulosa.", "d_celobiosa"],
  ["Maltosa", "Glcα(1→4)Glc.", "d_maltosa"],
  ["Lactosa", "β(1→4), pero el primero es Gal.", "d_lactosa"]
], null, null, 1);
M("G1", "Glúcidos I §3", "¿Cuál es la N-acetilglucosamina (GlcNAc)?", [
  ["GlcNAc", "NHAc en el C2.", "h_bglcnac"],
  ["β-D-glucuronato", "COO⁻ en C5.", "h_bglca"],
  ["Glucosa-6-fosfato", "Fosfato en C6.", "h_g6p"],
  ["β-D-galactopiranosa", "Sin amino.", "h_bgal"]
]);
M("G1", "Glúcidos I §5", "¿Cuál de estas cadenas corresponde al glucógeno?", [
  ["Glucógeno", "Ramas α(1→6) muy frecuentes (cada 8–12).", "s_glucogeno"],
  ["Amilopectina", "Ramas mucho más espaciadas (24–30).", "s_amilopectina"],
  ["Amilosa", "Lineal, en hélice.", "s_amilosa"],
  ["Celulosa", "Cadenas rectas paralelas con puentes de H.", "s_celulosa"]
]);
M("G1", "Glúcidos I §5", "¿Cuál es la unidad repetitiva de la celulosa?", [
  ["Celulosa", "Glc β(1→4) Glc: el enlace sale hacia arriba del C1.", "p_celulosa"],
  ["Amilosa", "Glc α(1→4) Glc: el enlace sale hacia abajo.", "p_amilosa"],
  ["Quitina", "Tiene NHAc en C2.", "p_quitina"],
  ["Peptidoglicano", "Tiene MurNAc con lactilo.", "p_peptidoglicano"]
]);
M("G1", "Glúcidos I §5", "¿Cuál es la unidad de la quitina?", [
  ["Quitina", "GlcNAc β(1→4) GlcNAc.", "p_quitina"],
  ["Celulosa", "Glucosas sin NHAc.", "p_celulosa"],
  ["Peptidoglicano", "El segundo residuo lleva el lactilo (MurNAc).", "p_peptidoglicano"],
  ["Amilosa", "Enlace α y glucosas.", "p_amilosa"]
]);
M("G1", "Glúcidos I §5", "¿Cuál es el ácido L-idurónico (IdoA)?", [
  ["IdoA", "Como el GlcA pero con el COO⁻ hacia abajo (epímero en C5).", "m_idoa"],
  ["GlcA", "COO⁻ hacia arriba.", "m_glca"],
  ["GlcNAc", "No es un urónico: tiene CH₂OH y NHAc.", "m_glcnac"],
  ["GlcNS6S", "Glucosamina sulfatada de la heparina.", "m_glcns6s"]
]);
M("G1", "Glúcidos I §5", "¿Qué GAG tiene esta unidad repetitiva?", [
  ["Hialuronano", "GlcA β1→3 GlcNAc β1→4, sin sulfatos.", null],
  ["Condroitín sulfato", "Tendría GalNAc (cuadrado amarillo) sulfatada.", null],
  ["Queratán sulfato", "Tendría Gal en lugar de urónico.", null],
  ["Heparina", "Tendría IdoA y muchos sulfatos.", null]
], null, "c_hialuronano");
M("G1", "Glúcidos I §5", "¿Qué GAG tiene esta unidad repetitiva?", [
  ["Queratán sulfato", "Gal + GlcNAc-6S: sin ácido urónico.", null],
  ["Condroitín sulfato", "GlcA + GalNAc.", null],
  ["Dermatán sulfato", "IdoA + GalNAc.", null],
  ["Hialuronano", "GlcA + GlcNAc sin sulfato.", null]
], null, "c_queratan");
M("G1", "Glúcidos I §5", "¿Qué GAG tiene esta unidad repetitiva?", [
  ["Dermatán sulfato", "IdoA α1→3 GalNAc-4S.", null],
  ["Condroitín sulfato", "Tendría GlcA (rombo azul).", null],
  ["Heparina", "Tendría glucosamina N-sulfatada y enlaces α1→4.", null],
  ["Queratán sulfato", "Tendría Gal.", null]
], null, "c_dermatan");
