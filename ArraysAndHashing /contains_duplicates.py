class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        s = set(nums)

        if len(nums) == len(s):
            return False
        
        return True

def main():
    test_case = [1,2,3,1]

    expected = True

    result = Solution().containsDuplicate(test_case)

    if result == expected:
        print("PASSED")
    else:
        print("FAILED")


if __name__ == "__main__":
    main()