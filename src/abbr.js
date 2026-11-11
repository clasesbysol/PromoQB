/* Abreviaturas.
   [abreviatura, significado, grupo, nivel, núcleo]
   nivel 1 = métodos, reactivos y laboratorio: se explican cada vez que aparecen (una vez por párrafo, celda o pregunta).
   nivel 2 = moléculas y enzimas: se explican la primera vez en cada sección de la teoría y en cada pregunta.
   nivel 0 = solo en la pestaña Abreviaturas.
   núcleo: si el párrafo ya contiene ese texto, no se repite la explicación. */
const ABBR = [
  // ---- Separación y purificación ----
  ["TCA", "ácido tricloroacético", "Separación y purificación", 1, "tricloroac"],
  ["TFA", "ácido trifluoroacético", "Separación y purificación", 1, "trifluoroac"],
  ["PGC-SPE", "extracción en fase sólida con carbono grafitizado poroso", "Separación y purificación", 1],
  ["PGC", "carbono grafitizado poroso", "Separación y purificación", 1, "grafitizado poroso"],
  ["SPE", "extracción en fase sólida", "Separación y purificación", 1],
  ["HPSEC", "cromatografía de exclusión por tamaño de alta resolución", "Separación y purificación", 1],
  ["SEC", "cromatografía de exclusión por tamaño", "Separación y purificación", 1, "exclusión"],
  ["V₀", "volumen muerto", "Separación y purificación", 1],
  ["Vₜ", "volumen total", "Separación y purificación", 1],
  ["Vₑ", "volumen de elución", "Separación y purificación", 1],
  ["GU", "unidades de glucosa", "Separación y purificación", 1],
  ["TLC", "cromatografía en capa delgada", "Separación y purificación", 1, "capa delgada"],
  ["Rf", "factor de retención", "Separación y purificación", 1],
  ["FACE", "electroforesis de carbohidratos asistida por fluoróforos", "Separación y purificación", 1],
  ["HPLC-MS", "cromatografía líquida de alta resolución acoplada a espectrometría de masas", "Separación y purificación", 1],
  ["HPLC", "cromatografía líquida de alta resolución", "Separación y purificación", 1],
  ["MW", "masa molecular", "Separación y purificación", 1],
  ["PM", "peso molecular", "Separación y purificación", 1],
  ["UV", "ultravioleta", "Separación y purificación", 1],
  // ---- Composición y estructura ----
  ["HPAEC-PAD", "cromatografía de intercambio aniónico de alta resolución a pH alto, con detección amperométrica pulsada", "Composición y estructura", 1],
  ["HPAEC", "cromatografía de intercambio aniónico de alta resolución a pH alto", "Composición y estructura", 1],
  ["PAD", "detección amperométrica pulsada", "Composición y estructura", 1, "amperométric"],
  ["GC-MS", "cromatografía gaseosa acoplada a espectrometría de masas", "Composición y estructura", 1],
  ["GC", "cromatografía gaseosa", "Composición y estructura", 1, "cromatografía gaseosa"],
  ["EI-MS", "espectrometría de masas por impacto electrónico", "Composición y estructura", 1],
  ["ESI-MS", "espectrometría de masas con ionización por electrospray", "Composición y estructura", 1],
  ["MALDI-TOF", "espectrometría de masas por desorción e ionización láser asistida por matriz, con tiempo de vuelo", "Composición y estructura", 1],
  ["MS", "espectrometría de masas", "Composición y estructura", 1, "espectrometría de masas"],
  ["RMN", "resonancia magnética nuclear", "Composición y estructura", 1],
  ["PMAA", "acetatos de alditoles parcialmente metilados", "Composición y estructura", 1, "parcialmente metilados"],
  ["ENR", "extremos no reductores", "Composición y estructura", 1],
  ["PR", "puntos de ramificación", "Composición y estructura", 1],
  // ---- Reactivos y marcas ----
  ["CH₃I", "yoduro de metilo", "Reactivos y marcas", 1],
  ["NaBH₄", "borohidruro de sodio", "Reactivos y marcas", 1],
  ["NaBD₄", "borodeuteruro de sodio", "Reactivos y marcas", 1],
  ["ANTS", "ácido 8-aminonaftaleno-1,3,6-trisulfónico, marca fluorescente", "Reactivos y marcas", 1],
  ["2-AB", "2-aminobenzamida, marca fluorescente neutra", "Reactivos y marcas", 1],
  ["2-AA", "ácido 2-aminobenzoico, marca fluorescente con carga", "Reactivos y marcas", 1],
  ["C:M", "cloroformo:metanol", "Reactivos y marcas", 1],
  ["FST", "fase superior teórica", "Reactivos y marcas", 1],
  // ---- Enzimas y lectinas de laboratorio ----
  ["PNGasa F", "péptido-N-glicosidasa F", "Enzimas y lectinas", 1],
  ["Endo H", "endoglicosidasa H", "Enzimas y lectinas", 1],
  ["Con A", "concanavalina A", "Enzimas y lectinas", 1],
  ["LCA", "lectina de lenteja", "Enzimas y lectinas", 1, "lenteja"],
  ["PSA", "lectina de arveja", "Enzimas y lectinas", 1, "arveja"],
  ["RCA-I", "lectina de ricino", "Enzimas y lectinas", 1],
  ["SNA", "lectina de saúco", "Enzimas y lectinas", 1],
  ["MAL", "lectina de Maackia amurensis", "Enzimas y lectinas", 1],
  ["E₄-PHA", "fitohemaglutinina E₄ de poroto", "Enzimas y lectinas", 1],
  // ---- Glúcidos ----
  ["Glc", "glucosa", "Glúcidos", 0], ["Gal", "galactosa", "Glúcidos", 0], ["Man", "manosa", "Glúcidos", 0], ["Fru", "fructosa", "Glúcidos", 0],
  ["GlcNAc", "N-acetilglucosamina", "Glúcidos", 2],
  ["GalNAc", "N-acetilgalactosamina", "Glúcidos", 2],
  ["MurNAc", "ácido N-acetilmurámico", "Glúcidos", 2],
  ["GlcA", "ácido glucurónico", "Glúcidos", 2],
  ["IdoA", "ácido idurónico", "Glúcidos", 2],
  ["GlcNS6S", "glucosamina N-sulfatada y 6-sulfatada", "Glúcidos", 2],
  ["Neu5Ac", "ácido N-acetilneuramínico (ácido siálico)", "Glúcidos", 2],
  ["NANA", "ácido N-acetilneuramínico (ácido siálico)", "Glúcidos", 2],
  ["GAG", "glicosaminoglicano", "Glúcidos", 2],
  ["HbA1c", "hemoglobina glicada", "Glúcidos", 2],
  ["AGE", "productos finales de glicación avanzada", "Glúcidos", 2],
  ["LPS", "lipopolisacárido", "Glúcidos", 2],
  ["UDP", "uridina difosfato", "Glúcidos", 0],
  ["CMP", "citidina monofosfato", "Glúcidos", 0],
  ["G6P", "glucosa-6-fosfato", "Glúcidos", 2],
  ["G3P", "gliceraldehído-3-fosfato", "Glúcidos", 2],
  ["DHAP", "dihidroxiacetona fosfato", "Glúcidos", 2],
  ["PEP", "fosfoenolpiruvato", "Glúcidos", 2, "fosfoenolpiruvato"],
  ["PFK-1", "fosfofructoquinasa 1", "Glúcidos", 2],
  ["PKA", "proteína quinasa A", "Glúcidos", 2],
  ["PP1", "proteína fosfatasa 1", "Glúcidos", 2],
  ["AMPc", "AMP cíclico", "Glúcidos", 2],
  ["GMPc", "GMP cíclico", "Glúcidos", 2],
  ["TPP", "tiamina pirofosfato (vitamina B1)", "Glúcidos", 2],
  // ---- Lípidos ----
  ["AG", "ácidos grasos", "Lípidos", 2, "ácidos grasos"],
  ["TAG", "triacilglicéridos", "Lípidos", 2, "triacilglic"],
  ["DAG", "diacilglicerol", "Lípidos", 2],
  ["PUFA", "ácidos grasos poliinsaturados", "Lípidos", 2, "poliinsaturado"],
  ["EPA", "ácido eicosapentaenoico (20:5 ω-3)", "Lípidos", 2],
  ["DHA", "ácido docosahexaenoico (22:6 ω-3)", "Lípidos", 2],
  ["PA", "ácido fosfatídico", "Lípidos", 2, "fosfatídico"],
  ["PC", "fosfatidilcolina", "Lípidos", 2, "fosfatidilcolina"],
  ["PE", "fosfatidiletanolamina", "Lípidos", 2, "fosfatidiletanolamina"],
  ["PS", "fosfatidilserina", "Lípidos", 2, "fosfatidilserina"],
  ["PG", "fosfatidilglicerol", "Lípidos", 2, "fosfatidilglicerol"],
  ["PI", "fosfatidilinositol", "Lípidos", 2, "fosfatidilinositol"],
  ["PIP₂", "fosfatidilinositol bisfosfato", "Lípidos", 2],
  ["MGDG", "monogalactosildiacilglicerol", "Lípidos", 2],
  ["DGDG", "digalactosildiacilglicerol", "Lípidos", 2],
  ["SQDG", "sulfoquinovosildiacilglicerol", "Lípidos", 2],
  ["PLA₂", "fosfolipasa A₂", "Lípidos", 2, "fosfolipasa"],
  ["GPI", "glicosilfosfatidilinositol", "Lípidos", 2],
  ["LNP", "nanopartículas lipídicas", "Lípidos", 2],
  ["CDP", "citidina difosfato", "Lípidos", 2],
  ["GPAT", "glicerol-3-fosfato aciltransferasa", "Lípidos", 2],
  ["LPAAT", "ácido lisofosfatídico aciltransferasa", "Lípidos", 2],
  ["LPCAT", "lisofosfatidilcolina aciltransferasa", "Lípidos", 2],
  ["LPIAT", "lisofosfatidilinositol aciltransferasa", "Lípidos", 2],
  ["SREBP", "proteína que se une al elemento regulador de esteroles", "Lípidos", 2],
  ["Tc", "temperatura de transición de fase", "Lípidos", 2],
  ["VLDL", "lipoproteína de muy baja densidad", "Lípidos", 2],
  ["IDL", "lipoproteína de densidad intermedia", "Lípidos", 2],
  ["LDL", "lipoproteína de baja densidad", "Lípidos", 2],
  ["HDL", "lipoproteína de alta densidad", "Lípidos", 2],
  ["LPL", "lipoproteína lipasa", "Lípidos", 2, "lipoproteína lipasa"],
  ["LCAT", "lecitina-colesterol aciltransferasa", "Lípidos", 2],
  ["HSL", "lipasa sensible a hormonas", "Lípidos", 2],
  ["ATGL", "lipasa de triglicéridos del tejido adiposo", "Lípidos", 2],
  ["CPT-I", "carnitina palmitoiltransferasa I", "Lípidos", 2],
  ["CPT-II", "carnitina palmitoiltransferasa II", "Lípidos", 2],
  ["ACC", "acetil-CoA carboxilasa", "Lípidos", 2, "acetil-coa carboxilasa"],
  ["FAS", "ácido graso sintasa", "Lípidos", 2, "ácido graso sintasa"],
  ["ACP", "proteína transportadora de acilos", "Lípidos", 2],
  ["AMPK", "quinasa activada por AMP", "Lípidos", 2],
  ["HMG-CoA", "3-hidroxi-3-metilglutaril-CoA", "Lípidos", 2],
  // ---- Ácidos nucleicos ----
  ["pb", "pares de bases", "Ácidos nucleicos", 2],
  ["Tm", "temperatura de fusión", "Ácidos nucleicos", 2, "temperatura de fusión"],
  ["A₂₆₀", "absorbancia a 260 nm", "Ácidos nucleicos", 2],
  ["ARNm", "ARN mensajero", "Ácidos nucleicos", 0], ["ARNt", "ARN de transferencia", "Ácidos nucleicos", 0], ["ARNr", "ARN ribosomal", "Ácidos nucleicos", 0],
  ["ARNnp", "ARN nuclear pequeño", "Ácidos nucleicos", 2], ["snRNA", "ARN nuclear pequeño", "Ácidos nucleicos", 2],
  ["SSB", "proteínas de unión a ADN de cadena simple", "Ácidos nucleicos", 2],
  ["UTR", "región no traducida del ARNm", "Ácidos nucleicos", 2],
  ["ORF", "marco abierto de lectura", "Ácidos nucleicos", 2],
  ["NTP", "nucleósido trifosfato", "Ácidos nucleicos", 2], ["NDP", "nucleósido difosfato", "Ácidos nucleicos", 2],
  ["PRPP", "5-fosforribosil-1-pirofosfato", "Ácidos nucleicos", 2],
  ["ARNsn", "ARN nuclear pequeño", "Ácidos nucleicos", 2],
  ["dNTP", "desoxirribonucleósido trifosfato", "Ácidos nucleicos", 2], ["dNDP", "desoxirribonucleósido difosfato", "Ácidos nucleicos", 2],
  ["dUTPasa", "desoxiuridina trifosfatasa", "Ácidos nucleicos", 2],
  ["dUTP", "desoxiuridina trifosfato", "Ácidos nucleicos", 2], ["dUDP", "desoxiuridina difosfato", "Ácidos nucleicos", 2],
  ["dUMP", "desoxiuridina monofosfato", "Ácidos nucleicos", 2], ["dTMP", "desoxitimidina monofosfato (timidilato)", "Ácidos nucleicos", 2],
  ["GTP", "guanosín trifosfato", "Ácidos nucleicos", 2], ["GMP", "guanosín monofosfato", "Ácidos nucleicos", 2],
  ["UMP", "uridín monofosfato", "Ácidos nucleicos", 2], ["CTP", "citidín trifosfato", "Ácidos nucleicos", 2],
  ["IMP", "inosina monofosfato (inosinato)", "Ácidos nucleicos", 2, "inosina"],
  ["XMP", "xantosina monofosfato", "Ácidos nucleicos", 2],
  ["OMP", "orotidina monofosfato (orotidilato)", "Ácidos nucleicos", 2, "orotidi"],
  ["ATCasa", "aspartato transcarbamilasa", "Ácidos nucleicos", 2, "transcarbamilasa"],
  ["THF", "tetrahidrofolato", "Ácidos nucleicos", 2],
  ["DHF", "dihidrofolato", "Ácidos nucleicos", 2],
  ["DHFR", "dihidrofolato reductasa", "Ácidos nucleicos", 2],
  ["FdUMP", "fluorodesoxiuridina monofosfato", "Ácidos nucleicos", 2],
  ["HGPRT", "hipoxantina-guanina fosforribosiltransferasa", "Ácidos nucleicos", 2],
  ["APRT", "adenina fosforribosiltransferasa", "Ácidos nucleicos", 2],
  ["SAM", "S-adenosilmetionina", "Ácidos nucleicos", 2],
  ["PABA", "ácido para-aminobenzoico", "Ácidos nucleicos", 2],
  ["FAD", "flavín adenín dinucleótido", "Ácidos nucleicos", 0], ["FMN", "flavín mononucleótido", "Ácidos nucleicos", 0],
  ["NAD", "nicotinamida adenín dinucleótido", "Ácidos nucleicos", 0], ["NADP", "nicotinamida adenín dinucleótido fosfato", "Ácidos nucleicos", 0],
  ["CoA", "coenzima A", "Ácidos nucleicos", 0],
  ["ATP", "adenosín trifosfato", "Ácidos nucleicos", 0], ["AMP", "adenosín monofosfato", "Ácidos nucleicos", 0]
];

