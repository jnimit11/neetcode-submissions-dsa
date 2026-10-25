class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Start only at the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                length = 1

                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    length += 1

                # Update the longest sequence
                longest = max(longest, length)

        return longest