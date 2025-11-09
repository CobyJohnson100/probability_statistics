# Set Theory Basics

## Software Implementation

### Requirements
Before implementing set theory operations in code:
- Define a Set class or use built-in set data structures
- Implement basic operations: union, intersection, complement, difference
- Handle edge cases: empty sets, universal sets
- Consider performance for large sets
- Ensure mathematical correctness of operations

### Set Representation Alternatives
Consider the following three approaches for representing sets and storing associated data:

1. **Built-in Python Set**: Use Python's native `set` type for element storage. Store set metadata (name, description) in a separate dictionary or class attributes. Pros: Fast operations, memory efficient. Cons: No inherent ordering, limited metadata storage.

2. **List-based Custom Class**: Implement a Set class with elements stored in a sorted list. Include metadata fields directly in the class. Pros: Maintains element order, easy to extend with metadata. Cons: Slower operations for large sets due to linear search.

3. **Dictionary-based Custom Class**: Use a dictionary with elements as keys and optional metadata as values. Store set-level metadata as class attributes. Pros: Fast lookups, rich per-element metadata possible. Cons: Higher memory usage, no natural ordering.

### Chosen Implementation: Built-in Python Set
We'll implement a custom `Set` class that wraps Python's built-in `set` type for optimal performance and simplicity. The class will include metadata storage and provide flexible initialization methods.

### Data Input Methods
Users should populate sets from a JSON file. The project standard is to load elements from a JSON file that contains a JSON array of elements (for example: `[1, 2, 3, 2]`). Duplicates are automatically handled by the `Set` implementation.

Use the `Set.from_json(path)` factory to create a set from a JSON file:

```python
# elements.json content: [1, 2, 3, 2]
my_set = Set.from_json("elements.json")  # Result: Set({1, 2, 3})
```

This single canonical input method simplifies documentation and encourages consistent data-loading behavior across the codebase.

## Theoretical Foundations

### Overview
This document provides a brief introduction to fundamental concepts in set theory, which form the foundation for probability theory and statistics. We'll cover basic definitions and operations that are essential for understanding probabilistic concepts.

### Basic Definitions

#### Set
A **set** is a collection of distinct objects, called elements or members. Sets are typically denoted by curly braces `{}`.

**Examples:**
- Natural numbers: ℕ = {1, 2, 3, ...}
- Empty set: ∅ = {}
- Finite set: A = {1, 2, 3}

#### Element Membership
- `x ∈ A` means "x is an element of set A"
- `x ∉ A` means "x is not an element of set A"

#### Subset
A set A is a **subset** of set B (denoted A ⊆ B) if every element of A is also an element of B.

### Set Operations

#### Union
The **union** of sets A and B (denoted A ∪ B) is the set containing all elements that are in A, in B, or in both.

**Example:** If A = {1, 2, 3} and B = {2, 3, 4}, then A ∪ B = {1, 2, 3, 4}

#### Intersection
The **intersection** of sets A and B (denoted A ∩ B) is the set containing all elements that are in both A and B.

**Example:** If A = {1, 2, 3} and B = {2, 3, 4}, then A ∩ B = {2, 3}

#### Complement
The **complement** of set A (denoted Aᶜ or ¬A) is the set of all elements not in A, within a universal set U.

#### Difference
The **difference** of sets A and B (denoted A - B or A \ B) is the set containing elements in A but not in B.