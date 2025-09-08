# MSCS532_Assignment1

Python **Insertion Sort (monotonically decreasing order)**

## Files
- `insertion_sort.py` — implementation + CLI runner
- `tests/test_insertion_sort.py` — simple pytest-style tests (can also be run directly)
- `README.md` — how to run and how to create the 3 commits
- `.gitignore` — standard Python ignores
- `requirements.txt` — empty for now (no external deps)

## Quick Run
```bash
python insertion_sort.py --arr 5 2 9 1 5 6
# expected -> 9 6 5 5 2 1
```

Or read from stdin (space/comma separated):
```bash
echo "3, -1, 3, 2, 10" | python insertion_sort.py
# expected -> 10 3 3 2 -1
```

## Tests
```bash
python -m tests.test_insertion_sort
```
(or `pytest` if you have it installed).

## GitHub: make 3 commits locally, then push
```bash
git init
git add .
git commit -m "feat: add insertion sort (descending) with cli"
# Make a small change (e.g., add docstring or extra test)
git add insertion_sort.py tests/test_insertion_sort.py
git commit -m "test: add more cases and clarifying docstring"
# Update README with run instructions or screenshots later
git add README.md
git commit -m "docs: expand README with run and test usage"

# create public repo named MSCS532_Assignment1 on GitHub, then:
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/MSCS532_Assignment1.git
git push -u origin main
```
