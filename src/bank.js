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
/* ======================= GLÚCIDOS II · ANÁLISIS ======================= */
M("G2", "Glúcidos II §2", "Partís de un extracto vegetal con proteínas, polisacáridos y sales. ¿Qué secuencia aísla los polisacáridos?", [
  ["TCA → etanol 80 % → diálisis", "TCA saca proteínas, el etanol precipita los polisacáridos y la diálisis saca sales."],
  ["Diálisis → TCA → etanol 80 %", "Al final quedarían sales del TCA y del medio."],
  ["Etanol 80 % → hidrólisis ácida → diálisis", "La hidrólisis rompería el polisacárido."],
  ["Cloroformo:metanol → diálisis", "La partición con solventes es para lípidos."]
], "Parcial 2023 (Maugeri)");
M("G2", "Glúcidos II §2", "Una columna de intercambio aniónico se eluye con 0; 0,3 y 0,6 M de NaCl. El polisacárido del pico de 0,6 M:", [
  ["Tiene la mayor densidad de carga negativa", "Elución escalonada: más carga, más sal para despegarlo."],
  ["Es el de mayor tamaño molecular", "El intercambio iónico separa por carga."],
  ["Es neutro y no interactúa con la resina", "Los neutros salen con 0 M."],
  ["Tiene la mayor carga positiva", "La resina positiva no retiene cationes."]
], "Parcial 2023 (Maugeri)");
M("G2", "Glúcidos II §2", "Un intercambiador aniónico es:", [
  ["Una resina positiva que retiene aniones", "El nombre dice qué ion retiene."],
  ["Una resina negativa que retiene aniones", "Una resina negativa retiene cationes."],
  ["Una resina positiva que retiene cationes", "Cargas iguales se repelen."],
  ["Una matriz porosa que separa por tamaño", "Eso es exclusión molecular."]
]);
M("G2", "Glúcidos II §2", "El primer pico tiene 5 polisacáridos distintos y el tercero, uno puro. En FACE se espera:", [
  ["5 bandas en el primero y 1 en el tercero", "Cada especie da su banda."],
  ["Una sola banda en cada pico", "Una banda indicaría una especie."],
  ["1 banda en el primero y 5 en el tercero", "Al revés."],
  ["Ninguna banda en ningún pico", "El ANTS les da fluorescencia y carga."]
], "Parcial 2023 (Maugeri)");
M("G2", "Glúcidos II §2", "En FACE, ¿para qué se une el ANTS al extremo reductor?", [
  ["Para darle fluorescencia y carga negativa", "Así migra al ánodo y se ve; los chicos migran más."],
  ["Para hidrolizar el glicano en monosacáridos", "No rompe enlaces."],
  ["Para metilar los OH libres del glicano", "Eso lo hace el CH₃I."],
  ["Para que el glicano se una a la sílica", "En FACE se usa un gel de electroforesis."]
]);
M("G2", "Glúcidos II §2", "En una exclusión molecular (SEC / Biogel P-4):", [
  ["Las moléculas grandes salen primero", "No entran a los poros: salen cerca de V₀."],
  ["Las moléculas chicas salen primero", "Entran a los poros y tardan más."],
  ["Se separa según la carga", "Eso es intercambio iónico."],
  ["Se obtiene la masa absoluta", "Da una masa aparente (depende de la forma)."]
]);
M("G2", "Glúcidos II §2", "En una TLC en sílica de una serie de oligosacáridos, ¿cuál tiene el mayor Rf?", [
  ["El disacárido", "Menos OH, menos retención en la sílica polar."],
  ["El tetrasacárido", "Migra menos que el disacárido."],
  ["El hexasacárido", "Es el más retenido."],
  ["Todos tienen el mismo Rf", "El Rf baja al crecer la cadena."]
]);
M("G2", "Glúcidos II §2", "En HPAEC-PAD, un azúcar neutro se retiene en la columna aniónica porque:", [
  ["A pH 12–13 sus OH se ionizan en parte", "Los OH tienen pKa 12–14: el azúcar queda como anión."],
  ["Se marca antes con ANTS", "HPAEC no necesita derivatizar."],
  ["Se reduce a alditol antes de inyectarlo", "Los alditoles casi no se retienen."],
  ["Forma puentes de H con la resina", "La retención es por intercambio iónico."]
]);
M("G2", "Glúcidos II §2", "Sobre HPAEC-PAD, ¿cuál es correcta?", [
  ["Da la composición, no los enlaces ni α/β", "Se usa después de la hidrólisis ácida."],
  ["Todos los azúcares se cuantifican con la curva de glucosa", "Cada uno se calibra por separado."],
  ["El detector PAD mide absorbancia UV", "Es amperométrico, con electrodo de oro."],
  ["Los azúcares ácidos se eluyen solo con NaOH", "Hace falta acetato de sodio."]
]);
M("G2", "Glúcidos II §2", "En HPAEC-PAD se agrega acetato de sodio al eluyente para:", [
  ["Competir y eluir los azúcares más retenidos", "Ácidos y oligosacáridos largos no saldrían solo con NaOH."],
  ["Derivatizar los azúcares antes de detectarlos", "No hay derivatización."],
  ["Bajar el pH a la neutralidad", "El pH tiene que quedar alto."],
  ["Limpiar el electrodo de oro", "Eso lo hacen los pulsos del detector."]
]);
M("G2", "Glúcidos II §2", "Tras metilación aparece 1,4,5-tri-O-acetil-2,3,6-tri-O-metilglucitol. Esa glucosa estaba:", [
  ["Unida en C4", "Los acetilos 1 y 5 vienen de la preparación; el 4 marca el enlace."],
  ["Unida en C5", "El 5 era el O del anillo."],
  ["Como terminal no reductora", "Sería 2,3,4,6-tetra-O-metil."],
  ["Como punto de ramificación", "Tendría dos posiciones de enlace."]
]);
M("G2", "Glúcidos II §2", "El derivado 2,3-di-O-metilglucosa indica una glucosa:", [
  ["Sustituida en C4 y C6 (ramificación)", "En el glucógeno es cada punto α(1→6)."],
  ["Terminal no reductora", "Sería 2,3,4,6-tetra-O-metil."],
  ["Unida solo en C6, como en una cadena lineal", "Sería 2,3,4-tri-O-metil."],
  ["Unida solo en C4", "Sería 2,3,6-tri-O-metil."]
]);
M("G2", "Glúcidos II §2", "Aparece 2,3,5,6-tetra-O-metil-galactitol. ¿Qué indica?", [
  ["Galactofuranosa terminal", "En la furanosa el O del anillo está en C4."],
  ["Galactopiranosa terminal", "Sería 2,3,4,6-tetra-O-metil."],
  ["Galactosa unida en C5", "El C5 está metilado: estaba libre."],
  ["Galactosa ramificada", "Solo los acetilos de la preparación."]
]);
M("G2", "Glúcidos II §2", "¿Para qué se reduce con NaBD₄ (y no NaBH₄) al preparar los PMAA?", [
  ["Para marcar el C1 y distinguir los extremos", "Algunos alditoles son simétricos."],
  ["Para terminar de metilar los OH que quedaron libres", "La reducción no metila."],
  ["Para que el derivado sea más polar", "Se buscan derivados volátiles."],
  ["Para romper los enlaces glicosídicos", "Eso lo hace la hidrólisis."]
]);
M("G2", "Glúcidos II §2", "Los PMAA de Glc, Man y Gal con iguales sustituyentes dan el mismo espectro de masas. Se distinguen por:", [
  ["El tiempo de retención en el GC", "Comparando con estándares."],
  ["El ion molecular del espectro", "Son estereoisómeros: misma masa."],
  ["Un análisis por HPAEC-PAD", "Los PMAA se analizan por GC-MS."],
  ["No pueden distinguirse", "Sí, por GC."]
]);
M("G2", "Glúcidos II §2", "Un glicano en 10,5 GU: con β-galactosidasa sigue igual y con α-galactosidasa pasa a 8,4 GU. Tiene:", [
  ["Galactosa terminal unida en α", "Cada exoglicosidasa es específica de azúcar y de α/β."],
  ["Galactosa terminal unida en β", "La β-galactosidasa no hizo nada."],
  ["Galactosa en el extremo reductor", "Las exoglicosidasas cortan desde las puntas."],
  ["Ninguna galactosa", "La α-galactosidasa lo achicó."]
]);
M("G2", "Glúcidos II §2", "¿Qué técnica informa si los enlaces son α o β?", [
  ["Exoglicosidasas secuenciales + SEC", "Además da el orden desde la punta."],
  ["Hidrólisis ácida + HPAEC-PAD", "Da composición."],
  ["Metilación exhaustiva + PMAA + GC-MS", "Da posiciones de enlace."],
  ["TLC con p-anisaldehído", "Evalúa pureza."]
]);
M("G2", "Glúcidos II §2", "Oligosacárido A: aparece 2,4-di-O-metil-manosa. Esa manosa:", [
  ["Está sustituida en C3 y C6", "Es el punto de ramificación."],
  ["Es una manosa terminal no reductora", "Sería 2,3,4,6-tetra-O-metil."],
  ["Está unida solo en C2", "Sería 3,4,6-tri-O-metil."],
  ["Está unida solo en C6", "Sería 2,3,4-tri-O-metil."]
], "Parcial 2023 (Maugeri)");
M("G2", "Glúcidos II §2", "En el oligosacárido A, una β-glucosidasa saca 2 residuos y hay dos 2,3,4,6-Me₄-Glc. Se deduce que:", [
  ["Las 2 Glc son terminales unidas en β", "Coinciden metilación y digestión."],
  ["Las 2 Glc están en el extremo reductor", "Las exoglicosidasas no cortan ahí."],
  ["Las 2 Glc están unidas en α", "La enzima es específica de β."],
  ["El oligosacárido es lineal", "Hay una manosa ramificada."]
], "Parcial 2023 (Maugeri)");
M("G2", "Glúcidos II §2", "¿Por qué secuenciar glicanos es más difícil que secuenciar proteínas?", [
  ["Se ramifican y no se copian de un molde", "Pueden unirse por distintos C, en α o β, y hay muchas variantes."],
  ["Porque no tienen ningún extremo", "Tienen un reductor y varios no reductores."],
  ["Porque son siempre muy pequeños para analizarlos", "Pueden ser enormes."],
  ["Porque son insolubles en agua", "La mayoría son solubles."]
]);
M("G2", "Glúcidos II §1", "¿Qué tienen de distinto N-glicanos y O-glicanos (tipo mucina)?", [
  ["Los N van a Asn; los O, a Ser o Thr", "N: GlcNAc–Asn; O: GalNAc–Ser/Thr."],
  ["Los N van a Ser; los O, a Asn", "Es al revés."],
  ["Los dos empiezan con GalNAc", "Los N empiezan con GlcNAc."],
  ["Los O se liberan con PNGasa F", "La PNGasa F libera N-glicanos."]
]);
M("G2", "Glúcidos II §1", "El precursor de los N-glicanos se arma en el RE sobre:", [
  ["Dolicol-fosfato", "Glc₃Man₉GlcNAc₂ se transfiere en bloque a la Asn."],
  ["Una serina de la proteína", "Ahí empiezan los O-glicanos."],
  ["UDP-glucosa libre", "Dona una sola glucosa."],
  ["La glucogenina", "Es del glucógeno."]
]);
M("G2", "Glúcidos II §1", "Querés liberar enteros N-glicanos complejos. ¿Qué herramienta usás?", [
  ["PNGasa F, que corta GlcNAc–Asn en todos", "La Asn queda como Asp."],
  ["Endo H, que corta entre las dos GlcNAc", "No actúa sobre los complejos."],
  ["Hidracinólisis a 60 °C", "A 60 °C salen los O-glicanos."],
  ["β-galactosidasa, que corta la Gal terminal", "Saca un azúcar de la punta."]
]);
M("G2", "Glúcidos II §1", "Después de la PNGasa F, en el sitio de N-glicosilación queda:", [
  ["Ácido aspártico", "Asn → Asp (+1 de masa): marca del sitio."],
  ["Asparagina con una GlcNAc", "Eso deja la Endo H."],
  ["Serina", "El sitio N está en Asn."],
  ["Glutamina", "No."]
]);
M("G2", "Glúcidos II §1", "La hidracinólisis a 60 °C libera O-glicanos pero no N-glicanos porque:", [
  ["El enlace a Ser/Thr es más lábil", "Los N necesitan ~95 °C."],
  ["La hidracina solo ataca serinas", "Rompe ambos según la temperatura."],
  ["Los N-glicanos no tienen GlcNAc", "Empiezan con GlcNAc–Asn."],
  ["A 60 °C la hidracina se inactiva", "No."]
]);
M("G2", "Glúcidos II §2", "Querés separar glicanos con fucosa en el núcleo. ¿Qué columna de lectina usás?", [
  ["LCA (lenteja), que reconoce fucosa del núcleo", "Se eluye con α-metilmanósido."],
  ["SNA, que reconoce ácido siálico unido α2-6", "Separa según el siálico."],
  ["RCA-I, que reconoce galactosa β1-4 terminal", "Separa según la galactosa."],
  ["Con A, que reconoce alta manosa", "No distingue la fucosa."]
]);
M("G2", "Glúcidos II §2", "Una glicoproteína retenida en una columna de Con A se eluye con:", [
  ["α-metilmanósido 100 mM", "Un azúcar parecido compite por la lectina."],
  ["NaCl 1 M en el buffer de elución", "La unión no es iónica."],
  ["PNGasa F", "Cortaría el glicano."],
  ["Ácido siálico libre", "Con A reconoce manosa/glucosa."]
]);
M("G2", "Glúcidos II §2", "Sobre las lectinas, ¿qué es correcto?", [
  ["Se unen de forma reversible, sin catalizar", "Por eso un azúcar libre las desplaza."],
  ["Cortan el glicano que reconocen, como una glicosidasa", "No son glicosidasas."],
  ["Separan glicanos según su tamaño", "Separan por reconocimiento."],
  ["Se unen de forma covalente", "La unión es reversible."]
]);
M("G2", "Glúcidos II §2", "En el cartucho de carbono grafitizado (PGC), ¿qué sale con el lavado de agua?", [
  ["Sales y monosacáridos", "Es el paso de desalado."],
  ["Oligosacáridos neutros", "Salen con acetonitrilo 25 %."],
  ["Oligosacáridos ácidos", "Salen con acetonitrilo + TFA."],
  ["Todos los glicanos juntos", "No: se retienen."]
]);
M("G2", "Glúcidos II §2", "Diferencia entre las etiquetas 2-AA y 2-AB:", [
  ["2-AA aporta carga negativa; 2-AB es neutra", "Las dos son fluorescentes y van al extremo reductor."],
  ["2-AB se une al extremo no reductor del glicano", "Las dos van al reductor."],
  ["2-AA no es fluorescente", "Ambas lo son."],
  ["Solo 2-AB sirve para cuantificar", "Ambas: una etiqueta por molécula."]
]);
M("G2", "Glúcidos II §2", "Un glicano en 7,0 GU (Biogel P-4) pierde un residuo con una exoglicosidasa. Ahora sale:", [
  ["En menos GU", "Quedó más chico."],
  ["En más GU", "Al achicarse baja."],
  ["En el mismo lugar", "Solo si la enzima no cortó."],
  ["En el volumen muerto", "Ahí salen los muy grandes."]
]);
M("G2", "Glúcidos II §2", "En FACE se corre una escalera de oligómeros de glucosa marcados (G4–G9) para:", [
  ["Estimar el tamaño de un glicano desconocido", "Se compara su movilidad con la escalera."],
  ["Calcular la composición de monosacáridos", "Eso es HPAEC-PAD."],
  ["Determinar la configuración α/β", "Eso dan las exoglicosidasas."],
  ["Medir la pureza de proteínas", "Es para carbohidratos."]
]);
M("G2", "Glúcidos II §1", "Durante la inflamación los leucocitos «ruedan» sobre el endotelio porque:", [
  ["Las selectinas reconocen sialyl-Lewis X", "Uniones transitorias que los frenan."],
  ["Se forman enlaces covalentes entre células", "Son uniones reversibles."],
  ["El receptor de manosa-6-P los retiene", "Ese receptor lleva enzimas al lisosoma."],
  ["La heparina los pega al endotelio", "No."]
]);
M("G2", "Glúcidos II §1", "¿Qué hace la neuraminidasa del virus de la influenza?", [
  ["Corta el ácido siálico y libera viriones", "Por eso hay antivirales que la inhiben."],
  ["Une el virus al ácido siálico de la célula", "Eso lo hace la hemaglutinina."],
  ["Glicosila las proteínas del virus", "No."],
  ["Degrada el ARN viral", "No."]
]);
M("G2", "Glúcidos II §1", "¿Por qué el LPS es un problema al producir proteínas recombinantes en E. coli?", [
  ["Contamina la proteína y causa inflamación", "Su lípido A es una endotoxina."],
  ["Degrada la proteína recombinante durante la purificación", "No es una proteasa."],
  ["Glicosila de más la proteína", "No."],
  ["Impide que la bacteria crezca", "Es parte de su membrana."]
]);

