# Hints for Exercise 09: Type Hints and Annotations

## typed_identity
Simply `return value`.

## first_or_default
```python
return items[0] if items else default
```

## apply
```python
return func(value)
```

## filter_by_type
```python
return [item for item in items if isinstance(item, target_type)]
```

## zip_to_dict
```python
return dict(zip(keys, values))
```

## flatten_optional
```python
return [item for item in items if item is not None]
```
