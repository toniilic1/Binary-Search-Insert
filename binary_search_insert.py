class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        value = 0

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                return mid
            elif guess < target:
                value = mid + 1
            elif guess > target:
                value = mid
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        return value

# uncomment a few examples below to test the code.
#print(Solution.searchInsert(None, [3, 6, 7, 8, 10], 5))
#print(Solution.searchInsert(None, [1, 2, 3, 4, 5, 10], 2))
#print(Solution.searchInsert(None, [2, 3, 4, 7, 8, 9], 11))
#print(Solution.searchInsert(None, [2, 3, 4, 7, 8, 9], 1))