/* ======================= CÁLCULOS ======================= */
M("GC", "Glúcidos II §3", "Testigo: 0,2 mL de glucosa 1 mM → A = 0,4 (Somogyi–Nelson). Con 0,1 mL de trehalosa 5 mM, ¿A antes y después de hidrolizar?", [
  ["0 y 2,0", "Antes: no reductora. Después: 0,5 µmol × 2 Glc = 1 µmol → 2,0."],
  ["1,0 y 2,0", "Eso sería la maltosa."],
  ["0 y 1,0", "Cada trehalosa libera dos glucosas."],
  ["2,0 y 2,0", "Eso sería glucosa 10 mM."]
], "Guía 4, problema 1");
M("GC", "Glúcidos II §3", "Tras hidrolizar sacarosa, ¿qué mide cada técnica?", [
  ["Somogyi–Nelson: glucosa + fructosa; Roe: solo fructosa", "Roe detecta cetohexosas."],
  ["Somogyi–Nelson: solo la glucosa; Roe: solo la fructosa", "La fructosa también reduce en medio alcalino."],
  ["Las dos miden solo la fructosa", "Somogyi–Nelson mide todo reductor."],
  ["Roe mide la sacarosa sin hidrolizar", "Detecta cetohexosas."]
], "Guía 4");
M("GC", "Glúcidos II §3", "1 mol de celulosa tratado con periodato produce:", [
  ["3 mol de ácido fórmico", "1 del extremo no reductor + 2 del reductor."],
  ["1 mol de ácido fórmico", "Falta el extremo reductor."],
  ["2 mol de ácido fórmico", "Falta el no reductor."],
  ["Depende del largo de la cadena", "Los internos no dan fórmico."]
], "Guía 4, problema 11");
M("GC", "Glúcidos II §3", "Periodato y 1 mol de glucosa-6-fosfato (abierta): IO₄⁻ / HCOOH / HCHO", [
  ["4 / 4 / 0", "El fosfato bloquea el C6."],
  ["5 / 4 / 1", "Así sería la glucosa libre."],
  ["4 / 3 / 1", "El C6 no da metanal."],
  ["3 / 2 / 1", "Así sería la 2-desoxiglucosa."]
], "Guía 4, problema 10");
M("GC", "Glúcidos II §3", "Periodato y 1 mol de sacarosa: IO₄⁻ / HCOOH / HCHO", [
  ["3 / 1 / 0", "Glucopiranosa: 2 cortes, 1 fórmico. Fructofuranosa: 1 corte."],
  ["5 / 3 / 1", "No se abre ningún anillo."],
  ["4 / 2 / 0", "No coincide con los cortes."],
  ["0 / 0 / 0", "Hay dioles vecinales."]
], "Guía 4, problema 10");
M("GC", "Glúcidos II §3", "5,67 g de glucógeno (PM 3.240.000) dan 3,50 mmol de tetra-O-metilglucosa. ¿Extremos no reductores por molécula?", [
  ["2000", "Moléculas = 0,00175 mmol; 3,50 / 0,00175 = 2000."],
  ["1999", "Son los puntos de ramificación."],
  ["20.000", "Son las glucosas por molécula."],
  ["10", "Es el promedio de residuos por rama."]
], "Guía 4, problema 16");
M("GC", "Glúcidos II §3", "Con 20.000 glucosas y 2000 extremos no reductores por molécula:", [
  ["10 por rama y 1999 ramificaciones", "20.000/2000 = 10; PR = ENR − 1."],
  ["10 por rama y 2001 ramificaciones", "Hay una ramificación menos que ENR."],
  ["20 por rama y 1000 ramificaciones", "No sale de los datos."],
  ["8 por rama y 2000 ramificaciones", "No sale de los datos."]
], "Guía 4, problema 16");
M("GC", "Glúcidos II §3", "Un oligosacárido de hexosas tiene PM = 666. ¿Cuántas unidades?", [
  ["4", "162n + 18 = 666 → n = 4."],
  ["3", "Daría 504."],
  ["5", "Daría 828."],
  ["3,7", "Tiene que ser entero."]
], "Guía 4, problema 12");
M("GC", "Glúcidos II §3", "Fehling (−); metilación: 2,3,6-tri-O-metil y 2,3,4,6-tetra-O-metilglucosa 1:2; uniones α. Estructura compatible:", [
  ["Glcα(1→4)Glcα(1↔1)αGlc", "Una unida en C4 y dos terminales; no reductor."],
  ["Glcα(1→4)Glcα(1→4)Glc", "Sería reductor."],
  ["Glcα(1→6)Glc", "Daría 2,3,4-tri-O-metil."],
  ["Trehalosa", "Solo daría tetra-O-metil."]
], "Guía 4, problema 7");
M("GC", "Glúcidos II §3", "¿Por qué cada mol de sacarosa suma 2 mol de reductor al hidrolizarla?", [
  ["Libera glucosa y fructosa, ambas reductoras", "Antes no aportaba nada."],
  ["Porque la sacarosa ya era reductora", "No lo es."],
  ["Porque la fructosa da el doble de señal que la glucosa", "Cada monosacárido cuenta uno."],
  ["Porque el ácido de la hidrólisis reduce", "El ácido solo hidroliza."]
], "Guía 4");
/* ======================= LÍPIDOS ======================= */
M("L", "Lípidos I", "¿Qué tienen en común todos los lípidos?", [
  ["Son poco solubles en agua y solubles en solventes orgánicos", "Se agrupan por una propiedad física."],
  ["Todos tienen un esqueleto de glicerol", "Esfingolípidos y esteroles no."],
  ["Todos tienen una cabeza polar", "Los TAG son totalmente apolares."],
  ["Todos tienen ácidos grasos unidos por enlaces éster al glicerol", "El colesterol no tiene."]
]);
M("L", "Lípidos I §1", "El ácido oleico se puede nombrar como:", [
  ["18:1 Δ9, ω-9 (cis-9-octadecenoico)", "Doble enlace cis en C9; 18 − 9 = 9."],
  ["18:1 Δ9, ω-6 (trans-9-octadecenoico)", "Es ω-9 y cis; el trans es el elaídico."],
  ["16:1 Δ9, ω-7 (cis-9-hexadecenoico)", "Ese es el palmitoleico."],
  ["18:2 Δ9,12, ω-6 (linoleico)", "Ese tiene dos dobles enlaces."]
], "Parcial 2023 (Scorticati)");
M("L", "Lípidos I §1", "El EPA es 20:5 Δ5,8,11,14,17. ¿Qué familia?", [
  ["ω-3", "20 − 17 = 3."],
  ["ω-5", "5 es la posición Δ más cercana al carboxilo."],
  ["ω-6", "El araquidónico es ω-6."],
  ["ω-9", "No coincide."]
]);
M("L", "Lípidos I §1", "Si un ácido graso ω-6 se alarga en 2 carbonos:", [
  ["Sigue siendo ω-6", "Los C se agregan del lado del carboxilo."],
  ["Pasa a ser ω-8", "La distancia al metilo no cambia."],
  ["Pasa a ser ω-3", "Las familias no se interconvierten."],
  ["Pasa a ser saturado", "Alargar no quita dobles enlaces."]
]);
M("L", "Lípidos I §1", "Ordená de mayor a menor punto de fusión: 18:1 cis, 18:0, 16:0.", [
  ["18:0 > 16:0 > 18:1 cis", "Más largo → más contactos; el cis empaqueta peor."],
  ["18:1 cis > 18:0 > 16:0", "El cis baja la Tm."],
  ["16:0 > 18:0 > 18:1 cis", "El más largo funde más alto."],
  ["16:0 > 18:1 cis > 18:0", "No sigue ninguna regla."]
]);
M("L", "Lípidos I §1", "¿Por qué el aceite de oliva es líquido y la grasa del bife es sólida?", [
  ["El aceite tiene más insaturados cis", "Empaquetan mal: menos van der Waals, menor Tm."],
  ["El aceite tiene más colesterol", "Casi no tiene, y no define el estado."],
  ["La grasa animal tiene cadenas más cortas", "Más cortas fundirían antes."],
  ["El aceite tiene más dobles enlaces trans", "Los trans suben la Tm."]
], "Parcial 2023 (Scorticati)");
M("L", "Lípidos I §1", "La margarina por hidrogenación parcial es sólida porque:", [
  ["Satura dobles enlaces y genera trans", "Cadenas casi rectas que se empaquetan bien."],
  ["Agrega dobles enlaces cis a las cadenas", "Hace lo contrario."],
  ["Elimina los ácidos grasos", "Siguen siendo TAG."],
  ["Acorta las cadenas", "No las acorta."]
]);
M("L", "Lípidos I §1", "¿Por qué el linoleico y el α-linolénico son esenciales en humanos?", [
  ["No desaturamos más allá del C9", "Las posiciones ω-6 y ω-3 quedan fuera de nuestro alcance."],
  ["No podemos alargar ácidos grasos", "Sí podemos (elongasas)."],
  ["Porque son ácidos grasos saturados", "Son poliinsaturados."],
  ["Solo los sintetiza el hígado fetal", "No los fabricamos nunca."]
]);
M("L", "Lípidos I §1", "¿Qué enzima libera araquidonato de los fosfolípidos para fabricar eicosanoides?", [
  ["Fosfolipasa A₂, desde sn-2", "Después la ciclooxigenasa (blanco de la aspirina) lo transforma."],
  ["Fosfolipasa A₂, desde sn-1", "Corta en sn-2."],
  ["Ciclooxigenasa, desde sn-3", "Actúa sobre el araquidonato ya libre."],
  ["Esfingomielinasa, desde la ceramida", "Genera ceramida."]
]);
M("L", "Lípidos I §2", "¿Por qué los TAG son una reserva de energía tan eficiente?", [
  ["Carbonos muy reducidos y sin agua", "~9 kcal/g contra ~4 de glúcidos."],
  ["Porque forman bicapas compactas", "No forman bicapas."],
  ["Porque son solubles en agua", "Son apolares."],
  ["Porque contienen fosfato", "No tienen fosfato."]
]);
M("L", "Lípidos I §2", "Una gota lipídica está rodeada por:", [
  ["Una monocapa de fosfolípidos", "Colas hacia el núcleo de TAG, cabezas al citoplasma."],
  ["Una bicapa de fosfolípidos", "Adentro no hay agua."],
  ["Una pared de glucógeno", "No."],
  ["Nada: es TAG desnudo", "Tiene monocapa y proteínas."]
]);
M("L", "Lípidos I §2", "Una cera está formada por:", [
  ["Un ácido graso + un alcohol graso largo", "Unidos por éster: cubiertas impermeables."],
  ["Glicerol unido a tres ácidos grasos por éster", "Eso es un TAG."],
  ["Esfingosina + un ácido graso", "Eso es la ceramida."],
  ["Colesterol + un ácido graso", "Eso es un éster de colesterol."]
]);
M("L", "Lípidos I §2", "Un glicerofosfolípido tiene:", [
  ["Glicerol con 2 AG y un fosfato con cabeza", "La cabeza define la clase (PC, PE, PS…)."],
  ["Esfingosina con un AG por amida", "Eso es la ceramida."],
  ["Glicerol con tres ácidos grasos unidos por éster", "Eso es un TAG."],
  ["Un núcleo de cuatro anillos", "Eso es un esterol."]
], "Parcial 2023 (Fonovich / Scorticati)");
M("L", "Lípidos I §2", "¿Cuál tiene carga neta negativa a pH 7?", [
  ["Fosfatidilserina", "También PA, PG, PI y cardiolipina."],
  ["Fosfatidilcolina", "Zwitterión: neutra."],
  ["Fosfatidiletanolamina", "Zwitterión: neutra."],
  ["Esfingomielina", "Lleva fosfocolina: neutra."]
]);
M("L", "Lípidos I §2", "Sobre la esfingomielina:", [
  ["Es ceramida con fosfocolina", "Esqueleto de esfingosina, no de glicerol."],
  ["Es un glicerofosfolípido con colina", "Tiene fosfocolina pero no glicerol."],
  ["Tiene ácido siálico en la cabeza", "Eso son los gangliósidos."],
  ["Es un esterol de la mielina", "No es un esterol."]
]);
M("L", "Lípidos I §2", "¿Qué distingue a un gangliósido de un globósido?", [
  ["El gangliósido tiene ácido siálico", "Por eso es ácido; GM1 es receptor de la toxina del cólera."],
  ["El gangliósido tiene glicerol", "Ambos son esfingolípidos."],
  ["El globósido tiene un solo azúcar", "Con uno solo es un cerebrósido."],
  ["El gangliósido tiene fosfocolina", "Esa es la esfingomielina."]
]);
M("L", "Lípidos I §2", "Un plasmalógeno se distingue porque:", [
  ["Su cadena sn-1 va unida por vinil-éter", "En lugar de un éster."],
  ["Su esqueleto es la esfingosina en lugar del glicerol", "Es un glicerofosfolípido."],
  ["No tiene grupo fosfato", "Sí tiene."],
  ["Tiene tres cadenas acilo", "Tiene dos."]
]);
M("L", "Lípidos I §2", "Galactolípidos y sulfolípidos (MGDG, DGDG, SQDG) en los tilacoides permiten:", [
  ["Armar membranas con poco fósforo", "Usan azúcares en vez de fosfato."],
  ["Guardar más energía en el cloroplasto", "No es su función."],
  ["Formar micelas en el estroma", "Forman membranas."],
  ["Reemplazar al colesterol", "No son esteroles."]
]);
M("L", "Lípidos I §2", "¿Por qué las membranas de las arqueas resisten condiciones extremas?", [
  ["Usan enlaces éter y cadenas isoprenoides", "Algunas forman tetraéteres que atraviesan toda la membrana."],
  ["Tienen mucho colesterol", "No es lo característico."],
  ["Solo tienen ácidos grasos insaturados", "No."],
  ["Usan los mismos lípidos que nosotros", "Usan glicerol-1-fosfato y éteres."]
]);
M("L", "Lípidos I §3", "¿Qué fuerza principal arma espontáneamente una bicapa?", [
  ["El efecto hidrofóbico", "Al juntarse las colas se libera agua ordenada: sube la entropía."],
  ["Enlaces covalentes entre colas", "No hay."],
  ["Puentes de hidrógeno entre colas", "Las colas no los forman."],
  ["La atracción entre cabezas polares", "No explica que se junten las colas."]
]);
M("L", "Lípidos I §3", "¿Qué lípido favorece formar micelas?", [
  ["Un lisofosfolípido (una sola cola)", "Forma de cono invertido, como los detergentes."],
  ["Fosfatidilcolina (forma de cilindro)", "Forma bicapas planas."],
  ["Fosfatidiletanolamina (cono)", "Favorece curvatura negativa."],
  ["Colesterol", "Se intercala en bicapas."]
]);
M("L", "Lípidos I §3", "¿Por qué los detergentes disuelven las membranas?", [
  ["Forman micelas que se llevan lípidos y proteínas", "Tienen forma de cono invertido."],
  ["Rompen enlaces covalentes de los lípidos", "No."],
  ["Son cilíndricos y arman bicapas nuevas con los lípidos", "Los cilíndricos no disuelven membranas."],
  ["Oxidan los ácidos grasos insaturados", "Eso es peroxidación."]
]);
M("L", "Lípidos I §3", "Las nanopartículas lipídicas de las vacunas de ARN funcionan porque:", [
  ["La bicapa se cierra y encierra el ARN", "Como un liposoma: no deja bordes."],
  ["Los lípidos se unen covalentemente al ARN", "No."],
  ["El ARN queda en el centro de una micela", "El ARN es polar."],
  ["Los TAG forman la cubierta", "No tienen cabeza polar."]
]);
M("L", "Lípidos I §3", "¿Qué efecto tiene el colesterol sobre la fluidez?", [
  ["Depende de la temperatura", "La baja cuando hace calor y la sube cuando hace frío."],
  ["Siempre la aumenta, a cualquier temperatura", "A temperatura alta la disminuye."],
  ["Siempre la disminuye", "A temperatura baja la aumenta."],
  ["No tiene efecto", "Es un regulador clave."]
]);
M("L", "Lípidos I §2", "Sobre los esteroles, ¿qué es correcto?", [
  ["Abundan en la membrana plasmática", "Más que en el RE."],
  ["Su parte polar es un fosfato", "Es el OH del C3."],
  ["Los hongos usan colesterol", "Usan ergosterol."],
  ["Son precursores de los eicosanoides", "Los eicosanoides vienen del araquidonato."]
], "Parcial 2023 (Scorticati)");
M("L", "Lípidos I §2", "Muchas bacterias no tienen esteroles. Algunas ordenan su membrana con:", [
  ["Hopanoides, parecidos a los esteroles", "Cumplen un papel similar."],
  ["Colesterol que toman del medio de cultivo", "No lo obtienen."],
  ["Ceras en la membrana plasmática", "No."],
  ["Gangliósidos", "Son de animales."]
]);
M("L", "Lípidos I §3", "En apoptosis aparece fosfatidilserina en la cara externa. ¿Qué la lleva ahí?", [
  ["Una scramblasa, sin gastar ATP", "La PS expuesta es la señal de «comeme»."],
  ["Una flipasa, que gasta ATP para moverla", "Las flipasas la devuelven adentro."],
  ["La fosfolipasa A₂", "Corta cadenas, no traslada."],
  ["El flip-flop espontáneo", "Es muy lento."]
]);
M("L", "Lípidos I §3", "Flipasa vs scramblasa:", [
  ["La flipasa usa ATP; la scramblasa no", "La flipasa lleva lípidos hacia adentro; la scramblasa mezcla."],
  ["La scramblasa usa ATP; la flipasa no", "Es al revés."],
  ["Las dos degradan lípidos", "Los trasladan."],
  ["Son la misma enzima", "Tienen efectos opuestos."]
]);
M("L", "Lípidos I §3", "La cara citoplasmática de la membrana plasmática es rica en:", [
  ["PE, PS y fosfoinosítidos", "La externa: PC, esfingomielina, glicolípidos."],
  ["PC, esfingomielina y glicolípidos", "Esa es la cara externa."],
  ["Gangliósidos", "Sus azúcares miran afuera."],
  ["Solo colesterol", "Está en ambas capas."]
]);
M("L", "Lípidos I §3", "¿Qué lípido caracteriza a la membrana mitocondrial interna?", [
  ["Cardiolipina", "Organiza la cadena respiratoria (su falla da el síndrome de Barth)."],
  ["Esfingomielina", "Mielina y membrana plasmática."],
  ["Galactolípidos", "Tilacoides."],
  ["Colesterol", "Es escaso en mitocondrias."]
]);
M("L", "Lípidos I §3", "¿Por qué la membrana del RE es delgada y laxa?", [
  ["Tiene poco colesterol y más insaturados", "Facilita insertar proteínas nuevas."],
  ["Tiene mucho colesterol y esfingolípidos", "Eso es la membrana plasmática."],
  ["No tiene fosfolípidos", "Sí tiene."],
  ["Es una monocapa", "Es una bicapa."]
]);
M("L", "Lípidos I §3", "El DHA abunda en retina y sinapsis porque:", [
  ["Hace la membrana flexible y facilita la fusión", "Mucho tráfico de vesículas."],
  ["Hace la membrana más rígida y ordenada, como el colesterol", "Es al revés."],
  ["Es un ácido graso saturado", "Es poliinsaturado."],
  ["Forma micelas", "No."]
]);
M("L", "Lípidos I §3", "En la vía de Kennedy, ¿cómo se forma la fosfatidilcolina?", [
  ["DAG + CDP-colina", "El CDP activa la cabeza, como el UDP en los azúcares."],
  ["CDP-DAG + colina", "Esa rama da PI, PG y cardiolipina."],
  ["Esfingosina + fosfocolina", "Eso da esfingomielina."],
  ["Glicerol + 3 acil-CoA", "Eso da TAG."]
], "Final 2002/2003");
M("L", "Lípidos I §3", "En el ciclo de Lands se cambia:", [
  ["La cadena de sn-2", "La PLA₂ la saca y una aciltransferasa pone otra."],
  ["La cadena de sn-1", "Es la sn-2."],
  ["La cabeza polar de sn-3", "Cambia cadenas, no cabezas."],
  ["El acilo de la ceramida", "Actúa sobre glicerofosfolípidos."]
]);
M("L", "Lípidos I §3 · Ciclo de Lands", "Después de que la fosfolipasa A₂ actúa sobre una fosfatidilcolina, ¿qué queda?", [
  ["Liso-PC y un ácido graso libre", "Se cortó el éster de sn-2; queda una sola cola."],
  ["Ácido fosfatídico y colina libre", "Eso sería cortar la cabeza (lo haría una fosfolipasa D)."],
  ["Diacilglicerol y fosfocolina", "Eso sería cortar del lado del fosfato (fosfolipasa C)."],
  ["Glicerol-3-fosfato y dos ácidos grasos", "La PLA₂ corta una sola cadena."]
]);
M("L", "Lípidos I §3 · Ciclo de Lands", "En el segundo paso del ciclo de Lands, ¿de dónde sale la cadena nueva?", [
  ["De un acil-CoA, vía una aciltransferasa", "Por ejemplo LPCAT para la PC: el ácido graso ya viene activado."],
  ["De un ácido graso libre, sin activar", "Tiene que venir activado como acil-CoA."],
  ["De la cadena de sn-1 de la misma molécula", "La sn-1 no se mueve."],
  ["Del CDP-DAG de la síntesis de novo", "El CDP-DAG es de la síntesis, no del remodelado."]
]);
M("L", "Lípidos I §3 · Ciclo de Lands", "Una PC pasa por el ciclo de Lands. ¿Qué cambió al final?", [
  ["Su especie molecular, no su clase", "Cambia la cadena de sn-2; la cabeza (colina) y la sn-1 siguen iguales."],
  ["Su clase: pasó a ser otro fosfolípido", "La cabeza no cambia: sigue siendo PC."],
  ["Su esqueleto: pasó a esfingosina", "El esqueleto sigue siendo glicerol."],
  ["Las dos cadenas a la vez", "Solo cambia la de sn-2."]
]);
M("L", "Lípidos I §3 · Ciclo de Lands", "¿Por qué el PI de una célula puede terminar muy enriquecido en un tipo de cadena en sn-2?", [
  ["Su aciltransferasa prefiere esa cadena", "Al repetirse el ciclo, la clase se enriquece en lo que la enzima elige."],
  ["Porque la PLA₂ no corta al PI", "La PLA₂ corta en sn-2 en general."],
  ["Porque el PI se fabrica solo con esa cadena", "De novo depende de los acil-CoA disponibles; el enriquecimiento viene del remodelado."],
  ["Porque las cadenas pasan de sn-1 a sn-2", "Las cadenas no migran de posición."]
]);
M("L", "Lípidos I §3 · Ciclo de Lands", "La tafazina, cuya falla causa el síndrome de Barth, hace con la cardiolipina algo parecido al ciclo de Lands. ¿Qué hace?", [
  ["Remodela sus cadenas", "Cambia las cadenas de la cardiolipina ya fabricada."],
  ["Fabrica la cardiolipina desde cero", "Eso lo hace la vía del CDP-DAG."],
  ["Le agrega colesterol", "La cardiolipina no lleva colesterol."],
  ["La transporta a la membrana plasmática", "La cardiolipina es de la membrana mitocondrial interna."]
]);
M("L", "Lípidos I §3", "Una bacteria pasa de 37 °C a 15 °C. Su membrana tendrá:", [
  ["Más insaturaciones cis", "Y cadenas más cortas o ramificadas: recupera fluidez."],
  ["Más saturados y más largos", "Eso compensa el calor."],
  ["Más colesterol", "Casi no tiene esteroles."],
  ["La misma composición", "Ajusta su composición."]
]);
M("L", "Lípidos I §3", "En B. subtilis, cuando el frío rigidiza la membrana, el sensor DesK:", [
  ["Termina activando una desaturasa", "Fosforila a DesR; se agregan dobles enlaces cis."],
  ["Termina activando una enzima saturadora", "Saturar la rigidizaría más."],
  ["Degrada fosfolípidos rígidos", "Es un sensor."],
  ["Hace que la bacteria capte colesterol", "No."]
]);
M("L", "Lípidos I §3", "En la levadura, una membrana muy saturada activa Mga2. ¿Qué logra?", [
  ["Que se exprese una desaturasa (OLE1)", "La membrana controla la maquinaria que la modifica."],
  ["Que se fabrique más ergosterol para ordenar la membrana", "No es esta respuesta."],
  ["Que se degraden los fosfolípidos", "No."],
  ["Que se exprese una elongasa", "La respuesta es desaturar."]
]);
M("L", "Lípidos I §3", "Pseudomonas expuesta a solventes isomeriza cis → trans (enzima Cti). ¿Para qué?", [
  ["Para rigidizar rápido la membrana", "Actúa sobre los AG que ya están, sin síntesis nueva."],
  ["Para aumentar la fluidez de la membrana", "Los trans ordenan la membrana."],
  ["Para fabricar AG esenciales", "No."],
  ["Para formar ciclopropanos", "Eso lo hace otra enzima (Cfa)."]
]);
M("L", "Lípidos I §3", "En Gram positivas, ¿qué ramificación fluidifica más la membrana?", [
  ["anteiso", "El metilo más adentro desordena más."],
  ["iso", "Fluidifica menos."],
  ["Las dos por igual", "No."],
  ["Ninguna", "Las dos alteran el empaquetamiento."]
]);
M("L", "Lípidos I §3", "La ciclopropanación de ácidos grasos (enzima Cfa) ocurre sobre todo:", [
  ["En fase estacionaria o estrés ácido", "Los dobles enlaces pasan a anillos de ciclopropano."],
  ["Durante el crecimiento rápido a alta temperatura", "No."],
  ["Solo en arqueas", "Ocurre en bacterias."],
  ["Al agregar colesterol", "No."]
]);
M("L", "Lípidos I §3", "El sistema SREBP/Scap se activa cuando:", [
  ["Falta colesterol en el RE", "Activa genes para fabricar y captar colesterol."],
  ["Sobran ácidos grasos poliinsaturados", "No."],
  ["Sube la curvatura de la membrana", "Eso lo detectan otros sensores (ALPS)."],
  ["Faltan esfingolípidos", "Eso lo vigila otro sistema."]
]);
M("L", "Lípidos I §3", "En la ferroptosis la célula muere porque:", [
  ["Se oxidan en cadena los PUFA de la membrana", "Peroxidación lipídica."],
  ["Se acumulan gotas de TAG que rompen el citoplasma", "No."],
  ["Le falta colesterol", "No."],
  ["Se expone fosfatidilserina", "Eso es apoptosis."]
]);
M("L", "TP4", "¿Qué mezcla de extracción usa el método de Folch?", [
  ["Cloroformo : metanol 2:1", "Se usó para mejillón y avena."],
  ["Cloroformo : metanol 1:1", "Bligh-Dyer adaptado (hojas)."],
  ["Hexano : éter : acético 60:40:2,5", "Es la fase móvil de la TLC."],
  ["KCl 0,88 %", "Es un lavado."]
], "TP4");
M("L", "TP4", "Después de los lavados con KCl y FST, ¿qué fase se conserva?", [
  ["La fase inferior (cloroformo)", "Retiene los lípidos."],
  ["La fase superior (acuosa, con metanol)", "Arrastra contaminantes polares."],
  ["El pellet sólido", "Es material insoluble."],
  ["Las dos mezcladas", "Se separan por partición."]
], "TP4");
M("L", "TP4", "En la TLC del TP4 (sílica; hexano:éter:acético), ¿qué migra más?", [
  ["Los triacilglicéridos", "Apolares: poca retención en la sílica."],
  ["Los fosfolípidos, por su cabeza cargada", "Quedan cerca del origen por su cabeza polar."],
  ["Migran igual", "Polaridades muy distintas."],
  ["Ninguno se mueve", "Los apolares avanzan."]
], "TP4");

