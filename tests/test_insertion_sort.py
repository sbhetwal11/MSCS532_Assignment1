# Simple tests for insertion_sort_desc

from insertion_sort import insertion_sort_desc

def _sorted_desc(a):
    return sorted(a, reverse=True)

def test_basic():
    data = [5, 2, 9, 1, 5, 6]
    assert insertion_sort_desc(data[:]) == _sorted_desc(data)

def test_duplicates_and_negatives():
    data = [3, -1, 3, 2, 10, -5, 0]
    assert insertion_sort_desc(data[:]) == _sorted_desc(data)

def test_already_descending():
    data = [9, 6, 5, 5, 2, 1]
    assert insertion_sort_desc(data[:]) == _sorted_desc(data)

def test_all_equal():
    data = [7, 7, 7, 7]
    assert insertion_sort_desc(data[:]) == _sorted_desc(data)

if __name__ == "__main__":
    # Minimal runner if pytest is not installed
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    print("All tests passed.")
