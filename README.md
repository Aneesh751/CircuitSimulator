# Circuit Simulator

The project is organized as Python packages. Each package exposes its public
classes through its `__init__.py` file:

```python
from circuit import Circuit
from components import Component
```

## Project classes

- `Component` stores a component name.
- `Circuit` stores a name and a list of `Component` objects.
- `GraphManager` holds a `Circuit`.
- `Simulator` holds a `GraphManager`.
- `MainGUI` creates and displays a `Canvas`; the canvas keeps a reference to
  its GUI.
- `main.py` starts the GUI.

The [circuit-simulator.puml](./circuit-simulator.puml) file contains a
PlantUML class diagram of these classes.

## Generate PlantUML

Install [`py2puml`](https://pypi.org/project/py2puml/) and run it from the
project root. Since the project root is not itself a Python package, inspect
each package separately:

```text
python -m pip install py2puml
py2puml --path components --namespace components
py2puml --path circuit --namespace circuit
py2puml --path graphs --namespace graphs
py2puml --path simulation --namespace simulation
py2puml --path gui --namespace gui
```

The checked-in diagram consolidates the classes from those package outputs and
shows the relationships between packages.

## Run the example

From the project root:

```text
python main.py
```

`GraphManager` and `Simulator` receive their dependencies through their
constructors.