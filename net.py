#coding=utf-8
import networkx as nx
import sys
import matplotlib.pyplot as plt

#create a graph
#������ͼ Graph()
#������ͼ DiGraph()
#���Ի�     Grap(),DiGraph()
#���ر�     MultiGraph(), MultiDiGraph()
g = nx.DiGraph()
g.clear()

#g.add_node(1)
#g.add_node("aaa")
##g.add_nodes_from([2,3])

#g.add_edge("aaa","ccc")
#g.add_edge("ddd","eee")

#a = [2,3]
#g.add_nodes_from(a)
#g.add_node("spam") #�����һ����Ϊspam�Ľڵ�
#g.add_nodes_from("spam") #�����4���ڵ㣬��Ϊs,p,a,m
#g.nodes() #���Խ�����5���ڵ��ӡ��������
#
#H = nx.path_graph(10)
#g.add_nodes_from(H) #��0~9�����˽ڵ�
#
##g.remove_node(node_name)
##g.remove_nodes_from(nodes_list)
#
#g.add_edge(1,2)
#e = (2,3)
#g.add_edge(*e) #ֱ��g.add_edge(e)�������Ͳ��ԣ�*�ǽ�Ԫ���е�Ԫ��ȡ��
#
#g.add_edges_from([(1,2),(1,3)])
#g.add_edges_from([("a","spam") , ("a",2)])
#
#n = 10
#H = nx.path_graph(n)
#g.add_edges_from(H.edges()) #�����0~1,1~2 ... n-2~n-1������n-1�������ı�
#
#g.remove_edge(edge)
#g.remove_edges_from(edges_list)
#
#g.number_of_nodes() #�鿴�������
#g.number_of_edges() #�鿴�ߵ�����
#g.nodes() #�������е����Ϣ(list)
#g.edges() #�������бߵ���Ϣ(list��ÿ��Ԫ����һ��tuple)
#g.neighbors(1) #������1����������ĵ����Ϣ���б����ʽ����
#g[1] #�鿴������1�����ıߵ����ԣ���ʽ�����{0: {}, 2: {}} ��ʾ1��0�����ı�û�������κ����ԣ�Ҳ����{}û����Ϣ����ͬ��1��2�����ı�Ҳû���κ�����

#Graph.has_node(n)                       Return True if the graph contains the node n.
#Graph.__contains__(n)                   Return True if n is a node, False otherwise.
#Graph.has_edge(u, v)                    Return True if the edge (u,v) is in the graph.
#Graph.order()                           Return the number of nodes in the graph.
#Graph.number_of_nodes()                 Return the number of nodes in the graph.
#Graph.__len__()                         Return the number of nodes.
#Graph.degree([nbunch, weight])          Return the degree of a node or nodes.
#Graph.degree_iter([nbunch, weight])     Return an iterator for (node, degree).  
#Graph.size([weight])                    Return the number of edges.
#Graph.number_of_edges([u, v])           Return the number of edges between two nodes.
#Graph.nodes_with_selfloops()            Return a list of nodes with self loops.
#Graph.selfloop_edges([data, default])   Return a list of selfloop edges.  
#Graph.number_of_selfloops()             Return the number of selfloop edges.

#Ϊͼ�����ʼ����
#g = nx.Graph(day="Monday") 
#g.graph # {'day': 'Monday'}
##�޸�ͼ������
#g.graph['day'] = 'Tuesday'
#g.graph # {'day': 'Tuesday'}
#
#g.add_node('benz', money=10000, fuel="1.5L")
#print(g.node['benz'])# {'fuel': '1.5L', 'money': 10000}
#print(g.node['benz']['money'])# 10000
#print(g.nodes(data=True))# dataĬ��false���ǲ����������Ϣ���޸�Ϊtrue���Ὣ�ڵ����ֺ�������Ϣһ�����

#ͨ�������ж�g[1]�Ľ��ܿ�֪�ߵ�������{}����ʾ���������ǿ��Ը��������ı������
#g.clear()
#n = 10
#H = nx.path_graph(n)
#g.add_nodes_from(H)
#g.add_edges_from(H.edges())
#g[1][2]['color'] = 'blue'
#
#g.add_edge(1, 2, weight=4.7)
#g.add_edges_from([(3,4),(4,5)], color='red')
#g.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])
#g[1][2]['weight'] = 4.7
#g.edge[1][2]['weight'] = 4


