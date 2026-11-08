# RAUM27 – Feldtheorie

> **Individuelles physikalisches Modell von Thomas – Diskussionsgrundlage.** Nicht begutachtet, kein Anspruch auf physikalische Gültigkeit. Kennungen: gemessen/geprüft · per Konstruktion · Abstraktion · Overlay.

Die Gitter-Feldtheorie: Kugel–Würfel–Kugel, Raum aus Feldern, formale Fassung v0.1, Schalenbild, Isotropie 2D→3D→4D, Gesamtsimulation Raum/Feld/Materie und Informationsebene. Am Ende der Stand vom 08.11.: Quadrantenoperator und die vier Sinusfunktionen.

## Kristallbrücke: von der Abstraktion zur echten Physik (02.11.)

**Gedanke (Thomas):** Wir bauen Kristallstrukturen, die immer mehr Energie über den Nullpunkt synchronisieren. Energie, die homogen von allen Seiten kommt, sammelt sich im Zentrum; die Gitterschwingung kann nur im Gitter schwingen. Saubere Kristalle (homogen verteilte Fremdatome als Kerne) sind symmetrisch um den Kristallisationspunkt; die Fremdatome prägen über Feldlinien die Farbe (RGB: Rubin, Smaragd, blau?).

**Geprüft (lokal, exakt mit Brüchen):**
- Würfel → Oktaeder (Flächenmitten) → Würfel (Mitten der Oktaederdreiecke): Ecke je Runde exakt ÷ 3 (Dreiecksmitte (1/3,1/3,1/3)); je Halbschritt 8→6 bzw. 6→8 Faktor exakt √3. Schalen 1, 1/3, 1/9, 1/27 … Alle Stufen haben dieselben 48 Symmetrien. (Skript k42check/dual.py)
- 16/9 ≈ √3 (Halbschritt), 13/9 ≈ √2.

**Echte Physik dazu (Gibt es schon):**
- 6 um 1 = NaCl (Oktaeder), 8 um 1 = CsCl (Würfel). Auswahl nach Pauling-Radienquotient: 0,414 = √2−1 … 0,732 = √3−1 → 6er; > 0,732 → 8er.
- Diamant: elektrisch Isolator, aber bester natürlicher Wärmeleiter (~2000 W/mK) – Energie läuft als Gitterschwingung (Phononen) sehr gut durch. Licht: Brechzahl 2,42, Totalreflexion hält Licht im Stein (Brillanz durch Schliff).
- Farbe durch Fremdatome = Kristallfeld (Ligandenfeld): das Gitterfeld spaltet die Energieniveaus des Fremdions. Gleiches Cr³⁺: rot in Korund (Rubin), grün in Beryll (Smaragd) – nur das Feld ist anders.
- Blau: Saphir = Korund + Fe²⁺/Ti⁴⁺ (Ladungstransfer); blauer Diamant = Bor.
- Stärkste Brücke: Rubinlaser (Maiman 1960): Blitzlampe pumpt Licht von allen Seiten in den Rubinstab, Energie wird in Cr³⁺ gespeichert und kohärent (synchron) abgegeben.

**Korrekturen:**
- Rubin/Smaragd/Saphir sind keine Kohlenstoffgitter (Al₂O₃ bzw. Be₃Al₂Si₆O₁₈); Kohlenstoff = Diamant.
- Richtung: das Gitterfeld verändert das Fremdatom (Farbe), nicht umgekehrt.
- Transparenter Kristall lädt sich durch Licht kaum auf; Energieaufnahme nur, wo absorbiert wird (Farbzentren, Fremdionen).
- Historisch: Kepler 1596 (geschachtelte platonische Körper für Planeten) – physikalisch falsch; bei Kristallen ist Verschachtelung real.

**Prüfbar (Kandidat K43):** Radienquotient-Grenzen √2−1, √3−1 aus Kugelpackung herleiten; Phononen im 27³-Gitter (Dispersion, Wärmeleitung); Kristallfeld-Aufspaltung für Cr³⁺ bei zwei Feldstärken → Farbe; einfaches Lasermodell (3 Niveaus, Pumpen von allen Seiten, Schwelle).

## Bauprinzip Kugel–Würfel–Kugel (02.11.)

**Gedanke (Thomas):** Kugelhaus, gehalten von einer Würfelgitterstruktur, umgeben von einer Kugel. Außen klettert ein Roboter auf der eigenen Hülle und druckt/legt sie (kein Mensch in der Höhe); innen wird von unten nach oben ausgebaut, Fallhöhe max. ein Stockwerk; Einrichtung gedämpft befestigt. Bauteile aus kristallinem/verstrecktem Kunststoff bzw. Carbon in Diamant-/Oktettgeometrie, als Vision für Großprojekte.

**Aufbau:** Außenkugel = Bilanzhülle (Lasten umleiten, keine Ecken) · Würfelgitter = Tragwerk und gerade Ebenen · Innenkugel = gedämpft aufgehängter Kern. Radien 1 : √2 : √3 (≈ 9/9 : 13/9 : 16/9).

**Gibt es schon:** Kugelbauten (Kugelhaus Dresden 1928, Biosphère Montréal 1967, Eden Project, Sphere Las Vegas 2023); Pendeldämpfer Taipei 101; kardanische Aufhängung; Röhren-/Diagrid-Bauweise; Carbonbeton (CUBE Dresden 2022); robotisches Faserwickeln (BUGA-Faserpavillon Heilbronn 2019, Uni Stuttgart); Kletterroboter (Minibuilders, IAAC 2014); 3D-gedrucktes Haus Beckum 2021; Baufabriken Shimizu/Obayashi (1990er); Vorspannung (Spannbeton, Tensegrity); Strukturhierarchie (Eiffelturm, Perlmutt, Lakes 1993).

