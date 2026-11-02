# Übungsblatt 5: UI-Test-Automatisierung mit Playwright

Zu testende Anwendung: https://demo.playwright.dev/todomvc/

## 1. Playwright starten (Docker Desktop)
Für diese Übung nutzen wir eine vorkonfigurierte **Playwright Desktop-Umgebung**, die Sie direkt im Browser (z. B. via GitHub Codespaces) nutzen können. 

1. Öffnen Sie ein Terminal im Hauptverzeichnis des Repositories.
2. Starten Sie die Umgebung mit:
   ```bash
   Uebung5/run.sh
Sobald das Terminal Desktop is READY! anzeigt, öffnen Sie den XFCE-Desktop:

In Codespaces: Klicken Sie auf den Reiter Ports und öffnen Sie den Port 6080 im Browser.

Lokal (Docker): Öffnen Sie http://localhost:6080/vnc.html?autoconnect=true&resize=scale im Browser.

(Hinweis: Wer Playwright stattdessen lieber lokal auf seinem eigenen Host-Rechner installieren möchte, findet die offizielle Anleitung hier: Playwright Installation Guide)

2. Tests aufzeichnen (CodeGen)
Mit Playwright CodeGen können Sie Klicks im Browser direkt als Code aufzeichnen lassen.

Doppelklicken Sie auf dem virtuellen Desktop auf Playwright Codegen.

Geben Sie im sich öffnenden Browser die URL https://demo.playwright.dev/todomvc/ ein.

Führen Sie Aktionen aus (Todos eintragen, abhaken). Der Playwright Inspector zeichnet alles als fertigen TypeScript-Code auf.

Kopieren Sie den generierten Code und fügen Sie ihn in die Datei Uebung5/tests/todo.spec.ts ein.

3. Manuelle Tests schreiben und Assertions hinzufügen
Beim manuellen Schreiben von Tests nutzen wir sogenannte Locators (z.B. getByPlaceholder, getByText, getByRole), um Elemente zu finden, und Assertions (expect), um Zustände zu prüfen.

Beispiel für einen manuellen Test in todo.spec.ts:

TypeScript
import { test, expect } from '@playwright/test';

test('Ein neues Todo wird hinzugefügt', async ({ page }) => {
  await page.goto('[https://demo.playwright.dev/todomvc/](https://demo.playwright.dev/todomvc/)');
  
  // Element finden und interagieren
  const newTodoInput = page.getByPlaceholder('What needs to be done?');
  await newTodoInput.fill('Mein erstes Todo');
  await newTodoInput.press('Enter');

  // Zustand prüfen (Assertion)
  await expect(page.getByText('Mein erstes Todo')).toBeVisible();
});
4. Tests ausführen
Um Ihre geschriebenen Tests auszuführen, haben Sie auf dem Desktop zwei Möglichkeiten:

Mit grafischer Oberfläche (UI Mode): Doppelklicken Sie auf Playwright UI. Hier können Sie Tests einzeln starten und im Trace Viewer genau sehen, was passiert ist.

Im Terminal: Doppelklicken Sie auf Terminal (öffnet sich direkt in Uebung5) und tippen Sie: npx playwright test.

5. Aufgaben für Studierende
Nutzen Sie Uebung5/tests/todo.spec.ts für die folgenden Aufgaben. Starten Sie mit CodeGen, um ein Gefühl dafür zu bekommen, und schreiben Sie komplexere Prüfungen danach manuell.

Aufgabe 1: Erste einfache Tests (mit CodeGen)
Zeichnen Sie das Hinzufügen von drei neuen Todos auf.

Setzen Sie mindestens ein Todo auf "erledigt" (Checkbox anklicken).

Kopieren Sie den Code in Ihre Test-Datei.

Fügen Sie manuell eine Assertion (expect) hinzu, die prüft, ob der Zähler „items left“ (unten links in der App) den korrekten Text anzeigt.

Aufgabe 2: Löschen & Toggle-All (Manuell)
Schreiben Sie einen Test, der ein Todo via rotem "X" löscht (Tipp: das "X" erscheint erst beim Hovern. Nutzen Sie .hover()).

Testen Sie den "Toggle-All"-Pfeil (links neben dem Eingabefeld). Er soll alle Todos auf erledigt setzen.

Prüfen Sie den Button „Clear completed“ (entfernt alle erledigten Todos).

Aufgabe 3: Filterung (Manuell)
Prüfen Sie die Filter „Active“, „Completed“ und „All“ in der unteren Leiste.

Schreiben Sie einen Test, der verifiziert, dass beim Klick auf „Active“ keine erledigten Todos mehr sichtbar sind.

Aufgabe 4: Edge Cases (Komplexer)
Was passiert bei einer leeren Eingabe (nur Enter drücken)?

Prüfen Sie das Verhalten, wenn noch gar keine Todos existieren (der Button „Clear completed“ sollte unsichtbar sein). Verifizieren Sie dies mit toBeHidden().