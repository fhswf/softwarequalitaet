# Übung 5: End-to-End-Testing mit Playwright

In dieser Übung lernen Sie, wie man moderne Webanwendungen mithilfe von **Playwright** automatisiert testet. Sie werden sowohl aufgezeichnete Tests mit dem **Playwright CodeGen** erstellen als auch eigene, komplexere E2E-Tests manuell programmieren und ausführen.

---

## 1. Playwright starten (Docker / Codespaces & Lokale Installation)

### Option A: Start über den Docker-Container (Empfohlen für GitHub Codespaces & Lokal)
Für diese Übung steht eine fertige Desktop-Umgebung (XFCE + noVNC) mit vorinstalliertem Playwright bereit:

1. Öffnen Sie ein Terminal und wechseln Sie in den Ordner `Uebung5`:
   ```bash
   cd Uebung5
   ```
2. Starten Sie den Container über das Startskript:
   ```bash
   ./run.sh
   ```
3. Öffnen Sie die grafische Oberfläche im Browser:
   * **Lokal:** Öffnen Sie [http://localhost:6080](http://localhost:6080) in Ihrem Browser.
   * **GitHub Codespaces:** Klicken Sie unten im Terminal-Bereich auf den Reiter **Ports**, suchen Sie den Port **6080** und klicken Sie auf das **Weltkugel-Symbol (Open in Browser)**.
4. Sie landen direkt auf dem Desktop. Alle Dateien, die Sie im Container unter `/workspace` (bzw. `/workspace/tests`) erstellen oder ändern, werden automatisch direkt in Ihrem `Uebung5`-Ordner gespeichert.
5. Zum Beenden drücken Sie im Terminal einmal `Ctrl + C`.

### Option B: Playwright lokal ohne Docker installieren (Optional)
Falls Sie Playwright direkt auf Ihrem eigenen Rechner ohne Docker nutzen möchten, benötigen Sie Node.js. Folgen Sie dazu der offiziellen Installationsanleitung auf der Playwright-Webseite:
* **Offizielle Anleitung:** [https://playwright.dev/docs/intro](https://playwright.dev/docs/intro)
* **Kurzform im Terminal:**
  ```bash
  npm init playwright@latest
  ```

---

## 2. Tests aufzeichnen mit Playwright CodeGen (Kurzanleitung)

Mit **CodeGen** können Sie Klicks und Eingaben direkt im Browser ausführen, während Playwright automatisch den passenden Testcode generiert.

### CodeGen starten
* **Über den Desktop:** Doppelklicken Sie auf dem VNC-Desktop auf das Symbol **Playwright Codegen**.
* **Über das Terminal:** Öffnen Sie das **Workspace Terminal** auf dem Desktop und führen Sie folgenden Befehl mit Ihrer gewünschten Ziel-URL aus:
  ```bash
  npx playwright codegen [https://demo.playwright.dev/todomvc/](https://demo.playwright.dev/todomvc/)
  ```

### Tests mit CodeGen aufzeichnen
1. Es öffnen sich zwei Fenster: das **Browserfenster** (mit der Webseite) und das **Playwright Inspector**-Fenster.
2. Klicken Sie im Browserfenster auf Elemente oder tippen Sie Text ein – jede Aktion wird sofort als Code im Inspector-Fenster aufgezeichnet.
3. **Assertions (Überprüfungen) hinzufügen:** Nutzen Sie die obere Werkzeugleiste im Inspector:
   * `Assert visibility` (prüft, ob ein Element sichtbar ist)
   * `Assert text` (prüft, ob ein bestimmter Text angezeigt wird)
   * `Assert value` (prüft den Wert eines Eingabefelds)
4. Klicken Sie auf **Record** (roter Punkt), um die Aufzeichnung zu beenden.
5. Kopieren Sie den generierten Code über das **Copy**-Symbol und fügen Sie ihn in eine `.spec.ts`-Datei im Ordner `/workspace/tests/` ein.

---

## 3. Tests manuell für Playwright schreiben

Manuelle Tests liegen im Ordner `tests/` und haben die Dateiendung `.spec.ts` (z. B. `tests/todo.spec.ts`).

### Grundstruktur eines Playwright-Tests
```typescript
import { test, expect } from '@playwright/test';

test('Neues Todo-Element hinzufügen und abhaken', async ({ page }) => {
  // 1. Webseite öffnen
  await page.goto('[https://demo.playwright.dev/todomvc/](https://demo.playwright.dev/todomvc/)');

  // 2. Element über Locator finden und Aktion ausführen
  const input = page.getByPlaceholder('What needs to be done?');
  await input.fill('Softwarequalität Übung 5 abschließen');
  await input.press('Enter');

  // 3. Ergebnis überprüfen (Assertion)
  await expect(page.getByTestId('todo-title')).toHaveText([
    'Softwarequalität Übung 5 abschließen'
  ]);
});
```

### Wichtige Befehle beim manuellen Schreiben
* **Navigation:** `await page.goto('https://...')` öffnet eine URL.
* **Locators (Elemente finden):**
  * `page.getByRole('button', { name: 'Submit' })` – findet Elemente anhand ihrer Rolle.
  * `page.getByPlaceholder('...')` – findet Eingabefelder über den Platzhaltertext.
  * `page.getByText('...')` – findet Elemente anhand ihres sichtbaren Textes.
* **Interaktionen:** `.click()`, `.fill('Text')`, `.press('Enter')`, `.check()`.
* **Assertions (Überprüfungen):**
  * `await expect(locator).toBeVisible()`
  * `await expect(locator).toHaveText('...')`
  * `await expect(locator).toHaveCount(3)`

---

## 4. Tests mit Playwright ausführen

Sie können Ihre Tests entweder interaktiv über die grafische Oberfläche oder direkt über das Terminal starten:

### Über die grafische Test-UI (Interaktiv)
* Doppelklicken Sie auf dem Desktop auf das Symbol **Playwright Test UI** (oder führen Sie im Workspace-Terminal `npx playwright test --ui` aus).
* Klicken Sie links neben einem Test auf das **grüne Play-Symbol (▶)**, um den Test auszuführen.
* Sie können jeden einzelnen Schritt auf der Zeitleiste anklicken, den DOM-Zustand vor und nach jedem Klick untersuchen und Fehler im Detail analysieren.

### Über das Terminal (Headless / CLI)
* Öffnen Sie das **Workspace Terminal** auf dem Desktop und führen Sie folgenden Befehl aus:
  ```bash
  npx playwright test
  ```
* Um einen HTML-Testbericht anzuzeigen:
  ```bash
  npx playwright show-report
  ```

---

## 5. Aufgabenstellung für die Übung

Bearbeiten Sie die folgenden Teilaufgaben auf der Beispiel-Anwendung [https://demo.playwright.dev/todomvc/](https://demo.playwright.dev/todomvc/) und speichern Sie Ihre Tests im Ordner `tests/`:

### Aufgabe 1: Einfache Tests mit CodeGen aufzeichnen
1. Starten Sie **Playwright Codegen** auf dem Desktop.
2. Zeichnen Sie einen einfachen Testablauf auf:
   * Fügen Sie **zwei neue Todo-Einträge** hinzu.
   * Markieren Sie das erste Todo als **erledigt (completed)**.
   * Prüfen Sie mit der Funktion **Assert text** im CodeGen-Inspector, dass unten die Anzeige `1 item left` erscheint.
3. Speichern Sie den aufgezeichneten Code in einer neuen Datei `tests/codegen-todo.spec.ts` und führen Sie ihn über die **Playwright Test UI** aus.

### Aufgabe 2: Komplexere Tests manuell schreiben
Erstellen Sie eine neue Datei `tests/manual-todo.spec.ts` und implementieren Sie die folgenden drei Testszenarien **manuell** ohne CodeGen:
1. **Filter-Logik testen (`Active` / `Completed`):**
   * Legen Sie drei Todos an und markieren Sie eines davon als erledigt.
   * Klicken Sie auf den Filter `Active` und prüfen Sie mit `expect(...).toHaveCount(2)`, dass nur die zwei offenen Einträge sichtbar sind.
   * Klicken Sie auf den Filter `Completed` und prüfen Sie, dass genau ein Eintrag sichtbar ist.
2. **Todo-Eintrag nachträglich bearbeiten:**
   * Legen Sie ein Todo an, führen Sie einen Doppelklick darauf aus (`await locator.dblclick()`), ändern Sie den Text und bestätigen Sie mit `Enter`.
   * Überprüfen Sie per Assertion, dass der geänderte Text in der Liste angezeigt wird.
3. **Erledigte Einträge löschen (`Clear completed`) & Reload-Persistenz:**
   * Markieren Sie ein Todo als erledigt und klicken Sie auf den Button `Clear completed`.
   * Laden Sie die Seite neu (`await page.reload()`) und überprüfen Sie, dass nur noch die offenen Todos vorhanden sind und das gelöschte Todo nicht wieder erscheint.