/* ---- imágenes ---- */
M("L", "Lípidos I §1", "¿Cuál es el ácido oleico?", [
  ["Ácido oleico", "18 C, un doble enlace cis en Δ9 (se ve el codo).", "oleico"],
  ["Ácido elaídico", "Mismo doble enlace pero trans: recto.", "elaidico"],
  ["Ácido esteárico", "Saturado.", "estearico"],
  ["Ácido linoleico", "Dos dobles enlaces.", "linoleico"]
], "Parcial 2023 (Scorticati)");
M("L", "Lípidos I §1", "¿Cuál tiene el punto de fusión más alto?", [
  ["Ácido esteárico 18:0", "Largo y saturado.", "estearico"],
  ["Ácido palmítico 16:0", "Saturado pero más corto.", "palmitico"],
  ["Ácido oleico 18:1", "El codo cis baja la Tm.", "oleico"],
  ["Ácido linoleico 18:2", "Dos codos.", "linoleico"]
]);
M("L", "Lípidos I §1", "¿Cuál es un ω-3 esencial?", [
  ["α-linolénico", "18 − 15 = 3.", "linolenico"],
  ["Linoleico", "ω-6.", "linoleico"],
  ["Araquidónico", "ω-6.", "araquidonico"],
  ["Oleico", "ω-9.", "oleico"]
]);
M("L", "Lípidos I §2", "¿Cuál tiene carga neta negativa a pH 7?", [
  ["Fosfatidilserina", "Fosfato −, NH₃⁺ y COO⁻: neto −1.", "ps"],
  ["Fosfatidilcolina", "Neutra.", "pc"],
  ["Fosfatidiletanolamina", "Neutra.", "pe"],
  ["Triacilglicérido", "Sin carga.", "tag"]
]);
M("L", "Lípidos I §2", "¿Cuál es la esfingomielina?", [
  ["Esfingomielina", "Ceramida + fosfocolina.", "esfingomielina"],
  ["Fosfatidilcolina", "Glicerol con dos ésteres.", "pc"],
  ["Ceramida", "Sin cabeza polar.", "ceramida"],
  ["Esfingosina", "Sin ácido graso.", "esfingosina"]
]);
M("L", "Lípidos I §2", "¿Cuál es el colesterol?", [
  ["Colesterol", "Un doble enlace en el anillo B y cadena lateral saturada.", "colesterol"],
  ["Ergosterol", "Más dobles enlaces (hongos).", "ergosterol"],
  ["Ceramida", "Esfingolípido.", "ceramida"],
  ["Triacilglicérido", "No es un esterol.", "tag"]
]);
M("L", "Lípidos I §2", "¿Cuál NO puede formar una bicapa por sí solo?", [
  ["Triacilglicérido", "Totalmente apolar.", "tag"],
  ["Fosfatidilcolina", "Anfipática y cilíndrica.", "pc"],
  ["Fosfatidiletanolamina", "Anfipática.", "pe"],
  ["Esfingomielina", "Anfipática.", "esfingomielina"]
]);
/* ======================= ÁCIDOS NUCLEICOS I ======================= */
M("N", "Ác. nucleicos I §5", "Tres ADN tienen 35, 50 y 66 % de G+C. ¿Cuál tiene la Tm más alta y por qué?", [
  ["El de 66 %: más pares G≡C", "3 puentes de H y mejor apilamiento."],
  ["El de 35 %: más pares A=T", "A=T tiene solo 2 puentes de H."],
  ["El de 50 %: está equilibrado", "El equilibrio no da ventaja."],
  ["Todos igual: depende del largo", "Depende sobre todo de la composición."]
], "Parcial 2023 (Scorticati)");
M("N", "Ác. nucleicos I §5", "Al desnaturalizar el ADN por calor:", [
  ["Se rompen puentes de H y apilamiento", "Los enlaces covalentes quedan intactos."],
  ["Se rompen los enlaces fosfodiéster", "No se rompe el esqueleto."],
  ["Se rompen los enlaces N-glicosídicos", "Son covalentes."],
  ["El ADN se degrada a nucleótidos", "Eso lo hacen las nucleasas."]
], "Parcial 2023 (Scorticati)");
M("N", "Ác. nucleicos I §5", "El efecto hipercrómico es:", [
  ["El aumento de A₂₆₀ al separarse las cadenas", "Las bases apiladas absorben menos."],
  ["La disminución de A₂₆₀ al desnaturalizar", "Es un aumento."],
  ["El aumento de A₂₈₀ de las proteínas", "Es de ácidos nucleicos a 260 nm."],
  ["El cambio de color al calentar el ADN", "Es absorción UV."]
]);
M("N", "Ác. nucleicos I §5", "Curva de fusión de 1,0 (apareado) a 1,4 (desapareado). La Tm se lee:", [
  ["En la temperatura donde la curva vale 1,2", "50 % desapareado."],
  ["En el eje vertical, en 1,2", "La Tm es una temperatura."],
  ["Donde la curva llega a 1,4", "Ahí ya está todo desapareado."],
  ["En la temperatura donde la curva empieza a subir", "Es el comienzo de la transición."]
]);
M("N", "Ác. nucleicos I §5", "Un ADN desnaturalizado se enfría lentamente. ¿Qué pasa?", [
  ["Se reaparea y baja la A₂₆₀", "Vuelve el apilamiento."],
  ["Queda roto en nucleótidos", "No se rompieron enlaces covalentes."],
  ["La A₂₆₀ sigue subiendo", "Baja al reaparearse."],
  ["Se transforma en ARN", "No."]
]);
M("N", "Ác. nucleicos I §1", "Adenina + ribosa + un fosfato en 5′ se llama:", [
  ["AMP", "Adenosín 5′-monofosfato (adenilato): nucleótido de ribosa."],
  ["Adenosina", "Es el nucleósido, sin fosfato."],
  ["dAMP", "La d indica desoxirribosa."],
  ["ADP", "Tendría dos fosfatos."]
], "Parcial 2023 (Scorticati)");
M("N", "Ác. nucleicos I §1", "Adenina unida a desoxirribosa, sin fosfato:", [
  ["Desoxiadenosina", "Purina → -osina; con desoxi."],
  ["Desoxiadenilato (dAMP)", "Tendría un fosfato."],
  ["Adenosina", "Tendría ribosa."],
  ["Desoxiadenidina", "-idina es para pirimidinas."]
], "Parcial 2023 (Scorticati)");
M("N", "Ác. nucleicos I §1", "La uridina es:", [
  ["Un nucleósido", "Uracilo + ribosa; pirimidina → -idina."],
  ["Una base nitrogenada", "La base es el uracilo."],
  ["Un nucleótido", "Sin fosfato; el nucleótido es UMP."],
  ["Un componente del ADN", "El uracilo es del ARN."]
]);
M("N", "Ác. nucleicos I §1", "Enlaces del ATP entre azúcar y fosfatos:", [
  ["1 fosfoéster y 2 fosfoanhídrido", "Los fosfoanhídrido son los de alta energía."],
  ["3 fosfoanhídrido", "Pα–azúcar es fosfoéster."],
  ["2 fosfodiéster", "El fosfodiéster une dos azúcares."],
  ["2 fosfoéster y 1 fosfoanhídrido", "Hay un solo fosfoéster."]
]);
M("N", "Ác. nucleicos I §1", "El enlace N-glicosídico de un nucleósido une:", [
  ["C1′ con N9 (purinas) o N1 (pirimidinas)", "Siempre β."],
  ["C1′ con N1 en purinas y pirimidinas", "En purinas es N9."],
  ["C5′ del azúcar con el fosfato", "Ese es el fosfoéster."],
  ["C3′ de un azúcar con C5′ del siguiente", "Ese es el fosfodiéster."]
]);
M("N", "Ác. nucleicos I §1", "¿Cuál NO es una diferencia entre ADN y ARN?", [
  ["El tipo de enlace del esqueleto", "Los dos usan fosfodiéster 3′→5′."],
  ["El azúcar (desoxirribosa vs ribosa)", "Sí es diferencia."],
  ["La base exclusiva (T vs U)", "Sí es diferencia."],
  ["La estabilidad en medio alcalino", "Sí: el ARN es lábil por el 2′-OH."]
], "Parcial 2023 (Scorticati)");
M("N", "Ác. nucleicos I §1", "¿Por qué el ARN se hidroliza fácil en medio alcalino y el ADN no?", [
  ["Su 2′-OH ataca el fosfodiéster vecino", "El ADN no tiene 2′-OH."],
  ["Porque contiene uracilo en lugar de timina", "La base no ataca el esqueleto."],
  ["Porque es de cadena simple", "No es la causa química."],
  ["Porque no tiene fosfodiéster", "Sí tiene."]
]);
M("N", "Ác. nucleicos I §2", "Griffith (1928) demostró que:", [
  ["Hay un factor transformante heredable", "S muertas + R vivas matan al ratón; no sabía qué molécula era."],
  ["El factor transformante es el ADN", "Eso fue Avery, MacLeod y McCarty."],
  ["El ADN es el material genético de los fagos", "Eso fue Hershey y Chase."],
  ["Las bacterias S muertas reviven", "Las que cambiaron fueron las R."]
]);
M("N", "Ác. nucleicos I §2", "Avery, MacLeod y McCarty concluyeron que el factor era ADN porque:", [
  ["Solo la ADNasa anuló la transformación", "Proteasas, ARNasa y polisacaridasa no."],
  ["Las proteasas anularon la transformación", "No la anularon."],
  ["La ARNasa anuló la transformación", "No la anuló."],
  ["Vieron ADN con ³²P dentro de las bacterias", "Eso es Hershey y Chase."]
], "Parcial 2019 (Scorticati)");
M("N", "Ác. nucleicos I §2", "Hershey y Chase: tras infectar, licuar y centrifugar:", [
  ["El ³²P queda en el pellet con las bacterias", "El ADN entró: es el material genético."],
  ["El ³⁵S queda en el pellet con las bacterias", "Las proteínas quedaron afuera."],
  ["Los dos quedan en el sobrenadante", "El ADN entró."],
  ["El ³²P marca las proteínas del fago", "El P está en el ADN."]
], "Parcial 2019 (Scorticati)");
M("N", "Ác. nucleicos I §2", "¿Por qué la hipótesis del tetranucleótido hacía ver al ADN incapaz de ser material genético?", [
  ["Implicaba una secuencia repetitiva y monótona", "Un bloque de 4 repetido no guarda información."],
  ["Decía que el ADN no tenía grupos fosfato en su estructura", "Sí lo incluía."],
  ["Decía que el ADN tenía 20 bases", "Tenía 4."],
  ["Decía que el ADN era una proteína", "No."]
]);
M("N", "Ác. nucleicos I §2", "Después de que Miescher aisló la «nucleína», el siguiente avance fue:", [
  ["Describir sus componentes y sus 5 bases", "Lo hizo Kossel: base + azúcar + fosfato."],
  ["Proponer el modelo de la doble hélice", "Eso fue en 1953."],
  ["Hacer la difracción de rayos X", "Eso fue Franklin y Wilkins."],
  ["Medir la composición de bases", "Eso fue Chargaff."]
]);
M("N", "Ác. nucleicos I §3", "Bicatenario de 1000 pb con 58 % de G+C. ¿Cuántas bases de cada tipo?", [
  ["G = C = 580; A = T = 420", "2000 bases; G+C = 1160."],
  ["G = C = 290; A = T = 210", "Contaste 1000 bases en vez de 2000."],
  ["G = C = 580; A = T = 580", "A+T debe ser 42 %."],
  ["G = 580; C = 420", "En doble cadena G = C."]
], "Guía 5, problema 10");
M("N", "Ác. nucleicos I §3", "Un ADN bicatenario tiene 22 % de G. ¿Cuánto tiene de A?", [
  ["28 %", "G+C = 44 % → A+T = 56 %."],
  ["22 %", "Eso es la C."],
  ["56 %", "Es A+T."],
  ["78 %", "No se resta así."]
]);
M("N", "Ác. nucleicos I §3", "Bacteria 1: G+C 36 %. Bacteria 2: G+C 66 %. ¿Cuál es más probablemente termófila?", [
  ["La 2", "Más G+C → mayor Tm."],
  ["La 1", "Más A–T → menor Tm."],
  ["No se puede saber con estos datos", "El G+C alcanza."],
  ["Las dos igual porque cumplen Chargaff", "Chargaff no habla de estabilidad."]
], "Guía 5, problema 12");
M("N", "Ác. nucleicos I §3", "[purinas] = [pirimidinas] se cumple para:", [
  ["ADN de doble cadena", "Cada purina tiene enfrente una pirimidina."],
  ["Cualquier ácido nucleico", "No en cadena simple ni ARN."],
  ["Solo el ARN", "Suele ser monocatenario."],
  ["Una cadena simple de ADN", "No necesariamente."]
]);
M("N", "Ác. nucleicos I §3", "Chargaff mostró que la composición de bases del ADN:", [
  ["Varía entre especies", "Y es igual en todos los tejidos de una especie."],
  ["Es igual en todas las especies", "Varía: por eso puede guardar información."],
  ["Cambia con la dieta", "No."],
  ["Es siempre 25 % de cada base", "Eso decía el tetranucleótido."]
]);
M("N", "Ác. nucleicos I §3", "Según el modelo de Watson y Crick:", [
  ["Cada par es purina–pirimidina", "Así el diámetro es constante (~20 Å)."],
  ["Las cadenas son paralelas", "Son antiparalelas."],
  ["Los fosfatos están adentro de la hélice", "Están afuera."],
  ["La hélice es levógira", "La B es dextrógira."]
]);
M("N", "Ác. nucleicos I §3", "La complementaria de 5′-ATGCCA-3′, escrita 5′→3′, es:", [
  ["5′-TGGCAT-3′", "3′-TACGGT-5′ invertida."],
  ["5′-TACGGT-3′", "Está escrita al revés."],
  ["5′-ATGCCA-3′", "Es la misma."],
  ["5′-UGGCAU-3′", "El ADN no tiene U."]
]);
M("N", "Ác. nucleicos I §3 · Foto 51", "En este esquema de la Foto 51, ¿qué indica lo que está marcado?", [
  ["Que la molécula es una hélice", "La cruz en X aparece porque los tramos de una hélice, vistos de costado, se inclinan hacia dos lados."],
  ["Que hay dos cadenas", "Eso lo indica la 4.ª línea que falta, no la X."],
  ["Que las bases están cada 3,4 Å", "Eso son las manchas fuertes arriba y abajo."],
  ["Que el diámetro es de 20 Å", "Eso sale de qué tan lejos del eje están las primeras manchas."]
], null, "f51_1");
M("N", "Ác. nucleicos I §3 · Foto 51", "En este esquema de la Foto 51, ¿qué indican las manchas marcadas, arriba y abajo?", [
  ["La separación de 3,4 Å entre bases apiladas", "Son las más lejanas del centro: la distancia más chica."],
  ["Lo que mide una vuelta, 34 Å", "Eso es la separación entre filas, cerca del centro."],
  ["El diámetro de la hélice", "Sale del ancho del patrón."],
  ["La presencia de una segunda cadena", "Eso lo indica la 4.ª línea ausente."]
], null, "f51_3");
M("N", "Ác. nucleicos I §3 · Foto 51", "En este esquema de la Foto 51, ¿qué te dice la fila marcada?", [
  ["Que hay dos cadenas desplazadas", "En la 4.ª fila lo que dispersa cada cadena se anula: falta esa línea."],
  ["Que la hélice es levógira", "La foto no indica eso; la forma B es dextrógira."],
  ["Que hay 4 pares de bases por vuelta", "Hay 10: las manchas de 3,4 Å caen en la fila 10."],
  ["Que la muestra estaba mal hidratada", "No."]
], null, "f51_4");
M("N", "Ác. nucleicos I §3 · Foto 51", "En este esquema de la Foto 51, ¿qué indican las zonas vacías marcadas (los rombos)?", [
  ["Que los fosfatos están afuera", "La mayor parte de los electrones está en el radio externo."],
  ["Que hay dos cadenas", "Eso lo indica la 4.ª línea."],
  ["Que la molécula no es una hélice", "La X dice que sí lo es."],
  ["Que la muestra estaba dañada", "Es parte del patrón de una hélice con los fosfatos afuera."]
], null, "f51_6");
M("N", "Ác. nucleicos I §3 · Foto 51", "La separación entre las filas horizontales de manchas de la Foto 51 corresponde a:", [
  ["Lo que mide una vuelta (34 Å)", "Las filas se repiten con la periodicidad de la hélice."],
  ["La distancia entre bases (3,4 Å)", "Esas son las manchas del meridiano, en la fila 10."],
  ["El diámetro de la hélice (20 Å)", "Sale de la distancia de las manchas al eje vertical."],
  ["El largo total de la molécula", "Es una distancia que se repite, no el largo total."]
]);
M("N", "Ác. nucleicos I §3 · Foto 51", "Si una hélice tuviera vueltas más largas que las del ADN B, en su foto de difracción las filas de manchas estarían:", [
  ["Más juntas", "Relación inversa: distancias grandes dan ángulos chicos."],
  ["Más separadas", "Eso pasaría con vueltas más cortas."],
  ["Igual que en la Foto 51", "Cambia la periodicidad, cambia el patrón."],
  ["Todas sobre el eje vertical", "No."]
]);
M("N", "Ác. nucleicos I §3 · Foto 51", "Según la ley de Bragg (nλ = 2d·sen θ), una mancha muy lejos del centro de la foto corresponde a:", [
  ["Una distancia chica en la molécula", "Ángulo grande ↔ d chica: por eso 3,4 Å aparece en los bordes."],
  ["Una distancia grande en la molécula", "Es al revés."],
  ["Una zona con más fosfato", "La posición indica distancias que se repiten."],
  ["Un error de la película", "No."]
]);
M("N", "Ác. nucleicos I §3 · Foto 51", "Las manchas de 3,4 Å caen en la fila número 10 de la Foto 51. ¿Qué se deduce?", [
  ["Que hay 10 pares de bases por vuelta", "34 Å ÷ 3,4 Å = 10."],
  ["Que el diámetro es de 10 Å", "Es de unos 20 Å."],
  ["Que hay 10 cadenas", "Hay dos."],
  ["Que la vuelta mide 10 Å", "Mide 34 Å."]
]);
M("N", "Ác. nucleicos I §3 · Foto 51", "¿Por qué los brazos de la Foto 51 forman una X?", [
  ["La hélice de costado es un zigzag", "Tramos inclinados hacia dos lados: cada dirección da una fila de manchas perpendicular."],
  ["Porque hay dos cadenas cruzadas", "Una sola hélice ya da una X."],
  ["Porque la fibra estaba cruzada", "Las fibras están alineadas."],
  ["Porque las bases forman una cruz", "Las bases dan las manchas del meridiano."]
]);
M("N", "Ác. nucleicos I §3 · Foto 51", "Para que se anule justo la 4.ª línea, la segunda cadena está corrida 3/8 de vuelta. ¿Qué consecuencia estructural tiene?", [
  ["Hay un surco mayor y uno menor", "Las cadenas no quedan equidistantes: 3/8 y 5/8 de vuelta."],
  ["Las dos cadenas son paralelas", "Son antiparalelas; el desfase no cambia eso."],
  ["La hélice es levógira", "No."],
  ["Las bases quedan afuera", "Quedan adentro."]
]);
M("N", "Ác. nucleicos I §3", "En la Foto 51, ¿qué indica que hay dos cadenas?", [
  ["La ausencia de la 4.ª línea de manchas", "Las ondas de las dos cadenas se anulan ahí."],
  ["La cruz en forma de X", "Indica que es una hélice."],
  ["Las manchas intensas a 3,4 Å en el meridiano", "Son las bases apiladas."],
  ["La repetición cada 34 Å", "Es una vuelta."]
]);
M("N", "Ác. nucleicos I §3", "En un patrón de difracción, la cruz en X indica que:", [
  ["La molécula es una hélice", "Patrón típico de hélice."],
  ["Tiene dos cadenas", "Eso lo indica la 4.ª línea ausente."],
  ["Las bases están adentro", "No se deduce de la cruz."],
  ["Tiene uracilo", "No."]
]);
M("N", "Ác. nucleicos I §3", "En el ADN B, una vuelta mide y contiene:", [
  ["34 Å y unos 10 pb", "34 / 3,4 = 10."],
  ["3,4 Å y 1 pb", "3,4 Å es entre pares."],
  ["20 Å y 12 pb", "20 Å es el diámetro; 12 pb es la Z."],
  ["340 Å y 100 pb", "No."]
]);
M("N", "Ác. nucleicos I §3", "El ADN de una célula humana (~6,4 × 10⁹ pb, 0,34 nm/pb) estirado mide:", [
  ["≈ 2 m", "6,4 × 10⁹ × 3,4 × 10⁻¹⁰ m."],
  ["≈ 2 µm", "Se queda corto."],
  ["≈ 34 Å", "Es una vuelta."],
  ["≈ 10 km", "Se pasa."]
], "Guía 5, problema 14");
M("N", "Ác. nucleicos I §3", "6 pg de ADN por célula y 2 × 10¹² células. ¿ADN total?", [
  ["12 g", "6 × 10⁻¹² × 2 × 10¹²."],
  ["12 mg", "Error de unidades."],
  ["1,2 kg", "Se pasa."],
  ["3 g", "No sale."]
], "Guía 5, problema 14");
M("N", "Ác. nucleicos I §4", "La forma Z del ADN:", [
  ["Es levógira y aparece con d(GC) repetido", "In vitro; esqueleto en zig-zag."],
  ["Es la forma más común en la célula", "La más común es la B."],
  ["Es dextrógira, igual que las formas A y B", "Es levógira."],
  ["Es de una sola cadena", "Es una doble hélice."]
]);
M("N", "Ác. nucleicos I §4", "Un híbrido ARN–ADN adopta la forma:", [
  ["A", "El 2′-OH impide la B."],
  ["B", "Es la del ADN fisiológico."],
  ["Z", "Aparece con d(GC)."],
  ["No forma hélice", "Sí la forma."]
]);
M("N", "Ác. nucleicos I §5", "¿Por qué el ADN usa timina y no uracilo?", [
  ["Para detectar las C desaminadas", "Todo U en el ADN es daño y se repara."],
  ["El U no se aparea con A", "Sí se aparea."],
  ["Fabricar timina es más barato que uracilo", "Es más caro."],
  ["La T forma 3 puentes de H", "A–T forma 2."]
]);
M("N", "Ác. nucleicos I §5", "La uracilo-ADN glicosilasa y la dUTPasa sirven para:", [
  ["Que no quede U en el ADN", "Una saca U del ADN; la otra elimina el dUTP antes de que se incorpore."],
  ["Fabricar dUTP para la replicación", "Al revés."],
  ["Convertir UTP en CTP", "Eso lo hace la CTP sintetasa."],
  ["Agregar U al ARN", "No."]
]);

