# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=%EB%86%8D%EC%9E%91%EB%AC%BC+%EC%88%98%ED%99%95&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import sys
from io import StringIO

test_input = '''\
2
5
14054
44250
02032
51204
52212
3
845
051
258
'''

sys.stdin = StringIO(test_input)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mid = N // 2
    answer = 0

    for r in range(N):
        row = list(map(int, input()))
        skip = abs(r - mid)
        answer += sum(row[skip:N - skip])


    print(f'#{tc} {answer}')