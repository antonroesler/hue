# hue
A lightweight coammd line app to controll basic functionalities of phillips hue lights.

To install: navaigte to the root direcory /hue
```bash
$ pip3 install -e .
````
To show all lights that are accessible via the bridge, run:
```bash
$ hue all
```

To save a light in the command line app 
```bash
$ hue set -light <id> -name <name>
```
To turn a saved light on:
```bash
$ hue on -n <name>
```