/* ---- imágenes ---- */
M("N", "Ác. nucleicos I §1", "¿Cuál es el azúcar del ADN?", [
  ["2-desoxirribosa", "H en lugar de OH en el C2′.", "h_bdrib"],
  ["Ribosa", "OH en C2′: ARN.", "h_brib"],
  ["Fructofuranosa", "Cetohexosa.", "h_bfru"]
]);
M("N", "Ác. nucleicos I §1", "¿Cuál es una purina?", [
  ["Guanina", "Dos anillos fusionados.", "guanina"],
  ["Citosina", "Un anillo.", "citosina"],
  ["Timina", "Un anillo.", "timina"],
  ["Uracilo", "Un anillo.", "uracilo"]
]);
M("N", "Ác. nucleicos I §1", "¿Cuál es la timina?", [
  ["Timina", "Uracilo con CH₃ en C5.", "timina"],
  ["Uracilo", "Sin metilo.", "uracilo"],
  ["Citosina", "NH₂ en C4.", "citosina"],
  ["5-fluorouracilo", "F en C5.", "fu"]
]);
M("N", "Ác. nucleicos I §1", "¿Cuál es un nucleósido?", [
  ["Adenosina", "Base + ribosa.", "adenosina"],
  ["AMP", "Tiene fosfato.", "amp"],
  ["Adenina", "Solo la base.", "adenina"],
  ["ATP", "Tres fosfatos.", "atp"]
]);
M("N", "Ác. nucleicos I §1", "¿Cuál es el dAMP?", [
  ["dAMP", "Sin OH en 2′ y con un fosfato.", "damp"],
  ["AMP", "Ribosa.", "amp"],
  ["Desoxiadenosina", "Sin fosfato.", "dadenosina"],
  ["AMP cíclico", "Fosfato 3′–5′.", "camp"]
]);

