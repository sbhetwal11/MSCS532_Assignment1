"""
Insertion Sort (descending / monotonically decreasing).

Time complexity:
  - Worst/Avg: O(n^2), Best: O(n) when already sorted descending.
Space: O(1) extra (in-place).
Usage:
  python insertion_sort.py --arr 5 2 9 1 5 6
  echo "3, -1, 3, 2, 10" | python insertion_sort.py
"""
from __future__ import annotations
import sys
from typing import List


def insertion_sort_desc(a: List[int]) -> List[int]:
    """
    Sort the list in-place into monotonically decreasing order using insertion sort.
    Returns the same list object (sorted).
    """
    # Iterate from the second element to the end
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        # Shift elements that are *smaller* than key to the right
        # Because we want descending order: larger elements should come first
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
    return a


def _parse_cli_args(argv: List[str]) -> List[int]:
    # If numbers are piped via stdin, prefer that
    if not sys.stdin.isatty():
        raw = sys.stdin.read().strip()
        if raw:
            # Allow spaces or commas
            parts = [p for p in raw.replace(",", " ").split() if p]
            return [int(x) for x in parts]

    # Otherwise parse after '--arr' as integers
    if "--arr" in argv:
        idx = argv.index("--arr")
        parts = argv[idx + 1:]
        if not parts:
            raise SystemExit("Provide numbers after --arr, e.g., --arr 5 2 9 1")
        return [int(x) for x in parts]

    raise SystemExit("Usage: python insertion_sort.py --arr 5 2 9 1 5 6  OR  echo \"3, -1, 3\" | python insertion_sort.py")


def main(argv: List[str]) -> None:
    arr = _parse_cli_args(argv)
    insertion_sort_desc(arr)
    print(" ".join(str(x) for x in arr))


if __name__ == "__main__":
    main(sys.argv[1:])
