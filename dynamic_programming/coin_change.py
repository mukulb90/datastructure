import collections
import functools
import cPickle

map = dict()

class Solution(object):

    def __init__(self):
        self.map = dict()

    def coinChange(self, coins, num):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if num in self.map:
            return self.map.get(num)

        if num == 0:
            return 0

        min_change = -1

        for coin in coins:
            if(num - coin >= 0 ):
                remainingCoinChange = self.coinChange(coins, num-coin);
                if remainingCoinChange is not -1:
                    if min_change is -1 or (remainingCoinChange + 1 < min_change):
                        min_change = remainingCoinChange + 1

        self.map.setdefault(num, min_change)
        return min_change


def main():
    coins = [370,417,408,156,143,434,168,83,177,280,117]
    num = 9953
    s = Solution()
    print s.coinChange(coins, num)

if __name__ == '__main__':
    main()
