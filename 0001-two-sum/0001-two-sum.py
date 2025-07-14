class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #approach: 
        #hash = {}
        #for num in nums:
        #   complement = target - num
        #   if complement in hashmap:
        #       return [[nums[num]], [hash[complement]]
        #   hash[num] = index

        #[3, 3], target = 6
        # {[3, 0]}
        #for 3 in nums:
        #complement = 6 - 3 = 3
        #return [1, 0]

        #[3, 3, 4], target = 7
        #{[3, 1]}
        #complement = 7 - 4 = 3
        #return [2, 1]

        #[1, 5, 9, 11], target = 14
        #{[1, 0], [5, 1]}
        # for 9
        # complement = 14 - 9 = 5
        #return [2, 1]

        hash = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash:
                return [i, hash[complement]]
            hash[num] = i
        return []

        