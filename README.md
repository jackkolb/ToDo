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

------

I recommend making this into a symlink so you can access it anywhere with ```todo (commands)```:
```sudo link [location of this folder]/todo.sh /usr/bin/todo```


Alternative commands are a bit faster to use, and convenient for your fingers:

add, 'a':    `$> todo a some task`

remove, 'r': `$> todo r task`
