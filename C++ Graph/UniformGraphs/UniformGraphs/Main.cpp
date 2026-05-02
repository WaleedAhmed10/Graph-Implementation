#include "Graph.h"
using namespace std;

int main()
{
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    cout << "BFS from node 0:\n";
    g.BFS(0);
    cout << "\nDFS from node 0:\n";
    g.DFS(0);

    Dijkstra d(6);
    d.addEdge(0, 1, 4);
    d.addEdge(0, 2, 1);
    d.addEdge(2, 1, 2);
    d.addEdge(1, 3, 1);
    d.addEdge(2, 3, 5);
    d.addEdge(3, 4, 3);
    d.addEdge(4, 5, 1);
    cout << "\nDijkstra from node 0:\n";
    d.shortestPath(0);
    return 0;
}