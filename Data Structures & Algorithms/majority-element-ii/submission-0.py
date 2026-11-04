class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None

        count1 = 0
        count2 = 0

        # Phase 1: Find potential candidates
        for num in nums:

            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Phase 2: Verify candidates
        result = []

        count1 = nums.count(candidate1)
        count2 = nums.count(candidate2)

        if count1 > len(nums) // 3:
            result.append(candidate1)

        if candidate2 != candidate1 and count2 > len(nums) // 3:
            result.append(candidate2)

        return result