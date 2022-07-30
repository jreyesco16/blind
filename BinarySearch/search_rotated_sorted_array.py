class Solution:
    def search(self, nums: list[int], target: int) -> int:

        # left (l) and right (r) pivot
        l, r = 0, len(nums)-1

        while l <= r:

            pivot = (l+r) // 2

            if target == nums[pivot]:
                return pivot

            # left sorted portion
            if nums[l] <= nums[pivot]:
                if target > nums[pivot] or target < nums[l]:
                    l = pivot + 1
                else:
                    r = pivot - 1
            # right sorted portion
            else:
                if target < nums[pivot] or target > nums[r]:
                    r = pivot - 1
                else:
                    l = pivot + 1

        return -1


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    expected = 4

    result = Solution().search(nums, target)

    print("result", result)

    if expected == result:
        print("PASSED")
    else:
        print("FAILED")


if __name__ == "__main__":
    main()
