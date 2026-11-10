#
import sys
from io import StringIO

test_input = '''\

'''

sys.stdin = StringIO(test_input)

T = int(input())
for tc in range(1, T + 1):
    answer = 0

    print(f'#{tc} {answer}')