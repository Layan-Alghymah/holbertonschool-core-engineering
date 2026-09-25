#!/usr/bin/env python3


class Animal:
    """Represent a generic animal."""

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog."""

    def speak(self):
        """Return the sound of a dog."""
        return "Woof"


class Cat(Animal):
    """Represent a cat."""

    def speak(self):
        """Return the sound of a cat."""
        return "Meow"


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())