**Grenzen:** Gigapascal-Druck nicht vor Ort; Ordnung über Faserausrichtung. Brandschutz, Kriechen/Alterung, Zulassung, Verbindungsstellen, Transport (≈ 3 × 4 m Querschnitt).

### Merkzettel K43 (Kandidaten, noch NICHT im Auftrag)
1. Kugel–Würfel–Kugel unter Erdbebensignal: Innenkugel starr gegen gedämpft; Vergleich reine Würfelhülle (Eckspannungen).
2. Gittervergleich gleiches Material: Würfel / Diamant / Oktett / hierarchisch (1–3 Ebenen): Steifigkeit, Bruchlast, Stoßenergie; spröde Knoten + zähe Verbindung (Perlmutt-Prinzip).
3. Vorspannung: Oktettgitter mit/ohne Vorspannung, Last bis erster Stab auf Zug.
4. Faserausrichtung: Stab mit Fasern entlang der Kraft gegen zufällig.
5. Kugelschale gegen Würfelschale unter Außendruck: Spannungsverteilung, Ankunft innen.
6. Gestapelt (Fugen) gegen lückenlos gefüllt, mit/ohne Pufferschale 9.
7. Würfel→Oktaeder→Würfel (÷3 je Runde, √3 je Halbschritt) – bereits lokal bestätigt; Pauling-Grenzen √2−1, √3−1 aus Kugelpackung.
8. Kristallwachstum vom Zentrum mit Einbaufaktor k < 1 (Zonenschmelzen) gegen k = 1.
9. Physik-Brücke: Paul-Falle (Stabilitätskarte), Laserkühlung, π-Puls; Tunneln (imaginärer Impuls); SU(2) 360°/720°; Wick-Rotation; Multipole (Monopol/Dipol, Gauß-Fluss); Gittermodell: Lagrange-Funktion, Kontinuumsgrenze (Welle, Diffusion, Klein-Gordon), Noether für 48 Symmetrien.
10. Phononen im 27³-Gitter; Kristallfeld Cr³⁺ bei zwei Feldstärken; 3-Niveau-Lasermodell.

### Auswertung K42 (02.11.)
- 23/23 Ziele ausgeführt, alle mit Skript + Log auf Drive. Beleg 36 neu gehasht = gemeldet; Kopf 89ce6fbc3d4b0877… (37 Belege).
- Alle Erwartungswerte getroffen; D1–D3 decken sich mit meinen unabhängigen lokalen Läufen (r 0,9359; 16,05 %/79,01 %; Hysterese 1,126 vs. meine 1,130 – andere Flächenformel). F1/F3/E2 von Hand nachgerechnet: stimmt.
- Echte Erkenntnis A1: 48er-Filter versagt bei schwacher Störung (0,10 = 5σ, unter Schwelle 0,11): 31–54 % Durchlass; bei globaler Störung (auch Ecksensoren) 6–60 % Durchlass. → Filter ist nicht allgemein, sondern auf ±x-Gegenstörung ≥ 0,25 zugeschnitten.
- D4: „sicher richtig“ (kein Kanal näher als 1σ an Schwelle) bei σ=0,0185 nur 65,9 %.

## Erste Simulation der Feldtheorie-Grundannahme (02.11., lokal, feld/feldtheorie.py)
Modell: reelles Feld f auf 27³ (periodisch), f̈ = ∇²f − (f³ − f) + J; Potential ¼(f²−1)² (Nullpunkt instabil/tachyonisch, stabil bei ±1 = voll); Punktquelle X1 im Zentrum; 8 Paritätsklassen über 3 Spiegelebenen.
1. Energie ohne Dämpfung: Drift 3,1 % über 2000 Schritte (einfaches Verfahren; für K43 genaueres Verfahren).
2. Masse um +1: gemessen 1,424, Theorie √2 = 1,414 (0,7 %).
3. Start am Nullpunkt + Rauschen 0,01: nach t = 20 sind 62 % voll, ab t = 50 99,9 % voll – ganzes Gitter kippt gemeinsam auf +1 (eine Domäne).
4. Punktmasse X1: stört nur 2–3 Zellen (Abfall wie Yukawa, Reichweite ≈ 1/m ≈ 0,7); Feld zu 100 % in Paritätsklasse „1“ (voll symmetrisch). Doppelte Quelle kippt nur das Zentrum (+0,25), Rest bleibt −1.
Deutung: Nullpunkt-Instabilität erzeugt Masse (√2) und Reichweite (Yukawa) – Anschluss an Higgs-/Klein-Gordon-Physik bestätigt (bekannt, nicht neu). Zentrumsmasse erzeugt nur das symmetrische Spiegelbild.

