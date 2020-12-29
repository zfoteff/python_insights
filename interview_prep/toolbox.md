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
