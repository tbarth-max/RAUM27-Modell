# RAUM27 – Urknall

> **Individuelles physikalisches Modell von Thomas – Diskussionsgrundlage.** Nicht begutachtet, kein Anspruch auf physikalische Gültigkeit. Kennungen: gemessen/geprüft · per Konstruktion · Abstraktion · Overlay.

Zwei Urknalle (Raum einmal, Information wiederholt), Nullpunkt als Inversion der Unendlichkeit, Hyperraum durch Spiegelung, Übertrag als neuer Nullpunkt, Kristall bei 180°. Ergänzt um den Stand vom 08.11.: c^c → N^N, simulierte Null/Unendlichkeit, 9⁹ und 27⁹, Weitergabe des Rests als zwei Keime.

## Nullpunkt als Inversion der Unendlichkeit, Würfel als Rückführung (02.11.)
Gedanke: Nullpunkt = Quelle/Senke (Rückschlagventil) gegenüber ∞ (Inversion 1/z); Zufluss entlang der unsichtbaren ±-Achse (Sichtlinie), sichtbar nur die Verteilung N/S/O/W. Die schwingende Kugel gibt Energie über die Flächenmitten ab; der Würfel lenkt sie über Achsen und Diagonalen zurück in den Schwingkreis, minimiert Verluste nach außen und stabilisiert das kugelsymmetrische, logarithmische Schalensystem um den verdichteten Nullpunkt (Radius 1).
Gibt es schon: Riemann-Kugel (0 ↔ ∞ über 1/z); Hohlraumresonator mit hoher Güte Q (supraleitende Kavitäten Q ~ 10¹⁰) – Wände reflektieren, Energie bleibt drin; Abstrahlungsverlust einer schwingenden Kugel; Gehäuse/Schirm. Prüfung: K44-E4 (Q gegen Wandreflexion R, Abfluss über Flächen/Kanten/Ecken).

## Kristall des schwarzen Lochs bei 180° (03.11.)
Gedanke: Bei 180°-Umkehr sieht man um den Horizont herum; bei perfekter Resonanz wird das Loch nach außen zum punktsymmetrischen Punkt X (Newton); die Struktur dazwischen als Kristall.
Gibt es schon: Retro-Lensing (180°), Photonenring mit Unterringen; Birkhoff-Satz (außen = Punktmasse); Schattenradius √27·GM/c².
Lokal nachgerechnet (Schwarzschild-Lichtbahnen, M = 1, scipy aus check/venv): Ablenkung n·180° bei Stoßparameter b = 5,356959 / 5,202680 / 5,196434 / 5,196165 (n = 1…4), nächster Abstand r0 = 3,521 / 3,090 / 3,018 / 3,004. Abstand zu √27: 1,61·10⁻¹ / 6,53·10⁻³ / 2,81·10⁻⁴ / 1,21·10⁻⁵; Verhältnis 0,0406 / 0,0431 / 0,0432 → e^(−π) = 0,0432.
Befund: Die Bilder um das Loch bilden ein logarithmisches Gitter (Kristall in log-Abstand) mit Gitterkonstante π je 180°-Umlauf, zentriert auf √27 (= √(3³)) und r = 3 (Photonensphäre). Gilt für nicht rotierendes Loch.

## Ring 1–9, Term ((6×8)^X)^N, Übertrag als neuer Nullpunkt (07.11.2026)
- Thomas: innen→außen 0–9 (X), außen→innen 10–1 (N = 9 − Ring, ebenfalls 0–9); erste Reaktion auf Auslöser 6×8; Strukturpaket ((6×8)^X)^N.
- Gerechnet: X=0 oder N=0 → 1 (je eine Eins ganz innen und ganz außen); X=N=3 → 48⁹ ≈ 10¹⁵; X=N=9 → 48⁸¹ ≈ 10¹³⁶ (81 = 9²). (a^X)^N = a^(X·N), kein Turm (Turm 48^(9⁹) ≈ 6,5·10⁸ Stellen). Korrektur Thomas: Rechenart, geklärt.
- 48 = |O_h| (Symmetrien Würfel/Oktaeder).
- Überlagerung äußere 9 + innere 9 → neuer Zustand 10 = neuer Nullpunkt: entspricht dem Übertrag im Stellenwertsystem (9+1 → „10“: Stelle wird 0, neue Stelle links). Basisunabhängig (2+1 → 10 in Basis 3, 1+1 → 10 in Basis 2) → Struktur, nicht Zählweise.
- Overlay: Kopplung Nachbar-Quadranten „c²“ (1–2, 1–3), Diagonal-Quadrant „c⁴“ (1–4) als Modellstufen, nicht als Geschwindigkeiten.
- Prüfbar: K49 Teil C (Felder 0→9 / 10→1), Treffen beider Fronten → neuer stabiler Zustand?

