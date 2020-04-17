#include "network.h"
#include "node.h"
#include "bits/stdc++.h"
vector<pair<float,int>>p;
float Q;
int x;
Network::Network()
{
    numberOfNodes = 0;
}

bool Network::initialize(string inputPath)
{
    try
    {

        QFile inputFile(QString::fromStdString(inputPath));

        if (!inputFile.open(QFile::ReadOnly)) // try to open the file
            return false;
        cout<<55;



        // first loop to get the number of nodes
        while (!inputFile.atEnd()) // read until EOF
        {
            QString line = inputFile.readLine(); // read line by line
            line = line.replace('\n', "\0"); // remove the endl

            QStringList list = line.split('\t'); // get two nodes

            int v1 = list.at(0).toInt(),
                    v2 = list.at(1).toInt();

            int value = (v2 > v1 ? v2 : v1);

            if (value > numberOfNodes)
                numberOfNodes = value;
        }


        // now get the edges
        inputFile.seek(0); // put the cursor at the beginning of the file

        x=numberOfNodes;
        // node labels start from zero so we should initializr from 1 to n
        edges = new SparseMatrix<int>(numberOfNodes);

        nodes = new Node[numberOfNodes + 1];
        for (int i = 1; i <= numberOfNodes; ++i)
            nodes[i].label = i;
        for (int i = 1; i <= numberOfNodes; ++i)
                {
                    nodes[i].degree=0;

                    nodes[i].kShell = 0;
                    nodes[i].labelInfluence = 0.0f;
                    nodes[i].nodeInfluence=0.0f;
                    nodes[i].newLabel = 0;
                    nodes[i].maxLi=0.0f;
                    nodes[i].cal=1;
                }


        // second loop to get the edges
        while (!inputFile.atEnd()) // get number of nodes
        {
            QString line = inputFile.readLine();
            line = line.replace('\n', "\0");


            QStringList list = line.split('\t');


            int v1 = list.at(0).toInt(),
                    v2 = list.at(1).toInt();


            // indirected graph; having edge in both direction
            edges->set(v1, v2, 1);
            edges->set(v2, v1, 1);

            // add the corresponding degree
            nodes[v1].degree++;
            nodes[v2].degree++;

        }



        // close the reading file
        inputFile.close();
    }
    catch(exception e)
    {
        cerr << e.what() << endl;
    }


}

bool Network::computeKShell()
{
    // to edit the degree
    Node copyNode[numberOfNodes + 1];
    for (int i = 1; i <= numberOfNodes; ++i)
        copyNode[i] = nodes[i];



    /* to edit (remove) the edges as a process
     * of computing the k-shell decomposition
     */
    SparseMatrix<int> copyEdges(*edges);



    int currentK = 1;

    bool endLoop;




    do
    {
        endLoop = true;

        bool goToNextK = true;


        for (int cntr = 1; cntr <= numberOfNodes; ++cntr)
        {


            // calculate this function ONCE
            if (copyNode[cntr].degree != 0)
                endLoop = false;
            else // skip nodes with zero degree
                continue;


            if (copyNode[cntr].degree == currentK)
            {
                int column;
                if (copyEdges.removeAnyEdge(cntr, column))
                {
                    copyNode[cntr].degree--;
                    copyNode[cntr].kShell++;

                    goToNextK = false;
                }

                // remove the correspondent indirected edge as well
                if (copyEdges.removeEdge(column, cntr))
                {
                    copyNode[column].degree--;
                    copyNode[column].kShell++;

                }
            }
        }


        if (goToNextK)
            currentK++;


    }while (!endLoop && currentK <= numberOfNodes);


    // add the nodes with zero k-shell to the minimum shell
    int minKShell = copyNode[1].kShell;
    for (int i = 2; i <= numberOfNodes; ++i) // compute the minimum
        if (minKShell > copyNode[i].kShell)
            minKShell = copyNode[i].kShell;

    for (int i = 1; i <= numberOfNodes; ++i) // assign the minimum
        if (copyNode[i].kShell == 0)
            copyNode[i].kShell = minKShell;


    for (int i = 1; i <= numberOfNodes; ++i) // assign the copy back to origin
        nodes[i].kShell = copyNode[i].kShell;




    return true;
}

