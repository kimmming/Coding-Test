# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=7%EC%9D%BC%EC%B0%A8&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=30&pageIndex=1
import sys
from io import StringIO
from collections import deque

test_input = '''\
1
9550 9556 9550 9553 9558 9551 9551 9551
2
2419 2418 2423 2415 2422 2419 2420 2415
'''

sys.stdin = StringIO(test_input)

for tc in range(1, 11):
    T = int(input())
    arr = deque(map(int, input().split()))

    count = -1
    while arr[-1] > 0:
        if count < -5:
            count = -1

        temp = arr.popleft()
        temp += count
        count -= 1

        if temp <= 0:
            temp= 0

        arr.append(temp)


    print(f'#{tc}', *arr)