/* ======================= ÁCIDOS NUCLEICOS II ======================= */
/* ======================= ÁCIDOS NUCLEICOS II (versión simplificada) ======================= */
/* §1 Dogma y ARN */
M("NM", "AN II simple §1 · Dogma y ARN", "¿Qué flujo de información prohíbe el dogma central?", [
  ["De proteína a ácido nucleico", "Una vez en la proteína, la información no puede volver a salir."],
  ["De ARN a ADN, como en los retrovirus", "Es la retrotranscripción de los retrovirus: no contradice el dogma."],
  ["De ADN a ARN", "Es la transcripción, el flujo normal."],
  ["De ADN a ADN", "Es la replicación, también permitida."]
]);
M("NM", "AN II simple §1 · Dogma y ARN", "¿Cuál es el ARN más abundante de la célula (casi el 80 % del total)?", [
  ["El ARNr (ribosomal)", "Forma los ribosomas, que son muchísimos."],
  ["El ARNm (mensajero)", "Es una fracción chica y dura poco."],
  ["El ARNt (de transferencia)", "Es abundante, pero mucho menos que el ribosomal."],
  ["El ARNsn (nuclear pequeño)", "Es una fracción mínima: forma el espliceosoma."]
]);
M("NM", "AN II simple §1 · Dogma y ARN", "Comparando ADN y ARN en una célula:", [
  ["Hay más ARN (hasta 10 veces)", "El ADN es una copia guardada; el ARN se fabrica en muchas copias."],
  ["Hay más ADN, porque es el que guarda todo", "Es al revés: el ARN se hace en muchas copias."],
  ["Hay cantidades iguales", "No: el ARN se transcribe en muchas copias."],
  ["Solo hay ARN en la división", "El ARN está siempre: se usa para fabricar proteínas."]
]);
M("NM", "AN II simple §1 · Dogma y ARN", "¿Qué molécula funciona como adaptador entre el codón y el aminoácido?", [
  ["El ARNt, con su anticodón", "Lleva el aminoácido en el 3′ y lee el codón con el anticodón."],
  ["El ARNr, con su peptidil transferasa", "El ARNr forma el enlace, no lee los codones."],
  ["El ARNm, con su cap", "El ARNm es el mensaje que se lee."],
  ["La aminoacil-ARNt sintetasa sola", "Carga el ARNt, pero el que lee el codón es el ARNt."]
]);
M("NM", "AN II simple §1 · Dogma y ARN", "¿Por qué se dice que el ribosoma es una ribozima?", [
  ["Su ARNr cataliza el enlace peptídico", "La peptidil transferasa es ARN, no proteína."],
  ["Porque sus proteínas catalizan el enlace peptídico", "Lo cataliza el ARNr, no las proteínas."],
  ["Porque corta intrones", "Eso lo hace el espliceosoma."],
  ["Porque se copia a sí mismo", "Los ribosomas no se autorreplican."]
]);

/* §2 Replicación */
M("NM", "AN II simple §2 · Replicación", "Que la replicación sea semiconservativa significa que:", [
  ["Cada hija: una cadena vieja y una nueva", "La cadena vieja sirve de molde."],
  ["Una hija queda toda vieja y la otra toda nueva", "Eso sería conservativa."],
  ["Cada cadena mezcla tramos viejos y nuevos", "Eso sería dispersiva."],
  ["Se copia solo la mitad del genoma", "Se copia todo."]
]);
M("NM", "AN II simple §2 · Replicación", "¿Por qué la ADN polimerasa necesita un cebador?", [
  ["Solo alarga un 3′-OH ya existente", "No puede empezar de cero; el cebador le da ese extremo."],
  ["Necesita el cebador para reconocer la cadena molde", "El molde lo reconoce igual; el problema es arrancar."],
  ["Para separar las dos cadenas", "Eso lo hace la helicasa."],
  ["Para sintetizar en sentido 3′→5′", "Siempre sintetiza 5′→3′."]
]);
M("NM", "AN II simple §2 · Replicación", "¿Qué enzima arma el cebador?", [
  ["La primasa (una ARN polimerasa)", "Por eso el cebador es de ARN."],
  ["La ADN polimerasa III, que también lo alarga", "Ella alarga el cebador, no lo hace."],
  ["La ADN ligasa", "Une fragmentos."],
  ["La helicasa", "Separa cadenas."]
]);
M("NM", "AN II simple §2 · Replicación", "La helicasa, en la horquilla de replicación:", [
  ["Separa las dos cadenas", "Rompe los puentes de H entre las bases, con gasto de ATP."],
  ["Saca la tensión de adelante", "Eso lo hace la topoisomerasa."],
  ["Mantiene estiradas las cadenas simples", "Eso lo hacen las SSB."],
  ["Une los fragmentos de Okazaki", "Eso lo hace la ligasa."]
]);
M("NM", "AN II simple §2 · Replicación", "Por delante de la horquilla se acumula superenrollamiento. ¿Quién lo resuelve?", [
  ["La topoisomerasa (girasa)", "Corta, deja girar y vuelve a sellar el ADN."],
  ["La helicasa, que la va soltando al avanzar", "Es la que genera la tensión al abrir la hélice."],
  ["Las proteínas SSB", "Cubren la cadena simple."],
  ["La primasa", "Pone cebadores."]
]);
M("NM", "AN II simple §2 · Replicación", "¿Para qué sirven las proteínas SSB?", [
  ["Separan las cadenas simples", "Evitan que se vuelvan a aparear o se plieguen."],
  ["Sacan los cebadores de ARN de la hebra retrasada", "Eso lo hace la ADN polimerasa I."],
  ["Reconocen el origen", "Eso lo hacen proteínas iniciadoras."],
  ["Sintetizan la hebra retrasada", "Eso lo hace la ADN polimerasa III."]
]);
M("NM", "AN II simple §2 · Replicación", "¿Por qué la hebra retrasada se sintetiza en fragmentos?", [
  ["Su síntesis va contra la horquilla", "Hay que ir arrancando de nuevo a medida que se abre."],
  ["Porque su molde está dañado", "No tiene nada de distinto químicamente."],
  ["Porque la copia otra polimerasa, más lenta y sin cebador", "La copia la misma ADN polimerasa III."],
  ["Porque se copia después de la adelantada", "Se copian a la vez."]
]);
M("NM", "AN II simple §2 · Replicación", "¿Qué hace la ADN polimerasa I?", [
  ["Cambia los cebadores por ADN", "Exonucleasa 5′→3′ para sacar y polimerasa para rellenar."],
  ["Copia la hebra adelantada de manera continua", "Eso lo hace la ADN polimerasa III."],
  ["Une los fragmentos con un enlace", "Eso lo hace la ligasa."],
  ["Abre la doble hélice", "Eso lo hace la helicasa."]
]);
M("NM", "AN II simple §2 · Replicación", "La ADN ligasa:", [
  ["Sella la mella con un enlace fosfodiéster", "Sella la mella y la hebra queda continua."],
  ["Pone los cebadores de ARN en la hebra retrasada", "Eso lo hace la primasa."],
  ["Saca el ARN de los cebadores", "Eso lo hace la ADN polimerasa I."],
  ["Separa las dos moléculas hijas", "No es su función."]
]);
M("NM", "AN II simple §2 · Replicación", "Que la replicación sea bidireccional significa que:", [
  ["Del origen salen dos horquillas opuestas", "Avanzan en sentidos contrarios."],
  ["Se sintetiza a la vez en sentido 5′→3′ y 3′→5′", "Siempre se sintetiza 5′→3′."],
  ["Se copian ADN y ARN a la vez", "Solo se copia ADN."],
  ["Cada cadena se copia dos veces", "Cada una se copia una vez."]
]);

