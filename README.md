# hue
A lightweight coammd line app to controll basic functionalities of phillips hue lights.

To install: navaigte to the root direcory /hue
```bash
$ pip3 install -e .
````
Two environment variables must be set:
```
HUE_KEY = <The Key to communicate with the bridge>
HUE_BRIDGE_IP = <IP Address of the bridge>
```

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
