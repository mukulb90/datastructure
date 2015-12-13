__author__ = 'mukul'

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        i = 0
        j = 0
        while (i<len(A) and j<len(B)):
            if A[i]<B[j]:
                i = i+1
            else:
                A.insert(i, B[j])
                i = i+1
                j = j+1

        if i == len(A):
            while (j<len(B)):
                A.append(B[j])
                j = j+1

        return A


if __name__ == '__main__':
    s = Solution()
    print s.merge([1,2,3,4], [0,3,6])
