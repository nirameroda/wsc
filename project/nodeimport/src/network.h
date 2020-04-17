#ifndef NETWORK_H
#define NETWORK_H

#include<iostream>
#include<QFile>
#include<iomanip>
#include<QTime>
#include"node.h"
#include<fstream>
class Node; // forward declaration


/* reference of the library:
 * https://github.com/meysam81/Sparse-Matrix
 */
#include "F:\2ndsem\wscproject\Sparse-Matrix-master\src\SparseMatrix\SparseMatrix.cpp"

using namespace std;

class Network
{
private:
    Node* nodes;
    int numberOfNodes;
    int x;
    float Q;


    SparseMatrix<int> *edges;
public:
    Network();
    bool initialize(string inputPath);

    bool computeNodeInfluence();

    bool computeLabelInfluence();

    bool computeNewLabels();

    bool writeResultsToFile(string resultPath);

    void computeLabelInfluence2();

};


#endif // NETWORK_H
