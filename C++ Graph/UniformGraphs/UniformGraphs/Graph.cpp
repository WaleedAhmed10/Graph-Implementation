#include "Graph.h"
using namespace std;

Graph::Graph(int v) : V(v), adj(v) {}

void Graph::addEdge(int u, int v)
{
    adj[u].push_back(v);
}

void Graph::BFS(int start)
{
    vector<bool> visited(V, false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    while (!q.empty())
    {
        int v = q.front();
        q.pop();
        cout << v << " ";

        for (int u : adj[v])
        {
            if (!visited[u])
            {
                visited[u] = true;
                q.push(u);
            }
        }
    }
    cout << endl;
}

void Graph::DFSUtil(int v, vector<bool>& visited)
{
    visited[v] = true;
    cout << v << " ";

    for (int u : adj[v])
    {
        if (!visited[u])
        {
            DFSUtil(u, visited);
        }
    }
}

void Graph::DFS(int start)
{
    vector<bool> visited(V, false);
    DFSUtil(start, visited);
    cout << endl;
}

Dijkstra::Dijkstra(int v) : V(v), adj(v) {}

void Dijkstra::addEdge(int u, int v, int w)
{
    adj[u].emplace_back(v, w);
}

void Dijkstra::shortestPath(int src)
{
    vector<int> dist(V, INF);
    dist[src] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({ 0, src });

    while (!pq.empty())
    {
        int u = pq.top().second;
        pq.pop();

        for (auto& edge : adj[u])
        {
            int v = edge.first;
            int weight = edge.second;

            if (dist[v] > dist[u] + weight)
            {
                dist[v] = dist[u] + weight;
                pq.push({ dist[v], v });
            }
        }
    }

    for (int i = 0; i < V; ++i)
    {
        cout << "Distance to " << i << ": ";
        if (dist[i] == INF)
            cout << "INF" << endl;
        else
            cout << dist[i] << endl;
    }
}