## Zwei Urknalle; Hyperraum durch Spiegelung; Orientierung +−/−+ (07.11.2026)
- Thomas: Raum-Urknall (einmal, Bühne) getrennt vom Informations-Urknall (wiederholt, Rückprojektion, neue Fraktalebenen). Hyperraum: Würfel in alle Nachbarrichtungen spiegeln (N, S, O, W und NO, SO, SW, NW), wieder zu einem Würfel verdichten; in 6 Ansichten zeigen, wo +− und −+ liegt; 8 Achtelkugeln mit je eigenem Koordinatenkreuz = 8 Würfel = eine Kugel; innen verdichtet, außen gefaltet; je 1/9 innen und außen frei (Deutung offen).
- Bekannt: ewige Inflation (wiederkehrende Blasen), konforme zyklische Kosmologie (Penrose: Ende wird umskaliert zum nächsten Anfang – unbestätigt); Spiegelladungsmethode (Spiegelbilder setzen Randbedingungen); Tesserakt hat 8 Würfelzellen, 24 Quadrate, 32 Kanten, 16 Ecken.
- Geprüft (Claude, `hyper/spiegel_und_zuendung.py` 250a8d0d…, Ergebnis f57fb13c…): Bild an Position v ∈ {−1,0,1}ⁿ entsteht aus k Spiegelungen, Orientierung (−1)^k.
  | Raum | Zellen | k = 0/1/2/3/4 | Orientierung gleich | umgekehrt |
  |---|---|---|---|---|
  | 2D | 9 | 1/4/4 | 5 (Mitte + 4 Diagonalen) | 4 (N, S, O, W) |
  | 3D | 27 | 1/6/12/8 | **13** (Mitte + 12 Kanten) | **14** (6 Flächen + 8 Ecken) |
  | 4D | 81 = 9² | 1/8/24/32/16 | 41 | 40 |
  ⇒ Die 6 Flächen und 8 Ecken sind genau die umgekehrt orientierten Bilder (−+); Mitte und 12 Kanten behalten die Orientierung (+−). Das ist die Paritätsteilung 13 + 14 aus Zustand 0. 4D-Zählung = Tesserakt (8 Würfelzellen bei k = 1).
- Informations-Urknall (Modell: feste Kapazität θ je Zelle, Zündung = Teilung in b³, Rückprojektion dünner Geschwister, Abfluss λ = 0,002): Bilanz exakt (Fehler ≤ 10⁻¹⁰). Mit Abfluss stellt sich ein fester Zustand ein (Zellzahl konstant); ohne Abfluss wächst sie weiter (Gegenprobe); θ zu groß ⇒ keine Zündung; θ klein bei b = 2 ⇒ Überlauf bis zur tiefsten Ebene. 3er-Teilung braucht weniger Zündungen als 2er (θ = 20: 11 gegen 33). Status: weitgehend per Konstruktion; nichttrivial nur der stationäre Zustand mit Abfluss (= „außen falten“ hält das Innen begrenzt).

