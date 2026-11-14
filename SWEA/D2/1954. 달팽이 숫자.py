#
import sys
from io import StringIO

test_input = '''\
2
3
4
'''

sys.stdin = StringIO(test_input)

for tc in range(1, 4):
    T = int(input())
    snail = [[0] * T for _ in range(T)]

    # 1. 시계방향 배열
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    row, col = 0,0
    direction = 0

    for num in range(1, T*T+1):
        snail[row][col] = num

        # 2. 다음 이동할 좌표 계산
        next_row = row + dr[direction]
        next_col = col + dc[direction]

        # 3. 범위를 벗어남 or 이미 방문했다면 방향 전환
        if not(0<=next_row<T and 0<=next_col<T) or snail[next_row][next_col] != 0:
            direction = (direction+1) % 4
            # direction+1 -> 다음 방향으로 이동
            # direction = 3 일때 +1 하면 4
            # dr[4], dc[4]는 없으니 다시 0으로
            # 0,1,2,3 -> dr[0],[1],[2],[3]
            # dir = (0+1) % 4 = 1 오른쪽 -> 아래로 방향 전환
            next_row = row + dr[direction]
            next_col = col + dc[direction]
        # 4. 방향에 맞춰 다음 좌표 갱신
        row, col = next_row, next_col

    print(f'#{tc}')
    for row in snail:
        print(*row)