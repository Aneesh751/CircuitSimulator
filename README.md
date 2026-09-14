# Circuit Simulator

This project is organized as Python packages. Each folder contains an
`__init__.py` file so its public classes can be imported from the package:

```python
from circuit import Circuit
from components import Component
```

## Basic OOP example

- `Component` stores a name and has a `describe()` method.
- `Circuit` stores `Component` objects in a list.
- `GraphManager` receives a `Circuit` object.
- `Simulator` receives a `GraphManager` object.
- `MainWindow` receives a `Simulator` object.
- `main.py` creates the objects and connects them together.

This demonstrates classes, constructors, attributes, methods, imports,
composition, and passing objects into other objects without adding simulation
rules yet.

## Run the example

From the project root:

```text
python main.py
```

The important pattern is that each object receives the object it needs in its
constructor instead of creating it internally.