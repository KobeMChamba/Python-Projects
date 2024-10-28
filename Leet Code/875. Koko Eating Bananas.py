class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        # Constant time improvements
        m = max(piles)
        n = len(piles)
        if n == h:
            return m

        s = sum(piles)
        l = (s + h - 1) // h
        # set r to the minimum eating speed she can do (we know h > n at this point)
        # 
        r = math.ceil(s /(h-n)) 

        while l < r:
            mid = (l + r) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)

            if hours > h :
                # koko needs to eat faster
                l = mid + 1
            else:
                # test slower time 
                r = mid
        return l