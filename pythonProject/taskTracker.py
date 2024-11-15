#!/usr/bin/python3

import sys
import json


DATABASE_NAME = "taskDB.json"
ID_KEY = "id"
NAME_KEY = "name"
DONE_KEY = "isDone"
PRIORITY_KEY = "priority"
TASKS_KEY = "allTasks"

def printStatus(status: bool) -> str:
    """
    Converts a task's status to a human-readable string.

    Args:
        status (bool): The status of the task (None, True, or False).

    Returns:
        str: "not started" if status is None, "done" if True, "in progress" if False.
    """

    if status is None:
        return "not started"
    elif bool(status):
        return "done"
    else:
        return "in progress"

def generateIdFromTasks(tasks: [dict]) -> int:
    """
    Generates a new unique task ID based on the existing tasks.

    Args:
        tasks (list): A list of task dictionaries.

    Returns:
        int: A new unique ID for the next task.
    """
    currentMaxID = 0
    for t in tasks:
        id = t[ID_KEY]
        if currentMaxID < id:
            currentMaxID = id
    return currentMaxID + 1


def loadTasks() -> [dict]:
    """
    Loads tasks from the JSON database file.

    Returns:
        list: A list of task dictionaries.
    """
    try:
        with open(DATABASE_NAME, 'r') as file:
            data = json.load(file)

        tasks = data[TASKS_KEY]
        for task in tasks:
            if PRIORITY_KEY not in task:
                task[PRIORITY_KEY] = 1

        return tasks
    except:
        return []


def saveTasks(tasks: [dict]):
    """
    Saves the current list of tasks to the JSON database file.

    Args:
        tasks (list): A list of task dictionaries.
    """
    tasksRecord = {
        TASKS_KEY: tasks
    }
    with open(DATABASE_NAME, 'w') as file:
        json.dump(tasksRecord, file, indent=4)


def add(tasks: [dict], taskName: str):
    """
    Adds a new task to the task list.

    Args:
        tasks (list): A list of task dictionaries.
        taskName (str): The name of the new task.
    """
    newTaskID = generateIdFromTasks(tasks)
    tasks.append({
        ID_KEY: newTaskID,
        NAME_KEY: taskName,
        DONE_KEY: None,
        PRIORITY_KEY: 1
    })
    print('added task: {} | ID: {}'.format(taskName, newTaskID))


def update(tasks: [dict], taskID: int, taskName: str) -> None:
    """
    Updates the name of a task.

    Args:
        tasks (list): A list of task dictionaries.
        taskID (int): The ID of the task to update.
        taskName (str): The new name for the task.
    """
    for t in tasks:
        id = t[ID_KEY]
        if id == taskID:
            t[NAME_KEY] = taskName
            print('updated task: {} | ID: {}'.format(taskName, taskID))
            return
    print(f"ID {taskID} doesn't exist")

def updatePriority(tasks: [dict], taskID: int, priority: int) -> None:
    """
    Updates the priority of a task.

    Args:
        tasks (list): A list of task dictionaries.
        taskID (int): The ID of the task to update.
        priority (int): The new priority level for the task.
    """
    for t in tasks:
        id = t[ID_KEY]
        if id == taskID:
            t[PRIORITY_KEY] = priority
            print(f"updated task priority. \nTaskID:{taskID}  |  Priority: {priority}")
            return
    print(f"ID {taskID} doesn't exist ")

def delete(tasks: [dict], taskID: int) -> None:
    """
    Deletes a task from the task list.

    Args:
        tasks (list): A list of task dictionaries.
        taskID (int): The ID of the task to delete.
    """
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


def markInProgress(tasks: [dict], taskID: int) -> None:
    """
    Marks a task as 'in progress'.

    Args:
        tasks (list): A list of task dictionaries.
        taskID (int): The ID of the task to mark as 'in progress'.
    """
    for t in tasks:
        id = t[ID_KEY]
        if id == taskID:
            t[DONE_KEY] = False
            print(f"task{taskID} successfully marked IN PROGRESS")
            return
    print("no such task ID")


def markDone(tasks: [dict], taskID: int) -> None:
    """
    Marks a task as 'done'.

    Args:
        tasks (list): A list of task dictionaries.
        taskID (int): The ID of the task to mark as 'done'.
    """
    for t in tasks:
        id = t[ID_KEY]
        if id == taskID:
            t[DONE_KEY] = True
            print(f"task{taskID} successfully marked DONE")
            return
    print("no such task ID")


def list(tasks: [dict]) -> None:
    """
    Prints all tasks in the task list.
    """
    for task in tasks:
        print(f"Task ID: {task[ID_KEY]}")
        print(f"Task: {task[NAME_KEY]}")
        print(f"Status: {printStatus(task[DONE_KEY])}")
        print(f"Priority: {task[PRIORITY_KEY]}")
        print('-' * 20)

def listInProgress(tasks: [dict]) -> None:
    """
    Prints all tasks that are 'in progress'.
    """
    taskFound = False
    for task in tasks:
        if task[DONE_KEY] == False:
            taskFound = True
            print(f"TaskID: {task[ID_KEY]}")
            print(f"Task: {task[NAME_KEY]}")
            print(f"Status: {printStatus(task[DONE_KEY])}")
            print(f"Priority: {task[PRIORITY_KEY]}")
            print("-" * 20)
    if taskFound == False:
        print("no tasks in progress")

def main():
    """
    Main function to handle user input and perform task operations.
    """
    if len(sys.argv) <= 1:
        print("no arguments detected")
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
        if len(sys.argv) == 3:
            markDone(tasks, int(sys.argv[2]))
        else:
            print("no valid input detected")
            exit(4)
    elif action == "list":
        if len(sys.argv) == 2:
            list(tasks)
        else:
            print("unknown action")
        exit(2)
    elif action == "list-in-progress":
        if len(sys.argv) == 2:
            listInProgress(tasks)
    elif action == "update-priority":
        if len(sys.argv) == 4:
            updatePriority(tasks, int(sys.argv[2]), int(sys.argv[3]))
        else:
            print("input priority")
            exit(5)
    saveTasks(tasks)

if __name__ == "__main__":
    main()

