#!/usr/bin/python3

import sys
import json


DATABASE_NAME = "taskDB.json"
ID_KEY = "id"
NAME_KEY = "name"
DONE_KEY = "isDone"
TASKS_KEY = "allTasks"

def printStatus(status):
    if status is None:
        return "not started"
    elif bool(status):
        return "done"
    else:
        return "in progress"


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


def add(tasks, taskName: str):
    newTaskID = generateIdFromTasks(tasks)
    tasks.append({
        ID_KEY: newTaskID,
        NAME_KEY: taskName,
        DONE_KEY: None
    })
    print('added task: {} | ID: {}'.format(taskName, newTaskID))


def update(tasks, taskID: int, taskName: str):
    for t in tasks:
        id = t[ID_KEY]
        if id == taskID:
            t[NAME_KEY] = taskName
            print('updated task: {} | ID: {}'.format(taskName, taskID))
            return
    print(f"Current ID {taskID} doesn't exist")


def delete(tasks, taskID: int):
    print(f"trying to delete task with taskId {taskID}")
    #i = index
    i = 0
    while i < len(tasks):
        print(f"i: {i}")
        task = tasks[i]
        id = task[ID_KEY]
        print(f"id: {id}")
        if id == taskID :
            tasks.pop(i)
            print("task {} successfully deleted".format(taskID))
            return
        else:
            print(f"taskId {taskID} is not equal to id {id}! go to the next iteration")
            i += 1
    print(f"Current ID {taskID} doesn't exist")


def markInProgress(tasks, taskID: int):
    for t in tasks:
        id = t[ID_KEY]
        if id == taskID:
            t[DONE_KEY] = False
            print(f"task{taskID} successfully marked IN PROGRESS")
            return
    print("no such task ID")


def markDone():
    print("mark done")


def list(tasks: [str]):
    for task in tasks:
        print(f"Task ID: {task[ID_KEY]}")
        print(f"Task: {task[NAME_KEY]}")
        print(f"Status: {printStatus(task[DONE_KEY])}")
        print('-' * 20)
    

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
        if len(sys.argv) == 4:
            update(tasks, int(sys.argv[2]), sys.argv[3])
        else:
            print("no valid input detected")
            exit(4)
    elif action == "delete":
        if len(sys.argv) == 3:
            delete(tasks, int(sys.argv[2]))
        else:
            print("no valid input detected")
            exit(4)
    elif action == "mark-in-progress":
        if len(sys.argv) == 3:
            markInProgress(tasks, int(sys.argv[2]))
        else:
            print("no valid input detected")
            exit(4)
    elif action == "mark-done":
        markDone()
    elif action == "list":
        if len(sys.argv) == 2:
            list(tasks)
    else:
        print("unknown action")
        exit(2)
    saveTasks(tasks)

if __name__ == "__main__":
    main()

