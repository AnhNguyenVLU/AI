#adjacency list

graph = {
    '1' : ['2'],
    '2' : ['7', '4'],
    '3' : ['4'],
    '4' : ['6'],
    '5' : ['4', '3'],
    '6' : [],
    '7' : ['5']
}

def BFS(graph, s):
    visited = set()
    queue   = set() #list in python is basically queue
    visited.add(s) #means make it black
    queue.add(s)
    
    while queue: #as long as the queue is not empty....
        u = queue.pop()  #pop the front guy.....basically index 0
        
        print(u, "-->", end = "")
        
        for neighbor in graph[u]: #for everyone who connects to u, 
            if neighbor not in visited:
                visited.add(neighbor)              #add them to the visited
                queue.add(neighbor)                #add them to the queue
                
BFS(graph, '1')
