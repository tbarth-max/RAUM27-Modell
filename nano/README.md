# Nano-Container: Zustandsraum gegen Zugangsraum

Kein Kopplungsversuch an das Makro-Netz. Die Innenschicht bleibt entkoppelt.

## Korrektur

Die erste Fassung faltete nur die Position und drehte die Geschwindigkeit nicht um. Der Punkt klebte an der Wand. Diese Fassung führt je Achse eine ungefaltete Ganzzahl-Koordinate. Position und Vorzeichen ergeben sich daraus, die Spiegelung ist eingebaut.

## Was hier liegt

- `nano_container.py` — elastisches Billard in `[0, Q]` mit `Q = 2^40`. Keine Kopplung.
- `zugangsraum.py` — zählt, über wie viele verschiedene Eintrittsrichtungen (Vorzeichentripel der Geschwindigkeit) derselbe Oktant erreicht wird.

## Der Prüfpunkt

Ein Eintritt ist das Paar `(Oktant, Vorzeichentripel)` im Moment des Übergangs.

Messung (100 000 Takte, Startwerte aus dem Antigravity-Bericht):

- Jeder Oktant wird aus 7 der 8 möglichen Vorzeichenrichtungen erreicht.
- Ausgeschlossen ist genau die Richtung, die auf allen drei Achsen von dem Oktanten wegzeigt.
- Der Zugangsraum ist größer als der Zustandsraum.
- Das ist eine Eigenschaft der Geometrie, kein Rechenvorteil. Die Bahn bleibt eine einzige deterministische Bahn ohne parallele Zweige.

Ausführen:

```
cd nano
python zugangsraum.py
```
