"""
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = zero?
    Find all unique triplets in the array which gives the sum of zero.
    Note:
    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
    The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    def threeSum(self, arr):
        arr.sort()
        result = set()
        n = len(arr)
        total = 0
        for i in range(0, n):
            j = i+1
            k=n-1
            while(k>j and j<n):
                temp = arr[i] + arr[j] + arr[k]
                if total == temp:
                    result.add((arr[i] ,arr[j] ,arr[k]))

                if temp <=0:
                    j = j+1
                else:
                    k = k-1
        result = list(result)
        result.sort()
        return result


if __name__ == '__main__':
    s = Solution()
    print s.threeSum([ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ])