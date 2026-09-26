#!/usr/bin/env python3
"""Define a verbose version of the built-in list class."""


class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print a notification."""
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Remove an item and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
