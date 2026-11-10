# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTtlrlKeDcDFAVT
import sys
from io import StringIO

test_input = '''\
2
3
1 2 3
2 3 4
3 4 5
3
1 9 1
1 1 1
9 1 1
'''

sys.stdin = StringIO(test_input)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * N for _ in range(N)]
    dp[0][0] = board[0][0]

    for r in range(N):
        for c in range(N):
            if r == 0 and c == 0:
                continue

            if r == 0:
                dp[r][c] = dp[r][c - 1] + board[r][c]

            elif c == 0:
                dp[r][c] = dp[r - 1][c] + board[r][c]

            else:
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + board[r][c]

    print(f'#{test_case} {dp[N - 1][N - 1]}')