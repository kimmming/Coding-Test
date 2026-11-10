# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
import sys
from io import StringIO

test_input = '''\
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''

sys.stdin = StringIO(test_input)

T = int(input())

def dfs(current, goal, graph, visited):
    # 1. 현재 노드가 목적지라면?
    if current == goal:
        return 1
    # 2. 현재 노드를 방문처리
    visited[current]= True

    # 3. 현재 노드와 연결된 노드들을 순회
    for next_node in graph[current]:
        # 4. 방문하지 않은 노드라면 재귀 호출
        if not visited[next_node]:
            result = dfs(next_node, goal, graph, visited)
            if result == 1:
                return result
    return 0

for tc in range(1, T+1):
    answer = 0

    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    start, goal = map(int, input().split())
    answer = dfs(start, goal, graph, visited)

    print(f'#{tc} {answer}')
