#include <iostream>
#include <vector>
#include <algorithm>

const int N = 2e5+5;
int n, m;
std::vector <std::pair<int, int>> g[N];
std::vector <int> col[N];
int us[N];
int colors;
int answer = 1e9+1;

void Dfs(int u) {
  us[u] = 1;
  col[colors].emplace_back(u);
  for (auto [v, w]: g[u]) {
    if (!us[v]) {
      Dfs(v);
    }
  }
}

struct DSU {
  int p[N];
  int h[N];
  void Init(int size) {
    for (int i = 1; i <= size; ++i) {
      p[i] = i;
      h[i] = 1;
    }
  }
  int Parent(int u) {
    if (p[u] == u) {
      return u;
    }
    return p[u] = Parent(p[u]);
  }
  bool Merged(int u, int v) {
    return Parent(u) == Parent(v);
  }
  void Join(int u, int v) {
    u = Parent(u);
    v = Parent(v);
    if (u == v) {
      return;
    }
    if (h[u] < h[v]) {
      std::swap(u, v);
    }
    h[u] += h[v];
    p[v] = u;
  }
};


void Solve(int color) {
  std::vector <std::pair<int, std::pair<int, int>>> cur_edges;
  for (auto u: col[color]) {
    for (auto [v, w]: g[u]) {
      if (v < u) {
        continue;
      }
      cur_edges.push_back({w, {u, v}});
    }
  }
  sort(cur_edges.begin(), cur_edges.end());
  reverse(cur_edges.begin(), cur_edges.end());
  DSU dsu;
  dsu.Init(col[color].size());
  for (auto [w, edge]: cur_edges) {
    int u = edge.first;
    int v = edge.second;
    if (dsu.Merged(u, v)) {
      continue;
    }
    dsu.Join(u, v);
    answer = std::min(answer, w);
  }

}

int main() {
  std::cin >> n >> m;
  for (int i = 1; i <= m; ++i) {
    int u, v, w;
    std::cin >> u >> v >> w;
    g[u].emplace_back(v, w);
    g[v].emplace_back(u, w);
  }
  for (int i = 1; i <= n; ++i) {
    if (!us[i]) {
      ++colors;
      Dfs(i);
    }
  }
  for (int color = 1; color <= colors; ++color) {
    Solve(color);
  }
  std::cout << answer - 1;
}