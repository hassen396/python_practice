def longestPalindrome( s: str) -> str:
    n = len(s)
    s = 'and'
    start = 0
    max_len = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            left = i - 1
            right = i
            while left >= 0 and right < n:
                if s[left] == s[right] and max_len < right - left + 1:
                    start = left
                    max_len = right - left + 1
                elif s[left] != s[right]:
                    break
                left -= 1
                right += 1
    return ''

# print(longestPalindrome('cbbd'))


def test():
    nums = []
    nums.insert(1, 1)
    nums.append([4,5])
    print([2,3] + nums)

test()