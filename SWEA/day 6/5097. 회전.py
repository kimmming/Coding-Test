# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTVjgHKbn8DFAVT&categoryId=AWTVjgHKbn8DFAVT&categoryType=CODE&problemTitle=6%EC%9D%BC%EC%B0%A8&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import sys
from io import StringIO

test_input = '''\
3
3 10
5527 731 31274
5 12
18140 14618 18641 22536 23097
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907	 
'''

sys.stdin = StringIO(test_input)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    index = M%N
    answer = nums[index]

    print(f'#{tc} {answer}')