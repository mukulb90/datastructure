def max_sub_array(arr):
    dp = [0 for item in arr]
    dp[0] = arr[0]
    for index in range(1, len(arr)):
        item = arr[index]
        if dp[index-1] > 0 :
            dp[index] = item + dp[index - 1]
        else:
            dp[index] = item
        print dp
    return max(dp)

def main():
    raw_input  = '10 -1 20 30 4 -100 -30 1 50'
    arr = [int(item) for item in raw_input.split(' ')]
    print max_sub_array(arr);

if __name__ == '__main__':
    main()
