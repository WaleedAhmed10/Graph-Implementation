#pragma once
#include <iostream>
#include <vector>
#include <queue>
#define INF 1e9
using namespace std;

class Graph
{
    int V;
    vector<vector<int>> adj;

public:
    Graph(int v);
    void addEdge(int u, int v);
    void BFS(int start);
    void DFS(int start);

private:
    void DFSUtil(int v, vector<bool>& visited);
};

class Dijkstra
{
    int V;
    vector<vector<pair<int, int>>> adj;

public:
    Dijkstra(int v);
    void addEdge(int u, int v, int w);
    void shortestPath(int src);
};