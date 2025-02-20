#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <iomanip>

using namespace std;

class UnionFind {
public:
    UnionFind(int n) : parent(n), rank(n, 0) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int u) {
        if (parent[u] != u) {
            parent[u] = find(parent[u]);
        }
        return parent[u];
    }

    void unionSet(int u, int v) {
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

double calculate_distance(pair<double, double> point1, pair<double, double> point2) {
    return sqrt(pow(point1.first - point2.first, 2) + pow(point1.second - point2.second, 2));
}

vector<tuple<int, int, double>> kruskal_mst(vector<pair<double, double>> points) {
    vector<tuple<double, int, int>> edges;
    int n = points.size();

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            double distance = calculate_distance(points[i], points[j]);
            edges.push_back(make_tuple(distance, i, j));
        }
    }

    sort(edges.begin(), edges.end());

    UnionFind uf(n);
    vector<tuple<int, int, double>> mst;

    for (auto &[distance, u, v] : edges) {
        if (uf.find(u) != uf.find(v)) {
            uf.unionSet(u, v);
            mst.push_back(make_tuple(u, v, distance));
        }
    }

    return mst;
}

int main() {
    int tests;
    cin >> tests;
    for (int t = 0; t < tests; ++t) {
        int vertices;
        cin >> vertices;
        vector<pair<double, double>> points(vertices);
        for (auto &point : points) {
            cin >> point.first >> point.second;
        }
        auto mst = kruskal_mst(points);
        double total_distance = 0;
        for (auto &[u, v, distance] : mst) {
            total_distance += distance;
        }
        cout << fixed << setprecision(3) << total_distance << endl;
    }
    return 0;
}