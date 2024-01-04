import numpy as np
import load_names
import random

# NAMES is a list or array with common first names.
NAMES = load_names.load_names()

class Person():
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


