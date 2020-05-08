"""Tools for data reading and writing."""

import json
import pandas as pd
import networkx as nx
from texttable import Texttable

def argument_printer(args):
    """
    Function to print the arguments in a nice tabular format.
    :param args: Parameters used for the model.
    """
    args = vars(args)
    keys = sorted(args.keys())
    t = Texttable() 
    t.add_rows([["Parameter", "Value"]])
    t.add_rows([[k.replace("_", " ").capitalize(), args[k]] for k in keys])
    print(t.draw())

def graph_reader(input_path):
    """
    Function to read graph from input path.
    :param input_path: Graph read into memory.
    :return graph: Networkx graph.
    """
    edges = pd.read_csv(input_path)
    graph = nx.from_edgelist(edges.values.tolist())
    
    return graph
def content_reader(input_path):
    """
    Function to read graph from input path.
    :param input_path: Graph read into memory.
    :return graph: Networkx graph.
    """
    
    data = pd.read_csv('./data/zachimp.csv')
   # print(data.iloc[:-1])
    x= data.iloc[:,-1:]
    #data['result'].values
    print(x)
    
    return x
def value_kshell(input_path):
    """
    Function to read graph from input path.
    :param input_path: Graph read into memory.
    :return graph: Networkx graph.
    """
    
    data = pd.read_csv('./data/zachkshell.csv')
   # print(data.iloc[:-1])
    z= data.iloc[:,-1:]
    #data['result'].values
    print(z)
    
    
    return z
def json_dumper(data, path):
    """
    Function to save a JSON to disk.
    :param data: Dictionary of cluster memberships.
    :param path: Path for dumping the JSON.
    """
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
