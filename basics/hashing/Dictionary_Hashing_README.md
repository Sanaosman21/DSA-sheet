# Dictionary Hashing (Python)

## Why?
Array hashing wastes memory for very large values. A dictionary stores only the elements that actually appear.

## Structure
- Key → Element
- Value → Frequency

Example:
```
100 -> 2
50 -> 1
```

## Pseudo Code
```
INPUT array
Create empty dictionary frequency
FOR every element
    IF element exists
        Increase frequency by 1
    ELSE
        Add element with frequency 1
```

## Python
```python
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
```

## Shortcut
```python
freq[num] = freq.get(num, 0) + 1
```
Equivalent to the if-else version.

## Complexity
- Pre-computation: O(N)
- Fetching: O(1) average
- Total: O(N + Q)
