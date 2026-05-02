#pragma once
#define MAXVERTEXS 5
#define TRUE 1
#define FALSE 0
#include <iostream>
using namespace std;

struct Edge
{
    int adj;
    int weight;
};

class WeightedGraph
{
private:
    Edge graph[MAXVERTEXS][MAXVERTEXS];

public:
    WeightedGraph();
    void join(int vertex1, int vertex2, int wt);
    void remove(int vertex1, int vertex2);
    bool adjacent(int vertex1, int vertex2) const;
    void display() const;
};