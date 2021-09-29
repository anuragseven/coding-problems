# You have given a list of q queries and for every query, you are given an integer N.
# The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

class Solution:
    def threeDivisors(self, queries):
        primes = self.sieveOfE(round(max(queries) ** 0.5))

        primes = [num ** 2 for num in primes]
        result = []

        for query in queries:
            if query >4:

                i = self.binarySearch(primes, query)
                result.append(i + 1)
            else:
                result.append(0)

        return result

    def sieveOfE(self, N):

        primes = [True for i in range(N + 1)]

        for i in range(2, int(N ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, N + 1, i):
                    primes[j] = False
        if primes == []:
            return []
        result = []
        for i in range(2, N + 1):
            if primes[i]:
                result.append(i)
        return result

    def binarySearch(self, arr, X):
        l = 0
        h = len(arr) - 1

        while l <= h:
            mid = l + (h - l) // 2
            if arr[mid] == X:
                return mid

            if mid > l and arr[mid] > X and arr[mid - 1] < X:
                return mid - 1

            if mid < h and arr[mid] < X < arr[mid + 1]:
                return mid

            if arr[mid] > X:
                h = mid - 1

            else:
                l = mid + 1
            if h == -1:
                return 0
            if l == len(arr):
                return len(arr) - 1
print('hello world')
