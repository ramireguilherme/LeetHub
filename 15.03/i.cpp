#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
#include <sstream>

class Graph {
private:
    std::unordered_map<char, std::vector<char>> adj_list;
    std::unordered_set<char> visited;

public:
    Graph() {}

    void add_edge(char u, char v) {
        if (adj_list.find(u) == adj_list.end()) {
            adj_list[u] = std::vector<char>();
        }
        if (adj_list.find(v) == adj_list.end()) {
            adj_list[v] = std::vector<char>();
        }
        adj_list[u].push_back(v);
        adj_list[v].push_back(u);
    }

    std::string to_string() {
        std::string output;
        for (const auto& pair : adj_list) {
            output += pair.first + std::string(": ");
            for (const auto& neighbor : pair.second) {
                output += neighbor + std::string(", ");
            }
            output.pop_back(); // Remove trailing comma
            output.pop_back(); // Remove trailing space
            output += "\n";
        }
        return output;
    }

    void dfs(char start) {
        visited.insert(start);
        for (const auto& neighbor : adj_list[start]) {
            if (visited.find(neighbor) == visited.end()) {
                dfs(neighbor);
            }
        }
    }

    const std::unordered_set<char>& get_visited() const {
        return visited;
    }

    const std::unordered_map<char, std::vector<char>>& get_adj_list() const {
        return adj_list;
    }
};

int main() {
    int tests;
    std::cin >> tests;
    std::cin.ignore(); // to ignore the newline character after the number of tests

    for (int t = 0; t < tests; ++t) {
        Graph g;

        while (true) {
            std::string line;
            std::getline(std::cin, line);
            if (line.find('*') != std::string::npos) {
                break;
            }
            char u = line[1];
            char v = line[3];
            g.add_edge(u, v);
        }

        std::string vertices_line;
        std::getline(std::cin, vertices_line);
        std::istringstream vertices_stream(vertices_line);
        std::string vertex;
        int trees = 0, acorns = 0;

        while (std::getline(vertices_stream, vertex, ',')) {
            char v = vertex[0];
            if (g.get_adj_list().find(v) == g.get_adj_list().end()) {
                acorns++;
            } else if (g.get_visited().find(v) == g.get_visited().end()) {
                g.dfs(v);
                trees++;
            }
        }

        std::cout << "There are " << trees << " tree(s) and " << acorns << " acorn(s).\n";
    }

    return 0;
}
