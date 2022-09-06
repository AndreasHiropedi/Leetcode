class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        
        total = amount
        S = [0 for i in range(len(coins))]
        C = [float("inf")] * (amount+1)
        P = [float("inf")] * (amount+1)
        C[0] = 0
        for w in range(1, amount+1):
            for i in range(0, len(coins)):
                if (coins[i] <= w) and (C[w-coins[i]] + 1 < C[w]):
                    C[w] = 1 + C[w-coins[i]]
                    P[w] = i
        while amount > 0:
            i = P[amount]
            if not isinstance(i, int):
                return -1
            S[i] = S[i] + 1
            amount = amount - coins[i]
        return C[total]