#Directed graphs
#DG = nx.DiGraph()
#DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75), (1,4,0.3)]) # ��Ӵ�Ȩֵ�ı�
#print DG.out_degree(1) # ��ӡ�����2 ��ʾ���ҵ�1�ĳ���
#print DG.out_degree(1, weight='weight') # ��ӡ�����0.8 ��ʾ����1��ȥ�ıߵ�Ȩֵ�ͣ�����Ȩֵ����weight����ֵ��Ϊ��׼���������һ��money���ԣ���ôҲ�����޸�Ϊweight='money'����ô������Ƕ�money�����
#print DG.successors(1) # [2,4] ��ʾ1�ĺ�̽ڵ���2��4
#print DG.predecessors(1) # [3] ��ʾֻ��һ���ڵ�3��ָ��1������
#
#Multigraphs
#�������������������ָ�������ͼ��������ͬ�ڵ�֮����������ر�
#MG=nx.MultiGraph()
#MG.add_weighted_edges_from([(1,2,.5), (1,2,.75), (2,3,.5)])
#print MG.degree(weight='weight') # {1: 1.25, 2: 1.75, 3: 0.5}
#GG=nx.Graph()
#for n,nbrs in MG.adjacency_iter():
#    for nbr,edict in nbrs.items():
#        minvalue=min([d['weight'] for d in edict.values()])
#        GG.add_edge(n,nbr, weight = minvalue)
#
#print nx.shortest_path(GG,1,3) # [1, 2, 3]
#
##ͼ�ı���
#g = nx.Graph()
#g.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])
#for n,nbrs in g.adjacency_iter(): #n��ʾÿһ����ʼ�㣬nbrs��һ���ֵ䣬�ֵ��е�ÿһ��Ԫ�ذ����������ʼ�����ӵĵ�������������߶�Ӧ������
#    print n, nbrs
#    for nbr,eattr in nbrs.items():
#        # nbr��ʾ��n���ӵĵ㣬eattr��ʾ�����������ߵ����Լ��ϣ�����ֻ������weight������㻹������color����ô�Ϳ���ͨ��eattr['color']���ʵ���Ӧ��colorԪ��
#        data=eattr['weight']
#        if data<0.5: print('(%d, %d, %.3f)' % (n,nbr,data))
#
##ͼ���ɺ�ͼ�ϵ�һЩ���� �·�����Щ����������networkx���ڵķ���
##subgraph(G, nbunch)      - induce subgraph of G on nodes in nbunch
##union(G1,G2)             - graph union
##disjoint_union(G1,G2)    - graph union assuming all nodes are different
##cartesian_product(G1,G2) - return Cartesian product graph
##compose(G1,G2)           - combine graphs identifying nodes common to both
##complement(G)            - graph complement
##create_empty_copy(G)     - return an empty copy of the same graph class
##convert_to_undirected(G) - return an undirected representation of G
##convert_to_directed(G)   - return a directed representation of G
#
#ͼ�Ϸ���
#g = nx.Graph()
#g.add_edges_from([(1,2), (1,3)])
#g.add_node("spam") 
#nx.connected_components(g) # [[1, 2, 3], ['spam']] ��ʾ����g�ϵĲ�ͬ��ͨ��
#sorted(nx.degree(g).values()) 
#
#ͼ�Ļ���
#������4��ͼ�Ĺ��췽����ѡ������һ��
#nx.draw(g)
#nx.draw_random(g) #������ֲ�
#nx.draw_circular(g) #��ķֲ��γ�һ����
#nx.draw_spectral(g)
#

#read node color
#line = file_color.read()           #��ȡ��ɫ����
#colors = (line.split(' '))         #��ɫ����
#for i in range(len(colors)):
#    colors[i] = int(colors[i])    #���ַ�תΪ����
colors = []
file_color = open(sys.argv[1], 'r')
for line in file_color.readlines():
    #lineArr = line.strip().split(" ")
    lineArr = list(filter(None,line.split(' ')))
    lineArr[1] = lineArr[1].rstrip("\n")
    print(lineArr[0])
    #g.add_nodes_from(lineArr)
    g.add_node(lineArr[0])
    #colors.append (int(lineArr[1]))
    colors.append (lineArr[1])

#read edges and nodes
node = []
file_node = open(sys.argv[2], 'r')
for line in file_node.readlines():
    #lineArr = line.strip().split(" ",num=-1)
    lineArr = list(filter(None,line.split(' ')))
    lineArr[1] = lineArr[1].rstrip("\n")
    
    print(lineArr)
    #g.add_nodes_from(lineArr)
    g.add_edge(lineArr[0],lineArr[1])
    #node.clear()
    #g.add_edge("aaa","ccc")



#�޸Ľڵ���ɫ���ߵ���ɫ
#g = nx.cubical_graph()
nx.draw(g,  pos = nx.shell_layout(g) , with_labels=True, node_color=colors, edge_color='black',font_size=8,node_size=200)
plt.show()
#plt.savefig("path.png")

