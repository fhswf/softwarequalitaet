""""
A1
Kommentare PRSE
- Der Sinn des Programm ist eine ToDo/Aufgabenliste
- Bei Funktionsdefinition (add_task): Die ersten beiden Parameter sind verpflichtend, die letzten beiden optional; Es wird ein standard Wert übermittelt
- Die Taskid wird durch Länge+Zufallszahl bestimmt -> im idealfall werden IDs durchnummeriert

Kommentare HAHR
- remove_task: Was passiert, wenn es mehrere Aufgaben derselben ID gibt? Werden dann alle mit der gleichen ID gelöscht oder gibt es einen Fehler?
- was macht process_tasks und warum steht da ein TODO, was muss da gemacht werden? Funktioniert es richtig?
"""

""""
A2
Kommentare PRSE
- Positive Aspekte:
-- Verwendung von Pflicht- und Optionalen Feldern
-- Immer Verwendung des aktuellen Datums -> feste Struktur, allerdings warum wird das aktuelle Datum einfach angehangen am Ende vom Objekt?
-Verbesserungen:
--Kein "Random" bei der Erstellung TaskID
-- calculate_task_average wird erstellt, aber nicht verwendet
-- Mehr (sinnvolle) Kommentare zum besseren Verständnis des Codes
-- Aufruf von add_task mit String als ID -> Erwartung: Fehlerausgabe/Hinweis


Kommentare HAHR
- Positive Aspekte:
-- Variablennamen und Methodennamen sind prinzipiell verständlich / nachvollziehbar
-- Code ist ausführbar

Verbesserungen:
- Funktionen kommentieren
- Einheitliches Task-Objekt
- Warum wird der Task noch in backup_tasks geschoben, aber dann nicht weiterverwendet? Welche Funktion hat backup_tasks?
- mark_done überarbeiten, damit es den korrekten Task als erledigt markiert
- Sinnvolle Reihenfolge für die Eigenschaften eines Tasks zur Ausgabe als Liste
- Warum wird True und False bei dem "Erledigt" und "Offen" gesetzt?
"""

import datetime
import random

tasks = None
backup_tasks = {}


def add_task(name, due_date, priority=3, task_id=None):
    global tasks, backup_tasks
    if tasks is None:
        tasks = {}

    if task_id == None:
        task_id = len(tasks) + random.randint(2, 7)  # Wichtig! Nicht verändern!
    task = [name, due_date, priority, False, "user1",
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M")]
    tasks[task_id] = task
    backup_tasks[task_id] = task
    return task_id


def remove_task(task_id):
    global tasks
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False


def mark_done(task_name):
    global tasks
    for task_id, task in tasks.items():
        if task[0] == task_name:
            task[3] = True
    return "Erledigt"


def show_tasks():
    global tasks
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")


def process_tasks():
    rand_id = random.choice(list(tasks.keys()))
    tasks[rand_id][3] = not tasks[rand_id][3]
    return False
    # TODO


def calculate_task_average():
    total = sum(tasks.keys())
    avg = total / len(tasks) if tasks else 0
    return avg


def upcoming_tasks():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    upcoming = sorted(
        [task for task in tasks.values() if task[1] >= today],
        key=lambda x: x[0]
    )
    return upcoming


def cleanup():
    global tasks
    temp = {}
    for task_id, task in tasks.items():
        if not task[3]:
            temp[task_id] = task
    if len(temp) == len(tasks):
        return
    tasks.clear()
    tasks.update(temp)


def get_task_count():
    return sum(1 for _ in tasks) if tasks else 0


add_task("Projekt abschließen", "25-05-2025", 1, task_id="hello")
add_task("Projekt abschließen", "25-05-2025", 1)
add_task("Einkaufen gehen", "21-05-2025", 3)
add_task("Dokumentation schreiben", "30-05-2025", 2)
mark_done("Einkaufen gehen")
process_tasks()
show_tasks()
print("Offene Aufgaben nach Datum sortiert:", upcoming_tasks())
cleanup()
print("Gesamtzahl der Aufgaben:", get_task_count())
