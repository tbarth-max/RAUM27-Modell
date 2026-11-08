# RAUM27 – Geometrisches Gittermuster des Raumes und seine Größe

> **Individuelles physikalisches Modell von Thomas – Diskussionsgrundlage.** Nicht begutachtet, kein Anspruch auf physikalische Gültigkeit. Kennungen: gemessen/geprüft · per Konstruktion · Abstraktion · Overlay.

Raute–Kugel–Würfel entlang der Diagonalen, Zustand 0 (Würfel R₀ = 9, Ränder Oktaeder/Kugel/Würfel), Kugeln + Oktaederlücken = RAUM27-Gitter, Ringe und Neunerprobe, Kausalitätsgrenze, die 9 in jeder Richtung, gemeinsame Zustandsebene. Die Größe des Raumes in c-Einheiten (07.11.): Zelle = c·τ, z. B. τ = 1 ns → 0,30 m, Raum mit 9 Schalen 2,7 m; 1 s → 3·10⁸ m je Zelle.

## Raute – Kugel – Würfel entlang der Diagonalen: 1 bis 9 (07.11.2026)
- Alle drei Formen mit gleicher Reichweite 1 auf den 6 Achsen (±x, ±y, ±z). Radius entlang Richtung u: Raute/Oktaeder 1/‖u‖₁, Kugel 1, Würfel/Quadrat 1/‖u‖∞.
- Achse 1/1/1; 45° 0,7071/1/1,4142; Raumdiagonale 0,5774/1/1,7321.
- Raute × Würfel = 1 genau auf Achsen, 45°- und Raumdiagonalen (Kugel = geometrisches Mittel, Inversion r·r* = 1); schief (2,1,0): 0,8333 ≠ 1.
- (Würfel/Raute)²: Achse 1, 45° 4, Raumdiagonale 9 → auf der Raumdiagonalen spannt das Quadrat des Radius genau 1 … 9; Kugel bei 3 (log-Mitte). Thomas' Normierung 1–9 auf der 45°-/Diagonallinie bestätigt (Abstraktion, geprüft).
- c², c⁴ als Geschwindigkeit bleiben Einheitenfrage; Rechnung in Gittereinheiten (Achsenreichweite 1 pro Takt).

## Zustand 0 – Definitionsraum / Bilanzraum (07.11.2026)
- Thomas: erste Abstraktionsebene, statisches Gerüst („Kristall“), kein Inhalt (kein Feld, keine Teilchen, keine Vakuumenergie, keine Bewegung). Nullpunkt = Betrachter. Später dringen äußere Wechselwirkungen ein, Gleichgewichte in den Sphären 1–9 (9⁹ = 387 420 489 Möglichkeiten).
- Gebaut (`zustand0/zustand0.py`), R₀ = 9 Schalen, drei geschachtelte Ränder: Oktaeder (Kausalfront) 1 159 Knoten, Kugel (Betrachtungshorizont) 3 071, Würfel (äußere Hülle) 6 859 = 19³.
- Schalen k = 1…9: Oktaeder 4k²+2 (6, 18, … 326); Würfel 24k²+2 (26, 98, … 1 946); Kugel unregelmäßig (Gitterpunkte auf Kugelschalen).
- Hash Zustand 0: c79052448d2fbd447dc2dd6c9556f46d835ce3a935e9c3cb2c8c21c02d75e25b (lokal, nicht in der Kette gebucht).
- Ebene: Abstraktion (Geometrie, geprüft). Physikalische Größe über R₀ ↔ 43,3 Mrd. Lj (Overlay).

## Kugeln + Oktaederlücken = RAUM27-Gitter (Schachbrett in 3D) (07.11.2026)
- Thomas: Kugel (dichteste Packung) und Rückprojektion (Lücken) schließen sich zum Kristallgitter = energetische Wechselwirkungskette.
- Befund (gerechnet): fcc-Kugeln + ihre Oktaederlücken = einfaches Würfelgitter mit Schachbrett-Belegung (Steinsalz-Struktur NaCl). Aufteilung nach Parität x+y+z: gerade = Kugeln (fcc), ungerade = Lücken.
- Im 27er-Würfel: gerade 13 = Zentrum + 12 Kanten (= fcc-Nachbarschaft, Koordinationszahl 12); ungerade 14 = 6 Flächen + 8 Ecken (= 6 + 8, Ecken des Rautenwürfels). 27 = 13 + 14.
- R₀ = 9: 6 859 = 3 429 gerade + 3 430 ungerade.
- Bekannt: NaCl-Struktur (zwei ineinandergestellte fcc-Gitter); numerisch Rot-Schwarz-Ordnung / versetzte Gitter (Yee-Gitter in der Elektrodynamik: E und B auf versetzten Plätzen, Energie pendelt).
- Folge: Die Wechselwirkungskette Kugel ↔ Lücke ist im simulierten Gitter schon enthalten; als Simulation: Rot-Schwarz-Takt (gerade/ungerade abwechselnd aktualisieren) – prüfbar in K50 Teil B.

