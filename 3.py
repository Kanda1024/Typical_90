from collections import deque

N = int(input())
A = []
B = []

Graph = [[] for i in range(N)]

for i in range(N-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    Graph[a].append(b)
    Graph[b].append(a)

ans = 0

que = deque()
que.append(0)
visited = [False]*N
visited[0] = True
cost = [0]*N
cost[0] = 0

while que:
    now = que.popleft()
    for v in Graph[now]:
        if visited[v] == False:
            que.append(v)
            visited[v] = True
            cost[v] = cost[now]+1

w = cost.index(max(cost))


que = deque()
que.append(w)
visited = [False]*N
visited[w] = True
cost = [0]*N
cost[w] = 0

while que:
    now = que.popleft()
    for v in Graph[now]:
        if visited[v] == False:
            que.append(v)
            visited[v] = True
            cost[v] = cost[now]+1

ans += max(cost)

print(ans+1)