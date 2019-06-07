Add your answers to the Algorithms exercises here.

a) O(n).
Although N is cubed, the same output grows at the same rate for every input.

b)O(n^3).
There are three loops nesting dependent on N. This means the loops will grow exponentially with N. Large numbers make it more obvious.

c)O(n)
The function is recursive, but the recursion solely relies on bunnies(n). It will only grow when bunnies grow.

d) Use a binary search style algorithm.
We are provided the height of the building and can determine the safe egg dropping distance based off of it. If we start at the midway point and the egg breaks. We need to test the lower half, if it doesn't break, we can test the upper half. We would do this over and over until we know exactly how many floors it takes for the egg to break.
Binary search is O(log n), so this would match.
