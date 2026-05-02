#include <iostream>
#include "Graph.h"
using namespace std;

int main()
{
    WeightedGraph g;

    g.join(0, 1, 7);
    g.join(0, 2, 4);
    g.join(1, 3, 5);
    g.join(2, 3, 6);
    g.join(3, 4, 3);

    cout << "Edge from 0 to 1? " << (g.adjacent(0, 1) ? "Yes" : "No") << "\n";
    cout << "Edge from 1 to 4? " << (g.adjacent(1, 4) ? "Yes" : "No") << "\n";

    g.display();
    g.remove(2, 3);
    cout << "\nAfter removing edge 2->3:\n";
    g.display();
    return 0;
}