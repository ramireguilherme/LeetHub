#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <tuple>

using namespace std;

class DisjointSet {
public:
    DisjointSet(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    int find(int u) {
        if (parent[u] != u) {
            parent[u] = find(parent[u]);
        }
        return parent[u];
    }

    void union_sets(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u != root_v) {
            if (rank[root_u] > rank[root_v]) {
                parent[root_v] = root_u;
            } else if (rank[root_u] < rank[root_v]) {
                parent[root_u] = root_v;
            } else {
                parent[root_v] = root_u;
                rank[root_u]++;
            }
        }
    }

private:
    vector<int> parent;
    vector<int> rank;
};

int kruskal_minmax_path(int n, vector<tuple<int, int, int>>& edges, int source, int target) {
    sort(edges.begin(), edges.end(), [](const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
        return get<2>(a) < get<2>(b);
    });

    DisjointSet ds(n);
    vector<tuple<int, int, int>> mst;

    for (size_t i = 0; i < edges.size(); ++i) {
        int u, v, weight;
        tie(u, v, weight) = edges[i];
        if (ds.find(u) != ds.find(v)) {
            ds.union_sets(u, v);
            mst.push_back(edges[i]);
            if (ds.find(source) == ds.find(target)) {
                break;
            }
        }
    }

    vector<vector<pair<int, int>>> adj_list(n);
    for (size_t i = 0; i < mst.size(); ++i) {
        int u, v, weight;
        tie(u, v, weight) = mst[i];
        adj_list[u].emplace_back(v, weight);
        adj_list[v].emplace_back(u, weight);
    }

    function<int(int, int, vector<char>&)> dfs = [&](int node, int target, vector<char>& visited) -> int {
        if (node == target) {
            return 0;
        }
        visited[node] = true;
        for (const auto& edge : adj_list[node]) {
            int neighbor = edge.first;
            int weight = edge.second;
            if (!visited[neighbor]) {
                int result = dfs(neighbor, target, visited);
                if (result != -1) {
                    return max(weight, result);
                }
            }
        }
        return -1;
    };

    vector<char> visited(n, false);
    return dfs(source, target, visited);
}

int main() {
    int test = 1;
    int vertices, edges, queries;
    cin >> vertices >> edges >> queries;
    while (vertices != 0 && edges != 0 && queries != 0) {
        vector<tuple<int, int, int>> edges_list;
        for (int i = 0; i < edges; ++i) {
            int u, v, w;
            cin >> u >> v >> w;
            edges_list.emplace_back(u, v, w);
        }
        cout << "Case #" << test << endl;
        test++;
        for (int i = 0; i < queries; ++i) {
            int source, target;
            cin >> source >> target;
            int value = kruskal_minmax_path(vertices + 1, edges_list, source, target);
            if (value != -1) {
                cout << value << endl;
            } else {
                cout << "no path" << endl;
            }
        }
        cin >> vertices >> edges >> queries;
        if (vertices != 0 && edges != 0 && queries != 0)
            cout<<  "\n";
    }
    return 0;
}
