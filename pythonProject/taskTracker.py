#!/usr/bin/python3

import sys
import json

DATABASE_NAME = "taskDB.json"
ID_KEY = "id"
NAME_KEY = "name"
DONE_KEY = "isDone"
TASKS_KEY = "allTasks"

def generateIdFromTasks(tasks):
    currentMaxID = 0
    for t in tasks:
        id = t[ID_KEY]
        if currentMaxID < id:
            currentMaxID = id
    return currentMaxID+1


def loadTasks():
    try:
        with open(DATABASE_NAME, 'r') as file:
            data = json.load(file)

        return data[TASKS_KEY]
    except:
        return []


def saveTasks(tasks):
    tasksRecord = {
        TASKS_KEY: tasks
    }
    with open(DATABASE_NAME, 'w') as file:
        json.dump(tasksRecord, file, indent=4)


def add(tasks, taskName):
    tasks.append({
        ID_KEY: generateIdFromTasks(tasks),
        NAME_KEY: taskName,
        DONE_KEY: None
    })


def update():
    print("update")


def delete():
    print("delete")


def markInProgress():
    print("mark in progress")


def markDone():
    print("mark done")


def list():
    print("list")


def main():
    if len(sys.argv) <= 1:
        print("invalid arguments")
        exit(1)

    tasks = loadTasks()
    action = sys.argv[1]
    if action == "add":
        if len(sys.argv) == 3:
            add(tasks, sys.argv[2])
        else:
            print("no valid task input detected")
            exit(3)
    elif action == "update":
        update()
    elif action == "delete":
        delete()
    elif action == "mark-in-progess":
        markInProgress()
    elif action == "mark-done":
        markDone()
    elif action == "list":
        list()
    else:
        print("unknown action")
        exit(2)
    saveTasks(tasks)

if __name__ == "__main__":
    main()

