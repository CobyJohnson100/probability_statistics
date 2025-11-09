"""Set theory operations.

Keep implementation comments minimal; detailed documentation lives in
`documentation/set_theory.md`.
"""

class SetOperations:
    """Utility methods for basic set operations."""

    @staticmethod
    def union(*sets):
        """Return the union of the provided sets."""
        if not sets:
            return set()
        result = set(sets[0])
        for s in sets[1:]:
            result.update(s)
        return result

    @staticmethod
    def intersection(*sets):
        """Return the intersection of the provided sets."""
        if not sets:
            return set()
        result = set(sets[0])
        for s in sets[1:]:
            result.intersection_update(s)
        return result

    @staticmethod
    def complement(s, universal):
        """Return elements in `universal` that are not in `s`."""
        if universal is None:
            raise ValueError("universal set must be provided")
        return set(universal) - set(s)


def union(*sets):
    """Return the union of the provided sets."""
    return SetOperations.union(*sets)


def intersection(*sets):
    """Return the intersection of the provided sets."""
    return SetOperations.intersection(*sets)


def complement(s, universal):
    """Return elements in `universal` that are not in `s`."""
    return SetOperations.complement(s, universal)

if __name__ == "__main__":
    # Demonstration examples
    print("Set Theory Operations Demonstration")
    print("=" * 40)

    # Example sets
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    C = {4, 5, 6, 7}

    print(f"Set A: {A}")
    print(f"Set B: {B}")
    print(f"Set C: {C}")
    print()

    # Union examples
    print("Union Operations:")
    print(f"A ∪ B = {union(A, B)}")
    print(f"A ∪ B ∪ C = {union(A, B, C)}")
    print(f"A ∪ ∅ = {union(A, set())}")
    print()

    # Intersection examples
    print("Intersection Operations:")
    print(f"A ∩ B = {intersection(A, B)}")
    print(f"A ∩ B ∩ C = {intersection(A, B, C)}")
    print(f"A ∩ ∅ = {intersection(A, set())}")
    print()

    # Using the class methods
    print("Using SetOperations class:")
    print(f"SetOperations.union(A, B) = {SetOperations.union(A, B)}")
    print(f"SetOperations.intersection(A, B) = {SetOperations.intersection(A, B)}")
    # Define a universal set for demonstration of complements
    U = set(range(1, 9))
    print(f"Universal set U = {U}")
    print(f"Complement of A w.r.t U = {complement(A, U)}")
