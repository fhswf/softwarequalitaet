# Aufgabenergebnisse

# A1
# Kommentare PRSE
# - Der Sinn des Programm ist eine ToDo/Aufgabenliste
# - Bei Funktionsdefinition (add_task): Die ersten beiden Parameter sind verpflichtend, die letzten beiden optional; Es wird ein standard Wert übermittelt
# - Die Taskid wird durch Länge+Zufallszahl bestimmt -> im idealfall werden IDs durchnummeriert
# Kommentare HAHR
# - remove_task: Was passiert, wenn es mehrere Aufgaben derselben ID gibt? Werden dann alle mit der gleichen ID gelöscht oder gibt es einen Fehler?
# - was macht process_tasks und warum steht da ein TODO, was muss da gemacht werden? Funktioniert es richtig?

# A2
# Kommentare PRSE
# - Positive Aspekte:
# -- Verwendung von Pflicht- und Optionalen Feldern
# -- Immer Verwendung des aktuellen Datums -> feste Struktur, allerdings warum wird das aktuelle Datum einfach angehangen am Ende vom Objekt?
# - Verbesserungen:
# --Kein "Random" bei der Erstellung TaskID
# -- calculate_task_average wird erstellt, aber nicht verwendet
# -- Mehr (sinnvolle) Kommentare zum besseren Verständnis des Codes
# -- Aufruf von add_task mit String als ID -> Erwartung: Fehlerausgabe/Hinweis
# Kommentare HAHR
# - Positive Aspekte:
# -- Variablennamen und Methodennamen sind prinzipiell verständlich / nachvollziehbar
# -- Code ist ausführbar
# - Verbesserungen:
# -- Funktionen kommentieren
# -- Einheitliches Task-Objekt
# -- Warum wird der Task noch in backup_tasks geschoben, aber dann nicht weiterverwendet? Welche Funktion hat backup_tasks?
# -- mark_done überarbeiten, damit es den korrekten Task als erledigt markiert
# -- Sinnvolle Reihenfolge für die Eigenschaften eines Tasks zur Ausgabe als Liste
# -- Warum wird True und False bei dem "Erledigt" und "Offen" gesetzt?

# -------------------------------------- Ab hier beginnt der Code der durch A3 überarbeitet wurde --------------------------------------

# HAHR: Deklaration von globalen Variablen, darunter einem Zähler für die Task-ID und einem einheitlichen Task-Objekt
import datetime
tasks = {}
task_counter = 1  # HAHR - Zähler für die Task-ID, der immer weiter hochgezählt wird


# Anlage von neuen Aufgaben
def add_task(name, due_date, priority=3):
    global task_counter
    # PRSE: Überprüft ob due_date ein String ist und wandelt diesen ggf. in ein Datum um
    if isinstance(due_date, str):
        due_date = datetime.datetime.strptime(due_date, "%d-%m-%Y").date()
    elif isinstance(due_date, datetime.datetime):
        due_date = due_date.date()
    elif not isinstance(due_date, datetime.date):
        print("Fehler: Ungültiges Datum")
        return None
    # HAHR - Einheitliches Task-Objekt erstellen und dann den Task Counter immer um 1 erhöhen, um eine einheitliche ID zu gewährleisten
    task_id = task_counter
    task_counter += 1
    task = {
        "name": name,
        "due_date": due_date,
        "priority": priority,
        "done": False,
        "user": "user1",
        "created_at": datetime.datetime.now()
    }
    tasks[task_id] = task
    return task_id


# Löschen von Aufgaben
def remove_task(task_id):
    global tasks
    if task_id in tasks:
        # HAHR - Löschen einer Aufgabe mit der entsprechenden ID
        del tasks[task_id]
        return True
    print("Fehler: Task-ID nicht gefunden.")
    return False


# Aufgaben als "erledigt" markieren
def mark_done(task_id):
    global tasks
    if task_id in tasks:
        tasks[task_id]["done"] = True  # PRSE: Aufgabe auf "erledigt" setzen
        return "Erledigt"
    return "Nicht gefunden"


# Anzeige von Aufgaben
def show_tasks():
    global tasks
    if not tasks:
        print("Keine Aufgaben vorhanden.")
        return
    # PRSE: Zeigt alle Aufgaben sortiert nach task
    for task_id, task in sorted(tasks.items()):
        status = "Erledigt" if task["done"] else "Offen"
        due = task["due_date"].strftime("%d-%m-%Y") if isinstance(
            task["due_date"], (datetime.date, datetime.datetime)) else task["due_date"]
        print(
            f"{task_id}: {task['name']} "
            f"(Prio {task['priority']}) - bis {due} - {status}"
        )


# Zukünftige Aufgaben
def upcoming_tasks():
    today = datetime.date.today()
    upcoming = [
        task for task in tasks.values()
        if isinstance(task["due_date"], (datetime.date, datetime.datetime)) and task["due_date"] >= today and not task["done"]
    ]
    # PRSE: Zeigt alle Aufgaben, sortiert nach dem Fälligkeitsdatum
    upcoming = sorted(upcoming, key=lambda x: x["due_date"])
    output_lines = [""]
    for task in upcoming:
        due = task["due_date"].strftime("%d-%m-%Y")
        output_lines.append(
            f"  - {task['name']} (Prio {task['priority']}) - bis {due} - Offen")
    return "\n".join(output_lines)


# Löscht alle erledigten Aufgaben
def cleanup():
    global tasks
    temp = {tid: t for tid, t in tasks.items() if not t["done"]}
    tasks.clear()
    tasks.update(temp)


# Zählt alle Aufgaben
def get_task_count():
    return sum(1 for task in tasks.values() if not task["done"])


# Testaufrufe
add_task("Projekt abschließen", "25-05-2026", 1)
add_task("Neues Projekt erstellen", "22-05-2026", 1)
add_task("Projekt abschließen", "25-05-2026", 2)
add_task("Einkaufen gehen", "21-05-2026", 3)
add_task("Dokumentation schreiben", "30-05-2026", 2)
mark_done(2)
show_tasks()
print("Offene Aufgaben nach Datum sortiert:", upcoming_tasks())
cleanup()
print("Gesamtzahl der offenen Aufgaben:", get_task_count())