## Raum aus Feldern, Strömungsbild, komplexe Spiegelmathematik (02.11.)
**Gedanke (Thomas):** Massen bewegen sich nicht durch den Raum, sie erzeugen ihn durch Überlagerung ihrer Felder; es gibt eine Höchstzahl von Resonanzpunkten. Bild: Würfel voll „Raum-Wasser“, jede Masse ein Zulauf, Abfluss an den Ecken, Rückführung zu den Massenpunkten; wo Expansions- und Druckwellen sich treffen (Rückprojektion), entsteht der Gravitationsvektor. Bleibt man im komplexen Zahlenraum (Spiegelmathematik der Projektion), passt es exakt.
**Gibt es schon:** Leibniz/Mach (Raum als Beziehung), Einstein (Masse formt Geometrie); Raum aus Verschränkung (Van Raamsdonk 2010, ER=EPR 2013 – offen); Weyl-Gesetz (endliche Moden), Bekenstein-Grenze; Bjerknes-Kräfte (pulsierende Kugeln im Wasser: gleichphasig Anziehung ∝ 1/r², gegenphasig Abstoßung); Fluss-Modell der ART (Gullstrand-Painlevé, Hamilton & Lisle 2008: Raum fließt in die Masse hinein); analoge Gravitation im Wasserbecken (Weinfurtner 2011). Widerlegt: Le-Sage-Druckgravitation.
**Komplexe Fassung (exakt in 2D):** Quelle w = (Q/2π)·ln z; Wand = Spiegelquelle (z̄); Kreis = Inversion 1/z̄; Kasten = Gitter aus Spiegelbildern; Kraft über Satz von Blasius. In 3D nicht so einfach.
**Ebenen:** belegt = Masse formt Geometrie, endliche Moden; Abstraktion/offen = Raum entsteht aus Feldern; prüfbar = Gitter aus Korrelationen zurückgewinnen, Bjerknes/Quellen im Kasten.
**Weitere heute geklärte Punkte:** 6 = Transport (sieht 1,x,y,z), 8 = Information (alle 8 inkl. XOR) – 6er-System kann kein XOR (Perzeptron, Minsky/Papert 1969); 90° um x · 90° um y = 120° um Raumdiagonale; Wythoff-Konstruktion (alles aus einem Y durch Spiegeln); 3 Spiegel → 8 Bilder (Spiegelladung) = 8 Paritätsklassen = K42-B1-Moden; Proton fest / Elektron beweglich (Born-Oppenheimer), Virialsatz T = −½V, s-Elektron am Kern; Kern ≠ schwarzes Loch; Higgs-Feld am Nullpunkt tachyonisch → Masse; Tachyonen nie beobachtet; Kettenleiter → φ; Ladeverlust 50 % bei fester Spannung; Superkondensator, Elektride, Photonen-/Polaritonspeicher.

## RAUM27-Gitter-Feldtheorie – formale Fassung v0.1 (02.11.)
1. Raum: Λ = {x = a·n, n ∈ ℤ³_N} (periodisch), Gitterabstand a, N = 27 (= 3³). Nachbarn: 6 Achsen (Transport), 8 Diagonalen (Information).
2. Feld: f: Λ × ℝ → ℝ, Wertebereich normiert: f = +1 voll, f = −1 leer, f = 0 instabiler Nullpunkt.
3. Wirkung: S = Σ_t Σ_x a³ [ ½ ḟ² − ½ Σ_{μ=1..3} ((f(x+aê_μ) − f(x))/a)² − V(f) + J·f ]
   V(f) = (λ/4)(f² − v²)², v = 1 (Mexikanerhut; V''(0) = −λ < 0 tachyonisch, V''(±1) = 2λ).
4. Bewegungsgleichung: f̈ = Δ_a f − λ f (f² − 1) + J − γ ḟ,  Δ_a f(x) = Σ_μ [f(x+aê_μ) + f(x−aê_μ) − 2f(x)]/a².
5. Energie (Noether, Zeitinvarianz, γ = 0): H = Σ_x a³ [ ½ ḟ² + ½ (∇_a f)² + V(f) − J f ] = konst.
6. Masse: kleine Schwingung um +1: m² = 2λ → m = √2 (λ = 1). Gemessen 1,424 (Vortest).
7. Punktmasse X1: J = q·δ_{x,0}. Linear um −1: (−Δ_a + m²) δf = J → δf(r) ≈ q e^{−m r}/(4π r) (Yukawa).
   Zwei Massen: E_int(d) ≈ − q₁q₂ e^{−m d}/(4π d) (gleiche Vorzeichen ziehen an) – Prüfung K43-A5.
8. Symmetrie: O_h (48 = 24 Drehungen + 24 Spiegelungen) wirkt auf Λ; bei J = 0 ist S invariant.
   Spiegel P_x, P_y, P_z (ℤ₂³) → 8 Paritätsklassen χ_s(f) = Projektion mit Vorzeichen s ∈ {±1}³ = Walsh-Moden {1,x,y,z,xy,xz,yz,xyz}.
   Flächenoperator F (6×8) hat Rang 4: sieht {1,x,y,z}; Eckenoperator sieht alle 8 (XOR = Produkt der Vorzeichen).
9. Null-Operator: N_δ(s) = Ja (s > δ), Nein (s < −δ), unsicher (|s| ≤ δ), δ = 3σ.
10. Sättigungs-/Spannungsform (dissipativ): E_{n+1} = tanh(g·H_a E_n + A·(G − ½)), H_a E = 0,4E + 0,15 Σ_Nachbarn; Stufen analog/klar/binär.
11. Schalen: r_k = 9/k, Potential einer Punktquelle 1/r → V(r_k) = k/9 (gleichabständig).
12. Kontinuumsgrenze a → 0: (∂_t² − ∇² + m²)δf = J (Klein-Gordon) bzw. φ⁴-Theorie – bekannte Physik.
**Status:** 1–6, 8–12 Modell bzw. bekannte Mathematik; 7 Vorhersage (K43-A5 prüft); neu ist nur die Zuordnung (6/8-Trennung, Null-Operator, Schalen 9/k, voll=1) – keine neue Physik behauptet.
**Offen:** Gravitation (bisher nur Yukawa, kurzreichweitig; für 1/r bräuchte es m → 0), Raum aus Korrelationen (K43-C), gegenläufige Wellen 6/8 (K43-G1).

