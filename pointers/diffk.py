__author__ = 'mukul'
"""
Given an array A of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

 Example: Input :
    A : [1 3 5]
    k : 4
 Output : YES as 5 - 1 = 4
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.
"""
__author__ = 'anonymous'

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, arr, diff):
        n = len(arr)
        i = 0
        j = 0
        while i < n and j < n:
            new_diff = arr[i] - arr[j]
            if new_diff == diff and i != j:
                return 1
            elif new_diff <= diff:
                i = i+1
            elif new_diff > diff:
                j = j+1

        return 0


if __name__ == '__main__':
    s = Solution()
    print s.diffPossible([ 1, 2, 2, 3, 4 ], 0)