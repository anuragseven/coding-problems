class Solution:
    def getPairsCount(self, arr, n, k):
        m = [0] * (max(arr)+1)
 
    # Store counts of all elements in map m
        for i in range(0, n):
            m[arr[i]] += 1
 
        twice_count = 0
 
    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
        for i in range(0, n):
            if k-arr[i]>0 and k-arr[i]<len(m)and m[k - arr[i]]>0:
                twice_count += m[k - arr[i]]
 
        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
            if (k - arr[i] == arr[i]):
                twice_count -= 1
 
    # return the half of twice_count
        return int(twice_count / 2)