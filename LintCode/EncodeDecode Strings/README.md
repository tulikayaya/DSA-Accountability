# Encode and Decode Strings

## Problem
Design an algorithm to encode a list of strings into a single string and decode it back to the original list.

The encoding should be reversible so that the original list of strings can be reconstructed exactly.

Example:

Input:
["neet","code","love","you"]

Encoded:
"4#neet4#code4#love3#you"

Decoded:
["neet","code","love","you"]

## Approach

Each string is encoded using the following format:

```
length#string
```

Where:
- `length` is the number of characters in the string
- `#` is a delimiter
- `string` is the original string

Example:

```
"neet" -> "4#neet"
"code" -> "4#code"
```

The encoded strings are concatenated together to produce the final encoded result.

### Why this works
Using the length allows us to correctly extract each string during decoding, even if the string itself contains special characters.

---

## Encoding Algorithm

1. Initialize an empty result string.
2. For each string in the list:
   - Compute its length.
   - Append `length + '#' + string` to the result.
3. Return the result.

Example:

```
["cat","dog"]

Encoded:
"3#cat3#dog"
```

---

## Decoding Algorithm

1. Traverse the encoded string using a pointer.
2. Read characters until `#` to determine the length of the next string.
3. Convert the length to an integer.
4. Extract the next `length` characters as the decoded string.
5. Move the pointer forward and repeat until the string ends.

---

## Python Implementation

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string)) + '#' + string
        
        return res


    def decode(self, s: str) -> List[str]:
        i, res = 0, []

        while i < len(s):
            characters = ""

            while s[i] != '#':
                characters += s[i]
                i += 1

            length = int(characters)
            i += 1

            res.append(s[i:i + length])
            i += length

        return res
```

---

## Time Complexity

Encoding:
```
O(n)
```

Decoding:
```
O(n)
```

Where `n` is the total number of characters across all strings.

---

## Space Complexity

```
O(n)
```

The encoded string and decoded list both require space proportional to the input size.

---

## Key Insight

The delimiter `#` separates the length from the string, while the length ensures that we read the exact number of characters needed for each decoded string.

This prevents ambiguity even if the strings contain special characters.