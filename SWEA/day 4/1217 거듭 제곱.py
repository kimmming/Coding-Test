# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
import sys
from io import StringIO

test_input = '''\
1
9 8
2
2 8
3
6 5
4
10 7
5
6 7
6
7 2
7
9 8
8
3 2
9
4 8
10
8 6

'''

sys.stdin = StringIO(test_input)


def cal(N, M):
    if M <= 0:
        return 1

    result = N * cal(N, M-1)
    return result

for tc in range(10):
    T = int(input())
    N, M = map(int, input().split())
    answer = cal(N, M)

    print(f'#{T} {answer}')