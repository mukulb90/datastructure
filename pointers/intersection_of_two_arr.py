__author__ = 'anonymous'
"""
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
 NOTE : For the purpose of this problem ( as also conveyed by the sample case ), assume that
"""
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i = 0
        j = 0
        result = []
        while i<len(A) and j <len(B):
            if A[i] == B[j]:
                result.append(A[i])
                i = i+1
                j = j+1
            elif A[i]<B[j]:
                i = i+1
            else:
                j = j+1

        return result


if __name__ == '__main__':
    s = Solution()
    print s.intersect([1,2,3], [1,2,2,2,3,4])