/* §3 Transcripción */
M("NM", "AN II simple §3 · Transcripción", "En bacterias, ¿qué le indica a la ARN polimerasa dónde empezar?", [
  ["La subunidad σ (sigma), en el promotor", "En eucariotas lo hacen los factores de transcripción."],
  ["Un cebador de ARN que pone la primasa al inicio", "La ARN polimerasa no necesita cebador."],
  ["La proteína Rho", "Rho interviene en la terminación."],
  ["El codón AUG", "El AUG es el inicio de la traducción."]
]);
M("NM", "AN II simple §3 · Transcripción", "Una diferencia clave entre ARN polimerasa y ADN polimerasa:", [
  ["La de ARN no necesita cebador", "Puede empezar de cero."],
  ["La ARN polimerasa sintetiza en sentido 3′→5′, al revés", "Las dos sintetizan 5′→3′."],
  ["La ARN polimerasa no usa molde", "Usa la cadena molde."],
  ["La ARN polimerasa usa dNTP", "Usa NTP (ribonucleótidos)."]
]);
M("NM", "AN II simple §3 · Transcripción", "Si la cadena codificante es 5′-ATG GCT-3′, el ARN es:", [
  ["5′-AUG GCU-3′", "Igual a la codificante, con U en lugar de T."],
  ["5′-UAC CGA-3′", "Eso sería complementario a la codificante."],
  ["3′-TAC CGA-5′", "Esa es la cadena molde (ADN)."],
  ["5′-ATG GCT-3′", "El ARN no lleva T."]
]);
M("NM", "AN II simple §3 · Transcripción", "En la terminación independiente de Rho, ¿qué suelta a la polimerasa?", [
  ["Una horquilla en el ARN y varias U", "La horquilla la traba y el apareamiento U-A es débil."],
  ["La proteína Rho, que corre por el ARN hasta alcanzarla", "Eso es la terminación dependiente de Rho."],
  ["Un codón stop", "Los stop son de la traducción."],
  ["La subunidad σ", "σ interviene al principio."]
]);
M("NM", "AN II simple §3 · Transcripción", "¿Qué modificación del pre-ARNm eucariota ocurre en el extremo 5′?", [
  ["Un cap de 7-metilguanosina", "Protege al ARNm y sirve para que lo reconozca el ribosoma."],
  ["La cola de poli(A), que lo estabiliza", "Esa va en el extremo 3′."],
  ["Se cortan los exones", "Se cortan los intrones; los exones quedan."],
  ["Se agrega un cebador", "No hay cebadores en la transcripción."]
]);
M("NM", "AN II simple §3 · Transcripción", "Durante el splicing:", [
  ["Salen intrones; se unen exones", "Lo hace el espliceosoma, que tiene ARNsn."],
  ["Salen los exones y se unen los intrones entre sí", "Es al revés: los exones quedan."],
  ["Se agrega la cola de poli(A)", "Es otra modificación."],
  ["Se traduce el ARNm", "La traducción es posterior."]
]);
M("NM", "AN II simple §3 · Transcripción", "¿Cómo puede un solo gen dar varias proteínas distintas?", [
  ["Por splicing alternativo", "Se combinan distintos exones y salen isoformas."],
  ["Porque el código genético es ambiguo", "Cada codón da un solo aminoácido."],
  ["Porque se replica varias veces", "La replicación no cambia la proteína."],
  ["Por tener varios codones stop", "Un stop solo termina la traducción."]
]);

/* §4 Traducción */
M("NM", "AN II simple §4 · Traducción", "¿Qué hace la aminoacil-ARNt sintetasa?", [
  ["Carga cada ARNt con su aminoácido", "Usa ATP; hay una para cada aminoácido."],
  ["Forma el enlace peptídico entre aminoácidos", "Eso lo hace la peptidil transferasa (ARNr)."],
  ["Lee el codón stop", "Eso lo hace el factor de liberación."],
  ["Une las dos subunidades", "No es su función."]
]);
M("NM", "AN II simple §4 · Traducción", "¿A qué sitio del ribosoma entra el ARNt iniciador?", [
  ["Al sitio P", "Es el único que entra directo a P."],
  ["Al sitio A, como todos", "Por A entran todos los demás."],
  ["Al sitio E", "Por E salen los ARNt vacíos."],
  ["A ninguno", "Sí entra: al P."]
]);
M("NM", "AN II simple §4 · Traducción", "En el ciclo de elongación, ¿cuál es el orden correcto?", [
  ["Entra al A, enlace, translocación", "Después el ARNt vacío sale por E."],
  ["Translocación → entra al A → enlace peptídico", "Primero tiene que entrar el aminoacil-ARNt."],
  ["Enlace → entra al A → translocación", "Para formar el enlace hace falta el aminoácido en A."],
  ["Entra al E → enlace → sale por A", "Los sitios están al revés."]
]);
M("NM", "AN II simple §4 · Traducción", "¿Qué pasa cuando un codón stop llega al sitio A?", [
  ["Entra un factor de liberación", "No hay ningún ARNt con anticodón para un stop."],
  ["Entra un ARNt sin aminoácido y la cadena se corta", "No hay ARNt para los stop."],
  ["El ribosoma vuelve al AUG", "No, se separa."],
  ["Se agrega una Met final", "Met es el aminoácido del inicio."]
]);
M("NM", "AN II simple §4 · Traducción", "¿Cómo encuentra la subunidad menor el AUG de inicio?", [
  ["Por Shine-Dalgarno o por el cap", "En eucariotas se pega al cap y recorre hasta el primer AUG."],
  ["Busca el primer codón stop y retrocede hasta el AUG", "El stop marca el final."],
  ["Se pega al poli(A) en ambos casos", "Las bacterias no tienen poli(A) en sus ARNm."],
  ["Lo marca la subunidad σ", "σ es de la transcripción bacteriana."]
]);
M("NM", "AN II simple §4 · Traducción", "¿Cuál es el aminoácido iniciador en bacterias y en eucariotas?", [
  ["fMet en bacterias; Met en eucariotas", "Los dos los trae el ARNt iniciador para el AUG."],
  ["Met en bacterias; fMet en eucariotas", "Está al revés."],
  ["Trp en los dos", "Trp se codifica por UGG."],
  ["Depende de la proteína que se vaya a fabricar", "Siempre se arranca con el AUG."]
]);

