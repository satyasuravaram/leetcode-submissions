class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0
        minCoins = [amount+1]*(amount+1)
        minCoins[0] = 0
        
        for i in range(amount+1):
            for num in coins:
                if i - num >= 0:
                    minCoins[i] = min(minCoins[i], 1 + minCoins[i-num])
        return -1 if minCoins[amount] == amount + 1 else minCoins[amount]