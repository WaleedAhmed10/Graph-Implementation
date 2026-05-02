#include "Graph.h"
#include <iostream>
using namespace std;

WeightedGraph::WeightedGraph()
{
    for (int i = 0; i < MAXVERTEXS; ++i)
    {
        for (int j = 0; j < MAXVERTEXS; ++j)
        {
            graph[i][j].adj = FALSE;
            graph[i][j].weight = 0;
        }
    }
}

void WeightedGraph::join(int vertex1, int vertex2, int wt)
{
    graph[vertex1][vertex2].adj = TRUE;
    graph[vertex1][vertex2].weight = wt;
}

void WeightedGraph::remove(int vertex1, int vertex2)
{
    graph[vertex1][vertex2].adj = FALSE;
    graph[vertex1][vertex2].weight = 0;
}

bool WeightedGraph::adjacent(int vertex1, int vertex2) const
{
    return graph[vertex1][vertex2].adj == TRUE;
}

void WeightedGraph::display() const
{
    cout << "Adjacency Matrix with Weights:\n";
    for (int i = 0; i < MAXVERTEXS; ++i)
    {
        for (int j = 0; j < MAXVERTEXS; ++j)
        {
            if (graph[i][j].adj)
                cout << graph[i][j].weight << "\t";
            else
                cout << "0\t";
        }
        cout << "\n";
    }
}