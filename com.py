#A community S is a subset of vertices such that all the edges
#have both end vertices are in S. Let it be called E(S) 

#density of a community is defined as p = |E(S)|/|S|

#Output is of the below format:
#CommunityNo. Density NoOfEdges NoOfVertices

fileName = 'livejournal-undirected.txt'
f= open(fileName)

def readPart():
    return f.readline()
nodes = set()

f= open(fileName)
for line in iter(readPart, ''):
    a = line.split()
    nodes.add(a[0])
    nodes.add(a[1])

f.close()

no_of_iter = 1
e = 0.05

#Finding 20 communities
while no_of_iter <= 20:
    S = set(nodes)
    S1 = set(nodes)  #max density community for this iteration
    p1 = 0           #density of the most dense community
    e1 = 0           #no.of edges in the most dense community
    
    while len(S) > 0:
        s = list(S)
        deg = dict.fromkeys(s,0)
        del s
        edgeCount = 0
		
		#computing degree of all the vertices in the set
        f= open(fileName)
        for line in iter(readPart, ''):
            a = line.split()
            if a[0] in S and a[1] in S:
                deg[a[0]] += 1
                deg[a[1]] += 1    
                edgeCount += 1
        f.close()
        
        p = float(edgeCount)/len(S)
        
		#storing maximum dense community
        if p1 < p:
            p1 = p
            S1.clear()
            S1 = set(S)
            e1 = edgeCount
        
		#adding vertices with low degree to a set
        AS = set()
        for v in S:
            if deg[v] <= 2*(1+e)*p:
                AS.add(v)
		
		#removing the low degree vertices from S
        S = S - AS
        AS.clear()
        deg.clear()
        
    print no_of_iter, p1, e1, len(S1) 
    nodes = nodes - S1
    S1.clear()
    S.clear()
    no_of_iter += 1