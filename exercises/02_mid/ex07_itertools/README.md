# Exercise 07: itertools

## Learning Objectives

- Use `itertools.chain` to combine iterables
- Use `itertools.combinations` and `itertools.permutations`
- Use `itertools.groupby` for grouping sorted data
- Use `itertools.takewhile`, `itertools.cycle`, `itertools.islice`

## Instructions

Fix the functions in `exercise.py` to make all tests pass.

## Key itertools Functions

```python
import itertools

# chain: combine iterables
list(itertools.chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# combinations: unique subsets
list(itertools.combinations([1, 2, 3], 2))  # [(1,2), (1,3), (2,3)]

# permutations: ordered arrangements
list(itertools.permutations([1, 2], 2))  # [(1,2), (2,1)]

# groupby: group consecutive elements (data must be sorted!)
for key, group in itertools.groupby([1, 1, 2, 2], lambda x: x):
    print(key, list(group))

# takewhile: take while condition is True
list(itertools.takewhile(lambda x: x > 0, [1, 2, -1, 3]))  # [1, 2]

# cycle + islice: repeat and limit
list(itertools.islice(itertools.cycle([1, 2]), 5))  # [1, 2, 1, 2, 1]
```

## Run Tests

```bash
uv run pytest exercises/02_mid/ex07_itertools/ -v
```
