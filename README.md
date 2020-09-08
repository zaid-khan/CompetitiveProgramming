# Competitive Programming
This is a repo of all competitive programming code. I have used Python to code.

## Points to remember:

1. There is always a big clue or hint given in the question. 

2. Think the way the question wants you to think. 

3. The loop starts with the assumption you have before it. So if you've already processed the first element and you're starting with the second one, assume this and write the loop.

## Python technicalities:

1. Always think of the negative sign in an index of list, as `len(list) - index` like for eg. 
   `li = [1, 2, 3, 4]`
   `li[-1] = li[len(li) - 1]`


## Handy Python Snippets:

1. Creating tuples by mapping multiple lists using the index position.
   Eg.
   ```
   list(zip('abc', [1, 2, 3, 4], 'wxyz')) 
   
   OUTPUT:
   [('a', 1, 'w'), ('b', 2, 'x'), ('c', 3, 'y')]
   ```

2. Iterating with `index` as well as the `number` using the `for-Each` type loop until the 2nd last element:
   Eg.
   ```
   for index, num in list(enumerate(nums))[:-1]:
       ...
   ```

3. Getting the `count` of a element in a list
   Eg.
   ```
   nums = [1, 1, 2, 2, 2, 3]
   search_element = 2
   count_of_search_element = sum(1 for elem in nums if elem == search_element)
   count_of_search_element                                                  
   
   OUTPUT:
   3
   ```