# Перебор O(t*n*n)

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    line = input()

    min_cnt = 200000
    for first in range(len(line) - k + 1):
        min_cnt = min(min_cnt, line.count('W', first, first + k))

    print(min_cnt)
