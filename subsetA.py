def subsetR(n, k):
    if n == 1:         #base case 1
        return 1
    if k == 0:         #base case 2
        return 1
    else:
        return subsetR(n-1,k-1) + subsetR(n-1,k)  #recursion
