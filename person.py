import numpy as np
import load_names
import random
"""
This files includes all functionality for the class Person.
The Person class stores the name, age, weight, and height of a person.
create_persons_list provides a way to randomly create a list of dummy persons.
This is mainly meant to make testing easier.

Complete, the rest of the Person class and the function create_persons_list.
"""

# NAMES is a list or array with common first names.
NAMES = load_names.load_names()  # Variables in the global namespace should be capitalized.

class Person():
    """
    Here, you will create the class Person.

    The __init__ method is already given and it is not allowed to create new object attribute (self.some_name = ...).

    Add all the needed (magic) methods described in the grading criteria.
    This includes a method such that printed objects are readable for the end user.
    Also, this class should also be made:
    comparable, sortable, subscriptable, iterable, and castable (to float, int, and string)
    """
    def __init__(self, name, age, height, weight):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight

    def __repr__(self):
        return f"Person(Name: '{self._name}', Age: {self._age}, Height: {self._height}cm, Weight: {self._weight}kg)"

    def __str__(self):
        return self._name

    def __int__(self):
        return self._age

    def __float__(self):
        return float(self._age)

    def __getitem__(self, index):
        return [self._name, self._age, self._height, self._weight][index]

    def check_type(self, obj):
        if not isinstance(obj, Person):
            raise NotImplementedError('You must compare Person class with another Person class')

    def __eq__(self, other):
        self.check_type(other)
        return self._height == other._height

    def __gt__(self, other):
        self.check_type(other)
        return self._height > other._height

    def __lt__(self, other):
        return not self.__gt__(other) and not self.__eq__(other)

    def __le__(self, other):
        return not self.__gt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

def create_persons_list(n=10):
    person_list = []
    for _ in range(n):
        name = random.choice(NAMES)
        age = random.choice(range(18, 101))
        height = random.choice(range(150, 201))
        weight = random.choice(range(45, 101))
        person_list.append(Person(name, age, height, weight))
    return person_list


