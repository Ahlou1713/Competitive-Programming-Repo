
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        @cache
        def dp(amount, idx) -> int:

            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if idx >= n:
                return 0
            
            return dp(amount - coins[idx], idx) + dp(amount, idx+1) 

        return dp(amount, 0)