### Einordnung Sprach-Zusammenfassung (02.11., anderer Chat)
- Passt: geschlossenes System mit fester Teilchenzahl (N³ Knoten, nur Energie ändert sich); RGB + Hex (4 Ecken = 1 Hexziffer); Tiefe = Zeit/Spiegeldicke statt 4. Raumachse (wie t nur als Einschwingen); Bereich 0…∞ (t = x/(1+x)); Masse/Energie/Simulation ≈ physisch/Abstraktion/Overlay.
- Korrektur r = 1 = Planck-Länge: zulässige Eichung (a = ℓ_P), aber Folge: m = √2 in Gittereinheiten ≈ 1,4 Planck-Massen (~3·10⁻⁸ kg), Yukawa-Reichweite ≈ ℓ_P → im Experiment unsichtbar. Planck-Gitter verletzt Lorentz-Invarianz bei höchsten Energien; Gamma-Blitz-Messungen (Fermi, GRB 090510) begrenzen das bereits. Eichung erst nach K43 festlegen.
- Korrektur Kurzschluss/Leerlauf: Symmetrie hebt den ohmschen Widerstand nicht auf. Richtig ist: Zwischen Punkten gleichen Potentials (abgeglichene Brücke, Wheatstone) fließt beim Kurzschließen kein Strom – deshalb harmlos. Widerstandsfreiheit gibt es nur bei Supraleitung.

### Auswertung K43 (02.11.)
- 48/48 Ziele ausgeführt, Skripte + Logs; Rechenzeit gesamt nur ~70 s (Aufgaben rechnerisch klein) – deshalb so schnell, nicht halb gemacht. Beleg 41 neu gehasht = gemeldet; Kopf 149eeb80821b86e9… (42 Belege).
- Feldtheorie: Leapfrog-Drift 0,26 % (dt 0,05), 1,07 % (dt 0,1); Masse 1,414139 (√2: 1,414214); zwei gleiche Quellen ziehen an, gegensätzliche stoßen ab; Gitter-Masse m = arccosh(2) = 1,317 (Fit 1,342) statt √2 – Gittereffekt, korrekt erkannt. 27³ friert in 2 Domänen ein (Torus-Wand), 54³ → 1 Domäne.
- Raum aus Korrelationen: 9³-Gitter 729/729 Nachbarschaften richtig, Abstände exakt (Graph); direkte Einbettung 10,8 % Fehler.
- Bjerknes |F|d² = 1/(8π); Eckabfluss verändert Kraft bis −21 % (d/L = 0,8). Kugel–Würfel–Kugel gedämpft 8× weniger Beschleunigung (vereinfachtes Modell). F-Teil überwiegend Formelmodelle (grob).
- Z1: Filter verbessert (verworfene Gute 0,01 %), aber Störung 0,10 (= 5σ) geht weiter zu ~30 % durch; globale Störung mit unabhängiger Referenz 62 % statt 99,9 % – grundsätzliche Grenze schwacher Störungen bleibt.

### 90°-Umschlag gegen Störungen (02.11., lokal, k42check/umschlag.py)
Idee (Thomas): Punkt (3,4) muss nach 90° als (−4,3) im Nachbarquadranten erscheinen – was nicht mitdreht, ist Störung.
Test: 20 000 Ereignisse, σ = 0,02; Störung fest am Sensor; 3 Messungen (Lage 0, 90° um z, 90° um x), Störung per kleinste Quadrate geschätzt und abgezogen.
Ergebnis: ohne Abgleich A = 0,10 → 50 % falsch, A ≥ 0,25 → 100 %; mit Umschlag bei ALLEN Stärken 0,00 % (Median-Fehler 0,027 statt 0,031). Gilt für Achsen- und Diagonalstörung.
Grenze: wirkt nur auf sensorfeste (mitdrehende), zeitlich konstante Störungen. Weltfeste Störung verhält sich wie Signal (nicht trennbar). Kosten: 3 Messungen statt 1.
Gibt es schon: Umschlagmessung (Metrologie), Carouselling bei Kreiseln, Chopper/Lock-in. Kandidat K44.

### Phase = Winkel, Log über die 1, Fraktale, Universal-Schnittstelle (02.11., lokal, k44/phase_log.py)
- 2 Achsen x=cos t, y=cos(t+φ): φ=0° Diagonale, 30° Ellipse 0,268, 60° 0,577, 90° Kreis, 180° Gegendiagonale (Lissajous).
- 3 Achsen x=cos t, y=cos(t+φ), z=cos(t+2φ): φ=0° Linie entlang Raumdiagonale (Länge bis √3 = Würfelecke); φ=120° exakter Kreis, Radius √(3/2)=1,2247, Ebene senkrecht auf (1,1,1) (Drehstrom-Prinzip); φ=60° Kreis um andere Diagonale; φ=90° Ellipse (Radius 1…√2).
  → Die Phase allein entscheidet: Würfeldiagonale (linear) oder Kreis (Kugel). Normierung über Phasenwinkel bestätigt.
