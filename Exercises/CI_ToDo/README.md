# Praktikumsaufgabe - Continuous Integration zur Verbesserung von Softwarequalität

## Aufgabe

In dieser Praktikumsaufgabe befassen Sie sich mit dem Thema Continuous Integration (CI) im Kontext von Softwarequalität. Die Basis hierfür bildet eine einfache 'ToDo'-Anwendung, die auf GitHub unter folgendem Link bereitsteht: https://github.com/fhswf/todo.

Ihre Aufgabe besteht darin, eine GitHub-Action zu erstellen, die automatisierte Tests und eine Qualitätsprüfung mit SonarQube durchführt. 
**Bitte bearbeiten Sie die Aufgabe in Gruppen à 2–3 Personen!**

### Vorbereitung

1. **Clonen des Repositories**: Legen Sie (**als Gruppe!**) einen Clone des [Repositories https://github.com/fhswf/todo](https://github.com/fhswf/todo) an. 
   Die Übung des Umgang mit GitHub in einem Entwicklerteam ist eines der Ziele der Aufgabe. 
   > **Achtung**: Änderungen am Code sollten Sie **nicht** auf dem *main branch* vornehmen. Legen Sie für Ihre individuellen Aufgaben *feature branches* an und erstellen Sie jeweils *pull requests*!

1. **Verstehen Sie die Anwendung**: Die Anwendung beruht auf der Beispielanwendung im letzten Semester. Machen Sie sich mit dem Code vertraut und verstehen Sie, wie die Anwendung funktioniert. 
   Bevor Sie mit der Aufgabe fortfahren, sollte Ihnen klar sein, was die Anwendung tut und wie sie das tut. 
   <br>Finden Sie bereits einen Fehler? Falls ja, **beheben Sie ihn jetzt noch nicht**!

### Aufgabenschritte

1. **Erstellen Sie automatisierte Tests**: Der nächste Schritt ist die Erstellung automatisierter Tests. Hierfür sollten Sie zunächst Tests für wichtige Funktionen der Anwendung erstellen und diese lokal ausführen. Gewährleisten Sie dabei eine gute Testabdeckung und achten Sie auf unterschiedliche Testarten (Unit-Tests für das Backend, End2End-Tests für die gesamte Anwendung).
<br>Erstellen Sie unter anderem auch einen Testfall für die Aktualisierung des Status eines ToDos über den Status-Button. Dieser sollte fehlschlagen.

3. **Einrichten einer GitHub-Action**: Nun sollen Sie eine GitHub-Action erstellen. In dieser soll automatisch bei jedem Push oder Pull Request auf das Repository der erstellte Test-Suite durchgeführt werden.
   > **HINWEIS**: Sie müssen dazu in Ihrem Workflow MongoDB als zusätzlichen Service einfügen.
   ```yaml
   services:
     mongodb:
       image: mongo:4.4
       ports:
         - 27017:27017
   ```

5. **Integration von SonarQube**: Neben den Tests wollen wir auch eine statische Code-Analyse durchführen. Verwenden Sie hierzu die SonarQube-Instanz [hopper.fh-swf.de/sonarqube](https://hopper.fh-swf.de/sonarqube). 
   Dort können Sie sich mit Ihrem GitHub-Account anmelden und ein Projekt anlegen.
   Passen Sie die GitHub-Action so an, dass nach den Tests automatisch SonarQube gestartet wird und den Code analysiert.<br>
   > **Tipp**: Dafür gibt es fertige Actions. Schauen Sie gerne [github.com/fhswf/book_me](https://github.com/fhswf/book_me) nach, wie man sie verwendet.

   > **HINWEIS**: Sie benötigen im Workflow folgende zusätzliche Einstellung 

   ```yaml
       env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} # Needed to get PR information
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }} # Generate a token on SonarQube, add it to the secrets of this repo with the name SONAR_TOKEN (Settings > Secrets > Actions > add new repository secret)
          SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}
   ```

6. **Auswertung der Ergebnisse**: Schauen Sie sich die Ergebnisse der Tests und die SonarQube-Berichte an. Falls es Fehler gibt, sollten Sie diese jetzt beheben und den Prozess erneut durchführen.

7. **Dokumentation**: Im letzten Schritt sollen Sie Ihre Arbeit dokumentieren. Tragen Sie dazu in der Datei `BERICHT.md` die Namen Ihrer Teammitglieder ein. 
Präsentieren Sie in dieser Datei
-  Ihre Vorgehensweise, 
- die gewählten Lösungen, 
- alle Probleme, die Sie hatten und wie Sie diese gelöst haben, erklären und 
- die Ergebnisse der automatisierten Tests und SonarQube-Analysen.

### Abgabe

Zur Abgabe erstellen Sie bitte einen Pull-Request im [Original-Repository https://github.com/fhswf/todo](https://github.com/fhswf/todo).

### Lernziele

- Kenntnisse in der Verwendung von GitHub und GitHub Actions
- Vertiefen Ihrer Kenntnisse in der Erstellung automatisierter Tests
- Kenntnisse in der Verwendung von SonarQube zur Durchführung von Code-Qualitätsprüfungen
- Fähigkeit, Probleme zu identifizieren und Lösungen zu implementieren
- Fähigkeit, Ihre Arbeit in Form eines Berichts zu dokumentieren

### Bewertung

Die Bewertung Ihrer Arbeit basiert auf
- der Vollständigkeit und Funktionalität Ihrer GitHub-Action,
- der Qualität und Abdeckung Ihrer Tests,
- der korrekten Einbindung und Nutzung von SonarQube,
- der Qualität Ihrer Dokumentation,
- Ihrem Umgang mit auftretenden Problemen und Ihrer Fähigkeit, diese zu lösen.
