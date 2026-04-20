# Hints for Exercise 07: Tuples

## create_tuple
Use parentheses with comma-separated values: `(1, 2, 3)`.

## get_first_last
Use index `0` for the first element and `-1` for the last: `(t[0], t[-1])`.

## unpack_coordinates
Use tuple unpacking: `x, y, z = point`, then return `(x, y, z)`.

## count_occurrences
Tuples have a `.count()` method just like lists: `t.count(value)`.

## concatenate_tuples
Use the `+` operator: `t1 + t2`.

## tuple_to_list_and_back
```python
lst = list(t)
lst.append(99)
return tuple(lst)
```
