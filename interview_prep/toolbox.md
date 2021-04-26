## Solution to collapsing an array of integers into one integer

```
# Method solution
def mapInt (numList):
	result = map(str, numList)
	result = ''.join(result)
	return int(result)

# One-line solution
result = int(''.join(map(str, numList))
```

## Solution to generate a permuation of the alphabet

```
# Generate List
lst = [chr(i) for i in range(ord('A), ord('Z')]
# Permute List
list = Permutations(lst).random_element()
print(lst)
```
