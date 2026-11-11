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
