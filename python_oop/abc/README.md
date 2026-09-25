# Python - Abstract Classes & Interfaces

## Description

This project explores advanced object-oriented programming concepts in Python, focusing on abstract classes, interfaces, duck typing, multiple inheritance, mixins, and extending built-in classes.

The goal is to understand how Python can define common behaviors and contracts while allowing different classes to provide their own implementations.

## Learning Objectives

By completing this project, I learned how to:

- Create abstract base classes using `ABC`
- Define abstract methods using `@abstractmethod`
- Implement subclasses that follow an abstract contract
- Apply interface-like design in Python
- Understand and use duck typing
- Work with multiple inheritance
- Use mixins to add reusable behavior
- Extend built-in Python classes while preserving their functionality

## Requirements

- Ubuntu 20.04
- Python 3.8
- All files start with `#!/usr/bin/env python3`
- All files are executable
- Code follows PEP 8 style guidelines
- All modules, classes, and functions contain documentation strings
- Only the Python standard library is used unless otherwise specified

## Project Structure

### 0. Abstract Animal Class and its Subclasses

Introduces abstract base classes using an `Animal` class with an abstract `sound()` method.

The `Dog` and `Cat` subclasses provide their own implementations of the required method.

### 1. Shapes, Interfaces, and Duck Typing

Explores abstract interfaces and duck typing by defining common behavior for different shape objects.

### 2. The Enigmatic FlyingFish - Exploring Multiple Inheritance

Demonstrates how a class can inherit behavior and attributes from multiple parent classes.

### 3. The Mystical Dragon - Mastering Mixins

Introduces mixins as a way to add reusable functionality to classes without creating a traditional inheritance hierarchy.

### 4. Extending the Python List

Demonstrates how built-in Python classes can be extended by creating a custom class based on `list`.

## Key Concepts

### Abstract Classes

Abstract classes define methods that subclasses are required to implement. They can be created using Python's `abc` module.

### Abstract Methods

Methods decorated with `@abstractmethod` define required behavior for subclasses.

### Duck Typing

Duck typing focuses on what an object can do rather than its specific class or inheritance hierarchy.

### Multiple Inheritance

Multiple inheritance allows a class to inherit functionality from more than one parent class.

### Mixins

Mixins are small classes designed to provide reusable functionality to other classes through inheritance.

## Repository

**GitHub repository:** `holbertonschool-core-engineering`  
**Directory:** `python_oop/abc`
