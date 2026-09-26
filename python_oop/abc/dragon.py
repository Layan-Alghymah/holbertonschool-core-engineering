#!/usr/bin/env python3
"""Demonstrate the use of mixins in Python."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon with swimming and flying abilities."""

    def roar(self):
        """Print a roaring message."""
        print("The dragon roars!")
