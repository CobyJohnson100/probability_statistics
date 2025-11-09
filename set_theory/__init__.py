"""Package entrypoint for the `set_theory` package.

Re-export the main helpers from the module so existing imports like
`from set_theory import union` continue to work after moving the
module into a package directory.
"""
from .set_theory import SetOperations, union, intersection, complement

__all__ = ["SetOperations", "union", "intersection", "complement"]
