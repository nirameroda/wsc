This REPOSITORY contains the information network analysis.
In part-1 following  properties of the graph is analyzed
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
