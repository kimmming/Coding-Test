# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQmA4uK8ygDFAXj&categoryId=AWQmA4uK8ygDFAXj&categoryType=CODE&problemTitle=%EC%98%A4%EC%85%80%EB%A1%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import sys
from io import StringIO
from pkgutil import resolve_name

test_input = '''\
1
4 12 
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''

sys.stdin = StringIO(test_input)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 1. 보드 생성
    board = [[0] * N for _ in range(N)]

    # 2. 초기 돌 배치
    mid = N // 2

    board[mid-1][mid-1] = 2
    board[mid-1][mid] = 1
    board[mid][mid-1] = 1
    board[mid+1][mid-1] = 2

    # 3. 8방향 설정
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    # 4. 돌 놓기
    for _ in range(M):
        col, row, color = map(int, input().split())
        row -= 1
        col -= 1

        board[row][col] = color
        opponent = 3 - color

        # 5. 8방향 탐색

    print(f'#{tc}')