## Karoraute = Lücke zwischen Kugeln = Fraktal-Tunnel (07.11.2026)
- Thomas: Kugel in jedem Quadranten + quadratische Struktur → „Karoraute“, zugleich Fraktal-Tunnel.
- Gerechnet: 2D Quadratpackung Kreise π/4 = 78,5 %, Lücke (gekrümmte Raute) 21,5 %, größter Kreis in der Lücke r·(√2−1) = 0,414 r. 3D einfach kubisch: Kugeln π/6 = 52,4 %, Lücke 47,6 %; Würfelhohlraum im Zentrum (bcc-Platz) r·(√3−1) = 0,732 r; Engstelle Fenster (Quadratfläche) 0,414 r.
- Tunnel: Hohlräume (Würfelmitten) über Fenster verbunden → durchgehendes Netz; Engstelle 0,414 r entscheidet, was durchkommt.
- Fraktal-Kette bei Faktor (√2−1) je Stufe: 1 → 0,414 → 0,172 → 0,071 → 0,029 → 0,012. Vergleich K49-Sieb: Faktor ½ je Stufe (gesetzt) – geometrisch natürlicher Faktor wäre √2−1 ≈ 0,414 (Fenster) bzw. √3−1 ≈ 0,732 (Hohlraum).

## Ringe, Neunerprobe, c_X-Skalierung, eingefrorene Expansion (07.11.2026)
- Ringe um die Mitte wachsen linear: Ring k hat 8k Zellen (8, 16, 24, 32); 1 + 8 + 16 + 24 + 32 = 81 = 9×9. Falten ist etwas anderes: ×8 je Raumfaltung (8ⁿ). Nur ungerade Kanten haben eine Mitte (10×10 nicht; 100 − 81 = 19 ist kein Ring).
- „Zehn = neue Eins“ = Rechnen mod 9 (Neunerprobe): 10 ≡ 1, 11 ≡ 2. 0,999… = 1 genau (Fehler bei Thomas geklärt: 9/10 = 0,9 endlich). Beherrschbare Periode = Bruch mit 9er-Nenner (1/9, 1/99).
- c meint c_X (eigene Ausbreitungsgeschwindigkeit des Systems, z. B. Signal in Leiterbahn); Missverständnis bei mir (Claude) geklärt. Maßstab s_X = c_X/c; Fläche ∝ s², Raum-Zeit-Volumen ∝ s⁴ – „c², c⁴“ nur als Verhältnisse, nicht als Geschwindigkeiten. c⁴/G ≈ 1,2·10⁴⁴ N (Planck-Kraft) ist der physikalische Ort von c⁴.
- Expansion einfrieren = mitbewegte Koordinaten + konforme Zeit (Kosmologie): Licht läuft 1 Gitterschritt je Zeiteinheit; λ = 1/f bei c = 1. Gilt nur für reine Wellen; Dispersion, Dämpfung/Diffusion, nichtlineare Impulse (Nerv) brauchen eigenen Formfaktor.

