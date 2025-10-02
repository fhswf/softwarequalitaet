#LNBT & JNHR

#Aufgabe 1
#tasks ist konstatnt aber klein geschrieben und warum ist sie als none deklariert, obwohl es dann weiter unten wieder als array deklariert wird
#tasks und backup_tasks wird immerwieder in den funktionen als global deklariert
#Tasks_id wird nicht vernünftig geprüft
#die Tasks id kann doppelt vorkommen und ist auch nicht einheitlich geregelt
#in mark_done wird die task_id abgefragt obwohl sie nicht verwendet wird
#bei mark_done wird ein string zurück gegeben, obwohl ein boolean gefordert wird
#in show_tasks sind die attribute nicht nachvollziehbar
#sinn von process_task nicht nachvollziehbar, vor allem unter berücksichtigung des randomizers
#task average berechnet den durchschnitt der id, was absolut keinen einsatzpunkt hat, wenn die id manuell gesetzt werden kann und teilweise strings enthält
#cleanup löscht nur nicht abgeschlossene tasks
#get tasks count ist nur eine verkomplizierte version von len(tasks)

#Aufgabe 2
#saubere deklaration der globalen variablen(und groß schreiben, damit man sie wieder erkennt)
#globale Variablen müssen nicht in jeder Funktion aufgerufen werden, sonst bräuchte man ja keine Globalen
#die Möglichkeit entfernen, die Ids manuell zu setzten und sie fest einer Task zuweisen. Außerdem längere Ids
#Task besser als struct als als array, weil es die zugriffe vereinfacht
#get_task_count vereinfachen oder löschen
#cleanup() korrigieren und lesbarer schreiben
#der datumsvergleich ist nicht für alle formate geeignet, besser mit datetime arbeiten
#process_tasks() überarbeiten oder löschen


import datetime
import random

tasks: dict[int, list] = {}  #klare typzuweisung der schlüssel und werte
backup_tasks: dict[int,list] = {} 
task_id_counter = 1  #Zähler für die Task IDs 


def add_task(name, due_date, priority=3):
#    global tasks, backup_tasks #neue globalen weden nicht in jeder funktion gebraucht
#   if tasks is None: #Wird nicht gebraucht, da tasks schon initialisiert ist
#        tasks = {} #Wird nicht gebraucht, da tasks schon initialisiert ist

    global task_id_counter    #Zähler für die Task IDs
    task_id_counter += 1 
    task_id =task_id_counter #Automatische Zuweisung der Task ID

    task = [name, datetime.datetime.strptime(due_date,"%d-%m-%Y"), priority, False, "user1", #für den Vergleich in upcoming_tasks wird das Datum in ein datetime Objekt umgewandelt
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M")]
    tasks[task_id] = task
    backup_tasks[task_id] = task
    return task_id


def remove_task(task_id):
#    global tasks #neue globalen weden nicht in jeder funktion gebraucht
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False


def mark_done(task_id): #es wird nach task_id und nicht nach name gefragt
#    global tasks #neue globalen weden nicht in jeder funktion gebraucht
    for task in tasks.items():  
        if task[0] == task_id:
            task[3] = True
    return True #sollte boolean zurückgeben, ob die aufgabe gefunden und als erledigt markiert wurde


def show_tasks():
#    global tasks #neue globalen weden nicht in jeder funktion gebraucht
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")


#def process_tasks(): #es gibt keinen sinnvollen Einsatzpunkt für diese Funktion
#    rand_id = random.choice(list(tasks.keys()))
#    tasks[rand_id][3] = not tasks[rand_id][3]
#    return False
#    # TODO


#def calculate_task_average(): #es gibt keinen sinnvollen Einsatzpunkt für diese Funktion
#    total = sum(tasks.keys())
#    avg = total / len(tasks) if tasks else 0
#    return avg


def upcoming_tasks():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    upcoming = sorted(
        [task for task in tasks.values() if task[1] >= today],
        key=lambda x: x[0]
    )
    return upcoming


def cleanup():
#    global tasks #neue globalen weden nicht in jeder funktion gebraucht
    temp = {}
    for task_id, task in tasks.items():
        if task[3]: #nur offene aufgaben werden behalten
            temp[task_id] = task
 #   if len(temp) == len(tasks):  #erfüllt keinen sinnvollen Zweck
 #      return       
    tasks.clear()
    tasks.update(temp)


def get_task_count():
    return sum(1 for _ in tasks) if tasks else 0


add_task("Projekt abschließen", "25-05-2025", 1) #id wird automatisch gesetzt
add_task("Projekt abschließen", "25-05-2025", 1)
add_task("Einkaufen gehen", "21-05-2025", 3)
add_task("Dokumentation schreiben", "30-05-2025", 2)
mark_done("Einkaufen gehen")
# process_tasks()
show_tasks()
print("Offene Aufgaben nach Datum sortiert:", upcoming_tasks())
cleanup()
print("Gesamtzahl der Aufgaben:", get_task_count())