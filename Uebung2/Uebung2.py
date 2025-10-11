#WMME CRVA TMWN


"""
Aufgabe 1:
--------------
-process_tasks:
Nicht aus Namen oder Code direkt ersichtlich, welche Funktion dahintersteht

-Struktur von "tasks" nicht direkt ersichtlich

-cleanup:
Nur vom Betrachten der Funktion wird nicht klar, was sie macht/machen soll, anschauen des restlichen Codes erforderlich

-Wie/ in welcher Reihenfolge muss man die Funktionen aufrufen, dass am Ende eine vollständige Liste entsteht? (wann add(), wann process_tasks()?)

"""

"""
Aufgabe 2:
--------------

-Struktur 
    -Was sind Hauptfunktionen, was Hilfsfunktionen?

-Lesbarkeit
    -gut! Keine kryptischen oder doppeldeutigen Funktions-, Klassen- oder Variablennamen
    -Kongruenter und bekannter Stil (snake_case)
    -Umständliche Funktionsimplementierung (get_task_count()) ---> nicht genutzte Standard

-Verständlichkeit
    -Sinn teilweise unverständlich (calculate_task_average())
    -Rückgabewerte finden keinerlei Verwendung: Warum werden bools / ints / Strings zurückgegeben, wenn sie nie verwendet werden? 
    -Kommentar "Wichtig! Nicht verändern!". Botschaft redundant, besser: Warum soll man das nicht verändern?
    -"backup_tasks" ein Mülleimer zur Widerherstellung von Tasks oder Sammlung erledigter Tasks?
    -nach näherer Betrachtung des Codes: tasks und backup_tasks: Man könnte tasks als "unfinished_tasks" bezeichnen, um backup_tasks mehr Sinn zu geben.
    
-Dokumentation
    -Kommentare hinzufügen
        -Erklärung der Funktionen
        -Was kommt aus der Funktion raus? (Datentyp)
        -Erklärung der Struktur "tasks" und somit "task"

    -Vorhandene Kommentare wenig hilfreich: 
        -Kommentar "# Wichtig! Nicht verändern!" nicht hilfreich. Warum wird als task-ID eine Zufallszahl addiert? Bug? Tasks könnten auf diese Weise fälschlicherweise überschrieben werden. 
        -"TODO Kommentar" ohne Erklärung, was zu tun ist.

-Robustheit
    -verbesserungswürdig! Beispiele:
    -Ducktyping schwierig, z.B. bei task_id (später wird versucht, als id einen String zuzuweisen, was auch klappt [**korrigiert**])
    -backup_tasks wird nicht verwendet, Entfernung der "Leiche"

-Fehlervermeidung
    -Division durch 0 - Offensichtlichkeit
    -Rückgabewerte der Funkionen werden nicht behandelt
    -kein Error-handling 
    -Doppeldeutigkeit bei mark_done(), da uneindeutiger Zugriff auf Task über String

-Wartbarkeit
    -siehe unter "Dokumentation"
    -magic-numbers: 
        -Warum muss task ein Array sein und ist nicht eine eigene Container-Klasse oder ein Dictionary? Man muss sich immer in die Reihenfolge "eindenken". Verbesserungsmöglichkeiten: Dictionaries, Klasse oder index über Enum 
"""


### Dieses Skript soll eine textbasierte Aufgabenliste darstellen. Es kümmert sich um Eingabe, Ausgabe und einfaches Taskmanagement
### Autor: XYZ
### Version: v 0.9.7
### Datum: 03.10.25

import datetime
# import random # dont need that 

# index positions for elements of task array
NAME = 0
DUE_DATE = 1
PRIORITY = 2
DONE = 3
AUTHOR = 4
CREATION_DATE = 5

tasks = {} # dictionary, keys: unique ids as int; values: tasks: tasks as arrays
# dictionary, keys: unique ids as int; values: tasks as arrays
# serves as container for tasks marked 'done'
backup_tasks = {} 

## Main methods ##############################################################################

# Adds a task with an id in the global var 'tasks'. If task_id is not unique, existing tasks will be overwritten in either tasks or backup_tasks.
# id should be int or will get an unused id otherwise.
# returns task_id assigned
def add_task(name, due_date, priority=3, task_id=None):
    global tasks, backup_tasks
    if tasks is None:
        tasks = {}

    if task_id == None or not isinstance(task_id, int): 
        task_id = find_unique_task_id()
    task = [name, due_date, priority, False, "user1",
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M")]
    tasks[task_id] = task
    return task_id

# removes a task with a given id and returns true/false if successful or not
def remove_task(task_id):
    global tasks
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False

# marks the task done ("Erledigt") using a taskname
# TODO / BUG: if task_name exists twice, it marks all tasks done (maybe unintentionally)
# better: use its id!
def mark_done(task_name):
    global tasks
    for task_id, task in tasks.items():
        if task[NAME] == task_name:
            task[DONE] = True
    return "Erledigt"

# shows all tasks details
def show_tasks():
    global tasks
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[NAME]} {task[CREATION_DATE]} - bis {task[DUE_DATE]} - {'Erledigt' if task[DONE] else 'Offen'} Priorität {task[PRIORITY]} von {task[AUTHOR]}")



# # grabs random task_id and inverts weather task is done # WHY???? 
# # unfinished, makes no sense, intention not clear, not production ready
# def process_tasks():
#     rand_id = random.choice(list(tasks.keys()))
#     tasks[rand_id][DONE] = not tasks[rand_id][DONE]
#     return False
#     # TODO


## redundant, makes no sense at all
# def calculate_task_average():
#     total = sum(tasks.keys())
#     avg = total / len(tasks) if tasks else 0 # div by zero!!! 
#     return avg


# returns an array of tasks with a due date greater than today, sorted by due date
def upcoming_tasks():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    upcoming = sorted(
        [task for task in tasks.values() if task[DUE_DATE] >= today],
        key=lambda x: x[DUE_DATE] # changed from name
    )
    return upcoming

# pushes all tasks marked done into backup_tasks and clears it from tasks
def cleanup():
    global tasks
    global backup_tasks
    temp = {}
    for task_id, task in tasks.items():
        if not task[DONE]:
            temp[task_id] = task
        else: 
            backup_tasks[task_id] = task
    # if len(temp) == len(tasks): # doesnt make sense
    #     return
    # tasks.clear()
    # tasks.update(temp)
    tasks = temp

# returns number of tasks
def get_task_count():
    return len(tasks)


## Helper methods ############################################################################

# to find an int that is unique in both tasks and backup_tasks
def find_unique_task_id(): 
    global tasks
    global backup_tasks
    id = 0
    while id in tasks or id in backup_tasks: 
        id += 1
    return id



## Test procedure ############################################################################

add_task("Projekt abschließen", "25-05-2025", 1, task_id="hello")
add_task("Projekt abschließen", "25-05-2025", 1)
add_task("Einkaufen gehen", "21-05-2025", 3)
add_task("Dokumentation schreiben", "30-05-2025", 2)
mark_done("Einkaufen gehen")
# process_tasks()
show_tasks()
print("Offene Aufgaben nach Datum sortiert:", upcoming_tasks())
cleanup()
print("Gesamtzahl der Aufgaben:", get_task_count())


