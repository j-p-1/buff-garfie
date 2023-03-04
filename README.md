# buff-garfie

Version: 1.0.0

Code that will open buff Garfield every second

## Install:

1. Click the green code button, then click download zip file.

2. Use some extraction utility on your machine to extract the code.

3. Open up a CMD window where the garfie code is and type the following below (Do not include > or $ (Terminal Cursor)!!!):

```
> pip install -r requirements.txt

> python garfie.py
```

or if you are running a machine with a different OS:

```
$ pip3 install -r requirements.txt

$ python3 garfie.py
```

## Bugs:

- I'm still trying to see if there is any bugs

Things that are not bugs:

- Window does not close upon clicking X. (Intentional by Design: Mainloop causes this so, the garf code must be executed before the event getter is executed.)
