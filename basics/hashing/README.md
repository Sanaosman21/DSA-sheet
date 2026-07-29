# DSA Revision Notes -- Hashing

## What is Hashing?

Hashing is a technique used to **pre-compute and store information** so
queries can be answered quickly.

Two phases: 1. Pre-computation 2. Fetching

------------------------------------------------------------------------

## Number Hashing

### Problem

Count the frequency of numbers in an array and answer multiple queries.

### Pseudo Code

``` text
INPUT array

Create frequency array

FOR every number
    frequency[number] = frequency[number] + 1

INPUT number of queries

FOR every query
    Read number
    Print frequency[number]
```

### Python

``` python
hash_arr = [0] * 13

for num in arr:
    hash_arr[num] += 1

q = int(input())

for _ in range(q):
    number = int(input())
    print(hash_arr[number])
```

### Complexity

-   Brute Force: O(Q × N)
-   Hashing: O(N + Q)

------------------------------------------------------------------------

## Character Hashing

### Why?

Lists use integer indices, so characters must be converted into numbers.

### ASCII

-   ord('a') = 97
-   ord('b') = 98
-   ord('f') = 102

### Mapping

``` text
a → 0
b → 1
c → 2
...
z → 25
```

Formula:

``` python
index = ord(character) - ord('a')
```

------------------------------------------------------------------------

## Character Hashing Pseudo Code

### Pre-computation

``` text
INPUT string

Create frequency array of size 26

FOR every character
    index = character - 'a'
    frequency[index] = frequency[index] + 1
```

### Fetching

``` text
INPUT number of queries

FOR every query
    Read character
    index = character - 'a'
    Print frequency[index]
```

### Python

``` python
s = input()

hash_arr = [0] * 26

for character in s:
    index = ord(character) - ord('a')
    hash_arr[index] += 1

q = int(input())

for _ in range(q):
    character = input()
    index = ord(character) - ord('a')
    print(hash_arr[index])
```

------------------------------------------------------------------------

## Key Ideas

-   Pre-computation: Store frequencies once.
-   Fetching: Answer queries instantly.
-   Number hashing uses the number directly as the index.
-   Character hashing first maps characters to indices (0--25).

------------------------------------------------------------------------

## Time Complexity

-   Pre-computation: O(N)
-   Each Fetch: O(1)
-   Total: O(N + Q)

------------------------------------------------------------------------

## Revision Checklist

-   [ ] What is hashing?
-   [ ] Pre-computation vs Fetching
-   [ ] Number hashing
-   [ ] Character hashing
-   [ ] ASCII values
-   [ ] ord()
-   [ ] Mapping: a→0 ... z→25
-   [ ] Frequency array
-   [ ] Time complexity
