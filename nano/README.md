# Nano-Container: Zustandsraum gegen Zugangsraum

Kein Kopplungsversuch an das Makro-Netz. Die Innenschicht bleibt entkoppelt.

## Was hier liegt

- `nano_container.py` — elastisches Billard in `[0, Q]` mit `Q = 2^40`. Keine Rotation, keine Kopplung.
- `zugangsraum.py` — zählt, über wie viele verschiedene Eintrittsrichtungen (Vorzeichentripel der Geschwindigkeit) derselbe Oktant erreicht wird.

## Der Prüfpunkt

Gemessen ist die Stabilität des Billards (Antigravity, 1 000 000 Takte, 5/5).  
Offen ist, ob die Faltung an den Wänden einen echten Zugangsraum erzeugt.

Ein Eintritt ist das Paar `(Oktant, Vorzeichentripel)` im Moment des Übergangs.

- Wenn jeder Oktant nur über eine Richtung erreicht wird, ist der Zugangsraum gleich dem Zustandsraum. Die Schleife ist dann nur eine andere Zeichnung derselben Bahn.
- Wenn derselbe Oktant über mehrere unabhängige Richtungen erreicht wird, ist der Zugangsraum größer. Der Vorteil liegt im Zugang, nicht in der Anzahl der Zustände.

Ausführen:

```
cd nano
python zugangsraum.py
```

Das Ergebnis ist eine Messung, keine Hypothese.
