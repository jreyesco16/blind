class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        l, r = 0, 1

        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r]-prices[l])

            else:
                l=r

            r+=1

        return profit
                



def main():
    test_case = [7,1,5,3,6,4]

    expected = 5

    result = Solution().maxProfit(test_case)

    if result == expected:
        print("PASSED")
    else:
        print('FAILED')

if __name__ == "__main__":
    main()