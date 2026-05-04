class Solution:
    def canEat(self, piles: List[int], k: int, h: int) -> bool:
        time = 0
        for pile in piles:
            time += math.ceil(pile / k)
            if time > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        res = high

        while low <= high:
            mid = (low + high) // 2
            if self.canEat(piles, mid, h):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res
        