class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        n = len(piles) // 3
        piles = piles[: len(piles) - n]
        return sum(piles[1::2])

        