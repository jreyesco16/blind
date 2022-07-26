class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'

        lowers = s.lower()

        fancy_str = ''

        for x in lowers:
            if x in alphabet:
                fancy_str += x
        
        pivot = int(len(fancy_str)/2)

        for i in range(0, pivot):
            if fancy_str[i] != fancy_str[len(fancy_str)-1-i]:
                return False
        
        return True


def main():

    test_case = "0P"

    expected = False

    result = Solution().isPalindrome(test_case)

    if expected == result:
        print("PASSED")
    else:
        print("FAILED")


if __name__ == "__main__":
    main()
