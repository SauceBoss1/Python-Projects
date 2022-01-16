def search(l, x, i, k):
    """Searches for an occurrence of x in list l, from position i to position k - 1 inclusive,
    using recursion."""
    # YOUR CODE HERE
    j = i + (k - i) //2
    lj = l[j]
    if k <= i:
      return None
    elif k == i + 1: #there are 2 elements left
      if lj != x:
        return None
      elif lj == x:
        return j
    elif k > i + 1:
      if lj < x:
        return search(l, x, j, k)
      elif lj > x:
        return search(l, x, i, j)
      elif lj == x:
        #return search(l, x, i, k - 1) if l[j - 1] == x else j
        ljLo = l[j-1]
        if ljLo == x:
          return search(l, x, i, k - 1)
        return j

def binary_search(l, x):
    """Helper function."""
    return search(l, x, 0, len(l))

print(binary_search([3, 4, 5, 6, 7, 8], 8))