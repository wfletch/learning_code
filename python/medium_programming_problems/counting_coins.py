class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin,amount+1): # Integer multiples of the coin.
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
    # Beautiful Solution To The Problem!
    # LC: 322
    # Space O(amount). We need array of that size
    # Time: O(amount * len(coins))
    # Note: This was taking from the modal solution.... it's very good!