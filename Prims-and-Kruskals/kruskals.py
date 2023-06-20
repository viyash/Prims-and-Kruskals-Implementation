import heapq
import glb

def read_graph(file, d):
    file_location = open(file)
    for readLines in file_location:
        readLine = [x.strip() for x in readLines.split(f'{d}')]
        vertex1 = readLine[0]
        vertex2 = readLine[1]
        edgesWeight = round(float(readLine[2]))
        if((int(edgesWeight),vertex2,vertex1) in glb.EDGES): #maintain edge as set
            continue
        heapq.heappush(glb.EDGES, (int(edgesWeight),vertex1,vertex2))
        glb.VERTICES.add(vertex1)
        glb.VERTICES.add(vertex2)
    return glb.EDGES

def make_set(v):
     glb.PARENT[v] = v
     glb.RANK[v] = 0

def find(v):
    if(glb.PARENT[v] != v):
        glb.PARENT[v] = find(glb.PARENT[v])
    return glb.PARENT[v]

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if(root1 != root2):
        if(glb.RANK[root1] > glb.RANK[root2]):
            glb.PARENT[root2] = root1
        else:
            glb.PARENT[root1] = root2
            glb.RANK[root2] += 1

def kruskals():
    cdist = 0
    for v in glb.VERTICES:
        make_set(v)
    while(glb.EDGES):
        e,vertex1,vertex2 = heapq.heappop(glb.EDGES)
        if(find(vertex1) != find(vertex2)):
            union(vertex1, vertex2)
            cdist += e
            glb.MST.append((vertex1, vertex2, str(e), str(cdist)))
    return (glb.MST,cdist)