bool Network::computeNodeInfluence()
{
    srand(QTime::currentTime().second());
     float alpha;
    cin>>alpha;
    for (int i = 1; i <= numberOfNodes; ++i)
    {
        cout<<5;
        nodes[i].nodeInfluence = nodes[i].kShell; // NI(i) = Ks(i) + ...
        nodes[i].newLabel=nodes[i].label;
    }
        float tmpSum = 0;
        for (int i = 1; i <= numberOfNodes; ++i)
           {

               for (int j = 1; j <= numberOfNodes; ++j)
               {
                  if(edges->get(i,j)!=0) tmpSum += (float) (nodes[j].kShell / nodes[j].degree);
               }
               // tmpSum *= alpha;

               nodes[i].nodeInfluence += (float)(alpha*tmpSum);

           }
       // for (int i = 1; i <= numberOfNodes; ++i)tmpSum += (float) (nodes[i].kShell / nodes[i].degree);
       // tmpSum *= alpha;

        //nodes[i].nodeInfluence += tmpSum;


    cout<<10;
    for(int i = 1; i <=100; ++i)
        {
            cout<<"\t"<<nodes[i].nodeInfluence;
        }

    for(int j = 1; j<=numberOfNodes; ++j)
        {
        // a[j]=nodes[j+1].nodeInfluence;
        p.push_back(make_pair(nodes[j].nodeInfluence,j));
        }


     sort(p.begin(),p.end());
        for(int j = 0; j<=numberOfNodes-1; ++j)
        {
          cout<<"\n"<<p[j].first;
          cout<<"\t"<<p[j].second;
        }
    //    cout<<"\n";




    return true;
}

bool Network::computeLabelInfluence()
{
    for (int i = 1; i <= numberOfNodes; ++i)
        {

                nodes[i].labelInfluence=(nodes[i].nodeInfluence/nodes[i].degree);

        }

        for(int i = 1; i <= 3; ++i)
        {
        cout<<"\t"<<nodes[i].labelInfluence;
        }
        return true;


}
void Network::computeLabelInfluence2()
{
    for (int i = 1; i <= numberOfNodes; ++i)
    {
        for(int j = 1; j <= numberOfNodes; ++j)
        {
            if(nodes[i].newLabel==nodes[j].newLabel)
             {
            nodes[i].labelInfluence+=(nodes[j].nodeInfluence/nodes[j].degree);
             }
         }
    }

    for(int i = 1; i <= 3; ++i)
    {
    cout<<"\t"<<nodes[i].labelInfluence;
    }

}


bool Network::computeNewLabels()
{
    int i=numberOfNodes-1;
        while(i>=0)
        {
            int j, indexMaxLi;
            for (j = 1; j <= numberOfNodes; ++j)
            {
                if (edges->get(p[i].second, j) != 0)
                {
                    nodes[p[i].second].maxLi = nodes[j].labelInfluence;
                    indexMaxLi = j;

                    break;
                }
                cout<<"\t"<<10;
            }

            for (; j <= numberOfNodes; ++j)
            {
                if (edges->get(p[i].second, j) != 0)
                {
                   if(nodes[indexMaxLi].cal<nodes[j].cal)
                   {
                       indexMaxLi = j;
                   }
                   else if(nodes[indexMaxLi].cal==nodes[j].cal)
                   {
                    if (nodes[j].labelInfluence >nodes[indexMaxLi].labelInfluence)
                    {
                        nodes[p[i].second].maxLi= nodes[j].labelInfluence;
                        indexMaxLi = j;
                    }
                  }
                }

            }
            cout<<"\t"<<11;
            nodes[p[i].second].newLabel = indexMaxLi; // finish
               i--;
              computeLabelInfluence2();
        }
        for (int i = 1; i <= numberOfNodes; ++i)
        {
        cout<<"\t"<<nodes[i].newLabel;
        }
     // computing modularity
     int f=0;
        for (int i = 1; i <= numberOfNodes; ++i)
        {

            int j;
            for (j = 1; j <= numberOfNodes; ++j)
            {
               f=10;
                  //cout<<"\t"<<edges->get(i,j);
                  // cout<<(nodes[i].newLabel==nodes[j].newLabel)<<"\t";
                  Q+=(float)(edges->get(i, j)-((nodes[i].degree)*(nodes[j].degree)/(2*x)))*((nodes[i].newLabel==nodes[j].newLabel)?1:0);

            }
        }
      //cout<<f;
     Q=Q/(2*x);
     cout<<"\n"<<Q;

        return true;

}

bool Network::writeResultsToFile(string resultPath)
{
    fstream output;
    try
    {
        output.open(resultPath, ios::app);
        for (int i = 1; i <= numberOfNodes; i++)
            output << i << "\t" << nodes[i].newLabel << endl;
        output.flush();
        output.close();
        return true;
    }
    catch (exception ex)
    {
        cerr << ex.what() << endl;
    }

}
