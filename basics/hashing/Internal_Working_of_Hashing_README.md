# Internal Working of Hashing

## Division Method
Formula:
```
Index = Number % Table Size
```
Example:
```
2->2
5->5
16->6
28->8
139->9
```

## Collision
Different elements map to the same index.
Example:
```
28 % 10 = 8
38 % 10 = 8
```

## Linear Chaining
Store colliding elements together in a chain.

```
Index 8
28
↓
38
↓
48
↓
18
```

## Worst Case
If all elements map to one index, searching becomes O(N).

## Interview Note
Python dictionaries handle collisions internally. Understand the concept; you usually don't implement it yourself.
