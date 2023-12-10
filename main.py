import time 

_inf = 99999
 
# example 1
A = [[0, 5, _inf, _inf, 10,10, 0],
    [50, 0, 15, 5,0, 15, 2],
    [30, _inf, 0, 15, 123, 0 ,1 ],
    [15, _inf, 5, 0, 123, 2, 2]]
 
# example 2
B = [[0, 3, _inf, 5],
    [2, 0, _inf, 4],
    [_inf, 1, 0, _inf],
    [_inf, _inf, 2, 0]]

# floyd warshall function
def floyd_warshall(graph):
    n = len(graph)
   # stepping loop
    for k in range(n):
       # outer loop
       for i in range(n):
           # inner loop
           for j in range(n):
               # replace direct path with path through k if direct path is longer
               graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
   # print complete graph in a pretty manner
    for row in graph:
        print(row)
    
startTime = time.time()
print("Example 1")
print("Shortest Paths Graph for A")
floyd_warshall(A)
print(f'Execution time: {time.time() - startTime}')

print(" ")

startTime = time.time()
print("Example 2")
print("Shortest Paths Graph for B")
floyd_warshall(B)
print(f'Execution time: {time.time() - startTime}')