## Hyper-RAUM27: Räume über die 6 + 8 Punkte verbinden und gegeneinander verschieben (07.11.2026)
- Thomas: nicht linear durch den Raum bewegen, sondern Räume über ihre 6 Flächen- und 8 Eckpunkte (Mittelpunkte) verbinden und 6 × 8 Räume gegeneinander verschieben; acht Hyperraum-Zustandsebenen; verbunden über Beobachter und Expansion auf dem Einheitskreis.
- Bekannt: Zwei um eine halbe Raumdiagonale verschobene Würfelgitter = raumzentriertes Gitter (bcc, z. B. Eisen); dessen Nachbarn sind genau 8 Ecken + 6 Flächen, Zelle = Oktaederstumpf (14 Flächen: 6 Quadrate, 8 Sechsecke), füllt den Raum lückenlos. Lattice-Boltzmann-Modell D3Q15 nutzt genau Ruhe + 6 + 8 mit Gewichten 2/9, 1/9, 1/72. 8 × 6 = 48 = Symmetriezahl des Würfels. 4D: Tesserakt hat 8 Würfelzellen; 4D-FCHC (24-Zelle) ist isotrop und liefert projiziert isotrope 3D-Gitter (d'Humières, Lallemand, Frisch 1986). Beobachter + Expansion: Monopol (Expansion) + Dipol (Eigenbewegung), wie Hintergrundstrahlung (Dipol ≈ 370 km/s).
- Geprüft (Claude, `hyper/sechs_acht_gitter.py` 7a1fd4c3…): 6 + 8 mit 1/9 : 1/72 ist **exakt isotrop 4. Ordnung** (M4 = 1/3 = 3·M22 = 3·1/9, c_s² = 1/3) – Neunerbrüche; nur 6 Nachbarn nicht isotrop (M22 = 0). Richtungsspreizung bei |k| = 1 (eigenes Maß): 6 + 8: 0,19 %; nur 6: 2,8 %; 26er 1 : ¼ : 1/16: 0,08 %. ⇒ 6 + 8 braucht 14 statt 26 Nachbarn bei ähnlicher Richtungsgleichheit.
- Offen: Doppler-Test (14 Fühler bewegt durch stehende Welle; Monopol/Dipol-Trennung auf der Einheitskugel); 8 Hyperraum-Ebenen konkret definieren (Tesserakt-Zellen oder 8 verschobene Kopien).

## Ergänzungen 08.11.

## G6 Urknall-These Thomas – Prüfstatus
- „e⁺e⁻ treffen sich nicht, 90° versetzt“ widerspricht der Messung (Grenze der Physik).
  - Ruhende e⁺e⁻ annihilieren in 2 × 511 keV-Photonen, die 180° auseinanderfliegen (PET).
  - Der Winkel bestimmt nur, wie viel Strahlenergie zusätzlich verfügbar ist.
- „mc² = kinetische Energie“: Physikalisch ist mc² die Ruhenergie.
  Kinetische Energie ist (γ−1)mc² und kommt dazu.
- c^c ist nicht definiert: Ein Exponent muss dimensionslos sein.
  - c in m/s: Ergebnis 10^2,5 Mrd.
  - c in km/s: Ergebnis 10^1,6 Mio.
  - c = 1: Ergebnis 1.
  - → Ersetzen durch eine dimensionslose Zahl N: Verdichtung N^−N, Auflösung N^N.
  - Kandidat aus dem Modell: N = 9 (9er-Fraktal). 9^9 = 387 420 489; 9^(9^9) hat 369 693 100 Stellen.
- Brauchbarer Kern: Das Verhältnis maximale Expansion / maximale Verdichtung ist eine reine Zahl der Form N^N.
  - Das ist prüfbar, sobald N aus der Geometrie folgt und nicht gesetzt wird.

## Z Keine echte Null/Unendlichkeit: simuliert über die Struktur; Umkehrfeld schließt die Bilanz
- Einzige Bedingung: eingeschwungen = nichts mehr messbar (J, K).
- Simulierte Null = kleinste Zelle 3^−K. Simulierte Unendlichkeit = 1/sin(3^−K) = 3^K. Produkt = 1 (Abweichung 4·10⁻¹⁰ bei K=9, sonst exakt). [M]
  - K = 9: 19 683
  - K = 18: 387 420 489 = 9^9 (18 Schritte ↔ 9^9, vgl. Treppe 18 und Verdichtung 9^9)
  - K = 27: 7,6·10¹²
- Verlust je Durchlauf 1 − cos 12,54° = 2,39 %.
  - Ohne Rückfeld nach 1000 Durchläufen 3·10⁻¹¹.
  - Mit Rückfeld (Verlust über 1/sin-Umkehr zurück): 1,0 exakt. [K: Rückgabe ist Regel]
- Normierung: Null und Unendlich sind keine Punkte im Raum, sondern die Grenzen der Verarbeitungstiefe K bei Geschwindigkeit c.

## AY Fläche vs. Raum über 9 Ebenen (gezählt)
- Fläche: 9 in 9, neunmal → 9⁹ = 387 420 489 = 3¹⁸. Gleiche Zahl wie die simulierte Unendlichkeit bei K = 18 (Z). [K]
- Raum: 27 in 27, neunmal → 27⁹ = 7 625 597 484 987 = 3²⁷. Gleiche Zahl wie die simulierte Unendlichkeit bei K = 27 (Z): „RAUM27“. [K]
- Bei 9 Ebenen im Raum:
  - Versorgungs-Zwerge 2/9 · 27⁹ = 6·27⁸ ≈ 1,7·10¹²
  - Organisationseinheiten 6⁹ = 10 077 696
  - 6^(9²) hätte 64 Stellen (Zustandszahl, Overlay).

## BL Vierfarben-Anzeige (Vorschlag Thomas, Regeln ausformuliert)
Messgröße je Knoten: Δ = Verzug − Vorhalt (Phase), Änderung je Takt dΔ.
- Grün: |Δ| < Schwelle und |dΔ| < Schwelle → eingeschwungen, gleicher Abstand.
- Rot: Δ nimmt ab (Kennung −) → Annäherung.
- Blau: Δ nimmt zu (Kennung +) → Flucht.
- Gelb: Rest in dieser Ebene nicht auflösbar (Courant > 1 oder Rest > Schwelle nach Einschwingzeit)
  → Übergabe über das 1/9-Tor nach außen (90°-Übertrag) oder nach innen (Inversion). Richt-Bit sagt, wohin.
- Hinweis: In der Physik (Doppler) ist es umgekehrt: Annäherung blau, Flucht rot. Für die Präsentation Konvention festlegen.
- BL2 Prüfung Gemini-Farbtext:
  - Richtig: Gelb = Rot + Grün (additiv), Komplement zu Blau; Farbtonkreis R 0° / Y 60° / G 120° / C 180° / B 240° / M 300°; Gegenfarben des Auges Rot–Grün und Blau–Gelb (Hering).
  - Ungenau: Höchste Helligkeitsempfindlichkeit liegt bei 555 nm (gelbgrün), nicht bei 575–580 nm. Spektrum 400–700 nm ist ein Verhältnis von 1,75, keine volle Oktave.
  - Widerspruch: Gemini setzt Rot = Expansion, Blau = Kontraktion. Bei Thomas (BL) ist Blau = Flucht, Rot = Annäherung. Muss einheitlich werden.
  - „6 Flächen ↔ 60°“ und „RGB = Weiß = Nullsumme“: Overlay.
- Empfehlung: 90°-Kreuz (passt zum 4-Takt 1234 und zum Übertrag):
  - Achse in der Ebene: Rot (Annäherung) ↔ Blau (Flucht), Kennung −/+.
  - Achse senkrecht dazu: Grün (bleibt in der Ebene, eingeschwungen) ↔ Gelb (verlässt die Ebene, 90°-Übertrag in die nächste Oktave).
  - Gelb ist damit genau der 90°-Sprung. Die Farbtheorie wird dafür nicht gebraucht (eigene Konvention).
- BL3 Festlegung Thomas (ersetzt BL/BL2):
  - Grün: in Phase, okay.
  - Blau: Phasenverschiebung, Richt-Bit sagt welche:
    - induktiv (Strom läuft nach, Verzug, Kennung +) = Entfernen
    - kapazitiv (Strom läuft vor, Kennung −) = Annähern
    - Elektrisch: Spule bis 90° nach, Kondensator bis 90° vor. Unser fester Verzug 12,54° ist induktiv.
  - Gelb: Rest, der weitergegeben wird. Entsteht erst, wenn 7/9 eines Blocks grün (stabil) sind.
    Dann geht der 2/9-Rest gelb über die 1/9-Tore nach außen/innen.
  - Rot: frei. Vorschlag: Abriss/Fehler (Courant > 1, Boden verletzt).
- BL4 Gelb genau (Thomas bestätigt):
  - Gelb = was nach dem Stabilisieren der Rotation als Schräglage gegenüber den perfekten 90° übrig bleibt.
    Das ist der Rest der 180°-Paarung (G14: Nutation ∝ 1/ω², bei Spin 40 ≈ 0,0009 von 0,17).
  - Weitergabe nach außen: Skala 1–10 (Übertrag bei 10, größere Ebene).
  - Weitergabe nach innen: Skala 0–9 (Nachkommastelle, feinere Ebene, über die Inversion).
  - Beide Skalen sind an der 1 gespiegelt.
- BL5 Der gelbe 2/9-Rest teilt sich in zwei einzelne Neuntel:
  - nach außen als 9/1
  - nach innen als 1/9
  9/1 · 1/9 = 1 → Spiegelpaar an der 1, die Bilanz bleibt geschlossen. Jedes Tor trägt genau ein Neuntel. [K]
- BL6 Aus der Dualität werden zwei Singularitäten (Thomas):
  - Das Paar 9/1 | 1/9 trennt sich in zwei einzelne Punkte.
  - Jeder wird zum neuen Zentrum (lokale Eins, ±0-Punkt aus N) seiner Ebene: außen der Keim der größeren, innen der Keim der feineren Ebene. Je ein neuer Ur-Zwerg.
  - Begriff: „Singularität“ hier = Einzelpunkt/Keim. Nicht im physikalischen Sinn unendlicher Dichte (nur 1/9 Menge, endlich).
