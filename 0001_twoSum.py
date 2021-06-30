class Solution1:
    def twoSum(self, nums: list, target: int) -> list:
        loop_range = range(len(nums))
        # start_idx = 0
        for start_idx in loop_range:
            for idx in loop_range:
                if start_idx != idx and nums[start_idx] + nums[idx] == target:
                    return [start_idx, idx]
        # start_idx += 1


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dic1 = {}
        for i, num in enumerate(nums):
            match = target - num
            if num in dic1:
                return [dic1[num], i]
            else:
                dic1[match] = i


sol = Solution()

nums = [2, 7, 11, 15]
target = 9
out = sol.twoSum(nums, target)
print(f'nums: {nums} target: {target} The output array: {out}')

nums = [3, 2, 4]
target = 6
out = sol.twoSum(nums, target)
print(f'nums: {nums} target: {target} The output array: {out}')

nums = [3, 3]
target = 6
out = sol.twoSum(nums, target)
print(f'nums: {nums} target: {target} The output array: {out}')

nums = [1, 3, 3, 6, 0, 9]
target = 9
out = sol.twoSum(nums, target)
print(f'nums: {nums} target: {target} The output array: {out}')
