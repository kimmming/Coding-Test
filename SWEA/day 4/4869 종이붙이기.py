# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AWTQWhlqQWADFAVT&categoryId=AWTQWhlqQWADFAVT&categoryType=CODE&problemTitle=4%EC%9D%BC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
import sys
from io import StringIO

test_input = '''\
3
30
50
70

'''

sys.stdin = StringIO(test_input)

T = int(input())
for tc in range(1, T + 1):
    answer = 0

    print(f'#{tc} {answer}')