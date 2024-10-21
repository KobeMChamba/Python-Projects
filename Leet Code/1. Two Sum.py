class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetdict = {}
        counter = 0
        for num in nums:
            if num in targetdict:
                return [counter, targetdict[num]]
            targetnum = target-num
            targetdict[targetnum] = counter
            print("t: ", targetnum, " c: ", counter)
            counter += 1