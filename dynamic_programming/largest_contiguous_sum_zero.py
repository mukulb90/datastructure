class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        sum = 0
        map = {};
        acc_sum = []
        for item in A:
            sum = item + sum
            acc_sum.append(sum)

        start = 0
        end = 0
        result = []
        for index in range(len(acc_sum)):
            sum = acc_sum[index]

            if sum in map or sum == 0:
                if sum == 0:
                    start_index = 0
                    end_index = index
                else:
                    start_index = map[sum] + 1
                    end_index = index
                if not result or  (len(result) < end_index - start_index + 1):
                    result = A[start_index: end_index+1]

            else:
                map[sum] = index

        return result



        
