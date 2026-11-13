#
import sys
from io import StringIO
from collections import deque

test_input = '''\
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2
'''


sys.stdin = StringIO(test_input)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    oven = deque()

    for i in range(N):
        oven.append([i+1, cheese[i]])

    next_idx = N

    while len(oven) > 1 or next_idx < M:
        pizza = oven.popleft()
        pizza[1] //= 2
        if pizza[1] > 0 :
            oven.append(pizza)
        else:
            if next_idx < M:
                oven.append([next_idx+1, cheese[next_idx]])
                next_idx += 1

    print(f'#{tc} {oven[0][0]}')