- Log über die 1 (log 1 = 0), nicht über die 0 (log 0 = −∞): log10(1…10) Abstände 0,301…0,046, Summe exakt 1; ab 10 Wiederholung (Mantisse). Benford: führende Ziffer d mit log10(1+1/d) (30,1 % … 4,6 %).
- Fraktale über log normiert: D = log N / log s: Cantor 0,631; Koch 1,262; Sierpinski-Dreieck 1,585; -Teppich 1,893; Menger 2,727; voller 3³-Würfel 3,000.
- Universal-Schnittstelle 27³ links 1, rechts 0: stationär exakt linear (Abw. 3·10⁻⁷); Welle braucht t ≈ 21 für 25 Zellen.

## Schalenbild der drei Ebenen (02.11., Thomas)
Physik (endlich: Bekenstein, Poincaré-Wiederkehr, Pseudozufall periodisch) ⊂ Energie (Thermodynamik, Feld) ⊂ Raum der unendlichen Variationen (Abstraktion; nach innen und außen als Überlagerung; 0…∞ ↔ 0…1 über t = x/(1+x); Kontinuum überabzählbar, Cantor).
Entsprechungen: Hilbertraum der Quantenmechanik (unendlich-dimensional) um endliche Messwerte; Fourier-Paar „innen“ (kleine Skalen, hohe Frequenz) ↔ „außen“ (große Skalen). Lernen = eigene Ordnung (Rezeptkarte RAUM27_Index.md), Speicherhierarchie heiß/warm/kalt; Null-Operator = dreiwertige Logik (Łukasiewicz 1920, Fuzzy Zadeh 1965).
Status: Rahmen bzw. Weltbild (Overlay/Abstraktion), als Ganzes nicht prüfbar; prüfbar sind die Übergänge (Messung schneidet Kontinuum auf endliche Stufen; Rauschen als nicht-periodische Quelle).

