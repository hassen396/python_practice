

def findTheWinner(n: int, k: int) -> int:
    friends = [i + 1 for i in range(n)]
    carry = 0
    while len(friends) > 1:
        offset = 1
        n = len(friends)
        for i in range(k - carry, n, k):
            del friends[i - offset]
            if i >= n - 1:
                carry = 1
            offset += 1
    return friends[0]
findTheWinner(5, 2)