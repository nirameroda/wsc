This REPOSITORY contains the information network analysis.
In assignment-1 
=================
following  properties of the graph is analyzed:
1. Degree distribution
2. Diameter
3. Geodesic path length
4. Clustering coefficient & average clustering coefficient
5. Strongly connected components
6. SCC their properties
7. Sparseness
8. 1-connectedness to k-connectedness; what is k for your graph?

In PART-2 the folowing models are used to analyze the properties which are not explained in above part

1.Erdos Renyi Model
2.Watts-Strogatz Model
3.Barabasi Albert Model


Download the dataset from here 
https://snap.stanford.edu/data/

In assignment2
===============
Using an open source crawler package (e.g. Crawler4J, Mercator...), design a site-specific crawler for any large domain of your choice. Give particular attention to the following and justify your choice with supporting evidence.
- Sequential crawling vs. Multithreaded crawling (observe crawling performance - no.of threads v/s time)
- Type of crawling strategy used (BFS v/s DFS v/s hybrid)
- Data structure used for indexing (optimal for searching, insertion... )

=========================
Process:

Input:  Starting URL, list of words, max number of pages to download.

Try each one of the below variants, while designing crawling strategies.
a. Crawl only from pages whose body text includes one of the words in the list.
b. Crawl only from pages whose title includes one of the words in the list.
c. Give priority to page with most words from list (either most different words or most occurrences of words)

In assignment3
===============
PART-1.
=======
For the different sized networks that you used for Assignment 1, implement the normalized metrics used to measure centrality of nodes - Degree centrality, Closeness centrality, Betweenness centrality and Eigenvector centrality.  Discuss your observations w.r.t the computed value of the metrics on the perceived importance of nodes in the network and submit a detailed report.

 

 

PART-2
=========
To implement   (i) HITS algorithm   (ii)  PageRank algorithm
1.Calculate and compare PageRank and HITS scores for the medium-scale networks (number of nodes in tens of thousands) that you used are:-
(i)p2p-Gnutella09.txt
(ii)email-Eu-core.txt
(iii)CA-GrQc.txt
2. Which of the Webpages (assuming the nodes in the dataset to be Webpages) have the highest and lowest PageRank and Hubs-Authorities score? Correlate your observations with reference to the experiments performed in Assignment 1 (w.r.t various network properties) and write a detailed analysis of your observations, along with plots of the rank/score distribution.
