# User-Defined Classes

In Python, we've used built-in classes like `str`, `int`, and `list`. However, for many problems, we need to **create our own data objects** with specific attributes and behaviors. This is done by defining a class.

## The `Point` Class Example

Let's consider a mathematical point. A point in two dimensions is a single object defined by two numbers, its `x` and `y` coordinates.

![Object](resource/objectpic2.png)

A class for this would look like this:

```python
class Point:
    """Point class for representing and manipulating x,y coordinates."""

    def __init__(self):
        """Create a new point at the origin (0, 0)"""
        self.x = 0
        self.y = 0
```

### Understanding the Code

  * **`class Point:`**: This is the class header, defining a new class named `Point`.
  * **`"""..."""`**: This is the **docstring**, providing a brief description of the class.
  * **`__init__(self)`**: This is the special **initializer method** or **constructor**. It's automatically called whenever a new `Point` object is created.
  * **`self`**: This parameter automatically refers to the newly created object instance. It's used to set up the object's attributes.
  * **`self.x = 0`** and **`self.y = 0`**: These lines create **instance variables** (or attributes) named `x` and `y` for each `Point` object and set their initial values to `0`.

## Creating `Point` Objects

Creating an object from a class is called **instantiation**. The class name itself acts as a function (a constructor) that creates and initializes the new object.

```python
p = Point()  # Instantiate a new Point object
q = Point()  # Instantiate a second, separate Point object

print(p)
print(q)
print(p is q)
```

**Output:**

```
<__main__.Point object at 0x...>
<__main__.Point object at 0x...>
False
```

### Key Takeaways from Instantiation

  * Each call to `Point()` creates a **new and distinct object** in memory.
  * The `is` operator confirms that `p` and `q` are **different objects**, even though they have the same initial attribute values (`x=0`, `y=0`).
  * You can think of a class as a **factory** for creating objects. The constructor (`__init__`) is like the production line that sets the object's default state.