# ToDo: a SUPER simple todo list manager

This project comes from my need for a basic todo list tracker, for me to easily add items, remove them, and display them through only a few keyboard presses.

Hence... ToDo. 

### Usage:

Adding a task
```
$> ./todo add some task
Tasks:
some task
```

Viewing tasks
```
$> ./todo
Tasks:
some task
```

Removing a task (uses Python's difflib)
```
$> ./todo remove some
Closest Match: some task
Task "some task" removed!
Tasks:
```
