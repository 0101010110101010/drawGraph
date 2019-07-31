#coding=utf-8
import networkx as nx
import sys
import matplotlib.pyplot as plt

#create a graph
#简单无向图 Graph()
#简单有向图 DiGraph()
#有自环     Grap(),DiGraph()
#有重边     MultiGraph(), MultiDiGraph()
g = nx.DiGraph()
g.clear()

#g.add_node(1)
#g.add_node("aaa")
##g.add_nodes_from([2,3])

#g.add_edge("aaa","ccc")
#g.add_edge("ddd","eee")

#a = [2,3]
#g.add_nodes_from(a)
#g.add_node("spam") #添加了一个名为spam的节点
#g.add_nodes_from("spam") #添加了4个节点，名为s,p,a,m
#g.nodes() #可以将以上5个节点打印出来看看
#
#H = nx.path_graph(10)
#g.add_nodes_from(H) #将0~9加入了节点
#
##g.remove_node(node_name)
##g.remove_nodes_from(nodes_list)
#
#g.add_edge(1,2)
#e = (2,3)
#g.add_edge(*e) #直接g.add_edge(e)数据类型不对，*是将元组中的元素取出
#
#g.add_edges_from([(1,2),(1,3)])
#g.add_edges_from([("a","spam") , ("a",2)])
#
#n = 10
#H = nx.path_graph(n)
#g.add_edges_from(H.edges()) #添加了0~1,1~2 ... n-2~n-1这样的n-1条连续的边
#
#g.remove_edge(edge)
#g.remove_edges_from(edges_list)
#
#g.number_of_nodes() #查看点的数量
#g.number_of_edges() #查看边的数量
#g.nodes() #返回所有点的信息(list)
#g.edges() #返回所有边的信息(list中每个元素是一个tuple)
#g.neighbors(1) #所有与1这个点相连的点的信息以列表的形式返回
#g[1] #查看所有与1相连的边的属性，格式输出：{0: {}, 2: {}} 表示1和0相连的边没有设置任何属性（也就是{}没有信息），同理1和2相连的边也没有任何属性

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

#为图赋予初始属性
#g = nx.Graph(day="Monday") 
#g.graph # {'day': 'Monday'}
##修改图的属性
#g.graph['day'] = 'Tuesday'
#g.graph # {'day': 'Tuesday'}
#
#g.add_node('benz', money=10000, fuel="1.5L")
#print(g.node['benz'])# {'fuel': '1.5L', 'money': 10000}
#print(g.node['benz']['money'])# 10000
#print(g.nodes(data=True))# data默认false就是不输出属性信息，修改为true，会将节点名字和属性信息一起输出

#通过上文中对g[1]的介绍可知边的属性在{}中显示出来，我们可以根据这个秀改变的属性
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
#DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75), (1,4,0.3)]) # 添加带权值的边
#print DG.out_degree(1) # 打印结果：2 表示：找到1的出度
#print DG.out_degree(1, weight='weight') # 打印结果：0.8 表示：从1出去的边的权值和，这里权值是以weight属性值作为标准，如果你有一个money属性，那么也可以修改为weight='money'，那么结果就是对money求和了
#print DG.successors(1) # [2,4] 表示1的后继节点有2和4
#print DG.predecessors(1) # [3] 表示只有一个节点3有指向1的连边
#
#Multigraphs
#简答从字面上理解就是这种复杂网络图允许你相同节点之间允许出现重边
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
##图的遍历
#g = nx.Graph()
#g.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])
#for n,nbrs in g.adjacency_iter(): #n表示每一个起始点，nbrs是一个字典，字典中的每一个元素包含了这个起始点连接的点和这两个点连边对应的属性
#    print n, nbrs
#    for nbr,eattr in nbrs.items():
#        # nbr表示跟n连接的点，eattr表示这两个点连边的属性集合，这里只设置了weight，如果你还设置了color，那么就可以通过eattr['color']访问到对应的color元素
#        data=eattr['weight']
#        if data<0.5: print('(%d, %d, %.3f)' % (n,nbr,data))
#
##图生成和图上的一些操作 下方的这些操作都是在networkx包内的方法
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
#图上分析
#g = nx.Graph()
#g.add_edges_from([(1,2), (1,3)])
#g.add_node("spam") 
#nx.connected_components(g) # [[1, 2, 3], ['spam']] 表示返回g上的不同连通块
#sorted(nx.degree(g).values()) 
#
#图的绘制
#下面是4种图的构造方法，选择其中一个
#nx.draw(g)
#nx.draw_random(g) #点随机分布
#nx.draw_circular(g) #点的分布形成一个环
#nx.draw_spectral(g)
#

#read node color
#line = file_color.read()           #读取颜色向量
#colors = (line.split(' '))         #颜色向量
#for i in range(len(colors)):
#    colors[i] = int(colors[i])    #将字符转为数字
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



#修改节点颜色，边的颜色
#g = nx.cubical_graph()
nx.draw(g,  pos = nx.shell_layout(g) , with_labels=True, node_color=colors, edge_color='black',font_size=8,node_size=200)
plt.show()
#plt.savefig("path.png")

