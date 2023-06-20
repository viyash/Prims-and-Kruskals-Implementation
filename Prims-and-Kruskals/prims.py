import glb

def read_graph(file, d):
    file_location = open(file)
    for readreadLines in file_location:
        readLine = [x.strip() for x in readreadLines.split(f'{d}')]
        distance1 = readLine[0]
        distance2 = readLine[1]
        edgesWeight = round(float(readLine[2]))
        if distance1 in glb.WGRAPH.keys():
            glb.WGRAPH[distance1][distance2] = edgesWeight
        else:
            glb.WGRAPH[distance1] = {}
            glb.WGRAPH[distance1][distance2] = edgesWeight
    return glb.WGRAPH

#return true if successfully added vertex to visited
#return false if vertex was already visited
def add_visited(Vertex):
    if(Vertex in glb.Vr):
        return False
    else:
        glb.Vr.append(Vertex)
        return True

def get_min():
    minimumVertex1 = None
    minimumVertex2 = None
    minimumDistance = 0
    for v1 in glb.Vr:
        neighbors = list(glb.WGRAPH.get(v1))
        for v2 in neighbors:
            if v2 in glb.Vr or v1 == v2:
                continue
            if minimumVertex1 == None or minimumVertex2 == None:
                minimumVertex1 = v1
                minimumVertex2 = v2
                minimumDistance = glb.WGRAPH[v1][v2]
                continue
            a = int(glb.WGRAPH[v1][v2])
            b = int(glb.WGRAPH[minimumVertex1][minimumVertex2])
            if a < b:
                minimumVertex1 = v1
                minimumVertex2 = v2
                minimumDistance = a
    return (minimumVertex1,minimumVertex2,minimumDistance)

def prims():
    cdist = 0 #cumulative dist
    length = len(list(glb.WGRAPH.keys()))
    v = list(glb.WGRAPH.keys())[0]
    add_visited(v)
    for i in range(0,length-1):
        v, v2, edist = get_min() #v2 min edgesWeight
        cdist += int(edist)
        #add v to MST
        glb.MST.append((v,v2,str(edist),str(cdist)))
        add_visited(v2)
    return (glb.MST,cdist)