/* ---------- expansión ---------- */
const ABBR_MAP = {};
ABBR.forEach(a => { ABBR_MAP[a[0]] = { x: a[1], lvl: a[3], core: (a[4] || a[1]).toLowerCase() } });
const ABBR_KEYS = ABBR.filter(a => a[3] > 0).map(a => a[0]).sort((a, b) => b.length - a.length);
const reEsc = s => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
// no se expande si va pegada a una fórmula: α, β, paréntesis, dígitos, /, ), barra o sufijos tipo -6S
const ABBR_RE = new RegExp("(?<![\\wÀ-ÿ₀-₉-])(" + ABBR_KEYS.map(reEsc).join("|") + ")(?![\\wÀ-ÿ₀-₉αβ(–-])", "g");
/* str: texto ya escapado. s1: abreviaturas de nivel 1 ya explicadas en este bloque; s2: de nivel 2 en esta sección o pregunta. ctx: texto del bloque en minúsculas */
function abbrExpand(str, s1, s2, ctx) {
  return str.replace(ABBR_RE, (m, k, off, full) => {
    const a = ABBR_MAP[k]; if (!a) return m;
    const nx = full[off + m.length] || "", pv = full[off - 1] || "";
    if (k[0] === "V" && /[\/)]/.test(nx)) return m;
    if (nx === ":" && k === "C:M") return m;
    const seen = a.lvl === 1 ? s1 : s2;
    if (seen.has(k)) return m;
    seen.add(k);
    if (ctx && ctx.includes(a.core)) return m;
    if (pv === "(" && nx === ")") return m + ': <span class="xp">' + a.x + "</span>";
    return m + ' <span class="xp">(' + a.x + ")</span>";
  });
}
