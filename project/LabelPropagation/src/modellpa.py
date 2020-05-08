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
            
           
    
    def make_a_pick(self, i, neighbors):
        """
        Choosing a neighbor from a propagation source node.
        :param source: Source node.
        :param neigbors: Neighboring nodes.
        """
        
        #max1=0 
        #max2=0
        print("entered into pick")
        #max1,k=self.equality(i,neighbors)
        scores = {}
        
        for neighbor in neighbors:
            neighbor_label = self.labels[neighbor]
            if neighbor_label in scores.keys():
                scores[neighbor_label] = scores[neighbor_label] + self.label_countarr[neighbor]
            else:
                scores[neighbor_label] = self.label_countarr[neighbor]
        top = [key for key, val in scores.items() if val == max(scores.values())]
        return random.sample(top, 1)[0]
       
           
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
        
        

    def do_a_propagation(self):
       
        for node in tqdm(self.nodes): 
            self.label_countarr[node]=1
                       
            
            #best label to update
        for node in tqdm(self.nodes):
                print("first")
                neighbors = nx.neighbors(self.graph,node)
                pick = self.make_a_pick(node, neighbors)
                print(pick)
                self.labels[node] = pick
                print(self.labels[node])
                self.label_countarr[node]=self.label_countarr[node]+1
        current_label_count = len(set(self.labels.values()))    
        if self.label_count == current_label_count:
            self.flag = False
        else:
             self.label_count = current_label_count    
            
        

    def do_a_series_of_propagations(self):
        """
        Doing propagations until convergence or reaching time budget.
        """
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
        json_dumper(self.labels, self.args.assignment_output)
