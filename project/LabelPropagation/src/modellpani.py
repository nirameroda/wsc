"""Model class label propagation."""
import numpy as np
import random
import networkx as nx
from tqdm import tqdm
from community import modularity
#from networkx.algorithms.community.quality import modularity
#from sknetwork.clustering import modularity
from print_and_read import json_dumper
from calculation_helper import overlap, unit, min_norm, normalized_overlap, overlap_generator
from sys import exit
import time
class LabelPropagator:
    """
    Label propagation class.
    """
    def __init__(self, graph,x, args):
        """
        Setting up the Label Propagator object.
        :param graph: NetworkX object.
        :param args: Arguments object.
        """
        self.rounds=100
        self.args = args
        self.seeding = args.seed
        self.graph = graph
        self.nodes = [node for node in graph.nodes()]
        self.rounds = args.rounds
        self.labels = {node: node for node in self.nodes}
        self.label_count = len(set(self.labels.values()))
        self.label_countarr= {node: node for node in self.nodes}
        self.flag = True
        self.ni={node: node for node in self.nodes}
        self.li={node: node for node in self.nodes}
        self.lst={node: node for node in self.nodes}
        self.weight_setup(args.weighting)
        self.degree={node: node for node in self.nodes}
        self.y=x
        print(len(graph.nodes()))

    def weight_setup(self, weighting):
        """
        Calculating the edge weights.
        :param weighting: Type of edge weights.
        """
        if weighting == "overlap":
            self.weights = overlap_generator(overlap, self.graph)
        elif weighting == "unit":
            self.weights = overlap_generator(unit, self.graph)
        elif weighting == "min_norm":
            self.weights = overlap_generator(min_norm, self.graph)
        else:
            self.weights = overlap_generator(normalized_overlap, self.graph)
            
    def equality1(self,i ,neighbors):    
        max1=0
        
        for neighbor in tqdm(neighbors):
                if self.label_countarr[neighbor]>max1:
                    max1=self.label_countarr[neighbor]
        print(max1)
        return max1   
    def equality(self,i ,neighbors,max1):
        neighbors=nx.neighbors(self.graph,i)
        for neighbor in tqdm(neighbors):
                print("entered into max")
                if max1==self.label_countarr[neighbor]:
                    k=neighbor
                    print(neighbor)
                    #print( max1)
                    break
        return max1,k            
    
    def make_a_pick(self, i, neighbors):
        """
        Choosing a neighbor from a propagation source node.
        :param source: Source node.
        :param neigbors: Neighboring nodes.
        """
        
        max1=0 
        max2=0
        print("entered into pick")
        #max1,k=self.equality(i,neighbors)
        scores = {}
        neighbors=nx.neighbors(self.graph,i)        
        for neighbor in tqdm(neighbors): 
                if max2<self.label_countarr[neighbor]:
                        max2=self.label_countarr[neighbor]
        #print(max1)
        max2,k=self.equality(i,neighbors,max2)
        scores[self.labels[k]] = self.li[k]
        neighbors=nx.neighbors(self.graph,i)
        for neighbor in tqdm(neighbors):
            neighbor_label = self.labels[neighbor]
            if k!=neighbor:
                    if self.label_countarr[neighbor]==max2:
                        if self.labels[k]==self.labels[neighbor]:
                               scores[self.labels[k]] = scores[self.labels[k]] + self.li[neighbor]
                        else  :
                               if neighbor_label in scores.keys():
                                        scores[neighbor_label] = scores[neighbor_label] + self.li[neighbor]
                               else:
                                        scores[neighbor_label] = self.li[neighbor]                
            #else :
            #    return self.labels[k]
        top = [key for key, val in scores.items() if val == max(scores.values())]
        print(top)
        max1=top[0]
        print(max1)
        
        for m in top:
          if scores[m]>scores[max1] :
                 max1=m
       
           
        #neighbors=nx.neighbors(self.graph,i)
           
        #neighbors=nx.neighbors(self.graph,i) 
        #sum1=self.li[k]
        #for neighbor in tqdm(neighbors):
        #    neighbors=nx.neighbors(self.graph,i)
        #    sum1=sum1+(self.ni[neighbor]/self.degree[neighbor]) 
                            
        
        #            sum2=self.li[neighbor]
        #            neighbors = nx.neighbors(self.graph,i)
         #           for neighbor1 in tqdm(neighbors):               
          #              sum2=sum2+(self.ni[neighbor1]/self.degree[neighbor1]) 
          #          if  sum2> sum1 :
          #              k=neighbor1
                
       #print(max1)
        #print(self.labels[k])
        #self.li[i]=self.li[i]+(self.ni[k]/self.degree[k])
        #self.li[k]=self.li[k]+(self.ni[i]/self.degree[i])
        #print(k)   
        #print(self.li[k])
        #print(self.li[k])
        
        return max1

    def do_a_propagation(self):
        """
        Doing a propagation round.
        """
        alpha=1.0
        print(alpha)
        random.seed(self.seeding)
        #random.shuffle(self.nodes)
        print(self.y)
        #lst = [None]* len(self.nodes)
        print(len(self.nodes))
        i=0
        for node in tqdm(self.nodes):
            print(i)
            self.lst[node]=self.y.result[node-1]
            #print(lst[node])
            i=i+1
        print(i)
        print(self.lst)
         #degree calcuation
        for node in tqdm(self.nodes):        
            self.degree[node]=self.graph.degree[node]
            self.labels[node]=node
        #node influence calculation       
        #self.ni=[None]* len(self.nodes)
        ni=[None]* len(self.nodes)
        for node in tqdm(self.nodes):
            self.ni[node]=self.lst[node]
           # ni[node]=self.lst[node]
            neighbors = nx.neighbors(self.graph, node)
            for neighbor in tqdm(neighbors): 
                self.ni[node]=self.ni[node]+((alpha*self.lst[neighbor])/self.degree[neighbor])
                #ni[node]=ni[node]+self.lst[neighbor]
        for node in tqdm(self.nodes):
            ni[node-1]=self.ni[node]
        print(len(set(self.labels.values())))
        
        print(ni[0])
        
        #print(ni)
        sort_value = np.sort(ni)
        #print(sort_value[3489])
        #print(sort_value[3488])
        #print(sort_value[3487])
        sort_index = np.argsort(ni)
        #print(sort_index[3489])
        #print(sort_index[3488])
        #print(sort_index[3487])
        
       
        #label influence calculation   
        for node in tqdm(self.nodes):
            self.li[node]=(self.ni[node]/self.degree[node])
            print(self.li[node])
        #print(self.li[3489])
        #print(self.li[3488])    
        
         
                 
        for node in tqdm(self.nodes): 
            self.label_countarr[node]=1
                   
        
        #best label to update
        for i in reversed(sort_index):
            print(i)
            j=i+1
            print("first")
            neighbors = nx.neighbors(self.graph, j)
            print(self.li[j])
            pick = self.make_a_pick(j, neighbors)
            print(pick)
            self.labels[j] = pick
            print(self.labels[j])
            self.label_countarr[j]=self.label_countarr[j]+1
        current_label_count = len(set(self.labels.values())) 
        print(len(set(self.labels.values())))
        if self.label_count == current_label_count:
            self.flag = False
        else:
            self.label_count = current_label_count    
            
       

    def do_a_series_of_propagations(self):
        """
        Doing propagations until convergence or reaching time budget.
        """
        start = time.time()
        index = 0
        while index < self.rounds and self.flag:
            index = index + 1
            print("\nLabel propagation round: " + str(index)+".\n")
            self.do_a_propagation()
            
        with open ('./data/lpani.txt','w') as f:
            for i in self.nodes:
                f.write(str(self.labels[i])+'\t')
                f.write(str(i)+'\t')
                f.write('\n')    
        print("")
        for node in tqdm(self.nodes): 
            print(self.labels[node])
        print("Modularity is: " + str(round(modularity( self.labels,self.graph), 40)) + ".\n")
        print(index)
        end = time.time()
        print(end - start)
        json_dumper(self.labels, self.args.assignment_output)
