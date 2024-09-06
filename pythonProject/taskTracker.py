#!/usr/bin/python3

import sys

def add():
    print("add")


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

    action = sys.argv[1]
    if action == "add":
        add()
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


if __name__ == "__main__":
    main()