## Sprung 2D → 3D → 4D: Isotropie ohne Gewichte (05.11.2026)
- 4. Moment (M4 − 3·M22 = 0 ⇒ richtungsgleich): 3D einfach (6) Rest 2; fcc (12) −4; bcc (8) −16 → in 3D kein einzelnes Gitter isotrop (nur Mischung: einfach:fcc = 1:½ oder 1:¼:1⁄16).
- 2D Hexagon/Ziegel (6 Nachbarn): isotrop ohne Gewichte (Spreizung ~100× kleiner als Quadrat).
- 4D FCHC (24 Nachbarn = Ecken des 24-Zellers, dessen Zellen Oktaeder sind): M4 12, M22 4, Rest 0 → isotrop ohne Gewichte.
- Bekannt: Gittergas-Automaten (FHP 1986 hexagonal 2D; d'Humières/Lallemand/Frisch 1986: 3D über FCHC in 4D und Projektion nach 3D).
- Thomas: „4D Okta, 3D Hex, die vierte Dimension verhindern = Sprung“ → passt: 3D ist die Lücke; Rundheit entweder durch Gewichte oder durch Projektion aus 4D. 8/6 = 4/3, 6/8 = 3/4, Produkt 1.

## Gesamtsimulation Stufe 1: Raum, Feld, Materie, Quadranten (07.11.2026, ohne Informationsebene)
Skripte `gesamt/gesamt.py` (a90be12f…, Ergebnis 035b34a5…) und `gesamt/materie.py` (81d2dd6a…, Ergebnis 93c946e9…), Gitter 61³, Zeittakt 0,1.
| Stufe | Ergebnis | Einordnung |
|---|---|---|
| Raum | Zustand 0 neu erzeugt, Hash = Referenz c7905244…; Spiegelklassen 1/6/12/8, Orientierung 13 gleich / 14 umgekehrt; 19 Schnittebenen-Zellen + 8 Achtelkugeln | exakt |
| Feld 6 Nachbarn | Front 0,964/0,970/0,977, Spreizung 1,34 % | gemessen |
| Feld 15 (6 + 8, 1/9 : 1/72) | 0,968/0,969/0,967, **Spreizung 0,135 %** (bester Wert) | gemessen |
| Feld 19 (Ebenen, 1/18 : 1/36) | 0,976/0,963/0,977, Spreizung 1,43 % | gemessen – als Wellen-Laplace nicht besser als 6 |
| Feld 27 (1 : ¼ : 1/16) | 0,976/0,969/0,974, Spreizung 0,72 % | gemessen |
| Energie | Drift 0,15–0,16 % über 20 Zeiteinheiten bei allen | Zeitschritt-Fehler, klein |
| Oktanten-Fluss (Quelle Mitte) | alle 8 gleich (z. B. 0,6150), gleiche Ankunft | per Konstruktion (Symmetrie) – Kontrolle bestanden |
| Quadranten-Erkennung | Quelle in einer Achtelkugel: 4/4 richtig erkannt (größter Hüllenfluss) | gemessen |
| Materie (Phasenblase, ε = 0,2 ≈ ΔV 0,4) | Schwelle R = 5 (R ≤ 4 fällt, R ≥ 5 wächst) **bei allen vier Nachbarschaften gleich** | gemessen; deckt sich mit früherem Spielzeug-Urknall |
- **Fehler bei mir (Claude), geklärt:** erster Materie-Lauf mit ε = 0,4 – oberhalb 2/(3√3) ≈ 0,385 gibt es keine zweite Mulde, also kein falsches Vakuum; alle Läufe „bleibt“. Neu gerechnet mit ε = 0,2.
- Erkenntnis: Die Isotropie-Gewichte der Strömungsgitter (D3Q19) sind für Geschwindigkeitsmomente gemacht, nicht automatisch für den Wellen-Laplace; dort ist **6 + 8 mit 1/9 : 1/72** am richtungsgleichsten, mit nur 14 Nachbarn. Die Materie-Schwelle hängt nicht vom Gitter ab, nur von ΔV.
- Stand: Raum, Feld, Materie und Quadranten-Logik sind konsistent ⇒ Grundlage für die Informationsebene.

## Gesamtsystem Stufe 2: Informationsebene auf dem 6+8-Gitter (07.11.2026)
Regeln vorher festgelegt (`info/info_ebene.py` 17dc3736…): Welle auf 6+8 (1/9 : 1/72), Gitter 81 = 3⁴; Abfluss nur im äußeren Neuntel (Faltungszone); alle 20 Takte ein Energiepuls im Oktanten (+,+,−), Saat 27; Informationszellen in 3er-Stufen (Kante 27/9/3/1), Zündung bei Energie > θ = 0,02 → 27 Unterzellen, Rückprojektion bei Geschwistersumme < θ/4; 2000 Schritte.
| Frage | mit Abfluss | ohne Abfluss (Gegenprobe) |
|---|---|---|
| F1 begrenzt? | ja: Zellzahl pendelt bei 70 000–78 000 (≈ 14 % von 81³) | nein: 528 711 ≈ 99,5 % von 81³ (Überlauf bis zur feinsten Ebene) |
| F2 Feinheit folgt Energie? | ja: Korrelation Zellebene ↔ log Energiedichte 0,69 | nein: 0,02 (alles gleich fein) |
| F3 Oktant der Quelle erkannt? | ja (+,+,−) | ja |
| F4 Bilanz rein = Feld + abgeflossen | Rest 0,06 % (598,6 = 124,3 + 474,7) | Rest 0,08 % |
| F5 reproduzierbar | Wiederholungslauf: Hash 7ee7737d… identisch | – |
- **Fehler bei mir (Claude), geklärt:** erster Lauf mit falscher Energiebuchhaltung (Gradientenanteil halbiert, Abflussleistung verdoppelt) ⇒ Bilanzrest −74 % bzw. +24 %. Nach Korrektur 0,06–0,08 %.
- Deutung: „Innen verdichten, außen falten“ funktioniert als Regel – der Abfluss im äußeren Neuntel hält die Informationsebene begrenzt und lässt die Feinheit der Energie folgen; ohne ihn läuft alles auf die feinste Ebene über und die Struktur geht verloren.
- Weiter an Antigravity: K53 (Gesamtsystem lang, Variationen, Gegenproben).

## KERN: Der Quadranten-Operator – Kugel im Würfel, gespiegelt an der Eins (08.11.2026, Thomas; Notizen als Fotos)
- **Struktur:** Kugel in 8 Achtelkugeln; jede zentriert in einem Würfel (Kugel im Würfel, eigenes Achsenkreuz); 8 Würfel ergeben wieder eine Kugel = Operator, in jedem Quadranten gleich.
- **Spiegel:** Einheitskugel r = 1 ist Fixfläche der Inversion x → 1/x. Innen (0…1) verdichtet x/n, außen expandiert n/x.
- **Funktionen je Quadrant (λ₁ Amplitude, λ₂ Wellenmaßstab, Argument 16x/(9λ₂)):** λ₁ sin = innen, Rotation um die Eins (Kreis); 1/(λ₁ sin) = außen, Inversion des Sinus, Cotes'sche Spirale mit nächstem Punkt auf r = 1, überstreicht 180°/k, k = 16/(9λ₂); λ₁ sin² = Verdopplung 1 → 2 (nächste Schale); λ₁ sinh = Hülle/Wand bis zum Rückkehrpunkt (Phasenblasen-Wand ist tanh = sinh/cosh). Kosinus nur einmal als Anstoß (Startphase, Richtung), danach nur Sinus; Richtung aus Takt-Übergängen.
- **Skalen (Notiz):** 10 linear (Würfel), 9 = 3² logarithmisch (Fläche), 27 = 3³ logarithmisch (Raum); Spiegellinien zwischen versetzten Reihen = Ziegelverband/Sechseck.
- **Korrektur bei mir (Claude):** λ₁ ≠ λ₂ ⇒ Selbstähnlichkeit nur für λ₁ = λ₂; 1/sin ist Spirale (Cotes), Gerade nur bei k = 1.
- **Status:** Bausteine im Modell geprüft (Inversion exakt, 6+8-Gitter, Informationsebene mit Abfluss begrenzt, Phasenblasen-Schwelle). „Funktion des Universums, die sich wiederholt“ = **Hypothese Thomas**; verwandt mit konformer zyklischer Kosmologie (Penrose: Ende wird umskaliert zum nächsten Anfang; Vorhersage „Hawking-Punkte“ in der Hintergrundstrahlung, umstritten, bisher nicht bestätigt). Für eine Prüfung nötig: eine Vorhersage, die sich vom Standardmodell unterscheidet.
- Offen: Inversion des Sinus je Achtelkugel exakt rechnen; Schließen der 8 gespiegelten Achtelkugeln zu einer Kugel; Kandidat für eine beobachtbare Vorhersage suchen.

## KERN (Fortsetzung): Sinus expandiert – Würfel komprimiert – Raute stabilisiert; 48 Verschiebungen (08.11.2026, Thomas)
- Thomas: In jeder Ebene, Spiegelung, Projektion, Schnittstelle, Wechselwirkung expandiert der Sinus kugelförmig und komprimiert wieder zum Würfel; dazwischen kristallisiert die Raute als Stabilisierung; Phasenschichten laufen nicht mehr glatt, sondern entlang der Kristallisationslinien; daher 6 × 8 verbundene Knoten / 48 Räume, die sich gegeneinander verschieben und stabilisieren.
- Bekannt: Rhombendodekaeder (12 Rauten, raumfüllend, Zelle der dichtesten Kugelpackung, trägt 1+6+12+8; Granat, Wabenböden). Raumzentriertes Gitter (6+8) hat **48 Gleitsysteme** ({110} 12, {112} 12, {123} 24, Richtung ⟨111⟩) – Schichten gleiten entlang von Rautenebenen; Kreuzen der Gleitsysteme verfestigt (Kaltverfestigung). 48 = Symmetriezahl des Würfels.
- Einordnung: Kristallphysik bekannt; „gleicher Ablauf auf jeder Ebene des Universums“ = Hypothese Thomas.
- Prüfbar: 48 gitter-invariante Verschiebungen entlang Rautenebenen zählen; 6+8-Gitter unter Scherung (Verfestigung bei mehreren Gleitrichtungen); Voronoi-Zellen aus wachsenden, sich begrenzenden Kugeln (Rhombendodekaeder bzw. Oktaederstumpf).

## HERZSTÜCK: Die vier Sinusfunktionen – Sinustransformation verbindet Flächen zu Räumen (08.11.2026)
Funktionen (Thomas): u = 16x/(9λ₂); (1) λ₁ sin u, (2) λ₁ sin² u, (3) λ₁ sinh u, (4) 1/(λ₁ sin u). Gerechnet (Claude, `sinus/sinus4.py`, Bild `sinus4.png`), λ₁ = λ₂ = 1:
- Periode in x = 9πλ₂/8 ≈ 3,534; Steigung am Ursprung von sin und sinh gleich 16λ₁/(9λ₂) = 16/9.
- (1) und (4) berühren sich genau dort, wo λ₁|sin u| = 1 – bei λ₁ = 1 an den Scheiteln y = ±1 = **Spiegellinien**. (4) bildet zwischen den Nullstellen abwechselnd nach oben und unten offene Zellen (U-Formen) – das ist das Zellenmuster der Skizze „Haut und Strich / Spiegellinie“.
- (2) λ₁ sin² u: halbe Periode, Werte 0…λ₁, Mittel λ₁/2, berührt (1) an den Scheiteln – Verdopplung.
- (3) λ₁ sinh u: keine Schwingung, wächst exponentiell – Wand/Hülle.
- Polar: r = sin(kθ) (innen, Kreis bei k = 1, Blatt bei k = 16/9) und r = 1/sin(kθ) (außen) sind exakt die Inversion am Einheitskreis (Fehler 0); 1/sin berührt r = 1 im Scheitel und überstreicht 180°/k = 101,25° bei k = 16/9.
- **Flächen zu Räumen:** Produkt sin(ux)·sin(uy)·sin(uz) zerlegt den Raum in Würfelzellen (Nullflächen = Würfelwände), in jeder Zelle ein runder Bauch (Kugel im Würfel), Vorzeichen wechselt von Zelle zu Zelle. Im 3×3×3-Block: **13 Zellen gleiches Vorzeichen, 14 umgekehrt** – genau die Spiegelparität 13/14. Inverse 1/(sin·sin·sin): Minimum |1| in der Zellmitte, Wände → unendlich (Gitterlinien).
- Bekannt: Produktsinus = Eigenschwingungen eines Kastens bzw. Basis der mehrdimensionalen Sinustransformation; Nullflächen = Knotenflächen.
- Offen: λ₁ ≠ λ₂ (Berührung nur, wenn λ₁ ≥ 1; sonst trennen sich Welle und Spiegelzellen), sinh als Randbedingung der Zellen (Wanddicke), Übergang zu 6+8-Gitter (Zellmitten = Würfelzentren, Ecken = Achtelkugeln).

## Herzstück über alle Ebenen geprüft (08.11.2026, `sinus/ebenen_test.py` 6fe60b18…, Ergebnis abc71933…)
| Test | Ergebnis | Einordnung |
|---|---|---|
| T1 Schnitte je Ebene (Frequenz ×2, Ebene 0–4) | immer 8 Oktanten; Sinusprodukt-Parität im 3×3×3-Block immer 13 gleich / 14 umgekehrt | exakt; folgt mathematisch aus dem Produktsinus (per Konstruktion sicher, aber bestätigt: gilt in jeder Ebene) |
| T2 Spiegel an der Eins je Ebene | Inversion sin ↔ 1/sin Fehler 0; kleinster Außenradius 1,000; Berührwinkel halbiert sich je Ebene (50,6° → 3,2°) | exakt |
| T3 Log-Uhr | Marken 0 / 0,301 / 0,477 / 0,602 / 0,699 / 0,778 / 0,845 / 0,903 / 0,954; alle Dekaden identisch; 9,999999 bleibt in Dekade 0, 10 springt in Dekade 1 | exakt |
| T3 7/9 gegen log₁₀ 6 | 0,77778 gegen 0,77815, Abstand 0,048 % | Beobachtung, kein Gesetz |
| T4 Benford | multiplikativer (selbstähnlicher) Prozess trifft die log-Abstände (max. Abw. 0,002); additiver nicht (0,19) | bekannt, bestätigt |
| T5 Feld schneller, Teilchen kleiner (Antwortzeit ∝ Größe, Frequenz ×2 je Schale) | Teilchen gleich groß: Phasenverzug wächst 17° → 79°; Teilchen halbiert je Schale: Verzug **bleibt 17,4° in jeder Schale** | Mitskalieren hält Verlust je Schale konstant; Verlust null erst, wenn Antwortzeit ≪ Feldperiode |
| T6 6 + 8 Tropfen (Gewichte) | Ruhe 2/9, Flächen 6·1/9 = 2/3, Ecken 8·1/72 = 1/9; **Nachbarn zusammen 7/9, Ruhe 2/9**; Summe 1; isotrop | exakt – die 7/9 und die zwei freien Neuntel stecken genau in den Gitter-Gewichten |
- Verbindliche Festlegungen in eigener Datei `RAUM27_Festlegungen.md` (zuerst lesen, nicht neu verhandeln).

## Zwei Tropfensysteme ineinander: 6 Achsen-Tropfen (Anode/Kathode) + 8 Diagonal-Tropfen (08.11.2026)
- Thomas: Tropfen verbinden ± auf N/S, O/W (und oben/unten) bzw. die 8 Diagonalen; zwei unterschiedliche Systeme, ineinander gepackt; jede Achse wie Anode/Kathode ⇒ daraus entstehen die Tropfen.
- Bekannt: Je Achse ein Dipol (Anode/Kathode) ⇒ 2 Keulen; drei Achsen ⇒ **6 Keulen** = Form der p-Orbitale (pₓ, p_y, p_z). Ecken mit abwechselndem Vorzeichen ⇒ Oktopol x·y·z ⇒ **8 Keulen zu den Raumdiagonalen** = Form des f_xyz-Orbitals. Kugelflächenfunktionen verschiedener Ordnung (l = 1 und l = 3) sind orthogonal ⇒ beide Systeme überlagern sich, ohne sich zu stören.
- Geprüft (Claude, `sinus/tropfen.py`): Mittel über die Kugel ⟨x·xyz⟩, ⟨y·xyz⟩, ⟨z·xyz⟩ ≈ 0 (Rauschen ≤ 5·10⁻⁵; analytisch exakt 0) ⇒ orthogonal. x·y·z ist auf den Achsen 0 und maximal genau auf den Raumdiagonalen (1/(3√3) = 0,19245); Vorzeichen der 8 Ecken abwechselnd (+ − − + − + + −) = Spiegelparität der Ecken. Achsen-Tropfen reichen auf der Diagonale nur 1/√3 = 0,577.
- Deutung: Die 6 und die 8 sind zwei unabhängige Kanäle auf derselben Kugel – ineinander gepackt ohne Übersprechen.

## Gesamtsimulation Stufe 3: Schalen, Tropfenfelder, Partikel mit Sieb (08.11.2026, `sinus/stufe3.py` f4516707…, Ergebnis 5cc22e23…)
Aufbau (Thomas): Mitte v⁴ (Ursprung), Achsenspitzen v², darin die Tropfenfelder (6 Achsen + 8 Diagonalen), darin die Partikel als Fraktale, Sieb lässt je Schale nur die halbe Größe durch. Regeln: Schalen Radius 1/2/4/8/16; Feldfrequenz je Schale ×b; Siebloch je Schale ×c; Antwortzeit ∝ Größe; Phasenverzug atan(2π f τ); 200 000 Partikel, Größen 1/64…1.
| Fall | mittlerer Phasenverzug je Schale (Grad) | Ergebnis |
|---|---|---|
| Halbierung passt (f ×2, Loch ×½) | 12,74 / 12,72 / 12,76 / 12,76 / (9,60 Randschale) | **gleich in jeder Schale** (Innen-Spreizung 0,04°) |
| 3er (f ×3, Loch ×⅓) | 10,76 / 10,78 / 10,77 / (11,87 Rand) | gleich (0,02°) |
| falsch gepaart (f ×2, Loch ×⅓) | 10,8 → 7,3 → 4,8 → 3,6 | driftet |
| ohne Sieb | 4,2 → 8,3 → 15,1 → 24,8 → 36,7; Verlust 0,07 → 0,31 | wächst nach außen (×4 Verlust) |
- **Ergebnis:** Verluste bleiben über alle Radien gleich, **wenn das Sieb genau im Kehrwert der Feldbeschleunigung verkleinert** (Feld ×b ⇔ Teilchen ×1/b; Halbierung bei Verdopplung, Drittel bei Verdreifachung). Jede Fehlpaarung driftet; ohne Sieb steigen Verzug und Verlust nach außen. Randschale = Sammelbecken der kleinsten Teilchen (endliche Ebenenzahl) – kein Widerspruch.
- **Feldlösung (exakt):** Oktopol-zu-Dipol-Verhältnis innen ∝ r² (1, 4, 16, 64, 256), außen ∝ r⁻² – Winkelform der Tropfen auf jedem Radius gleich, nur das Mischungsverhältnis wandert mit r² bzw. r⁻² (wieder Inversion x ↔ 1/x).
- Per Konstruktion: Sortierung der Größen in Schalen (Siebregel) und gleiche Winkelform je Schale. Gemessen: Konstanz bzw. Drift des Verzugs, Verlustverlauf.
