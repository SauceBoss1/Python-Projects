import math
import random
def search(l, x, i, k):
    """Searches for an occurrence of x in list l, from position i to position k - 1 inclusive,
    using recursion."""
    # YOUR CODE HERE
    
    mid = i + (k - i) // 2
    if mid == len(l):
      return None
    lMid = l[mid]

    if k == i and l[mid] == x:
        return mid

    if k <= i:
        return None
    elif k == i + 1:
        lLo = l[mid - 1]
        if lLo != x and lMid != x:
            return None
        elif lLo == x and lMid == x:
            return mid - 1
        elif lMid == x:
            return mid
        elif lLo == x:
            return mid -1
    else:
        if lMid < x:
            return search(l, x, mid + 1, k)
        elif lMid > x:
            return search(l, x, i, mid)
        else:
            check_dupes = search(l, x, i, mid)
            if check_dupes == None:
                return mid
            else:
                return check_dupes


def binary_search(l, x):
    """Helper function."""
    return search(l, x, 0, len(l))

#print(binary_search([3, 4, 5, 6, 7, 8], 7))
#print(binary_search([1, 2, 3, 3, 3, 4, 5], 3))
#print(binary_search([1,2], 1))
l = [0, 6, 6, 7, 8, 11, 11, 12, 13, 16, 17, 18, 
20, 20, 22, 23, 25, 34, 34, 35, 38, 39, 46, 47, 
48, 50, 52, 52, 58, 58, 62, 64, 66, 69, 69, 69, 
70, 71, 73, 76, 80, 80, 80, 81, 82, 82, 82, 89, 
89, 90, 91, 95, 96, 97, 98, 98, 98, 98] #k: 99 i: 8
#l = [1, 2, 3, 4, 5, 6]
#print(binary_search([3, 4, 4, 5, 7, 7, 7,], 7))
#print(binary_search(l, 99))
print(binary_search([1,2], 1))


# #5 points.

# assert binary_search([1, 2, 3, 4, 5, 6], 2) == 1
# assert binary_search([1, 2, 3, 5, 6, 7], 4) is None

# #e did say, the earliest occurrence.
# assert binary_search([1, 2, 3, 3, 3, 4, 5], 3) == 2
# assert binary_search([1, 2, 2, 2, 2, 3, 4, 5], 2) == 1
# assert binary_search([1, 1, 1, 1, 1, 2, 3], 1) == 0

def random_tester():
    for _ in range(1000):
        n = random.randint(10, 100)
        l = list(random.choices(list(range(100)), k=n))
        l.sort()
        k = random.randint(0, 99)
    return l, k

l, x = random_tester()

# print(l,x)
# print(binary_search(l, x))