/* §5 Nucleótidos */
M("NM", "AN II simple §5 · De novo y rescate", "¿Cuál es la diferencia entre la síntesis de novo y la recuperación?", [
  ["De novo: desde cero; rescate: recicla bases", "La recuperación reutiliza bases de la degradación."],
  ["De novo solo hace purinas y el rescate solo pirimidinas", "Las dos vías existen para ambas."],
  ["De novo: en el núcleo; recuperación: afuera", "No se distinguen por el lugar."],
  ["Son la misma vía con dos nombres", "Son vías distintas."]
]);
M("NM", "AN II simple §5 · De novo y rescate", "¿De dónde vienen las bases que usa la vía de recuperación?", [
  ["De degradar ácidos nucleicos", "Propios (intracelular) o de la dieta (digestión)."],
  ["Solo de la síntesis de novo", "Esas ya son nucleótidos nuevos."],
  ["Del ácido úrico", "El ácido úrico es un producto final, no se recicla."],
  ["Directamente del ciclo de Krebs, en la mitocondria", "Krebs no da bases."]
]);
M("NM", "AN II simple §5 · De novo y rescate", "¿Cuál es la ruta principal de importación de bases y nucleótidos?", [
  ["Digerir los ácidos nucleicos de la dieta", "La digestión de los ácidos nucleicos que comemos."],
  ["La síntesis de novo que ocurre en el hígado", "Eso es fabricar, no importar."],
  ["La degradación de proteínas", "Las proteínas no tienen bases."],
  ["La replicación del ADN", "La replicación los consume."]
]);
M("NM", "AN II simple §5 · De novo y rescate", "Si las bases no se reutilizan, ¿en qué terminan?", [
  ["Purinas: úrico; pirimidinas: β-ureidopropionato", "Son los productos finales de degradación."],
  ["Purinas: β-ureidopropionato; pirimidinas: ácido úrico", "Está al revés."],
  ["Las dos en ácido úrico", "El ácido úrico es solo de las purinas."],
  ["Las dos se acumulan sin cambios", "Se degradan."]
]);
M("NM", "AN II simple §5 · PRPP", "¿Qué aporta el PRPP (5-fosforribosil-1-pirofosfato)?", [
  ["La ribosa-fosfato de los nucleótidos", "Es el dador de ribosa, en novo y en recuperación."],
  ["La base nitrogenada ya armada para el nucleótido", "La base se arma aparte o se recicla."],
  ["El grupo metilo de la timina", "Ese lo da el metilen-THF."],
  ["La energía de la traducción", "La traducción usa ATP y GTP."]
]);
M("NM", "AN II simple §5 · Anillos", "¿Con qué se arma el anillo de purinas?", [
  ["Aminoácidos, THF y CO₂", "Glicina, glutamina y aspartato, más THF y CO₂."],
  ["Carbamoil fosfato y aspartato", "Eso arma el de pirimidinas."],
  ["Ácido úrico reciclado", "El ácido úrico no se recicla."],
  ["Solo glucosa", "La glucosa da la ribosa, no el anillo."]
]);
M("NM", "AN II simple §5 · Anillos", "¿Con qué se arma el anillo de pirimidinas, más simple?", [
  ["Carbamoil fosfato y aspartato", "Por eso es más sencillo que el de purinas."],
  ["Glicina, THF, CO₂ y glutamina juntas", "Eso arma el de purinas."],
  ["Hipoxantina y PRPP", "Eso es rescate de purinas."],
  ["Solo glutamina", "Hace falta más que eso."]
]);
M("NM", "AN II simple §5 · Estrategias", "En la síntesis de purinas, ¿cuándo aparece la ribosa-fosfato?", [
  ["Desde el principio: el anillo va encima", "El PRPP es la base sobre la que se construye."],
  ["Al final, cuando el anillo ya está completo", "Eso pasa en las pirimidinas."],
  ["Nunca: las purinas no tienen ribosa", "Los nucleótidos de purina sí la tienen."],
  ["Solo en la vía de recuperación", "También en la de novo."]
]);
M("NM", "AN II simple §5 · Estrategias", "En la síntesis de pirimidinas, el anillo:", [
  ["Se arma solo y después toma la ribosa", "Al revés que en las purinas."],
  ["Se arma encima del PRPP, átomo por átomo", "Eso es en purinas."],
  ["Viene armado de la dieta siempre", "También se fabrica de novo."],
  ["Se forma a partir del IMP", "El IMP es de purinas."]
]);
M("NM", "AN II simple §5 · Hipoxantina", "¿Qué es la hipoxantina?", [
  ["La base del IMP (inosinato)", "Del IMP salen AMP y GMP."],
  ["La base del UMP", "La del UMP es el uracilo."],
  ["El producto final de las purinas", "El producto final es el ácido úrico."],
  ["Una pirimidina modificada", "Es una purina."]
]);
M("NM", "AN II simple §5 · Hipoxantina", "En el rescate, la hipoxantina se combina con PRPP y da:", [
  ["IMP", "Por la enzima HGPRT: se recicla en vez de degradarse."],
  ["AMP directamente", "La adenina es la que da AMP (por la APRT)."],
  ["Ácido úrico", "Eso es degradarla, no rescatarla."],
  ["dTMP", "dTMP es de pirimidinas."]
]);
M("NM", "AN II simple §5 · Regulación", "¿Cómo se regula la síntesis de purinas?", [
  ["IMP, AMP y GMP frenan el 1.er paso", "Es retroinhibición: el producto frena su propia síntesis."],
  ["El ácido úrico activa el primer paso de la vía", "El ácido úrico no regula la síntesis."],
  ["El CTP frena el primer paso", "El CTP regula las pirimidinas."],
  ["No tiene regulación", "Está regulada por sus productos."]
]);
M("NM", "AN II simple §5 · Regulación", "Para hacer AMP se gasta GTP, y para hacer GMP se gasta ATP. ¿Para qué?", [
  ["Para equilibrar A y G", "Si sobra uno, se fabrica más del otro."],
  ["Porque el GTP es más barato que el ATP", "Cuestan lo mismo."],
  ["Para frenar la síntesis de pirimidinas", "No afecta a las pirimidinas."],
  ["Para producir ácido úrico", "No tiene que ver con la degradación."]
]);
M("NM", "AN II simple §5 · Desoxi y dTMP", "¿Qué hace la ribonucleótido reductasa?", [
  ["Pasa ribo a desoxirribonucleótidos", "Saca el OH del carbono 2′ de la ribosa."],
  ["Pasa el dUMP a dTMP poniéndole un metilo", "Eso lo hace la timidilato sintasa."],
  ["Degrada purinas a ácido úrico", "Eso lo hace la xantina oxidasa."],
  ["Forma el PRPP", "Eso lo hace la PRPP sintetasa."]
]);
M("NM", "AN II simple §5 · Desoxi y dTMP", "¿Para qué sirve la dUTPasa?", [
  ["Evita U en el ADN y da dUMP", "Hidroliza el dUTP a dUMP, el sustrato de la timina."],
  ["Pone el metilo de la timina", "Eso lo hace la timidilato sintasa."],
  ["Saca la U que ya quedó metida en el ADN", "Eso lo hace la uracilo-ADN glicosilasa."],
  ["Fabrica dUTP para el ADN", "Al revés: lo elimina."]
]);
M("NM", "AN II simple §5 · Desoxi y dTMP", "La timidilato sintasa:", [
  ["Metila el dUMP y da dTMP", "Le pone el CH₃ en el C5 (lo da el metilen-THF)."],
  ["Pasa ribosa a desoxirribosa", "Eso lo hace la ribonucleótido reductasa."],
  ["Hidroliza el dUTP", "Eso lo hace la dUTPasa."],
  ["Recicla la timina de la dieta", "Es síntesis, no rescate."]
]);
M("NM", "AN II simple §5 · Desoxi y dTMP", "¿Por qué el 5-fluorouracilo sirve contra el cáncer?", [
  ["Inhibe la timidilato sintasa", "Sin dTMP no se copia el ADN: frena células que se dividen mucho."],
  ["Inhibe la xantina oxidasa", "Eso lo hace el alopurinol."],
  ["Bloquea los ribosomas de las células tumorales", "No actúa en el ribosoma."],
  ["Aumenta la síntesis de purinas", "No: frena la síntesis de dTMP."]
]);
M("NM", "AN II simple §5 · T y U", "¿Qué le pasa a la citosina de forma espontánea en el ADN?", [
  ["Se desamina y queda uracilo", "Le pasa a miles de bases por día en cada célula."],
  ["Se metila en el C5 y queda timina", "La desaminación da uracilo, no timina."],
  ["Se oxida a ácido úrico", "El ácido úrico viene de purinas."],
  ["Se convierte en guanina", "No."]
]);
M("NM", "AN II simple §5 · T y U", "Si una citosina desaminada (ahora U) no se corrige, en la siguiente replicación:", [
  ["G-C pasa a A-T", "La U se aparea con A, y esa A después con T: mutación."],
  ["El par G-C se conserva igual", "La U se aparea con A, no con G."],
  ["Se corta la cadena", "No se corta: se copia mal."],
  ["Se pierde un par de bases", "Hay un cambio de base, no una pérdida."]
]);
M("NM", "AN II simple §5 · T y U", "¿Por qué el ADN usa timina en lugar de uracilo?", [
  ["Así toda U en el ADN es un error", "El metilo del C5 es la etiqueta de base original."],
  ["Porque la timina es más barata de fabricar", "Es más cara: necesita un paso extra."],
  ["Porque la timina se aparea con G", "La timina se aparea con A."],
  ["Porque el uracilo no se aparea con nada", "El uracilo se aparea con A."]
]);
M("NM", "AN II simple §5 · T y U", "¿Qué enzima saca el uracilo que aparece en el ADN?", [
  ["La uracilo-ADN glicosilasa", "Después la reparación por escisión de bases repone la C."],
  ["La dUTPasa, antes de que entre", "Actúa sobre el dUTP libre, no sobre el ADN."],
  ["La timidilato sintasa", "Fabrica dTMP."],
  ["La xantina oxidasa", "Degrada purinas."]
]);
M("NM", "AN II simple §5 · T y U", "¿Por qué el ARN puede usar uracilo sin problema?", [
  ["Dura poco y un error no se hereda", "Un error en un ARN no se hereda ni es grave."],
  ["Porque en el ARN la citosina no se desamina", "También se le desamina, pero no importa tanto."],
  ["Porque el ARN se replica", "El ARN celular no se replica."],
  ["Porque el uracilo es más estable", "No es esa la razón."]
]);
M("NM", "AN II simple §5 · Gota", "¿Qué causa los síntomas de la gota?", [
  ["Cristales de ácido úrico", "Es poco soluble: si se acumula, precipita y las inflama."],
  ["Falta de ácido úrico en la sangre y las articulaciones", "Es al revés: hay de más."],
  ["Acumulación de pirimidinas", "El ácido úrico viene de las purinas."],
  ["Exceso de timidilato sintasa", "No tiene relación."]
]);
M("NM", "AN II simple §5 · Gota", "¿Cómo actúa el alopurinol?", [
  ["Inhibe la xantina oxidasa", "Es análogo de la hipoxantina: se forma menos ácido úrico."],
  ["Inhibe la timidilato sintasa", "Eso es el 5-fluorouracilo."],
  ["Disuelve los cristales ya formados", "Actúa antes, evitando que se forme ácido úrico."],
  ["Activa la síntesis de purinas", "No."]
]);
M("NM", "AN II simple §5 · Gota", "Con alopurinol se acumulan hipoxantina y xantina. ¿Por qué no es un problema?", [
  ["Son más solubles que el ácido úrico", "Se eliminan sin formar cristales."],
  ["Porque se convierten en pirimidinas", "Las purinas no pasan a pirimidinas."],
  ["Porque no llegan al riñón", "Se eliminan por el riñón."],
  ["Porque se vuelven ácido úrico soluble", "Justamente no llegan a ácido úrico."]
]);
M("NM", "AN II simple §5 · Gota", "Si la enzima de rescate de purinas (HGPRT) no funciona:", [
  ["Sube el ácido úrico", "Al no reciclarse, terminan como ácido úrico: gota."],
  ["Baja el ácido úrico porque se degradan menos purinas", "Es al revés."],
  ["Se frena la síntesis de pirimidinas", "No afecta a las pirimidinas."],
  ["Se acumula dUTP en el ADN", "No tiene relación."]
]);
