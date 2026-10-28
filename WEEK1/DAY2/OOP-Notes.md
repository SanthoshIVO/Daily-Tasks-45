# Object-Oriented Programming (OOP) Notes

Object-oriented programming organizes code around **objects**: values that
combine data (attributes or properties) with behavior (methods). A **class**
defines how objects of that type are created and what they can do.

```text
Class = blueprint
Object = a particular instance created from that blueprint
```

For example, `Student` can be a class, and `student1` can be one `Student`
object with its own name and student ID.

## The four pillars of OOP

### 1. Encapsulation

**Encapsulation** keeps an object's data and the operations on that data
together. It provides a controlled public interface so other code does not
need to depend on internal implementation details.

For example, instead of letting callers change a bank balance arbitrarily,
provide a `deposit` method that checks whether the amount is valid.

**Python:**

```python
class BankAccount:
    def __init__(self, opening_balance: float) -> None:
        self._balance = opening_balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero")
        self._balance += amount
```

The leading underscore in `_balance` communicates that it is intended for
internal use. Python does not strictly prevent code from accessing it.
`@property` provides a public read-only `balance` interface here; there is no
setter, so callers cannot assign `account.balance = ...` through that
interface.

**TypeScript:**

```typescript
class BankAccount {
  #balance: number;

  constructor(openingBalance: number) {
    this.#balance = openingBalance;
  }

  get balance(): number {
    return this.#balance;
  }

  deposit(amount: number): void {
    if (amount <= 0) {
      throw new Error("Deposit must be greater than zero");
    }
    this.#balance += amount;
  }
}
```

TypeScript's `#balance` is a JavaScript private field with runtime privacy.
TypeScript also supports the `private` modifier, which is enforced by
TypeScript's type checker, but `#balance` is the stronger runtime-private
form.

### 2. Inheritance

**Inheritance** lets a class reuse and specialize behavior from another
class. The child (or subclass) inherits from the parent (or base class).

**Python:**

```python
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> str:
        return f"Hello, I am {self.name}."


class Student(Person):
    def __init__(self, name: str, student_id: str) -> None:
        super().__init__(name)
        self.student_id = student_id
```

**TypeScript:**

```typescript
class Person {
  constructor(public name: string) {}

  introduce(): string {
    return `Hello, I am ${this.name}.`;
  }
}

class Student extends Person {
  constructor(name: string, public studentId: string) {
    super(name);
  }
}
```

Use inheritance for a genuine **is-a** relationship: a student is a person.
Avoid using it only to share a few unrelated methods; composition (objects
that contain or use other objects) may be a better fit.

### 3. Polymorphism

**Polymorphism** means that different object types can be used through a
common operation or interface, while each type provides its own behavior.

**Python** commonly supports this through method overriding and duck typing:

```python
class Dog:
    def speak(self) -> str:
        return "Woof"


class Cat:
    def speak(self) -> str:
        return "Meow"


def make_it_speak(animal: Dog | Cat) -> None:
    print(animal.speak())
```

Both objects work with `make_it_speak` because both provide `speak`.
Python does not require the classes to share a parent class for this example.

**TypeScript** can express the common shape with an interface:

```typescript
interface Speaker {
  speak(): string;
}

class Dog implements Speaker {
  speak(): string {
    return "Woof";
  }
}

class Cat implements Speaker {
  speak(): string {
    return "Meow";
  }
}

function makeItSpeak(animal: Speaker): void {
  console.log(animal.speak());
}
```

The function accepts any value that satisfies the `Speaker` interface.
TypeScript checks this compatibility while type-checking the program.

### 4. Abstraction

**Abstraction** exposes the important operations while hiding the details
of how they are implemented. An interface or abstract class can describe
what a type must provide without specifying every implementation detail.

**Python** can use the `abc` module to define an abstract base class:

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
```

`Shape` describes an operation that concrete shapes must implement.
Attempting to instantiate `Shape` without implementing `area` raises an
error.

**TypeScript** can use an interface or an abstract class:

```typescript
interface Shape {
  area(): number;
}

class Rectangle implements Shape {
  constructor(
    private width: number,
    private height: number,
  ) {}

  area(): number {
    return this.width * this.height;
  }
}
```

An interface describes a required shape and is used by the type checker.
An abstract class can also contain implementation and state that subclasses
inherit.

## Python and TypeScript OOP comparison

| Topic | Python | TypeScript |
|---|---|---|
| Class and instance | `class Student: ...`; create with `Student(...)` | `class Student { ... }`; create with `new Student(...)` |
| Constructor | `__init__(self, ...)` | `constructor(...)` |
| Current instance | Explicit `self` parameter | `this` keyword |
| Type checking | Dynamically typed at runtime; annotations help tools but are not generally enforced by Python itself | Static type checking before runtime; types are generally erased from emitted JavaScript |
| Encapsulation | `_name` is a convention; `__name` triggers name mangling, not strict privacy; properties provide controlled access | `public`, `protected`, and `private` are checked by TypeScript; `#name` has JavaScript runtime privacy |
| Inheritance | `class Child(Parent)` and `super()` | `class Child extends Parent` and `super(...)` |
| Interfaces | No built-in `interface` keyword; use protocols, abstract base classes, or duck typing | `interface` describes a type shape; classes can `implements` interfaces |
| Abstract classes | Use `abc.ABC` and `@abstractmethod` | Use the `abstract class` and `abstract` member keywords |
| Polymorphism | Often duck typing: an object works if it provides the needed behavior | Structural typing: compatible shapes are accepted; classes can also implement interfaces |
| Multiple inheritance | Supported for classes, with method resolution order rules | Classes extend only one class; a class can implement multiple interfaces |
| Properties | `@property` and optional setter methods | `get` and `set` accessors |

### Important notes about access modifiers

- In Python, `name` is public by convention, `_name` signals internal use,
  and `__name` is name-mangled to reduce accidental clashes. None of these
  provides Java-style strict private access control.
- In TypeScript, members are `public` by default. `private` and `protected`
  are checked by the TypeScript compiler. JavaScript `#field` is private at
  runtime and cannot be accessed as an ordinary property from outside.
- Access control is not a substitute for validating data. A public method
  such as `deposit` should still check its inputs.

## Choosing the right OOP feature

- Use **encapsulation** when an object's state needs controlled access or
  validation.
- Use **inheritance** when one type is truly a specialized form of another.
- Use **polymorphism** when different types should respond to the same
  operation in type-specific ways.
- Use **abstraction** when callers need to know what an object can do, but
  not how it does it.
- Consider **composition** when one object can use another without being a
  subtype of it. For example, a `Car` has an `Engine`; a car is not an
  engine.

## Small practice exercise

Implement a `Course` class and a `Student` class in both Python and
TypeScript:

1. Keep the course code as internal data.
2. Expose a read-only public course-code property.
3. Add an `enroll` operation that avoids enrolling the same student twice.
4. Define a shared operation such as `describe()` and implement it for both
   classes.
5. Identify which parts demonstrate encapsulation and polymorphism.
