class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount: int) -> int:
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]

            min_coins = float('inf')
            for coin in coins:
                result = dp(amount - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            memo[amount] = min_coins
            return memo[amount]
        
        result = dp(amount)
        return result if result != float('inf') else -1