## Kausalitätsgrenze: Raute, Quadrat, Kugel; 7 : 2 (03.11.)
Gedanke: c als maximale Auslenkung vom gemeinsamen Fluchtpunkt in 3D; wo Kausalität abreißt, entsteht zwischen den Achsen eine Raute, aufgestellt ein Quadrat/Würfel; zur Kugel aufgerollt landet man bei 7 von 9, Rest 2 zum Schwingen (Ordnung 7 : Chaos 2).
Gibt es schon: Lichtkegel. Auf dem Gitter hängt die Form der Kausalgrenze von der Nachbarschaft ab: nur Achsenschritte (von Neumann, unser Δₐ) → Raute (2D) bzw. Oktaeder (3D); mit Diagonalschritten (Moore) → Quadrat/Würfel; isotroper Grenzfall (Kontinuum) → Kreis/Kugel. Zelluläre Automaten nennen das „Lichtgeschwindigkeit“ (1 Zelle je Takt).
Gerechnet: 2D im 3×3-Feld: Raute 4,5, Kreis (r = 1,5) 7,069, Quadrat 9 → Kreis : Rest = 7,07 : 1,93 (π/4 = 0,785 ≈ 7/9 = 0,778). 3D im 3×3×3: Oktaeder 4,5, Kugel 14,14, Würfel 27 → Kugel : Rest ≈ 14 : 13 (π/6 = 0,524). Die 7 : 2 gilt also in der Fläche, nicht im Raum.
Ebene: Gitter-Kausalität = Abstraktion (geprüft); „Ordnung : Chaos = 7 : 2“ = Overlay.
Korrektur der Lesart (Thomas): 7/9 = feste Struktur (Materie/Energie, Ordnung), 2/9 = dynamischer Zufalls-/Chaosbereich (Quantenraum, reagiert). Gibt es schon: Zerlegung Signal + Rauschen (Varianzanteile), „Rand des Chaos“ (Systeme nahe dem kritischen Punkt), Exploration/Exploitation, Simulated Annealing, Dropout. 7 : 2 ist Festlegung (Overlay), nicht gemessen; prüfbar als Varianzanteil fest/zufällig in einem Lauf (z. B. Gitter-Feld mit Rauschen: bei welchem Rauschanteil Lernen/Anpassung am besten ist, liegt das Optimum nahe 2/9 = 22 %?).

## Die 9 in jeder Richtung, Verdopplungsbahnen mod 9 (03.11.)
Gedanke (Thomas): Die 9 setzt sich in jede Richtung fort – halbieren (4,5; 2,25; …) und verdoppeln (9·2ⁿ) – und bleibt in jedem binären Fraktalzweig; das ist der Einzelspiegel, in die nächste Ebene geschoben (Durchmesser 2 → Radius 1 der nächsten Ebene).
Geprüft: Ziffernwurzel von 9/2ᵏ (k = 0…7: 9; 4,5; 2,25; 1,125; 0,5625; 0,28125; 0,140625; 0,0703125) und 9·2ᵏ (k = 0…11: 9 … 18432) stets 9; einfache Quersumme teils 18 (288, 576, 4608, 9216, 18432), erst die wiederholte ist 9. Grund: 10 ≡ 1 (mod 9); 9/2ᵏ = 9·5ᵏ/10ᵏ.
Verdoppeln mod 9 zerfällt in drei Bahnen: Fixpunkt 9; Spiegelpaar 3 ↔ 6; Umlauf 1 → 2 → 4 → 8 → 7 → 5 → 1 (Halbieren läuft rückwärts 1 → 5 → 7 → 8 → 4 → 2). Dreiteilung Fixpunkt / Spiegelpaar / Umlauf. Die 9 = Einzelspiegel, auf jeder Ebene unverändert.
Einordnung: Bahnen sind echte Modul-Arithmetik (Abstraktion, geprüft); „3-6-9“-Deutungen (Tesla/Vortex) sind Zahlenmystik ohne Beleg. Im Zehnersystem; allgemein Fixpunkt bei Basis − 1.
K48 hochgeladen (03.11.): Ordner 1PjtQVpgxN8pVIScNwuZZ_XxlPpqCNT4k, Auftrag 1GoEraMs3NlFmRnQKFjZbA9i4JD37KlkQ (8 875 Bytes, sha256 83cd96bc…), Ergebnis 1dlG1CyLfu-E-hflxZYTZyv1WxuXlOgQy. Teile A–J (Urknall-Modell, Mühlrad, Antwortmatrix, Feld folgt Geometrie, Schalen 6/8, Oktant-Kammern, Dreh-Rechner, Sensorwürfel, Zahlen, Lean kompiliert).

