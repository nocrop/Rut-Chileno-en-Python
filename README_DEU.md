# Validator für chilenische RUN (besser bekannt als RUT) in Python
*Sprechen Sie eine andere Sprache?
[Spanisch](README.md) Todo lo que necesitas saber en Español. 
[English](README_EN.md)* Everything you need to know in English. 


<img align="right" src="https://media.giphy.com/media/ehOmuAGboX837Dx9LR/giphy.gif" width="300"/>

## Beschreibung
Hallo, mit diesem kleinen Code können Sie überprüfen, ob ein chilenischer RUT (Run) (Rol Unico Tributario) gültig ist. 
Der Validator prüft nicht nur die Prüfziffer, sondern auch, ob die Zahl innerhalb eines realistischen Bereichs liegt, um offensichtlich gefälschte RUTs auszuschließen.
Dies ist sehr nützlich, wenn Sie es zu einem Projekt hinzufügen möchten, um ihm eine zusätzliche Validierung zu geben. 

## Wie funktioniert es?
Das Skript fordert den Benutzer auf, eine RUT einzugeben. Es führt dann zwei Überprüfungen durch:
1. **Format und Bereich**: Es prüft, ob die RUT richtig formatiert ist und ob die Zahl innerhalb eines realistischen Bereichs liegt (standardmäßig von 1.000.000 bis 25.000.000).
2. **Prüfziffer**: Berechnet und prüft die Prüfziffer nach dem offiziellen Algorithmus für chilenische RUTs.

## Anforderungen
- Python
- Ein Editor zum Ausführen des Programms
- Kaffee

## Um dieses Skript auszuführen, ist keine zusätzliche Bibliotheksinstallation erforderlich. Klonen Sie einfach das Repository und führen Sie das Hauptskript aus. 
Sie müssen keine Credits oder ähnliches angeben, aber wenn Sie mir einen Kommentar hinterlassen könnten, um mich wissen zu lassen, dass Sie es benutzen, würden Sie mich, Sonic und ein Kätzchen sehr glücklich machen.
