# Day 7 – Inheritance & Encapsulation

## Topics Covered
- Single inheritance
- Multiple inheritance
- Multi-level inheritance
- Hierarchical inheritance
- Hybrid inheritance
- Encapsulation
- Problem solving using OOP inheritance types

## Key Notes
- Inheritance allows a class (child) to reuse and extend another class (parent).
- Types:
  - Single: one parent → one child.
  - Multiple: one child inherits from multiple parents.
  - Multi-level: parent → child → grandchild chain.
  - Hierarchical: one parent → multiple children.
  - Hybrid: combination of the above.
- Encapsulation hides internal data and provides controlled access (via methods or properties).
- Use `self._attribute` or `self.__attribute` for protected/private-like behavior.

## Example Concepts / Pseudo-Code
- Base class `Vehicle`, child class `Car` and `Bike`.
- Multi-level inheritance: `Person` → `Employee` → `Manager`.
- Encapsulation example: private balance in `BankAccount` class with deposit/withdraw methods.

## What I Practiced
- Writing examples for each inheritance type.
- Accessing parent class methods from child classes.
- Using encapsulation to protect data and expose it via methods.

## Reflection
- Inheritance helps reduce code duplication and organize related classes.
- Encapsulation is important for security and clean design.
- I need more practice designing small class hierarchies for real scenarios.