## Gemeinsame Zustandsebene auf den drei Kugelschnitten (07.11.2026)
- Thomas: Hyperebenen = die 8 Spiegelungen des Ursprungsquadrats (N, S, O, W, NO, SO, SW, NW) → nächstes, größeres Quadrat; das in den Schnittflächen der Kugel (zwei Polschnitte + Äquatorschnitt), die die Kugel in 8 Achtelkugeln teilen; gemeinsame Zustandsebene auf diesen Schnittflächen definiert, die 8 Quadranten darüber verbinden.
- Geprüft (Claude): Drei senkrechte Schnittebenen mit je 3×3 Spiegelbildern ergeben zusammen **19 Zellen**: Mitte 1, Flächen 6 (eine Spiegelung, Orientierung umgekehrt), Kanten 12 (zwei Spiegelungen, Orientierung gleich). Die übrigen **8** der 27 (Ecken, drei Spiegelungen, umgekehrt) liegen in keiner Ebene = die 8 Achtelkugeln.
- Bekannt: Das ist das Lattice-Boltzmann-Gitter D3Q19; Gewichte 1/3, 1/18, 1/36 machen es exakt isotrop 4. Ordnung (M4 = 1/3 = 3·M22, c_s² = 1/3) – Neunerbrüche. Zusammen: Ebenen (19) + Achtelkugeln (8) = 27 (D3Q27; Gewichte 8/27, 2/27, 1/54, 1/216 liegen auf der Familie f = 2e + 8c).
- Übersicht der drei Verknüpfungen: Ebenen allein = 19 (Mitte + 6 + 12); Flächen + Ecken = 15 (Mitte + 6 + 8, raumzentriert); alles = 27. Alle drei mit passenden Neunerbrüchen isotrop.

## RAUM27 in c-Einheiten – Simulation (07.11.2026)
- Ziel Thomas: Raum unabhängig von der Rechengeschwindigkeit der Hardware definieren; c = 1 Zelle pro Zeiteinheit; jeder hat denselben Raum (gleiche Knoten), Umrechnung in m/s nur beim Ablesen.
- Skript raum_c/raum27_c.py: lineare Welle f̈ = Δf auf 61³ (Messraum R₀ = 9 Schalen, Puffer gegen Rand), Gauß-Puls σ = 1,5 im Nullpunkt, Rechentakt dt = 0,1 (≠ physikalische Zeit), Ankunft der führenden Front je Schale.
- Frontgeschwindigkeit (Zellen/Zeiteinheit, Fit r ≥ 3): 6-Nachbar Achse 0,969 / 45° 0,969 / Raumdiag. 0,983 (Spreizung 0,014); isotrop 1:¼:1⁄16 0,958 / 0,966 / 0,962 (Spreizung 0,008). → c ≈ 1 auf ±4 %; Rest = Gitterdispersion des endlich breiten Pulses; isotrop richtungsgleicher.
- Invarianz: gleicher Lauf „schnell“ (1,7 s) und künstlich „langsam“ (2,1 s) → identischer Hash b19baaff… → Ergebnis in Gittereinheiten hängt nicht von der Hardware-Geschwindigkeit ab.
- Grenze: Bit-Gleichheit über verschiedene Rechner/Rechenreihenfolgen mit Kommazahlen nicht garantiert → dafür ganzzahlig/Brüche (K48b X3).
- Ablesen (Zelle = c·τ): τ = 1 ns → 0,30 m (Raum 9 Schalen 2,7 m); 3 GHz → 0,10 m; 1 ms → 300 km; 1 s → 3·10⁸ m.

## Eigenes c je System – Gleichstellung (07.11.2026)
- Thomas: jedes System X definiert c_X = Knotenabstand / Durchlaufzeit als 1; innen gleiche Struktur ohne Umrechnen, niemand benachteiligt.
- Innen: gilt (Simulation raum_c: Ergebnis unabhängig von Rechengeschwindigkeit, identischer Hash).
- Zwischen Systemen: Benachteiligung nur, wenn in echter Zeit (Wanduhr) synchronisiert wird. Lösung: Abgleich in logischen Takten (Durchläufe) statt Sekunden – bekannt als Lockstep / Zugbetrieb / logische Uhren (Lamport 1978). Dann zählt jeder Schritt gleich, Schnelle warten auf Langsame.
- Bezug Grundsatz: Gleichstellung der Struktur = keine Benachteiligung durch Hardware (Gesetz 1–3).

## Zusammenfassung Raum (Gesamtsystem 07.11.)

## 2. Raum
- **Zustand 0:** Würfel R₀ = 9 mit drei Rändern: Oktaeder L1 1159, Kugel L2 3071, Würfel L∞ 6859 Knoten. [G]
- **Mitte und Ringe:** In der Ebene hat Ring k genau 8k Zellen. 1 + 8 + 16 + 24 + 32 = 81 = 9×9. Nur ungerade Kanten haben eine Mitte. [G]
- **Isotropie:** Gewichte 1 : ¼ : 1/16. Richtungs-Spreizung der Welle 0,15 % gegenüber 1,56 % bei 6 Nachbarn. [G]
- **Kristallbild:** Kugeln (fcc) + Oktaederlücken = einfach kubisches Gitter. 27 = 13 + 14 (Paritätsteilung). [G]
