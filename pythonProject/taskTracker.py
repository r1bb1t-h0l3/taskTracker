#!/usr/bin/python3

import sys
import json

DATABASE_NAME = "taskDB.json"
NAME_KEY = "name"
DONE_KEY = "isDone"
TASKS_KEY = "allTasks"


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


def add(tasks):
    tasks.append({
        NAME_KEY: 'my first task',
        DONE_KEY: False
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
        add(tasks)
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

