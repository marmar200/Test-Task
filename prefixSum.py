# Метод префиксных сумм O(t*2*n)
# беда с памятью, используется дополнительный список
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = input()

    w = [0] * (n + 1)
    for j in range(1, n + 1):
        w[j] = w[j - 1] + (1 if s[j - 1] == 'W' else 0)

    result = float('inf')
    for j in range(k, n + 1):
        result = min(result, w[j] - w[j - k])

    print(result)
