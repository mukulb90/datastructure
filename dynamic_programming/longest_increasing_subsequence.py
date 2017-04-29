def _longest_increasing_subsequence(arr, end):
    cost = [1 for item in arr];
    for outer in range(1, end + 1):
        max_so_far = cost[0];
        for inner in range(0, outer):
            # lis till inner -> cost[inner]
            if(arr[inner] < arr[outer]):
                max_so_far = max([cost[inner] + 1, max_so_far])
        cost[outer] = max_so_far;
    return cost[end];

def longest_increasing_subsequence(arr):
    return _longest_increasing_subsequence(arr, len(arr) - 1);

def main():
    input = '10, 9, 2, 5, 3, 7, 101, 18'
    #
    values = [int(item) for item in input.split(', ')]
    print(longest_increasing_subsequence(values));

if __name__ == '__main__':
    main()
