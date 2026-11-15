# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=%EC%88%AB%EC%9E%90+%EB%B0%B0%EC%97%B4&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import sys
from io import StringIO

test_input = '''\
10
3
1 2 3
4 5 6
7 8 9
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
7
9 3 1 8 5 0 5
1 1 1 7 9 1 8
3 6 1 4 7 7 4
3 1 8 5 3 0 7
2 5 2 5 7 6 8
2 8 5 2 6 7 0
0 5 5 9 3 6 0
3
6 0 4
7 9 3
8 1 2
6
1 6 4 0 8 1
0 8 0 4 1 2
7 7 6 8 4 3
8 6 3 8 0 0
5 7 7 7 6 4
9 1 8 1 7 1
3
4 1 9
9 9 7
8 0 1
5
1 0 2 2 7
5 2 4 8 5
4 7 8 2 3
9 6 2 8 5
9 6 1 6 6
3
4 8 3
4 6 3
3 9 6
3
4 9 7
0 1 3
4 4 3
5
1 1 7 4 1
0 7 9 3 5
5 2 5 8 6
6 1 9 0 6
7 0 1 3 9
'''

sys.stdin = StringIO(test_input)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 0
    maps = []
    for _ in range(N):
        arr = list(map(str,input().split()))
        maps.append(arr)
    print(f'#{tc}')

    # 90도 - [N -1 -c][r]
    # 180도 - [N-1-r][N-1-c]
    # 270도 - [c][N-1-r]

    for r in range(N):
        row90, row180, row270 = "","",""

        for c in range(N):
            row90 += maps[N-1-c][r]
            row180 += maps[N-1-r][N-1-c]
            row270 += maps[c][N-1-r]
        print(row90, row180, row270)